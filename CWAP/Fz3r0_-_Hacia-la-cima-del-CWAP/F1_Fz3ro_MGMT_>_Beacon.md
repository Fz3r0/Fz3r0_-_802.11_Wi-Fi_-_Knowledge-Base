# 📡💊 Management Frames (802.11): `Beacon`

Los PCAPs utilizados para los ejemplos de este bloque son los siguientes:

- [`PCAP1` - **Fz3r0 Beacon** - Ruckus R850 - 2.4 GHz Ch 11 - WPA2 - ESS Centralized WLC - 1mb Data Rate Legacy Compatible](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779892/Beacon_Fz3r0_CH_11.zip)
- [`PCAP2` - **Fz3r0 Beacon** - Ruckus R850 - 5 GHz Ch 60 - WPA2 - ESS Centralized WLC - 24mb Data Rate OFDM Only](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11779906/Beacon_Fz3r0_CH_60.zip)
- [`PCAP3` - **Infinitum Beacon** - Telmex Home Generic - 2.4 GHz Ch 6 - WPA2 - ESS Home WLAN - 6mb Data Rate](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11780434/Infinitum_Beacon_2.4GHz.zip)
- [`PCAP4` - **Public Beacon** - Ruckus H510 - 5 GHz - 802.1X - ESS Centralized WLC](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11782465/Ruckus.H510.Public.Network.802.1x.RSN.zip)

## 🦈⚫ `BlackShark Filter`: Beacon Frames (802.11)

````py
## Opción 1
wlan.fc.type_subtype == 8

## Opción 2
wlan.fc.type_subtype == 0x0008
````

## Beacon Frames: Descripción

Los `Beacon Frames` son utilizados por los `APs` (y `STAs` en una `IBSS`) para **comunicar a través del área de servicio las características de la conexión ofrecida a los miembros de una `WLAN` dentro de la celda de cobertura del `AP`. Esta información es utilizada por los clientes que intentan conectarse a la red, así como por los clientes que ya están asociados al `BSS`.**

- Las Beacon Frames se envían periódicamente en un momento llamado `Target Beacon Transmission Time (TBTT).`

Los valores por default de un Beacon Frame son los siguientes:

- **`1 TU` = 1024 microsegundos**
- **`Beacon interval`  = 100 TU** (100 x 1024 microsegundos o 102.4 milisegundos)

### Ejemplo:

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

# Beacon Frame Body: `Mandatory Fields`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/df5d86c3-ff5a-4453-9554-c6b4e5b29067)

## 01 - `Timestamp` - 8 byte

### BlackShark Filter:

````py
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

## 02 - `Beacon Interval` - 2 byte

### BlackShark Filter:

````py
wlan.fixed.beacon == 100
````

---

### Descripción:

- Este campo representa el número de `Time Units (TU)` entre los tiempos de `Target Beacon Trasmission Times (TBTT)`.
- El **valor default** es `100 TU` (102.4 milisegundos) = **`0.102400 segundos`**

---

### Disponible en Frames:

- `Beacon` 

---

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/89935078-04ed-49dc-88ae-fbd0b8c2d053)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 03 - `Capability Information` - 2 byte

### BlackShark Filter:

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

---

### Descripción:

- Este campo contiene una serie de **subcampos** que se utilizan para indicar las capacidades opcionales solicitadas o anunciadas.   

**Este campo se encuentra en los Frames:**

- `Beacon` 

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/0aa3320b-1965-4f1f-b1d5-d8a16d1fbe90)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 04 - `SSID` - _Variable_

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 0

### Tag Lenght
wlan.tag.length == 5

### SSID
wlan.ssid == "Fz3r0"
````

---

### Descripción:

- Este campo contiene una serie de **subcampos** que se utilizan para indicar las capacidades opcionales solicitadas o anunciadas. 
- Se identifica mediante un número de etiqueta (tag number) igual a 0. 
- La longitud del campo SSID puede tener un máximo de 32 caracteres, aunque es importante destacar que el SSID puede configurarse para ser oculto, lo que implica que no se transmiten en los `Beacon Frame` _(Pero si en probes, es por eso ocultar el SSID no necesariamente es seguro)._
- **Cuando un dispositivo cliente busca redes inalámbricas disponibles, escanea los `Beacon Frames` y analiza los campos `SSID` para encontrar una red con un nombre específico o para descubrir las redes visibles en su entorno. Al conectarse a una red, el dispositivo debe proporcionar el SSID correcto y coincidente para establecer la conexión con éxito.**
- El SSID desempeña un papel fundamental en la identificación y configuración de redes inalámbricas, permitiendo a los dispositivos distinguir y conectarse a la red deseada.  

