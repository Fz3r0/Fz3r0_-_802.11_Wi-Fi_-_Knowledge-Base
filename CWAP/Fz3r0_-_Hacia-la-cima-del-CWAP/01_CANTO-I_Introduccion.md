# 👹 `CANTO I`: Introducción al CWAP 

La certificación **`CWAP (Certified Wireless Analysis Professional)`**, otorgada por la prestigiosa organización **`CWNP (Certified Wireless Network Professional)`**, representa una credencial de alto nivel en el ámbito de las `Wireless Networks`. Diseñada específicamente para aquellos profesionales que buscan demostrar su competencia en el **análisis avanzado y resolución de problemas en entornos de redes inalámbricas**, esta certificación implica un conocimiento profundo de `Wireless Network Protocols`, `Wireless Network Security` y `High-Performance Wireless Network Design`. <br>

- Los profesionales que buscan obtener la certificación `CWAP` deben demostrar un amplio conocimiento de los principios y técnicas de análisis de redes inalámbricas, protocolos, así como habilidades para resolver problemas complejos y mejorar tanto rendimiento como la seguridad de redes inalámbricas para diferentes tipos de verticales, incluyendo redes complejas y de alta densidad.

Los temas abordados en la certificación `CWAP` incluyen la **captura y análisis de tráfico inalámbrico, análisis de espectro, la identificación y solución de problemas de cobertura y rendimiento, el análisis de interferencias y la aplicación de soluciones de seguridad inalámbrica**. A través de la certificación `CWAP`, los profesionales pueden demostrar su experiencia en la gestión y optimización de redes inalámbricas avanzadas y su capacidad para abordar los desafíos de análisis y resolución de problemas en entornos de red inalámbrica complejos. <br>

En este writeup, incluyo los demas de estudio y mi camino hacia la certificación `CWAP`, cubriendo **TODOS** los temas incluidos en el plan de estudios oficial de `CWNP`. ¡Pero no solo eso! la intención es abordar y profundizar temas que no se presentan en la documentación oficial, brindando una comprensión completa de los desafíos y soluciones en el análisis avanzado de redes inalámbricas y un panorame más amplio en cuanto al conocimiento requerido. 

También incluyo mis propios laboratorios de prácticas, análisis y laboratorios, en los cuales no solo incluyo temas relacionados con análisis de protocolos y de espectro, sino también temas como packet forging y packet tampering con Scappy o laboratorios de Pentesting y Hacking Ético de redes 802.11, útil para otras certificaciones de Wireless 802.11.

**Este documento es una bitácora de mi expedición: `hacia la cima del CWAP`. 🗻** <br><br>

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/225515551-3de68463-c5b1-4573-8a22-bfa77fd7e834.png" alt="CWAP" height=165px/> </a>   </p> 

---

### 🟢 Perfil de un `Wireless Analysis Professional` - `CWAP Engineer`

Un ingeniero `CWAP (Certified Wireless Analysis Professional)` debe tener una amplia gama de habilidades para **diseñar, implementar, solucionar problemas y asegurar el rendimiento de las redes inalámbricas.** <br>

1. Debe estar capacitado para **realizar un `análisis exhaustivo de la red inalámbrica`, incluyendo el análisis de tráfico, la identificación de interferencias, el diagnóstico de problemas de conectividad y la resolución de problemas de rendimiento. Para ello, deben utilizar `herramientas de captura de tráfico` y `análisis de protocolos`, como Wireshark, y `herramientas de análisis de espectro`, como los `analizadores de espectro Wi-Fi`.**

2. Debe ser capaz de **diseñar e implementar redes inalámbricas seguras y de alto rendimiento, considerando factores como la cobertura, la capacidad, la interferencia, la calidad de servicio, la compatibilidad con los dispositivos cliente y la seguridad de la red**. Además, deben estar familiarizados con las últimas tecnologías y normas de la industria, como Wi-Fi 6, 802.11ac Wave 2, WPA3, entre otras.** 

