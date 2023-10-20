# 📡💊 Management Frames (802.11): `Probe Request & Response`

Descubrir la red escaneando todos los posibles canales y escuchando por `Beacon Frames` desde nuestro dispositrivo no se considera muy eficiente _(`Passive Scanning`)_. Para mejorar este proceso de descubrimiento, las `STA` a menudo utilizan `Active Scanning` y para este proceso se unas los Frames `Probe Request` & `Probe Response`.

- Los **`Probe Request`** los utilizan las `STA` para descubrir la WLAN de modo: **`Active Scanning`** _([Passive Scanning, Active Scanning & Roaming](https://www.youtube.com/watch?v=HPJonmd8z1c))_
- Los **`Probe Response`** simplemente es la respuesta desde un `AP` que escucho por el Probe Request enviado desde una STA. 

En el `Active Scanning`, las `STA` aún recorren cada canal uno por uno, pero en lugar de escuchar pasivamente las señales en esa frecuencia, la `STA` envía un `Probe Request` preguntando qué red está disponible en ese canal.

- NOTA: Las `STA` deben tener aprendida la red previamente. 

Los `Probe Request` se envían a la dirección `Broadcast`: 

- `DA (Destination Address)` :: `FF:FF:FF:FF:FF:FF`.

Una vez que se envía un `Probe Request`, la `STA` inicia un temporizador llamado `ProbeTimer Countdown` y espera respuestas (`Probe Response`) de un posible AP en el área. Cuando el temporizador del `ProbeTimer Countdown` termina, la `STA` procesa la respuesta que ha recibido. Si no se reciben respuestas, la `STA` pasa al siguiente canal y repite el proceso de descubrimiento.

Las `STA` que envían `Probe Request` pueden especificar el `SSID` que están buscando, a esto se le llama `Directed Probe Request`. Luego, solo los APs _(o IBSSS STAs)_ que admitan ese SSID responderán. El valor del SSID también se puede establecer en 0 (es decir, el campo del SSID está presente pero vacío).

- **Esto se llama `Wildcard SSID` o `Null Probe Request`.**

## PCAPs de Laboratiorio: `Probe Request & Response`

Los PCAPs utilizados para los ejemplos de este bloque son los siguientes:

- [`PCAP1` - **Fz3r0 Beacon** - Ruckus R850 - 2.4 GHz Ch 11 - WPA2 - ESS Centralized WLC - 1mb Data Rate Legacy Compatible](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779892/Beacon_Fz3r0_CH_11.zip)

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
wlan.fc.type_subtype == 4

## Opción 2
wlan.fc.type_subtype == 0x0004

##########################################################################
#                      ALL Probe Response Frames:                        #
##########################################################################

## Opción 1
wlan.fc.type_subtype == 5

## Opción 2
wlan.fc.type_subtype == 0x0005 

##########################################################################
#              ALL Probe Request + Probe Response Frames:                #
##########################################################################

## Opción 1
(wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5) && !wlan.fc.retry ==1

## Opción 2
(wlan.fc.type_subtype == 0x0004 || wlan.fc.type_subtype == 0x0005) && !wlan.fc.retry ==1

##########################################################################
#     Specific STA <--> AP :: Probe Request + Probe Response Frames:     #
##########################################################################

## Ejemplo    ::    STA(Request) <--> AP(Response)

# STA (Probe Request Transmiter/Source): Fz3r0 PC Wi-Fi Adapter:
## MAC :: 44:E5:17:06:E4:60
wlan.ta == 44:e5:17:06:e4:60

# AP (Probe Response Transmiter/Source): AP - Telmex Casero:
## MAC :: 50:4e:dc:90:2e:b8
wlan.ta == 50:4e:dc:90:2e:b8

# STA (Probe Response Receiver/Destination): Fz3r0 PC Wi-Fi Adapter:
## MAC :: 44:E5:17:06:E4:60
wlan.ra == 44:e5:17:06:e4:60

# Fz3r0: Super command for searching specific Probe Request & Response Between STA <--> AP  || SUPREME VICTORY
    ## Se deben cambiar 3 direcciones en total para que funcione
    ## 1. Probe Request   ::   wlan.TA(transmiter) (STA)
    ## 2. Probe Response  ::   wlan.TA(transmiter) (AP)
    ## 3. Probe Response  ::   wlan.RA(receiver)   (STA)
(wlan.fc.type_subtype == 4 && wlan.ta == 44:E5:17:06:E4:60) || (wlan.fc.type_subtype == 5 && wlan.ta == 50:4e:dc:90:2e:b8 && wlan.ra == 44:e5:17:06:e4:60) && !wlan.fc.retry ==1

##########################################################################
#    Specific STA <--> AP :: Probe Request & Response + Authentication   #
##########################################################################

# Fz3r0: Super command for searching specific Probe Request & Response Between STA <--> AP  || SUPREME VICTORY
#  +
# Fz3r0: 4-way-handshake Authentication Process (SUPREME VICTORY PERFECT!!! Sin Probes & Sin Actions - IT'S DANGEROUS!!!)
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol) || (wlan.fc.type_subtype == 4 && wlan.ta == 44:E5:17:06:E4:60) || (wlan.fc.type_subtype == 5 && wlan.ta == 50:4e:dc:90:2e:b8 && wlan.ra == 44:e5:17:06:e4:60)

# Fz3r0: Super command for searching specific Probe Request & Response Between STA <--> AP  || SUPREME VICTORY
#  +
# Fz3r0: 4-way-handshake Authentication Process (SUPREME VICTORY PERFECT!!! Sin Probes & Sin Actions - IT'S DANGEROUS!!!)
#
# ACKs!!! (Ultra Ultra Ultra)
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol) || (wlan.fc.type_subtype == 4 && wlan.ta == 44:E5:17:06:E4:60) || (wlan.fc.type_subtype == 5 && wlan.ta == 50:4e:dc:90:2e:b8 && wlan.ra == 44:e5:17:06:e4:60) || (wlan.fc.type_subtype == 0x001d && wlan.ra == 50:4e:dc:90:2e:b8)


##########################################################################
#                         Probe Request Fields:                          #
#************************************************************************#
#        -  01 [+] Timestamp         (8 byte)                            #
#        -  02 [+] Beacon Interval   (2 byte)                            #
#        -  03 [+] Capability info   (2 byte)           #
#        -  04 [+] SSID              (variable size)*   #
#        -  05 [+] Supported Rates   (variable size)*   #
##########################################################################

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

## 📡 Probe Request & Response Frames: Descripción


















## 🧪 Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/2d0fe58e-49f1-48da-a227-cb27dc8588b9)

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