---

### Disponible en Frames:

- `Beacon frames`
- `probe requests`
- `probe responses`
- `association requests`
- `reassociation requests`

---

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a812eca5-92b9-44e7-b4cf-92ff23422491)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 05 - `Supported Rates` - 8 byte

### BlackShark Filter:

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

---

### Descripción:

- Es un campo de `8 octetos` donde **cada octeto describe una `Data Rate` soportada.** 
- Tiene los campos `Element ID`, `Length` y `Supported Rates`. 
- El `AP` debe establecer al menos un rate obligatorio y cualquier `STA` que desee unirse a la celda debe ser copatible con los `Basic Rates`. 

### Disponible en Frames:

- `Beacons`
- `Probe Requests`
- `Probe Responses`
- `Association Request`
- `Re-Association Requests`
- `Re-Association Response`

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/5329371d-b715-4f37-95d3-becc9d7be761)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

# Beacon Frame Body: `Optional Fields`

### Ejemplo 1: Ruckus

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a0d3dc35-88fa-4354-b62d-2c0102dfd3de)

### Ejemplo 2: Telmex

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/13c894cb-21ba-4f70-8c5f-f4982ad1331c)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 06 - `FH parameter set` - _Variable_

### BlackShark Filter:

````py

````

---

### Descripción:

- Este parámetro se utiliza en `STA legacy` que utilizan la `Frequency Hopping (FH)`. 
- El conjunto de parámetros `FH` proporciona información específica sobre la configuración y características del `Frequency Hopping (FH)` utilizado por estas estaciones.

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 07 - `DS Parameter` - 2 byte

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 3

### Tag Lenght
wlan.tag.length == 1

### Current Channel
wlan.ds.current_channel == 60
````

---

### Descripción:

- El `DS Parameter` indica **el conjunto de canales permitidos para su uso en la red.**
- `DS` es la abreviatura de `Distribution System`. 
- `DS` se refiere al `sistema de distribución` que proporciona conectividad entre las `STA` móviles (por ejemplo, dispositivos cliente) y los `AP` en una red inalámbrica. 
- Este parámetro está presente en los `Beacon Frames` generados por `STA` que utilizan `PHY` según lo definido en las `cláusulas 15, 18 o 19` del estándar `IEEE 802.11`. 
- También puede estar presente si la `Beacon Frames` se envía utilizando una de las tasas definidas en alguna de estas cláusulas. 
- El Tag number es su identificador específico. 

### Fz3r0 Troubleshooting Tip!!!:

**Cuando un Beacon tiene este campo opcional se puede saber el canal real en el que se encuentra ese AP, no corresponde al canal en el que se está capturando. Esto es importante en la red 2.4 para identificar interferencias ACI, ya que si por ejemplo estoy en `canal 11` podría cpaturar interferencias de canales alrededor, como `9` y `10`**

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/eafdb15e-db4e-44c7-8c27-1a6cbb715d8c)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 08 - `CF Parameter (8 byte)` - 2 byte

### BlackShark Filter:

````py

````

---

### Descripción:

- El parámetro `CF (Control Frame)` se utiliza en conjunción con el `PCF (Point Coordination Function)` que es parte del estándar `IEEE 802.11`. 
- Sin embargo, en la práctica, **este parámetro NO se utiliza comúnmente en redes reales**, ya que el `PCF` no es ampliamente implementado.

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 09 - `IBSS parameter` - 4 byte

### BlackShark Filter:

````py

````

---

### Descripción:

- Este parámetro está presente solo en los `Beacon Frames` generados por `STAs` en redes `IBSS (Independent Basic Service Set)` o redes `ad-hoc`. 
- El `IBSS` parameter proporciona **información específica sobre la configuración y características de la red `ad-hoc`, como el `operation mode` y las `capabilities` admitidas.

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 10 - `TIM (Traffic Indication Map)` - 2 byte

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 5

