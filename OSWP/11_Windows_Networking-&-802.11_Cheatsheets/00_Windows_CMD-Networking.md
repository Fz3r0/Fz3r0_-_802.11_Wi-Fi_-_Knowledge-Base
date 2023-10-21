




##

````cmd
# Borrar la IP y lease 
ipconfig /release

# Reinicializar la IP (DHCP)
ipconfig /renew
````

````cmd
@echo off
echo Borrando la caché DNS...
ipconfig /flushdns
echo Caché DNS borrada con éxito.

echo Releasear la dirección
ipconfig /release
echo Dirección IP renovada con éxito.

echo Olvidando las redes WiFi conocidas...
netsh wlan delete profile name="Fz3r0::CWAP"
netsh wlan delete profile name="NombreDeRed2"
echo Redes WiFi olvidadas con éxito.

echo Proceso completado. Cierra esta ventana.
pause
````
