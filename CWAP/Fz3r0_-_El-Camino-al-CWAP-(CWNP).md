<!-- 

Y ARRANCAN!!!

 -->

# El camino al CWAP - Certified Wireless Analysis Professional
_Writeup en español por Fz3r0 💀 (CWNA)_

## Conocimiento Requerido para CWAP-402

- El examen está dividido de la siguiente manera:

| **Conocimiento CWAP**         | **Porcentaje** |
|:-----------------------------:|:--------------:|
| **Protocol Analysis**         | 15%            |
| **Spectrum Analysus**         | 10%            |
| **PHY Layers & Technologies** | 10%            |
| **MAC Sublayers & Functions** | 25%            |
| **WLAN Medium Access**        | 10%            |
| **802.11 Frame Exchanges**    | 30%            |

## CWAP: Objetivos

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

## CWAP: Modelo OSI (usado en el libro)

- `Layer 7` - Application Layer `Data`
- `Layer 6` - Presentation Layer `Data`
- `Layer 5` - Session Layer `Data`
- `Layer 4` - Transport Layer `Segment`
- `Layer 3` - Network Layer `Packet`
- `Layer 2` - Data Link Layer `Frame`    
- `Layer 1` - Physical Layer `Frame/Bit`

![image](https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png)

### 💀 `Fz3r0 Pro Tip:`

- `Layer 1`, `Layer 2`, `Layer 3` y `Layer 4` son los importantes en Networking
- Los estándares `IEEE 802.3 (ethernet)` y `802.11 (wireless)` operan primariamente en `Layer 1` & `Layer 2` 
- Los estándares `IETF` de los protocolos `TCP` & `IP` operan primariamente en `Layer 3` & `Layer 4` 
- `Layer 1` & `Layer 2` son las capas principales en las que se enfoca el `CWAP` (Ya que el WiFi es donde funciona realmente 😉) 

## Funcionamiento de los Layers

- Se dice que cada Layer sirve hacia el Layer de arriba y abajo de él, excepto por las 2 Layers finales: `Layer 1 (capa final de transmisión)` & `Layer 7 (capa final de recepción)`
- Mientras los datos se mueven por las capas del Modelo OSI, se van `encapsulando` y `decapsulando`