### Lenght
wlan.tag.length == 4

### DTIM Count
wlan.tim.dtim_count == 0

### DTIM Period
wlan.tim.dtim_period == 1

### Multicast Pendientes
wlan.tim.bmapctl.multicast == 0

### Bitmap Control Offset
wlan.tim.bmapctl.offset == 0x00

### Partial Virtual Bitmap
wlan.tim.partial_virtual_bitmap == 00
````

---

### Descripción:

- El `TIM` permite a las STAs en `modo de bajo consumo de energía` saber si hay datos `multicast` o `broadcast` almacenados en `Buffer` en el `AP`. Esto les permite "despertar" (`wake-up`) de su modo de bajo consumo y recibir los datos correspondientes cuando sea necesario. 
- Presente solo en los `Beacon Frames` generados por `APs`. 
- El `AP` utiliza el `Delivery Traffic Indication Map (DTIM)` para informar a la celda si tiene `broadcast frames` o `multicast frames` almacenadas en búfer. 
- **El `DTIM` no está presente en todas los `Beacons` y todos los `TIMs`. En ocasiones puede variar, por ejemplo, cada 3 Beacons.**

---

### Campos TIM:

- `Element ID` (1 byte): Identificador del elemento.
- Length (4 byte): Longitud del campo.
- DTIM Count (1 byte): Cantidad de marcos de baliza (incluido el actual) antes del próximo DTIM. **El valor `0` indica que el `TIM actual` es un `DTIM`**.
- DTIM Period (1 byte): Número de intervalos de Beacons entre DTIM sucesivos.
- Bitmap Control (1 byte): Si el primer bit es 1, indica que hay datos multidifusión/difusión almacenados en búfer en el AP. Si el primer bit es 0, no hay datos multidifusión/difusión en el AP.
- Partial Virtual Bitmap (1-251 byte): Representa las estaciones en modo de bajo consumo de energía para las cuales el AP tiene tráfico almacenado en búfer.

---

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/b25024c4-006b-4561-b23a-1c87ba4ede7a)


---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 11 - `Country Information` - _Variable_

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 7

### Lenght
wlan.tag.length == 36

### Country Code
wlan.country_info.code == "MX"

### Enviorment
wlan.country_info.environment == 32

### First Channel Number (Principal en caso de 40MHz o más)
wlan.country_info.fnm.fcn == 36

### Maximum Transmit Power Level
wlan.country_info.fnm.mtpl == 23

````

---

### Descripción:

- Cada país tiene organismos reguladores que limitan los canales o niveles de potencia permitidos en su dominio regulatorio. 
- Este campo define el país de operación junto con los canales permitidos y la potencia máxima de transmisión. 
- Este campo no es obligatorio en un Beacon.

---

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/e7202c08-398d-4440-afbf-75cbafa0df67)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 12 - `FH Parameters` - _Variable_

### BlackShark Filter:

````py

````

---

### Descripción:

- Utilizado en STAs legacy FH y ya no utilizado en OFDM o estándares nuevos como Wi-Fi 4,5,6 (802.11n/ac/ax)
- El campo "FH Parameters" se refiere a los parámetros relacionados con la técnica de salto de frecuencia o `Frequency Hopping`
- Sin embargo, en los estándares más recientes de IEEE 802.11, como Wi-Fi 4 (802.11n), Wi-Fi 5 (802.11ac) y Wi-Fi 6 (802.11ax), el uso de salto de frecuencia se ha vuelto menos común y ha sido reemplazado por otras técnicas de acceso al medio más eficientes como el `OFDM Schema`

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 13 - `FH Pattern table` - _Variable_

### BlackShark Filter:

````py

````

---

### Descripción:

- Utilizado en STAs legacy FH y ya no utilizado en OFDM o estándares nuevos como Wi-Fi 4,5,6 (802.11n/ac/ax)
- Se refiere a una estructura de datos que contiene la información detallada sobre los patrones de salto de frecuencia utilizados por las estaciones heredadas que implementan la técnica de salto de frecuencia (FH).
- La tabla de patrones FH permite a las estaciones heredadas coordinar y sincronizar sus saltos de frecuencia para evitar colisiones y asegurar una comunicación eficiente y confiable. 
- Al seguir el patrón de salto de frecuencia definido en la tabla, las estaciones pueden cambiar rápidamente entre frecuencias para mitigar las interferencias y mejorar la robustez de la comunicación.
- la técnica de salto de frecuencia es menos común en las redes inalámbricas modernas, ya que ha sido reemplazada en gran medida por otras técnicas más eficientes y avanzadas, como la modulación OFDM utilizada en los estándares Wi-Fi más recientes.

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 14 - `Power Constraint` - 3 byte

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 32

