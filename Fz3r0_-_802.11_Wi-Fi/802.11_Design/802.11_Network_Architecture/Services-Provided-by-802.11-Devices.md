## 🟢 `Services` Provided by `802.11 Devices`

- [Tech Mike: `Wireless in all the areas`](https://techimike.com/cwna-chapter-7-wireless-in-all-the-areas/)

Los `802.11 Services` son servicios definidos por el `IEEE 802.11 Standard` para redes inalámbricas, también conocidad como `WiFi`. **Estos servicios son una serie de funciones que permiten a los dispositivos inalámbricos comunicarse y establecer conexiones en la red.**

Los `802.11 Services` se dividen específicamente `3 categorías` que permiten comunicaciones en la `Layer 1` y `Layer 2` y operan en la `MAC layer`.

1. **`SS (Station Service)`**
2. **`DSS (Distribution System Service)`**
3. **`PCPS (PBSS Control Point Service)`** _Fuera del alcance del CWAP_

- Nota: El `PCPS` funciona para redes `personal basic service set (PBSS)` las cuales están **fuera del alcance del `CWAP`** y redes de alta densidad.

### 🟣 `SS (Station Service) `

El `SS (Station Service)` o "Servicio de Estación" se refiere a los servicios proporcionados por una STA en la red Wi-Fi. Estos servicios incluyen la `autenticación`, la `asociación` y la `desasociación` de dispositivos en la red. La `STA` también proporciona `servicios de entrega de datos` a través de la red y puede `administrar el tráfico de la red`.

- El `SS (Station Service)` es un conjunto de servicios los cuales admiten `MSDU` entre `STA` dentro de un `BSS`. 
- **El `SS` está en todas las `STA`, incluidos los `AP`, `mesh gates`, `portals` y `clients`.**

Existen `2 tipos de STA` diferentes, tanto la `Client Station` como la `Access Point Station` se consideran como `STA (Station)` en el `802.11 Standard`. La `STA` es el **término genérico utilizado para referirse a cualquier dispositivo que pueda conectarse a una red inalámbrica y que tenga la capacidad de transmitir y recibir datos de forma inalámbrica.**

- [Programming esp8266-wifi - AP Mode & STA Mode](https://www.embedded-robotics.com/esp8266-wifi/)

1. **`Client Station`** 
    - Se refiere a **cualquier dispositivo** que se conecta a una red inalámbrica, **pero NO actúa como AP**. 
    - Es decir, tiene una conexión de nivel 2 con el AP y puede utilizar la red inalámbrica para comunicarse con otros dispositivos en la red. 
    - Cuando un dispositivo "Client Station" se conecta a un punto de acceso, se considera "asociado" <br><br>

![image](https://user-images.githubusercontent.com/94720207/227821492-297e7ad0-e314-429c-aea1-03a1bdb93fc7.png)



3. `AP Station`


"Client Station" . . Es decir, tiene una conexión de nivel 2 con el punto de acceso y puede utilizar la red inalámbrica para comunicarse con otros dispositivos en la red.

Un "Access Point Station" es un dispositivo que funciona como punto de acceso para los dispositivos "Client Station". El punto de acceso proporciona una puerta de enlace para que los dispositivos se comuniquen de forma inalámbrica y también les permite acceder a una conexión física como Ethernet a través del "Distribution System Access Function (DSAF)". El punto de acceso mantiene una tabla de asociación de los dispositivos "Client Station" conectados y dirige el tráfico en la red.

![image](https://user-images.githubusercontent.com/94720207/227821618-bde5645a-97ec-44ab-a39e-2629f88eb2e3.png)


Los **`10 servicios`** que conforman la **`SS`** son los siguientes:

1. **`Authentication`**
2. **`Deauthentication`**
3. **`Data confidientality (encryption)`**
4. **`MSDU delivery`**
5. **`DFS - Dynamic Frequency Selection`**
6. **`TPC - Transmit Power Control`**
7. **`Time Synchronization with higher layers (QoS facility only)`**
8. **`QoS traffic scheduling (QoS facility only)`**
9. **`Radio Measurment`**
10. **`DSE - Dynamic STA Enablement`**

| **Service**                                                     	| **Descripción**                                                                                                                                                                                                                                                                                                                                                                                                                                                	|
|-----------------------------------------------------------------	|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| **Authentication**                                              	| Proceso mediante el cual un dispositivo comprueba su identidad ante el punto de acceso (AP) de la red. El AP verifica las credenciales del dispositivo y le permite unirse a la red.                                                                                                                                                                                                                                                                           	|
| **Deauthentication**                                            	| Proceso mediante el cual el AP desconecta a un dispositivo de la red. Esto puede ocurrir por razones de seguridad, como cuando un dispositivo se ha comprometido, o simplemente porque el dispositivo ha finalizado su sesión en la red.                                                                                                                                                                                                                       	|
| **Data confidentiality (encryption)**                           	| Servicio que garantiza que los datos que se transmiten entre los dispositivos en la red no puedan ser leídos por usuarios no autorizados. Se utiliza una clave de cifrado para codificar los datos que se transmiten.                                                                                                                                                                                                                                          	|
| **MSDU delivery**                                               	| Servicio que garantiza que los paquetes de datos se entreguen correctamente en la red.                                                                                                                                                                                                                                                                                                                                                                         	|
| **DFS - Dynamic Frequency Selection**                           	| Servicio que permite al AP cambiar de canal de forma dinámica en función de la congestión en el canal actual.                                                                                                                                                                                                                                                                                                                                                  	|
| **TPC - Transmit Power Control**                                	| Servicio que permite al AP ajustar la potencia de transmisión para minimizar las interferencias y maximizar la eficiencia energética.                                                                                                                                                                                                                                                                                                                          	|
| **Time Synchronization with higher layers (QoS facility only)** 	| Servicio que permite sincronizar los relojes de los dispositivos en la red con una fuente de tiempo común. Esto es importante para garantizar que los datos se entreguen en el momento adecuado y para evitar retrasos en la red. Este servicio solo está disponible cuando se utiliza el mecanismo de Calidad de Servicio (QoS).                                                                                                                              	|
| **QoS traffic scheduling (QoS facility only)**                  	| Servicio que garantiza que los paquetes de datos con requisitos de calidad de servicio (QoS) se entreguen antes que otros paquetes menos críticos. Esto es importante para garantizar una entrega de datos suave y sin interrupciones en aplicaciones de alta prioridad como voz y video. Este servicio solo está disponible cuando se utiliza el mecanismo de Calidad de Servicio (QoS).                                                                      	|
| **Radio Measurement**                                           	| Servicio que permite a los dispositivos medir la calidad de la señal y el nivel de interferencia en diferentes canales. Esto es importante para seleccionar el canal más adecuado para la transmisión de datos y para evitar interferencias en la red.                                                                                                                                                                                                         	|
| **DSE - Dynamic STA Enablement**                                	| Servicio que permite al AP activar o desactivar la funcionalidad de los dispositivos de la red. Esto puede ocurrir para ahorrar energía, mejorar la eficiencia de la red o garantizar la seguridad de la red. Por ejemplo, si un dispositivo ha estado inactivo durante un tiempo, el AP puede desactivar su funcionalidad para ahorrar energía. Cuando el dispositivo necesita volver a comunicarse en la red, el AP puede volver a activar su funcionalidad. 	|



### 🟣 `DSS (Distribution System Service)`

El DSS (Distribution System Service) es un conjunto de servicios que proporciona el "Distribution System" (DS) de una red WiFi para la comunicación entre Access Points (AP), mesh gates y el portal de un "Extended Service Set" (ESS).

Para comprender mejor, Todos los APs de una red wireless pueden ir armando un "rompecabezas" que al final se convierte en un solo "Extended Service Set".

El DS es el sistema o red a través del cual las STA con DSS (AP) se interconectan o, más específicamente, a través del cual las redes Basic Service Set (BSS) se interconectan una con otra.

El DS Medium (DSM) es el medio utilizado por el DS, como por ejemplo cables Ethernet (como UDP o fibra),  RF Mesh, etc.

![image](https://user-images.githubusercontent.com/94720207/227799137-f1505092-751e-45da-85c0-3c5689867f66.png)


Los **`9 servicios`** que conforman la **`DSS`** son los siguientes:

1. **`Service Set Identifier (SSID)`**
2. **`Basic Service Set (BSS)`**
3. **`Basic Service Area (BSA)`**
4. **`Basic Service Set Identifier (BSSID)`**
5. **`Multiple Basic Service Set Identifiers (MBSSID)`**
6. **`Extended Service Set (ESS)`**
7. **`Independent Basic Service Set (IBSS)`**
8. **`Personal Basic Service Set (PBSS)`**
9. **`Mesh Basic Service Set (MBSS)`**

| **Service Name**                           	| **Descripción**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
|--------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| **Service Set Identifier (SSID)**          	| Es el nombre lógico que se le da a una red 802.11 para identificarla. Para un roaming adecuado, el SSID y la seguridad deben ser exactamente iguales.                                                                                                                                                                                                                                                                                                                                                                  	|
| **Basic Service Set (BSS)**                	| Consiste en un punto de acceso (AP) con una o más estaciones de cliente, que tienen conectividad L2. Cuando tienen esta conectividad L2, están asociados. Si en casa tienes un solo enrutador inalámbrico y no tienes otros puntos de acceso inalámbrico, esto se consideraría un BSS.                                                                                                                                                                                                                                 	|
| **Basic Service Area (BSA)**               	| El área de cobertura producida por su BSS es el BSA. Es la cobertura proporcionada por un solo AP. El tamaño y la forma de esta cobertura varían según la ubicación del AP, la potencia de transmisión, la ganancia de la antena, el entorno y la sensibilidad de recepción.                                                                                                                                                                                                                                           	|
| **Basic Service Set Identifier (BSSID)**   	| La dirección MAC de la radio de los APs es el BSSID. Cada radio de AP debe tener un BSSID único para permitir el roaming de las estaciones de clientes de un BSS a otro. De nuevo, necesitamos asegurarnos de que el SSID y la seguridad sean los mismos de BSS a BSS. Este movimiento de un AP a otro durante el proceso de roaming se llama transición de BSS. El BSSID se encuentra en el encabezado MAC 802.11.                                                                                                    	|
| **Multiple Basic Service Set Identifiers (MBSSID)** 	| A menudo necesitará tener múltiples SSID en un solo AP. Se recomienda mantener esto al mínimo. Lo más recomendado es limitarlo a tres si es posible. Dicho esto, cuando tenga más de uno, necesitará un identificador de BSSID L2 único. Cuando esto ocurre, el AP creará una MAC única en incrementos de su MAC codificada en hardware, cada una asignada a una red L3 vlan única. Cada SSID adicional agrega sobrecarga en forma de balizas, respuestas de sonda y otras sobrecargas de marcos de gestión y control. 	|
| **Extended Service Set (ESS)**             	| Es cuando tiene dos o más BSS configurados de manera idéntica conectados por un medio DS. Puede pensar en esto como todos los AP y clientes que están unidos por un DSM. El área de cobertura del ESS en la que los clientes pueden comunicarse y cambiar de AP se llama área de servicio extendida (ESA). Solo porque tenga un ESS no significa que tenga un roaming garantizado.                                                                                                                                     	|
| **Independent Basic Service Set (IBSS)**   	| Solo radios de clientes, sin APs. Los clientes se comunican directamente. También conocido como peer-to-peer o ad-hoc. Todos los clientes deben compartir el tiempo del medio y respetar el mismo canal. El primer cliente que se conecta crea el BSSID.                                                                                                                                                                                                                                                               	|
| **Personal Basic Service Set (PBSS)**      	| Utilizado para comunicación directa entre estaciones 802.11ad en la banda de 60GHz. Un cliente asume el rol de punto de control PBSS (PCP) y sincroniza la comunicación entre todos los clientes.                                                                                                                                                                                                                                                                                                                      	|
| **Mesh Basic Service Set (MBSS)**          	| Conjunto de APs que proporcionan distribución de malla. Los AP conectados a la red cableada son llamados puertas de enlace o "mesh gate". Los AP no conectados a la red cableada forman conexiones inalámbricas de backhaul hacia las puertas de enlace y se conocen como puntos de malla. La selección de ruta se realiza mediante el protocolo HWMP, basado en métricas como RSSI, SNR, carga del cliente y cantidad de saltos. La selección de ruta se realiza mediante MAC y no mediante IP.                       	|




![image](https://user-images.githubusercontent.com/94720207/227790252-ef2dafde-f83e-43c8-9024-f2600658ae6e.png)

### 🟣 `Client Mode` & `AP Mode`

- [IP Cisco: `Wireless AP Modes`](https://ipcisco.com/lesson/wireless-access-point-modes/)

**`Client Mode` y `AP Mode` son `modos de operación` utilizados en redes inalámbricas 802.11 (Wi-Fi).**

### ⭕ `AP (Access Point) Mode`

- El Modo de Punto de Acceso es el modo de operación por defecto de un punto de acceso Wi-Fi, el cual permite que los dispositivos clientes se conecten a la red inalámbrica y accedan a los recursos de la red cableada a través del punto de acceso. 
- El AP se encarga de la gestión de la red, incluyendo la asignación de direcciones IP, la autenticación y el cifrado. <br><br>

![image](https://user-images.githubusercontent.com/94720207/227803837-ce12bd19-6c01-4aa4-8d33-7bbf501a51c4.png)

![image](https://user-images.githubusercontent.com/94720207/227820777-2fecc6ff-f2ea-4bf9-a9e4-a50cb1d7e94d.png)

| **Name**                  	| **Mode** 	| **Descripción**                                                                                                                        	|
|---------------------------	|----------	|----------------------------------------------------------------------------------------------------------------------------------------	|
| **Root Mode**             	| AP       	| El modo predeterminado para un AP. El AP funciona como un portal hacia una red cableada (LAN).                                         	|
| **Mesh Mode**             	| AP       	| El AP funciona como un Wireless Backhaul Radio para un entorno Mesh.                                                                   	|
| **Sensor Mode**           	| AP       	| El AP se convierte en un radio sensor, lo que le permite integrarse en un sistema Wireless Intrusion Detection System (WIDS).          	|
| **Bridge Mode**           	| AP       	| El radio del AP se convierte en un Bridge inalámbrico.                                                                                 	|
| **Workgroup Bridge Mode** 	| AP       	| El radio del AP se transforma en un Working Group Bridge, proporcionando enlace ascendente inalámbrico para clientes 802.3 conectados. 	|


### ⭕ `Client Mode`

- El Modo Cliente es un modo de operación en el cual un dispositivo inalámbrico actúa como un cliente en una red Wi-Fi. 
- En este modo, el dispositivo se conecta a un punto de acceso inalámbrico, similar a como lo hace un ordenador portátil o un teléfono móvil, y accede a los recursos de la red a través de ese punto de acceso. 

El `Client Mode` incluye los modos `Ad-Hoc Mode` e `Infraesctucture Mode`:

![image](https://user-images.githubusercontent.com/94720207/227801827-6ff3cbbe-a14e-4824-afa6-d85ba75af6a6.png)




| **Name**                	| **Mode** 	| **Descripción**                                                                                             	|
|-------------------------	|----------	|-------------------------------------------------------------------------------------------------------------	|
| **Infrastructure Mode** 	| Client   	| El cliente permitirá la comunicación a través de un AP. Esto permite que el cliente participe en BSS o ESS. 	|
| **Ad-Hoc Mode**         	| Client   	| Todas las comunicaciones son de igual a igual y no se comunican con un AP.                                  	|