![image](https://user-images.githubusercontent.com/94720207/223029707-a67719fd-de81-407c-97d0-7c118cbf9b80.png)

### Encapsulamiento

- Simplemente es `append` o `preppend` (poner antes o después) bits de datos adicionales. 
- Es una técnica utilizada por protcolos por capas (layers) para cargar protocolos ajenos de esa capa particular en una red. 
- Por ejemplo, Que Layer 2 pueda contener los datos que vienen de arriba en Layer 3, 4, 5, 6 o 7... sin necesidad que esa capa los "entienda". 

    - Si los datos se mueven de `Arriba (Layer 7)` hacia --->>> `Abajo (Layer 1)` los datos se `encapsulan`
    - Si los datos se mueven de `Abajo (Layer 1)` hacia --->>> `Arriba (Layer 7)` los datos se `decapsulan`

![image](https://user-images.githubusercontent.com/94720207/223026259-b2f1cd67-9dba-4a2a-b76b-8e99d2a54242.png)

![image](https://user-images.githubusercontent.com/94720207/223026368-7c497884-9f6f-489b-9fe6-ab46fc521b01.png)


- **`CWAP Definition`** 

    - `Encapsulation` - Is the process of of **prepending and/or appending information to a message for `transmission`** (communication) `TO a peer`.
    - `Decaspulation` - Is the process of **reading, processing and removing prepended and/or appended information for `reception`** (communication) `FROM a peer`.




## `Layer 4` Transport

- La Capa 4 del modelo OSI es la capa de transporte, y su función principal es proporcionar un medio para que los procesos de aplicaciones en diferentes dispositivos puedan establecer, mantener y terminar conexiones de comunicación. En esta capa se encuentran dos protocolos principales: TCP y UDP.

- `Medio` _(Hablando de la capa 4 de transporte)_: Conjunto de servicios y protocolos que permiten a los procesos de aplicaciones en diferentes dispositivos establecer y gestionar una conexión de comunicación extremo a extremo.

### TCP

- `TCP` (Transmission Control Protocol): Protocolo orientado a conexión y confiable. `Connection-oriented and Reliable`
- Proporciona un canal de comunicación extremo a extremo que garantiza que los datos enviados sean recibidos en el orden correcto y sin errores `ACK`, `Checksum`, `Seq`, etc. 
- Para lograr esto, TCP establece una conexión entre dos dispositivos antes de enviar datos `3-way-handshake`. 
- Los datos se envían en segmentos y se espera que el receptor confirme la recepción de cada segmento. 
- Si un segmento no se recibe correctamente, TCP lo retransmite hasta que el receptor lo confirma. 
- TCP también controla la tasa de transmisión para evitar la congestión de la red.

### UDP

- `UDP` (User Datagram Protocol) es un protocolo sin conexión y no confiable `Connectionless and Unreliable`. 
- No establece una conexión antes de enviar datos y no proporciona garantías de que los datos sean recibidos correctamente o en el orden correcto `No tiene ACK, Cheksum, etc` _(Algunos pueden llegar a traer Seq)_. 
- Los datos se envían en datagramas, y no hay confirmación de recepción ni retransmisión de paquetes perdidos. 
- UDP es útil para aplicaciones en las que la velocidad es más importante que la confiabilidad, como en la transmisión de audio o video en tiempo real.

![image](https://user-images.githubusercontent.com/94720207/223029378-5c82410f-0388-4e63-8fe1-1c968da26008.png)



### Otros

- Además de TCP y UDP, hay otros protocolos de transporte en la Capa 4 del modelo OSI, como SCTP (Stream Control Transmission Protocol), que es similar a TCP pero se utiliza para aplicaciones de tiempo real y en redes móviles, y DCCP (Datagram Congestion Control Protocol), que es similar a UDP pero con mecanismos para evitar la congestión de la red.

## `Layer 3` Network

- La Capa 3 del modelo OSI es la capa de red, y su función principal es proporcionar servicios para enrutar los paquetes de datos a través de la red desde el origen al destino. `Origen(IP) <---> Destino(IP)`

### IP (Internet Protocol)

- En esta capa se encuentra el protocolo de Internet (IP) `IP (Internet Protocol)`, que es el protocolo principal utilizado en Internet para enrutar paquetes entre dispositivos.
- Los paquetes de datos se envían en forma de datagramas, y cada datagrama incluye la `IP Address` del dispositivo de `origen` y del dispositivo de `destino`. 
- La dirección IP se utiliza para enrutar el datagrama a través de la red.
- El protocolo de Internet versión 4 `IPv4` es el protocolo de red más utilizado en la actualidad. 
- IPv4 utiliza direcciones de 32 bits para identificar los dispositivos en la red. 
- Sin embargo, debido a la cantidad limitada de direcciones IPv4 disponibles, se ha desarrollado un nuevo protocolo de Internet versión 6 `IPv6` que utiliza direcciones de 128 bits para permitir un mayor número de dispositivos en la red.

![image](https://user-images.githubusercontent.com/94720207/223030711-14388bc0-b4b9-43ea-9645-ec7c02c65722.png)

![image](https://user-images.githubusercontent.com/94720207/223030667-0e798b26-03da-48b1-97e9-5e5050eee172.png)

### Otros

- Además de IP, hay otros protocolos de la Capa 3 en el modelo OSI, como ICMP (Internet Control Message Protocol), que se utiliza para enviar mensajes de error y de control entre dispositivos en la red, y IGMP (Internet Group Management Protocol), que se utiliza para gestionar grupos de dispositivos que desean recibir un flujo de datos en multicast.

## `Layer 2` Data Link

- La Capa 2 del modelo OSI es la capa de enlace de datos, y su función principal es proporcionar servicios para la transmisión fiable de datos entre dispositivos en la misma red física. 
- Tanto WiFi como Ethernet (inalámbrico y alámbrico) utilizan la Capa 2 de manera similar
- La principal diferencia entre Ethernet y Wi-Fi en la Capa 2 es la forma en que los datos se transmiten a través del medio físico (aire o cables).
- Esta capa se divide en dos subcapas: 

    1. `LLC - Logical Link Control` = Capa de Control de Enlace Lógico
    2. `MAC - Medium  Access Control` = Capa de Control de Acceso al Medio

- [Extreme Networks @ Layer 2 – the Data Link Layer](https://youtu.be/B0Uf3uojpv0)

![image](https://user-images.githubusercontent.com/94720207/223143142-42e11745-b223-4637-93af-0e5238f4ffcd.png)

![image](https://user-images.githubusercontent.com/94720207/223142755-ec76569c-f874-4dda-979e-95bd53ce1929.png)

### LLC - Logical Link Control (Sublayer)

- El protocolo de control lógico (LLC) es el protocolo que proporciona un `enlace de comunicación entre la Capa 2 y la Capa 3`.
- El LLC se encarga de proporcionar servicios de control de enlace de datos a la capa de red superior y garantizar que la información se transmita de manera confiable entre dos dispositivos de red (Por ejemplo, PC-A y PC-B en una red ethernet cableada).
- La subcapa LLC proporciona servicios para la comunicación entre dispositivos en diferentes redes lógicas. 
- Proporciona un mecanismo para multiplexar y desmultiplexar diferentes protocolos de la Capa 3 (como IPX, TCP, etc.) en la misma red física (como el cable que usa ethernet, o el aire que usa WiFi). 

![image](https://user-images.githubusercontent.com/94720207/223312112-66e4f3c8-9800-4ae8-a4d8-7c2285a4e194.png)


![image](https://user-images.githubusercontent.com/94720207/223311481-6e5e391b-d28c-403d-8384-492f018be840.png)

![image](https://user-images.githubusercontent.com/94720207/223023071-19560cf8-3027-4be2-9496-80fe121a3775.png)


#### Multiplexación y desmultiplexación 

- La multiplexación es la capacidad de la Capa 2 de Enlace de Datos para combinar varios flujos de datos que vienen de de la Capa 3 (como por ejemplo, diferentes protocolos de red) en un solo flujo de datos que se transmite a través de un único medio físico compartido (como un cable o el aire), y luego separarlos nuevamente en la Capa 2 del otro extremo.
- En palabras más sencillas: 

    - Es una manera de convertir "datos digitales de computadora" que tienen como `origen: PC-A` a "pulsos eléctricos, ondas de radio, etc" que `pasan por un cable o el aire`, y luego volverlos a convertir a "datos digitales de computadora" los cuales recibe el `destino: PC-B`. Aunque en realidad es algo un poco más complejo, esa es la idea principal. 

- Nota_ Ethernet es una tecnología de red cableada que utiliza un cable para conectar dispositivos a una red. La tecnología Wi-Fi, por otro lado, es una tecnología inalámbrica que utiliza ondas de radio para transmitir datos a través del aire.
    
#### Ejemplo de Multiplexación:
    
- En el caso de comunicaciones DSL, se utiliza la técnica de multiplexación por división de frecuencia (FDM) para combinar la señal de datos con la señal de voz en una señal única que se transmite a través del cableado de cobre. 
- Los datos se transmiten a través del medio físico en forma de pulsos eléctricos modulados utilizando técnicas de modulación de amplitud.

### MAC (Sublayer)

- Este es el sublayer en el que más se enfoca el `CWAP`
- La subcapa MAC, proporciona servicios para la comunicación entre dispositivos en la misma red física.
- En esta capa se encuentran mecanismos como CSMA/CA y CSMA/CD para evitar colisiones.
- Esta subcapa permite crear un `local link`, que se refiere a la comunicación en la `red local (LAN)` utilizando `Layer 1` y `Layer 2`.
- El local link trabaja en Layer 1 y 2, pero trae el payload y los datos de las capas superiores para ser trasnmitadas.
- La MAC se define en el estándar IEEE 802.3 en caso de Ethernet y 802.11 en caso de WiFi.
- Los `3 tipos de Frames` que principalmente se estudian en este curso y que forman el `MAC sublayer de 802.11` son:
1. **`Management Frames`**
2. **`Control Frames`**
3. **`Data Frames`**

![image](https://user-images.githubusercontent.com/94720207/223311147-d3127cac-05ec-4f5b-a290-4cf011504175.png)

### LLC 

![image](https://user-images.githubusercontent.com/94720207/223023395-805f7429-af91-4920-b38d-866cab8046ba.png)



![image](https://user-images.githubusercontent.com/94720207/223023334-c1b51e69-ee9e-4976-b571-877f3e9c77c5.png)

## `Layer 1` Physical

## `Frames`: En `Layer 1` y `Layer 2`

- Los Frames son paquetes de datos que vienen de capas superiores en el modelo OSI.
- A estos paquetes se les agrega al principio o al final (append prepend) frames para poder realizar su trasnmisión en el medio local. 

### Layer 1: `Physical Layer Frame`

- En `Layer 1 (Physical Layer)`, un frame se refiere a un `conjunto de bits` que se transmiten en la red en una única transmisión. 
- Estos bits se organizan en un formato específico para que puedan `ser enviados a través de medios físicos como cables, fibra óptica o ondas de radio`. 
- El formato de estos bits se llama `Physical Layer Frame`.

### Layer 2: `Data Link Layer Frame`

- En `Layer 2 (Data Link Layer)`, un frame se refiere a un `paquete de datos` que se transmite entre dispositivos de red en una red local. 
- Este paquete de datos incluye `información de control adicional`, como `direcciones de origen y destino`, que permiten que los dispositivos de red se comuniquen entre sí de manera efectiva. 
- El formato de estos paquetes se llama `Data Link Layer Frame`.

### Append y Prepend

- En cuanto a la referencia a un "append" y "prepend" del upper layer, esto se refiere al hecho de que, en algunos casos, los datos que se transmiten a través de la red pueden tener información de control adicional agregada por capas superiores del modelo OSI, incluyendo su `payload` (data)
- El `append` se refiere a agregar esta información de control al final del paquete de datos, 
- El `prepend` se refiere a agregar esta información de control al principio del paquete de datos.

![image](https://user-images.githubusercontent.com/94720207/223307931-405fc7e5-1474-4c24-a4d0-60f6e0faa451.png)

![image](https://user-images.githubusercontent.com/94720207/223145162-b19d49b2-7160-4a81-bc68-93f7891b11cf.png)