### Lenght
wlan.tag.length == 1

---

### Local Power Constraint
wlan.powercon.local == 0
````

---

### Descripción:

- Este elemento está relacionado con el estándar **`802.11h`**. 
- Se aplica a las bandas UNII2 y UNII-2 extendida (CH52,56,60,64 y CH100-139) donde el espectro se utiliza para otros fines, como el radar de aeropuertos civiles y el radar meteorológico. Para evitar interferencias con esos sistemas, el punto de acceso (AP) debe operar a la potencia máxima especificada por estos campos de restricción.
- El estándar **`802.11h`** es una extensión del estándar IEEE 802.11 que se enfoca en la implementación de mecanismos de mitigación de interferencias, gestión dinámica de canales y mejoramiento de la coexistencia de redes inalámbricas.
- El objetivo principal del **`802.11h`** es permitir una operación más eficiente y confiable de las redes Wi-Fi en entornos donde se comparte el espectro con otros sistemas, como el radar de aeropuertos y otras aplicaciones gubernamentales.

### Disponible en Frames:

- `Beacons`
- `Probe Requests`
- `Association Request`

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/19af10d1-2e74-42b0-abc6-d665f0e757b4)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 15 - `Channel Switch` - 6 byte

### BlackShark Filter:

````py

````

---

### Descripción:

- Esto también está relacionado con el estándar **`802.11h`**. 
- Cuando se detecta una explosión de radar, todas las estaciones deben abandonar el canal afectado. El punto de acceso (AP) puede configurarse para anunciar a la célula cuál será el siguiente canal.

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 16 - `Quiet` - 8 byte

### BlackShark Filter:

````py

````

---

### Descripción:

- Otro elemento relacionado con el estándar **`802.11h`**. 
- Permite que un punto de acceso (AP) solicite un tiempo de silencio durante el cual ninguna estación debe transmitir con el fin de realizar pruebas en el canal para detectar la presencia de radares.

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

 ## 17 - `IBSS DFS` - _Variable_

### BlackShark Filter:

````py

````

---

### Descripción:

- Utilizado con el estándar **`802.11h`** en una red de Servicio Básico Independiente (IBSS, por sus siglas en inglés).

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 18 - `TPC Report` - 4 byte

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 32

### Lenght
wlan.tag.length == 1

---

### Local Power Constraint
wlan.powercon.local == 0
````

---

### Descripción:

- Este elemento también está relacionado con el estándar **`802.11h`**. 
- El elemento `Transmit Power Control (TPC) Report` (Informe de Control de Potencia Transmitida, por sus siglas en inglés) contiene información sobre la `Transmit Power` & `Link Margin`, y generalmente se envía en respuesta a un `TPC Request` transmitida. 

### Disponible en Frames:

- `Beacons`
- `Probe Requests`
- `Probe Responses`
- `Association Request`
- `Association Response`

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/b7898423-3f88-474d-9d80-84e005cb9cee)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 19 - `ERP Information` - 3 byte

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 42

### Lenght
wlan.tag.length == 1

---

### ERP info
wlan.erp_info == 0x00

### ERP bit present or not (T-Shoot hot papi, set to 1)
wlan.erp_info.erp_present == 0

### Use Protection
wlan.erp_info.use_protection == 0

### Barker Preamble Mode
wlan.erp_info.barker_preamble_mode == 0

### Reserved
wlan.erp_info.reserved == 0x00
````

---

### Descripción:

