# 📡💊 Management Frames (802.11): `Probe Request & Probe Response`

Los PCAPs utilizados para los ejemplos de este bloque son los siguientes:

- [`PCAP1` - **Fz3r0 Beacon** - Ruckus R850 - 2.4 GHz Ch 11 - WPA2 - ESS Centralized WLC - 1mb Data Rate Legacy Compatible](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779892/Beacon_Fz3r0_CH_11.zip)
- [`PCAP2` - **Fz3r0 Beacon** - Ruckus R850 - 5 GHz Ch 60 - WPA2 - ESS Centralized WLC - 24mb Data Rate OFDM Only](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779906/Beacon_Fz3r0_CH_60.zip)
- [`PCAP3` - **Infinitum Beacon** - Telmex Home Generic - 2.4 GHz Ch 6 - WPA2 - ESS Home WLAN - 6mb Data Rate](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11780434/Infinitum_Beacon_2.4GHz.zip)
- [`PCAP4` - **Public Beacon** - Ruckus H510 - 5 GHz - 802.1X - ESS Centralized WLC](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11782465/Ruckus.H510.Public.Network.802.1x.RSN.zip)

## 🦈 `BlackShark Filter`: Probe Request & Probe Response (802.11)

````py

##########################################################################
#                                                                        #
#   Fz3r0 - BlackShark Filter: Probe Request & Probe Response (802.11)   #
#                                                                        #
##########################################################################

##########################################################################
#                      ALL Probe Request Frames:                         #
##########################################################################

## Opción 1
wlan.fc.type_subtype == 8

## Opción 2
wlan.fc.type_subtype == 0x0008

##########################################################################
#                      ALL Probe Response Frames:                        #
##########################################################################







#########################################################
#           Beacon Frames - MANDATORY Fields:           #
#*******************************************************#
#        -  01 [+] Timestamp         (8 byte)           #
#        -  02 [+] Beacon Interval   (2 byte)           #
#        -  03 [+] Capability info   (2 byte)           #
#        -  04 [+] SSID              (variable size)*   #
#        -  05 [+] Supported Rates   (variable size)*   #
#########################################################

## [+] 01 - Timestamp - 8 byte >>>
wlan.fixed.timestamp == 2078442701205

## [+] 02 - Beacon Interval - 2 byte

   ## Beacon Interval
   wlan.fixed.beacon == 100

## [+] 03 - Capability Information - 2 byte

   # NOTA: 1 = SI / 0 = NO

   ### ALL Capabilities / HEX code combination
   wlan.fixed.capabilities == 0x1511

   ### ESS capabilites 
   wlan.fixed.capabilities.ess == 1

   ### IBSSS status
   wlan.fixed.capabilities.ibss == 0

   ### Reserved 1
   wlan.fixed.capabilities.reserved1 == 0

   ### Reserved 2
   wlan.fixed.capabilities.reserved2 == 0

   ### Privacy 
   wlan.fixed.capabilities.privacy == 1

   ### Short Preamble
   wlan.fixed.capabilities.short_preamble == 0

   ### Reserved 3
   wlan.fixed.capabilities.reserved3 == 0

   ### Reserved 4
   wlan.fixed.capabilities.reserved4 == 0

   ### Spectrum Management
   wlan.fixed.capabilities.spec_man == 1

   ### QoS
   wlan.fixed.capabilities.qos == 0

   ### Short Slot Time
   wlan.fixed.capabilities.short_slot_time == 1

   ### Automatic Power Save Delivery
   wlan.fixed.capabilities.apsd == 0

   ### Radio Measurement
   wlan.fixed.capabilities.radio_measurement == 1

   ### EPD
   wlan.fixed.capabilities.epd == 0

   ### Reserved 5
   wlan.fixed.capabilities.reserved5 == 0

   ### Reserved 6
   wlan.fixed.capabilities.reserved6 == 0

## [+] 04 - SSID - _Variable Size_

   ### Tag Number
   wlan.tag.number == 0

   ### Tag Lenght
   wlan.tag.length == 5

   ### SSID
   wlan.ssid == "Fz3r0"

   ### Hidden SSID (Wildcard)
   wlan.ssid == ""

