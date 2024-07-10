# Dirección IP y puerto SSH, modificar la IP a conveniencia, ejemplo una controladora en nube y ejecutar desde LAN

# IP de WLC que si tiene SSH abierto
$ip = "54.157.171.87"
# IP de google para verficiar el puerto cerrado, ya que este siempre estará cerrado
#$ip = "8.8.8.8"

$puertoSSH = 22

# Intenta conectarte al puerto SSH
try {
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    $tcpClient.Connect($ip, $puertoSSH)
    if ($tcpClient.Connected) {
        Write-Host "La conexión SSH a $ip en el puerto $puertoSSH está abierta."
    } else {
        Write-Host "La conexión SSH a $ip en el puerto $puertoSSH está cerrada o no disponible."
    }
} catch {
    Write-Host "La conexión SSH a $ip en el puerto $puertoSSH está cerrada o no disponible."
} finally {
    if ($tcpClient.Connected) {
        $tcpClient.Close()
    }
}
