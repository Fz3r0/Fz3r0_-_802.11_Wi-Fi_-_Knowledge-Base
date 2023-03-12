<!-- 

Y ARRANCAN!!!


<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# El camino al `CWAP-402`: <br> `Certified Wireless Analysis Professional` 📡🔍🦈  
_Writeup para la certificación **CWAP-402** de **CWNP (Certified Wireless Network Professional)**_ <br>
_por @ **Fz3r0** 💀 (CWNA)_

## Conocimiento Requerido para `CWAP-402`

- El examen está dividido de la siguiente manera:

| **Conocimiento CWAP**         | **Porcentaje** |
|:-----------------------------:|:--------------:|
| **Protocol Analysis**         | 15%            |
| **Spectrum Analysus**         | 10%            |
| **PHY Layers & Technologies** | 10%            |
| **MAC Sublayers & Functions** | 25%            |
| **WLAN Medium Access**        | 10%            |
| **802.11 Frame Exchanges**    | 30%            |

## `CWAP`: Objetivos

- El Ingeniero CWAP debe asegurarse que el troubleshooting se está llevando a cabo con todos los tipos de anlálisis y poder realizar los siguientes pasos:

1. Definir el problema
2. Determinar la escala del problema 
3. Identificar las posibles causas
4. Capturar y Analizar los datos
5. Observar el problema
6. Seleccionar los pasos apropiados para remediar el problema
7. Documentar el problema y resolución 

- El Ingeniero CWAP debe ser experto en aplicar y comprender los conocimientos respecto a los **PHY Technologies** como son: `PHY headers`, `Preambles`, `Training Fields`, `Frame Aggregation`, `Data Rates`, etc.
- Entender por completo el `Frame` y `Frame Aggregation`
 
     - Frame Aggregation: `A-MSDU` & `A-MPDU` 

## `CWAP`: Modelo OSI _(usado en el libro)_

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223612406-8d8a9825-2405-4f88-927b-fe767d8b0973.png" alt="Modelo OSI"/> </a> </p> 

### 💀 `Fz3r0 Pro Tip:`

- `Layer 1`, `Layer 2`, `Layer 3` y `Layer 4` son los importantes y donde ocurre la magia en Networking
- `Layer 5`, `Layer 6`, y `Layer 7` están fuera del alcance del CWAP.
- Los estándares `IEEE 802.3 (ethernet / cableado)` y `802.11 (wireless / aire)` operan primariamente en `Layer 1` & `Layer 2`. 
- Los estándares `IETF` de los protocolos `TCP/IP` operan primariamente en `Layer 3` (Direccionamiento `IPv4/IPv6`) & `Layer 4` (Segmentación `TCP / UDP`)
- `Layer 1` & `Layer 2` son las capas principales en las que se enfoca el `CWAP` (Ya que el WiFi es donde funciona realmente 😉) 

---

### 💀 `Fz3r0 Bonus`: Upper Layers Basic Knowledge

