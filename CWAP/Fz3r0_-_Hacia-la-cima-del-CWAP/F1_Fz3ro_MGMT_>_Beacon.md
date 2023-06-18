# Management Frames: `Beacon`

## Fz3r0 Lab: `Beacon Frame`

Los PCAPs utilizados para los ejemplos de este bloque son los siguientes:

- [`PCAP1` - **Fz3r0 Beacon** - Ruckus R850 - 2.4 GHz Ch 11 - WPA2 - ESS Centralized WLC - 1mb Data Rate Legacy Compatible](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779892/Beacon_Fz3r0_CH_11.zip)
- [`PCAP2` - **Fz3r0 Beacon** - Ruckus R850 - 5 GHz Ch 60 - WPA2 - ESS Centralized WLC - 24mb Data Rate OFDM Only](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779906/Beacon_Fz3r0_CH_60.zip)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## Beacon Frames

**BlackShark Filter:**

````py
## Opción 1
wlan.fc.type_subtype == 8

## Opción 2
wlan.fc.type_subtype == 0x0008
````

**Descripción:**

Los `Beacon Frames` son utilizados por los `APs` (y `STAs` en una `IBSS`) para **comunicar a través del área de servicio las características de la conexión ofrecida a los miembros de una `WLAN` dentro de la celda de cobertura del `AP`. Esta información es utilizada por los clientes que intentan conectarse a la red, así como por los clientes que ya están asociados al `BSS`.**

- Las Beacon Frames se envían periódicamente en un momento llamado `Target Beacon Transmission Time (TBTT).`

Los valores por default de un Beacon Frame son los siguientes:

- **`1 TU` = 1024 microsegundos**
- **`Beacon interval`  = 100 TU** (100 x 1024 microsegundos o 102.4 milisegundos)

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/88424fcf-e9cf-4889-801a-69fbaa74c44a)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

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

## Beacon Frame: `Frame Body`

- En la sección del `Frame Body`, hay algunos **campos obligatorios** y algunos **campos opcionales**. 

Estos son los campos obligatorios en un `Beacon Frame`:

1. **`Timestamp`** (8 byte)
2. **`Beacon Interval`** (2 byte)
3. **`Capability info`** (2 byte)
4. **`SSID`** (variable size)
5. **`Supported Rates`** (variable size)

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/1c129e19-63c3-465a-9423-f48420682ea6)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

# Frame Body: `Mandatory Fields`

## `Timestamp` - 8 byte

**BlackShark Filter:**

````py
wlan.fixed.timestamp == 2078442701205
````

**Descripción:**

- Un valor que representa el tiempo en el que el AP ha estado activo, que es el número de **microsegundos que el AP ha estado en funcionamiento**.
- Cuando el timestamp alcanza su máximo (2^64 microsegundos o ~580,000 años), se reinicia a 0. 

**Este campo se encuentra en los Frames:**

- `Beacon` 
- `Probe Response`    

**Ejemplo:**

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/f5f9fcbb-cbf5-4056-90aa-a1c79f16eabd)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## `Beacon Interval` - 2 byte

**BlackShark Filter:**

````py
wlan.fixed.beacon == 100
````

**Descripción**

- Este campo representa el número de `Time Units (TU)` entre los tiempos de `Target Beacon Trasmission Times (TBTT)`.
- El **valor default** es `100 TU` (102.4 milisegundos) = **`0.102400 segundos`**

**Este campo se encuentra en los Frames:**

- `Beacon` 

**Ejemplo:**

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/89935078-04ed-49dc-88ae-fbd0b8c2d053)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## `Capability Information` - 2 byte

**BlackShark Filter:**

````py
## Capabilities
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
````

**Descripción**

- Este campo contiene una serie de **subcampos** que se utilizan para indicar las capacidades opcionales solicitadas o anunciadas.   

**Este campo se encuentra en los Frames:**

- `Beacon` 

**Ejemplo:**

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/0aa3320b-1965-4f1f-b1d5-d8a16d1fbe90)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## `SSID` - _Variable_

**BlackShark Filter:**

````py
### Tag Number
wlan.tag.number == 0

### Tag Lenght
wlan.tag.length == 5

### SSID
wlan.ssid == "Fz3r0"
````

**Descripción**

- Este campo contiene una serie de **subcampos** que se utilizan para indicar las capacidades opcionales solicitadas o anunciadas.   

**Este campo se encuentra en los Frames:**

- `Beacon` 

**Ejemplo:**

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a812eca5-92b9-44e7-b4cf-92ff23422491)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## `Supported Rates` - 8 byte

**BlackShark Filter:**

````py
### Supported Data Rate = 24mbps
wlan.supported_rates == 0xb0

### Supported Data Rate = 36mbps
wlan.supported_rates == 0x48

### Supported Data Rate = 48mbps
wlan.supported_rates == 0x60

### Supported Data Rate = 54mbps
wlan.supported_rates == 0x6c
````

**Descripción:**

- Es un campo de `8 octetos` donde **cada octeto describe una `Data Rate` soportada.** 
- Tiene los campos `Element ID`, `Length` y `Supported Rates`. 
- El `AP` debe establecer al menos un rate obligatorio y cualquier `STA` que desee unirse a la celda debe ser copatible con los `Basic Rates`. 

**Este campo se encuentra en los Frames:**

- `Beacons`
- `Probe Requests`
- `Probe Responses`
- `Association Request`
- `Re-Association Requests`
- `Re-Association Response`

**Ejemplo:**

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/5329371d-b715-4f37-95d3-becc9d7be761)


---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

# Frame Body: `Optional Fields`

## `FH parameter set` - _Variable_

**BlackShark Filter:**

````py

````

**Descripción:**

- Este parámetro se utiliza en `STA legacy` que utilizan la `Frequency Hopping (FH)`. 
- El conjunto de parámetros `FH` proporciona información específica sobre la configuración y características del `Frequency Hopping (FH)` utilizado por estas estaciones.

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>



























FH parameter set: 

DS Parameter (2 byte): Este parámetro está presente en los marcos de baliza generados por estaciones que utilizan PHY (capa física) según lo definido en las cláusulas 15, 18 o 19 del estándar IEEE 802.11. También puede estar presente si la baliza se envía utilizando una de las tasas definidas en alguna de estas cláusulas. El DS Parameter indica el conjunto de canales permitidos para su uso en la red.

CF Parameter (8 byte): El parámetro CF (Control Frame) se utiliza en conjunción con el PCF (Point Coordination Function) que es parte del estándar IEEE 802.11. Sin embargo, en la práctica, este parámetro no se utiliza comúnmente en redes reales, ya que el PCF no es ampliamente implementado.

IBSS parameter (4 byte): Este parámetro está presente solo en los marcos de baliza generados por estaciones en redes IBSS (Independent Basic Service Set) o redes ad-hoc. El IBSS parameter proporciona información específica sobre la configuración y características de la red ad-hoc, como el modo de operación y las capacidades admitidas.








---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## Recursos

[CWNE#153 (Rasika Nayanajith) - 802.11 Mgmt : Beacon Frame](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