## [+] 05 - Supported Rates - _Variable Size_

### All Supported Rates
wlan.supported_rates

   ### Supported Data Rate   =   12 Mbps
   wlan.supported_rates == 0x98

   ### Supported Data Rate   =   18 Mbps
   wlan.supported_rates == 0x24

   ### Supported Data Rate   =   24 Mbps
   wlan.supported_rates == 0x30

   ### Supported Data Rate   =   36 Mbps
   wlan.supported_rates == 0x48

   ### Supported Data Rate   =   48 Mbps
   wlan.supported_rates == 0x60

   ### Supported Data Rate   =   54 Mbps
   wlan.supported_rates == 0x6c

#########################################################
#            Beacon Frames - OPTIONAL Fields:           #
#*******************************************************#
#        -  01 [+] Timestamp         (8 byte)           #
#        -  02 [+] Beacon Interval   (2 byte)           #
#        -  03 [+] Capability info   (2 byte)           #
#        -  04 [+] SSID              (variable size)*   #
#        -  05 [+] Supported Rates   (variable size)*   #
#########################################################

````

## 📡 Beacon Frames: Descripción

Los `Beacon Frames` son utilizados por los `APs` (y `STAs` en una `IBSS`) para **comunicar a través del área de servicio las características de la conexión ofrecida a los miembros de una `WLAN` dentro de la celda de cobertura del `AP`. Esta información es utilizada por los clientes que intentan conectarse a la red, así como por los clientes que ya están asociados al `BSS`.**

- Los `Beacon Frames` se utilizan para descubrir la WLAN de modo: **`Passive Scanning`**

Las Beacon Frames se envían periódicamente en un momento llamado `Target Beacon Transmission Time (TBTT).`

- Los valores por default de un TBTT en un Beacon Frame son `100 TU`:

    - **`1 TU` = 1024 [Microsegundos]**
    - **`Beacon interval`  = 100 TU's** || 100 x 1024 microsegundos = `102.4 Milisegundos` ó = `0.102400 Segundos`

## 🧪 Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/88424fcf-e9cf-4889-801a-69fbaa74c44a)

## Beacon Frame: `Frame Format`

Este es el Frame Format de un Beacon Frame:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/2ac8ca5b-c2c8-4fe2-9fea-764ff9e57f77)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 📡 Beacon Frame: `Frame Body`

- En la sección del `Frame Body`, hay algunos **campos obligatorios** y algunos **campos opcionales**. 

Estos son los campos obligatorios en un `Beacon Frame`:

1. **`Timestamp`** (8 byte)
2. **`Beacon Interval`** (2 byte)
3. **`Capability info`** (2 byte)
4. **`SSID`** (variable size)
5. **`Supported Rates`** (variable size)

---

### Ejemplo 1: `Ruckus R850` + `SmartZone`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/1c129e19-63c3-465a-9423-f48420682ea6)

### Ejemplo 2: `Telmex Generic Home Wi-Fi Router`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/8fd599f5-5773-440f-97c8-608bec4977ab)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

# 📡🕵️ Beacon Frame Body: `Mandatory Fields`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/df5d86c3-ff5a-4453-9554-c6b4e5b29067)

## 01 - `Timestamp` - 8 byte

### BlackShark Filter:

````py
## 01 - Timestamp - 8 byte
wlan.fixed.timestamp == 2078442701205
````

---

### Descripción:

- Un valor que representa el tiempo en el que el AP ha estado activo, que es el número de **microsegundos que el AP ha estado en funcionamiento**.
- Cuando el timestamp alcanza su máximo (2^64 microsegundos o ~580,000 años), se reinicia a 0. 

---

### Disponible en Frames:

- `Beacon` 
- `Probe Response`    

---

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/f5f9fcbb-cbf5-4056-90aa-a1c79f16eabd)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 📡 02 - 



























---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## Recursos

[CWNE#153 (Rasika Nayanajith) - 802.11 Mgmt : Probe Request & Response Frame](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/)