3. Tener la capacidad de **realizar `troubleshooting` de conectividad y rendimiento en tiempo real. Para ello, deben utilizar herramientas de monitoreo de red en tiempo real, que les permiten detectar problemas de conectividad, interferencias, problemas de autenticación y otros problemas de rendimiento.** 

4. Debe tener una **sólida comprensión de la seguridad de las redes inalámbricas, incluyendo la autenticación, el cifrado y la prevención de intrusiones. Esto les permite diseñar e implementar redes seguras que cumplan con los requisitos de privacidad y seguridad de los usuarios.** 

**El ingeniero `CWAP` debe ser capaz de diseñar, implementar, solucionar problemas y asegurar el rendimiento de las redes inalámbricas, utilizando herramientas especializadas y conocimientos avanzados en tecnologías inalámbricas, protocolos y seguridad de redes. Estas habilidades les permiten ofrecer soluciones eficaces y de alta calidad a las organizaciones que utilizan redes inalámbricas, incluyendo las tecnologías más recientes.** 

<div align="center">

![image](https://media.tenor.com/C2ZnZj6Gl-gAAAAM/anime-dragon-ball.gif)

 </div>

---

### 🟢 Conocimiento Requerido para `CWAP-402`

- [CWAP® - Certified Wireless Analysis Professional - Current version: CWAP-404 released in September 2021](https://www.cwnp.com/certifications/cwap)

La tabla presentada muestra los la manera en la que el examen `CWAP-402` está dividido, según fuentes oficiales de `CWNP`

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

## 🚨☢️ `Importante`: Antes de tomar el CWAP ☢️🚨

**Para presentar el examen de certificación `CWAP`, es necesario tener acreditado el examen `CWNA` y que éste se encuentre vigente.** El `CWNA` es un requisito previo para poder presentar el examen `CWAP`, ya que **se considera una base fundamental en cuanto a los conocimientos y habilidades necesarios para entender y manejar el protocolo de redes inalámbricas `IEEE 802.11`.** <br>

**Además, se recomienda tener una serie de conocimientos previos y certificaciones que pueden ser de gran ayuda para el candidato, tales como:**

### 1. ✅ `Routing & Switching` + `Network Protocols`

- La certificación `CWAP` se enfoca en la implementación y análisis de redes inalámbricas (WiFi), pero es necesario tener conocimientos sólidos de routing y switching a nivel LAN (redes cableadas) porque las redes inalámbricas se conectan y comunican con las redes cableadas.
- Además, las redes inalámbricas se integran con la red cableada para permitir el acceso a los recursos compartidos. De hecho, tanto clientes Wireless o Wired puedes comuicarse entre si por igual  


- Por lo tanto, es importante entender la topología y arquitectura de la red a nivel de switching y routing para obtener la certificación CWAP con éxito.

Personalmente recomiendo el `Cisco CCNA`, `CompTIA Network+` y `Ruckus ICX Implementer`, que son certificaciones reconocidas en la industria que cubren los `fundamentos de networking`, incluyendo `routing` y `switching`, además de funamentos de `Wireless`. Estas certificaciones son diseñadas para proporcionar una comprensión sólida de cómo funcionan las redes, cómo se conectan y cómo se comunican los dispositivos en una red.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/226084436-c5f11a9c-9e3b-49ce-82d1-cbf5e2696775.png" alt="CWAP" height=145px/> </a>   </p> 



### 3. ✅ `Wireless` = `CWNP: CWNA`

- Es necesario contar con la certificación CWNA, ya que esta certificación es la base fundamental para comprender el protocolo de redes inalámbricas y es obligatoria para presentar el CWAP.
- Es importante tener un conocimiento profundo sobre las tecnologías inalámbricas, incluyendo los diferentes estándares de redes inalámbricas, protocolos de seguridad, administración de redes inalámbricas, entre otros. <br> <br>

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/227316603-2adc530c-54a7-453b-9fe5-7719b71c975e.png" alt="CWAP" height=130px/> </a>   </p> 




### 4. ✅ `Network Security` (ej. `Offensive Security: OSCP`, `Comptia: Security+`)

- Es importante tener conocimientos sólidos sobre seguridad en redes inalámbricas, incluyendo el uso de VPNs, autenticación y autorización de usuarios, cifrado de datos, entre otros. 
- En este caso, la certificación Security+ de CompTIA puede ser de gran ayuda, aunque también hay una gran gama que se pueden seleccionar, además que son temas también abordados durante el `CWNA`. <br>

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/226111039-0910d2b0-e838-4ce5-801e-3afdcc3b9a98.png" alt="CWAP" height=165px/> </a>   </p> 

### 5. ✅ `Wireless Security` (ej. `CWNP: CWSP`,  `Offensive Security: OSWP`)

- Se recomienda tener conocimientos básicos a intermedios de `Wireless Security` antes de cursar `CWAP`
- `CWAP` puede ir de la mano con otras certificaciones de `Wireless Security` como el `CWSP` y el `OSWP`
- El examen CWAP cubre temas avanzados de seguridad inalámbrica y es un paso hacia otras certificaciones relacionadas con la seguridad inalámbrica.
- El CWAP aborda el análisis de Frames 802.11 enfocados a Sucurity, lo que es esencial para detectar y solucionar vulnerabilidades en la red inalámbrica.

![image](https://user-images.githubusercontent.com/94720207/236709020-8995daab-5a30-45f8-b42e-a02bb93d4e68.png)


### 6. ✅ `Protocol Analysis` (ej. `Wireshark`, `TCP Dump`)

- Wireshark es una herramienta de análisis de tráfico de red gratuita y de código abierto que permite capturar y examinar el tráfico de red en tiempo real. Con Wireshark, es posible analizar el tráfico de redes cableadas e inalámbricas para solucionar problemas y detectar fallos de seguridad.
- También existen otros tipos de analizadores de protocolos, pero este writeup se centrará en `Wireshark` y en específico mi porpia modificación y perfil llamado `The BlackShark`  <br> <br> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/226084984-53d0035a-6285-4c8c-8849-1d8d0df7343b.png" alt="CWAP" height=90px/> </a>   </p> <br>

## 🏔️ La analogía del `CWAP` y una expedición al `K2` 

**La manera en la que he ajustado mi mente, cuerpo y espíritu para lograr la motivación y disciplina que representa estudiar esta certificación y documentar en este repositorio todos los recursos necesarios para salir adelante con el reto, fue imaginarlo como escalar el `K2` por la ruta `Abruzzi Spur`:**

![image](https://user-images.githubusercontent.com/94720207/224564103-b9889d9f-2bb3-4ba8-aa31-ce31bddfa949.png)

La montaña **`K2`**, también conocida como **`la "Montaña Salvaje"`**, es un coloso de hielo y roca que se eleva majestuoso en la cordillera del Karakórum, en el corazón de los Himalaya. Con una altura de más de 8.600 metros, es la segunda montaña más alta del mundo después del `Monte Everest`. `K2` es una de las cumbres más temibles y es un reto indomable que ha desafiado a los alpinistas más valientes y experimentados. La `Abruzzi Spur` es la vía de ascenso más icónica y desafiante del `K2`, esta ruta atraviesa la cara sureste de la montaña, presentando una serie de desafíos técnicos extremos. <br>

**La `tasa de mortalidad` en las expediciones al `K2` es asombrosamente alta**, y a menudo deja una estela de tragedia y dolor en su camino. Se estima que alrededor del **`25%` de los alpinistas que intentan escalar el `K2` no regresan con vida, es decir, `1 de cada 4` expedicionarios mueren en el intento**. 

Las expediciones que intentan subir al `K2`, **suelen permanecer en la montaña durante varias semanas o incluso meses**. El tiempo que pasan en el campamento base y los campamentos siguientes **depende del plan de escalada específico de la expedición, el clima y las condiciones de la montaña**. Hay años donde simplemente es imposible subir para unos y deben regresar hasta la siguiente temporada. 

Los escaladores que se aventuran en esta ruta ponen sus vidas en juego con cada paso que dan, mientras luchan contra la montaña y contra ellos mismos, poniendo a prueba su coraje, determinación, control mental y altas habilidades técnicas. Los supervivientes de estas expediciones a menudo describen el `K2` como una montaña implacable y cruel, donde los peligros acechan en cada paso.
 
- **Cursar el `CWAP` es como intentar llegar a la cima del `K2` por la `Abruzzi Spur`, no es una certificación para principiantes y aún a los expertos puede representar un gran reto.**

---

### 🟣 `Bottleneck` & `Serarc` = Examen CWAP-404 @ Pearson Veu

El `Bottleneck` es una sección crítica de la `Abruzzi Spur`, esta zona es un corredor estrecho de hielo y roca que se encuentra a una altitud de casi 8.000 metros. Es un lugar donde el aire es escaso y el peligro es constante, lo que la convierte en un desafío extremadamente difícil para los escaladores que intentan llegar a la cima. <br>

Para tener éxito en el `Bottleneck`, se necesita más que solo coraje y determinación. **Se requiere un conocimiento experto en la técnica, un entrenamiento riguroso en las condiciones más extremas y una habilidad sobrehumana para mantener la calma y el enfoque en medio del caos**. Los expedicionarios deben ser capaces de navegar con habilidad en terrenos empinados, sobre hielo y roca, y de escalar con seguridad en condiciones extremadamente peligrosas. Deben estar preparados para enfrentar el clima adverso, la falta de oxígeno y la incertidumbre constante.

En la cima del `Bottleneck` se encuentra su majestuosa `serac`, es ahí donde se pone a prueba todo lo que los escaladores han aprendido y entrenado. La `serac` es un monstruo gigante de hielo, amenazando con hacer trizas a cualquiera que se cruce en su camino. Solo aquellos con la más alta técnica y habilidad pueden escalar con éxito a través de ella. <br>

Se dice que es en el `Bottleneck` es donde tu vida deja de estar en tus manos... <br>

- **El Bottleneck es el Día-D del examen para el `CWAP`, el punto de no retorno. Normalmente suele ser una experiencia no muy cómoda, algo tensa y estresante, pero gratificante al lograr pasar la prueba.**

- [Vista de la serac del Bottleneck desde Camp 4](https://youtu.be/jB3D99ZyB8A)

![image](https://user-images.githubusercontent.com/94720207/225210926-c1e5788f-3f22-42af-994b-350232c730fb.png)

### 🟣 `Cima del K2` = `Certifcación como Ingeniero CWAP-404`

Al superar los todos los obstáculos, solo hay que dar unos pasos más hacia la cima "The Summit Ridge" o simplemente, "el último emuje"... y disfrutar la de vista de los Himalaya, ¡para después seguir con el siguiente reto!

La `ruta Abruzzi del K2` es un camino lleno de peligros y desafíos que ponen a prueba la resistencia física y mental de los alpinistas. Desde el `base camp` hasta la `cima del K2`, la ruta está plagada de peligros mortales. A pesar de esto, aquellos que logran completar la ruta pueden considerarse verdaderos héroes, capaces de enfrentar lo inimaginable y triunfar sobre él. <br> 

**La hazaña de superar la ruta completa del `K2` es una demostración de la fuerza y la determinación humana y un recordatorio de que, con suficiente dedicación y perseverancia, no hay nada que el ser humano no pueda superar.** <br> 

 _"K2, avanzar a morir!"_

---


<!-- 

FIN DE CAPITULO :D

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br><br><br>

