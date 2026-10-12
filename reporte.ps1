# reporte.ps1 - Reporte de servicios y procesos en CSV
$destino = "$HOME\automatizacion"
New-Item -ItemType Directory -Force -Path $destino | Out-Null

Get-Service | Select-Object Name, DisplayName, Status |
    Export-Csv "$destino\servicios.csv" -NoTypeInformation -Encoding UTF8

Get-Process | Sort-Object CPU -Descending |
    Select-Object -First 15 Name, Id, CPU, WorkingSet |
    Export-Csv "$destino\procesos.csv" -NoTypeInformation -Encoding UTF8

Write-Host "Reporte generado en $destino"
