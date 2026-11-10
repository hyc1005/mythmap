#requires -Version 5.1
[CmdletBinding()]
param(
  [ValidateSet('serve', 'copy')]
  [string]$Mode = 'serve',
  [int]$Port = 8080,
  [string]$Target = '',
  [switch]$Force,
  [switch]$Foreground,
  [switch]$Open
)

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Site = Join-Path $Root 'site'
$Sums = Join-Path $Root 'SHA256SUMS'
$Required = @(
  'site/index.html',
  'site/opening-film.html',
  'site/data/myth-world.json',
  'site/assets'
)

function Fail([string]$Message) {
  Write-Host "ERROR: $Message" -ForegroundColor Red
  exit 1
}

function Confirm-Step([string]$Message) {
  if ($Force) { return }
  $answer = Read-Host "$Message [y/N]"
  if ($answer -notmatch '^(y|yes)$') {
    Write-Host 'Cancelled.'
    exit 0
  }
}

Write-Host '== MythMap static deployment ==' -ForegroundColor Cyan
Write-Host "Package: $Root"
Write-Host "Mode:    $Mode"

# 1. Environment
if ($PSVersionTable.PSVersion.Major -lt 5) { Fail 'PowerShell 5.1 or newer is required.' }
$Python = $null
foreach ($candidate in @('python', 'python3', 'py')) {
  $command = Get-Command $candidate -ErrorAction SilentlyContinue
  if ($command) {
    try {
      $version = & $command.Source --version 2>&1
      if ($version -match 'Python 3\.') { $Python = $command.Source; break }
      if ($candidate -eq 'py') {
        $version = & $command.Source -3 --version 2>&1
        if ($version -match 'Python 3\.') { $Python = $command.Source; break }
      }
    } catch { }
  }
}
if (-not $Python) { Fail 'Python 3 is required to serve the package. Use copy mode or install Python 3.' }

# 2. File integrity
foreach ($relative in $Required) {
  if (-not (Test-Path -LiteralPath (Join-Path $Root $relative))) { Fail "Missing required path: $relative" }
}
if (-not (Test-Path -LiteralPath $Sums)) { Fail 'SHA256SUMS is missing.' }
$checked = 0
Get-Content -LiteralPath $Sums -Encoding UTF8 | ForEach-Object {
  if ($_ -notmatch '^([0-9a-f]{64})\s{2}(.+)$') { Fail "Malformed checksum line: $_" }
  $expected = $Matches[1]
  $relative = $Matches[2].Trim()
  $path = Join-Path $Root $relative
  if (-not (Test-Path -LiteralPath $path)) { Fail "Missing packaged file: $relative" }
  $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($actual -ne $expected) { Fail "Checksum mismatch: $relative" }
  $checked++
}
Write-Host "Integrity: $checked files match SHA256SUMS" -ForegroundColor Green

if ($Mode -eq 'copy' -and -not $Target) { Fail 'Copy mode needs -Target <directory>.' }
if ($Mode -eq 'serve') {
  if ($Port -lt 1 -or $Port -gt 65535) { Fail 'Port must be between 1 and 65535.' }
  $inUse = $false
  try {
    $client = [System.Net.Sockets.TcpClient]::new()
    $client.Connect('127.0.0.1', $Port)
    $inUse = $true
  } catch {
    $inUse = $false
  } finally {
    if ($client) { $client.Dispose() }
  }
  if ($inUse) { Fail "Port $Port is already in use." }
} else {
  $Target = [System.IO.Path]::GetFullPath($Target)
  if (-not (Test-Path -LiteralPath $Target)) {
    New-Item -ItemType Directory -Path $Target | Out-Null
  }
  if ((Get-ChildItem -LiteralPath $Target -Force | Measure-Object).Count -gt 0 -and -not $Force) {
    Fail 'Target directory is not empty. Re-run with -Force to overwrite.'
  }
  $probe = Join-Path $Target '.write-test'
  try { [System.IO.File]::WriteAllText($probe, 'ok'); Remove-Item -LiteralPath $probe -Force }
  catch { Fail "Target is not writable: $Target" }
  Write-Host "Target:  $Target"
}

# 3. Confirm
$sizeMb = [math]::Round(((Get-ChildItem -LiteralPath $Site -Recurse -File | Measure-Object Length -Sum).Sum / 1MB), 1)
Write-Host "Files:   $checked checks; site size $sizeMb MB"
Confirm-Step "Deploy the verified static site now?"

# 4. Serve or copy
if ($Mode -eq 'serve') {
  $url = "http://127.0.0.1:$Port/"
  if ($Foreground) {
    if ($Open) {
      Start-Process -FilePath 'powershell' -ArgumentList '-NoProfile', '-WindowStyle', 'Hidden', '-Command', "Start-Sleep -Milliseconds 900; Start-Process '$url'" | Out-Null
    }
    Write-Host "Serving $url  (Ctrl+C to stop)" -ForegroundColor Green
    & $Python -m http.server $Port --bind 127.0.0.1 --directory $Site
  } else {
    $arguments = "-m http.server $Port --bind 127.0.0.1 --directory `"$Site`""
    $process = Start-Process -FilePath $Python -ArgumentList $arguments -WorkingDirectory $Root -PassThru
    Start-Sleep -Seconds 1
    Write-Host "Serving $url (PID $($process.Id))" -ForegroundColor Green
    Write-Host 'Press Ctrl+C in the serving terminal or stop the Python process to finish.'
  }
} else {
  Copy-Item -Path (Join-Path $Site '*') -Destination $Target -Recurse -Force
  if (-not (Test-Path -LiteralPath (Join-Path $Target 'index.html'))) { Fail 'Copy finished but index.html is missing.' }
  Write-Host "Copied to $Target" -ForegroundColor Green
  Write-Host 'Point any static web server at this directory; no Node or API process is needed.'
}
