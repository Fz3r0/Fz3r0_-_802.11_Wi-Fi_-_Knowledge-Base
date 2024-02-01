## CMD
- Obtener datos generales de Wi-Fi, incluyendo datarates
````bat
netsh wl sh in
````

## Powershell

- Obtener linkspeed de ethernet
````ps
 Get-NetAdapter | Where-Object { $_.Name -eq 'Ethernet' } | Select-Object Name, LinkSpeed
````
