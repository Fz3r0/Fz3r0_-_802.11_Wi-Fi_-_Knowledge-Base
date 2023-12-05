## Se puede copiar y pegar en powershell

# Dirección IP y puerto SSH, modificar la IP a conveniencia, ejemplo una controladora en nube y ekecutar desde LAN
$ip = "44.194.16.224"
$puertoSSH = 22

# Intenta conectarte al puerto SSH
try {
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    $tcpClient.Connect($ip, $puertoSSH)
    Write-Host "La conexión SSH a $ip en el puerto $puertoSSH está abierta."
} catch {
    Write-Host "La conexión SSH a $ip en el puerto $puertoSSH está cerrada o no disponible."
} finally {
    $tcpClient.Close()
}
