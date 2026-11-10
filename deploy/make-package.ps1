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
$OutputDirectory = if ($OutputDirectory) { [System.IO.Path]::GetFullPath($OutputDirectory) } else { Join-Path $Root 'output\deploy' }
$Stage = Join-Path $OutputDirectory 'mythmap-static'
$Site = Join-Path $Stage 'site'
$Zip = Join-Path $OutputDirectory ("mythmap-static-{0}.zip" -f (Get-Date -Format 'yyyyMMdd'))

function Fail([string]$Message) { Write-Host "ERROR: $Message" -ForegroundColor Red; exit 1 }

New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
if (-not $SkipBuild) {
  if (Test-Path -LiteralPath $Stage) { Remove-Item -LiteralPath $Stage -Recurse -Force }
  New-Item -ItemType Directory -Path $Site -Force | Out-Null
  Push-Location $Frontend
  try {
    Write-Host 'Building static site with base "/"...'
    & npm run build -- --base / --outDir $Site --emptyOutDir
    if ($LASTEXITCODE -ne 0) { Fail 'Vite build failed.' }
  } finally { Pop-Location }
} elseif (-not (Test-Path -LiteralPath $Site)) {
  Fail "No staged site found at $Site; run without -SkipBuild."
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

$commit = try { (& git -C $Root rev-parse --short HEAD).Trim() } catch { 'unknown' }
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

if (Test-Path -LiteralPath $Zip) { Remove-Item -LiteralPath $Zip -Force }
Write-Host "Compressing $($files.Count) files..."
Compress-Archive -Path (Join-Path $Stage '*') -DestinationPath $Zip -CompressionLevel Optimal
Write-Host ("Package: {0} ({1:N1} MB)" -f $Zip, ((Get-Item -LiteralPath $Zip).Length / 1MB)) -ForegroundColor Green
Write-Host "Stage kept for inspection: $Stage"
