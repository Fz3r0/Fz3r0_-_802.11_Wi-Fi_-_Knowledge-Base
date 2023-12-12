<!-- 

Y ARRANCAN!!!
http://

<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Hacia el Infierno del `OSWP`: <br> `Offensive Security Wireless Professional` 📡🦈💀  

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/7c94fd0b-296e-4884-a604-c6db7c386ca6) <br>
_Writeup y bitácora para la certificación **CWAP-402** de **CWNP (Certified Wireless Network Professional)**_ <br>
_por @ **Fz3r0 💀** (CWNA)_

---

<br><br>

# 💀 Fz3r0 Cheatsheet: `Monitor Mode`

Scripts para configurar adaptadores Wi-Fi en `monitor mode` en kernels Linux basados en Debian.

## 🕵️📡 Monitor Mode Activation: `Basics`

````sh
# Monitor Mode: airmon
airmon-ng start wlan0

# Monitor Mode: iw
iw wlan0 set monitor control

# Monitor Mode: iwconfig
iwconfig wlan0 mode monitor

# Verificaciones:
clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev
````

## 🕵️📡 Monitor Mode Activation: `x1 Adapter`

````sh
# Activando Monitor Mode en un adaptador Fresh (wlan0) 
clear; airmon-ng start wlan0; iwconfig wlan0mon channel 6 && ifconfig wlan0mon down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0mon; ifconfig wlan0mon up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev

# Activando Monitor Mode en un adaptador ya en Monitor Mode (wlan0mon) 
clear; airmon-ng start wlan0mon; iwconfig wlan0mon channel 6 && ifconfig wlan0mon down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0mon; ifconfig wlan0mon up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev

# Activando Monitor Mode en un adaptador Fresh (wlan0) = TP-Link (o cualquier adaptador que siempre se llame wlan0) 
# Primero instalar driver: apt install -y realtek-rtl8188eus-dkms
clear; airmon-ng start wlan0; iwconfig wlan0 channel 6 && ifconfig wlan0 down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0; ifconfig wlan0 up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev
````

---

## 🕵️📡📡📡 Monitor Mode Activation: `x3 Adapters`

### Triple encendido con **diferentes** canales `1,6,11`

````sh
# Triple encendido de Adaptadores desde 0 (wlan0) 
# [Channels: 1, 6, 11]
clear;airmon-ng start wlan0; airmon-ng start wlan1; airmon-ng start wlan2 && iwconfig wlan0mon channel 1 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 11 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

# Triple encendido de Adaptadores ya en Monitor (wlan0mon)
# [Channels: 1, 6, 11]
clear;airmon-ng start wlan0mon; airmon-ng start wlan1mon; airmon-ng start wlan2mon && iwconfig wlan0mon channel 1 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 11 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````
### Triple encendido con **mismos** canales `6,6,6`

````sh
# Triple encendido de Adaptadores desde 0 (wlan0) 
# [Channels: 6, 6, 6]
clear;airmon-ng start wlan0; airmon-ng start wlan1; airmon-ng start wlan2 && iwconfig wlan0mon channel 6 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 6 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 6 | CHANNEL 6 | CHANNEL 6] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

# Triple encendido de Adaptadores ya en Monitor (wlan0mon)
# [Channels: 6, 6, 6]
clear;airmon-ng start wlan0mon; airmon-ng start wlan1mon; airmon-ng start wlan2mon && iwconfig wlan0mon channel 6 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 6 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 6 | CHANNEL 6 | CHANNEL 6] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````

## 📡🔛↩️ Apagar / Reiniciar Adaptador

````sh
# Detener la Interfaz 'wlan'
airmon-ng stop wlan0

# Reiniciar Servicio de Red :: Opcion 1:
service network-manager restart
# Reiniciar Servicio de Red :: Opcion 2:
/etc/init.d/networking restart

    ## Este es un reinicio completo de interfaz, así que vuelve el nombre de wlan0mon a > wlan0

# x1 Adapter Restart
airmon-ng stop wlan0mon && /etc/init.d/networking restart; iwconfig

# x3 Adapter Restart
airmon-ng stop wlan0mon;airmon-ng stop wlan1mon;airmon-ng stop wlan2mon && /etc/init.d/networking restart; iwconfig
````

