# CWAP

## Conocimiento Requerido para CWAP-402

- Está en cortina:

| **Conocimiento CWAP**         | **Porcentaje** |
|:-----------------------------:|:--------------:|
| **Protocol Analysis**         | 15%            |
| **Spectrum Analysus**         | 10%            |
| **PHY Layers & Technologies** | 10%            |
| **MAC Sublayers & Functions** | 25%            |
| **WLAN Medium Access**        | 10%            |
| **802.11 Frame Exchanges**    | 30%            |

## CWNA Troubleshooting Methodology

## CWAP: Objetivos

- Asegurarse que el troubleshooting se está llevando a cabo con todos los tipos de anlálisis.

1. Definir el problema
2. Determinar la escala del problema 
3. Identificar las posibles causas
4. Capturar y Analizar los datos
5. Observar el problema
6. Seleccionar los pasos apropiados para remediar el problema
7. Documentar el problema y resolución 

- Aplicar y comprender los conocimientos respecto a los **PHY Technologies** como son: `PHY headers`, `Preambles`, `Training Fields`, `Frame Aggregation`, `Data Rates`.

- Entender por completo el `Frame` y `Frame Aggregation`

    - Frame Aggregation: `A-MSDU` & `A-MPDU` 

## CWAP: Modelo OSI (usado en el libro)

- `Layer 7` - Application Layer
- `Layer 6` - Presentation Layer
- `Layer 5` - Session Layer
- `Layer 4` - Transport Layer
- `Layer 3` - Network Layer
- `Layer 2` - Data Link Layer     
- `Layer 1` - Physical Layer 

### `Pro Tip:`

- Los estándares `IEEE 802.3 (ethernet)` y `802.11 (wireless)` operan primariamente en `Layer 1` & `Layer 2` 
- Los estándares `IETF` de los protocolos `TCP` & `IP` operan primariamente en `Layer 3` & `Layer 4` 

### Funcionamiento de los Layers

- Se dice que cada Layer sirve hacia el Layer de arriba y abajo de él, excepto por las 2 Layers finales: `Layer 1 (capa final de transmisión)` & `Layer 7 (capa final de recepción)`
- Mientras los datos se mueven por las capas del Modelo OSI, se dan encapsulando y decapsulando _(`encapsular`: append o preppend (poner antes o después) bits de datos adicionales. "Técnica utilizada por protcolos por capas (layers) para cargar protocolos ajenos de esa capa particular en una red. Por ejemplo, Que Layer 2 pueda contener los datos que vienen de arriba en Layer 3, 4, 5, 6 o 7")_

    - Si los datos se mueven de `Arriba (Layer 7)` hacia --->>> `Abajo (Layer 1)` los datos se `encapsulan`
    - Si los datos se mueven de `Abajo (Layer 7)` hacia --->>> `Arriba (Layer 1)` los datos se `decapsulan`

- **`CWAP Definition`** 

    - `Encapsulation` - Is the process of of **prepending and/or appending information to a message for `transmission`** (communication) `TO a peer`.
    - `Decaspulation` - Is the process of **reading, processing and removing prepended and/or appended information for `reception`** (communication) `FROM a peer`.

<!-- 

AGREGAR UN MODELO OSI DE REFERENCIA

 -->


## `Layer 4` Transport

- La Capa 4 del modelo OSI es la capa de transporte, y su función principal es proporcionar un medio para que los procesos de aplicaciones en diferentes dispositivos puedan establecer, mantener y terminar conexiones de comunicación. En esta capa se encuentran dos protocolos principales: TCP y UDP.

- `Medio`: Conjunto de servicios y protocolos que permiten a los procesos de aplicaciones en diferentes dispositivos establecer y gestionar una conexión de comunicación extremo a extremo.

### TCP

- `TCP` (Transmission Control Protocol): Protocolo orientado a conexión y confiable. `Connection-oriented and Reliable`
- Proporciona un canal de comunicación extremo a extremo que garantiza que los datos enviados sean recibidos en el orden correcto y sin errores `ACK`. 
- Para lograr esto, TCP establece una conexión entre dos dispositivos antes de enviar datos (3-way-handshake). 
- Los datos se envían en segmentos y se espera que el receptor confirme la recepción de cada segmento. 
- Si un segmento no se recibe correctamente, TCP lo retransmite hasta que el receptor lo confirma. 
- TCP también controla la tasa de transmisión para evitar la congestión de la red.

### UDP

- `UDP` (User Datagram Protocol) es un protocolo sin conexión y no confiable `Connectionless and Unreliable`. 
- No establece una conexión antes de enviar datos y no proporciona garantías de que los datos sean recibidos correctamente o en el orden correcto `No tiene ACK, Cheksum, etc`. 
- Los datos se envían en datagramas, y no hay confirmación de recepción ni retransmisión de paquetes perdidos. 
- UDP es útil para aplicaciones en las que la velocidad es más importante que la confiabilidad, como en la transmisión de audio o video en tiempo real.

### Otros

- Además de TCP y UDP, hay otros protocolos de transporte en la Capa 4 del modelo OSI, como SCTP (Stream Control Transmission Protocol), que es similar a TCP pero se utiliza para aplicaciones de tiempo real y en redes móviles, y DCCP (Datagram Congestion Control Protocol), que es similar a UDP pero con mecanismos para evitar la congestión de la red.

## `Layer 3` Network

- La Capa 3 del modelo OSI es la capa de red, y su función principal es proporcionar servicios para enrutar los paquetes de datos a través de la red desde el origen al destino. `Origen(IP) <---> Destino(IP)`
- En esta capa se encuentra el protocolo de Internet (IP) `IP (Internet Protocol)`, que es el protocolo principal utilizado en Internet para enrutar paquetes entre dispositivos.
- Además de IP, hay otros protocolos de la Capa 3 en el modelo OSI, como ICMP (Internet Control Message Protocol), que se utiliza para enviar mensajes de error y de control entre dispositivos en la red, y IGMP (Internet Group Management Protocol), que se utiliza para gestionar grupos de dispositivos que desean recibir un flujo de datos en multicast.


## Layer 2

![image](https://user-images.githubusercontent.com/94720207/223023042-7de1473a-2859-44f0-8a14-5f86a476bd72.png)

![image](https://user-images.githubusercontent.com/94720207/223023071-19560cf8-3027-4be2-9496-80fe121a3775.png)

![image](https://user-images.githubusercontent.com/94720207/223023334-c1b51e69-ee9e-4976-b571-877f3e9c77c5.png)



