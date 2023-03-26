<!-- 

Y ARRANCAN!!!


<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Hacia la cima del `CWAP-402`: <br> `Certified Wireless Analysis Professional` 📡🔍🦈  

![image](https://user-images.githubusercontent.com/94720207/226141680-289c202f-47d7-48d8-b61a-950372a58da0.png)
_Writeup y bitácora para la certificación **CWAP-402** de **CWNP (Certified Wireless Network Professional)**_ <br>
_por @ **Fz3r0 💀** (CWNA)_



## 🗂️ `ÍNDICE`


 
### [🟢 `Introducción`]()
- [🚨 Importante]()

### [🏔️ `La analogía del CWAP y una expedición al K2`]() 
- [🟣 Bottleneck & Serarc = Examen CWAP-404 @ Pearson Veu]()
- [🟣 Cima del K2 = Certifcación como Ingeniero CWAP-404]()

### [🟢 `Introducción`]()
- [🚨 Importante]()

## 🟢 `Introducción`


La certificación **`CWAP (Certified Wireless Analysis Professional)`**, otorgada por la prestigiosa organización **`CWNP (Certified Wireless Network Professional)`**, representa una credencial de alto nivel en el ámbito de las redes inalámbricas. Diseñada específicamente para aquellos profesionales que buscan demostrar su competencia en el análisis avanzado y resolución de problemas en entornos de redes inalámbricas, esta certificación implica un conocimiento profundo de los protocolos de red, la seguridad de la red inalámbrica y el diseño de redes inalámbricas de alto rendimiento. <br>

Los profesionales que buscan obtener la certificación `CWAP` deben demostrar un amplio conocimiento de los principios y técnicas de análisis de redes inalámbricas, protocolos, así como habilidades para resolver problemas complejos y mejorar tanto rendimiento como la seguridad de redes inalámbricas. <br>

Los temas abordados en la certificación `CWAP` incluyen la **captura y análisis de tráfico inalámbrico, análisis de espectro, la identificación y solución de problemas de cobertura y rendimiento, el análisis de interferencias y la aplicación de soluciones de seguridad inalámbrica**. A través de la certificación `CWAP`, los profesionales pueden demostrar su experiencia en la gestión y optimización de redes inalámbricas avanzadas y su capacidad para abordar los desafíos de análisis y resolución de problemas en entornos de red inalámbrica complejos. <br>

En este writeup, abordaré el camino hacia la certificación `CWAP`, cubriendo todos los temas incluidos en el plan de estudios oficial de `CWNP`. Además, profundizaré en temas que no se abordan en detalle en la documentación oficial, brindando una comprensión completa de los desafíos y soluciones en el análisis avanzado de redes inalámbricas. También incluyo mis propios laboratorios de análisis que realicé a lo largo de mi travesía: hacia la cima del CWAP. <br><br>

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/225515551-3de68463-c5b1-4573-8a22-bfa77fd7e834.png" alt="CWAP" height=165px/> </a>   </p> 

---

### 🚨☢️ `Importante` ☢️🚨

**Para presentar el examen de certificación `CWAP`, es necesario tener acreditado el examen `CWNA` y que éste se encuentre vigente.** El CWNA es un requisito previo para poder presentar el examen CWAP, ya que se considera una base fundamental en cuanto a los conocimientos y habilidades necesarios para entender y manejar el protocolo de redes inalámbricas. <br>

**Además, se recomienda tener una serie de conocimientos previos y certificaciones que pueden ser de gran ayuda para el candidato, tales como:**

#### 1. ✅ `Routing & Switching` + `Network Protocols`

- La certificación `CWAP` se enfoca en la implementación y análisis de redes inalámbricas (WiFi), pero es necesario tener conocimientos sólidos de routing y switching a nivel LAN (redes cableadas) porque las redes inalámbricas se conectan y comunican con las redes cableadas.
- Además, las redes inalámbricas se integran con la red cableada para permitir el acceso a los recursos compartidos. De hecho, tanto clientes Wireless o Wired puedes comuicarse entre si por igual  


- Por lo tanto, es importante entender la topología y arquitectura de la red a nivel de switching y routing para obtener la certificación CWAP con éxito.

Personalmente recomiendo el `Cisco CCNA`, `CompTIA Network+` y `Ruckus ICX Implementer`, que son certificaciones reconocidas en la industria que cubren los `fundamentos de networking`, incluyendo `routing` y `switching`, además de funamentos de `Wireless`. Estas certificaciones son diseñadas para proporcionar una comprensión sólida de cómo funcionan las redes, cómo se conectan y cómo se comunican los dispositivos en una red.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/226084436-c5f11a9c-9e3b-49ce-82d1-cbf5e2696775.png" alt="CWAP" height=145px/> </a>   </p> 



#### 3. ✅ `Wireless` = `CWNP: CWNA`

- Es necesario contar con la certificación CWNA, ya que esta certificación es la base fundamental para comprender el protocolo de redes inalámbricas y es obligatoria para presentar el CWAP.
- Es importante tener un conocimiento profundo sobre las tecnologías inalámbricas, incluyendo los diferentes estándares de redes inalámbricas, protocolos de seguridad, administración de redes inalámbricas, entre otros. <br> <br>

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/227316603-2adc530c-54a7-453b-9fe5-7719b71c975e.png" alt="CWAP" height=130px/> </a>   </p> 




#### 4. ✅ `Network Security` (ej. `Offensive Security: OSCP`, `Comptia: Security+`)

- Es importante tener conocimientos sólidos sobre seguridad en redes inalámbricas, incluyendo el uso de VPNs, autenticación y autorización de usuarios, cifrado de datos, entre otros. 
- En este caso, la certificación Security+ de CompTIA puede ser de gran ayuda, aunque también hay una gran gama que se pueden seleccionar, además que son temas también abordados durante el `CWNA`. <br>

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/226111039-0910d2b0-e838-4ce5-801e-3afdcc3b9a98.png" alt="CWAP" height=165px/> </a>   </p> 

#### 5. ✅ `Protocol Analysis` (ej. `Wireshark`, `TCP Dump`)

- Wireshark es una herramienta de análisis de tráfico de red gratuita y de código abierto que permite capturar y examinar el tráfico de red en tiempo real. Con Wireshark, es posible analizar el tráfico de redes cableadas e inalámbricas para solucionar problemas y detectar fallos de seguridad.
- También existen otros tipos de analizadores de protocolos, pero este writeup se centrará en `Wireshark` y en específico mi porpia modificación y perfil llamado `The BlackShark`  <br> <br> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/226084984-53d0035a-6285-4c8c-8849-1d8d0df7343b.png" alt="CWAP" height=90px/> </a>   </p> <br>

## 🏔️ La analogía del `CWAP` y una expedición al `K2` 

**La manera en la que he ajustado mi mente, cuerpo y espíritu para lograr la motivación y disciplina que representa estudiar esta certificación y documentar en este repositorio todos los recursos necesarios para salir adelante con el reto, fue imaginarlo como escalar el `K2` por la ruta `Abruzzi Spur`:**

![image](https://user-images.githubusercontent.com/94720207/224564103-b9889d9f-2bb3-4ba8-aa31-ce31bddfa949.png)

La montaña **`K2`**, también conocida como **`la "Montaña Salvaje"`**, es un coloso de hielo y roca que se eleva majestuoso en la cordillera del Karakórum, en el corazón de los Himalaya. Con una altura de más de 8.600 metros, es la segunda montaña más alta del mundo después del Monte Everest. `K2` es una de las cumbres más temibles y es un reto indomable que ha desafiado a los alpinistas más valientes y experimentados. <br>

La `Abruzzi Spur` es la vía de ascenso más icónica y desafiante del `K2`, esta ruta atraviesa la cara sureste de la montaña, presentando una serie de desafíos técnicos extremos, que incluyen empinadas escaladas en hielo y roca, peligrosas travesías y zonas expuestas a avalanchas. Los alpinistas deben enfrentar la altitud extrema y las duras condiciones climáticas que cambian rápidamente, incluyendo fuertes vientos, temperaturas bajo cero y tormentas de nieve.

La `tasa de mortalidad` en las expediciones al `K2` es asombrosamente alta, y a menudo deja una estela de tragedia y dolor en su camino. Se estima que alrededor del `25% de los alpinistas que intentan escalar el K2 no regresan con vida`, es decir, `1 de cada 4` expedicionarios mueren en el intento. Los supervivientes de estas expediciones a menudo describen el `K2` como una montaña implacable y cruel, donde los peligros acechan en cada paso.

Las expediciones que intentan subir al K2, suelen permanecer en la montaña durante varias semanas o incluso meses. El tiempo que pasan en el campamento base y los campamentos siguientes depende del plan de escalada específico de la expedición, el clima y las condiciones de la montaña. Hay años donde simplemente es imposible subir para unos y deben regresar hasta la siguiente temporada. 

Los escaladores que se aventuran en esta ruta ponen sus vidas en juego con cada paso que dan, mientras luchan contra la montaña y contra ellos mismos, poniendo a prueba su coraje, determinación, control mental y altas habilidades técnicas. 

**Cursar el `CWAP` es como la `Abruzzi Spur`, no es una certificación para principiantes y aún a los expertos puede representar un gran reto.**

---

### 🟣 `Bottleneck` & `Serarc` = Examen CWAP-404 @ Pearson Veu

El `Bottleneck` es una sección crítica de la `Abruzzi Spur`, esta zona es un corredor estrecho de hielo y roca que se encuentra a una altitud de casi 8.000 metros. Es un lugar donde el aire es escaso y el peligro es constante, lo que la convierte en un desafío extremadamente difícil para los escaladores que intentan llegar a la cima. <br>

Para tener éxito en el Bottleneck, se necesita más que solo coraje y determinación. Se requiere un conocimiento experto en la técnica, un entrenamiento riguroso en las condiciones más extremas y una habilidad sobrehumana para mantener la calma y el enfoque en medio del caos. Los expedicionarios deben ser capaces de navegar con habilidad en terrenos empinados, sobre hielo y roca, y de escalar con seguridad en condiciones extremadamente peligrosas. Deben estar preparados para enfrentar el clima adverso, la falta de oxígeno y la incertidumbre constante.

En la cima del `Bottleneck` se encuentra su majestuosa `serac`, es ahí donde se pone a prueba todo lo que los escaladores han aprendido y entrenado. La `serac` es un monstruo gigante de hielo, amenazando con hacer trizas a cualquiera que se cruce en su camino. Solo aquellos con la más alta técnica y habilidad pueden escalar con éxito a través de ella. <br>

Se dice que es en el `Bottleneck` donde tu vida deja de estar en tus manos... <br>

**El Bottleneck es el Día-D del examen para el `CWAP`, el punto de no retorno.**

![image](https://user-images.githubusercontent.com/94720207/225210926-c1e5788f-3f22-42af-994b-350232c730fb.png)

Al lograr pasar la Serarc, el camino a la cima son tan solo unos cortos pasosa los cuales le llaman `traverse` "el último empuje"...

### 🟣 `Cima del K2` = `Certifcación como Ingeniero CWAP-404`

Al superar los todos los obstáculos, solo hay que dar unos pasos más hacia la cima y disfrutar la de vista de los Himalaya, para después seguir con el siguiente reto...

La `ruta Abruzzi del K2` es un camino lleno de peligros y desafíos que ponen a prueba la resistencia física y mental de los alpinistas. Desde el `base camp` hasta la `cima del K2`, la ruta está plagada de peligros mortales. A pesar de esto, aquellos que logran completar la ruta pueden considerarse verdaderos héroes, capaces de enfrentar lo inimaginable y triunfar sobre él. <br> 

**La hazaña de superar la ruta completa del K2 es una demostración de la fuerza y la determinación humana y un recordatorio de que, con suficiente dedicación y perseverancia, no hay nada que el ser humano no pueda superar.** <br> 

 _"K2, avanzar a morir!"_

## 🟢 Conocimiento Requerido para `CWAP-402`

- El examen está dividido de la siguiente manera:

<div align="center">
  
|     **Conocimiento CWAP**     	| **Porcentaje** 	|                                                                                                                                                                                                                             **Descripción**                                                                                                                                                                                                                             	|
|:-----------------------------:	|:--------------:	|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
| **Protocol Analysis**         	|     **15%**    	| Se centra en el análisis y comprensión de los protocolos utilizados en redes inalámbricas, incluyendo el análisis de tramas y paquetes, y la comprensión de los diferentes campos de los encabezados de los protocolos.                                                                                                                                                                                                                                                 	|
| **Spectrum Analysis**         	|     **10%**    	| Cubre la comprensión de los conceptos básicos de la espectroscopia y el uso de herramientas y equipos para analizar y solucionar problemas relacionados con el espectro en redes inalámbricas.                                                                                                                                                                                                                                                                          	|
| **PHY Layers & Technologies** 	|     **10%**    	| Se enfoca en los diferentes tipos de tecnologías y técnicas utilizadas en las capas físicas (PHY) de redes inalámbricas, incluyendo las diferentes modulaciones, técnicas de codificación y características de antena.                                                                                                                                                                                                                                                  	|
| **MAC Sublayers & Functions** 	|     **25%**    	| Cubre las diferentes subcapas y funciones de la capa de control de acceso al medio (MAC) en redes inalámbricas, incluyendo la comprensión de los diferentes métodos de acceso al medio, la planificación de canal y la gestión de tráfico.                                                                                                                                                                                                                              	|
| **WLAN Medium Access**        	|     **10%**    	| Se centra en la comprensión de los diferentes mecanismos y técnicas utilizados para el acceso al medio en redes inalámbricas, incluyendo el protocolo de acceso múltiple por detección de portadora con evitación de colisiones (CSMA/CA).                                                                                                                                                                                                                              	|
| **802.11 Frame Exchanges**    	|     **30%**    	| Cubre la comprensión detallada de los diferentes tipos de tramas y paquetes utilizados en redes inalámbricas, como overhead y payload. También se enfoca en el proceso de autenticación, asociación y roaming . Se cubre en detalle el proceso de transmisión y recepción de tramas y paquetes en redes inalámbricas, incluyendo los diferentes modos de operación de AP y STA, y el uso de los diferentes tipos de frames para el control y la transferencia de datos. 	|
 
</div>

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

## El truco del `Modelo OSI` para `Wireless`

Antes que nada, quiero destacar que tanto para CWNA como CWAP no se utliza el `modelo TCP/IP`, sino que se basa en el `modelo OSI`, aunque no totalmente como lo conocemos... <br>

Al principio es algo confuso cuando mencionan los cursos de `CWNP` (u otros cursos y certificaciones) cuando dicen "no estamos usando el modelo OSI, solo hacemos referencia para que se comprenda el concepto" y a partir de eso se dan explicaciones de X o Y cosa... pero después de todo para eso es el modelo... simplemente es una referencia! <br> 

Por ejemplo, en hacking y cyber-seguridad ya he realizado writeups donde podemos hacer `packet tampering` e inyectarlos a la red sin importarnos para nada la estructura del `modelo OSI`. Básicamente puedo inyectar HEX random y los paquetes/frames se transmiten sin importar que estén completamente mal-formados sin respetar el modelo por capas. <br>

**El truco que he encontrado para comprender al 100% el proceso de transmisión que se llevará a cabo y será el pan de cada día de esta certificación consiste en "añadir un sublayer al modelo original".** Pero ¿A qué me refiero con esto?

---

### Modelo OSI "original"

- [OSI/IEC Reference Model - Second Edition 1994](https://standards.iso.org/ittf/PubliclyAvailableStandards/s020269_ISO_IEC_7498-1_1994(E).zip)

El `OSI model` original se basa en `7 layers`, para las alturas de este curso ya se debe tener muy bien comprendido para que sirve cada capa, a grandes rasgos es el siguiente:  

| **Layer** 	|     **Name**     	|   **Protocol Data Unit (PDU)**   	|                                                                       **Función**                                                                      	|
|:---------:	|:----------------:	|:--------------------------------:	|:------------------------------------------------------------------------------------------------------------------------------------------------------:	|
|   **7**   	|  **Application** 	|               Data               	| Interactúa con aplicaciones de software que implementan un componente de comunicación.                                                                 	|
|   **6**   	| **Presentation** 	|               Data               	| Traduce, encripta y/o comprime datos en un formato que pueda ser entendido por el sistema receptor.                                                    	|
|   **5**   	|    **Session**   	|               Data               	| Maneja sesiones de comunicación entre aplicaciones y establece, gestiona y termina conexiones.                                                         	|
|   **4**   	|   **Transport**  	| Segment (TCP) <br>Datagram (UDP) 	| Proporciona entrega confiable (TCP) o no confiable (UDP) de datos entre dispositivos de red y maneja el control de flujo y la verificación de errores. 	|
|   **3**   	|    **Network**   	|              Packet              	| Determina la mejor ruta para que los datos viajen desde el remitente al receptor y maneja la dirección lógica y el enrutamiento.                       	|
|   **2**   	|   **Data Link**  	|               Frame              	| Transfiere datos entre dispositivos de red y maneja la dirección física, la corrección de errores y el control de flujo.                               	|
|   **1**   	|   **Physical**   	|                Bit               	| Convierte los datos a un formato que se puede transmitir por la red física y maneja los medios, la señal y la transmisión de datos.                    	|

---

### Modelo OSI "Fz3r0 WiFi Custom"

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

![image](https://user-images.githubusercontent.com/94720207/227751705-c561fa0f-16ed-4785-9f53-f8dfe6ceecaa.png)

Ahora que ya se tiene el concepto visual de como se distribuyen las `sublayer 1 - PHY`, `sublayer 2 lower - MAC` y `sublayer 2 upper - LLC`, es así como se vería el modelo OSI completo (sin embargo, siempre utilizaré la tabla que presenté anteriormente para fines prácticos):

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/227752796-9110c821-c5c2-4424-b39e-7247fc0b0954.png" alt="Modelo OSI"/> </a> </p> 



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























## 🟢 `802.11 Aggregation` / `Frame Aggregation`

- [`802.11 Aggregation` - Friend or Foe? | Wes Purvis](https://www.youtube.com/watch?v=3jqYwFQSqnE)
- [`Aggregation in WiFi`](https://www.youtube.com/watch?v=RvLVDi41lKQ)
- [`Aggregation`](https://www.youtube.com/watch?v=kT5KS1-2ZQE)

Para que `802.11n` o `802.11ac` puedan obtener mayor `throughput` existen 4 maneras posibles:

1. **`Increase Modulation`** (Incrementar la modulación)
2. **`Wider Channel Bandwith`** (Incrementar el ancho de la banda. ej. 5 GHz)
3. **`MIMO - Multiple Input / Multiple Output`** (Antentas MIMO. ej. 2x2:2)
4. **`Frame Aggregation`** (Agregación de Tramas)

![image](https://user-images.githubusercontent.com/94720207/224576441-f3589df1-50b1-4c49-bd6d-10325994564b.png)

---

### 🟣 La analogía de la carretera, los coches y el camión

**¿Por qué "agregar"?** Es el mismo beneficio que brinda esa típica foto del camión VS muchos coches en una autopista, donde al mismo tiempo ambas solcuiones tienen la misma capacidad para transportar exactamente a la misma cantidad de gente... <br>

Sin embargo, **al hacerlo en coches la autopista se satura lo que casua problemas como más tráfico, lentitud y más consumo de rescursos. En cambio, `"agregar" a todas esas personas en un solo camión, hace que el tráfico y la velocidad sean más eficientes`** <br> 

- Los coches representan el `overhead` (`headers`, `footers`, `QoS`, `management`, `control`, etc, etc...) ya que es tráfico de diferentes personas que no se conocen y viajan en diferentes coches (la clásica segmentación en frames que contienen un payload, es decir, como tradicionalmente es la transferencia de datos en una red). 
- **Pero... si estas personas se pusieran de acuerdo, podrían viajar todos de manera más `eficiente` en el mismo camión, siempre y cuando todos vengan del mismo `origen` y vayan al mismo `destino`.** 

![image](https://user-images.githubusercontent.com/94720207/224576564-19103768-81c5-4a1d-8b85-551d97eaf703.png)

**Esto es lo que realmente hace el `Frame Aggregation`, reduce de gran manera el `overhead` y hace que el `WiFi` sea mucho más eficiente.**

---

### 🟣 Tipos de `Frame Aggregation`

A continuación se explican a detalle los `3` tipos de `Aggregation`:

1. `A-MPDU Aggregation`
2. `A-MSDU Aggregation`
3. `A-MPDU and A-MSDU Aggregation`

---

### ⭕ `No aggregation`

- Este es un frame normal, sin `aggegation`.
- Tiene un `un PHY header`, `un MAC header`, `un MSDU`,... y **existe un ``ACK` (Acknowledgement) para cada uno de esos frames.**
- Este funciona generalmente para estándares legacy como `802.11a`, es bueno, pero no tan eficiente. 

![image](https://user-images.githubusercontent.com/94720207/224578454-86728faa-a9ee-4b1b-8a2e-27c6f82e7610.png)

#### 💥 `Escenario de Falla` : `No aggregation`

- En caso de error **`solo se retransmite 1 frame`**
- Cada frame contiene dentro un `MSDU`
- Cada frame contiene sus respectivos headers como `MAC`, `PHY` y `ACK`

![image](https://user-images.githubusercontent.com/94720207/225209145-b5b3654d-5422-47fa-bd02-331c57f3ebd8.png)

---

### ⭕ `A-MPDU Aggregation`

- Este tipo de `aggregation` es **el más `común`.**
- Proporciona una enorme cantidad de incremento en el `throughput`.
- Básicamente lo que hace es enviar una serie de `MPDU's` que se delimitan con cada `MAC header`.
- Así que, lo que hace es evitar las retranmisiones de `PHY headers` y cada `ACK` de intermedio. 
- Es decir: Solo hay 1 `ACK`, que se llama `Block ACK` para responder a, por ejemplo, 64 frames juntos que generan un `block` (bloque) de frames.

![image](https://user-images.githubusercontent.com/94720207/225181794-df541475-46ed-42ef-8a6d-ff5786bebc6d.png)

#### 💥 `Escenario de Falla` : `A-MPDU`

- En caso de error **`solo se retransmite 1 frame... (1 subframe MPDU con su propia MAC y PHY header)`**
- De hecho una gran ventaja, es que ese `1 subrame MPDU` puede viajar en el siguiente `A-MPDU` en alguno de los "espacios del camión". 

![image](https://user-images.githubusercontent.com/94720207/225212751-1052128c-8168-46a6-8349-afc217404377.png)

**`A-MPDU Aggregation` agrupa múltiples `MPDUs` en un solo paquete.** En el proceso de A-MPDU Aggregation, varios paquetes de datos que se dirigen al mismo destinatario se agrupan en un solo paquete, lo que se conoce como una "unidad de datos de protocolo de agregación" `A-MPDU`. Este paquete más grande se divide en varias subunidades de datos `MPDUs`, cada una de las cuales se transmite en una trama de radio separada. <br>

En la recepción, el destinatario reensambla los paquetes originales a partir de las subunidades de datos recibidas. Este proceso de agrupación y desagrupación de paquetes es manejado por la capa MAC del sistema de comunicaciones inalámbricas.

---

### ⭕ `A-MSDU Aggregation`

- Este tipo de `aggregation` es **el más `eficiente`.**
- Tiene los mayores pros... Pero, también es el que tiene los mayores contras.
- Son basicamente frames largos en el aire, por ejemplo, pueden contener muchos `MSDU de 500 bytes`, combinados y con overheads adicionales podría repretentar `6000 bytes en el aire`
- `6000 bytes` en el aire, ¡claro, está perfecto! 😀... cuando funciona 😑... ¡¿Imagina retransmitir 6000 bytes siempre que exista un error 😧?! Hay que recordar que las retransmisiones en WiFi son comunes a cierta escala.

![image](https://user-images.githubusercontent.com/94720207/225184155-30cf5564-2664-453f-8128-9dc2612d3118.png)

#### 💥 `Escenario de Falla` : `A-MSDU`

- En caso de error **`se retransmite 1 frame largo... (el frame es igual a tooodo el A-MSDU) `**
- Por ejemplo, si la suma de todos los `MSDU` que van dentro del `A-MSDU` son `6000 bytes`, entonces se retransmiten TODOS los `6000 bytes`
- En caso de errores, retransmisiones tan largas podrían generar falta de eficiencia en la red y problemas derivados. 

![image](https://user-images.githubusercontent.com/94720207/225452761-80551fbf-dd51-45d6-b21e-2f68f3b20a81.png)

A diferencia de A-MPDU Aggregation, que agrupa múltiples MPDUs en un solo paquete... A-MSDU Aggregation **combina múltiples MSDUs (unidades de servicio de datos de capa superior) en un solo paquete más grande**, lo que mejora aún más la eficiencia de la transmisión inalámbrica. <br>

En el proceso de A-MSDU Aggregation, varios paquetes de nivel superior, que pueden ser fragmentados en múltiples MPDUs, se agrupan en un solo paquete A-MSDU. Este paquete más grande se divide en varias subunidades de datos (MPDUs), cada una de las cuales se transmite en una trama de radio separada. <br>

En general, la elección de utilizar A-MPDU Aggregation o A-MSDU Aggregation dependerá de las características específicas de la aplicación y de los requisitos de transmisión de datos. Por ejemplo, en aplicaciones con cargas de datos más pesadas, A-MSDU Aggregation puede ser más eficiente, mientras que en aplicaciones con cargas de datos más ligeras, A-MPDU Aggregation puede ser más adecuado.

---

### ⭕ `A-MPDU of an A-MSDU Aggregation`

- Este tipo de `aggregation` **combina lo mejor de `ambos anteriores`.**
- Continúan siendo frames largos en el aire, pero en caso de existir un error no se generaría una retransmisión tan larga debido a los `MPDU delimiter` que genera dividir los `MSDUs` en `MPDUs`.

![image](https://user-images.githubusercontent.com/94720207/225208271-123232c2-11fb-4c6f-b4d4-f14d7086524a.png)

#### 💥 `Escenario de Falla` : `A-MPDU and A-MSDU Aggregation`

- En caso de error **`se retransmite 1 frame mediano... (el frame es igual al MPDU que se debe retransmitir) `**
- En este ejemplo, sólo se retransmitiría la mitad de todo el `A-MPDU + A-MSDU`, esto debido al delimitados del `MPDU`
- Esto lo hace más eficiente que el `A-MSDU`, pero sin tanto problema por las grandes retransmisiones. 

![image](https://user-images.githubusercontent.com/94720207/225468575-45fcf166-3ea8-40ea-9fac-c1ac537c3213.png)

En esta técnica, se agrupan múltiples MSDUs en un solo paquete A-MSDU y, a su vez, se agrupan múltiples paquetes A-MSDU en un solo paquete A-MPDU. Este paquete A-MPDU más grande se divide en varias subunidades de datos (MPDUs), cada una de las cuales se transmite en una trama de radio separada. <br>

La combinación de A-MPDU y A-MSDU Aggregation tiene como objetivo mejorar aún más la eficiencia de la transmisión inalámbrica al aprovechar los beneficios de ambas técnicas de agregación de paquetes. Al agrupar múltiples MSDUs en un paquete A-MSDU, se reduce la sobrecarga de la capa MAC y se disminuye la cantidad de tiempo de transmisión necesario para transmitir un conjunto de paquetes. Luego, al agrupar varios paquetes A-MSDU en un paquete A-MPDU, se reduce aún más la sobrecarga de la capa MAC y se mejora la eficiencia de la transmisión inalámbrica.

---

### 🟣 `Tráfico TCP` vs `Throughput` | `A-MPDU` + `802.11ac @ 80MHz`

#### ⭕ `A-MPDU` : `Throughput`

- Este ejemplo se hace con el `A-MPDU`, la `agregación más común`, usando `802.11ac @ 80 MHz`
- Estos solo son unos cálculos muy optimistas para darnos una idea el Throughtput posible con esta combinación. 
- Las lineas azules representan las medidas promedio y usuales
- Cada linea de colores respresenta un `spatial stream` diferente `1x1`, `2x2`, `3x3`

![image](https://user-images.githubusercontent.com/94720207/225475120-173be773-0ffe-4562-9795-aba74f64eeb0.png)

#### ⭕ `A-MSDU` : `Throughput`

- Este ejemplo se hace con el `A-MPDU`, la `agregación más eficiente, pero con contras de largas retransmisiones`, usando `802.11ac @ 80 MHz`
- Estos solo son unos cálculos muy optimistas para darnos una idea el Throughtput posible con esta combinación. 
- Las lineas azules representan las medidas promedio y usuales
- Cada linea de colores respresenta un `spatial stream` diferente `1x1`, `2x2`, `3x3`

![image](https://user-images.githubusercontent.com/94720207/225476948-fb7606ae-734c-4ed1-be85-8fc396e621ea.png)

**Sin duda con A-MSDU se consigue un mucho mejor Throughput, el problema son esas largas retransmisiones... Es por eso que para utilizarlo lo mejor es combinar ambos tipos de `Aggregation` para lograr el tercero (fusión de ambos) = `A-MPDU of an A-MSDU Aggregation`.** <br>

**Ahora sabemos que: `Existe un gran beneficio de hacer "A-MPDU Aggregation", además, existé un significativamente gran beneficio de utilizar "A-MPDU of an A-MSDU Aggregation"`** <br>

---

### 🦈 Estructura de `A-MSDU in a A-MPDU` @ `Wireshark`

- Se puede saber que es un `A-MPDU` cuando se ven un grupo de `data frames` apilados uno encima del otro.
- Comienza con un `RTS`(Ready-To-Send) para avisar que enviará `frames` al aire.
- Al final se podrá encontrar el `Block ACK`.
- El `RSSI` solo se puede encontrar en el `último frame`
- En este ejemplo, debido al `lenght` de `3104` se puede saber que se trata de `2 A-MSDU` dentro de `1 A-MPDU`

![image](https://user-images.githubusercontent.com/94720207/225499979-157c6084-9440-4595-b8ea-0131634b2b28.png)

- En el ejemplo anterior se utilizaron `2 A-MSDU` dentro de `1 A-MPDU` (como la mayoría de vendors utilizan)
- Pero ¿Qué pasaría si metiéramos `8 A-MSDU` dentro de `1 A-MDPU`?
- Tendríamos `1 A-MDPU`, es decir `1 frame`, totalmente impráctico y gigantesco... pero divertido para experimentar!!! 🧪

![image](https://user-images.githubusercontent.com/94720207/225503072-d0624a4b-a1fe-477a-90d2-9c0d03183aaa.png)




















































<br>
<br>

## 🟢 `802.11 Standard Protocol`

- **El estándar de protocolo IEEE 802.11 define a la `MAC` y la `PHY` para comunicaciones en una `LAN` utilizando `RF` como `medio de transmisión` (osea una `WLAN`).**
- Las enmiendas modernas de 802.11 incluyen soporte a redes `mesh` y otro métodos de comunicaciones `devide-to-device`
- Este estándar es utilizado por dispositivos como **computadoras, smartphones, y otros dispositivos para conectarse a `redes Wi-Fi.`**
- El estándar 802.11 especifica las `frecuencias de radio`, los` protocolos de acceso al medio`, los `mecanismos de autenticación` y `encriptación`, `y otros aspectos` necesarios para el funcionamiento de una red inalámbrica. 
- El estándar también define diferentes variantes, como `802.11a`, `802.11b`, `802.11g`, `802.11n`, `802.11ac`, `802.11ax`; cada una con **diferentes características y velocidades de transmisión de datos.**

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223910395-92a65b7d-d17f-4688-bf4c-1c220526f038.png" alt="encoding"/> </a> </p> 

---

### `IEEE 802.11` & `PHY Modulations`

En las redes WiFi, se utilizan diferentes tipos de modulación según la capacidad del canal de radio y el entorno de la red. Los estándares más antiguos como 802.11b utilizan modulaciones más básicas como ASK y PSK, mientras que los estándares más recientes como 802.11ac y 802.11ax utilizan modulaciones más complejas como QAM. La elección de la modulación adecuada es importante para optimizar la tasa de transferencia de datos y la calidad de la señal en una red inalámbrica.

- Durante el `CWNA` hice una tabla que me ayudó mucho a entender los `PHY`, `Ammandments`, `Standards`. Esta es la versión simplificada:

| IEEE Standard 	| PHY     	| PHY (Full Name)                            	| Year 	| Band(s)               	| Bandwidth                  	| Modulation(s)                                 	| Max. Data Rate 	| Max. Spatial Streams 	|
|---------------	|---------	|--------------------------------------------	|------	|-----------------------	|----------------------------	|-----------------------------------------------	|----------------	|----------------------	|
| 802.11-prime  	| DSSS    	| Direct Sequence Spread Spectrum            	| 1997 	| 2.4 GHz               	| 22 MHz                     	| ASK, PSK, QAM                                 	| 2 Mbps         	| 1                    	|
| 802.11b       	| HR/DSSS 	| High Rate/Direct Sequence Spread Spectrum  	| 1999 	| 2.4 GHz               	| 22 MHz                     	| DSSS                                          	| 11 Mbps        	| 1                    	|
| 802.11a       	| OFDM    	| Orthogonal Frequency Division Multiplexing 	| 1999 	| 5 GHz                 	| 20 MHz                     	| OFDM                                          	| 54 Mbps        	| 1                    	|
| 802.11g       	| ERP     	| Extended Rate PHY                          	| 2003 	| 2.4 GHz               	| 20 MHz                     	| OFDM, DSSS                                    	| 54 Mbps        	| 1                    	|
| 802.11n       	| HT      	| High Throughput PHY                        	| 2009 	| 2.4 GHz, 5 GHz        	| 20, 40, 80, 160 MHz        	| OFDM, MIMO-OFDM                               	| 600 Mbps       	| 4                    	|
| 802.11ac      	| VHT     	| Very High Throughput PHY                   	| 2013 	| 5 GHz                 	| 20, 40, 80, 160, 80+80 MHz 	| OFDM, MIMO-OFDM                               	| 6.9 Gbps       	| 8                    	|
| 802.11ax      	| HE      	| High Efficiency PHY                        	| 2019 	| 2.4 GHz, 5 GHz, 6 GHz 	| 20, 40, 80, 80+80, 160 MHz 	| OFDM, MIMO-OFDM, MU-MIMO, QAM, PSK, QPSK, FSK 	| 9.6 Gbps       	| 12                   	|



















|                IEEE                	|                        802.11-prime                       	|                         802.11b                        	|                             802.11a                             	|                       802.11g                       	|                                                 802.11n                                                	|                                            802.11ac                                           	|                                               802.11ax                                               	|
|:----------------------------------:	|:---------------------------------------------------------:	|:------------------------------------------------------:	|:---------------------------------------------------------------:	|:---------------------------------------------------:	|:------------------------------------------------------------------------------------------------------:	|:---------------------------------------------------------------------------------------------:	|:----------------------------------------------------------------------------------------------------:	|
| PHY                                	| DSSS                                                      	| HR/DSSS                                                	| OFDM                                                            	| ERP                                                 	| HT                                                                                                     	| VHT                                                                                           	| HE                                                                                                   	|
| PHY Name                           	| Direct Sequence Spread Spectrum                           	| High Rate/Direct Sequence Spread Spectrum              	| Orthogonal Frequency Division Multiplexing                      	| Extended Rate PHY                                   	| High Throughput PHY                                                                                    	| Very High Throughput PHY                                                                      	| High Efficiency PHY                                                                                  	|
| Year                               	| 1997                                                      	| 1999                                                   	| 1999                                                            	| 2003                                                	| 2009                                                                                                   	| 2013                                                                                          	| 2019                                                                                                 	|
| Band(s)                            	| 2.4 GHz                                                   	| 2.4 GHz                                                	| 5 GHz                                                           	| 2.4 GHz                                             	| 2.4 GHz, 5 GHz                                                                                         	| 5 GHz                                                                                         	| 2.4 GHz, 5 GHz, 6 GHz                                                                                	|
| Bandwidth                          	| 22 MHz                                                    	| 22 MHz                                                 	| 20 MHz                                                          	| 20 MHz                                              	| 20, 40, 80, 160 MHz                                                                                    	| 20, 40, 80, 160, 80+80 MHz                                                                    	| 20, 40, 80, 80+80, 160 MHz                                                                           	|
| Modulation(s)                      	| ASK, PSK, QAM                                             	| DSSS                                                   	| OFDM                                                            	| OFDM, DSSS                                          	| OFDM, MIMO-OFDM, MU-MIMO, QAM, PSK, QPSK, FSK                                                          	| OFDM, MIMO-OFDM, MU-MIMO, QAM, PSK, QPSK, FSK                                                 	| OFDM, MIMO-OFDM, MU-MIMO, QAM, PSK, QPSK, FSK                                                        	|
| Max Rate                           	| 2 Mbps                                                    	| 11 Mbps                                                	| 54 Mbps                                                         	| 54 Mbps                                             	| 600 Mbps (4x4)                                                                                         	| 6.9 Gbps (8x8)                                                                                	| 9.6 Gbps (8x8)                                                                                       	|
| Spatial Streams                    	| 1                                                         	| 1                                                      	| 1, 2, 4                                                         	| 1, 2                                                	| 1, 2, 3, 4                                                                                             	| 1, 2, 3, 4, 8                                                                                 	| 1, 2, 4, 8, 12, 16                                                                                   	|
| Recommended SNR for Max. Data Rate 	| 25 dB                                                     	| 25 dB                                                  	| 25 dB                                                           	| 25 dB                                               	| 25 dB                                                                                                  	| 25 dB                                                                                         	| 25 dB                                                                                                	|
| Max. Coding Rate                   	| N/A (No MIMO)                                             	| N/A (No MIMO)                                          	| 64-QAM \| 3/4 or 256-QAM \| 5/6                                 	| 64-QAM \| 3/4 or 256-QAM \| 5/6                     	| 64-QAM \| 5/6 or 256-QAM \| 5/6 for 1 or 2 spatial streams, 1024-QAM \| 5/6 for 3 to 8 spatial streams 	| 1024-QAM \| 5/6 for 1 or 2 spatial streams, 4096-QAM \| 3/4 or 5/6 for 3 to 8 spatial streams 	| 1024-QAM \| 5/6 or 3/4 for 1 to 8 spatial streams                                                    	|
| MIMO                               	| N/A                                                       	| N/A                                                    	| N/A                                                             	| N/A                                                 	| 2x2, 3x3, 4x4                                                                                          	| 2x2, 4x4, 8x8                                                                                 	| 2x2, 4x4, 8x8, 16x16                                                                                 	|
| Aggreg                             	| -                                                         	| -                                                      	| -                                                               	| -                                                   	| A-MSDU, A-MPDU                                                                                         	| A-MSDU, A-MPDU                                                                                	| A-MSDU, A-MPDU                                                                                       	|
| Security                           	| WEP, WPA                                                  	| WEP, WPA                                               	| WEP, WPA, WPA2                                                  	| WEP, WPA, WPA2                                      	| WEP, WPA, WPA2, WPA3                                                                                   	| WEP, WPA, WPA2, WPA3                                                                          	| WEP, WPA, WPA2, WPA3, WPA3-Personal, WPA3-Enterprise, Enhanced Open, OWE, Dragonfly, WPA3-Transition 	|
| Auth.                              	| Open, Shared                                              	| Open, Shared                                           	| 802.1X/EAP                                                      	| Open, Shared, 802.1X/EAP                            	| 802.1X/EAP, PSK                                                                                        	| 802.1X/EAP, PSK, SAE                                                                          	| 802.1X/EAP, PSK, SAE, DPP                                                                            	|
| Enc.                               	| RC4, TKIP, AES-CCMP                                       	| RC4, TKIP, AES-CCMP                                    	| AES-CCMP                                                        	| AES-CCMP, TKIP                                      	| AES-CCMP, TKIP, WEP-40/104, GCMP-128                                                                   	| AES-CCMP, GCMP-128                                                                            	| AES-CCMP, GCMP-128, TKIP, BIP                                                                        	|
| Enhance.                           	| -                                                         	| -                                                      	| -                                                               	| -                                                   	| LDPC, STBC, MLD, TxBF, RIFS, HT-Delayed Block Ack                                                      	|                                                                                               	|                                                                                                      	|
| Extra Info & Features of the PHY   	| Legacy PHY with low data rates but immune to interference 	| High data rates using DSSS with backward compatibility 	| Higher data rates with more robustness and reduced interference 	| Introduced shorter slot times and frame aggregation 	| Introduced MIMO technology for increased throughput and range                                          	| Introduced MU-MIMO, beamforming, and wider channels for higher throughput                     	| Introduced Uplink and Downlink OFDMA, Target Wake Time, and spatial reuse for better efficiency      	|
| Guard Interval                     	| N/A                                                       	| N/A                                                    	| 800 ns                                                          	| 800 ns                                              	| 800 ns / 400 ns                                                                                        	| 800 ns / 400 ns / 160 ns                                                                      	| 800 ns / 400 ns / 200 ns / 100 ns / 50 ns / 25 ns                                                    	|




| **IEEE 802.11** 	| **Year** 	| **Technology**                                                   	| **Descirpción**                                                                                                                                                                                                                                                                                                                                                                                                                 	|
|-----------------	|----------	|------------------------------------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| **802.11**      	| 1997     	| Original WLAN standard                                           	| El primer estándar de la familia 802.11, desarrollado en 1997.                                                                                                                                                                                                                                                                                                                                                                  	|
| **802.11b**     	| 1999     	| 2.4 GHz, up to 11 Mbps                                           	| Estándar publicado en 1999 que define una tasa de transmisión máxima de 11 Mbps utilizando la banda de frecuencia de 2.4 GHz. Es compatible con el estándar 802.11 original y utiliza la modulación por secuencia directa por espectro expandido (DSSS).                                                                                                                                                                        	|
| **802.11a**     	| 1999     	| 5 GHz, up to 54 Mbps                                             	| Estándar publicado en 1999 que define una tasa de transmisión máxima de 54 Mbps utilizando la banda de frecuencia de 5 GHz. A diferencia de 802.11b, utiliza la modulación por ortogonalización de frecuencia (OFDM) para transmitir datos. Debido a que la banda de frecuencia de 5 GHz es menos congestionada que la de 2.4 GHz, 802.11a ofrece una mayor calidad de señal y menos interferencia.                             	|
| **802.11d**     	| 2001     	| Global harmonization                                             	| Publicado en 2001, este estándar permitió que los dispositivos inalámbricos funcionen en diferentes regiones geográficas mediante la incorporación de la identificación del país en la información de señalización del dispositivo. Esto aseguró que los dispositivos cumplan con las regulaciones de emisiones de radio en su área de operación.                                                                               	|
| **802.11g**     	| 2003     	| 2.4 GHz, up to 54 Mbps                                           	| Publicado en 2003, este estándar mejora la velocidad de transmisión de datos de 802.11b a 54 Mbps utilizando la banda de frecuencia de 2.4 GHz. También es compatible con 802.11b.                                                                                                                                                                                                                                              	|
| **802.11h**     	| 2003     	| Spectrum management                                              	| Publicado en 2003, este estándar mejora la interoperabilidad con otros dispositivos que operan en la banda de frecuencia de 5 GHz, como los sistemas de radar. Utiliza técnicas de espectro ensanchado y selección de frecuencia dinámica para cumplir con las regulaciones de emisiones de radio en Europa.                                                                                                                    	|
| **802.11i**     	| 2004     	| Security enhancements                                            	| Publicado en 2004, este estándar define mejoras en la seguridad de la red inalámbrica, como el cifrado AES-CCMP para reemplazar el cifrado WEP obsoleto. También especifica la autenticación y administración de claves, así como la privacidad de la información de identificación personal.                                                                                                                                   	|
| **802.11j**     	| 2004     	| Japan regulatory modifications                                   	| Publicado en 2004, este estándar habilita dispositivos inalámbricos para su uso en Japón utilizando la banda de frecuencia de 4.9 GHz. También incluye especificaciones para cumplir con las regulaciones de emisiones de radio en Japón.                                                                                                                                                                                       	|
| **802.11e**     	| 2005     	| Quality of service (QoS) enhancements                            	| Estándar de mejora de calidad de servicio (QoS) que permite la asignación de prioridades a diferentes flujos de datos para proporcionar servicios de voz, vídeo y datos más confiables y de mayor calidad en redes inalámbricas.                                                                                                                                                                                                	|
| **802.11k**     	| 2008     	| Radio resource management, roaming                               	| Estándar para medición de recursos que proporciona información de diagnóstico y estadísticas para optimizar el rendimiento de la red y facilitar la itinerancia de dispositivos entre diferentes puntos de acceso (AP). Permite que los dispositivos inalámbricos midan la calidad de la señal de la red, determinen la intensidad de la señal y seleccionen el AP adecuado para conectarse.                                    	|
| **802.11r**     	| 2008     	| Fast roaming                                                     	| Estándar de itinerancia rápida que permite a los dispositivos inalámbricos moverse de un punto de acceso (AP) a otro de manera más rápida y fluida, lo que permite conexiones más estables y sin interrupciones en aplicaciones en tiempo real.                                                                                                                                                                                 	|
| **802.11y**     	| 2008     	| U.S. public safety                                               	| Estándar de WLAN para operaciones en bandas de frecuencia no licenciadas en las regiones de América del Norte y del Sur, y que establece una serie de requisitos obligatorios y opcionales para dispositivos que operan en la banda de 3650-3700 MHz.                                                                                                                                                                           	|
| **802.11n**     	| 2009     	| MIMO, up to 600 Mbps                                             	| Estándar de WLAN de alta velocidad y rango extendido que utiliza múltiples antenas para mejorar el rendimiento y la cobertura. Proporciona velocidades de transmisión de hasta 600 Mbps y utiliza tecnologías de modulación avanzadas para aumentar la eficiencia espectral. Es compatible con versiones anteriores de dispositivos WLAN que operan en las bandas de 2,4 GHz y 5 GHz.                                           	|
| **802.11w**     	| 2009     	| Protected management frames                                      	| Estándar de seguridad que proporciona protección adicional contra ataques de denegación de servicio (DoS) y de inyección de paquetes en redes WLAN. Utiliza un cifrado AES más seguro para proteger los datos y proporciona autenticación de clave previamente compartida (PSK) mejorada para proteger las contraseñas de acceso a la red.                                                                                      	|
| **802.11p**     	| 2010     	| Wireless access for vehicular environment                        	| Estándar de WLAN para redes vehiculares (VANET) que permite la comunicación inalámbrica entre vehículos y dispositivos de infraestructura de carreteras para mejorar la seguridad y la eficiencia del transporte. Proporciona canales de comunicación dedicados y una calidad de servicio (QoS) mejorada para aplicaciones de seguridad críticas, como el control de crucero adaptativo y la advertencia de colisión inminente. 	|
| **802.11z**     	| 2010     	| Extensions to direct link setup (DLS)                            	| Establece un mecanismo para la transferencia de información de la red a dispositivos móviles a través de señales acústicas, conocido como "Wi-Fi Aware".                                                                                                                                                                                                                                                                        	|
| **802.11v**     	| 2011     	| Network management                                               	| Ofrece una optimización del rendimiento y la capacidad de gestión de la red, mediante la mejora de la calidad de servicio (QoS) y la gestión de energía.                                                                                                                                                                                                                                                                        	|
| **802.11u**     	| 2011     	| Interworking with external networks                              	| Define los servicios de red y la interfaz de programación de aplicaciones (API) para la interconexión de redes inalámbricas con redes de área amplia (WWAN).                                                                                                                                                                                                                                                                    	|
| **802.11s**     	| 2011     	| Wireless mesh networking                                         	| Establece una red de malla inalámbrica, que permite una comunicación inalámbrica descentralizada entre nodos, sin la necesidad de un punto de acceso central.                                                                                                                                                                                                                                                                   	|
| **802.11ae**    	| 2012     	| MAC security enhancements                                        	| Define un mecanismo de seguridad de capa de enlace de datos, denominado "MACsec", que protege las comunicaciones de la red inalámbrica contra ataques de seguridad.                                                                                                                                                                                                                                                             	|
| **802.11aa**    	| 2012     	| Robust audio/video streaming                                     	| Proporciona un mecanismo de recuperación de errores en la transmisión de paquetes de datos, mediante la retransmisión selectiva de paquetes perdidos.                                                                                                                                                                                                                                                                           	|
| **802.11ad**    	| 2012     	| 60 GHz, up to 7 Gbps                                             	| También conocido como "WiGig", utiliza frecuencias de onda milimétricas para ofrecer altas velocidades de transferencia de datos a corta distancia.                                                                                                                                                                                                                                                                             	|
| **802.11ac**    	| 2013     	| 5 GHz, up to 6.9 Gbps                                            	| Introduce mejoras significativas en la velocidad y capacidad de las redes inalámbricas, mediante el uso de tecnología "multi-user MIMO" y canales más amplios.                                                                                                                                                                                                                                                                  	|
| **802.11af**    	| 2013     	| TV white space spectrum                                          	| Operación en bandas de TV blancas (TVWS) para proveer conectividad de red inalámbrica. Permite el uso de frecuencias no utilizadas por señales de televisión. Se usa para extender la cobertura de la red Wi-Fi y brindar acceso a Internet en áreas remotas.                                                                                                                                                                   	|
| **802.11ah**    	| 2016     	| Sub-1 GHz, up to 1000 nodes                                      	| Operación en bandas de frecuencia sub-1GHz para redes de área amplia y baja velocidad de datos. Diseñado para brindar conectividad a dispositivos IoT que requieren baja energía, bajo costo y larga duración de batería.                                                                                                                                                                                                       	|
| **802.11ai**    	| 2016     	| WLAN direct link setup                                           	| Mejoras en la calidad de servicio (QoS) y capacidad de manejo de congestión de red. Introduce mecanismos de programación de tiempo de activación y duración del sueño para dispositivos de baja energía. Admite la operación en redes de alta densidad de dispositivos, como estaciones de carga de baterías eléctricas o salas de conferencias.                                                                                	|
| **802.11aj**    	| 2018     	| China millimeter wave, up to 4.6 Gbps                            	| Operación en bandas de frecuencia de ondas milimétricas (mmWave) de 45 GHz a 60 GHz para redes de alta velocidad de datos.                                                                                                                                                                                                                                                                                                      	|
| **802.11ak**    	| 2018     	| Extended service set IDs (ESSIDs)                                	| Mejoras en la capacidad de manejo de congestión y en la calidad de servicio (QoS) en redes de alta densidad de dispositivos.                                                                                                                                                                                                                                                                                                    	|
| **802.11aq**    	| 2018     	| Pre-association discovery                                        	| Mejoras en la calidad de servicio (QoS) y seguridad en redes Wi-Fi.                                                                                                                                                                                                                                                                                                                                                             	|
| **802.11ax**    	| 2019     	| High efficiency WLAN (HEW), up to 10 Gbps                        	| Mejoras significativas en la capacidad de manejo de congestión y en la eficiencia espectral de la red Wi-Fi. Introduce múltiples mejoras, incluyendo modulación más avanzada, división de canales espaciales, programación de tiempo de activación y duración del sueño, y técnicas avanzadas de beamforming.                                                                                                                   	|
| **802.11ay**    	| 2020     	| High Throughput, Next Generation                                 	| Operación en bandas de frecuencia de ondas milimétricas (mmWave) de 60 GHz para redes de alta velocidad de datos a largas distancias. Diseñado para brindar conectividad inalámbrica a alta velocidad en entornos de corto alcance y alta densidad de dispositivos, como aeropuertos, estadios y centros comerciales.                                                                                                           	|
| **802.11ba**    	| 2021     	| Wake-Up Radio, Next Generation                                   	| Especifica requisitos para la integración de dispositivos de automatización del hogar y sistemas de construcción inteligente con redes inalámbricas IEEE 802.11.                                                                                                                                                                                                                                                                	|
| **802.11at**    	| 2018     	| PoE Plus                                                         	| Estándar de mejora de la eficiencia energética que proporciona una forma de suministrar energía a dispositivos que requieren más de los 802.3at actuales.                                                                                                                                                                                                                                                                       	|
| **802.11az**    	| 2018     	| Fast Initial Link Setup, Location                                	| Protocolo de medición de la distancia inalámbrica que permite a los dispositivos calcular su ubicación relativa y ajustar su comportamiento en consecuencia.                                                                                                                                                                                                                                                                    	|
| **802.11bb**    	| 2020     	| Low Energy Critical Infrastructure Monitoring                    	| Especifica los requisitos de calidad de servicio (QoS) para los sistemas de comunicaciones inalámbricas de alta velocidad utilizados en aplicaciones de realidad virtual, aumentada y mixta.                                                                                                                                                                                                                                    	|
| **802.11bc**    	| 2020     	| Transmission of Broadcast, Unknown Unicast, and Multicast Frames 	| Especifica una nueva PHY para IEEE 802.11, denominada WLAN HE MAC PHY, que admite tasas de datos de hasta 6,1 Gbps y utiliza una modulación de amplitud en cuadratura de 4096-QAM.                                                                                                                                                                                                                                              	|
| **802.11bd**    	| 2020     	| mmWave, Next Generation                                          	| Estándar para la comunicación de alta velocidad de vehículos (IEEE 802.11p) que utiliza bandas de frecuencia de 60 GHz y admite tasas de datos de hasta 20 Gbps.                                                                                                                                                                                                                                                                	|
| **802.11be**    	| 2021     	| Enhancements for High Efficiency WLAN                            	| Especifica una nueva PHY para IEEE 802.11, denominada WLAN HE PHY, que admite tasas de datos de hasta 11 Gbps y utiliza una modulación de amplitud en cuadratura de 1024-QAM.                                                                                                                                                                                                                                                   	|
| **802.11bf**    	| 2022     	| Multi-Access Point Coordination                                  	| Especifica requisitos para el soporte de un enfoque basado en el tiempo para la transmisión de datos en redes inalámbricas IEEE 802.11.                                                                                                                                                                                                                                                                                         	|
| **802.11bh**    	| 2021     	| Spectrum and Signal Intelligence                                 	| Especifica requisitos para la operación de dispositivos en entornos no autorizados, como el espectro de televisión en blanco, para permitir la comunicación de red en caso de emergencia.                                                                                                                                                                                                                                       	|
| **802.11bi**    	| 2016     	| FILS Discovery                                                   	| Es una enmienda al estándar 802.11 que proporciona características de "alta eficiencia" para redes inalámbricas. Esta enmienda es importante para aplicaciones que requieren un bajo consumo de energía, como el IoT (Internet de las cosas).                                                                                                                                                                                   	|
| **802.11bt**    	| 2022     	| WLAN Technical Enhancements for Positioning                      	| También conocido como Wi-Fi 6E, es una enmienda al estándar 802.11ax que aprovecha las frecuencias de 6 GHz para aumentar la capacidad y la velocidad de las redes inalámbricas. Proporciona un rendimiento de alta velocidad y baja latencia para una variedad de dispositivos.                                                                                                                                                	|
| **802.11bu**    	| 2021     	| Light Communications                                             	| Es una enmienda al estándar 802.11 que proporciona una solución de baja potencia para el IoT (Internet de las cosas) y las aplicaciones de automatización del hogar. Se enfoca en reducir el consumo de energía en los dispositivos inalámbricos, lo que prolonga la duración de la batería y reduce los costos de energía.                                                                                                     	|
| **802.11bv**    	| 2020     	| WLAN Enhanced Location Services                                  	| Es una enmienda al estándar 802.11 que define el protocolo de enrutamiento de la red inalámbrica. Proporciona un método eficiente para enrutar los paquetes de datos a través de la red inalámbrica para garantizar una entrega rápida y confiable.                                                                                                                                                                             	|
| **802.11bw**    	| 2022     	| WLAN Operation in License-Exempt Bands above 6 GHz               	| Es una enmienda al estándar 802.11 que permite la comunicación inalámbrica de baja potencia y baja velocidad en entornos industriales. Se utiliza principalmente para la comunicación entre sensores y actuadores en aplicaciones de automatización industrial.                                                                                                                                                                 	|
| **802.11bx**    	| 2024     	| WLAN Enhancements for IoT                                        	| También conocido como Wi-Fi 6, es una enmienda al estándar 802.11 que mejora la eficiencia y la velocidad de las redes inalámbricas. Proporciona una mejor capacidad de gestión de tráfico, mejorando la experiencia del usuario en entornos de alta densidad de dispositivos.                                                                                                                                                  	|
| **802.11bz**    	| 2021     	| 2.4 GHz Operations                                               	| También conocido como NBASE-T Alliance, es una enmienda al estándar 802.11 que proporciona una solución de alta velocidad para la conexión inalámbrica a la red cableada. Utiliza la tecnología Ethernet para proporcionar velocidades de hasta 2.5 y 5 Gbps a través de cables de cobre.                                                                                                                                       	|
| **802.11ca**    	| 2022     	| High Efficiency WLAN and WLAN Sensing                            	| Es una enmienda al estándar 802.11 que se centra en mejorar la calidad de servicio (QoS) en las redes inalámbricas. Proporciona una mejor gestión del tráfico de la red, priorizando los datos críticos para garantizar una entrega confiable y oportuna.                                                                                                                                                                       	|




- Los `Data Rates` varían mucho depende de la `PHY` que esté siendo usada. 
- Los primeros `dispositivos WiFi` soportaban un máximo de 1 o 2 Mbps... Pero actualmente pueden llegar a data rates de casi 10 Gbps
- Sin embargo, en un mundo real `casi ningún dispositivo sería capaz de llegar a ese data rate` por razones como:
1. El medio (aire) se comparte con otros dispositivos WiFi en el mismo canal.
2. Los `Management Frames` de 802.11 crean `overhead` lo cual también consume `airtime`.

- Los `802.11 PHY` utilizan un `PHY header` (también conocidos como `campos de PPDU`) que son `prepended` al `payload` que proviene del `MAC Layer`
- El `PHY header` contiene la información necesaria para que el `receptor` ajuste su `data rate` dependiendo sus posibilidades para así poder sincronizarse con el `transmisor`


---

### 🟣 Utilizando `radiofrecuencias` para comunicar `datos` - `Physical Layer`

**Comunmente se les llama simplemente `PHY` a las `enmiendas IEEE 802.11` que funcionan en la `physical layer 1`, y que utilizan `métodos de modulación de radiofrecuencias (b/a/g/n/ac/ax)` para lograr la `interoperabilidad` de redes wireless y así poder enviar datos a través del `wireless medium`.** <br>

Las radiofrecuencias o `RF` se utilizan en la `Physical Layer 1` de la comunicación `WiFi 802.11` para transmitir datos a través del aire. Las `RF waves` se utilizan como portadoras de datos o `data carriers`, lo que significa que **los datos se `modulan` en una `señal de RF` y se `transmiten` a través del aire.** 

- Para realizar el `envío` de datos, los datos se `modulan`.
- En la `recepción`, los datos se extraen de la señal de RF modulada y se `decodifican` para su uso.

Las mayoría de redes Wi-Fi modernas pueden operar en frecuencias de `2.4 GHz` y `5 GHz`, pero las nuevas tecnologías de Wi-Fi, como `Wi-Fi 6E`, también soportan frecuencias más altas en la banda de `6 GHz`, además de que se presume pronto será el release de `WiFi7`. Esta banda se ha reservado específicamente para Wi-Fi, lo que significa que hay menos interferencia y una mayor capacidad para transmitir datos. <br> 

Además, **las frecuencias más altas permiten un mayor `bandwith & throughput`**, lo que se traduce en una mayor capacidad para transmitir datos a mayores velocidades. Cabe señalar que, aunque las frecuencias más altas proporcionan velocidades más rápidas, **también tienen una menor penetración y alcance de la señal y son más susceptibles a la atenuación por obstáculos como paredes, lo que puede afectar la calidad de la señal.**

- **Para que las `RF waves` (ondas de radiofrecuencia) sirvan como `carriers` de datos, los `wireless devices` utilizan `modulación` para ingresar `datos` a las ondas de radiofrecuencia. **

## 🟢 `802.11` - `Modulation Methods`

En el contexto de las redes `WiFi 802.11`, la `modulación` se refiere al **proceso de convertir una `señal digital`, que representa `bits de información`, en una `señal analógica` que se puede transmitir a través de un medio de comunicación, como el aire a través de `RF`. La `modulación` es una `técnica de transmisión` que permite enviar información a través de `ondas electromagnéticas` y es esencial para la `transmisión inalámbrica de datos`. <br>

La modulación es una técnica utilizada para transmitir información a través de una `señal de alta frecuencia`, llamada portadora o `carrier` que es modificada pra transmitir. Es decir, la `modulación` es una manera de **manipular un medio de comunicación, como una `onda de radio`, para representar `bits de información`**. La modulación puede ser de varios tipos, incluyendo:

### ⭕ `ASK (Amplitude Shift Keying)` 

En `ASK` o `modulación por desplazamiento de amplitud`, la `amplitud` de la `carrier wave` se modifica para representar los bits de información. Por ejemplo, si un bit 1 se representa aumentando la amplitud de la onda portadora y un bit 0 se representa manteniendo la amplitud sin cambios, entonces ASK se utiliza para transmitir información.

### ⭕ `PSK (Phase Shift Keying)` 

En `PSK` o `modulación por desplazamiento de fase`, la `fase` de la onda portadora se modifica para representar los bits de información. Por ejemplo, si un bit 1 se representa desplazando la fase de la onda portadora 180 grados y un bit 0 se representa sin cambios en la fase, entonces PSK se utiliza para transmitir información.

### ⭕ `FSK (Frequency Shift Keying)` 

En `FSK` o `modulación por desplazamiento de frecuencia`, `frecuencia` de la onda portadora se modifica para representar los bits de información. Por ejemplo, si un bit 1 se representa transmitiendo una onda portadora a una frecuencia más alta y un bit 0 se representa transmitiendo una onda portadora a una frecuencia más baja, entonces FSK se utiliza para transmitir información.

![image](https://user-images.githubusercontent.com/94720207/226231485-87e1936e-bdb9-4762-91bf-6882a28382c6.png)

**Actualmente la modulación `FSK` NO se utiliza en WLAN.** Los estándares de WiFi actuales `802.11a/b/g/n/ac/ax` utilizan principalmente la modulación `OFDM` para transmitir datos de manera eficiente y confiable. <br>

La modulación `ASK` se utiliza en **sistemas de comunicaciones de `baja velocidad`, como sensores inalámbricos y sistemas de control remoto, donde la transmisión de datos no requiere un alto ancho de banda.** <br> 

**La modulación `PSK` se utiliza en aplicaciones de comunicaciones de `alta velocidad`, como la comunicación satelital y la transmisión de datos de alta velocidad a través de fibra óptica. Específicamente, el estándar `802.11 WiFi` utiliza la `variante PSK` llamada `QPSK (Quadrature Phase Shift Keying)`, que permite transmitir dos bits por símbolo y, por lo tanto, aumenta la tasa de transferencia de datos** <br>

- **Como se puede observar, ninguna de estas modulaciones básicas son utlizadas actualmente para WiFi, pero son las bases que fundamentan todo el `esquema de modulación OFDM`, puesto que `OFDM` se compone de varios tipos de modulación que parten que es la principalmente utilizada en la actualidad para redes `Wifi 802.11` como lo son las `QPSK (basada en PSK)` y `QAM (basada en ASK)`**

---

### 🟣 `OFDM Modulation Scheme` = `QAM`/`BPSK`/`QPSK` Modulations

La razón por la que la modulación `OFDM (Orthogonal Frequency Division Multiplexing)` se describe comúnmente como un **"esquema de modulación" o `Modulation Scheme`** en lugar de simplemente una "modulación" o `modulation` es porque **`OFDM` NO es una técnica de modulación tradicional en sí misma, sino que se compone de varias técnicas diferentes de modulación.** <br> 

La `modulación` es una técnica utilizada para transmitir información a través de una `señal de alta frecuencia`, llamada portadora o `carrier`. En la modulación tradicional, esta portadora se modifica para transmitir la información. <br> 

Por otro lado, en el `OFDM modulation scheme`, la señal de información se divide en **varias señales de `baja frecuencia`**, llamadas subportadoras o `subcarriers`. Cada `subcarrier` se modula individualmente con una técnica de modulación convencional, como `QPSK` o `QAM`. <br> 

**Después de que cada `subcarrier` se modula, se combinan todas para formar la señal `OFDM` final que se transmite.** <br> 

![image](https://user-images.githubusercontent.com/94720207/226240066-e6ea677a-9339-47c2-870c-2fe018c34b35.png)

`OFDM` permite que **un solo AP transmita múltiples subportadoras con diferentes técnicas de modulación para adaptarse a diferentes necesidades de transmisión de información. Además, cada cliente puede recibir las subportadoras que mejor se adapten a sus necesidades específicas de transmisión.** <br>

Por ejemplo, si un `AP` necesita transmitir diferentes tipos de información a diferentes velocidades hacia diferentes clientes, puede usar diferentes técnicas de modulación en diferentes subportadoras para adaptarse a cada tipo de información y cada tipo de cliente/dispositivo. <br>

En cuanto a los clientes, cada cliente puede recibir las "subportadoras" que mejor se adapten a sus necesidades de transmisión. En otras palabras, **si un cliente necesita una alta velocidad de transmisión, el AP puede asignarle subportadoras con una técnica de modulación `más avanzada`, como `64-QAM`. Por otro lado, si un cliente está en un lugar con una señal débil o interferencia, el `AP` puede asignarle subportadoras con una técnica de modulación `menos avanzada`, como `QPSK`.** <br>

- **`Importante`: Mientras más rápida y compleja sea la modulación, es necesario que tenga mejor `señal/SNR`, es decir, a `64-QAM` le afecta mucho más el `ruido` y la `interferencia` que a `QPSK`** 

---

### 🟣 Factores que influyen a la elección de Modulación

Existen varios factores críticos para la elección adecuada de la modulación y codificación en la transmisión inalámbrica. Por ejemplo, a medida que la complejidad y la velocidad de la modulación aumentan, se requiere una señal más fuerte y una SNR más alta para asegurar la transmisión confiable de datos. Por lo tanto, los dispositivos que utilizan modulaciones más complejas, como 64-QAM o 256-QAM, deben estar ubicados más cerca del punto de acceso o tener menos interferencia para asegurar una transmisión exitosa. Además, la elección de la codificación de canal adecuada también puede mejorar la eficiencia de la transmisión y reducir la tasa de errores de transmisión. 

![image](https://user-images.githubusercontent.com/94720207/227722275-9f1c9ba5-f2c7-4895-821e-28fc9e5cef92.png)

A continuación se exponen algunos factores que influyen le lección de modulación en OFDM:

Señal: La calidad de la señal recibida afecta directamente la elección de la modulación. Modulaciones más complejas requieren una señal más fuerte para una transmisión efectiva de datos.

Relación señal-ruido (SNR): La relación señal-ruido es un factor crítico para la elección de la modulación. Las modulaciones más complejas requieren una SNR más alta para una transmisión efectiva de datos.

Ancho de banda disponible: El ancho de banda disponible en el canal inalámbrico puede limitar la tasa de transmisión de datos. Modulaciones más complejas requieren más ancho de banda para transmitir la misma cantidad de datos que una modulación más básica.

Interferencia en el canal: La interferencia en el canal puede afectar la calidad de la señal y reducir la tasa de transmisión de datos. Las modulaciones más complejas son más susceptibles a la interferencia y pueden ser menos efectivas en entornos con alta interferencia.

Distancia de transmisión: La distancia entre el transmisor y el receptor también es importante para determinar la elección de la modulación. Las modulaciones más complejas pueden ser efectivas a distancias cortas, pero pueden ser menos efectivas a distancias más largas.

Requerimientos de energía: Las modulaciones más complejas pueden requerir más energía para transmitir la misma cantidad de datos que una modulación más básica. Esto puede ser un factor importante a considerar en dispositivos que funcionan con batería.

---





---

### 🟣 `OFDM Modulation Scheme Subcarriers`

A continuación se explica el `OFDM Modulation Scheme` y las técnicas de modulación de sus `subcarriers` para redes `802.11 WiFi`:

![image](https://user-images.githubusercontent.com/94720207/227729443-fbb458b1-76bd-43ad-ba1d-7a169e90ca42.png)

### ⭕ `OFDM (Orthogonal Frequency Division Multiplexing)`

OFDM es una técnica de modulación que divide el ancho de banda disponible en una serie de subportadoras más estrechas, cada una de las cuales se modula individualmente utilizando una técnica de modulación como QAM, PSK, BPSK, QPSK, 16-QAM, 64-QAM o 256-QAM.

### ⭕ `BPSK (Binary Phase Shift Keying)`

BPSK (Binary Phase Shift Keying) es una forma de PSK en la que se utiliza una sola señal portadora que cambia de fase entre dos estados diferentes para representar los datos.

![image](https://user-images.githubusercontent.com/94720207/227410891-7deb087c-14fa-4ea5-9abe-a5cf3a579d16.png)


![image](https://user-images.githubusercontent.com/94720207/227403843-58842dee-697e-4853-bc52-aed31b5e878f.png)

![image](https://user-images.githubusercontent.com/94720207/227410671-f3b41dfb-c0d9-4eb5-8e27-12fdbf3e6bd5.png)





![image](https://user-images.githubusercontent.com/94720207/227403605-6e93eb0d-0aa7-4f69-9684-2cd9e9f0f6dc.png)

### ⭕ `QPSK (Quadrature Phase Shift Keying)`

QPSK (Quadrature Phase Shift Keying) es una forma de PSK en la que se utilizan dos señales portadoras en cuadratura, cada una de las cuales cambia de fase entre cuatro estados diferentes para representar los datos.

![image](https://user-images.githubusercontent.com/94720207/227410403-dc4da348-b660-4249-9ed5-fd706ca82695.png)

![image](https://user-images.githubusercontent.com/94720207/227410281-f3597e0c-3057-485e-965a-8302b595e81a.png)


![image](https://user-images.githubusercontent.com/94720207/227410268-3f8e7794-fd65-4d57-9368-9ca4b2f5ec0b.png)



### ⭕ `QAM (Quadrature Amplitude Modulation)` - `16-QAM`, `32-QAM`, `64-QAM`, `128-QAM`, 

QAM es una técnica de modulación que combina dos señales portadoras en cuadratura, cada una de las cuales se modula con una señal digital, para producir una señal compleja. La amplitud y la fase de la señal compleja se utilizan para transmitir la información. <br>

16-QAM, 64-QAM y 256-QAM son formas de QAM en las que se utilizan 16, 64 y 256 estados diferentes de amplitud y fase de la señal compleja para representar los datos. A medida que aumenta el número de estados de la señal, se puede transmitir más información en la misma cantidad de ancho de banda, pero se requiere una mayor precisión en la detección de la señal.

![image](https://user-images.githubusercontent.com/94720207/227402853-9bc8b232-1829-4c4a-bfae-db0abf2a7ff6.png)

![image](https://user-images.githubusercontent.com/94720207/227402972-ca67092a-d8fc-4762-8898-f4beb9399966.png)









![image](https://user-images.githubusercontent.com/94720207/226239572-61cab589-7986-415b-863a-9d88a5a1710e.png)




![image](https://user-images.githubusercontent.com/94720207/226239299-3e1fe2fc-b60d-4285-9d96-3370d56c682c.png)


![image](https://user-images.githubusercontent.com/94720207/226240122-754717bf-ddb6-483b-bef9-434fb72889a4.png)

---




















---


## 🟢 `MCS Table` - Modulation & Coding Scheme

- [Wireless LAN Professionals: `MCS Table and How You Can Use it`](https://youtu.be/QBiBPbME5tY)
- [Inside Wireless: `MCS Rates`](https://youtu.be/f6zesWNDGXc)
- [`VHT` (802.11n/ac) MCS Chart – Wave 1](https://www.wirelesstrainingsolutions.com/wireless-tools/vht-mcs-chart-wave-1/)

La `MCS Table` es una herramienta esencial para **evaluar la calidad del ambiente de RF y determinar el `data rate` en las redes Wi-Fi de `2.4 GHz` y `5 GHz`. Los `dispositivos inalámbricos`, como los `AP`, los `teléfonos celulares` y las `antenas WiFi`, deben **seleccionar la `modulación` y la `codificación` adecuadas para enviar datos en un canal específico.** <br>

La `MCS Table` establece la relación entre la `modulación` y la tasa de bits por segundo o `bit rate`, teniendo en cuenta la calidad del canal, la interferencia y otros factores. Además, la elección adecuada de la modulación y codificación es fundamental para optimizar la eficiencia y la confiabilidad de la transmisión inalámbrica, ya que una modulación y codificación más robusta pueden aumentar la tasa de transmisión pero también la posibilidad de errores de transmisión. En resumen, la MCS Table es una herramienta valiosa para garantizar la máxima eficiencia y fiabilidad de las redes inalámbricas. <br>

`MCS` agrupa varias cosas como:

1. `Modulation Scheme`
2. `Coding Rate`
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

|    **Standard**   	| **IETF Standard** 	| **Release Year** 	|   **Modulation**   	|     **Band**    	|           **Additional Technologies**          	| **MIMO Spatial Streams** 	| **Channel Bandwidth** 	| **Maximum Data Rate** 	|
|:-----------------:	|:-----------------:	|:----------------:	|:------------------:	|:---------------:	|:----------------------------------------------:	|:------------------------:	|:---------------------:	|:---------------------:	|
| **IEEE 802.11a**  	| _prime_           	| 1999             	| **OFDM**           	| 5 GHz           	| _N/A_                                          	| N/A                      	| 20 MHz                	| **54 Mbps**           	|
| **IEEE 802.11g**  	| _N/A_             	| 2003             	| **OFDM**           	| 2.4 GHz         	| _N/A_                                          	| N/A                      	| 20 MHz                	| **54 Mbps**           	|
| **IEEE 802.11n**  	| **Wi-Fi 4**       	| 2009             	| **OFDM & HT-OFDM** 	| 2.4 GHz & 5 GHz 	| **MIMO**                                       	| 1-4                      	| 20/40 MHz             	| **600 Mbps**          	|
| **IEEE 802.11ac** 	| **Wi-Fi 5**       	| 2013             	| **OFDM**           	| 5 GHz           	| **MU-MIMO More Channel Bandwidth**             	| 1-8                      	| 20/40/80/160 MHz      	| **6.9 Gbps**          	|
| **IEEE 802.11ax** 	| **Wi-Fi 6**       	| 2021             	| **OFDM & HE-OFDM** 	| 2.4 GHz & 5 GHz 	| **Optimized MU-MIMO Multiple Frequency Bands** 	| 1-12                     	| 20/40/80/160 MHz      	| **11 Gbps**           	|

Las tasas de datos más altas se logran utilizando modulaciones más complejas y una mayor cantidad de bits por símbolo, lo que aumenta la eficiencia espectral de la transmisión. Sin embargo, **estas tasas de datos máximas solo se pueden lograr en condiciones óptimas de transmisión**, y la tasa real de datos puede variar según las condiciones del entorno y el hardware utilizado.

---

### 💀 `Fz3r0 Pro Tip`: ¿Cómo leer la MCS Table like a sir?

Es mejor aprender con la `MCS Table` con la tabla de `802.11n/ac` ya que `802.11ax` se vuelve demasiado grande para comprender al principio. Sin embargo, al final es exctamente la misma manera de leerla. 

![image](https://user-images.githubusercontent.com/94720207/224502878-2edac492-fcc3-492d-86e1-f1f46740e546.png)

Antes de aprender a leer la `MCS Table`, hay que identificar exactamente `cada parte que la compone`, yo usaré el ejemplo de `802.11n/ac`, pero en realidad se puede leer cualquier `PHY` ya sea anterior o posterior a ese `Estándar IEEE`.** 

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

- Existen diferentes `técnicas de modulación`, como `BPSK`, `QPSK`, `16-QAM`, `64-QAM`, `256-QAM` y no sabemos que nos depara el futuro! 🤖
- Cada una de estas técnicas utiliza una diferente combinación de `amplitud`, `fase` y `frecuencia` de onda para representar `bits de información`. 

Las técnicas de modulación `más complejas`, como `64-QAM`, **pueden transmitir más bits de información en un solo `symbol` que las técnicas más simples, como `BPSK`**. Sin embargo, **las técnicas de modulación más complejas también son más susceptibles a errores de transmisión debido a la presencia de ruido y otros factores en el canal de comunicación.**

![image](https://user-images.githubusercontent.com/94720207/227726920-29c6ef1d-6fb5-442d-abc1-556ff7081c8b.png)

Por lo tanto, la elección de la técnica de modulación adecuada depende de varios factores, como la calidad de la señal, el ancho de banda disponible y la tasa de errores de transmisión permitida. Las combinaciones de técnicas de modulación y codificación que se muestran en una tabla MCS se organizan en función de su eficiencia en términos de:

1. Tasa de transferencia de datos = `data rate` 
2. Resistencia a errores de transmisión = `coding rate`

![image](https://user-images.githubusercontent.com/94720207/224521846-04cf91ad-dfac-4813-adeb-2afa274ed362.png)

---

### Coding Rate

### `Symbol`


| **Modulation** 	| **Symbols** 	| **Coding Rate**          	| **Bits per Symbol**     	| **Bit Combinations**  	| **Bits per Combination** 	| **BER per Symbol**           	| **SER per Symbol**          	| **Minimum SNR**                  	| **Data Rate**                                  	|
|----------------	|-------------	|--------------------------	|-------------------------	|-----------------------	|--------------------------	|------------------------------	|-----------------------------	|----------------------------------	|------------------------------------------------	|
| **BPSK**       	| 2           	| 1/2<br>3/4               	| 1<br>1.5                	| 00, 01, 10, 11        	| 2 bits                   	| 0.08<br>0.04                 	| 0.08<br>0.04                	| 9 dB<br>12 dB                    	| 6 Mbps<br>9 Mbps                               	|
| **QPSK**       	| 4           	| 1/2<br>3/4               	| 2<br>2.25               	| 00, 01, 10, 11        	| 2 bits                   	| 0.11<br>0.07                 	| 0.11<br>0.07                	| 12 dB<br>16 dB                   	| 12 Mbps<br>18 Mbps                             	|
| **16-QAM**     	| 16          	| 1/2<br>3/4<br>5/6        	| 4<br>4.5<br>4.8         	| 0000-<br>1111         	| 4 bits                   	| 0.15<br>0.11<br>0.09         	| 0.6<br>0.44<br>0.36         	| 18 dB<br>22 dB<br>24 dB          	| 24 Mbps<br>36 Mbps<br>48 Mbps                  	|
| **64-QAM**     	| 64          	| 1/2<br>2/3<br>3/4<br>5/6 	| 6<br>6.67<br>7.2<br>7.2 	| 000000-<br>111111     	| 6 bits                   	| 0.21<br>0.16<br>0.13<br>0.11 	| 1.34<br>1.02<br>0.83<br>0.7 	| 21 dB<br>24 dB<br>27 dB<br>30 dB 	| 33.6 Mbps<br>44.8 Mbps<br>48 Mbps<br>72.2 Mbps 	|
| **256-QAM**    	| 256         	| 3/4<br>5/6               	| 8.25<br>9.6             	| 00000000-<br>11111111 	| 8 bits                   	| 0.13<br>0.11                 	| 3.3<br>2.8                  	| 24 dB<br>27 dB                   	| 72 Mbps<br>86.7 Mbps                           	|

En la transmisión de datos inalámbrica, un símbolo es la unidad básica de información que se transmite de un dispositivo a otro.

Cada símbolo representa una combinación de valores de amplitud, fase y/o frecuencia, que se modulan para transmitir información. La elección de la técnica de modulación adecuada (por ejemplo, BPSK, QPSK, 16-QAM, etc.) determina el número de estados que se pueden representar con cada símbolo y la cantidad de bits de información que se pueden transmitir en cada símbolo.

Por ejemplo, en una modulación BPSK, cada símbolo representa uno de dos estados posibles, que pueden representar los bits 0 o 1. En una modulación QPSK, cada símbolo representa uno de cuatro estados posibles, que pueden representar combinaciones de dos bits (00, 01, 10, 11). En una modulación 16-QAM, cada símbolo representa uno de 16 estados posibles, que pueden representar combinaciones de 4 bits (0000, 0001, 0010, etc.).

### `Coding` AKA `Coding Rate`

- [Iain Explains - `What are Channel Capacity and Code Rate?`](https://www.youtube.com/watch?v=P0WY96WBUyA)

- El `coding rate` en redes inalámbricas es la **proporción de `bits de información transmitidos` en comparación con la `cantidad total de bits transmitidos`**, lo que **incluye bits redundantes para la corrección de errores.** 
- Un `coding rate alto aumenta la confiabilidad` de la transmisión pero `disminuye la eficiencia de la transmisión`. La elección del `coding rate` depende de la calidad de la señal y otros factores para lograr un equilibrio entre la eficiencia y la confiabilidad de la transmisión.



### BER y SER

El Error Rate o Tasa de Error Bit (BER, por sus siglas en inglés) representa la probabilidad de que un bit se transmita incorrectamente en una transmisión de datos. El valor del BER se expresa como un número decimal entre 0 y 1, o como un porcentaje entre 0% y 100%.

Por ejemplo, si la tasa de error por símbolo es de 0.08 para la modulación BPSK con una tasa de código de 1/2, significa que, en promedio, se espera que el 8% de los bits transmitidos sean recibidos de manera incorrecta.

(BER y SER) se representan como un número decimal entre 0 y 1, o como un porcentaje entre 0% y 100%.

Por ejemplo, si la tasa de error de bits (BER) es 10^-6, esto significa que en promedio, un bit de cada millón se transmitirá incorrectamente. Si se expresa como un porcentaje, sería 0.0001%.

Si la tasa de error de símbolos (SER) es 10^-3 para una modulación QPSK, significa que en promedio, 1 de cada 1000 símbolos se transmitirá incorrectamente. Si se expresa como un porcentaje, sería 0.1%.

En términos generales, cuanto más baja sea la tasa de error (ya sea BER o SER), mejor será la calidad de la transmisión. Es importante tener en cuenta que estas medidas pueden variar según los diferentes parámetros de la comunicación, como la modulación, la tasa de datos, el SNR y el tipo de codificación utilizada.





![image](https://user-images.githubusercontent.com/94720207/224524309-07be4db5-af3b-45fe-8fcd-71bbb0b068a3.png)

El parámetro de `coding` se refiere a la tasa de codificación `code rate` utilizada en la transmisión de datos wireless y se expresan como una fracción que indica la cantidad de bits codificados por cada símbolo transmitido. La `coding rate` es la relación entre la cantidad de bits de información transmitidos y la cantidad total de bits transmitidos, incluyendo los bits de control y corrección de errores.

Por ejemplo, en el caso de "bpsk coding = 1/2", significa que se utiliza una modulación BPSK (Binary Phase Shift Keying) para transmitir los datos, y se está codificando cada bit con una longitud de código de 1, lo que resulta en una tasa de codificación de 1/2. Esto significa que por cada símbolo transmitido, se están enviando 2 bits de información.

De manera similar, en el caso de "qpsk coding = 3/4", significa que se está utilizando una modulación QPSK (Quadrature Phase Shift Keying) para transmitir los datos, y se está codificando cada bit con una longitud de código de 2, lo que resulta en una tasa de codificación de 3/4. Esto significa que por cada símbolo transmitido, se están enviando 3 bits de información.

![image](https://user-images.githubusercontent.com/94720207/227722433-84a79817-2966-4dc1-b95d-f3a93b0cdb95.png)

En general, cuanto mayor sea la tasa de codificación, mayor será la cantidad de información que se puede transmitir en un período de tiempo determinado. Sin embargo, a medida que aumenta la tasa de codificación, también aumenta la sensibilidad de la transmisión a la interferencia y al ruido en la señal, lo que puede reducir la calidad y la confiabilidad de la transmisión.

Por lo tanto, la elección de la tasa de codificación adecuada depende de las condiciones específicas de la red y del tipo de datos que se están transmitiendo, y debe ser cuidadosamente seleccionada para optimizar la eficiencia y la confiabilidad de la transmisión.




![image](https://user-images.githubusercontent.com/94720207/227722487-4b573a45-e2ab-4df1-8dab-be08a7c428b6.png)




![image](https://user-images.githubusercontent.com/94720207/227722554-38e475a7-6f4e-4db5-910e-11f7c4965bb7.png)



---


### Guard Interval

El GI se define como un período de tiempo que se utiliza para proporcionar una separación entre símbolos adyacentes en la transmisión de datos en una red inalámbrica. El GI se agrega como un intervalo entre los símbolos de datos transmitidos y se utiliza para proporcionar una protección contra el desvanecimiento de la señal y la interferencia.

![image](https://user-images.githubusercontent.com/94720207/227756891-f5129820-82fc-4dd3-9b3d-528947a7683e.png)

La separación entre símbolos adyacentes en la transmisión de datos en una red inalámbrica, como el Guard Interval (GI), se utiliza para ayudar a reducir los efectos del desvanecimiento de la señal y la interferencia en la transmisión de datos.

![image](https://user-images.githubusercontent.com/94720207/227756794-3daf6555-cbd7-4a57-94fd-7bce50ae086f.png)

El desvanecimiento de la señal ocurre cuando la intensidad de la señal inalámbrica se atenúa debido a obstáculos en el camino de la señal o la distancia entre el transmisor y el receptor. La interferencia, por otro lado, ocurre cuando hay señales inalámbricas adicionales que pueden superponerse con la señal original, causando distorsión en la señal y reduciendo su calidad.

La separación entre símbolos adyacentes ayuda a reducir estos efectos de desvanecimiento e interferencia, proporcionando un tiempo muerto entre la transmisión de los símbolos de datos. Esto permite que la señal inalámbrica se recupere y se estabilice antes de la transmisión del siguiente símbolo de datos. Además, al aumentar el tiempo entre los símbolos de datos, se reduce la probabilidad de que se produzca una superposición o interferencia entre los símbolos adyacentes.

![image](https://user-images.githubusercontent.com/94720207/227756849-97d79fb8-37ca-4335-952d-998abf645c13.png)

En resumen, la separación entre símbolos adyacentes en la transmisión de datos en una red inalámbrica es necesaria para ayudar a reducir los efectos del desvanecimiento de la señal y la interferencia, y mejorar la calidad y la confiabilidad de la transmisión de datos en la red inalámbrica.

---

### Elección del Guard Interval 

La elección del guard interval (GI) en una red inalámbrica 802.11 depende de varios factores, como la velocidad de transmisión de datos, la calidad de la señal inalámbrica y el entorno de la red.

En general, cuanto más corto es el GI, mayor es la velocidad de transmisión de datos que se puede lograr en una red inalámbrica. Sin embargo, un GI más corto también significa menos protección contra el desvanecimiento de la señal y la interferencia, lo que puede reducir la calidad y la confiabilidad de la transmisión de datos.

![image](https://user-images.githubusercontent.com/94720207/227756684-2a39afbb-ba85-49ff-aed3-63bc144253a8.png)

El AP (punto de acceso) y la STA (estación) pueden ambos establecer el GI utilizado en la transmisión de datos. En la mayoría de los casos, el AP establece el GI utilizado en la red y la STA lo sigue. Sin embargo, en algunos casos, la STA puede establecer su propio GI en la transmisión de datos.

En la mayoría de los casos, el GI se establece automáticamente en función de la velocidad de transmisión de datos seleccionada. Por ejemplo, en una red inalámbrica 802.11ac, el GI se establece automáticamente en 320 ns para velocidades de transmisión de datos de 80 MHz y 160 MHz. Para velocidades de transmisión de datos de 20 MHz y 40 MHz, el GI se establece automáticamente en 800 ns.

Por ejemplo, los controladores/AP de Ruckus no tienen la opción de establecer explícitamente SGI/LGI, se deja a decisión del cliente/AP basado en el entorno. En la mayoría de los casos, los clientes negocian con la bandera SGI-False (LGI).

En algunos otros casos como en la WLC de Aruba, es posible ajustar manualmente el GI en una red inalámbrica. Por ejemplo, algunos controladores de tarjetas de red inalámbricas permiten la configuración manual del GI utilizado en la transmisión de datos.

![image](https://user-images.githubusercontent.com/94720207/227757109-63212fe0-b91e-40ca-bcaa-36e05aa42bc5.png)

---

### Evolución del Guard Interval

En las redes inalámbricas 802.11b y 802.11g, se utiliza un GI de 800 ns. Esto significa que después de cada símbolo de datos, se agrega un intervalo de tiempo de 800 ns antes de que se transmita el siguiente símbolo. En las redes inalámbricas 802.11a y 802.11n, se utilizó un GI de 400 ns, lo que permitió una transmisión de datos más rápida en comparación con las redes 802.11b y 802.11g.

En la especificación 802.11ac, se introdujo el GI de 320 ns. Este intervalo de tiempo más corto permitió una mayor eficiencia en la transmisión de datos, lo que resultó en un mayor rendimiento de la red inalámbrica. El GI de 320 ns también proporcionó una mejor protección contra la interferencia y el desvanecimiento de la señal, lo que mejoró la calidad de la transmisión de datos en la red.

Finalmente, en la especificación 802.11ax, se ha introducido el GI de 160 ns. Este GI aún más corto permite una mayor eficiencia en la transmisión de datos y una mayor velocidad de la red inalámbrica. El GI de 160 ns también proporciona una protección mejorada contra la interferencia y el desvanecimiento de la señal, lo que mejora aún más la calidad de la transmisión de datos en la red.

En resumen, el GI en las redes inalámbricas 802.11 se ha ido reduciendo en tamaño a medida que la tecnología ha evolucionado. Esto ha permitido una mayor eficiencia y velocidad de transmisión de datos en las redes inalámbricas más modernas y avanzadas, así como una mejor protección contra la interferencia y el desvanecimiento de la señal.



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

**En un entorno ideal y "mundo perfecto", donde todas las `STAs` tienen la misma `señal`, `calidad` y `distancia de conexión`, etc... el `throughput` (es decir, el `bandwith` total disponible) se distribuiría equitativamente entre las `STAs`.** <br>

**Sin embargo, cuando hay un `mayor tráfico generado por una STA`, es probable que `esta STA tenga un mayor throughput` en comparación con las estaciones que generan menos tráfico.**

- `Por ejemplo`: Una `STA` que está haciendo `stream en 4k` puede tener un `mayor throughput`, en comparación con una `STA` que solo está mandando `mensajes de texto` por WhatsApp.

![image](https://user-images.githubusercontent.com/94720207/224558297-b6c1ab57-4caf-489c-ac95-b7023087581a.png)


![image](https://user-images.githubusercontent.com/94720207/224558987-ef8e02b8-53af-481d-886a-1d9ae7621891.png)

- **Un test de `"velocidad de internet"` como el que ofrece `speedtest.com` en realidad mide el `throughput` de la conexión de un usuario hacia los servidores del ISP, no el `Bandwith` asignado por el ISP.** 
- El throughput medido por el test de velocidad indica la cantidad de datos que se pueden transmitir en un período de tiempo determinado, lo que refleja la capacidad real de la conexión de un usuario en ese preciso momento.

Es importante tener en cuenta que el `bandwith asignado` por el ISP puede variar en función de diferentes factores lo cual resulta en el `throughput` real, como la hora del día, la demanda de la red y la calidad de la conexión física. Por lo tanto, el ancho de banda asignado puede no ser siempre el mismo que el anunciado por el ISP, y es posible que el throughput real que se pueda obtener en un momento determinado sea menor al anunciado.












## 🟢 `Industry Troubleshooting Methods`

Los métodos de `troubleshooting` en `redes inalámbricas` se refieren al **conjunto de pasos que se utilizan para `identificar y resolver problemas` en la `conectividad`, `rendimiento` y `seguridad` de las redes inalámbricas**. Estos métodos suelen incluir la identificación del problema, la recopilación de datos, el análisis de datos, las pruebas y la implementación de soluciones. <br>

Cada vendor (proveedor) de equipos de redes inalámbricas puede tener sus propios métodos y pasos específicos para el troubleshooting de problemas. Esto se debe a que cada proveedor puede tener su propia tecnología y enfoque para la implementación de redes inalámbricas, lo que puede afectar la forma en que se resuelven los problemas. <br>

Además, cada vendor puede tener diferentes herramientas y recursos de soporte disponibles para ayudar en el proceso de troubleshooting, lo que puede influir en los métodos y pasos que se utilizan. Por ejemplo, algunos vendors pueden tener herramientas de diagnóstico específicas para su hardware y software, mientras que otros pueden requerir herramientas de terceros. <br>

### 🚨☢️ `Importante` ☢️🚨

- **En el exámen `CWAP` no se pregunta por ningún método de troubleshooting específico de un vendor, sin embargo, se pregunta del `CWNP Troubleshooting Method` que abordaré más adelante**

--- 

### 🟣 `Cisco Troubleshooting Process`

- [Cisco Troubleshooting Process](https://www.cisco.com/en/US/docs/internetworking/troubleshooting/guide/tr1901.html)

El `Cisco Troubleshooting Process` es un marco de trabajo utilizado para identificar y resolver problemas en redes y tecnologías de `Cisco Networks`. Este proceso sigue `8 pasos` sistemáticos para garantizar que los problemas sean identificados de manera efectiva y resueltos de manera rápida.  <br>

Los pasos del proceso son los siguientes:

1. ⭕ `Definir el problema`: para analizar adecuadamente el problema, es necesario definirlo en términos de síntomas y posibles causas. Identifique los síntomas generales y determine qué tipos de problemas (causas) podrían provocar estos síntomas.

2. ⭕ `Recopilar información`: recopile información de fuentes como sistemas de gestión de red, trazas de analizadores de protocolo, salida de comandos de diagnóstico de enrutadores o notas de lanzamiento de software. También debe hacer preguntas a los usuarios afectados, administradores de red, gerentes y otras personas clave.

3. ⭕ `Considerar posibles problemas`: utilizando la información recopilada, elimine algunos de los posibles problemas de su lista. Trate de reducir el número de problemas potenciales para crear un plan de acción eficiente.

4. ⭕ `Crear un plan de acción`: cree un plan de acción basado en los problemas potenciales restantes. Comience con el problema más probable y diseñe un plan en el que solo se manipule una variable a la vez.

5. ⭕ `Implementar el plan de acción`: realice cada paso del plan con cuidado mientras prueba para ver si el síntoma desaparece.

6. ⭕ `Recolectar resultados`: siempre que cambie una variable, asegúrese de recopilar resultados de la misma manera que lo hizo en el paso 2.

7. ⭕ `Analizar los resultados`: analice los resultados para determinar si el problema ha sido resuelto. Si es así, el proceso ha terminado.

8. ⭕ Si el problema no se ha resuelto, cree un nuevo plan de acción basado en el siguiente problema más probable en su lista. Regrese al paso 4, cambie una variable a la vez y repita el proceso hasta que se resuelva el problema.

_Se puede obtener información más detallada de este método en el link que compartí al inicio._

--- 

### 🟣 `Cisco Troubleshooting Process`



































---

## 🟢 `Services` Provided by `802.11 Devices`

- [Tech Mike: `Wireless in all the areas`](https://techimike.com/cwna-chapter-7-wireless-in-all-the-areas/)

Los `802.11 Services` son servicios definidos por el `IEEE 802.11 Standard` para redes inalámbricas, también conocidad como `WiFi`. **Estos servicios son una serie de funciones que permiten a los dispositivos inalámbricos comunicarse y establecer conexiones en la red.**

Los `dispositivos 802.11` brindan específicamente `2 servicios` que permiten comunicaciones en la `Layer 1` y `Layer 2`.

1. **`SS (Station Service)`**
2. **`DSS (Distribution System Service)`**
3. **`PCPS (PBSS Control Point Service)`** _Fuera del alcance del CWAP_

- Nota: El `PCPS` funciona para redes `personal basic service set (PBSS)` las cuales están **fuera del alcance del `CWAP`** y redes de alta densidad.

### 🟣 `SS (Station Service) `

El `SS (Station Service)` o "Servicio de Estación" se refiere a los servicios proporcionados por una STA en la red Wi-Fi. Estos servicios incluyen la `autenticación`, la `asociación` y la `desasociación` de dispositivos en la red. La `STA` también proporciona `servicios de entrega de datos` a través de la red y puede `administrar el tráfico de la red`.

- El `SS (Station Service)` es un conjunto de servicios los cuales admiten `MSDU` entre `STA` dentro de un `BSS`. 
- **El `SS` está en todas las `STA`, incluidos los `AP`, `mesh gates`, `portals` y `clients`.**

Existen `2 tipos de STA` diferentes, tanto la `Client Station` como la `Access Point Station` se consideran como `STA (Station)` en el `802.11 Standard`. La `STA` es el **término genérico utilizado para referirse a cualquier dispositivo que pueda conectarse a una red inalámbrica y que tenga la capacidad de transmitir y recibir datos de forma inalámbrica.**

1. **`Client Station`** 
    - Se refiere a **cualquier dispositivo** que se conecta a una red inalámbrica, **pero NO actúa como AP**. 
    - Es decir, tiene una conexión de nivel 2 con el AP y puede utilizar la red inalámbrica para comunicarse con otros dispositivos en la red. 
    - Cuando un dispositivo "Client Station" se conecta a un punto de acceso, se considera "asociado" <br><br>
3. `AP Station`


"Client Station" . . Es decir, tiene una conexión de nivel 2 con el punto de acceso y puede utilizar la red inalámbrica para comunicarse con otros dispositivos en la red.

Un "Access Point Station" es un dispositivo que funciona como punto de acceso para los dispositivos "Client Station". El punto de acceso proporciona una puerta de enlace para que los dispositivos se comuniquen de forma inalámbrica y también les permite acceder a una conexión física como Ethernet a través del "Distribution System Access Function (DSAF)". El punto de acceso mantiene una tabla de asociación de los dispositivos "Client Station" conectados y dirige el tráfico en la red.

Los `10 servicios` que conforman la `SS` son los siguientes:

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

El DS es el sistema o red a través del cual las STA con DSS (AP) se interconectan o, más específicamente, a través del cual las redes Basic Service Set (BSS) se interconectan una con otra

El DS Medium (DSM) es el medio utilizado por el DS, como por ejemplo cables Ethernet (como UDP o fibra),  RF Mesh, etc.

Los `10 servicios` que conforman la `DSS` son los siguientes:

1. **`Service Name`**
2. **`Service Set Identifier (SSID)`**
3. **`Basic Service Set (BSS)`**
4. **`Basic Service Area (BSA)`**
5. **`Basic Service Set Identifier (BSSID)`**
6. **`Multiple Basic Service Set Identifiers`**
7. **`Extended Service Set (ESS)`**
8. **`Independent Basic Service Set (IBSS)`**
9. **`Personal Basic Service Set (PBSS)`**
10. **`Mesh Basic Service Set (MBSS)`**

| **Service Name**                           	| **Descripción**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
|--------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| **Service Set Identifier (SSID)**          	| Es el nombre lógico que se le da a una red 802.11 para identificarla. Para un roaming adecuado, el SSID y la seguridad deben ser exactamente iguales.                                                                                                                                                                                                                                                                                                                                                                  	|
| **Basic Service Set (BSS)**                	| Consiste en un punto de acceso (AP) con una o más estaciones de cliente, que tienen conectividad L2. Cuando tienen esta conectividad L2, están asociados. Si en casa tienes un solo enrutador inalámbrico y no tienes otros puntos de acceso inalámbrico, esto se consideraría un BSS.                                                                                                                                                                                                                                 	|
| **Basic Service Area (BSA)**               	| El área de cobertura producida por su BSS es el BSA. Es la cobertura proporcionada por un solo AP. El tamaño y la forma de esta cobertura varían según la ubicación del AP, la potencia de transmisión, la ganancia de la antena, el entorno y la sensibilidad de recepción.                                                                                                                                                                                                                                           	|
| **Basic Service Set Identifier (BSSID)**   	| La dirección MAC de la radio de los APs es el BSSID. Cada radio de AP debe tener un BSSID único para permitir el roaming de las estaciones de clientes de un BSS a otro. De nuevo, necesitamos asegurarnos de que el SSID y la seguridad sean los mismos de BSS a BSS. Este movimiento de un AP a otro durante el proceso de roaming se llama transición de BSS. El BSSID se encuentra en el encabezado MAC 802.11.                                                                                                    	|
| **Multiple Basic Service Set Identifiers** 	| A menudo necesitará tener múltiples SSID en un solo AP. Se recomienda mantener esto al mínimo. Lo más recomendado es limitarlo a tres si es posible. Dicho esto, cuando tenga más de uno, necesitará un identificador de BSSID L2 único. Cuando esto ocurre, el AP creará una MAC única en incrementos de su MAC codificada en hardware, cada una asignada a una red L3 vlan única. Cada SSID adicional agrega sobrecarga en forma de balizas, respuestas de sonda y otras sobrecargas de marcos de gestión y control. 	|
| **Extended Service Set (ESS)**             	| Es cuando tiene dos o más BSS configurados de manera idéntica conectados por un medio DS. Puede pensar en esto como todos los AP y clientes que están unidos por un DSM. El área de cobertura del ESS en la que los clientes pueden comunicarse y cambiar de AP se llama área de servicio extendida (ESA). Solo porque tenga un ESS no significa que tenga un roaming garantizado.                                                                                                                                     	|
| **Independent Basic Service Set (IBSS)**   	| Solo radios de clientes, sin APs. Los clientes se comunican directamente. También conocido como peer-to-peer o ad-hoc. Todos los clientes deben compartir el tiempo del medio y respetar el mismo canal. El primer cliente que se conecta crea el BSSID.                                                                                                                                                                                                                                                               	|
| **Personal Basic Service Set (PBSS)**      	| Utilizado para comunicación directa entre estaciones 802.11ad en la banda de 60GHz. Un cliente asume el rol de punto de control PBSS (PCP) y sincroniza la comunicación entre todos los clientes.                                                                                                                                                                                                                                                                                                                      	|
| **Mesh Basic Service Set (MBSS)**          	| Conjunto de APs que proporcionan distribución de malla. Los AP conectados a la red cableada son llamados puertas de enlace o "mesh gate". Los AP no conectados a la red cableada forman conexiones inalámbricas de backhaul hacia las puertas de enlace y se conocen como puntos de malla. La selección de ruta se realiza mediante el protocolo HWMP, basado en métricas como RSSI, SNR, carga del cliente y cantidad de saltos. La selección de ruta se realiza mediante MAC y no mediante IP.                       	|

![image](https://user-images.githubusercontent.com/94720207/227790313-3c22efa8-3160-4af1-b82a-21937547f973.png)


![image](https://user-images.githubusercontent.com/94720207/227790252-ef2dafde-f83e-43c8-9024-f2600658ae6e.png)





























https://www.wirelesstrainingsolutions.com/understanding-ofdm-part-4-refresh/







- [Sunny: `Bandwidth, throughput, and speed`](https://www.youtube.com/watch?v=TVpg7StOxgg)
- [Lian Explain Signals: `How are Throughput, Bandwidth, and Data Rate Related?`](https://youtu.be/IY6fDYwC2fU)







- [OFDM Frame Structure](https://rfmw.em.keysight.com/wireless/helpfiles/89600b/webhelp/Subsystems/wlan-ofdm/Content/ofdm_80211-overview.htm)