## 📡🔛↩️ Apagar / Reiniciar Adaptador: `FULL`

````sh
# x1 Adapter Restart
airmon-ng stop wlan0mon && /etc/init.d/networking restart; clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev

# x3 Adapter Restart
airmon-ng stop wlan0mon;airmon-ng stop wlan1mon;airmon-ng stop wlan2mon && /etc/init.d/networking restart; clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev
````

## 🖥️📝❌ Network Services: Check & Kill

````sh
# Opcional para kill
airmon-ng check kill

# Opcional para tener internet
systemctl stop NetworkManager.service

# Opcional para detener wpa_suplicant
systemctl stop wpa_suplicant.service

# Opcional para detener Network manager
systemctl start NetworkManager.service

````

## 🕹️🕵️📡 Monitor Mode Activation: `x1 Adapter` :: `Bash Script`

````sh
#!/bin/bash


# Limpia la pantalla
clear

# Inicia el modo monitor en la interfaz WLAN0
airmon-ng start wlan0

# Configura la interfaz WLAN0 en el canal 6
iwconfig wlan0mon channel 6

# Desactiva la interfaz WLAN0MON
ifconfig wlan0mon down

# Cambia la dirección MAC de la interfaz WLAN0MON a "f0:f0:f0:f0:f0:f0"
macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0mon

# Activa la interfaz WLAN0MON
ifconfig wlan0mon up

# Limpia la pantalla nuevamente
clear

# Fz3r0 Info
echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"
echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"
echo ""

# Imprime información del sistema
echo -e "\033[97m--- SYSTEM:\033[0m"
echo ""
echo -e "\033[32m$(uname -a)\033[0m"
echo ""

# Imprime información de adaptadores USB y controladores
echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"
echo ""

# Comprueba si la interfaz WLAN0MON está en modo monitor y muestra el estado
if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then
    printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"
elif iwconfig 2>/dev/null | grep -q 'no wireless'; then
    echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"
else
    echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"
fi
echo ""

# Imprime información de airmon-ng
echo -e "\033[32m$(airmon-ng)\033[0m"
echo ""

# Imprime información de las interfaces físicas
echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"
echo ""
echo -e "\033[36m$(ifconfig)\033[0m"
echo ""

# Imprime información de adaptadores inalámbricos y su modo
echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"
echo ""
iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'

````

## 🕹️🕵️📡 Monitor Mode Activation: `FZ3R0 COCONUT 14-ch` :: `Bash Script`

````sh
#!/bin/bash

# Limpia la pantalla
clear

# Muestra letrero de esperar
# Fz3r0 Info
echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"
echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"
echo ""

# Imprime información del sistema
echo -e "Wait a moment, this shit is working..."


# Inicia el modo monitor en 14 Adaptadores (quitar "#")
airmon-ng start wlan0 2>/dev/null
airmon-ng start wlan1 2>/dev/null
airmon-ng start wlan2 2>/dev/null
airmon-ng start wlan3 2>/dev/null
airmon-ng start wlan4 2>/dev/null
airmon-ng start wlan5 2>/dev/null
airmon-ng start wlan6 2>/dev/null
airmon-ng start wlan7 2>/dev/null
airmon-ng start wlan8 2>/dev/null
airmon-ng start wlan9 2>/dev/null
airmon-ng start wlan10 2>/dev/null
airmon-ng start wlan11 2>/dev/null
airmon-ng start wlan12 2>/dev/null
airmon-ng start wlan13 2>/dev/null
airmon-ng start wlan14 2>/dev/null

# Configura la adaptadores del canal 1 al 14 (Todos en 2.4 GHz)
iwconfig wlan0mon channel 1 2>/dev/null
iwconfig wlan1mon channel 2 2>/dev/null
iwconfig wlan2mon channel 3 2>/dev/null
iwconfig wlan3mon channel 4 2>/dev/null
iwconfig wlan4mon channel 5 2>/dev/null
iwconfig wlan5mon channel 6 2>/dev/null
iwconfig wlan6mon channel 7 2>/dev/null
iwconfig wlan7mon channel 8 2>/dev/null
iwconfig wlan8mon channel 9 2>/dev/null
iwconfig wlan9mon channel 10 2>/dev/null
iwconfig wlan10mon channel 11 2>/dev/null
iwconfig wlan11mon channel 12 2>/dev/null
iwconfig wlan12mon channel 13 2>/dev/null
iwconfig wlan13mon channel 14 2>/dev/null

