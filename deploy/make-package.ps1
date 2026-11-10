#requires -Version 5.1
[CmdletBinding()]
param(
  [string]$OutputDirectory = '',
  [switch]$SkipBuild
)

$ErrorActionPreference = 'Stop'
$DeployDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $DeployDir
$Frontend = Join-Path $Root 'frontend'
$commit = (& git -C $Root rev-parse --short=7 HEAD)
$stamp = Get-Date
$OutputDirectory = if ($OutputDirectory) { [System.IO.Path]::GetFullPath($OutputDirectory) } else { Join-Path $Root ("output\deploy\static-{0:yyyy-MM-dd}-{1}" -f $stamp, $commit) }
$Stage = Join-Path $OutputDirectory 'mythmap-static'
$Site = Join-Path $Stage 'site'
$Zip = Join-Path $OutputDirectory ("mythmap-static-{0:yyyyMMdd}-{1}.zip" -f $stamp, $commit)
$Partial = "$Zip.partial"

function Fail([string]$Message) { Write-Host "ERROR: $Message" -ForegroundColor Red; exit 1 }

if ($commit -notmatch '^[0-9a-f]{7,40}$') { Fail 'Could not identify the Git commit.' }
if ((Test-Path -LiteralPath $Zip) -or (Test-Path -LiteralPath $Partial)) {
  Fail 'An archive already exists. Choose a new -OutputDirectory.'
}
$Python = Get-Command python, python3, py -CommandType Application -ErrorAction SilentlyContinue |
  Where-Object { (& $_.Source --version 2>$null) -match '^Python 3\.' } | Select-Object -First 1
if (-not $Python) { Fail 'Python 3 is required to create the ZIP.' }

New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
if (-not $SkipBuild) {
  if (Test-Path -LiteralPath $Stage) { Fail 'A staging directory already exists. Choose a new -OutputDirectory.' }
  New-Item -ItemType Directory -Path $Stage | Out-Null
  New-Item -ItemType Directory -Path $Site | Out-Null
  Push-Location $Frontend
  try {
    Write-Host 'Building static site with base "/"...'
    & npm run build -- --base / --outDir $Site --emptyOutDir --logLevel warn
    if ($LASTEXITCODE -ne 0) { Fail 'Vite build failed.' }
  } finally { Pop-Location }
} elseif (-not (Test-Path -LiteralPath $Site)) {
  Fail "No staged site found at $Site; run without -SkipBuild."
} elseif (-not (Select-String -LiteralPath (Join-Path $Stage 'PACKAGE-INFO.txt') -Pattern "^commit: $commit$" -Quiet -ErrorAction SilentlyContinue)) {
  Fail 'The staged site must have package metadata matching the current Git commit.'
}

foreach ($relative in @('index.html', 'opening-film.html', 'data/myth-world.json', 'assets')) {
  if (-not (Test-Path -LiteralPath (Join-Path $Site $relative))) { Fail "Build output is missing: $relative" }
}

Get-ChildItem -LiteralPath $DeployDir -File | Where-Object { $_.Name -ne 'make-package.ps1' } | ForEach-Object {
  Copy-Item -LiteralPath $_.FullName -Destination $Stage -Force
}

$files = Get-ChildItem -LiteralPath $Site -Recurse -File | Sort-Object FullName
$lines = foreach ($file in $files) {
  $relative = 'site/' + $file.FullName.Substring($Site.Length).TrimStart('\', '/').Replace('\', '/')
  $hash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
  "$hash  $relative"
}
$utf8 = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText((Join-Path $Stage 'SHA256SUMS'), (($lines -join "`n") + "`n"), $utf8)

$totalBytes = ($files | Measure-Object Length -Sum).Sum
$info = @(
  'MythMap static deployment package',
  "built:  $(Get-Date -Format o)",
  "commit: $commit",
  'base:   /',
  "files:  $($files.Count)",
  "bytes:  $totalBytes"
) -join "`n"
[System.IO.File]::WriteAllText((Join-Path $Stage 'PACKAGE-INFO.txt'), $info + "`n", $utf8)

Write-Host "Compressing $($files.Count) files..."
$zipScript = @'
import shutil
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

stage = Path(sys.argv[1])
with ZipFile(sys.argv[2], "x", compression=ZIP_DEFLATED) as archive:
    for path in sorted(stage.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(stage)
        executable = len(relative.parts) == 1 and path.suffix in {".sh", ".command"}
        entry = ZipInfo.from_file(path, relative.as_posix())
        entry.create_system = 3
        entry.external_attr = (0o100755 if executable else 0o100644) << 16
        entry.compress_type = ZIP_DEFLATED
        with path.open("rb") as source, archive.open(entry, "w") as target:
            shutil.copyfileobj(source, target)
'@
$zipScript | & $Python.Source - $Stage $Partial
if ($LASTEXITCODE -ne 0) { Fail 'ZIP creation failed.' }
Move-Item -LiteralPath $Partial -Destination $Zip
Write-Host ("Package: {0} ({1:N1} MB)" -f $Zip, ((Get-Item -LiteralPath $Zip).Length / 1MB)) -ForegroundColor Green
Write-Host "Stage kept for inspection: $Stage"