- El elemento ERP "Enhanced Rate PHY" o "Física de Tasa Mejorada" consta de 3 bytes y **está presente solo en redes de 2.4 GHz que admiten 802.11g**. 
- Se refiere a un conjunto de mejoras y modificaciones introducidas en el estándar 802.11 para admitir tasas de datos más altas y una mayor eficiencia en la transmisión de datos. 
- El modo ERP permite tasas de datos más altas, como las especificadas en el estándar 802.11g, que utiliza modulación OFDM en comparación con las tasas más bajas del estándar 802.11b, que utiliza modulación DSSS.  
- La capa física ERP se utiliza en redes Wi-Fi que admiten el estándar 802.11g y permite tasas de datos más rápidas y una mayor capacidad de transmisión.
 
Cuando el bit `no-ERP_Present` se establece en `1` en las siguientes condiciones:

1. Una estación no-ERP (802.11 heredado o 802.11b) se asocia a la celda.
2. Se detecta una celda vecina que permite solo tasas de datos no-ERP.
3. Se recibe cualquier otro marco de administración (excepto solicitud de sondeo) de una célula vecina que admite solo tasas de datos no-ERP.

### Disponible en Frames:

- `Beacons` _solo 2.4 GHz_
- `Probe Response` _solo 2.4 GHz_

### Fz3r0 Troubleshooting Tip!!!:

**Filtrar estos beacons con `1` permite saber si hay alguna red alrededor soportando legacy, lo que puede significar data rates reducidos u otras singularidades. Por ejemplo, redes sin `OFDM Only` con un dispositivo/cliente que esté utilizando 802.11b DSSS está asociado a ese AP**

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a1a59a93-2904-4930-983e-8e95e41f8691)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 20 - `Extended Supported Rates` - _Variable_

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 50

### Lenght
wlan.tag.length == 4

---

### Extended Supported Rate = 6 Mbps
wlan.extended_supported_rates == 0x0c

### Extended Supported Rate = 9 Mbps
wlan.extended_supported_rates == 0x12

### Extended Supported Rate = 12 Mbps
wlan.extended_supported_rates == 0x18

### Extended Supported Rate = 48 Mbps
wlan.extended_supported_rates == 0x60
````

---

### Descripción:

- El elemento Extended Supported Rates (Tasas de Soporte Extendidas) especifica las tasas de datos admitidas que no se incluyen en el elemento Supported Rates (Tasas Admitidas).
- Solo es necesario si hay más de 8 tasas de datos admitidas en la red. 
- Este elemento se utiliza para proporcionar información adicional sobre las tasas de datos que son compatibles con la red, pero que no se incluyeron en el elemento Supported Rates debido a limitaciones de espacio.

### Disponible en Frames:

- `Beacons`
- `Probe Requests`
- `Probe Responses`
- `Association Request`
- `Re-Association Requests`
- `Re-Association Response`

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/eee57624-cf29-4225-8fd7-3127afb70cf5)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 21 - `RSN Information` - 8 byte

### BlackShark Filter:

````py
### Tag Number
wlan.tag.number == 48

### Lenght
wlan.tag.length == 20

---

### RSN Version
wlan.rsn.version == 1

### Group Cipher Suite Type
wlan.rsn.gcs.type == 4

### Pairwise Cipher Suite Type
wlan.rsn.pcs.type == 4

### Authentication Key Management (AKM)
wlan.rsn.akms.type == psk
wlan.rsn.akms.type == 2

---

### RSN Capabilities
wlan.rsn.capabilities == 0x0000

### RSN Pre-Auth Capabilities
wlan.rsn.capabilities.preauth == 0
````

---

### Descripción:

- El campo RSN (Robust Secure Network) contiene información relacionada con la seguridad y la autenticación de la red.
- Este campo proporciona detalles sobre los **cifrados utilizados, los algoritmos de autenticación admitidos y otras capacidades relacionadas con la seguridad de la red.**
- En un beacon, el campo RSN permite a los clientes y otros dispositivos obtener información sobre las medidas de seguridad implementadas en la red Wi-Fi.

---

### Disponible en Frames:

- `Beacon`
- `Probe response`
- `Association request`
- `Association response` 
- `Reassociation request` 
- `Reassociation response` 
- `Authentication`
- `Deauthentication`
- `Disassociation`

### Ejemplo 1 - `WPA2 - AES - PSK`:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/f4b7d5be-f468-4570-ae99-c527e5f833ec)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 22 - `QBSS Load Element 802.11e` - _Variable_

### BlackShark Filter:

````py

````

---

### Descripción:

