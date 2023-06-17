# Management Frames: `Beacon`

## Fz3r0 Lab: `Beacon Frame`

Los PCAPs utilizados para los ejemplos de este bloque son los siguientes:

- [`PCAP1` - **Fz3r0 Beacon** - Ruckus R850 - 2.4 GHz Ch 11 - WPA2 - ESS Centralized WLC - 1mb Data Rate Legacy Compatible](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779892/Beacon_Fz3r0_CH_11.zip)
- [`PCAP2` - **Fz3r0 Beacon** - Ruckus R850 - 5 GHz Ch 60 - WPA2 - ESS Centralized WLC - 24mb Data Rate OFDM Only](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779906/Beacon_Fz3r0_CH_60.zip)

---

<br><br>

## Beacon Frames

Los `Beacon Frames` son utilizados por los `APs` (y `STAs` en una `IBSS`) para **comunicar a través del área de servicio las características de la conexión ofrecida a los miembros de una `WLAN` dentro de la celda de cobertura del `AP`. Esta información es utilizada por los clientes que intentan conectarse a la red, así como por los clientes que ya están asociados al `BSS`.**

- Las Beacon Frames se envían periódicamente en un momento llamado `Target Beacon Transmission Time (TBTT).`

Los valores por default de un Beacon Frame son los siguientes:

- **`1 TU` = 1024 microsegundos**
- **`Beacon interval`  = 100 TU** (100 x 1024 microsegundos o 102.4 milisegundos)

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/88424fcf-e9cf-4889-801a-69fbaa74c44a)

---

<br><br>

## Beacon Frame: `Frame Format`

Este es el Frame Format de un Beacon Frame:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/2ac8ca5b-c2c8-4fe2-9fea-764ff9e57f77)

---

<br><br>

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

<br><br>

## `Timestamp` - 8 byte

**BlackShark Filter:**

````py
wlan.fixed.timestamp == 2078442701205
````

**Descripción**

- Un valor que representa el tiempo en el que el AP ha estado activo, que es el número de **microsegundos que el AP ha estado en funcionamiento**.
- Cuando el timestamp alcanza su máximo (2^64 microsegundos o ~580,000 años), se reinicia a 0. 

**Este campo se encuentra en los Frames:**

- `Beacon` 
- `Probe Response`    

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/f5f9fcbb-cbf5-4056-90aa-a1c79f16eabd)

---

<br><br>

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

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/89935078-04ed-49dc-88ae-fbd0b8c2d053)

### `Capability Information` - 2 byte

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

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/0aa3320b-1965-4f1f-b1d5-d8a16d1fbe90)

---

<br><br>

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

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a812eca5-92b9-44e7-b4cf-92ff23422491)





| **Beacon Field**             | **Lenght** | **Descripción**                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`Timestamp`**              | `8 byte`   | Un valor que representa el tiempo en el que el AP ha estado activo, que es el número de **microsegundos que el AP ha estado en funcionamiento**.<br> <br>Cuando el timestamp alcanza su máximo (2^64 microsegundos o ~580,000 años), se reinicia a 0. <br><br>Este campo se encuentra en los Frames: `Beacon` & `Probe Response`                                                                                                                                                           |
| **`Beacon Interval`**        | `2 byte`   | Este campo representa el número de `Time Units (TU)` entre los tiempos de `Target Beacon Trasmission Times (TBTT)`.<br><br>El **valor default** es `100 TU` (102.4 milisegundos).                                                                                                                                                                                                                                                                                                          |
| **`Capability Information`** | `2 byte`   | Este campo contiene una serie de **subcampos** que se utilizan para indicar las capacidades opcionales solicitadas o anunciadas.                                                                                                                                                                                                                                                                                                                                                           |
| **`SSID`**                   | _Variable_ | El ID del elemento es `0` para el `Information Element (IE)` de `SSID`. <br><br>El `SSID` puede tener un **máximo de 32 caracteres**. <br><br>Este campo se encuentra en los Frames: `Beacons`, `Probe Requests`, `Probe Responses`, `Association Request` & `Re-Association Requests`.                                                                                                                                                                                                    |
| **`Supported Rates`**        | `8 byte`   | Es un campo de `8 octetos` donde **cada octeto describe una `Data Rate` soportada.** <br><br>Tiene los campos `Element ID`, `Length` y `Supported Rates`. <br><br>El `AP` debe establecer al menos un rate obligatorio y cualquier `STA` que desee unirse a la celda debe ser copatible con los `Basic Rates`. <br><br>Este campo se encuentra en los Frames: `Beacons`, `Probe Requests`, `Probe Responses`, `Association Request`, `Re-Association Requests` & `Re-Association Response` |

## Recursos

[CWNE#153 (Rasika Nayanajith) - 802.11 Mgmt : Beacon Frame](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
