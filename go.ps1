$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RootDir

$Port = if ($env:FOYER_PORT) { $env:FOYER_PORT } else { '8000' }
$HostName = if ($env:FOYER_HOST) { $env:FOYER_HOST } else { '127.0.0.1' }
$Url = "http://localhost:$Port"

try {
    py -c "import mkdocs" | Out-Null
}
catch {
    Write-Host "Installation des dependances docs..."
    py -m pip install -r requirements-docs.txt
}

Write-Host "Assemblage du contenu dans docs/..."
New-Item -ItemType Directory -Force docs | Out-Null
Copy-Item Manifeste-Foyer.md,Methode-Foyer.md,Boucle-de-retroaction.md,Simulateur-Synthese.md docs -Force
Copy-Item README.md docs/carte.md -Force
Copy-Item skills,personas,bmad,tools docs -Recurse -Force
Copy-Item notebooklm docs/notebooklm -Recurse -Force
py scripts/gen_supports.py
py scripts/gen_gates.py

Write-Host "Serveur local en cours de lancement..."
Write-Host "Ouvre $Url"
py -m mkdocs serve --dev-addr "$HostName`:$Port" --watch "README.md" --watch "Manifeste-Foyer.md" --watch "Methode-Foyer.md" --watch "Boucle-de-retroaction.md" --watch "Simulateur-Synthese.md" --watch "skills" --watch "personas" --watch "bmad" --watch "tools" --watch "notebooklm"