- [ICND1 - **Layers 5-7** - The Upper Layers](https://youtu.be/vfRL4n1vxyE)
- [`WireShark Analysis`: **Layer 5 Session**](https://www.youtube.com/watch?v=ORR3tAAz4F4)
- [`WireShark Analysis`: **Layer 6 Presentation**](https://www.youtube.com/watch?v=qnEFsoz-cwQ)
- [`WireShark Analysis`: **Layer 7 Application**](https://www.youtube.com/watch?v=L_wLexApMkA)
- [`File Formats` & `Magic Numbers`](https://youtu.be/qm33nCV1nkA) 

## Funcionamiento de los Layers

- Se dice que cada Layer sirve hacia el Layer de arriba y abajo de él, excepto por las 2 Layers finales (que ya no tienen nada antes/después): `Layer 1 (capa final de transmisión)` & `Layer 7 (capa final de recepción)`
- Mientras los datos se mueven por las capas del Modelo OSI, se van `encapsulando` y `decapsulando`

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223029707-a67719fd-de81-407c-97d0-7c118cbf9b80.png" alt="Modelo OSI" height=520px/> </a> </p> 

---

### `Encapsulation` & `Decapsulation`

- `Encapsular` es simplemente un `append` o `preppend` (poner antes o después) de bits de datos adicionales a los paquetes que vienen de capas superiores. 
- `Decapsular` es lo contrario, una vez que el paquete se envía a las capas superiores. 
- Es una técnica utilizada por protcolos por capas (layers) para cargar protocolos ajenos de esa capa particular en una red. 
- Por ejemplo, Layer 2 encapusla los datos que vienen de arriba en Layer 3, 4, 5, 6 o 7... sin necesidad que esa capa los "entienda", así los puede transmitir por un medio físico sin importar que los datos sean por ejemplo: un mensaje de whatsapp, una transmisión ssh o una partida de Street Fighter VI. 

    - Si los datos se mueven de `Arriba (Layer 7)` hacia --->>> `Abajo (Layer 1)` los datos se `encapsulan`
    - Si los datos se mueven de `Abajo (Layer 1)` hacia --->>> `Arriba (Layer 7)` los datos se `decapsulan`

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223026259-b2f1cd67-9dba-4a2a-b76b-8e99d2a54242.png" alt="Encapsula" height=418px/> </a> </p> 

<span align="center"> <p align="center"> ![image](https://user-images.githubusercontent.com/94720207/223026368-7c497884-9f6f-489b-9fe6-ab46fc521b01.png) </p> </span> 

### `Append` y `Prepend`

- Un `append` y `prepend` (por ejemplo en el sublayer superior de capa 2 `llc`), se refiere al hecho de que, en algunos casos, los datos que se transmiten a través de la red pueden tener información de control adicional agregada por capas superiores del modelo OSI, incluyendo su `payload` (data)
- El `append` se refiere a agregar esta información de control al `final` del paquete de datos. 
- El `prepend` se refiere a agregar esta información de control al `principio` del paquete de datos.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223307931-405fc7e5-1474-4c24-a4d0-60f6e0faa451.png" alt="Encapsula" height=175px/> </a> </p> 

### 💀 `Fz3r0 Pro Tip:`

- Por ejemplo, el `FCS` es un campo que se agrega **al final de una trama** en la mayoría de los protocolos de red, incluido Ethernet y WiFi. 
- Por lo tanto, FCS se agrega típicamente `al final de una trama`. 
- El propósito de FCS se verá más adelante a fondo, pero en resumen: 
- Permite que el `dispositivo receptor` **verifique** si la trama se ha corrompido durante la transmisión. 
- El dispositivo receptor puede utilizar FCS para determinar si ocurrieron errores durante la transmisión y, en caso afirmativo, la trama se descarta.

### ⚠️ **`CWAP Definition`** ⚠️ 

- `Encapsulation` - Is the process of of **prepending and/or appending information to a message for `transmission`** (communication) `TO a peer`.
- `Decaspulation` - Is the process of **reading, processing and removing prepended and/or appended information for `reception`** (communication) `FROM a peer`.

## `Frames`: En `Layer 1` y `Layer 2`

- [IEEE `802.11 Frame` Format vs. IEEE `802.3 Frame` Format](https://dot11ap.wordpress.com/ieee-802-11-frame-format-vs-ieee-802-3-frame-format/)
- [Difference between Ethernet and Wi-Fi @ `Sunny`](https://www.youtube.com/watch?v=Uyrun_ZB3EE)
- Los Frames son paquetes de datos que vienen de capas superiores en el modelo OSI.
- A estos paquetes se les agrega al principio o al final `append / prepend` frames para poder realizar su **trasnmisión en el medio local**. 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223580792-368e0582-1170-4b24-ad31-812aa5aa7912.png" alt="Encapsula" height=165px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223580827-9a0f5347-fcfa-4a52-a884-c20bef35b568.png" alt="Encapsula" height=170px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223580395-cd80622a-5239-4151-8cf0-fbd77cf0a12a.png" alt="Encapsula" height=427px/> </a> </p> 

### Layer 1: `Physical Layer Frame`

- En `Layer 1 (Physical Layer)`, un frame se refiere a un `conjunto de bits` que se transmiten en la red en una única transmisión. 
- Estos bits se organizan en un formato específico para que puedan `ser enviados a través de medios físicos como cables, fibra óptica o ondas de radio`. 
- El formato de estos bits se llama `Physical Layer Frame`.

### Layer 2: `Data Link Layer Frame`

- En `Layer 2 (Data Link Layer)`, un frame se refiere a un `paquete de datos` que se transmite entre dispositivos de red en una red local. 
- Este paquete de datos incluye `información de control adicional`, como `direcciones de origen y destino`, que permiten que los dispositivos de red se comuniquen entre sí de manera efectiva. 
- El formato de estos paquetes se llama `Data Link Layer Frame`.

## `Layer 4` Transport

- La Capa 4 del modelo OSI es la capa de transporte, y su función principal es proporcionar un medio para que los procesos de aplicaciones en diferentes dispositivos puedan establecer, mantener y terminar conexiones de comunicación. 
- En esta capa se encuentran **2 protocolos principales**: `TCP` y `UDP`.

    - `Propoprcionar un Medio (Lógico)` _(Hablando de la capa 4 de transporte)_: Similar a un cable (medio físico), la capa de transporte utiliza un medio pero a nivel de software (lógico) para transmitir datos.
    - Este medio en realidad son un conjunto de servicios y protocolos que permiten a los procesos de aplicaciones en diferentes dispositivos establecer y gestionar una conexión de comunicación extremo a extremo.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223029378-5c82410f-0388-4e63-8fe1-1c968da26008.png" alt="Transport" height=300px/> </a> </p> 

### `TCP` - Transmission Control Protocol

- `TCP`: Protocolo orientado a conexión y confiable. `Connection-oriented and Reliable`
- Proporciona un canal de comunicación extremo a extremo que garantiza que los datos enviados sean recibidos en el orden correcto y sin errores `ACK`, `Checksum`, `Seq`, etc. 
- Para lograr esto, TCP establece una conexión entre dos dispositivos antes de enviar datos `3-way-handshake`. 
- Los datos se envían en segmentos y se espera que el receptor confirme la recepción de cada segmento. 
- Si un segmento no se recibe correctamente, TCP lo retransmite hasta que el receptor lo confirma. 
- TCP también controla la tasa de transmisión para evitar la congestión de la red.

### `UDP` - User Datagram Protocol

- `UDP`: Protocolo sin conexión y no confiable `Connectionless and Unreliable`. 
- No establece una conexión antes de enviar datos y no proporciona garantías de que los datos sean recibidos correctamente o en el orden correcto `No tiene ACK, Cheksum, etc` _(Algunos pueden llegar a traer Seq)_. 
- Los datos se envían en datagramas, y no hay confirmación de recepción ni retransmisión de paquetes perdidos. 
- UDP es útil para aplicaciones en las que la velocidad es más importante que la confiabilidad, como en la transmisión de audio o video en tiempo real.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223545373-28bf556f-62da-40fd-85fd-3a7290f0815c.png" alt="TCP vs UDP" height=340px/> </a> </p> 

### 💀 `Fz3r0 Pro Tip:` TCP (Unicast) & UDP (Mulitcast & Broadcast)

- `TCP` se usa para la transmisión de datos confiables que deben entregarse en orden y solo admite la transmisión `unicast` a un `único destinatario`.
- `UDP` se usa comúnmente para la `transmisión de datos en tiempo real` que pueden tolerar la pérdida de paquetes, y admite `multicast` y `broadcast` para enviar datos a múltiples destinatarios.
- No necesariamente todos los protocolos de `UDP` son `multicast` o `broadcast`, de hecho también permite `unicast`.
- Por ejemplo un paquete `ARP` es un protocolo `UDP` que llega a todos los clientes dentro de la misma red como `broadcast`.
- Pero una llamada telefónica por internet utiliza el protocolo `UDP` de manera `unicast` (punto-a-punto)

#### El ejemplo de `Whatsapp`

- `WhatsApp` utiliza tanto `TCP` como `UDP` para la `transmisión de datos`, **dependiendo del tipo de datos que se estén transmitiendo.**

    - Por ejemplo, cuando envías un `mensaje de texto`, se utiliza `TCP` para la transmisión de datos. 
    - `TCP` se utiliza para garantizar que los datos se entreguen correctamente y en orden, lo que es importante para asegurar que los mensajes de texto se entreguen de manera confiable.
    - Por otro lado, cuando realizas una `llamada de voz o video`, se utiliza `UDP` para la transmisión de datos. 
    - La transmisión de voz y video en tiempo real **no requiere la misma garantía de entrega confiable que un mensaje de texto**, por lo que se utiliza `UDP` para minimizar la latencia y permitir una comunicación en tiempo real.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223623288-52bb135f-3685-409c-9029-1745c04aa2b2.png" alt="TCP vs UDP" height=240px/> </a> </p> 




### Otros protocolos Layer 4

- Además de TCP y UDP, hay otros protocolos de transporte en la Capa 4 del modelo OSI, como: 
    - `SCTP` (Stream Control Transmission Protocol): similar a TCP pero se utiliza para aplicaciones de tiempo real y en redes móviles
    - `DCCP` (Datagram Congestion Control Protocol): similar a UDP pero con mecanismos para evitar la congestión de la red.

## `Layer 3` Network

- La Capa 3 del modelo OSI es la capa de red, y su función principal es proporcionar servicios para enrutar los paquetes de datos a través de la red desde el origen al destino. 

    * `Origen(IP) <---> Destino(IP)`

### `IP` - Internet Protocol

- En esta capa se encuentra el protocolo de Internet (IP) `IP (Internet Protocol)`, que es el protocolo principal utilizado en Internet para enrutar paquetes entre dispositivos.
- Los paquetes de datos se envían en forma de datagramas, y cada datagrama incluye la `IP Address` del dispositivo de `origen` y del dispositivo de `destino`. 
- La dirección IP se utiliza para enrutar el datagrama a través de la red.
- El protocolo de Internet versión 4 `IPv4` es el protocolo de red más utilizado en la actualidad. 
- IPv4 utiliza direcciones de 32 bits para identificar los dispositivos en la red. 
- Sin embargo, debido a la cantidad limitada de direcciones IPv4 disponibles, se ha desarrollado un nuevo protocolo de Internet versión 6 `IPv6` que utiliza direcciones de 128 bits para permitir un mayor número de dispositivos en la red.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223030711-14388bc0-b4b9-43ea-9645-ec7c02c65722.png" alt="TCP vs UDP" /> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223030667-0e798b26-03da-48b1-97e9-5e5050eee172.png" alt="TCP vs UDP" /> </a> </p> 

#### El ejemplo de `Sony - Osaka Japón`

- Por ejemplo si hago un `trace route` hacia un servidor de `Sony` en `Osaka Japón` mi tráfico debe hacer varios `hops` por diferentes `routers`.
- Sería impráctico e inseguro que el `payload/datos` se tengan que desencapsular en cada uno de estos `hops`.
- En cambio, el pasar por un `router` que de hecho se considera un `dispositivo layer 3`, entonces hasta ahí se `desencapsula` para volver a `encapsular` hacia layers inferiores.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223628375-b3beb844-e855-413b-941f-78f76a90cee6.png" alt="TCP vs UDP" /> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223629553-d9f562d8-7a7e-4e4d-9f53-850f8ee270de.png" alt="TCP vs UDP" height=270px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223630137-b56e4cad-fa9e-403c-ba13-b3946b5cf083.png" alt="TCP vs UDP" /> </a> </p> 


### Otros

- Además de IP, hay otros protocolos de la Capa 3 en el modelo OSI, como ICMP (Internet Control Message Protocol), que se utiliza para enviar mensajes de error y de control entre dispositivos en la red, y IGMP (Internet Group Management Protocol), que se utiliza para gestionar grupos de dispositivos que desean recibir un flujo de datos en multicast.

## `Layer 2` Data Link

- [Extreme Networks @ Layer 2 – the Data Link Layer](https://youtu.be/B0Uf3uojpv0)
- La Capa 2 del modelo OSI es la capa de enlace de datos, y su función principal es proporcionar servicios para la transmisión fiable de datos entre dispositivos en la misma red física. 

    * `Origen(MAC) <---> Destino(MAC)`

- Tanto WiFi como Ethernet (inalámbrico y alámbrico) utilizan la Capa 2 de manera similar
- La principal diferencia entre Ethernet y Wi-Fi en la Capa 2 es la forma en que los datos se transmiten a través del medio físico (aire o cables).

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223143142-42e11745-b223-4637-93af-0e5238f4ffcd.png" alt="TCP vs UDP" height=320px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223142755-ec76569c-f874-4dda-979e-95bd53ce1929.png" alt="TCP vs UDP" height=330px/> </a> </p> 

- `Layer 2 - Data Link (Enlace de Datos)` se divide en `2 sublayers`: 

    1. `LLC - Logical Link Control` = Capa de Control de Enlace Lógico `UPPER`
    2. `MAC - Medium  Access Control` = Capa de Control de Acceso al Medio `LOWER`

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223023395-805f7429-af91-4920-b38d-866cab8046ba.png" alt="TCP vs UDP" height=400px/> </a> </p> 

---

### Layer 2: `LLC` - Logical Link Control `Upper Sublayer` - `802.2`

- El protocolo de control lógico (LLC) es el protocolo que proporciona un `enlace de comunicación entre la Capa 2 y la Capa 3`.
- El LLC se encarga de proporcionar servicios de control de enlace de datos a la capa de red superior y garantizar que la información se transmita de manera confiable entre dos dispositivos de red (Por ejemplo, PC-A y PC-B en una red ethernet cableada).
- La subcapa LLC proporciona servicios para la comunicación entre dispositivos en diferentes redes lógicas. 
- Proporciona un mecanismo para multiplexar y desmultiplexar diferentes protocolos de la Capa 3 (como IPX, TCP, etc.) en la misma red física (como el cable que usa ethernet, o el aire que usa WiFi). 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223464477-b3c49e23-d208-493c-a8fc-1d79c73ef37e.png" alt="Fz3r0 llc" height=370px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223485061-0c34d8a0-0ae0-4156-ae94-a7964522a016.png" alt="Fz3r0 llc" height=210px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223311481-6e5e391b-d28c-403d-8384-492f018be840.png" alt="Fz3r0 llc" /> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223555349-76ae229e-c0b6-486d-9f54-bce4573d65fd.png" alt="Fz3r0 llc" height=410px/> </a> </p> 

#### `Multiplexación` y `desmultiplexación`

- La multiplexación es la capacidad de la Capa 2 de Enlace de Datos para combinar varios flujos de datos que vienen de de la Capa 3 (como por ejemplo, diferentes protocolos de red) en un solo flujo de datos que se transmite a través de un único medio físico compartido (como un cable o el aire), y luego separarlos nuevamente en la Capa 2 del otro extremo.
- En palabras más sencillas: 

    - Es una manera de convertir "datos digitales de computadora" que tienen como `origen: PC-A` a "pulsos eléctricos, ondas de radio, etc" que `pasan por un cable o el aire`, y luego volverlos a convertir a "datos digitales de computadora" los cuales recibe el `destino: PC-B`. Aunque en realidad es algo un poco más complejo, esa es la idea principal. 

- `Nota`: Ethernet es una tecnología de red cableada que utiliza un cable para conectar dispositivos a una red. La tecnología Wi-Fi, por otro lado, es una tecnología inalámbrica que utiliza ondas de radio para transmitir datos a través del aire.
    
#### `Ejemplo`: Multiplexación:
    
- En el caso de comunicaciones DSL, se utiliza la técnica de multiplexación por división de frecuencia (FDM) para combinar la señal de datos con la señal de voz en una señal única que se transmite a través del cableado de cobre. 
- Los datos se transmiten a través del medio físico en forma de pulsos eléctricos modulados utilizando técnicas de modulación de amplitud.

---

### Layer 2: `MAC` - Media Access Control `Lower Sublayer` - `802.3 (Ethernet)` & `802.11 (Wireless)`

- Este es el sublayer en el que más se enfoca el `CWAP`
- La subcapa MAC, proporciona servicios para la comunicación entre dispositivos en la misma red física.
- En esta capa se encuentran mecanismos como CSMA/CA y CSMA/CD para evitar colisiones.
- Esta subcapa permite crear un `local link`, que se refiere a la comunicación en la `red local (LAN)` utilizando `Layer 1` y `Layer 2`.
- El local link trabaja en Layer 1 y 2, pero trae el payload y los datos de las capas superiores para ser trasnmitadas.
- La MAC se define en el estándar IEEE 802.3 en caso de Ethernet y 802.11 en caso de WiFi.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223023071-19560cf8-3027-4be2-9496-80fe121a3775.png" alt="mac ofrmat" height=403px/> </a> </p> 

- Los `3 tipos de Frames` que principalmente se estudian en este curso y que forman el `MAC sublayer de 802.11` son:
1. **`Management Frames`**
2. **`Control Frames`**
3. **`Data Frames` / `QoS Data Frames`**

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223311147-d3127cac-05ec-4f5b-a290-4cf011504175.png" alt="mac ofrmat" height=360px/> </a> </p> 

## `Layer 1` Physical

- La capa física se encarga de la `transmisión de bits` a través de un `medio físico`. 
- La diferencia entre `Ethernet` y `WiFi` en esta capa es el `medio de transmisión` utilizado: `cableado` versus `inalámbrico`.
- Capacidades típicas de Layer 1 se encuentran:
1. `Encoding` & `Signaling`
2. `Modulation`
3. `Demodulation`
4. `Timing`
5. `Signal Processing`
6. otros...

---

### `Encoding` & `Signaling`

- El encoding (codificación) se refiere al proceso de `convertir los datos` de entrada en una `secuencia de bits` que se puedan transmitir a través del medio físico. - - En otras palabras, el encoding es la forma en que los datos se transforman para que puedan ser transmitidos en el medio de comunicación utilizado, ya sea un cable, fibra óptica o una señal de radio.
- Por ejemplo, se toman todos los datos ya encapusolados de todas las capas superiores y se transforman en pulsos eléctricos para viajar por el cable en el caso de ethernet. En caso de WiFi se convierte en ondas de radio que viajan por el aire. 
- `decoding` se refiere al proceso inverso 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223327865-2fc7626b-23b4-4bb1-a510-22ee19eb54db.png" alt="encoding" height=305px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/224503344-cd1e18f7-0442-4ed6-9205-5fb159e06507.png" alt="encoding" height=305px/> </a> </p> 




---

### `Modulation` & `Demodulation`

- La modulación es importante en la capa física porque permite la transmisión de información a través de medios de comunicación físicos, como cables o señales de radio. 
- La modulación también ayuda a mejorar la eficiencia y la velocidad de la transmisión de datos, al permitir la transmisión de una gran cantidad de información en una sola onda portadora.
- La modulación se utiliza para transmitir datos de un dispositivo a otro mediante la modificación de una onda portadora, que puede ser una señal eléctrica o electromagnética. 
- La `información se modula` en la `onda portadora` mediante la variación de alguna propiedad física de la onda, como su `Amplitude (amplitud)`, `Frequency (frecuencia)` o `Phase (fase)`.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223328544-aada1576-a6f9-4a16-a9b2-1d3640409f52.png" alt="encoding" height=345px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223328643-b5cbe71d-2d0f-4997-a5cf-c24baf2da84f.png" alt="encoding" height=340px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223328510-984e3a58-16dd-4428-b5da-ca1d83d9c2e4.png" alt="encoding" height=425px/> </a> </p> 

---

### `Timing Synchronization` (Timing)

- [Time Synchronization in Wireless Networks](https://www.cse.wustl.edu/~jain/cse574-06/ftp/time_sync/index.html)
- **En una transmisión WiFi, el `receptor` debe estar soncronizado con el `transmisor`**
- "Time Synchronization" o "Sincronización de Tiempo" se refiere al proceso de `sincronización del reloj entre los dispositivos inalámbricos` dentro de una red Wi-Fi.
- La sincronización de tiempo es esencial en las redes Wi-Fi para garantizar una transmisión de datos confiable y sin errores. 
- Cuando los dispositivos están sincronizados en tiempo, se asegura que los paquetes de datos se transmitan y reciban en el momento adecuado, y evita que los dispositivos transmitan en el mismo canal y en el mismo tiempo, lo que podría provocar colisiones y errores en la transmisión de datos.
- En las redes Wi-Fi, la sincronización de tiempo se realiza mediante un protocolo denominado `Wi-Fi Time Synchronization Protocol - WTS`. 
- Este protocolo permite a los dispositivos inalámbricos sincronizar sus relojes y establecer un intervalo de tiempo común para la transmisión y recepción de paquetes de datos.



<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223516228-0393f57b-74e4-4a8f-a8d2-add576ec21bd.png" alt="encoding" /> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223516131-3b4b8377-1be3-43ca-ae51-4f9a17c0b0cf.png" alt="encoding" /> </a> </p> 

---

### `Preamble` & `Training Fields`

- En `802.11 / WiFi` el `timing` se lleva a cabo utilizando `Preamble` & `Training Fields`
- El `Preamble` es una `secuencia de bits` que se utiliza para `sincronizar el reloj` de recepción del dispositivo receptor con el reloj de transmisión del dispositivo emisor. 
- Esto ayuda a garantizar que los bits de datos se transmitan en el momento correcto y se interpreten correctamente en el extremo receptor.
- Los `Training Fields` son una `serie de bits` que se utilizan para `ajustar la señal de transmisión en el receptor`. 
- Esto incluye la compensación de la atenuación de la señal y la eliminación de interferencias o ruido en la señal de transmisión.
- Los `Training Fields` también ayudan al receptor a `detectar errores en la transmisión` y a `realizar correcciones` si es necesario.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223516976-b101676d-f484-4dd3-971f-d9e111c9ecfa.png" alt="encoding" /> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223570605-a13fd0bf-cd6e-49fe-ace8-e2f68b87a9e7.png" alt="encoding" /> </a> </p> 

- Ambos están diseñados para ayudar a mejorar el rendimiento y la confiabilidad de la transmisión inalámbrica de datos en Wi-Fi. 
- Están estrechamente relacionados con el timing o el tiempo de la señal de transmisión ya que la secuencia de bits del preámbulo y los campos de entrenamiento se transmiten en un patrón de tiempo específico que permite al receptor sincronizarse con la señal de transmisión y recibir los datos de manera precisa.

---

### `Signal Processing`

- El procesamiento de señal (Signal Processing) en Layer 1 del modelo OSI en Ethernet & Wi-Fi se refiere al conjunto de técnicas y algoritmos utilizados para la transmisión y recepción de señales de datos en el medio físico de la red.
    - En `Ethernet - 802.3`, el procesamiento de señal en Layer 1 se refiere a la `codificación` y `decodificación` de los `bits de datos` en `señales eléctricas` que se transmiten a través del `cable de cobre` o `fibra óptica`. 
        - Estas `señales son moduladas` en diferentes `frecuencias` para evitar interferencias y atenuaciones que puedan afectar la calidad de la transmisión de datos.
    - En `Wi-Fi - 802.11`, el procesamiento de señal en Layer 1 se refiere a la `modulación` y `demodulación` de las `ondas de radio` utilizadas para transmitir datos `a través del aire`. 
        - Esto implica la codificación y decodificación de los bits de datos en señales de radio de diferentes frecuencias y amplitudes que son transmitidas a través de la antena del dispositivo.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223568602-8cfe0fc5-2e93-4f6b-b17c-50588475c069.png" alt="encoding" height=285px/> </a> </p> 

## Layer 1: `Physical`

- La `subcapa PHY` comparte Layer 1 con la `subcapa MAC` en el modelo OSI.
- La `subcapa MAC` es responsable de la gestión del acceso al medio y del control de flujo en la capa física. 
- La `MAC` se encarga de garantizar que sólo un dispositivo pueda transmitir datos a través del medio físico a la vez, y que los datos se entreguen de manera segura y confiable.
- La `PHY` es responsable de la transmisión y recepción de datos a través del medio físico. Esto incluye la conversión de los datos digitales en señales analógicas (en el caso de la transmisión por cable) o la conversión de los datos digitales en señales de radiofrecuencia (en el caso de la transmisión inalámbrica).

### Layer 1: `MAC Sublayer - 802.11-2016` / (Antes: `PLCP` + `PMD`) `upper`

- **No es curioso que se **reptita en Layer 1 la misma sublayer que en Layer 2**: `MAC`**
- Es por eso que en Layer 2 la `MAC` es la `Lower Sublayer` mientras que en Layer 1 es la `Upper Sublayer`, en realidad es la misma y contiene la misma información. 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223585212-9e7fbe05-fb01-46eb-a172-ed06ead03631.png" alt="sublayers"/> </a> </p> 
  
### Layer 1: `PHY Sublayer - 802.11-2016` / (Antes: `PLCP` + `PMD`) `lower`

- [802.11 PHY – PPDU (2014)](https://mrncciew.com/2014/10/14/cwap-802-11-phy-ppdu/)
- Antes de 2016, la Physical Layer de la norma IEEE 802.11, se dividía en dos subcapas: 
1. `PLCP - Physical Layer Conversion Protocol` (Control de Enlace de Capa Física) 
2. `PMD - Physical Medium Dependent` (Dispositivo de Medios Físicos)
 
### `PLCP` & `PMD` (Legacy)

- Se encargaba de la gestión de la señal de transmisión en la capa física, mientras que el PMD se encargaba de la transmisión de la señal a través del medio físico, como el aire.
- En `2016`, se publicó una` nueva versión del estándar IEEE 802.11` conocida como `IEEE 802.11-2016`. 
- En esta versión, se simplificó la capa física eliminando la distinción entre el PLCP y el PMD y se los agrupó como una única subcapa, denominada `PHY` (Physical Layer) sublayer.
- La simplificación de la capa física permitió una mayor flexibilidad y eficiencia en la implementación de la norma Wi-Fi, ya que se eliminaron las restricciones que antes limitaban las opciones de diseño y los fabricantes de hardware y software. 
- También permitió una mayor interoperabilidad entre los dispositivos Wi-Fi de diferentes fabricantes y un mayor rendimiento en general.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223579886-5fe1c532-062b-450e-9a45-537b5b085deb.png" alt="encoding" height=325px/> </a> </p> 

---

### `PHY Sublayer` (802.11-2016 [Actual])

- Actualmente, la `PHY Sublayer` se encarga de lo que hacía antes el `PLCP` & `PMD`
- La `PHY` se encarga de agregar parámetros como los `trainging fields` que necesitan recibir las Estaciones receptoras `STA` para que procesen la transmisión correctamente. 
- Las `STA`receptoras usan la información del `PHY Header` para sincronizar sus radios al mismo `data rate` y así poder lograr recibir frames de `Data (802.11)` que es el `PHY payload`
- La `PHY` sublayer se encarga de la `transmisión y recepción de la señal` de datos a través del `medio físico`, como el `aire` en el caso de las redes inalámbricas. 
- Esta subcapa está diseñada para ser independiente del medio físico específico utilizado y **proporciona una interfaz estándar entre la capa física y la capa de enlace de datos, que se encuentra en el nivel 2 del modelo OSI**.
- La PHY sublayer contiene una serie de estándares y especificaciones técnicas que definen cómo se transmite la señal de datos a través del medio físico. Esto incluye ejemplos como: 
1. La codificación y modulación de los datos. 
2. La gestión del ancho de banda.
3. La gestión de la potencia de la señal.
4. Implementación de mecanismos de corrección de errores para garantizar la fiabilidad de la transmisión.
5. Otros...

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223601083-7bbb8add-e106-4ed9-b096-84da49a96b5a.png" alt="encoding" /> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223601578-3857ebdc-5cb8-4884-b244-86c002f586bd.png" alt="encoding" height=185px/> </a> </p> 

---

### 💀 `Fz3r0 Pro Tip`: ¿Qué es un`Payload`?

- En el contexto de las `redes informáticas` o `Networking`, `payload` se refiere al `contenido útil` o `información` que se transmite a través de la red. 
- En una `transmisión de datos`, el payload es la `parte de los datos` que contiene la información real que se envía, **`excluyendo` cualquier información adicional necesaria para enviar los datos, como los `headers`, `source`, `destination`, `FCS` y otros `metadatos/metadata`.** (Como los headers agregados en cada capa para la transmisión de datos 😉)
- Es decir, si por ejemplo quiero enviar una `foto.jpg` por `whatsapp`, lo importante en el envío es la foto después de todo... Eso es el `payload`!!!
- Sin embargo, para lograr enviar esta foto por la red, ese `payload` se debe segmentar, fragmentar, encapsular, encriptar, agregar headers, enviar por un medio físico como un cable o aire, etc, etc... 
- Cada proceso de pasar por layers y transmisión agrega metadata (bit adicionales de datos con información) para lograr la transmisión del `payload` original. 

![image](https://user-images.githubusercontent.com/94720207/223599815-51381029-f32b-44c9-93a5-9dabcaaaba24.png)


#### Payload en Seguridad Informática y Hacking

- El término `payload` se utiliza comúnmente en el contexto de la seguridad informática y el hacking porque, en muchos casos, los atacantes utilizan un `payload malicioso` para comprometer un sistema. 
- Es importante tener en cuenta el contexto en el que se utiliza el término para evitar confusiones y malentendidos.
- Un `payload malicioso` es un tipo de `código malicioso` diseñado para ser `ejecutado` en un sistema comprometido con el fin de llevar a cabo acciones maliciosas, como robo de datos, daños al sistema, etc.
- Esta confusión puede surgir porque el término `payload` se utiliza tanto en el contexto de la transmisión de datos legítima como en el contexto de los ataques cibernéticos maliciosos. 
    - Es decir... **Un payload puede ser tanto legítimo como una `foto.jpg` como lo puede ser un payload malicioso como una `Reverse Shell` usando `MSF Venom / Metasploit` ya que ambos es el "contenido de datos importante" viajando por el medio después de todo!!!**

---

### 💀 `Fz3r0 Pro Tip`: ¿Qué es un`Header` y  un `Footer`?

- En el contexto de la transmisión de datos en redes informáticas y en el modelo OSI, un `header` y un `footer` (también conocido como `trailer`) son dos componentes importantes de un paquete de datos.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223602287-09982459-bfe5-42e2-be0f-7e7e31968dbc.png" alt="encoding" height=185px/> </a> </p> 

### `Header`

- El header está `prepended` (puesto antes) de los datos que proceden de los upper layers. 
- El `header` es la parte del paquete de datos que **contiene información sobre el origen y el destino del paquete, así como información sobre cómo se deben procesar los datos en el paquete.** 
- El encabezado (`header`) **también puede contener información de control, como el número de secuencia o el tiempo de vida del paquete.**

![image](https://user-images.githubusercontent.com/94720207/223600032-ebdd85fa-ffdf-4a5a-a0c1-f5886c184905.png)

### `Footer`

- El `footer`, también conocido como `tráiler`, está `appended` (puesto después) del payload. 
- El contenido del `footer` generalmente contiene el resultado del `CRC` conocido como `FCS` (uno depende del otro)
- Es la parte del paquete de datos que se utiliza para `verificar la integridad de los datos que se están transmitiendo`. 
- El `tráiler/footer` suele contener un "código de verificación de redundancia cíclica" `Cyclic Redundancy Check - CRC`, que es un valor numérico que se calcula a partir de los datos que se están transmitiendo. 
- El `CRC` es un algoritmo utilizado para `detectar errores` en la transmisión de datos en redes de comunicación. 
- **El resultado del cálculo del algoritmo CRC se conoce como `FCS (Frame Check Sequence)`, que es el valor numérico utilizado para verificar la integridad de los datos transmitidos.**
- Cuando el paquete de datos llega a su destino, se calcula un nuevo valor CRC a partir de los datos recibidos y se compara con el valor CRC en el tráiler. Si los dos valores coinciden, esto indica que los datos se transmitieron correctamente.

![image](https://user-images.githubusercontent.com/94720207/223602974-c43aa55c-61b5-4d15-aa50-fdf8c4904752.png)

### 💀 `Fz3r0 Pro Tip:` ¿Que es `overhead`?

- `Overhead` se refiere a los `datos adicionales` que `se agregan a los paquetes` de red para `permitir la comunicación` y el `control del flujo de datos` a través de la red.
- Es decir, varios campos tanto de `header`, `footer` o incluso en `payload/data` puede existir `overhead`
- En el modelo OSI, los `protocolos de capa superior` (como `HTTP` o `SMTP`) `agregan datos a los paquetes` que se envían a través de la red... 
- Mientras que los `protocolos de capa inferior` (como `Ethernet` o `WiFi`) `agregan información adicional` para ayudar a que los paquetes se entreguen correctamente.
- Como se ha visto anteriormente, sin `overhead` los datos, segmentos, frames y bits no se podrían transmitir por la red. 
- Algunas veces la palabra `overhead` se confunde con algo malo... pero en realidad cualquier paquete transmitido por la red tiene `overhead`.
- En este sentido, la palabra `overhead` no tiene una connotación negativa en sí misma, pero puede afectar negativamente el rendimiento de la red si se agrega demasiado. 
- Un exceso de overhead puede disminuir la eficiencia de la red al consumir ancho de banda y reducir la velocidad de transferencia de datos.
- Esta caída de performance se debe a que los paquetes se hacen mas grandes, se necesita más tiempo, aire, ancho de banda, etc, etc... para completar la trasnmisión. 

![image](https://user-images.githubusercontent.com/94720207/224216682-69c67fa4-3113-42f1-91ba-ff662383e656.png)

![image](https://user-images.githubusercontent.com/94720207/224217527-a7e42d07-4b60-46df-8d99-314ecf541e09.png)


---

<br>
<br>

## 802.11 Standard Protocol

- **El estándar de protocolo IEEE 802.11 define a la `MAC` y la `PHY` para comunicaciones en una `LAN` utilizando `RF` como `medio de transmisión` (osea una `WLAN`).**
- Las enmiendas modernas de 802.11 incluyen soporte a redes `mesh` y otro métodos de comunicaciones `devide-to-device`
- Este estándar es utilizado por dispositivos como **computadoras, smartphones, y otros dispositivos para conectarse a `redes Wi-Fi.`**
- El estándar 802.11 especifica las `frecuencias de radio`, los` protocolos de acceso al medio`, los `mecanismos de autenticación` y `encriptación`, `y otros aspectos` necesarios para el funcionamiento de una red inalámbrica. 
- El estándar también define diferentes variantes, como `802.11a`, `802.11b`, `802.11g`, `802.11n`, `802.11ac`, `802.11ax`; cada una con **diferentes características y velocidades de transmisión de datos.**

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223910395-92a65b7d-d17f-4688-bf4c-1c220526f038.png" alt="encoding"/> </a> </p> 

## `Physical Layer` para la comunicación WiFi - `PHY`

- Comunmente se les llama simplemente `PHY` a las enmiendas que utilizan `métodos de modulación de radiofrecuencias (b/a/g/n/ac/ax)` para lograr la `interoperabilidad` de redes wireless.
- La mayoría soportan `2.4 GHz` & `5 GHz`, aunque algunas soportan `otras frecuencias` mas `altas` o `bajas`.
- Para que las `RF waves` (ondas de radiofrecuencia) sirvan como `carriers` de datos, los `wireless devices` utilizan `modulación` para ingresar `datos` a las ondas de radiofrecuencia. 

### `802.11` - `Modulation Methods` AKA `PHY`

- Durante el `CWNA` hice una tabla que me ayudó mucho a entender los `PHY`, `Ammandments`, `Standards`:
- Esta es la versión simplificada en .md: 

| **Nombre**     | **Acrónimo** | **Nombre Completo**                        | **Año** | **Banda(s)**          | **Bandwith**                               | **Max. Data Rate** |
|----------------|--------------|--------------------------------------------|---------|-----------------------|--------------------------------------------|--------------------|
| **802.11-prime**     | DSSS         | Direct Sequence Spread Spectrum            | 1997    | 2.4 GHz               | 22 MHz                                     | 2 Mbps             |
| **802.11b**    | HR/DSSS      | High Rate/Direct Sequence Spread Spectrum  | 1999    | 2.4 GHz               | 22 MHz                                     | 11 Mbps            |
| **802.11a**    | OFDM         | Orthogonal Frequency Division Multiplexing | 1999    | 5 GHz                 | 20 MHz                                     | 54 Mbps            |
| **802.11g**    | ERP          | Extended Rate PHY                          | 2003    | 2.4 GHz               | 20 MHz                                     | 54 Mbps            |
| **802.11n**    | HT           | High Throughput PHY                        | 2009    | 2.4 GHz, 5 GHz        | 20 MHz, 40 MHz, 80 MHz, 160 MHz            | 600 Mbps           |
| **802.11ac**   | VHT          | Very High Throughput PHY                   | 2013    | 5 GHz                 | 20 MHz, 40 MHz, 80 MHz, 160 MHz, 80+80 MHz | 6.9 Gbps           |
| **802.11ax**   | HE           | High Efficiency PHY                        | 2019    | 2.4 GHz, 5 GHz, 6 GHz | 20 MHz, 40 MHz, 80 MHz, 80+80 MHz, 160 MHz | 9.6 Gbps           |
| **_802.11ad_** | _WiGig_      | _Wireless Gigabit_                         | _2012_  | _60 GHz_              | _2.16 GHz_                                 | _7 Gbps_           |
| **_802.11af_** | _TVWS_       | _Television White Spaces_                  | _2014_  | _54-790 MHz_          | _6 MHz, 7 MHz, 8 MHz_                      | _570 Mbps_         |
| **_802.11ah_** | _HaLow_      | _High Efficiency WLAN_                     | _2016_  | _900 MHz_             | _1 MHz, 2 MHz, 4 MHz, 8 MHz, 16 MHz_       | _347 Mbps_         |

- Los `Data Rates` varían mucho depende de la `PHY` que esté siendo usada. 
- Los primeros `dispositivos WiFi` soportaban un máximo de 1 o 2 Mbps... Pero actualmente pueden llegar a data rates de casi 10 Gbps
- Sin embargo, en un mundo real `casi ningún dispositivo sería capaz de llegar a ese data rate` por razones como:
1. El medio (aire) se comparte con otros dispositivos WiFi en el mismo canal.
2. Los `Management Frames` de 802.11 crean `overhead` lo cual también consume `airtime`.

- Los `802.11 PHY` utilizan un `PHY header` (también conocidos como `campos de PPDU`) que son `prepended` al `payload` que proviene del `MAC Layer`
- El `PHY header` contiene la información necesaria para que el `receptor` ajuste su `data rate` dependiendo sus posibilidades para así poder sincronizarse con el `transmisor`


## `MCS Table` - Modulation & Coding Scheme

- [Wireless LAN Professionals: `MCS Table and How You Can Use it`](https://youtu.be/QBiBPbME5tY)
- [`VHT` (802.11n/ac) MCS Chart – Wave 1](https://www.wirelesstrainingsolutions.com/wireless-tools/vht-mcs-chart-wave-1/)
- La `MCS Table` Ayuda a evular la calidad del ambiente de RF `quality of the RF enviorment`
- La `tabla MCS` se utiliza en las redes Wi-Fi que operan en las bandas de frecuencia de `2,4 GHz` y `5 GHz`. 
- Cada dispositivo que `transmite` en una red `WiFi` (como un AP, celular, o cualquier antena WiFi) debe tomar `decisiones internas` y preguntarse `"¿Qué MCS usaré?"`
- La `MCS (Modulation and Coding Scheme)` es una tabla utilizada en las redes Wi-Fi para definir la el `data rate` (tasa de transmisión de datos) que se puede lograr en un canal de comunicación inalámbrico. 
- La tabla MCS establece la relación entre la modulación utilizada para enviar datos y la tasa de bits por segundo (bps) que se puede alcanzar.

`MCS` agrupa varias cosas como:

1. `Modulation`
2. `Coding Scheme`
3. `Guard Interval`
4. `Channel Width`

![image](https://user-images.githubusercontent.com/94720207/224502668-3671d933-d4f7-4338-a7c3-fdd65f85062c.png)

### `PHYs compatibles` con `MCS Table`

- La `MCS table` se utiliza **únicamente en los estándares 802.11 que utilizan la técnica de modulación `OFDM`** para transmitir datos. 

La técnica `OFDM` es una forma de `dividir la señal de transmisión` en múltiples subportadoras que `se transmiten en paralelo`, lo que permite una mayor eficiencia espectral y una mayor capacidad de transmisión.

- Por otro lado, poniendo el ejemplo del estándar `802.11b` que utiliza la técnica de modulación `DSSS (Direct-Sequence Spread Spectrum)` que **NO es compatible con la MCS table.** 
 
`DSSS` utiliza una técnica de `esparcimiento de espectro` que extiende la señal de transmisión en un ancho de banda más amplio que la señal original, lo que reduce la interferencia y mejora la calidad de la señal. Debido a esta técnica de transmisión, no se pueden utilizar las mismas combinaciones de modulación y codificación que se utilizan en OFDM, por lo que la MCS table no es aplicable en 802.11b. 

**Cada `PHY` (enmienda IEEE) tiene su propia tabla `MCS`**, que especifica las tasas de datos máximas que se pueden lograr en diferentes condiciones de transmisión, como la `calidad de la señal`, la `interferencia` y la `distancia` entre el dispositivo emisor y el receptor. <br>

`Nota`: A medida que la tecnología avanza y **se añaden nuevas características y tecnologías adicionales** a la `PHY`, también la `MCS Table` crece.

|    **Estándar**   | **Estándar IETF** | **Año de lanzamiento** | **Técnica de modulación** | **Banda de frecuencia** |            **Tecnologías adicionales**           | **Máxima tasa de datos** |
|:-----------------:|:-----------------:|:----------------------:|:-------------------------:|:-----------------------:|:------------------------------------------------:|:------------------------:|
| **IEEE 802.11a**  | prime             | 1999                   | OFDM                      | 5 GHz                   | N/A                                              | 54 Mbps                  |
| **IEEE 802.11g**  | N/A               | 2003                   | OFDM                      | 2,4 GHz                 | N/A                                              | 54 Mbps                  |
| **IEEE 802.11n**  | Wi-Fi 4           | 2009                   | OFDM y HT-OFDM            | 2,4 GHz y 5 GHz         | MIMO                                             | 600 Mbps                 |
| **IEEE 802.11ac** | Wi-Fi 5           | 2013                   | OFDM                      | 5 GHz                   | canales más anchos, MU-MIMO                      | 6,9 Gbps                 |
| **IEEE 802.11ax** | Wi-Fi 6           | 2021                   | OFDM y HE-OFDM            | 2,4 GHz y 5 GHz         | múltiples bandas de frecuencia, MU-MIMO mejorada | 11 Gbps                  |

Las tasas de datos más altas se logran utilizando modulaciones más complejas y una mayor cantidad de bits por símbolo, lo que aumenta la eficiencia espectral de la transmisión. Sin embargo, **estas tasas de datos máximas solo se pueden lograr en condiciones óptimas de transmisión**, y la tasa real de datos puede variar según las condiciones del entorno y el hardware utilizado.

---

### 💀 `Fz3r0 Pro Tip`: ¿Cómo leer la MCS Table like a sir?

Es mejor aprender con la `MCS Table` con la tabla de `802.11n/ac` ya que `802.11ax` se vuelve demasiado grande para comprender al principio.

![image](https://user-images.githubusercontent.com/94720207/224502878-2edac492-fcc3-492d-86e1-f1f46740e546.png)

- **`IMPORTANTE`: Antes de aprender a leer la `MCS Table`, hay que identificar exactamente `cada parte que la compone`, al saber leer la `MCS` de `802.11n/ac`, en realidad se puede leer cualquiera ya sea anterior o posterior a ese Estándar IEEE.** 

---

### **`Spatial Streams`**

Los `spatial streams` son una técnica utilizada en los estándares inalámbricos `IEEE 802.11n` y IEEE `802.11ac` (y posteriores...) que permite `transmitir y recibir varios flujos de datos simultáneamente` mediante la `utilización de múltiples antenas`. <br>

Cada `spatial stream` se puede pensar como **una vía separada para transmitir datos**, lo que **aumenta la capacidad del sistema inalámbrico** y **mejora la velocidad de transmisión**.

Para utilizar los spatial streams se necesita una configuración de antenas `MIMO (Multiple Input Multiple Output)` en el dispositivo inalámbrico. 

- `Nota`: Recordar que el `MIMO` se implementó a partir de `802.11n-2009`. Antes existía OFDM pero utilizaban `SISO (Single Input Single Output)`, es decír **NO tenía más de 1 solo spatial stream** (Como 802.11a) con una sola antena de transmisión y una sola antena de recepción.

Los sistemas `MIMO` tienen `múltiples antenas de transmisión y recepción` que se utilizan para `transmitir y recibir datos simultáneamente`. En un sistema MIMO, **las antenas transmiten y reciben señales de forma independiente**, lo que `permite que múltiples spatial streams` **se transmitan a través de múltiples antenas**.

![image](https://user-images.githubusercontent.com/94720207/224518340-64f3f973-a551-475b-9bf9-a44fc9902d1f.png)

- La configuración de antenas MIMO más común es `2x2 MIMO`. 
- Utiliza `dos antenas de transmisión` y `dos antenas de recepción`. 

Con esta configuración, se pueden utilizar `dos spatial streams para transmitir y recibir datos`, lo que **aumenta la capacidad del sistema inalámbrico y mejora la velocidad de transmisión en comparación con un sistema `SISO (Single Input Single Output)`** con una sola antena de transmisión y una sola antena de recepción. <br>

Para maximizar la capacidad del sistema inalámbrico y la velocidad de transmisión, se recomienda **que ambos extremos tengan la misma configuración de antenas MIMO y que las antenas estén configuradas de manera óptima para aprovechar las condiciones del canal inalámbrico en tiempo real**. <br>

Cuando se combinan diferentes configuraciones de antenas de cada lado de una comunicación inalámbrica, por ejemplo, una configuración de `1x1 SISO`  en un extremo y una configuración de `2x2 MIMO` en el otro extremo, se producen algunas limitaciones en el sistema inalámbrico. <br>

- La configuración de `2x2` puede transmitir y recibir `dos spatial streams simultáneamente`
- La configuración de `1x1` solo puede transmitir y recibir `un spatial stream`. 

Esto significa que, en la comunicación entre ambos extremos, **solo se pueden utilizar un spatial stream**, ya que este `es el máximo` que puede ser transmitido y recibido por `ambas configuraciones de antenas`. <br>

![image](https://user-images.githubusercontent.com/94720207/224517321-e03d7e75-6d26-4b8b-a28f-d94c478dbe96.png)

- `IMPORTANTE`: No siempre se utilizan todas las antenas de un sistema MIMO para transmitir o recibir datos en un momento dado!!!! La selección de las antenas se realiza dinámicamente para aprovechar las mejores condiciones del canal inalámbrico en tiempo real. La selección de las antenas MIMO se basa en una combinación de factores técnicos y de las condiciones del canal, y puede variar dinámicamente para optimizar la capacidad y la velocidad de transmisión en tiempo real.

Ahora, podemos saber lo que en realidad se refieren esas diviones de `spatial streams` en la MCS table, y todo depende de la combinación de ambas antenas durante la tranmisión. Es decir, las etiquetas `1 spatial stream`, `2 spatial stream`, `3 spatial stream`, etc., se refieren a la **cantidad de streams que se pueden transmitir simultáneamente utilizando una `determinada configuración de antenas MIMO` (`2x2`, `3x3`, `4x4`, etc...).**

![image](https://user-images.githubusercontent.com/94720207/224517178-f31b1ee0-8fac-4f3f-9eea-2b9c0f3e22ff.png)

---

### **`Identificación de PHY / 802.11 IEEE Standard`**

- `HT` corresponde a `802.11n`
- `VHT` corresponde a `802.11ac`

![image](https://user-images.githubusercontent.com/94720207/224513646-18efeefd-17d5-4cfd-89fe-b8cc4fc69e78.png)

`Importante`: Como cada `PHY` funciona diferente hay que encontrar el específico que queremos buscar.

---

### `HT` = `802.11n`

- Modulación y Esquema de Codificación de Alta Velocidad (HT-MCS)
- En caso de `HT` = `802.11n` la encontramos en la `primer` columna.
- Representado por **un número entero en el rango de `0-76`.**
- Se cuenta primero de `0` a `7`, después de `8` a `16`... Y si viéramos la tabla completa sigue haciendo esos bloques hasta llegar a `77`.
- **Es decir, un total de `77 rows` (filas) de `combinaciones posibles en total.`**

![image](https://user-images.githubusercontent.com/94720207/224515014-47294704-4d6d-41f4-bbb5-4f6232ed3bb3.png)

**Sin embargo, en caso de `VHT` es un poco diferente:**

---

### `VHT` = `802.11ac`

![image](https://user-images.githubusercontent.com/94720207/224514909-7e8a0c9a-4c54-45c7-a153-38a7e9a7f8d3.png)

- Modulación y Esquema de Codificación de Muy Alta Velocidad (VHT-MCS)
- En caso de `VHT` = `802.11ac` la encontramos en la `segunda` columna.
- Representado por **un número entero en el rango de `0-9`**.

`OJO!!!`: Si se siguiera el mismo método que `HT` se convertiría en cientos y cientos de `rows` en la misma tabla, para evitar esto se hizo lo siguiente: 

1. Se cuenta del `0` al `9` el cual corresponde a un `spatial stream`
2. Cada que se pasa al siguiente spatial stream se aumenta nuevamente el doble. Por ejemplo, al pasar al segundo bloque de `spatial stream 2` es del `0` al `9` dos veces y con las nuevas combinaciones correspondientes. 
    - Es decir, primer bloque `1 spatial stream` = `0` to `9`, segundo bloque `2 spatial stream` **son 2 veces** `0` to `9`, tercer bloque `3 spatial stream` **son 3 veces** `0` to `9`, etc, etc... 

Los valores en la tabla que se repiten en el rango de `0-9` corresponden a diferentes `combinaciones` de `modulación`, `esquemas de codificación` y `ancho de banda` que se pueden utilizar en `802.11ac` para lograr diferentes tasas de transferencia de datos o `data rate`. <br>

Cada combinación de valores se representa con un número en el rango de 0-9 en la columna VHT-MCS de la tabla. Es importante tener en cuenta que el valor 9 en VHT-MCS no es lo mismo que el valor 9 en HT-MCS, ya que corresponden a diferentes combinaciones de modulación y esquemas de codificación en cada estándar.

---

### **`Modulation Scheme`**

- Existen diferentes `técnicas de modulación`, como `BPSK`, `QPSK`, `16-QAM`, `64-QAM`, entre otras... 
- Cada una de estas técnicas utiliza una diferente combinación de `amplitud`, `fase` y `frecuencia` de onda para representar `bits de información`.
- Las técnicas de modulación `más complejas`, como `64-QAM`, **pueden transmitir más bits de información en un solo símbolo que las técnicas más simples, como `BPSK`**. Sin embargo, **las técnicas de modulación más complejas también son más susceptibles a errores de transmisión debido a la presencia de ruido y otros factores en el canal de comunicación.**

![image](https://user-images.githubusercontent.com/94720207/224524309-07be4db5-af3b-45fe-8fcd-71bbb0b068a3.png)

Por lo tanto, la elección de la técnica de modulación adecuada depende de varios factores, como la calidad de la señal, el ancho de banda disponible y la tasa de errores de transmisión permitida. Las combinaciones de técnicas de modulación y codificación que se muestran en una tabla MCS se organizan en función de su eficiencia en términos de tasa de transferencia de datos y resistencia a errores de transmisión.

![image](https://user-images.githubusercontent.com/94720207/224521846-04cf91ad-dfac-4813-adeb-2afa274ed362.png)





• Esquema de Modulación
Define la fase y amplitud requerida para el cálculo de bits, desde BPSK hasta QPSK, 16-QAM, 64-QAM y 256-QAM.

• Codificación
Tasa de bits transferidos y corrección de errores hacia adelante. Una codificación de 1/2 significa que se transfieren dos bits y se recibe uno. Minimizar el esquema de codificación implicaría enviar los datos más rápido pero perdiendo robustez.

• Ancho de Banda de Datos
Especifica el canal utilizado: 20MHz, 40MHz, 80MHz y 160MHz.

• Intervalo de Guarda
Tiempo de espera o pausa entre cada transmisión de paquete. 802.11n tiene 400ns y 802.11ac tiene 800 ns. Cuanto menor sea el intervalo de guarda, mayor será la velocidad de transferencia de datos.

• SNR mínimo y RSSI
Determina el SNR mínimo y el RSSI requerido para un índice MSC específico.

![image](https://user-images.githubusercontent.com/94720207/224523058-f4960b76-873a-4b03-aa7d-c8151efb2ee4.png)


### `Bandwith`

- La tasa de transmisión de datos se le llama "data transmission rate" o "data transfer rate" en inglés. También puede ser conocida como "data rate", "bit rate" o "throughput".

### `Analogía de la carretera`

- En esta analogía el `bandwith` representa la capacidad total de `coches` que puede soportar una carretera en un momento exacto. 
- Es decir, la cantidad de datos que pueden pasar en un segundo... 
- Por ejemplo, un bandwith de 24 Mbps, es igual a una carretera que soporta `24 coches`
- 24 Mbps sería el bandwith total, quiere decir que puede transferir 24 Mb cada segundo que pasa, si una canción `.mp3` pesara `24Mb` se transferiría en `1 segundo exacto.`

**Sin embargo, en `un mundo real` esto sería imposible, ya que nunca podrían ponerse de acuerdo esos `24 coches` para abarcar exactamente los espacios necesarios de la carretera, en un mundo real la capacidad quizás bajaría a unos `20 coches`... o `20 Mbps`**. <br>

**Factores como el `ruido`, `interferencia`, otros `clientes` (STA), coding, etc, etc... representan esos espacios en la carretera, eso sería el `throughput` real:**

![image](https://user-images.githubusercontent.com/94720207/224551755-a707ebfd-f37a-423b-99e1-b360f9b08cb1.png)

- Cuando hay `varias STA` (Estaciones) conectadas a `un mismo AP` (Punto de Acceso), el ancho de banda total del AP se comparte entre todas las estaciones. 
- Sin embargo, el `throughput` disponible para cada `STA` dependerá de varios factores que ya se han mencionado (tráfico de la red, el tipo de protocolo de acceso al medio utilizado (como el protocolo CSMA/CA), la cantidad de dispositivos conectados, la calidad de la señal, ruido, etc, etc.

**En un entorno ideal, donde todas las estaciones tienen la misma prioridad y una señal fuerte y estable, el `ancho de banda se distribuiría de manera equitativa entre todas las estaciones conectadas.` Sin embargo, `en la práctica, esto rara vez sucede` debido a la variabilidad en las condiciones de la red y a la congestión de la red.**

![image](https://user-images.githubusercontent.com/94720207/224553627-80e02f16-a8cf-499c-9914-8b312ccedbd4.png)

- Normalmente, **una `STA` que genere `más tráfico` puede tener un `mayor throughput` que una `STA` que genere `menos tráfico`, siempre y cuando el ancho de banda disponible lo permita.** 
- El `throughput` se define como `la cantidad de datos que se pueden transmitir en un período de tiempo determinado`, por lo que si una `STA` está generando `más tráfico`, es posible que pueda `transmitir más datos en el mismo período de tiempo` en comparación con una `STA` que genere menos tráfico.

**En un entorno ideal y "mundo perfecto", donde todas las `STAs` tienen la misma `señal`, `calidad` y `distancia de conexión`, etc... el `throughput` (es decir, el `bandwith` total disponible) se distribuiría equitativamente entre las `STAs`. <br>

**Sin embargo, cuando hay un `mayor tráfico generado por una STA`, es probable que `esta STA tenga un mayor throughput` en comparación con las estaciones que generan menos tráfico.

- Por ejemplo: Una `STA` que está haciendo `stream en 4k` puede tener un `mayor throughput`, en comparación con una `STA` que solo está mandando `mensajes de texto` por WhatsApp.




https://www.wirelesstrainingsolutions.com/understanding-ofdm-part-4-refresh/















- [OFDM Frame Structure](https://rfmw.em.keysight.com/wireless/helpfiles/89600b/webhelp/Subsystems/wlan-ofdm/Content/ofdm_80211-overview.htm)
