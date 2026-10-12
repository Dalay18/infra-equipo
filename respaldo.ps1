# respaldo.ps1 - Comprime una carpeta con la fecha en el nombre
$origen  = "$HOME\automatizacion"
$destino = "$HOME\respaldos"
New-Item -ItemType Directory -Force -Path $destino | Out-Null

$fecha   = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$archivo = "$destino\respaldo_$fecha.zip"
$log     = "$destino\respaldo.log"

try {
    Compress-Archive -Path $origen -DestinationPath $archivo -ErrorAction Stop
    $mensaje = "Respaldo creado: $archivo"
}
catch {
    $mensaje = "ERROR al crear el respaldo: $_"
}

Add-Content $log "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $mensaje"
Write-Host $mensaje
