$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$classes = Join-Path $PSScriptRoot 'build/classes'
New-Item -ItemType Directory -Force -Path $classes | Out-Null
javac --add-modules jdk.httpserver -encoding UTF-8 -d $classes (Join-Path $PSScriptRoot 'src/main/java/org/shanhai/atlas/MythWorldServer.java')
java --add-modules jdk.httpserver -cp $classes org.shanhai.atlas.MythWorldServer (Join-Path $projectRoot 'frontend/public/data/myth-world.json')
