<!-- 

Y ARRANCAN!!!


<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Hacia el Infierno del `OSWP`: <br> `Offensive Security Wireless Professional` 📡🦈💀  

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/7c94fd0b-296e-4884-a604-c6db7c386ca6) <br>
_Writeup y bitácora para la certificación **CWAP-402** de **CWNP (Certified Wireless Network Professional)**_ <br>
_por @ **Fz3r0 💀** (CWNA)_

---

<br><br>

# 💀 Fz3r0 Cheatsheet: `Channels` & `Frequency`

Scripts para configurar `canales` y `frecuencia` utilizando adaptadores Wi-Fi en `monitor mode` en kernels Linux basados en Debian.

## Basic Channel Selection

````sh
# Opción 1: iwconfig
iwconfig wlan0mon channel 6

# Opción 2: iwconfig (auto)
iwconfig wlan0mon channel auto

# Opción 3: iw
iw dev wlan0mon set channel 6
````

## Channel Selection: `x1 Adapter` @ `2.4 ghZ`

````sh
## CHANNEL :: [ 01 ] 
iwconfig wlan0mon channel 1 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 1 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 02 ] 
iwconfig wlan0mon channel 2 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 2 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 03 ] 
iwconfig wlan0mon channel 3 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 3 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 04 ] 
iwconfig wlan0mon channel 4 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 4 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 05 ] 
iwconfig wlan0mon channel 5 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 5 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 06 ] 
iwconfig wlan0mon channel 6 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 6 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 07 ] 
iwconfig wlan0mon channel 7 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 7 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 08 ] 
iwconfig wlan0mon channel 8 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 8 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 09 ] 
iwconfig wlan0mon channel 9 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 9 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 10 ] 
iwconfig wlan0mon channel 10 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 10 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 11 ] 
iwconfig wlan0mon channel 11 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 11 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 12 ] 
iwconfig wlan0mon channel 12 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 12 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 13 ] 
iwconfig wlan0mon channel 13 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 13 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## CHANNEL :: [ 14 ] 
iwconfig wlan0mon channel 14 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Channel Selector v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] SINGLE WIRELESS CHANNEL SELECTION\033[0m";echo -e "\033[97m[*] SINGLE ADAPTER START - [ CHANNEL 14 ] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

````

## 💀 `Fz3r0 Cheatsheet`: Band & Frequency Selection


````sh
# Opción 1: iwconfig
iwconfig wlan0mon channel 6

# Opción 2: iwconfig (auto)
iwconfig eth0 channel auto

# Opción 3: iw
iw dev wlan0mon set channel 6
````


---

## Frequency Selection & Validation

### Frequency Validation

````sh
# Validation: Available Channels
iwlist wlan0mon frequency

    # Channel 01 : 2.412 GHz
    # Channel 02 : 2.417 GHz
    # Channel 03 : 2.422 GHz
    # Channel 04 : 2.427 GHz
    # Channel 05 : 2.432 GHz
    # Channel 06 : 2.437 GHz
    # Channel 07 : 2.442 GHz
    # Channel 08 : 2.447 GHz
    # Channel 09 : 2.452 GHz
    # Channel 10 : 2.457 GHz
    # Channel 11 : 2.462 GHz

````
### Frequency Validation

````sh

iwconfig eth0 freq 2422000000
iwconfig eth0 freq 2.422G
iwconfig eth0 channel 3
iwconfig eth0 channel auto
````