# Desactiva todos los adaptadores (Para config limpia de MAC)
iwconfig wlan0mon down 2>/dev/null
iwconfig wlan1mon down 2>/dev/null
iwconfig wlan2mon down 2>/dev/null
iwconfig wlan3mon down 2>/dev/null
iwconfig wlan4mon down 2>/dev/null
iwconfig wlan5mon down 2>/dev/null
iwconfig wlan6mon down 2>/dev/null
iwconfig wlan7mon down 2>/dev/null
iwconfig wlan8mon down 2>/dev/null
iwconfig wlan9mon down 2>/dev/null
iwconfig wlan10mon down 2>/dev/null
iwconfig wlan11mon down 2>/dev/null
iwconfig wlan12mon down 2>/dev/null
iwconfig wlan13mon down 2>/dev/null

# Cambia la dirección MAC de los adaptadores
macchanger --mac=f0:01:f0:f0:f0:f0 wlan0mon 2>/dev/null
macchanger --mac=f0:02:f0:f0:f0:f0 wlan1mon 2>/dev/null
macchanger --mac=f0:03:f0:f0:f0:f0 wlan2mon 2>/dev/null
macchanger --mac=f0:04:f0:f0:f0:f0 wlan3mon 2>/dev/null
macchanger --mac=f0:05:f0:f0:f0:f0 wlan4mon 2>/dev/null
macchanger --mac=f0:06:f0:f0:f0:f0 wlan5mon 2>/dev/null
macchanger --mac=f0:07:f0:f0:f0:f0 wlan6mon 2>/dev/null
macchanger --mac=f0:08:f0:f0:f0:f0 wlan7mon 2>/dev/null
macchanger --mac=f0:09:f0:f0:f0:f0 wlan8mon 2>/dev/null
macchanger --mac=f0:10:f0:f0:f0:f0 wlan9mon 2>/dev/null
macchanger --mac=f0:11:f0:f0:f0:f0 wlan10mon 2>/dev/null
macchanger --mac=f0:12:f0:f0:f0:f0 wlan11mon 2>/dev/null
macchanger --mac=f0:13:f0:f0:f0:f0 wlan12mon 2>/dev/null
macchanger --mac=f0:14:f0:f0:f0:f0 wlan13mon 2>/dev/null

# Activa los adaptadores con la nueva MAC
ifconfig wlan0mon up 2>/dev/null
ifconfig wlan1mon up 2>/dev/null
ifconfig wlan2mon up 2>/dev/null
ifconfig wlan3mon up 2>/dev/null
ifconfig wlan4mon up 2>/dev/null
ifconfig wlan5mon up 2>/dev/null
ifconfig wlan6mon up 2>/dev/null
ifconfig wlan7mon up 2>/dev/null
ifconfig wlan8mon up 2>/dev/null
ifconfig wlan9mon up 2>/dev/null
ifconfig wlan10mon up 2>/dev/null
ifconfig wlan11mon up 2>/dev/null
ifconfig wlan12mon up 2>/dev/null
ifconfig wlan13mon up 2>/dev/null
ifconfig wlan14mon up 2>/dev/null

# Limpia la pantalla nuevamente
clear

# Fz3r0 Info
echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"
echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"
echo ""

# Imprime información del sistema
echo -e "\033[97m--- SYSTEM:\033[0m"
echo ""
echo -e "\033[32m$(uname -a)\033[0m"
echo ""

# Imprime información de adaptadores USB y controladores
echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"
echo ""

# Imprime información de airmon-ng
echo -e "\033[32m$(airmon-ng)\033[0m"
echo ""

# Imprime información de las interfaces físicas
echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"
echo ""
echo -e "\033[36m$(ifconfig)\033[0m"
echo ""

# Imprime información de adaptadores inalámbricos y su modo
echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"
echo ""
iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'

````









---

saber la wlan utilizada
ifconfig -a | awk '/wlan/ {print $1}'





<br><br><br>