- Este elemento se utiliza solo cuando se admite QoS y a menudo se denomina elemento de carga QBSS.
- Proporciona información sobre la carga de la celda desde el punto de vista del punto de acceso (AP).

Tiene los siguientes subcampos:

1. `Station Count`: Cuántas estaciones están actualmente asociadas.
2. `Channel Utilization`: Porcentaje de tiempo que el AP percibió que el medio estaba ocupado (normalizado de 0 a 255).
3. `Available Admission Capacity`: Indica la capacidad disponible para admitir nuevas estaciones en la celda BSS.
 
Ejemplo de Admission Capacity:

````py
## Resultado de Ejemplo
available admission capacity: 23437 [*32us]
````

- El valor 23437 representa la cantidad de unidades de tiempo disponibles, y se multiplica por 32 microsegundos (32us). 
- Esto significa que **la capacidad de admisión disponible en la célula BSS es de `23437` * `32us` = `749,984 microsegundos`**.
- Este valor se utiliza para determinar la cantidad de tiempo disponible para admitir nuevas estaciones en la célula BSS.<br><br>
    - **Cuanto mayor sea este valor, más capacidad habrá disponible para aceptar nuevas conexiones. Es un indicador importante para gestionar el acceso y la capacidad de la red inalámbrica.**

Estos subcampos brindan información valiosa sobre la carga y la capacidad del punto de acceso y pueden ser utilizados por los dispositivos cliente para tomar decisiones relacionadas con la selección de la red y la asignación de recursos."

---

### External Info & Labs

- [Cisco - QBSS Load element](https://dot11zen.blogspot.com/2017/04/qbss-load-element_5.html)

---

### Fz3r0 Troubleshooting Tips!

- **Este campo es muy útil para hacer troubleshooting de airtime utilization y capacidad en el AP.**
- Se pueden llegar a detemrinar problemas de interferencia o alta utilización en el AP, por ejemplo, por muchos clientes conectados y utilizando el medio. 

---

### Linux

- Comando `iw`
````sh
# Linux QBSSS Load Element 802.11e
sudo iw dev wlp3s0 scan
````

---

### Fz3r0 QBSSS Scripts

1. `batch script`

````bat
@echo off

rem '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
rem '                                                                                                        '
rem '                        Fz3r0 - Wireless 802.11 (Wi-Fi) AirTime Calculator v1.0                         '
rem '                                                                                                        '
rem '    Github :  Fz3r0                                                                                     '
rem '    Twitter: @Fz3r0_OPs                                                                                 '
rem '    Youtube: @Fz3r0_OPs                                                                                 '
rem '                                                                                                        '
rem ' Instrucciones:                                                                                         '
rem '                                                                                                        '
rem '     1. En un Frame Capture 802.11 donde se esté analizando un Beacon, buscar el Tagged Parameter:      '
rem '        QBSSS Load Element 802.11e                                                                      '
rem '                                                                                                        '
rem '     2. Dentro de este elemento se podrá encontrar el campo "Channel Utilization" que da un valor 0-255 '
rem '        Filtro: wlan.qbss.cu                                                                            '
rem '                                                                                                        '
rem '     3. Insertar el valor entre 0 y 255 que da el valor de wlan.qbss.cu en el programa                  '
rem '        Filtro: wlan.qbss.cu                                                                            '
rem '                                                                                                        '
rem ' Troubleshooting Hint:                                                                                  '
rem '                                                                                                        '
rem '     -  En caso que el resultado sea alto & con POCAS estaciones asociadas:                             '
rem '     >  Normalmente es por interferencia Wi-Fi (o no WI-FI)                                             '
rem '                                                                                                        '
rem '     -  En caso que el resultado sea alto & con MUCHAS estaciones asociadas:                            '
rem '     >  Normalmente es por capacidad al limite del AP                                                   '
rem '                                                                                                        '
rem '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'

rem Titulo:
echo.                                                     
echo.   
echo Fz3r0 - Wireless 802.11 (Wi-Fi) AirTime Calculator v1.0
echo.  
echo Github :  Fz3r0
echo Twitter: @Fz3r0_OPs
echo Youtube: @Fz3r0_OPs
echo. 
echo.  

setlocal enabledelayedexpansion

:inicio
rem Solicitar al usuario que ingrese el valor del airtime utilization
set /p utilization=Ingresa el valor entre 0 y 255 obtenido en el QSS Load Element 802.11e (Channel Utilization): 
echo.

rem Validar que el valor ingresado esté dentro del rango válido
if %utilization% LSS 0 (
    echo El valor ingresado esta por debajo del rango valido.
    echo.
    goto :preguntar_repetir
)
if %utilization% GTR 255 (
    echo El valor ingresado esta por encima del rango valido.
    echo.
    goto :preguntar_repetir
)

rem Calcular el porcentaje del airtime utilization
set /a percentage=(%utilization% * 100) / 255

rem Mostrar el resultado al usuario
echo El airtime utilization es: !percentage!%%
echo.

:preguntar_repetir
rem Preguntar al usuario si desea ingresar otro valor
set /p repeat=?Deseas ingresar otro valor? (S/N): 
echo.

rem Validar la respuesta del usuario
if /i "%repeat%"=="S" (
    goto :inicio
) else if /i "%repeat%"=="N" (
    echo Adios. 
    echo.
    pause
    exit
) else (
    echo Respuesta invalida. Por favor, ingresa S para si o N para no.
    echo.
    goto :preguntar_repetir
)
````

- PoC:

<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/4dea8353-0745-4253-8513-c805fa35b288" alt="center" height=500px/></a></p> 

---

### Disponible en Frames:

- `Beacon`

---

### Ejemplo 1 - Low Utilization & Few Clients:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/aef2aa18-50d4-4875-9ae4-943fb4ddfbad)

---

### Ejemplo 2 - 2.4 & 5 GHz example | same AP & same time

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/50d1ff83-36d7-451b-a7e4-718ea7eddeee)

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/44057770-ad2b-4311-9c50-62121d6da692)

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/616023a3-b65f-46b5-b338-75baa6d7f75d)

