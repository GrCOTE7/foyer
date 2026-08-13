$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RootDir

$Port = if ($env:FOYER_PORT) { $env:FOYER_PORT } else { '8000' }
$HostName = if ($env:FOYER_HOST) { $env:FOYER_HOST } else { '127.0.0.1' }
$Url = "http://localhost:$Port"

try {
    python -c "import mkdocs; import mkdocs_open_in_new_tab" | Out-Null
}
catch {
    Write-Host "Installation des dépendances docs..."
    python -m pip install -r requirements-docs.txt
}

# MkDocs exige que docs_dir existe avant de charger la configuration.
New-Item -ItemType Directory -Path ".build/docs" -Force | Out-Null

Write-Host "Serveur local en cours de lancement..."
Write-Host "Ouvre $Url"
python -m mkdocs serve --dev-addr "$HostName`:$Port" --watch "README.md" --watch "Manifeste-Foyer.md" --watch "Methode-Foyer.md" --watch "Boucle-de-retroaction.md" --watch "Simulateur-Synthese.md" --watch "skills" --watch "personas" --watch "bmad" --watch "tools" --watch "notebooklm"
