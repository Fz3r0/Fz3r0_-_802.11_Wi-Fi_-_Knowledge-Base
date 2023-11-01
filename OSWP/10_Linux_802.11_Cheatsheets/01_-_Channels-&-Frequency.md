## 💀 `Fz3r0 Cheatsheet`: Channel Selection

- Basics

````sh
# Opción 1: iwconfig
iwconfig wlan0mon channel 6

# Opción 2: iwconfig (auto)
iwconfig eth0 channel auto

# Opción 3: iw
iw dev wlan0mon set channel 6

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

- Channel Selection: `x1 Adapter`

````sh
# Cambiar Canales a 3 Adaptadores (Necesario que estén en Monitor): Channels: 1,6,11 [Incluye MAC Spoofing por 01,02,03]
iwconfig wlan0mon channel 1 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 11 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````

- Channel Selection: `x3 Adaptes` - Channels: `1`,`6`,`11`

````sh
# Cambiar Canales a 3 Adaptadores (Necesario que estén en Monitor): Todos Channel 6 [Incluye MAC Spoofing por 01,02,03]
iwconfig wlan0mon channel 6 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 6 && clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 6 + CHANNEL 6 + CHANNEL 6] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
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

###

````sh

iwconfig eth0 freq 2422000000
iwconfig eth0 freq 2.422G
iwconfig eth0 channel 3
iwconfig eth0 channel auto
````