- **[PCAP - Channel/AirTime Utilization 2.4 & 5 GHz same time](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11809173/Captura_Airtime_channel_utilization.zip)**

#### 2.4 GHz - SSID `FULL clientes` | `Fz3r0 AP`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/515fe5d0-4212-413e-bda8-c263d38054b3)
<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/2bab65ed-4f61-4170-84eb-d46e3af5d259" alt="center" height=220px/> </a></p> 
####  5 GHz - SSID `FULL clientes` | `Fz3r0 AP`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/2f296289-ac69-492f-ae32-e70768435649)
<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/b3684f40-6643-4f88-9378-27d7344f2319" alt="center" height=220px/></a></p> 


####  5 GHz - SSID `vacío de clientes & oculto` | `Fz3r0 AP`

En esta captura se puede ver un contreo de `0 STA` & `19% de Airtime/Channel Utilization`. Esto debido a que el otro SSID es quien está ocupando ese aire en esa celda. 

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a6bfb7d6-f271-4140-8af3-e282031b1c6b)
<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a14ce244-7425-46e3-bc2d-bc238a8c731a" alt="center" height=220px/></a></p> 

#### Resultados

- Si se comparan por ejemplo los 2 Beacons de 5 GHz donde uno tiene `0 clientes` y el otro tiene `87 clientes` se puede ver que ambos tienen exactamente el `mismo utilization`.
- Esto es debido a que ambos utilizan la misma celda y el mismo aire!!! He ahí la respuesta!:<br><br>

    - **A pesar que un SSID tenga 0 clientes, al compartir la celda con un SSID en el mismo canal que tiene 87 clientes, también es afectado por ese `AirTime/Channel Utilization`!!!** :


<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/f204e243-e648-4404-b72c-4a37f8630114" alt="center" /> </a></p> 
<p align="center"> <img src="https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/43a666af-e6f2-4302-a2da-bbd567602db5" alt="center" /> </a></p> 


---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## `Supported Rates` - 8 byte

### BlackShark Filter:

````py

````

---

### Descripción:

- 

### Disponible en Frames:

- 

### Ejemplo:














































































Extended Capabilities:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/e9405321-e517-418a-89ea-45447ffac973)





































































---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## `Supported Rates` - 8 byte

### BlackShark Filter:

````py

````

---

### Descripción:

- 

### Disponible en Frames:

- 

### Ejemplo:










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
