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
