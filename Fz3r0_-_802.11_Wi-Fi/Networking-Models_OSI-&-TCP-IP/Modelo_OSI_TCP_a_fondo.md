## 💀 `Modelo OSI` para el `CWAP`, by `Fz3r0 💀` 

Antes que nada, quisiera destacar que tanto para las certificaciones de `CWNP` como lo es el `CWAP`, **NO se utiliza el `Modelo TCP/IP`**, sino que **se basa en el `Modelo OSI`**, sin embargo, se utiliza únicamente como referencia _(¡Hay que recordar que el `OSI Model` es un modelo de referencia!)_.

![image](https://user-images.githubusercontent.com/94720207/233547224-ea09d28c-e72f-44e9-8242-fd61dc2b8da4.png)

Al principio, puede resultar confuso cuando se mencionan los cursos de CWNP _(además de otras certificaciones de Networking)_ cosas como: 

- _"...No estamos usando el modelo OSI, solo hacemos referencia para que se comprenda el concepto..."_. 

A partir de ahí se de una explicación de X o Y tecnología o proceso de comunicación... ¡Pero! quizás en otro curso u otra tecnología pareciera que el modelo OSI se comportara un poco diferente en ciertos layers y ya no toma mucho sentido lo aprendido antes ¡¿Por qué ocurre esto?! 

Es porque el modelo OSI solo es una referencia y no son leyes inamovibles. Por ejemplo, el modelo OSI consta de 7 layers, pero existe una estructura un poco más compleja dentro de esas 7 capas, donde quizás para detallar una capa más a fondo pareciere que se pueden sacar más capas; u otras capas no existen y no son utilizadas en determinado escenario... Es decir, no siempre se tiene que seguir exactamente la misma regla para todas las posibilidades que nos ofrece el Networking en general, por ejemplo, un red Wireless no funcionará igual que una red cableada fisicamente, sin embargo ambos tienen Layer 1 y Layer 2, pero para lograr comprender cómo realmente funciona desde la raíz, debemos ir más allá de el báscio `Layer 1` y `Layer 2`, o únicamente de `7 Layers` del `Modelo OSI "tradicional"`

El _"truco"_ que he encontrado para comprender completamente el proceso de transmisión Wireless y que será esencial para esta certificación consiste en **"añadir un sublayer al modelo original"**. ¿A qué me refiero con esto? Es muy fácil:

- El modelo OSI se divide en siete capas o `7 layers`, cada una con una función específica. Pero para comprender mejor el proceso de transmisión, es bastante útil agregar un sublayer adicional en `Layer 2 Data Link` que se centra en la transmisión de datos a través del medio físico, lo cual también convierte `Layer 1 Physical` en otro `sublayer`.

El resultado final es sencillo:

- En lugar de 2 "layers", se tendrán 3 "sublayers", ya que se convierte Layer 1 y Layer 2 en en total de 3 sublayers _(en lugar de solo 2 layers)_.

Esto se puede visualizar así:

![image](https://user-images.githubusercontent.com/94720207/229313916-c727db5a-1785-48d8-a687-be6793b49a84.png)

### Layers en `OSI original`

2. Layer 2 - `Data Link`
1. Layer 1 - `Physical`

### Layers en `OSI Fz3r0 Custom`

2. Upper Sublayer 2 - `LLC`
2. Lower Sublayer 2 - `MAC`
1. Sublayer 1 - `PHY`

Es importante solo recordar que "El sublayer MAC, también es parte del sublayer PHY", explicaré más a detalle este proceso en el siguiente bloque.

---

### 🟢 ISO/IEC 7498-1:1994 Information technology - Open Systems Interconnection (OSI) -- Basic Reference Model: The basic model

- [OSI/IEC Reference Model - Second Edition 1994](https://standards.iso.org/ittf/PubliclyAvailableStandards/s020269_ISO_IEC_7498-1_1994(E).zip)
- [Sunny - OSI Model](https://www.youtube.com/watch?v=nFnLPGk8WjA)

El modelo OSI (Open Systems Interconnection) es un modelo de referencia para la comunicación de datos entre sistemas abiertos, es decir, sistemas que están diseñados para comunicarse con otros sistemas de manera estándar y no necesariamente están basados en una tecnología específica. Fue desarrollado por la Organización Internacional de Normalización (ISO) en la década de 1980 y se compone de siete capas, cada una de las cuales tiene una función específica en la comunicación de datos.

El modelo OSI proporciona una forma estandarizada y estructurada de dividir el proceso de comunicación de datos en capas lógicas, lo que facilita la comprensión y el diseño de sistemas de comunicación. Cada capa del modelo OSI tiene una función bien definida y se comunica con las capas adyacentes para lograr la transferencia de datos a través de una red. La ventaja de este modelo es que permite la interoperabilidad entre sistemas de diferentes fabricantes y tecnologías, ya que todos ellos siguen las mismas normas y estándares para la comunicación de datos.

El ISO/IEC (International Organization for Standardization/International Electrotechnical Commission) es un organismo internacional que se dedica a establecer estándares en diversos campos, incluyendo la tecnología de la información y las comunicaciones.

El modelo OSI fue desarrollado por la Organización Internacional de Normalización (ISO) en 1984 y formalmente publicado en 1985 como el estándar ISO/IEC 7498-1. El ISO y la Comisión Electrotécnica Internacional (IEC) a menudo colaboran en el desarrollo de estándares técnicos, y es por eso que el modelo OSI también se conoce como ISO/IEC 7498-1.

Las diferentes versiones del modelo OSI han surgido a medida que se han desarrollado nuevas tecnologías y necesidades de comunicación. Por ejemplo, el modelo OSI originalmente solo tenía siete capas, pero posteriormente se agregó una octava capa (la capa de gestión de red) para abordar la administración de redes. Además, se han desarrollado modelos más específicos para aplicaciones y dispositivos específicos, como el modelo de referencia TCP/IP, que es ampliamente utilizado en Internet.

El `OSI model` originalmente se basa en `7 layers`, a grandes rasgos estos son los layers y la función de cada uno: 

| **Layer** 	|     **Name**     	|   **Protocol Data Unit (PDU)**   	|                                                                       **Función**                                                                      	|
|:---------:	|:----------------:	|:--------------------------------:	|:------------------------------------------------------------------------------------------------------------------------------------------------------:	|
|   **7**   	|  **Application** 	|               Data               	| Interactúa con aplicaciones de software que implementan un componente de comunicación.                                                                 	|
|   **6**   	| **Presentation** 	|               Data               	| Traduce, encripta y/o comprime datos en un formato que pueda ser entendido por el sistema receptor.                                                    	|
|   **5**   	|    **Session**   	|               Data               	| Maneja sesiones de comunicación entre aplicaciones y establece, gestiona y termina conexiones.                                                         	|
|   **4**   	|   **Transport**  	| Segment (TCP) <br>Datagram (UDP) 	| Proporciona entrega confiable (TCP) o no confiable (UDP) de datos entre dispositivos de red y maneja el control de flujo y la verificación de errores. 	|
|   **3**   	|    **Network**   	|              Packet              	| Determina la mejor ruta para que los datos viajen desde el remitente al receptor y maneja la dirección lógica y el enrutamiento.                       	|
|   **2**   	|   **Data Link**  	|               Frame              	| Transfiere datos entre dispositivos de red y maneja la dirección física, la corrección de errores y el control de flujo.                               	|
|   **1**   	|   **Physical**   	|                Bit               	| Convierte los datos a un formato que se puede transmitir por la red física y maneja los medios, la señal y la transmisión de datos.                    	|

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228987616-e7b59209-5fff-4e1e-b9b2-5c2cf81051d2.png" alt="Modelo OSI" height=820px/> </a> </p> 

- [networkwalks-summary-cheatsheets](https://networkwalks.com/networkwalks-summary-cheatsheets/)

---

### 🟢 Modelo OSI "Fz3r0 WiFi Custom"

- En este modelo se agregan las sublayers correspondientes de las que tanto se hablan en el curso, donde `layer 1` y `layer 2` se convierten en una especia de `sub-layers`. 
- La `MAC sublayer` existe tanto el `layer 1` como en `layer 2`, pero para fines prácticos que se ven más adelante durante `Encapsulation` y `Frame Aggregation` el truco está en plasmarlo en una tabla esas 3 capas como `sublayers`: <br>
    - Mientras que `MAC sublayer` permanece aparentemente solo en `layer 2`, en realidad esa es la `lower sublayer` de `layer 2`
    - Es decir, la `MAC sublayer` también "baja" hacia `layer 1 physical`. 

En este modelo existen 3 sublayers en total:

1. `LLC` - `Layer 2`
2. `MAC` - `Layer 2 & Layer 1`
3. `PHY` - `Layer 1`

La manera más páctica que encontré de representarlo en una tabla, y de hecho, el que utilizaré muy seguido en este write-up es la siguiente: 

| **Layer** 	|              **Name**              	| **Protocol Data Unit (PDU)** 	| **Sublayer Name**                                     	| **Sublayer PDU** 	|                                                                          **Función**                                                                          	|
|:---------:	|:----------------------------------:	|:----------------------------:	|-------------------------------------------------------	|:----------------:	|:-------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
|   **7**   	|             Application            	|             Data             	|                                                       	|         -        	| Interactúa con aplicaciones de software que implementan un componente de comunicación.                                                                        	|
|   **6**   	|            Presentation            	|             Data             	|                                                       	|         -        	| Traduce, encripta y/o comprime datos en un formato que pueda ser entendido por el sistema receptor.                                                           	|
|   **5**   	|               Session              	|             Data             	|                                                       	|         -        	| Maneja sesiones de comunicación entre aplicaciones y establece, gestiona y termina conexiones.                                                                	|
|   **4**   	|              Transport             	| Segment (TCP) Datagram (UDP) 	|                                                       	|         -        	| Proporciona entrega confiable (TCP) o no confiable (UDP) de datos entre dispositivos de red y maneja el control de flujo y la verificación de errores.        	|
|   **3**   	|               Network              	|            Packet            	|                                                       	|         -        	| Determina la mejor ruta para que los datos viajen desde el remitente al receptor y maneja la dirección lógica y el enrutamiento.                              	|
|   **2**   	| **Data Link <br>(upper sublayer)** 	|      **Data Link Frame**     	| **LLC <br>Logical-Link-Control <br>(upper sublayer)** 	|     **LPDU**     	| Se encarga de la interconexión de los dispositivos en la misma red física y maneja el acceso al medio físico.                                                 	|
|   **2**   	| **Data Link <br>(lower sublayer)** 	|      **Data Link Frame**     	| **MAC <br>Media-Access-Control <br>(lower sublayer)** 	|     **MPDU**     	| Se encarga de la interconexión de dispositivos en redes diferentes y maneja la detección y corrección de errores en la capa física.                           	|
|   **1**   	|            **Physical**            	|   **Physical Layer Frame**   	| **PHY <br>Logical-Link-Control**                      	|     **PPDU**     	| Convierte los datos en un formato que puede ser transmitido a través de la red física y maneja la transmisión y recepción de datos a través del medio físico. 	|

Sin embargo, para que se comprenda al 100% como "baja" la `MAC Sublayer` desde `layer 2` hacia la `layer 1`, la mejor manera es representarlo en una tabla donde se deben combinar celdas para poder detallar con exactitud a lo que me refiero: 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/227751705-c561fa0f-16ed-4785-9f53-f8dfe6ceecaa.png" alt="Modelo OSI" height=320px/> </a> </p> 



Ahora que ya se tiene el concepto visual de como se distribuyen las `sublayer 1 - PHY`, `sublayer 2 lower - MAC` y `sublayer 2 upper - LLC`, es así como se vería el modelo OSI completo (sin embargo, siempre utilizaré la tabla que presenté anteriormente para fines prácticos):

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/227752796-9110c821-c5c2-4424-b39e-7247fc0b0954.png" alt="Modelo OSI"/> </a> </p> 


Ahora, lo mismo pasa en un escenario real, por ejemplo al visitar una página `http` donde el `payload` sea un archivo `password.txt`, este va a seguir siendo un paquete `TCP` justo como el ejemplo anterior, pero visto desde `Baclkshark`

````sh
python3 -m http.server 666
````

1. Hago un `HTTP Server` en python3, utilizando el directorio de `CWAP` donde tengo un archivo `.txt`

![image](https://user-images.githubusercontent.com/94720207/235366670-4813c8df-4e5f-40c8-b7e2-86391bf49d2d.png)

2. Si entro desde mi otra PC puedo ver el servicio desde cualquier explorador y puedo descargar el `.txt`

![image](https://user-images.githubusercontent.com/94720207/235366956-edce3a71-d5a2-47c3-9cbe-c1c028c08416.png)

- Es en el momento desde que se da click a la URL así como en el momento que se descarga el archivo cuando se crea tráfico TCP
- Si yo pusiera un `sniffer` a escuchar el tráfico entre las 2 PCs, podrá capturar ese tráfico HTTP

---

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

La certificación CWAP (Certified Wireless Analysis Professional) se centra en la comprensión y la resolución de problemas en redes inalámbricas, y por lo tanto, se enfoca principalmente en las capas más bajas del modelo OSI (las capas físicas, de enlace de datos y de red). La certificación CWAP está diseñada para evaluar las habilidades de los profesionales de redes inalámbricas en áreas como la planificación, el diseño, la implementación, la resolución de problemas y la optimización de redes inalámbricas. <br>

Las capas superiores del modelo OSI (capas de sesión, presentación y aplicación) se centran en la comunicación entre aplicaciones y procesos en diferentes dispositivos de red, y no están directamente relacionadas con las redes inalámbricas. 

**Por lo tanto, la certificación CWAP no incluye estas capas superiores, ya que no son relevantes para la evaluación de las habilidades de los profesionales de redes inalámbricas.** <br>

Sin embargo, es importante tener en cuenta que el modelo OSI es solo un modelo de referencia y que en la práctica, los diferentes protocolos y tecnologías de red pueden implementarse de manera diferente y no necesariamente seguir el modelo OSI de manera estricta. Por lo tanto, los profesionales de redes inalámbricas también pueden necesitar tener conocimientos y habilidades en las capas superiores del modelo OSI, dependiendo de las necesidades específicas de su trabajo.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/227809209-1263ebe3-035a-4373-8a29-e77bfdae2075.png" alt="Modelo OSI" height=270px/> </a> </p> 

El modelo OSI (Open Systems Interconnection) es un modelo de referencia para la comunicación de redes de computadoras que se divide en siete capas. Las capas se agrupan en dos secciones: la sección inferior, que consta de las capas físicas y de enlace de datos, y la sección superior, que consta de las capas de red, transporte, sesión, presentación y aplicación.

Las capas superiores, también conocidas como "upper layers", son las capas 5, 6 y 7. Estas capas se centran en la comunicación entre aplicaciones y procesos en diferentes dispositivos de red.

### La Capa 5 - Capa de Sesión: 

Esta capa se encarga de establecer, mantener y terminar sesiones de comunicación entre dispositivos. También controla la sincronización de datos y la recuperación de errores en la comunicación. La capa de sesión proporciona servicios que permiten que las aplicaciones se comuniquen a través de la red, como la autenticación, la autorización y la gestión de permisos de acceso.

### La Capa 6 - Capa de Presentación: 

Esta capa se encarga de la representación de datos y de la gestión de formatos y codificaciones. Su objetivo es garantizar que los datos se presenten de la manera adecuada, independientemente del formato en que se envíen. La capa de presentación realiza tareas como la conversión de formatos de datos, la compresión y la encriptación de datos.

### La Capa 7 - Capa de Aplicación: 

Esta capa es la capa más alta del modelo OSI y se encarga de proporcionar servicios de red a las aplicaciones del usuario final. La capa de aplicación proporciona una interfaz entre la red y las aplicaciones, permitiendo que las aplicaciones accedan a los servicios de red, como el correo electrónico, la transferencia de archivos y el acceso a bases de datos.

---

### 🟣 Funcionamiento de los Layers

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

### IEEE 802.11 Frame Structure

- [IEEE 802.11 MAC Frame](https://www.geeksforgeeks.org/ieee-802-11-mac-frame/)

![image](https://user-images.githubusercontent.com/94720207/227808549-e7246deb-16a2-48ef-91ff-96224c99fae4.png)


### Layer 1: `Physical Layer Frame`

- En `Layer 1 (Physical Layer)`, un frame se refiere a un `conjunto de bits` que se transmiten en la red en una única transmisión. 
- Estos bits se organizan en un formato específico para que puedan `ser enviados a través de medios físicos como cables, fibra óptica o ondas de radio`. 
- El formato de estos bits se llama `Physical Layer Frame`.

### Layer 2: `Data Link Layer Frame`

- En `Layer 2 (Data Link Layer)`, un frame se refiere a un `paquete de datos` que se transmite entre dispositivos de red en una red local. 
- Este paquete de datos incluye `información de control adicional`, como `direcciones de origen y destino`, que permiten que los dispositivos de red se comuniquen entre sí de manera efectiva. 
- El formato de estos paquetes se llama `Data Link Layer Frame`.

## `Layer 4` Transport

- [Sunny - TCP vs. UDP](https://www.youtube.com/watch?v=SLY4Ud53UGs)

La Capa 4 del modelo OSI es la capa de transporte, y su función principal es proporcionar un medio para que los procesos de aplicaciones en diferentes dispositivos puedan establecer, mantener y terminar conexiones de comunicación. <br>

En esta capa se encuentran **2 protocolos principales**: `TCP` y `UDP`.

- La `Layer 4 Transport` sirve para **`Propoprcionar un Medio (Lógico)`**, es decir, **similar a un cable (medio físico), la capa de transporte utiliza un medio pero a nivel de software (lógico) para transmitir datos.**
- Este medio en realidad son un conjunto de servicios y protocolos que permiten a los procesos de aplicaciones en diferentes dispositivos establecer y gestionar una conexión de comunicación extremo a extremo.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223029378-5c82410f-0388-4e63-8fe1-1c968da26008.png" alt="Transport" height=300px/> </a> </p> 

### `TCP` - Transmission Control Protocol

- `TCP`: Protocolo orientado a conexión y confiable. `Connection-oriented and Reliable`
- Proporciona 
de comunicación extremo a extremo que garantiza que los datos enviados sean recibidos en el orden correcto y sin errores `ACK`, `Checksum`, `Seq`, etc. 
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

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/226150472-5d122e77-8fbb-486c-953f-2f57ff5e8fd2.png" alt="mac ofrmat" height=233px/> </a> </p> 


### 🚨☢️ `Importante` ☢️🚨

- Los `3 tipos de Frames` que principalmente se estudian para el `CWAP` y que forman el `MAC sublayer de 802.11` son:
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

### 💀 `Fz3r0 Pro Tip`: ¿Qué es el `Preamble`?

[WiFi Preamble Type: Short Or Long](https://routerguide.net/preamble-type-short-or-long/)

- El `preamble` es una secuencia de bits que **se incluye al inicio (prepended) de cada `physical layer frame` transmitido ya sea en una red `LAN-Ethernet` o `WLAN-WiFi`.
- En `WLAN WiFi` el `preamble` se utiliza en la `physical sublayer` de la `layer 2 data link (MAC)`
- En `LAN Ethernet` el `preamble` incluye en la trama Ethernet en la `physical sublayer` de `layer 2 data link`.

El propósito del `preamble` es **permitir a los dispositivos receptores `sincronizarse` con el `data frame` entrante y `ajustar su reloj interno` para asegurar que la información se reciba de manera correcta. La secuencia de bits en el "preamble" es siempre la misma, lo que facilita la sincronización. <br>

#### `preamble` en `ethernet LAN`

El "preamble" consta de 7 bytes (56 bits) y es seguido por el "start of frame delimiter" (SFD), que indica el comienzo de la trama de datos y tiene un valor fijo de 10101011. Juntos, el "preamble" y el SFD forman los primeros 8 bytes de la trama Ethernet y permiten a los dispositivos receptores detectar el inicio de la trama y sincronizar su reloj interno con el transmisor.

en que layer funciona 

 y se 


En el caso de Wi-Fi, el "preamble" se utiliza en la subcapa física de la capa de enlace de datos (MAC) y también tiene como objetivo permitir la sincronización de los dispositivos receptores con la trama de datos entrante y ajustar su reloj interno para asegurar la correcta recepción de los datos. Sin embargo, en Wi-Fi, el "preamble" es diferente al de Ethernet y tiene una longitud variable en lugar de una longitud fija de 7 bytes.

en wifi 

El "preamble" en las redes inalámbricas basadas en IEEE 802.11, como Wi-Fi, es una secuencia de bits que se incluye al principio de cada trama de datos transmitida.

El propósito del "preamble" en Wi-Fi es permitir a los dispositivos receptores sincronizarse con la trama de datos entrante y ajustar su reloj interno para asegurar que la información se reciba correctamente. Además, el "preamble" también se utiliza para informar a los dispositivos receptores sobre la velocidad de transmisión que se utilizará para transmitir los datos.

El "preamble" en Wi-Fi consta de una secuencia de bits de 56 u 80 microsegundos de duración, conocida como "Short Preamble" o "Long Preamble", respectivamente. Esta secuencia de bits se transmite antes de la trama de datos y consta de dos partes: la "Sync Sequence" y la "Signal" o "Start Frame Delimiter" (SFD).

La "Sync Sequence" es una secuencia de 10 u 30 microsegundos de duración, que se utiliza para permitir a los dispositivos receptores sincronizarse con la señal entrante.
La "Signal" o "Start Frame Delimiter" es una secuencia de 2 u 4 microsegundos de duración, que indica el comienzo de la trama de datos y se utiliza para informar a los dispositivos receptores sobre la velocidad de transmisión que se utilizará para transmitir los datos.
En resumen, el "preamble" en las redes inalámbricas basadas en IEEE 802.11, como Wi-Fi, es una secuencia de bits que se utiliza para sincronizar los dispositivos receptores con la trama de datos entrante, informarles sobre la velocidad de transmisión que se utilizará y asegurar la correcta recepción de los datos.

### Short Preamble VS Long Preamble

Normalmente el "Long Preamble" es más utilizado en redes Wi-Fi de alta velocidad, ya que es necesario para las tasas de datos más altas, como 54 Mbps. Por lo tanto, se puede decir que el "Long Preamble" es adecuado para redes inalámbricas más modernas y rápidas.

Por otro lado, el "Short Preamble" se utiliza en redes Wi-Fi más antiguas y de menor velocidad, ya que se diseñó originalmente para soportar tasas de datos de hasta 20 Mbps. También es importante tener en cuenta que el uso del "Short Preamble" puede ahorrar tiempo en la transmisión y reducir el consumo de energía.

**La elección entre el "Short Preamble" y el "Long Preamble" dependerá de las necesidades y requerimientos específicos de la red Wi-Fi en cuestión.**

- En una red Wi-Fi más antigua o en una red que no requiere tasas de datos muy altas, el "Short Preamble" puede ser suficiente y adecuado. 
- En una red Wi-Fi más moderna y rápida que requiere tasas de datos más altas, el "Long Preamble" es necesario.
























## 🟢 `Network Frames` - `Data Link (MAC) Layer`

- Los `Network Frames` operan en la `Layer 2 - Data Link` del modelo `OSI`.
- Se utilizar para proveer comunicaciones en una red LAN y están basados típicamente, en `Medium Access Control (MAC) Addresses` (Direcciones MAC).
- Lo mismo ocurre tanto para redes cableadas `LAN`, como redes inalámbircas `WLAN`.

Para saber analizar los frames del tráfico de red, primero se deben conocer con conceptos como lo son `Encapsulation` y `Frame Aggregation`

### 🟣 `Encapsulation`

- Mientras los `datos` se mueven `de ARRIBA hacia ABAJO` en el modelo `OSI` los datos se `encapsulan` para su `delivery` (entrega).

Cada `layer` del modelo OSI se puede conceptualizar **como si se comunicara con la capa del mismo nivel en la STA de destino.** 

- Por ejemplo: La `network layer 3 (AP Address)` del dispositivo `source`, se comunicará con la `network layer 3 (AP Address)` del dispositivo `destination`; así mismo con cada uno de los layers.

Cada `layer` depende del `layer` que se encuentra debajo para poder proveer comunicación. 

- Por ejemplo: Un `IP packet (layer 3)` destinado a `192.168.1.2` que fue enviado desde `192.168.1.1`, depende de la `Data Link (layer 2)` para comunicaciones basadas en `MAC Address (layer 2)`, a pesar que las `IP Addresses (layer 3)` se encuentren en la misma subnet. 
- Después, la `Data Link (layer 2) MAC` **encapsula** el `Network (layer 3) IP Packet` poniendo antes o `prepending` un `frame header`, y poniendo después o `appending` un `FCS (Frame Check Sequence)` para detectar errores en la transmisión. 

![image](https://user-images.githubusercontent.com/94720207/226181901-cf64e1f6-27fc-4895-910e-428ec33326d2.png)

### ⚠️ **`CWAP Definition`** ⚠️ 

- `Encapsulation` - Is the process of of **prepending and/or appending information to a message for `transmission`** (communication) `TO a peer`.
- `Decaspulation` - Is the process of **reading, processing and removing prepended and/or appended information for `reception`** (communication) `FROM a peer`.
- `Encapsulation` is the process of **enclosing upper-layer information into the current layer's delivey format**. For example, IP packets encapsulate TCP datagrams or messages, and 802.11 frames encapsulate IP packets. 

_La encapsulación es el proceso de "encerrar" la información de `layers` superiores en el formato de entrega de la `layer` actual. Por ejemplo, los `IP packets` encapsulan `datagramas o mensajes TCP`, y los `frames 802.11` encapsulan `IP packets`._

---

### ⭕ `Service Data Units (SDU)` & `Protocol Data Units (PDU)` in the OSI Model

[Unidad de datos de servicio `SDU`](https://es.wikipedia.org/wiki/Unidad_de_datos_de_servicio#Relaci%C3%B3n_con_la_PDU)

- **`SDU` (Service Data Unit)**: Datos que se mantienen inalterados entre capas pares y se van transmitiendo en forma transparente a través de la red.
- **`PDU` (Protocol Data Unit)**: UDS más la información de control (Header) de ese nivel. 

La diferencia es que la `PDU` de una capa, **especifica el conjunto de datos a enviar al protocolo par ubicado en el receptor**, mientras que la `SDU` **es el conjunto de datos que proviene de la capa superior, aún no encapsulada**. 

**Es decir, el `SDU` de cada capa corresponderá a la porción de `datos (payload)` de la `PDU` de la misma capa. Se podría decir que el `SDU` es lo que va dentro de un `PDU`**

![image](https://user-images.githubusercontent.com/94720207/226130762-5342bd37-d22e-4879-a3af-7920b06c4103.png)

**El SDU es como un paquete que un nivel superior entrega a un nivel inferior, mientras que el PDU es como una caja que cada nivel envuelve al paquete antes de entregárselo al siguiente nivel inferior.** <br>

Cada layer cuenta con su propio `PDU` y `SDU` que lo identifica, por ejemplo el `MPDU` y `MSDU` que sirven a `layer 2 MAC`; lo mismo pasa con los `PPDU` y `PSDU` de `layer 1 PHY`: 

![image](https://user-images.githubusercontent.com/94720207/226131377-5e0059bf-31f0-42df-bacb-4220ded4cd11.png)

#### 🪬 `PDU`

- Un `PDU (Protocol Data Unit)` es una `unidad de información` que se usa en la **comunicación entre los diferentes niveles de la red**. 
- **Cada nivel agrega su propio `PDU` y lo envía al siguiente nivel para que lo procese.**

#### 🪬 `SDU`

- Un `SDU (Service Data Unit)` es `toda la información` que **un nivel recibe del nivel superior para `procesarla y convertirla en su propio PDU`**. - Es decir, **es la información que se entrega `de un nivel superior a un nivel inferior`.**

#### 🪬 `MSDU` : `Layer 2: MAC`

- **Un `MSDU (MAC Service Data Unit)` simplemente equivale al `SDU` que se utiliza específicamente a nivel de `layer 2 - data link - MAC`.**
- Un `MSDU` se refiere a los datos que se entregan desde la capa de red al nivel de enlace de datos para su posterior procesamiento.

![image](https://user-images.githubusercontent.com/94720207/226147231-c788bb67-b987-44dc-8f09-75b56413e68c.png)

En otras palabras, un `MSDU` es un `conjunto de datos` que se entrega **desde arriba** `layer 3 network` **hacia abajo** `layer 2 - data link` para su **posterior encapsulamiento** en un `MPDU`.

#### 🪬 `MPDU` : `Layer 2: MAC`

- **Un `MPDU (MAC Protocol Data Unit)` simplemente equivale al `PDU` que se utiliza específicamente a nivel de `layer 2 - data link - MAC`.**
- Un `MPDU` consta de un `header` y un `body`.
- El `header` incluye información de `control`, como las direcciones de `origen` y `destino`
- El `body` contiene los `datos / payload` que se transmitirá.

![image](https://user-images.githubusercontent.com/94720207/226146355-9a2aed7f-9143-4b41-9179-076abc2a7534.png)


En el nivel de `layer 2 - data link`, **los `MSDU` se encapsulan en `MPDU` antes de ser transmitidos en la red.**

#### 🪬 `PSDU` : `Layer 1: PHY`

- **Un `PSDU (Physical Service Data Unit)` simplemente equivale al `SDU` que se utiliza específicamente a nivel de `layer 1 - physical - PHY`.**
- Es `PSDU` el conjunto de datos que se entregan desde arriba la capa de enlace de datos al nivel físico para su posterior procesamiento y transmisión.
- La PSDU incluye tanto los datos que se transmitirán como los encabezados de la capa física necesarios para la transmisión.

![image](https://user-images.githubusercontent.com/94720207/226147253-40389e22-7664-43ff-ba32-eca2d2e06282.png)

En otras palabras, un `PSDU` es un `conjunto de datos` que se entrega **desde arriba** `layer 2 - data link` **hacia abajo** `layer 1 - physical` para su **posterior encapsulamiento** en un `PPDU`.

#### 🪬 `PPDU` : `Layer 1: PHY`

- **Un `PPDU (Physical Protocol Data Unit)` simplemente equivale al `PDU` que se utiliza específicamente a nivel de `layer 1 - physical - PHY`.**
Un PPDU (Physical Protocol Data Unit) es una unidad de datos de protocolo físico que se utiliza en el nivel físico del modelo OSI.
Es la unidad de datos que se transmite físicamente en la red, y que incluye tanto los datos que se transmitirán como los encabezados de la capa física necesarios para la transmisión.

![image](https://user-images.githubusercontent.com/94720207/226147447-c18bd2bd-905d-459d-8e8a-734bdeb20c84.png)

**La PPDU es el resultado de encapsular la PSDU en los encabezados de la capa física, y es lo que se transmite a través del medio físico de la red. Es decir, a través del aire por medio de radio frecuancias moduladas.**

### `Fz3r0 Pro Tip`: El ejemplo del `Beacon Frame` y los `PPDU`

Se podría decir que **CASI SIEMPRE** los `PPDU` que se transmiten en el `wireless medium` (osea por el aire), contienen los datos del `payload` que viene desde capas superiores que se han ido `encapsulando` a lo largo de los `layers` del `modelo OSI`, hasta llegar a la `layer 1 PHY`... <br>

Sin embargo, hay algunos casos donde no necesariamente viene desde `layers superiores` el frame `PPDU`, por ejemplo, los `beacon frames` son `control frames` que envía directamente el `Access Point` hacia el `wireless medium` en forma de `broadcast` cada `102.4 ms`. <br>

El `beacon frame` es un `layer 2 frame - data link` que se genera directamente por el `AP (Acess Point)` y proveé la información del `BSS (Basic Service Set)` para que un cliente `STA (Station)` pueda conectarse a la red Wireless. <br>

Entonces está bien decir que: 

- **El `PPDU` del `Beacon Frame` no viene de `layers` superiores, sino que se origina en `layer 2` por el `AP` y se envía directamente hacia `layer 1`.** 
- **Entonces, un `PPDU` de `Beacon Frame` no cuenta con información por ejemplo de: `IP Address (Layer 3)` o  `TCP/UDP Protocols (Layer 4)`**

### 👹 `Fz3r0 Table` : `SDU` + `PDU` + `MSDU` + `MPDU` + `PSDU` + `PPDU`

- En la siguiente tabla hice el modelo para que se comprenda más la encapsulación de los `SDU` y `PDU`. 
- Se especifican los nombres de los `SDU` y `PDU` de cada `layer` determinada. (`LSDU, LPDU` & `MSDU, MPDU` & `PSDU, PPDU`)
- Se pone mayor detalle en `layer 1` y `layer 2` que es la que más nos interesa para el `CWAP`. 

|      **Layer**     	|  **OSI Layer** 	|                       **Sublayer**                       	|  **PDU** 	|            **PDU Name**            	|  **SDU** 	|            **SDU Name**            	|     **Technology**    	|
|:------------------:	|:--------------:	|:--------------------------------------------------------:	|:--------:	|:----------------------------------:	|:--------:	|:----------------------------------:	|:---------------------:	|
| _7_                	| _Application_  	| _-_                                                      	| _ADU_    	| _Application Data Unit_            	| _-_      	| _User Data_                        	| _Data_                	|
| _6_                	| _Presentation_ 	| _-_                                                      	| _PD_     	| _Presentation Data_                	| _-_      	| _User Data_                        	| _Data_                	|
| _5_                	| _Session_      	| _-_                                                      	| _SD_     	| _Session Data_                     	| _-_      	| _User Data_                        	| _Data_                	|
| _4_                	| _Transport_    	| -                                                        	| -        	| _Segment (TCP) <br>Datagram (UDP)_ 	| _-_      	| _User Data_                        	| _TCP/UDP_             	|
| _3_                	| _Network_      	| -                                                        	| -        	| _Packet_                           	| _-_      	| _Datagram_                         	| _IP_                  	|
| **2** <br> _upper_ 	| **Data Link**  	| **LLC <br>(Logical Link Control)** <br> (upper sublayer) 	| **LPDU** 	| **LLC <br>Protocol Data Unit**     	| **LSDU** 	| **LLC <br>Service Data Unit**      	| **Ethernet/Wireless** 	|
| **2** <br> _lower_ 	| **Data Link**  	| **MAC <br>(Media Access Control)** <br> (lower sublayer) 	| **MPDU** 	| **MAC <br>Protocol Data Unit**     	| **MSDU** 	| **MAC <br>Service Data Unit**      	| **Wireless**          	|
| **1**              	| **Physical**   	| **PHY <br>(Physical Layer)**                             	| **PPDU** 	| **PHY <br>Protocol Data Unit**     	| **PSDU** 	| **Physical <br>Service Data Unit** 	| **Wireless**          	|



