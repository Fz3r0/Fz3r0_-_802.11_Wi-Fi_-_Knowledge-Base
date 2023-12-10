# 👹 `CANTO II`: Protocol Analysis

En primer lugar, quiero destacar que para todo este capítulo y básicamente para todo el curso de `CWAP`, el `Software` que utilizaré como `Sniffer` / `Protocol Analyzer` para ejemplos y laboratorios será `Wireshark`, en específico utilizando mi mod de profile y OUI `Blackshark by Fz3r0`. En la literatura oficial del `CWAP` utilizan ejemplos de otras herramientas como `Omnipeek`, sin embargo, además que es mi herramienta preferida de análisis de paquetes (packets) y tramas (frames), esta herramienta es de código abierto y al alcance de todo mundo de manera gratuita.

[BlackShark v4.0 by Fz3r0]()

![image](https://user-images.githubusercontent.com/94720207/231305756-4bea1b6a-9c73-4333-94e2-0f737cd0980c.png)

Personalmente, considero que antes de cursar un `CWAP` **es fundamental tener un buen background de conocimiento y experiencia en la captura y análisis de tráfico Ethernet 802.3 antes de siquiera intentar adentrarse en el análisis de redes inalámbricas** y entender la tranmsisión y comunicación de protocolos comunes vistos desde una red cableada como `ethII`, `TCP/UDP`, `http/https`, `telnet/ssh`, `ping = ARP + ICMP`, `decodificar imágenes`, `desencriptar tráfico`, etc. Si no se cuenta con estas habilidades, recomiendo revisar cursos de `Wireshark` impartidos por expertos en la materia como `David Bombal` y `Chris Greer`. Ambos son reconocidos en la comunidad de `Wireshark` por su amplia experiencia y conocimiento en la herramienta de análisis de red que además cuentan con numerosos cursos y talleres sobre el tema en linea, varios de esos cursos son gratuitos. 

`Chris Greer` es un experto en redes y análisis de tráfico de red, además de ser el fundador de la empresa Packet Pioneer. Chris ha sido un usuario activo de Wireshark desde sus primeras versiones y es un instructor y orador reconocido a nivel internacional que ha capacitado a miles de profesionales en el uso de Wireshark y técnicas de análisis de tráfico de red. Para mi es el gran gurú y una de mis grandes inspiraciones por las cuales actualmente realizo análsis de tráfico en redes Ethernet y WiFi. Yo lo llamo Chris "The Megalodon" Greer, un experto analista con que nunca se le escapará la presa, el megalodón es el tiburón más grande que ha existido, considerado uno de los depredadores más grandes y poderosos que haya existido en la Tierra.

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/231304586-ab25cfa5-ffa3-4879-bc49-7b968b163dd3.png" alt="encoding" height=200px/> </a> </p> 

`David Bombal` es uno de los expertos en redes más respetados y reconocidos a nivel mundial, y es conocido por sus habilidades en la enseñanza de tecnologías de redes complejas en un lenguaje simple y accesible. Ha enseñado a miles de estudiantes en todo el mundo sobre redes, seguridad y Wireshark a través de sus cursos en línea, y ha publicado varios libros técnicos. También es un instructor de certificación de Cisco Certified Network Associate (CCNA) y un Certified Cisco Systems Instructor (CCSI). Su enfoque en la enseñanza es enriquecedor y práctico, y su conocimiento y experiencia son invaluables para aquellos que buscan aprender sobre tecnologías de redes y Wireshark. Creo que si alguien algún día lee esto... sabrá perfectamente quien en este señor, máximo respeto y fuente de inspiración ¡Vámos Bombal!

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/231305004-3098efac-a6e8-4a97-8f3d-0b29e6a887e3.png" alt="encoding" height=200px/> </a> </p> 

## `Protocol Analysers` & `Sniffers`

Un `protocol analyzer` (analizador de protocolos) y un `sniffer` (olfateador) son herramientas de software que se utilizan para analizar y monitorear el tráfico de red. **Aunque a menudo se usan indistintamente, hay una sutil diferencia entre ellos.**

- **Un `sniffer` se enfoca en capturar y analizar paquetes de red en tiempo real. Mientras que un `protocol analyzer` se centra en analizar el tráfico de red que se ha capturado previamente. Es decir, un `protocol analyzer` se utiliza para analizar y estudiar los paquetes de red que ya han sido capturados y almacenados.**

Existen varias herramientas y posibilidades en el mercado para realizar estas tareas, por ejemplo:

### ⭕ Wireshark

`Wireshark` es una herramienta de software de `código abierto` que se utiliza para analizar el tráfico de red en tiempo real y también para analizar los paquetes de red capturados anteriormente. Es decir, Wireshark es capaz de realizar tanto la función de un sniffer como la de un protocol analyzer. Wireshark es una de las herramientas de análisis de red más populares y ampliamente utilizadas, debido a su facilidad de uso y su capacidad para analizar una amplia variedad de protocolos de red.

Tipo de Licencia: `Código Abierto` :) 

![image](https://user-images.githubusercontent.com/94720207/234611476-e2e9201a-e86d-46d3-bfe1-55809c095372.png)

![image](https://user-images.githubusercontent.com/94720207/234611540-570c0d4a-3738-4564-a90d-c34fbc010756.png)

![image](https://user-images.githubusercontent.com/94720207/234611750-55c8b13f-6fd5-4b98-a913-1880a8040528.png)


### ⭕ Omnipeek

Omnipeek es otra herramienta de análisis de red que es utilizada para monitorear, analizar y solucionar problemas de red. Ofrece una amplia variedad de características, incluyendo la capacidad de analizar el tráfico de red en tiempo real, visualizar la topología de red y realizar análisis detallados de protocolos. Omnipeek también es capaz de analizar una amplia variedad de protocolos de red.

Tipo de Licencia: `$$$$`

![image](https://user-images.githubusercontent.com/94720207/234612267-994a88d8-8591-4336-b848-81d5e296a553.png)

![image](https://user-images.githubusercontent.com/94720207/234612435-9ad31469-3318-409d-85b5-8e517574ba4b.png)

![image](https://user-images.githubusercontent.com/94720207/234612515-46323d26-6629-4e32-8d83-d0d34d6383d7.png)


### ⭕ Acrylic WiFi Analyzer & Acrylic WiFi Capture

Acrylic WiFi Analyzer es una herramienta de software que se enfoca en el análisis de redes inalámbricas, en realidad esta herramienta es una Suite con varios módulos integrados.

Acrylic WiFi Analyzer se utiliza para monitorear y analizar la calidad de la señal, el rendimiento de la red y la seguridad de las redes Wi-Fi, tiene también un módulo de packet capture que permite a los usuarios capturar y analizar paquetes de red inalámbricos en tiempo real. Ambas herramientas son útiles para diagnosticar problemas en redes Wi-Fi.

Tipo de Licencia: `$$$$`

![image](https://user-images.githubusercontent.com/94720207/234612758-b5beb709-51da-4f23-b0c2-891fdbb74b2a.png)

![image](https://user-images.githubusercontent.com/94720207/234613663-1f847780-b1ad-47c6-8d6e-78333157fe8a.png)

![image](https://user-images.githubusercontent.com/94720207/234613950-5ed6b5d4-1f56-4d37-8587-57c24effc599.png)


### ⭕ TCPdump & T-Shark

`Tcpdump` y `TShark` son herramientas de `línea de comandos` para capturar y analizar el tráfico de red. Ambos son parte del conjunto de herramientas `libpcap`, que es una biblioteca utilizada para capturar paquetes de red.

- `Tcpdump` es una herramienta que se utiliza principalmente para capturar y analizar paquetes de red en sistemas Unix y Linux. Es una herramienta de línea de comandos que muestra el contenido de los paquetes capturados en la pantalla, lo que la hace útil para usuarios avanzados y administradores de sistemas que trabajan en una interfaz de línea de comandos.

![image](https://user-images.githubusercontent.com/94720207/234615030-4b670af8-7100-450c-a70e-c2bad253933a.png)


- `TShark`, es la versión de línea de comandos de `Wireshark`. Al igual que Wireshark, TShark puede capturar y analizar paquetes de red en tiempo real o desde un archivo previamente capturado. TShark tiene la capacidad de decodificar y analizar una amplia variedad de protocolos de red, y también puede filtrar y analizar paquetes específicos utilizando una variedad de criterios, como dirección IP de origen y destino, número de puerto, tipo de protocolo y mucho más.

![image](https://user-images.githubusercontent.com/94720207/234615446-f9526c13-63e1-444c-b6e7-9c29534f7dc1.png)

Ambas herramientas son muy útiles para monitorear y analizar el tráfico de red en tiempo real o para analizar capturas de paquetes previamente capturadas. Tcpdump es más adecuado para usuarios avanzados o administradores de sistemas que prefieren trabajar en una interfaz de línea de comandos, mientras que TShark es una buena opción para aquellos que prefieren trabajar con la potencia y versatilidad de Wireshark desde la línea de comandos.

## Biblia de Wireshark y Cheatsheets

![image](https://user-images.githubusercontent.com/94720207/234449297-dd2981e3-6404-43d7-b73c-cad60706ebc8.png)

- [Wireshark Filter Manual Page - Wireshark display filter syntax and reference](https://www.wireshark.org/docs/man-pages/wireshark-filter.html)
- [Wireshark - Where to Start?](https://www.wireshark.org/docs/)
- [Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- https://www.wireshark.org/docs/dfref/w/wlan.html
- https://www.wireshark.org/docs/dfref/w/wlan_radio.html

### Wireshark Sourcecode & About

- https://gitlab.com/wireshark/wireshark/-/tree/master
- [About Wireshark](https://www.wireshark.org/about.html)

## Capturando y Analizando: 802.3 Ethernet VS 802.11 WiFi

Si bien he mencionado que es fundamental tener experiencia en cuanto a la captura y análisis de tráfico Ethernet 802.3 antes de estudiar la captura WiFi, también es fundamental saber que los protocolos inalámbricos 802.11 son significativamente diferentes y más complejos que los protocolos Ethernet 802.3, por ello, requieren herramientas adicionales para diagnósticos y un conjunto de habilidades adicional para implementarlos y comprender cómo se están utilizando. En redes 802.11 WiFi se necesita tener en cuenta diferentes variables y conceptos a considerar al capturar tráfico inalámbrico. Por ejemplo: 

- Que se capturen todfos los tipos de frames 802.11, en lugar de por ejemplo, solo las tramas de management o data.  
- Elegir las herramientas tanto de Hardware como de Software indicados, incluso drivers y sistemas operativos compatibles. 
- Elegir la banda y canal adecuados, utilizando herramientas como el espectro radioeléctrico, logs o herramientas de monitoreo. 
- Sincronizar el reloj del dispositivo de captura para evitar desincronizaciones, 
- Etc...

Sin duda, la captura de frames en redes inalámbricas WiFi es más compleja que en redes cableadas Ethernet debido a la naturaleza inalámbrica y a los desafíos técnicos asociados. Por lo tanto, es fundamental contar con un conjunto de habilidades y herramientas adecuadas para garantizar una captura y análisis preciso de los frames 802.11, y de esto se trata este capítulo ¡Allá vamos!

El `CANTO II` se divide de la siguiente manera:

1. ⭕ `Capturando 802.11 Frames like a Sir!`
2. ⭕ `Configuración de Parámetros en Wireshark`
3. ⭕ `Utilizando Radio-Frecuencias (RF) para comunicarse`
4. ⭕ `Fundamentos de Network Frames`
5. ⭕ `Métodos de Troubleshooting`












## 🟢 `Capturando 802.11 Frames like a Sir!`

Como ya se ha mencionado, las comunicaciones 802.11 Wireless y las 802.3 Ethernet, aunque similares, no son iguales. Por ejemplo, no hay un puerto solo del plano de `management` en un switch al cual conectarse y simplemente capturar cada `frame` que se envía al medio.

El tráfico inalámbrico no se segmenta utilizando un switch como en Ethernet 802.3, pero si se puede segmentar, por ejemplo utilizando una frecuencia diferente, más comúnmente llamada "un canal". En Wireless las transmisiones están en el aire "volando" y no están contenidas dentro de un conjunto de cables, switches y routers. **Este es el claro ejemplo de la diferencia entre una `LAN (Ethernet / IEEE 802.3)` y una `WLAN (WiFi / IEEE 802.11)`**

Para capturar transmisiones inalámbricas o `802.11 Frames`, se debe utilizar software de análisis de protocolo o `Protocol Analyzer` y un adaptador de red inalámbrico o `Network Adapter` que funcione con el software, es decir, `hardware` y `software` capaz de capturar y procesar la captura de 802.11 Frames. 

El `Network Adapter` debe estar en `Monitor Mode`. El modo monitor significa que el adaptador inalámbrico se ha configurado para **capturar el tráfico que está destinado a cualquier dirección MAC y no solo a la suya.** Esto se logra mediante el uso de un `driver` requerido que funciona no solo con el adaptador sino también con su software de análisis de protocolo.

### 🟢 `Monitor Mode` & `Promiscous Mode`

Es importante entender que `Monitor Mode` y `Promiscous Mode` no son los mismos conceptos. Para la captura de `Ethernet` solo necesita activar `Promiscous Mode`, sin embargo, para capturar `WiFi` es más complejo y se necesita utilizar tanto `Monitor Mode` y `Promiscous Mode`.

### ⭕ `Promiscous Mode`

**Este modo se debe tener encendido siempre que se quiera capturar frames, ya sea `Ethernet` o `WiFi`** _(De hecho los sniffers como Wireshark lo tienen activado por default)_. Es un modo en el que un adaptador de red `inalámbrico` o `cableado` se configura para capturar todos los paquetes que se envían en la red, **independientemente de si están destinados al adaptador o no.** Esto significa que, **en el `Promiscuous Mode`, se pueden capturar paquetes que no están destinados a nuestro dispositivo**, lo que es útil para el análisis de red. 

El `Promiscuous Mode` permite a una interfaz o adaptador de red **"escuchar"** todo el tráfico que pasa por una interfaz _(puede ser Ethernet o una antena WiFi)_, aunque no esté dirigido específicamente a ese dispositivo o aunque no se pertenezca a esa subnet o VLAN, mientras haya tráfico pasando por esa interfaz se podrá escuchar. 

- **`IMPORTANTE`**: NO se puede usar el modo promiscuo para capturar `tráfico unicast` entre dos dispositivos que no son el dispositivo en modo promiscuo, ya que ese determinado tráfico no se transmite directamente por la interfaz donde se está escuchando, sino que en otras 2 interfaces aparte que están transmitiendo unicast ya sea por medio de un switch o directamente peer-to-peer (punto a punto), ya que es la "conversación" unicast entre 2 dispositivos ajenos.**

Existen diferencias de `Modo` entre capturar en WiFi o Ethernet:

- Para capturar `Ethernet 802.3` solo es necesario conectar el cable ethernet a la interfaz, encender `Promiscous Mode` y ya se podrá capturar tráfico ¡Así de fácil!
- Para capturar `WiFi 802.11` es un poco más complejo, ya que además de tener activado el `Promiscous Mode`, se necesitan herramientras de hardware adicional, también se deben confgurar los drivers para una función diferente, como el `Monitor Mode`. Tanto el Sistema Operativo, Hardware _(adaptadores WiFi)_ y Software _(Protocol Analyzers & Sniffers)_ deben ser compatibles con `Monitor Mode`

### ⭕ `Monitor Mode`

Es un modo especial en el que un adaptador de red inalámbrico se configura para capturar todo el tráfico de la red inalámbrica, incluyendo los paquetes dirigidos a direcciones MAC que no sean la del adaptador en sí _(Similar al concepto del `Promiscous Mode` pero en Wireless, ¡pero el `Promiscous Mode` sigue siendo requerido!)_

En otras palabras, en Monitor Mode, el adaptador de red inalámbrico captura todos los paquetes que se envían en la red inalámbrica, independientemente de si están destinados al adaptador o no. **Esto permite capturar paquetes que no están destinados a nuestro dispositivo, lo que es útil para analizar todo el tráfico de la red inalámbrica, incluyendo el tráfico que no está dirigido directamente a nuestro dispositivo.**

Es decir, si queremos capturar todos los frames que se envían en una red inalámbrica, necesitamos usar un adaptador de red inalámbrico WiFi 802.11 en Monitor Mode. Por otro lado, si queremos capturar todos los paquetes que se envían en una red cableada Ethernet 802.3, podemos usar un adaptador de red cableado en Promiscuous Mode. Sin embargo, si queremos capturar todos los paquetes que se envían en una red mixta inalámbrica y cableada, necesitaríamos usar tanto un adaptador de red inalámbrico en Monitor Mode como un adaptador de red cableado en Promiscuous Mode para asegurarnos de capturar todos los paquetes.

Hay que recordar que, el tráfico WiFi en el aire puede ser capturado por cualquiera que esté a su alcance y tenga las herramientas adecuadas _(por ello la importancia de la encriptación y otros procesos de seguridad)_

![image](https://user-images.githubusercontent.com/94720207/231614242-d43e9592-73e2-4a22-9417-b8d8e630fdd6.png)

Por ejemplo en Apple MAC-OS es posible poner wireshark en `Monitor Mode` sin necesidad de un adaptador USB adicional y otros drivers como ocurre con Windows. En Linux depende del adaptador, distro, drivers, updates, y muchas variables. 

![image](https://blog.packet-foo.com/wp-content/uploads/2019/04/WiresharkMonitorModeCheckboxWorks.gif)


![image](https://user-images.githubusercontent.com/94720207/231615038-3a046e6c-d072-454d-b200-5a265c54ac12.png)


## Opciones para capturar frames 802.11

Básicamente los dispositivos o posibilidades para capturar frames 802.11 WiFi se dividen en 3 _(aunque también existen soluciones más híbridas y modulares que uno puede modificar a placer)_

1. `Mobile`
2. `Infrastructure`
3. `Distributed`

### Captura de tráfico Wi-Fi móvil 

Esta opción implica el uso de dispositivos móviles, como laptops con Linux y adaptadores USB Wi-Fi, como el popular adaptador Alfa. Estos dispositivos se pueden utilizar para capturar tráfico Wi-Fi mientras se desplazan por una red inalámbrica. La captura de tráfico móvil es flexible y portátil, lo que permite la captura de tráfico en diferentes ubicaciones de la red inalámbrica. Además, no se requiere una inversión significativa en hardware especializado, ya que muchos dispositivos móviles están equipados con adaptadores Wi-Fi integrados. 

Sin embargo, la captura de tráfico móvil puede ser limitada en términos de alcance y capacidad, ya que los no todos los disposiitvos móviles no están diseñados específicamente para esta tarea, lleva mucho tiempo de preparación y configuración, también en ocasiones hay que pelear con drivers y demás obstáculos...

![image](https://user-images.githubusercontent.com/94720207/233807666-0ebb4985-ecf7-418a-84f4-a567cdee458c.png)

Lograr dominar por completo esta alternativa es bastante gratificante y lleva a aprender mucho del tema, incluso para comenzar a desarrollar nuestras propias antenas WiFi o Sniffers, por ejemplo para proyectos de Raspberri Pi de APs, Sniffers WiFi o hasta herramientas de penetración como deautenticadores. En este write-up se utiliza mucho este enfoque para los laboratorios y ejemplos. 

![image](https://user-images.githubusercontent.com/94720207/233803737-3c33f13c-1bc0-42c9-a793-8501b28e5d37.png)

También existen soluciones pre-fabricadas, DIY u otras basadas en dispositivos como Raspberry PI como el `WLAN PI`

![image](https://user-images.githubusercontent.com/94720207/236651136-2ecf1dfb-d49d-40bd-b56e-640e4df4bbaf.png)

Este tipo de soluciones también se pueden reproducir de manera casera:

![image](https://user-images.githubusercontent.com/94720207/236651111-5e8c934b-4a6a-4a0c-b313-5e46bd5fd098.png)

### Accesibilidad de captura mobil:

Esta es la mas accesible, aunque también se puede hacer bastante costosa dependiendo del alcance. Es decir, se puede invertir en una siple RaspBerry, una antena USB que soporte modo monitor y listo, por unos cientos de dólares ya se tiene el dispositivo listo para capturar frames 802.11 y exportarlos en .pcap. Sin embargo, también se pueden hacer proyectos complejos y utilizar computadoras de gama alta para lograr complejos sistemas de captura o incluso hacking. ¡Sky is the limit!

### Captura de tráfico Wi-Fi mediante infraestructura 

Esta opción implica el uso de dispositivos de red inalámbrica profesional, por ejemplo infraestructura como `Ruckus Networks` o `Ubiquiti` permiten la captura de tráfico desde sus `Access Points` al mismo tiempo que funcionan para distribuir la red inalámbrica a sus clientes. En este Writeup utilizaré casi siempre ejemplos de `Access Points Ruckus` y la plataforma de `Wireless Controller SmartZone` ya que son los dispoiticos que tengo experiencia y la fortuna de tener acceso a ellos gracias a mi trabajo y fueron de mucha ayuda para capturar tráfico 802.11, por ejemplo, para capturar eventos de roaming en diferentes canales ya que se puede capturar en varios APs al mismo tiempo, aunque estén en diferentes canales. 

![image](https://user-images.githubusercontent.com/94720207/233806039-c4baf586-8984-494e-a563-e682c4d64165.png)

![image](https://user-images.githubusercontent.com/94720207/233806071-77f2b6ac-fe0b-4cc5-8406-6f87ada30c97.png)

![image](https://user-images.githubusercontent.com/94720207/233806077-c995b5d2-a51c-4c96-bed1-e7e32b3bb70f.png)

![image](https://user-images.githubusercontent.com/94720207/233805815-91b28a53-e0ce-459e-bcb0-0af56964fdc7.png)

![image](https://user-images.githubusercontent.com/94720207/233805834-e5559fa7-19f5-4c15-ae77-b6aa08e51393.png)

Estos dispositivos están diseñados para ofrecer conectividad Wi-Fi a los usuarios, pero también pueden recopilar información sobre la actividad de la red inalámbrica y los dispositivos conectados. Además, se pueden configurar para permitir la captura de tráfico de manera centralizada, lo que facilita la gestión y el análisis de la información. Algunas de las ventajas de la captura de tráfico Wi-Fi mediante infraestructura son su escalabilidad, ya que se pueden agregar más dispositivos de red inalámbrica según sea necesario, y su eficiencia, ya que los dispositivos de red inalámbrica están diseñados específicamente para esta tarea. 

![image](https://user-images.githubusercontent.com/94720207/233806582-ec4d01aa-4b5c-452b-812d-9c4aec2c356d.png)

![image](https://user-images.githubusercontent.com/94720207/233806228-1f59d894-d5a6-4a24-ac49-ad5c126a862c.png)

![image](https://user-images.githubusercontent.com/94720207/233806496-4e20d835-5a2b-426d-a975-9a9be8db1b4d.png)

Ruckus permite tanto la captura remota donde se guarda un .pcap de máximo 20mb en la memoria del AP para posterioprmente ser descargada, como poder hacer un stream en tiempo real haciendo una conexión remota entre AP y Wireshark, haciendo de esta capacidad algo increíblemente útil para el troubleshooting de la red tanto 802.11 como 802.3 ya que también, permite capturar desde la interfaz Ethernet. 

Como dato adicional, la captura desde APs pueden soportar el PHY que soporte el AP, por ejemplo, en caso que sea un AP de gama alta se podría capturar 3x3 streams de WiFi6 802.11ax en escenarios de roaming, algo muy complicado con móvil. 

### Accesibilidad de Captura mediante Infraestructura

La captura de tráfico mediante infraestructura puede ser costosa, ya que se requiere la inversión en dispositivos de red inalámbrica especializados. Sin embargo, soluciones como APs ubiquiti stand alone o Ruckus unleashed podría funcionar para capturar a manera de infraestructura. 


### Captura de tráfico Wi-Fi distribuido: 

Esta opción implica el uso de sensores especializados como los denominados `Muli-Sensor Wireless Overlay System`, los cuales pueden capturar en diferentes canales al mismo tiempo gracias al uso de múltiples interfaces (radios), siempre que se implemente y configure correctamente. 

Estos sensores se pueden colocar en varios puntos de la red inalámbrica para capturar tráfico de manera distribuida y permitir un análisis detallado de la actividad de la red inalámbrica. La captura de tráfico distribuido permite la captura de tráfico en diferentes ubicaciones de la red inalámbrica y permite un análisis detallado de la actividad de la red inalámbrica. 

Por ejemplo, en el libro del `CWAP`muestran el [`Savvius Omnipliance Ultra`](https://www.ctctechnologies.com/catalog/savvius-omnipliance-ultra/)

![image](https://user-images.githubusercontent.com/94720207/233794545-45b4d5dc-3d94-4067-a948-d6c115e29c4e.png)

![image](https://user-images.githubusercontent.com/94720207/233805689-00d95c85-5868-45c1-86ae-fecbd52b27dd.png)

![image](https://user-images.githubusercontent.com/94720207/233794294-0ded40af-45ec-4f95-a541-5a2608d22e34.png)

`Omnipliance Ultra` combina `Savvius Spotlight` para monitoreo de red con el analizador `Savvius Omnipliance` _(Es un protocol Analyzer similar a `Wireshark`)_ para captura y análisis de datos de paquetes. Omnipliance Ultra captura datos de paquetes de red y realiza monitoreo en tiempo real de hasta 20 Gbps con hasta 128 TB de almacenamiento.

_"Omnipliance Ultra es la solución de monitoreo y análisis de rendimiento de una sola caja más poderosa y completa disponible. Con Omnipliance Ultra, todo lo que necesita para reducir el tiempo medio de resolución (MTTR) de problemas de red está incluido."_

![image](https://user-images.githubusercontent.com/94720207/233809521-ee135227-50aa-43ff-9dd3-5c7e172195ac.png)


![image](https://user-images.githubusercontent.com/94720207/233809155-2752609e-8321-4185-8e0b-5baba56255e6.png)


### **`Accesibilidad y Costo`: 

La configuración y gestión de los sensores especializados pueden ser más complejas y costosas que cualquier otra opción, como las capturas de tráfico mediante infraestructura o móvil.**

---

### Software: Omnipeek VS Wireshark

https://www.youtube.com/watch?v=U_zzdl7xV7I





















## 🟢 Instalacion de Drivers para Modo Monitor

Para el análisis de protocolo y la catpura de 802.11 WiFi Frames se comienza determinando cuáles serán las herramientas tanto de Hardware y Software que se utilizarán. Existen muchas opciones como ya se ha visto, pero caalquiera sea la combinación siempre de basa en 3 cosas:

1. ⭕ El `Sistema Operativo` que se está utilizando
2. ⭕ El `Software` requerido: `Protocol Analyzer` & `Drivers`
3. ⭕ El `Hardware` requerido: Adaptadores, Antenas, Computadora, Access Points, WLC, etc

En el análisis de protocolos, existen herramientas que solo son compatibles con ciertos sistemas operativos, como `Windows`, `Linux` y `Mac OS`. Existen `Protocol Analyzers` que solo funcionan en `Windos`, pero no en `Linux` o `MacOS`, y viceversa. En caso de `Infraestructure` o `Distributed` pueden incluso a utilizar sus propios Sistemas Operativos, muchos de ellos basados en `Unix`.

- **Un dato importante es que `Mac OS` tiene la ventaja de permitir la captura nativa de `802.11 Frames` sin la necesidad de `Drivers` adicionales.**

La elección del `hardware`, `software`, `drivers` y `sistema operativo` **dependerá del presupuesto y de las necesidades específicas en ese momento**. Al utilizar software y hardware con **licencia**, es necesario seguir los pasos de cada proveedor para obtener la licencia y utilizar la tecnología. Algunos software solo admiten versiones antiguas de Java, mientras que otros solo tienen soporte web y pueden variar en su compatibilidad con diferentes navegadores.

En caso de utilizar captura por método `infraestructure` o `distributed` hay que tomar en cuenta que los APs o infraestructura involucrada soporte la captura de frames 802.11, además que todo tenga su firmware correcto para su funcionamiento. En caso de `Ruckus Commscope` que es el utilizado en este `Writeup` es compatible tanto en implementación centralizada con `WLC SmartZone` como independiente con `Ruckus Unleashed`.

Es importante tener en cuenta cada uno de estos puntos al elegir la combinación adecuada de hardware, drivers, software y sistema operativo para garantizar la compatibilidad y el funcionamiento adecuado según las necesidades y según el método de captura deseado. 

---

### ⭕ El `Sistema Operativo` que se está utilizando

Es importante seleccionar herramientas de software que sean compatibles con el sistema operativo utilizado para la captura de tráfico de red inalámbrica, como Windows, Linux o macOS.

- `Microsoft Windows`: Es muy limitado para la captura de tráfico 802.11, existen herramientas que facilitan mucho la captura en Windows, pero normalmente son costosas. 
- `Apple Mac OS`: Una gran ventaja de Mac OS es que puede capturar tráfico y ponerse en modo monitor de fábrica sin realizar ninguna configuración adicional.
- `Linux`: Linux se tienen muchísimas herramientas y opciones para analizar, capturar e inyectar tráfico 802.11. Pero en ocasiones las configuraciones requeridas no son tán simples como podría serlo en Windows o Mac OS. 
- `Raspberry PI`: Otra gran opción muy similar a Linux, pero un poco más complejo aún por la necesidad de aún mas equipo. 
- `Android`: Personalmente no recomiendo capturar tráfico con las pocas herramientas que existen en Android ya que no están a la altura de sus contra partes mencionadas anteriormente. 
- `Sistemas Operativos de Propietario`: Si se están usando sistemas de captura de `infraestructura` o `distribuido` es muy probable que utilicemos directamente los Sistemas Operativos del fabricante, por ejemplo, en caso de Ruckus Smartzone estaríamos usando la UI basada en web, mientras que el sistema operativo y las entrañas de SmartZone trabajan con bases de Unix, cosa que no importa realmente mucho, ya que en este tipo de soluciones es muy fácil trabajar con sus drivers ya que son sistemas licenciados y con soporte. 

**En este documento procuro utilizar ejemplos de `mobile` tanto de Windows, Linux y Mac OS ya que tengo acceso a los 3. Sin embargo, para las prácticas y laboratorios de instalación de drivers utilizaré especificamente Linux Parrot Security basado en Debian. Además, también utilizo `infraestructure` de Ruckus Smartzone. Durante mis estudios no tuve acceso a un sistemas `distributed` como sensores dedicados a la captura.**

---

### ⭕ El software de análisis de protocolo y los drivers para la interfaz WiFi 

Ya hubo anteriormente una sección enfocada directamente a los `protocol analyzers` y `sniffers`, es importante elegir el que sea compatible tanto con los adaptadores WiFi como con los drivers que vayamos a utilizar, ya que esto asegura que la herramienta de captura pueda aprovechar al máximo la capacidad del adaptador WiFi y el driver para capturar todos los paquetes de red necesarios para el análisis profesional.

Una herramienta de captura que no sea compatible con el adaptador WiFi o el driver podría perder paquetes importantes durante la captura, lo que puede afectar la calidad y la integridad de los datos capturados. Además, la herramienta de captura puede tener dificultades para decodificar correctamente los paquetes capturados si no es compatible con los formatos y protocolos específicos utilizados por el adaptador y el driver.

**El driver del adaptador puede influir en la cantidad de tipos de frames que se pueden capturar durante una captura 802.11.** Por ejemplo, algunos drivers pueden estar diseñados para capturar solo paquetes de datos, mientras que otros pueden capturar paquetes de control y gestión, lo que permite una captura más completa de la red inalámbrica.

---

### ⭕ El hardware requerido 

El hardware necesario puede variar dependiendo del tipo de análisis y captura que se desee realizar, pero puede incluir dispositivos como puntos de acceso inalámbricos (AP), sistemas distribuidos, antenas USB, tarjetas de red inalámbricas, y computadoras con capacidad de procesamiento y almacenamiento suficiente para manejar grandes cantidades de datos capturados.

En la documentación del CWAP solo dan un ejemplo de instalación de Drivers en Omnipeek apliance, que honestamente es solo darle Next y funciona en un Windows común y corriente, recordemos que Omnipeek no es una herramienta al alcance de cualquiera, estas facilidades y automatización cuestan en la cartera...

En mi experiencia personal, he probado con diferentes antenas que venden en mercados como Amazon y son las que usan en foros de Internet, sin embargo, varias tienen algunos trucos para hacerlas funcionar y en ocasiones esto puede generar un dolor de cabeza. Aconsejo este par de videos de David Bombal para entender más a fondo estas problemáticas: 


Para llevar el aprendizaje más allá compartiré 2 laboratorios que hice con diferentes antenas la primera con Panda Wireless y la segunda con Alfa

















## 🟢 Laboratorio  de Drivers Fz3r0

Este laboratiorio lo hice solo para entender por completo y vivir la experiencia del dolor de cabeza que suelen ser los drivers en caso de querer construir un sniffer a la medida del tipo `Mobile`, por ejemplo con un sistema Linux o RaspBerry Pi, también los comparo con otros métodos de captura donde no tuve que instalar ningún driver por ejemplo con otros sistemas `Mobile` como Mac OS, o sistemas de infraestructura como `Ruckus Commscope`. 

_Durante mis estudios no tuve acceso a sistemas `Distributed` como sensores dedicados de `Omnipeek`, sin embargo, siendo que son sistemas de gama alta y licenciados, tienen soporte directo con el proveedor por lo cual la instalación de drivers no representa un reto complejo y pueden ser utilizados en cualquier sistema Windows con una instalación sencilla._ 

### Hardware utilizado

### PC1 - Windows 11

### PC2 - Windows 11

### PC3 - Macbook Pro

### VM1 - Parrot-Sec Custom (Debian)

### VM2 - Kali Linux (Debian)

### Antenas

[captura de 3 rfaw](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11339142/Fz3r0_airPwn_3_war.zip)

---

### Adaptadores WiFi recomendados para capturar 802.11 Frames en 2023

Después de las pruebas relaizadas en el laboratorio y con la documentación reciente encontrada en linea, realicé esta tabla donde están las antenas más recomendadas para capturar sin tanto problema. Toda esta información se basa en mi experiencia en el laboratorio anterior y conforme experiencia de otros usuarios en la red, aunque me limitaré a recomendar solo unas cuantas antenas. 

- **El driver es más importante que la antena o la marca**

Tal cual dijo David Bombal y me pude dar cuenta comprando antenas chinas baratas... es que lo importante es fijarse en el driver, el driver combinado con el sistemas operativo es lo que logrará la mejor captura posible. Actualmente, he notado que el driver Atheros ha sido infalible, tal cual se ha mencionado en la red... Pero también es cierto que existen drivers nuevos como el `alfa` que es soportado para capturar incluso WiFi6. 

- https://github.com/morrownr/USB-WiFi/issues/87 drivers para wifi6



| **Adaptador**              | **Tipo**            | **Driver**      | **Bandas**    | **MIMO**        | **Ventajas**                                                                                                                                                                     | **Desventajas**                                                                                                  | **Calificación** |
|----------------------------|---------------------|-----------------|---------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------|
|                            | Sistema Distribuido |                 |               |                 | Top Notch & Price $$$                                                                                                                                                            | Top Notch & Price $$$                                                                                            | **10 ???**       |
| **Ruckus APs & SmartZone** | Infraestructura     | Ruckus Internal | 2.4, 5, 6 GHz | AP capabilities | - Fácil de capturar<br>- Acceso Remoto exacto al sitio de captura<br>- Fácil captura de roaming y eventos<br>- Captura tanto WLAN como LAN<br>- Capacidad de stream en Wireshark | - No accesible para cualquiera<br>- Usa infraestructura en producción <br>- Necesita última versión de SmartZone | **9.5**          |
| **WLAN Pi**                | Mobile              |                 |               |                 | - Más barato que comprar APs<br>- Utilizable para mil usos diferentes<br>- Cambio de antenas a placer                                                                            | - No siempre disponible<br>- Necesita Raspberry Pi                                                               | **9 ???**        |
| **Macbook Pro**            | Mobile              |                 |               |                 | - Modo monitor de fábrica<br>- Muy fácil capturar con su adaptador built-in                                                                                                      | - Es cara la plataforma Apple<br>- Para capturar roaming se necesitarían 2 Macbook o más                         | **8.5**          |
| **Panda AU06**             | Mobile              |                 |               |                 |                                                                                                                                                                                  | - No captura FCS (Frame Check Sequence)<br>- Solo trabaja en banda 2.4 GHz                                       | **8**            |
| **Alfa 1900**              | Mobile              |                 |               |                 | - Captura en 5ghz<br>- Largo alcance                                                                                                                                             | - No captura Control Frames<br>- Driver incompatible con nuevos updates Linux<br>- Muy costosa para lo que hace  | **4**            |
| **TP-Link V2**             | Mobile              |                 |               |                 |                                                                                                                                                                                  | - No captura varios tipos de Frames                                                                              | **4**            |
| **TP-Link V1**             | Mobile              |                 |               |                 | Plug & Play Compatible                                                                                                                                                           | Ya no la venden                                                                                                  | **???**          |
|                            |                     |                 |               |                 |                                                                                                                                                                                  |                                                                                                                  |                  |



### Linux Parrot Security Specs

![image](https://user-images.githubusercontent.com/94720207/233811214-ddc89822-2263-468f-b714-c75fa1f63840.png)


### Panda

![image](https://user-images.githubusercontent.com/94720207/233815231-a89c72ba-610e-4910-81a3-d9e6bf50c2d0.png)

![image](https://user-images.githubusercontent.com/94720207/233815326-1b0f4699-03f0-4ae0-87aa-4a7531b9125f.png)



1. Primero lanzaré lo siguientes comandos para revisar mis configuraciones actuales:

![image](https://user-images.githubusercontent.com/94720207/233811007-3357c207-d1d8-4846-9845-e51889099799.png)

2. Ahora solo conecto el usb y selecciono enviar a la VM de Parrot la interfaz recién conectada:

![image](https://user-images.githubusercontent.com/94720207/233811281-ec0a37bf-b2c1-4836-8b8a-4dc882647916.png)

3. Si vuelvo a revisar mis configuraciones y dispositivos ya veré la Panda detectada:

![image](https://user-images.githubusercontent.com/94720207/233811418-bbf73b8b-84d3-430d-b8b2-8238cad4471b.png)

4. Ahora solo la debo poner en modo `Monitor`:

![image](https://user-images.githubusercontent.com/94720207/233811882-c3b08fcf-375c-4070-89c6-f74c862d453f.png)

5. Ahora puedo incluso auditar la red WiFi, como se ha visto en certificaciones de Seguridad Ofensiva y Hacking Ético como el CWSP

![image](https://user-images.githubusercontent.com/94720207/233812126-d04de7c7-d211-4208-b6c8-b331833c54b2.png)

Bonus: Cambiar de canal

![image](https://user-images.githubusercontent.com/94720207/233812022-9c62ae8e-a828-4d50-9a24-15433774fa36.png)

- En este punto ya puedo capturar, auditar y hacer análisis Wireless, por ejemplo aquí hay una captura de todo un proceso de handshake hecho para mi laboratorio de [`Ataque con frames CTS`](https://github.com/Fz3r0/WiFi-CTS-Frame-Attack-802.11-Frame):

![image](https://user-images.githubusercontent.com/94720207/233812248-b84bcc3b-3e17-4e12-a63a-fd180a2b016c.png)

### Desventajas de Panda

Existen 2 grandes desventajas que he encontrado de esta tarjeta, que a pesar de sus facilidades de "plug-and-play", carecen de 2 cosas:

1. `No Captura FCS` - Los `FCS` o `Frame Check Sequence` son importantes en la captura de WiFi, además de para la certificación `CWAP`, si bien ayuda muchísimo a la captura de frames 802.11, le falta este gran detalle. 
2. `No captura 5 GHz` - Esta inetrface solo es compatible con la banda 2.4 GHz, exsite la versión para ambas bandas! pero tiene el mismo problema del FCS :(

![image](https://user-images.githubusercontent.com/94720207/233812366-5d05e17b-5b21-41c8-8de4-576047742794.png)

---

### Alfa


https://miloserdov.org/?p=5493

Realizaré el paso a paso de la instalación de estos drivers para dar un ejemplo real, elegí esta antena ya que si bien es de las mejores actualmente para capturar tráfico 2.4ghz como 5ghz, también es de las más complicadas para hacerlas funcionar debido a problemas con nuevos drivers y headers de Linux. 

Personalmente esta antena me generó muchos problemas al principio, a pesar que es parrot pareciera que funciona plug and play como pasa con la Panda

![image](https://user-images.githubusercontent.com/94720207/233812880-07b5fbf1-158d-445e-b8bb-a4b61980df9d.png)

2. Ahora la conecto y la reconoce plug and play muy similar a la Panda

    - OJO!!! Esto solo lo hace con Parrot, por ejemplo en Kali Linux u otra distro en ocasiones no se muestra nada y hay que instalar el driver desde 0, de todos modos es lo que se temrinará haciendo en este caso también.  

![image](https://user-images.githubusercontent.com/94720207/233812955-2e1fa96f-3b70-438e-9033-88f406cfc446.png)

3. También la puedo poner en modo monitor y hasta aquí pareciera que todo va bien!!!

![image](https://user-images.githubusercontent.com/94720207/233813077-44a38f21-1ff0-4dde-8406-8f96d91fe3c5.png)

- Incluso puedo auditar la red:

![image](https://user-images.githubusercontent.com/94720207/233814176-308fba70-0f4c-4f59-ae99-494c2ce4656a.png)

Ahora viene el verdadero problema, muchos no se dan cuenta que en realidad hasta este momento aún no funciona correctamente esta tarjeta... Falta una cosa muy importante:

- **IMPORTANTE: ¡En este momento no se pueden capturar `Control Frames`, donde si incluyen por ejemplo los `ACKs`!**

Mucha gente en la red no se da cuenta de este gran problema ya que solo la utilizan para laboratorios básicos de Cyber-Seguridad como hacer ataques de De-Autenticación _(Para esto no se necesitan control frames)_ , pero si se revisan las capturas nunca se encontrarán Control Frames, lo mismo pasa lanzando un ataque de de autenticación, que aunque funciona, nunca se reciben ACKs como se muestra en esta pantalla:

![image](https://user-images.githubusercontent.com/94720207/233814350-06ad8742-a514-4b64-9108-0375acde8c66.png)

Esto se puede hacer mas claro si se captura el ataque de deautenticación, donde en wireshark al tratar de filtrar ya sea Control Frames o ACK Frames no se encuentra nada, así me di cuenta que no se pueden capturar 802.11 Control Frames con el driver que funciona "plug-and-play" en Parrot, ni que decir otras distros de Linux que no sirve al conectar. 

En este ejemplo no utilizo ningñun filtro y veo en su mayoría solo Beacons (Management Frames). [_La captura se puede descargar de aquí_](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11302660/fz3r0_CWAP_alfa.zip)

![image](https://user-images.githubusercontent.com/94720207/233814691-8d8f07b4-5791-46b4-b4f5-591cbf81694c.png)

Si trato de filtrar por Control Frames (Donde se incluyen los ACKs) no se verá nada:

![image](https://user-images.githubusercontent.com/94720207/233815430-32db336a-9ecd-4909-a35b-d58e42bb53e7.png)

Es por eso que la instalación de Drivers quie funcionen bien en Alfa es algo cansado, sin embargo, logré hacerlo funcionar y documenté el proceso:

### Instalación Alfa RTL8814AU chipset (Alfa AWUS1900) <br> _(funcionando 2023 Real no Fake papu Pro)_

Debido a los problemas que trae esta interfaz para funcionar bien y la falta de documentación online, tomé como reto para entender bien este bloque de dirvers lograr instalar y hacer funcionar bien esta antena, ya que es bastante buena, de las mas recientes y se pude capturar 802.11n/ac (2.4 GHz & 5 GHz). 

- **Un agradecimiento al equipo de [miloserdov.com](https://miloserdov.org/) que fue el único que realmente logró hacer funcionar esta tarjeta de manera correcta, además que es un increíble portal con muchos laboratorios y documentación en cuanto a hacking y pentesting.**

Existen online otros tutoriales e isntrucciones que no sirven al 100%, la misma historia pasa con otras tarjetas ¿Ahora te das cuenta de la problemática de los drivers en la vida real? Constantemente se actualizan los sistemas y las tarjetas y hay que estar al día en ello así que como laboratorio decidí hacer funcionar estos drivers e interface con mi sistema operativo Linux Custom y adaptaré este tutorial a mi experiencia, ya que les aseguro se enocntrarán documentación que no funcionará en la red y todas estas problemáticas las resume el libro de CWAP como: _"La instalación de drivers en modo Monitor que sean compatbles con el sistema es escencial"_ , hay que recordar que en el libro de usan generalmente herramientas como Omnipeek y no herramientas para simples mortales y tampoco se adentran en este tipo de instalaciones y configuraciones. 

Anteriormente, el controlador `realtek-rtl88xxau-dkms` tenía soporte para el chipset `RTL8814AU` y para que estas tarjetas inalámbricas funcionaran, era suficiente instalar el controlador especificado. En `Kali Linux` o `Parrot Security`, esto se podía hacer directamente desde el repositorio predeterminado, en otras distribuciones era necesario compilarlo. 

- **¡Pero ahora el soporte para el chipset `RTL8814AU` se ha deshabilitado en el controlador `realtek-rtl88xxau-dkms`!** 

Se ha creado un controlador separado para este chipset, que puede entrar en conflicto con el `RTL8814AU`. Estos cambios son recientes, por lo que **las instrucciones antiguas para instalar el controlador para la Alfa AWUS1900 no funcionan.**

![image](https://user-images.githubusercontent.com/94720207/233818107-361f5495-26d3-4fe8-8d20-90f527bb1baa.png)

A continuación explico el proceso de instalación que me funcióno a mediados del 2023:

### Proceso de instalación:

1. Este es el Status antes de empezar:

![image](https://user-images.githubusercontent.com/94720207/233817491-55369a91-6ed9-40ad-a224-d638286980a2.png)

2. Reviso que todo esté full update y upgrade: 

![image](https://user-images.githubusercontent.com/94720207/233817553-66f47236-db9a-400a-adea-5ea3a1b70387.png)

3. Si no se necesita el controlador realtek-rtl88xxau-dkms que ahora soporta los chipsets RTL8812AU/21AU de otras tarjetas Alfa, entonces hay que desinstalarlo, de lo contrario podría generar conflictos. Personalmente recomiendo borrarlo y en caso de tener otras tarjetas guardar 2 states diferentes de la Máquina Virtual. 

````sh
sudo apt remove realtek-rtl88xxau-dkms
````

![image](https://user-images.githubusercontent.com/94720207/233818385-b4784f90-c419-41c1-ad0d-4037409a7af7.png)

4. Descargar el Driver:

    - IMPORTANTE: Este paso es crítico ya que los Drivers oficiales dan error, pero funcionan los de el siguiente repositiorio:

````sh
git clone https://github.com/morrownr/8814au && cd 8814au 
````

![image](https://user-images.githubusercontent.com/94720207/233818938-56c1baac-73e0-43d4-b3f6-acedfabf526c.png)

5. Instale el controlador como un módulo DKMS, lo que significa que al actualizar el kernel, no es necesario volver a compilar manualmente el controlador para la nueva versión del kernel. Esto se hará automáticamente por el módulo DKMS. Además, tenga en cuenta que el comando make es innecesario ya que la compilación es realizada por el módulo DKMS.

````sh
sudo ./install-driver.sh
````

![image](https://user-images.githubusercontent.com/94720207/233818971-42fbd8b3-6ee4-4332-87bc-79d74ae587eb.png)

- En algún momento solicitará el reinicio _Es opcionar cambiar el archivo de configuración_

![image](https://user-images.githubusercontent.com/94720207/233819004-feafccee-ed6e-449e-b324-3a9ae10181fd.png)

6. Este es el status al terminar y haber reiniciado, se ve exactamente igual que antes en realidad...

![image](https://user-images.githubusercontent.com/94720207/233819132-fd6c64c3-5b22-4202-a484-743d81bfef23.png)



Ahora si, viene la prueba de fuego y revisar si puedo capturar Control Frames, pero para eso hice también una guía detallada de como utilizar la Alpha 1900 en 2023

![image](https://user-images.githubusercontent.com/94720207/233819441-9d9df029-89b3-445a-aa17-e853a5d2dc5e.png)

Mismo problema

![image](https://user-images.githubusercontent.com/94720207/233819481-c9f346c9-7145-4217-a601-9971cdd352c3.png)

Eso es porque por el momento tampoco esta´soportada la suite de Aircrack para este driver, es necesario adaptarse a los comando `ip` e `iw` 

### Cómo utilizar la Alfa 1900 en 2023

Nuevamente comparto este excelente portal donde viene una cheatsheet increíble de cómo utilizar esta tarjeta en Kali Linux, que se adapta a mi parrot

- [Linux Wi-Fi Cheat Sheet: Tips and Troubleshooting](https://miloserdov.org/?p=4819)


How to set Alfa AWUS1900 into monitor mode
The main thing to learn by now is to use the “ip” and “iw” commands instead of “ifconfig” and “iwconfig” – this applies to all Wi-Fi adapters.

For details, see the article: Linux Wi-Fi Cheat Sheet: Tips and Troubleshooting.

USB2.0/3.0 mode switch
Initial it will use USB2.0 mode which will limit 5G 11ac throughput (USB2.0 bandwidth only 480Mbps => throughput around 240Mbps). When modprobe add following options will let it switch to USB3.0 mode at initial driver:

1
options 8814au rtw_switch_usb_mode=1
Switch usb2.0 => usb3.0

1
sudo sh -c "echo '1' > /sys/module/8814au/parameters/rtw_switch_usb_mode"
Switch usb3.0 => usb2.0

1
sudo sh -c "echo '2' > /sys/module/8814au/parameters/rtw_switch_usb_mode"














### Comandos Básicos

````sh
# Buscar el nombre de la interfaz Wireless
iw dev

### Detener los programas conflictivos
systemctl stop NetworkManager && airmon-ng check kill && systemctl start NetworkManager

### Reiniciar Network Manager
systemctl restart NetworkManager
````

![image](https://user-images.githubusercontent.com/94720207/233819814-ab1b8d25-e746-408a-8c7c-d95ddf653568.png)

### Modo Monitor

````sh
ip link set wlan0 down && iw wlan0 set monitor control && ip link set wlan0 up
````

![image](https://user-images.githubusercontent.com/94720207/233820109-f6979e76-7e0c-46ca-afc0-7daad5457708.png)

- Resultado, ahora puedo hacer channel hopping incluso dual, de 2.4 y 5 GHz lo que antes no se podía: 

![image](https://user-images.githubusercontent.com/94720207/233820218-2fe6195e-5ad8-49b2-86bc-902a06e38bfc.png)



---

Driver: https://github.com/aircrack-ng/rtl8812au

````
* Use "ip" and "iw" instead of "ifconfig" and "iwconfig"
     It's described further down, READ THE README!
````

https://secwiki.org/w/Npcap/WiFi_adapters

![image](https://user-images.githubusercontent.com/94720207/233827035-6a9069da-db18-4f8b-b40d-22ff26196667.png)



- RTL

![image](https://user-images.githubusercontent.com/94720207/234780343-172f9125-8099-49b9-8421-07714f7f5aea.png)


### Atheros

![image](https://user-images.githubusercontent.com/94720207/233827184-13b744cf-1e2e-40db-b8b4-791e424eb99a.png)

drivers y demas epxlicaco0nes 

[ALFA AWUS036NHA: Does it have Atheros AR9271 chipset or AR9271L, and what is the difference anyway?](https://www.youtube.com/watch?v=zeRh_9IRVi8)

https://www.aircrack-ng.org/doku.php?id=compatibility_drivers_old


https://blog.finchsec.com/awus036axml-part1 la de wifi 6 alfa

![image](https://user-images.githubusercontent.com/94720207/235054553-73144374-6192-4ff1-92da-51b9db789da3.png)

Atheros AR9271 chipset inside the ALFA Network AWUS036NHA.
![image](https://user-images.githubusercontent.com/94720207/235055186-124bdf31-52d9-4106-a40f-0397ed16bc47.png)



awud 036h
![image](https://user-images.githubusercontent.com/94720207/235054228-6020bc7a-b690-468c-8122-5082f440a429.png)



![image](https://user-images.githubusercontent.com/94720207/235052181-a15ed182-2cb8-47d4-a9ec-ea7ef3fd6a21.png)

![image](https://user-images.githubusercontent.com/94720207/235052791-fdd70788-2187-460c-88fc-2394268d7d74.png)


---
---
---

comparación de ambas interfaces: 

````sh
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m";echo "";echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nDriver Manufacturer:%27s\nMonitor Mode:%33s\033[0m\n" "Present" "$(lsusb -D /dev/bus/usb/002/003 2>/dev/null | grep "iManufacturer" | awk '{print $3}')" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[35m$(lsusb | grep -E "^Bus (00[2-9]|[1-9][0-9]*)")\033[0m";echo "";echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m";echo "";echo -e "\033[36m$(ifconfig)\033[0m";echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m";echo "";iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````

![image](https://user-images.githubusercontent.com/94720207/235034361-e7c072fd-467e-436c-a206-8af4f808ad82.png)







coparacion beacon:

![image](https://user-images.githubusercontent.com/94720207/234753754-d08ed189-fbdd-4255-8337-977edd8842ac.png)

comparación beacon 2:

![image](https://user-images.githubusercontent.com/94720207/234755626-f99e73be-e753-43fe-bcd1-4784bed34e73.png)


comparacion 3:

![image](https://user-images.githubusercontent.com/94720207/234758726-04e31b24-ff0b-4f5b-81c4-e04efb1c001a.png)

comparación 4, el beacon tal cual :

![image](https://user-images.githubusercontent.com/94720207/234769138-2204dee7-873f-435c-9e66-e823a7d2d168.png)

comparando ahora que sabemos las diferencias el HEX

![image](https://user-images.githubusercontent.com/94720207/234774176-f482d198-147d-4981-ad85-e982bfb20efe.png)














## Comparación entre varias antenas

### Panda:

beacon airpwn

![image](https://user-images.githubusercontent.com/94720207/234749014-0c7a50eb-53d5-4c61-8926-16bf26f7268f.png)

---

### Atheros

![image](https://user-images.githubusercontent.com/94720207/234749869-4488f725-a05e-4df5-8e05-ab94fbb376c3.png)

---

### Alfa 1900

![image](https://user-images.githubusercontent.com/94720207/234750675-7d174888-0b07-4f2b-9152-a59a9d2b74bb.png)





















---

## 🟢 Selección de `Dispositivos de Captura`

Como ya se ha mencionado anteriormente, se tienen 3 tipos de sistemas que se pueden utilizar para capturar IEEE 802.11 Wireless frames:

1. `Mobile Protocol Analysis`
2. `Infraestructure AKA AP-based Analysis`
3. `Distributed Overlay analysis`

En el caso de los antenas utilizadas en `Mobile` pueden existir una amplia gama y cada vendor tendrá sus props y sus contras, tal cual se vió durante el `Laboratiorio de Drivers Fz3r0`. Esto también incluye el soporte de banda `2.4 GHz` y `5 GHz`, `Bandwith`, `MIMO`, `Spatial Streams`, etc... Cada una de estas cualidades de cada adaptador y sus antenas, le darán capacidades adicionales o limitarán a los dispositivos a capturar ya sea todo el tráfico posible o quizás solo una parte. 

- **Por ejemplo, una antena de `2.4 GHz` no puede capturar tráfico `5 GHz`, lo mismo pasa si el adaptador no soporta `MIMO` o no todas las `PHY` son compatibles. Si una antena y adaptador donde se está capturando solo tiene la capacidad de `1x1:1` podrá captruar tráfico, pero no verá todo el panorama completo y solo será capaz de capturar `1 spatial stream`.**

- [Alfa - AWUS036AXML - Triband 802.11b/a/g/n/ac/ax](https://www.alfa.com.tw/products/awus036axml?variant=39754360684616)
- [Panda Wireless - PAU06](http://www.pandawireless.com/panda300mbpsant.htm)

![image](https://user-images.githubusercontent.com/94720207/234764690-2d2d103f-c885-4c6d-8ffe-2aa95803b4bb.png)

En caso de captura con `Infraestructure AKA AP-based Analysis` todo depende del AP que se está capturando, por ejemplo comparando un `Ruckus R850` y un `Ruckus R300`, ambos pueden capturar frames 802.11 por infraestructura, pero el `R850` es de gama alta con capacidad incluso de WiFi6, mientras que el `R300` tiene menos capacidades. Es por ello que el `R850` podrá capturar aún más que el `R300`. Sin embargo, algo curioso es que el `R300` puede capturar `FCS - Frame Check Sequence` y los `R850` no.  REVIUSAR BIEN ESTOOOO CUAL ERA CUAL 

- [Ruckus R320 Datasheet](https://webresources.ruckuswireless.com/datasheets/r320/ds-ruckus-r320.pdf)
- [Ruckus R850 Datasheet](https://www.commscope.com/globalassets/digizuite/458063-ds-ruckus-r850.pdf)

![image](https://user-images.githubusercontent.com/94720207/234682042-d0a6c5dd-87d9-4286-b110-e554ddc3852a.png)

- **En caso de Ruckus, al momento de capturar 802.11 los clientes pueden seguir conectados sin problemas y el servicio sigue funcionando, algo que lo hace demasiado poderoso en comparación a otros vendors, los cuales deben desconectar a los clientes para poner sus APs en `Monitor Mode` y capturar `802.11 frames`.**

**Una ventaja abismal entre `Infraestructure AKA AP-based Analysis` y `Distributed Overlay analysis` frente a `Mobile Protocol Analysis` es que estos se pueden hacer de manera remota, justo en sitio del problema y la ubicación de la red misma, además, tenemos capacidades de captura de PHY bastante complejas como el ejemplo del `Ruckus R850` que tiene capacidades de `8x8:8` y `WiFi 6 802.11ax` cosa que ningún adaptador al alcance de cualquier persona pueda capturar, sin embargo, esto solo está al alcance de empresas que pueden costear estos servicios e infraestructura. 

- **Para hacer el mejor análisis posible y en caso de ser necesario, lo mejor sería combinar los 3 métodos de captura desde diferentes lugares.**



## 🟢 Selección `Ubicación de Captura`

Para llevar a cabo una captura de tráfico de manera efectiva, es importante seleccionar cuidadosamente tanto los canales como las ubicaciones óptimas desde las cuales llevar a cabo esta tarea.

Para realizar una captura de tráfico deseado dentro del alcance de recepción, es importante seleccionar cuidadosamente las ubicaciones óptimas desde las cuales llevar a cabo esta tarea. Una estrategia común es capturar cerca de los clientes que presentan problemas o comportamientos sospechosos, o en escenarios de pruebas de penetración, cerca de los clientes y redes que se desean atacar para explotar vulnerabilidades o crear puntos de acceso malintencionados.

Algunas áreas de donde se pueda llevar a cabo en análisis, es posible que requieran de autorización previa o escolta para poder llevar a cabo la captura de tráfico, al igual que sucede cuando se realizan `site surveys on-site` para el diseño de redes inalámbricas. En algunos casos, también puede ser necesario el uso de equipos de seguridad especiales como cascos o arnés.

En cuanto a la elección de la ubicación para la captura de tráfico, es recomendable estar cerca de los dispositivos que presentan problemas, ya que esto permite exponer las herramientas de captura a los mismos problemas que está experimentando el dispositivo del cliente. Al monitorear en la ubicación inmediata del cliente, se pueden detectar problemas en la capa 1 o capa 2 de manera más rápida que si se recopila información desde una ubicación más cercana al punto de acceso.

Es importante tener en cuenta que al estar cerca de un cliente con problemas, la captura de tráfico se asemejará más a la experiencia del usuario, lo que puede resultar en una mejor comprensión y resolución del problema.

![image](https://user-images.githubusercontent.com/94720207/235498840-78e3608e-f511-4d69-a433-5dbad29662d8.png)

- Si varios clientes tienen problemas, sería mejor capturar cerca del AP donde todos estén conectados, además de capturar cerca de los clientes. Al capturar en ambas ubicaciones, cerca de los clientes y cerca del AP, es posible que pueda encontrar una solución más rápida que capturando desde solo una ubicación.
- Si todos los clientes de un AP en particular tienen problemas y reiniciar el AP no resuelve el problema, capturar más cerca del AP puede revelar un problema constante causado por el AP.

![image](https://user-images.githubusercontent.com/94720207/235499059-135e3fcd-f3d3-4c87-becc-0d1ff39a7dec.png)

El tipo de problemas que se informen por parte del cliente, nos puede guiar en la selección de las ubicaciones de captura: 

- **Si solo un cliente tiene problemas, capture cerca de él.** 
- **Si varios clientes informan problemas, se debe capturar cerca del AP y de algunos, si no de todos los clientes, hasta encontrar la fuente del problema.**
- **Los problemas persistentes se diagnostican más rápidamente que los intermitentes.**

![image](https://user-images.githubusercontent.com/94720207/235499381-1cfbf252-8bc1-40c2-983b-29a039990f7a.png)

A veces, la primera captura brindará las respuestas que estamos buscando. Cuando no... puede ser necesario capturar desde otras ubicaciones o durante períodos más largos de tiempo, o incluso al mismo tiempo con diferentes herramientas. 

Se pueden utilizar múltiples métodos de captura cuando estén disponibles y también capturar desde diferentes ubicaciones, hasta que se diagnostique el problema... pero...  ¡No todos los problemas se resolverán con la captura de paquetes! No se pueden resolver los problemas de WiFi capturando 802.11 frames en el aire mientras que los switches de lis IDFs están en el suelo, llenos de telarañas y los cables comidos por serpientes. ¡Una captura nunca mostrará eso! Hay que ser objetivos en los escenarios que se requiere una captura realmente. 

![image](https://user-images.githubusercontent.com/94720207/234729826-49f212c8-9450-478b-8460-535c732e8b6d.png)

También no hay que olvidar que nos podemos basar en otras herramientas como `logs`, `error messages` y un `análisis profundo de configuraciones`. Por ejemplo revisar dispositivos `layer 3` y sus configuraciones como `firewalls` o `routers`, o dispositivos `layer 2` como `switches`, incluso el mismo medio que suele ser cableado ya sea por `cobre` o `fibra` utilizando el estándar `IEEE Ethernet 802.3`.

Las capturas no solo deben ser desde diferentes ubicaciones, sino también desde diferentes canales utilizados alrededor de esa área, ya sean dispositrivos propios o quizás dispositivos ajenos como otras antenas, rogues u otros clientes. Si tenemos problemas en un `SS - Service Set`, debemos fijar manualmente el analizador en ese mismo canal o canales utilizados por los `APs` y `STAs`.

![image](https://user-images.githubusercontent.com/94720207/235500146-bf845370-d424-4378-991d-5daaa9ef1ada.png)

Si se trabaja en 2,4 GHz, se puede bloquear el analizador en un solo canal, pero aún es posible ver el tráfico transmitido en canales adyacentes superpuestos, siempre y cuando el dispositivo receptor esté lo suficientemente cerca de las radios transmisoras. Al examinar tramas, se pueden observar dos canales en un análisis de trama capturada:

1. **El primer canal que se ve es el canal en el que el adaptador estaba cuando capturó la trama.**
2. **El segundo canal, que se ve en el cuerpo de la trama, es el canal en el que la trama indica que fue transmitida.**

![image](https://user-images.githubusercontent.com/94720207/235506651-c1ed3b20-dec7-4f96-ba10-00cd2b360897.png)

Si la trama se está transmitiendo en un canal adyacente superpuesto, **se puede corregir el problema ajustando el plan de uso de canales en la configuración del AP o controlador inalámbrico.**

---

### ☠️ 🦈 `Fz3r0 Blackshark Filter`: 2.4 GHz Channel & Adjacent Channel Capture + Malformed & Undecoded Packets

🟢 **CANTO II - Selección Ubicación de Captura**

- Este filtro es utilizado para filtrar el canal real y el canal donde se capturó el frame, para asi poder comprarar, muy útil para ponerlo en la lista ;)

````py
## Fz3r0 Blackshark v4.0 - Standalone Filter for CWAP

## - Filtrar por el canal en donde se está capturando (Este es el filtro que normalmente se utiliza)
wlan_radio.channel
wlan_radio.channel == 1
wlan.ds.current_channel == 6
wlan.ds.current_channel == 11

## - Canal real de AP / Antena - Visto desde un Beacon Frame en el Body
wlan.ds.current_channel
wlan.ds.current_channel == 1
wlan.ds.current_channel == 6
wlan.ds.current_channel == 11
````

**Ejemplo:**

- [Fz3r0_Adjacent_Channel_CWAP (PCAP)](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11363588/Fz3r0_Adjacent_Channel_CWAP.zip)
- Estoy capturando en `Channel 5`, pero mi red `Fz3r0_Air_PWN` está en `Channel 6`, pero como hacen `overlap` puedo capturar ambos, sin embargo, el `Radiotap Header` (en otros softwares viene como `Network Media Info`) marca `Channel 5` ya que aquí capturé, pero... 

![image](https://user-images.githubusercontent.com/94720207/235409105-d8de9088-570f-4798-8e2a-635760745be6.png)

- ...pero en realidad ese SSID yo lo hice en el `Channel 6`, y yo estoy seguro haberlo configurado en ese canal, esto se puede ver en el body del `Beacon Frame`:

![image](https://user-images.githubusercontent.com/94720207/235409429-2bba6ea8-5321-4bd8-846c-c657b69a3bdd.png)

- Si simplemente se detecta la trama mientras el adaptador está en un canal adyacente superpuesto y se observa que el AP está en un canal correcto y no se detecta ninguna interferencia superpuesta, se puede eliminar este problema potencial y asumir que la trama estaba corrupta y mal interpretada (decodificada incorrectamente).

![image](https://user-images.githubusercontent.com/94720207/235479568-a79c41e2-aed7-4ab6-b5a2-50cf00b313ee.png)

- Puedes encontrarse tanto errores `malformed packets` como de `undecoded`, incluso ambos en un mismo paquete:

![image](https://user-images.githubusercontent.com/94720207/235481033-025aca27-1d43-49c6-929b-f132ae6564f3.png)

- En el siguiente filtro se muestra como filtrar `malformed packets`:

````py
## Fz3r0 Blackshark v4.0 - Standalone Filter for CWAP

## - Filtrar por Malformed Packets en un Beacon Frame
_ws.malformed
_ws.expert.group == "Malformed"
````

---

Antes de comenzar la captura, es importante determinar el mejor método de captura, las mejores ubicaciones para la captura y si se fijará en un canal específico o se escanearán todos los canales mientras se captura.

Al solucionar problemas de roaming, es útil tener múltiples adaptadores, cada uno fijo en un canal utilizado por un AP diferente en el área dentro de la banda que se está analizando. Por ejemplo:

- Si hay 3 APs que utilizan la banda de 2,4 GHz en el área de captura:
    - Cada AP está en un canal diferente: CH 1, CH 6, CH 11.
    - Se necesitarán 3 adaptadores para capturar: CH 1, CH 6, CH 11.
    - Esto permitirá capturar todo el proceso de roaming incluso si el cliente se mueve entre los 3 AP que utilizan diferentes canales. 
    
- _*Si solo se está capturando en un canal, la solución de problemas de roaming llevará más tiempo y será mucho más difícil._

![image](https://user-images.githubusercontent.com/94720207/235501677-bfa14270-f9ea-4f8c-84dc-49c0b3fe3264.png)

En cuanto a la ubicación, si se captura con un solo dispositivo usando varios adaptadores, colocarlo entre los APs (relativamente centrado en RF) hará que sea probable capturar los eventos de roaming entre esos 2 AP. Si se usan varios dispositivos de captura con varios adaptadores cada uno, pueden colocarse de manera distribuida muy cerca de los APs en cuestión ya sean 2, 3, 4, etc... y las múltiples capturas se pueden combinar para ver lo que ven los diferentes APs, lo que debería incluir transmisiones relacionadas con el roaming.

![image](https://user-images.githubusercontent.com/94720207/235510744-feaed8ca-70d7-4d8a-a9a2-5a6bff12bb2a.png)

**Para obtener los mejores resultados, se debe intentar tener los radios utilizados en la captura de frames 802.11 lo más cerca posible de los dispositivos que transmiten los frames 802.11 y en los mismos canal(es). Esto puede o no ser posible según el método de captura disponible: móvil, infraestructura o distribuido. Por ejemplo, con infraestructura se podrían tomar diferentes APs al mismo tiempo para capturar exactamente en su ubicación**

![image](https://user-images.githubusercontent.com/94720207/235499638-39ee673a-9d09-4c23-803e-5c7bf3713fcf.png)

Es posible que se necesite capturar desde muchas ubicaciones de clientes para obtener la mejor información para su diagnóstico. Para determinar el mejor lugar desde el cual capturar, se deberán tomar algunas decisiones como:

- El tipo de 802.11 Frames que se necesitan capturar.
- Alcance de captura de BSS o ESS (uno o varios AP).
- Captura para un STA o AP específico.
- Captura para varios AP y escenarios de roaming.
- Captura para un grupo de STAs o APs.

También se determinará qué áreas físicas proporcionarán la mejor perspectiva de los paquetes: el lado del cliente o el lado del AP de las conversaciones. Se deberá determinar si es necesario solo un lado de la conversación o ambos lados. Se deberá saber si la captura es para diseñar, solucionar problemas o establecer una línea base de la red.

- **Al analizar el tráfico de un cliente inalámbrico, se deberá mover junto con el cliente para aumentar la probabilidad de capturar todo lo que el cliente transmite y recibe.**

Conocer los AP en la ruta de roaming y sus canales es necesario para un mejor análisis de los problemas de roaming. Se deberían usar varios adaptadores, cada uno bloqueado en los canales apropiados para capturar y solucionar problemas de roaming, como se discutió anteriormente. Los problemas localizados se diagnostican más fácilmente. Los problemas que abarcan toda la empresa requerirán diagnósticos en varios lugares, tanto estacionarios como móviles.

![image](https://user-images.githubusercontent.com/94720207/235513875-b70e4239-282f-40ae-ada8-d1d28b8366ab.png)

- https://excalidraw.com/#json=KTbDCxXrfHfjQCLblq_FK,2N9NxWjVlDCTbmXZ--BHlA
- https://excalidraw.com/#json=08JAHCru-VuxDt7ig9cfl,2Lw9YhsKBtoVVYGt4dn08Q
- https://excalidraw.com/#json=uNNI-dc6NyvE9S7JiGmK7,78IrP7RAIpDpeAzLiII1eA

La ubicación de la captura de paquetes 802.11 frames es muy importante para exponer los mismos problemas que experimenta el dispositivo del cliente, lo que permite una mejor comprensión y resolución del problema y siempre hay que tener en cuenta las bases que se expusieron en este bloque:

1. **Es recomendable estar cerca de los dispositivos que presentan problemas para detectarlos de manera más rápida.** 
2. **Si varios clientes presentan problemas, es mejor capturar cerca del punto de acceso y algunos, si no de todos los clientes, para encontrar la fuente del problema.**
3. **Los problemas persistentes se diagnostican más rápidamente que los intermitentes.** 
4. **Aunque no todos los problemas se resolverán con la captura de paquetes, se pueden utilizar otras herramientas como logs, mensajes de error y un análisis profundo de configuraciones.** 
5. **Es recomendable capturar desde diferentes ubicaciones y canales utilizados en esa área para obtener una perspectiva más completa del problema.** 
6. **El análisis de tramas capturadas en diferentes canales puede revelar información valiosa sobre la ubicación de dispositivos transmisores y receptores.**
7. **Se recomienda capturar con diferentes métodos de ser posible, por ejemplo `mobile` e `infraestructura`**

Hay que tener siempre presente que cada escenario será un mundo diferente y con estos conceptos hay que saber improvisar sobre la marcha y utilizar el sentido común, la experiencia y saber identificar la necesidad del momento para diagnosticar cuál será la mejor ubicación para capturar. 

---

<!-- 

FIN DE CAPITULO :D

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 🟢 Selección `Tiempo de Captura`

Algunos problemas pueden ocurrir ocasionalmente, mientras que otros duran períodos de tiempo más largos y son persistentes. Si el problema que se está diagnosticando ocurre en los mismos periodos de tiempo una y otra vez, es en esos momentos cuando se debe realizar la captura de Frames 802.11. Si el problema es persistente, se puede realizar la captura en cualquier momento prácticmenete para diagnosticar el problema, mientras se realice en la ventana de tiempo de la incidencia. 

Capturar una cantidad adecuada de tiempo revela rápidamente los beneficios de una solución de monitoreo superpuesta dedicada 24/7. Tal solución debería permitirle acceder a los registros o panel de control y ver capturas, posiblemente tanto del protocolo como del espectro, en cualquier momento del pasado almacenado. Es importante tener en cuenta que el sistema puede almacenar una ventana de tiempo histórico limitada, pero siempre y cuando sea inclusiva de las últimas 24-48 horas, suele ser suficiente para "regresar en el tiempo" al momento en que ocurrió el problema y ver la actividad que se produjo en el entorno en ese momento.

Además, es fundamental tener conocimientos técnicos sólidos para realizar una captura y un análisis adecuados de los datos capturados. Es importante asegurarse de tener las herramientas adecuadas y la experiencia necesaria para interpretar los resultados de la captura de tramas y poder realizar un diagnóstico preciso del problema.

- [Saavius Omnipeek - Network Analysis Software - Datasheet](https://www.neox-networks.com/downloads/savvius_omnipeek_datasheet_nxen.pdf)

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/235543278-4f827624-c587-4107-ad2c-514d26224206.png" alt="TCP vs UDP" height=680px/> </a> </p> 

Es importante que antes de empezar cualquier tipo de captura, ya sea corta o larga, se sincronice el `timestamp` de los dispositivos de captura con el mismo `servidor NTP` que se utiliza para sincronizar la red. Esto es fundamental porque la captura de frames deberá ser combinada con otras capturas, registros de servicios y de depuración, tanto inalámbricos como alámbricos. Si los timestamps no están sincronizados, se dificulta la tarea de combinación y análisis de los datos. Por lo tanto, **es necesario asegurarse de que todos los dispositivos de captura estén sincronizados con el mismo `servidor NTP` para poder combinar y analizar los datos de manera efectiva.**

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/235807462-bd034955-d372-4599-84aa-e931c481ba8b.png" alt="TCP vs UDP" height=200px/> </a> </p> 



 - **Al proceso de recopilación y combinación de datos de varias fuentes en un solo lugar o conjunto de datos coherente se le llama `collation`.**

El `collation` se refiere a la necesidad de **recopilar y combinar los datos capturados de diferentes dispositivos y registros de servicios** para analizar el rendimiento y solucionar problemas de la red. Al sincronizar los `timestamp` en todos los dispositivos de captura con el mismo `servidor NTP`, se facilita la tarea de `collation` de los datos capturados y se obtiene una imagen más clara y precisa del rendimiento de la red.

- **En `Blackshark` existen columnas con el timestamp desde la fecha hasta millonésimas de segundos por default, además del delta:**

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/235801050-277a2046-0906-4192-b850-0ffdb57c69b6.png" alt="TCP vs UDP" height=680px/> </a> </p> 

Un problema común es el fallo de autenticación o `Authentication Failure`. Aunque esto puede suceder en cualquier momento en que los usuarios o dispositivos intenten conectarse, los momentos críticos son el inicio de los turnos y el regreso de las pausas de comida. Es importante capturar durante estos picos de autenticación para encontrar la fuente de los problemas de autenticación que afectan a múltiples usuarios.

- Si solo una persona o dispositivo tiene problemas para conectarse, es probable que el problema se deba al dispositivo o al usuario. Para capturar estos frames, necesitarás estar cerca del usuario o dispositivo en el momento en que intentan conectarse. Este diagnóstico suele completarse en cuestión de segundos.
- ¡Recuerda! Se recomienda capturar cerca del cliente si solo un cliente tiene problemas de autenticación, pero es mejor capturar cerca del AP y analizar ambas capturas. La mayoría de las veces será suficiente estar cerca del cliente.

Cuando se utiliza `PSK`, **la causa más probable de que un solo usuario o dispositivo no pueda autenticarse es el uso de la PSK incorrecta**. Para saber como verificar esto, hice un pequeño laboratorio e inicié sesión sesión en la red `Fz3r0_Air_PWN`: 

- [Fz30_AuthFail_Authgood.zip](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11378786/Fz30_AuthFail_Authgood.zip)

````py

## Fz3r0 Air Shark Filter

# Papu pro full 4-way-handsjake process
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol)
````

![image](https://user-images.githubusercontent.com/94720207/236555643-93622105-4f90-451c-862a-28032bb689f3.png)


1. `Primer Intento`: Se escribe la **contraseña incorrecta**
    - Se escribe un `PSK` incorrecto `askjdha6786sadasdqa23423` una sola vez, automáticamente el dispositivo trata de autenticar varias veces al AP, pero este lo deautentica una y otra vez ya que la contraseña es incorrecta.
    - Se puede ver muy claramente que el `4-way-handshake` no está completo y solo están los mensajes `1` y `2` 

2. `Segundo Intento`: Contraseña correcta: `godzilla2000`
    - Al escribir bien el `PSK` correcto se tiene acceso a la red y tráfico de Internet sin problemas.
    - En la captura se ve un único intento y los `4` mensajes del `4-way-handshake`

Si analizo exactamente el `timestamp` me puedo dar cuenta con exactitud en qué momento ha intentado hacer log-in, además de saber exactamente en el segundo que logró hacer login, con una presición de millonésimas de segundo, las cuales se pueden incrementar aún más: 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/235818099-b4aed1e7-13fe-4271-a199-5f63c089b01f.png" alt="TCP vs UDP" height=620px/> </a> </p> 

Cuando se utiliza la `autenticación 802.1X`, **existen varias posibles causas de falla en la autenticación** a diferencia con PSK WPA2. De cualquier modo, con cualquier método de autenticación, **la ventana de tiempo que se requiere para capturar los `802.11 frames` necesarios para el diagnóstico de `autenticación` es muy corto, una cuestión de segundos.**

- Los problemas simples pueden ser considerados como aquellos que no tienen muchas ramificaciones, es decir: **O funcionan o no funcionan**, como la `autenticación`, son fácilmente diagnosticadas. Solo es necesario conoces respecto al `Frame Exchange` de un proceso de autenticación y buscar por el proceso en un `.pcap` durante un corto periodo de captura. Se puede comparar la información durante la autenticación con lo que se encuentra en la captura, lo que le permite identificar rápidamente el problema.

Los problemas que se prolongan durante períodos más largos de tiempo, también tomarán más tiempo para diagnosticar. ¿Qué sucede si los usuarios se quejan de que la red es lenta? ¡El clásico reporte de que "la red es lenta"! En realidad esto es muy abstracto y puede tener demasiadas variables y ramificaciones... 

- Primero, se debe definir "lento" y compilar diferentes variables, por ejemplo:
    
    - Conocer la capacidad de la red
    - Utilización del tiempo de aire
    - Tipos de clientes
    - Protocolos utilizados
    - Ancho de banda del enlace a Internet del ISP
    - Ancho de banda Ethernet
    - Versiones de MIMO admitidas
    - Cualquier limitación en los perfiles de RF de los puntos de acceso
    - Varias otras piezas de información que podrían definir "lento"....

- **Una vez que sepamos para qué está diseñada la red, se pueden empezar a ejecutar capturas de `frames 802.11` para ver qué está sucediendo en el espacio.**
- **En escenarios que requieran `capturas prolongadas`, resulta conveniente emplear métodos `infraestructure` y `distributed`. De lo contrario, se podría requerir mucho tiempo en el lugar utilizando un método `Mobile` para diagnosticar el problema.**

![image](https://user-images.githubusercontent.com/94720207/234778168-e385cfd2-b5b8-4900-83c0-9c3913e93ecf.png)

Al solucionar problemas de red, es una buena práctica **"ir trabajando de abajo-hacia-arriba"**. Esto significa que se debe comenzar el diagnóstico en la capa más baja del modelo OSI y avanzar hacia la cima. Si no se detecta un problema en `Layer 1`, como una cámara inalámbrica u otra fuente de interferencia que esté saturando el medio, se debe pasar a analizar `Layer 2` y realizar una captura de `Frames 802.11`. 

- **En algunos casos, el problema NO está relacionado con `WiFi`**, sino con `DNS`, `DHCP` o el `Firewall`. Algunos problemas se pueden solucionar rápidamente, mientras que otros pueden requerir mucho tiempo para diagnosticar. Es por eso que también es importante saber capturar en Ethernet 802.3, por ejemplo saber revisar si existió un proceso completo de DHCP:

````py
## Buscar por protocolo DHCP
DHCP

## Buscar por un ID de transacción DHCP
dhcp.id == 0x53078034
````

![image](https://user-images.githubusercontent.com/94720207/235826778-698facfc-6ba3-444a-a196-e946fdd3cfe7.png)

Si se determina que el problema está en la red Ethernet cableada, puede ser necesario mostrar y explicar la captura al administrador de red cableada. Un problema común en el lado LAN cableado que se atribuye erróneamente a WiFi es **la falta de `IP Addresses` en el ámbito de `DHCP`. Esto también se puede capturar Wireless (es importante realizer `IEEE 802.11 Desencrypt`)**

![image](https://user-images.githubusercontent.com/94720207/236560285-c8a257cd-70cf-4e45-9d2f-206b20d0d116.png)

- Una captura inalámbrica mostrará el `Probe Request`, la `Probe Response` y el `Authentication Exchange`. Después de estos eventos, se debe observar una `DHCP Request` desde el cliente inalámbrico seguida de una `DHCP Response` desde el `DHCP Server`:

![image](https://user-images.githubusercontent.com/94720207/236561376-fe126a40-0734-4294-9a21-905bc564b202.png)

- Si el servidor no está disponible, no habrá respuesta

- Si el servidor está disponible pero no hay direcciones IP disponibles, se verá una respuesta negativa de DHCP

La captura inalámbrica de este proceso es muy similar a la de un proceso de DHCP de una estación cableada, con la adición de las transmisiones del punto de acceso para la gestión del medio inalámbrico. Un administrador de red con cable debería poder ver esto y resolver el problema en el lado con cable de la red. El diagnóstico de este problema lleva solo unos momentos más que el diagnóstico de una falla de autenticación.

---

<!-- 

FIN DE CAPITULO :D

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 🟢 Capturando un `canal a la vez` VS `varios canales`

Es muy importante comprender que solo se puede capturar en un canal a la vez con un adaptador 802.11. **Para capturar más de un canal al mismo tiempo, se deben utilizar múltiples adaptadores y software que permita capturar con varios adaptadores al mismo tiempo.** Se puede escanear un canal con un único adaptador, pero esto no es lo mismo que capturar en varios canales simultáneamente. El escaneo simplemente captura lo que hay en ese momento en el canal. 

Este límite se impone porque la radio solo puede sintonizarse en un canal específico en un momento dado y, por lo tanto, solo puede capturar tramas del canal sintonizado. Dependiendo del escenario de resolución de problemas, puede ser aceptable capturar en cada canal durante un período y luego analizar los datos agregados. Este último método se utiliza principalmente para resolver problemas de rendimiento o validar configuraciones de seguridad. **Para un análisis efectivo de roaming, se requieren típicamente múltiples adaptadores.**

- **En ocasiones, se necesita capturar en `un solo canal`, en otras ocasiones `todos los canales` y en otras se requiere `un grupo específico de canales`... todas estas técnicas tienen sus respectivos problemas:**

- [USB WiFi Adapters that are supported with Linux in-kernel drivers](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)

---

### ⭕ Capturando en un solo canal

- Cuando se escanean un solo canal, se pierde tráfico transmitido en todos los demás canales. Es decir, si se captura en el Channel 6 de 2.4 GHz, se perderá información de los canales: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14.
- Ojo!!! No se perderán todos los frames en realidad de los demás canales, hay que recordar que en caso que algún canal adyacente haga ACI, se podrán capturar frames de ese canal, con sus respectivas pérdidas y retransmisiones por el hecho de ser interferencia, esto solo puede pasar en la banda de 2.4 GHz o en caso que el bandwith del 5 GHz haga overlap, como puede pasar con 40, 80 y 160 MHz.
- Cuando se escanea un solo canal, independientemente de la banda, se recopila la mayor cantidad de información posible sobre el uso de ese canal específico en ese espacio.
- **Para este tipo de captura solo se necesita `1 adaptador`**

**📡 Ejemplos de adaptadores que capturan 1 solo canal en banda 2.4 GHz:**

![image](https://user-images.githubusercontent.com/94720207/236634132-fd794d85-66ec-4554-aa92-00441d301fa4.png)

**📡 Ejemplos de adaptadores que capturan 1 solo canal en banda 2.4 GHz y 5 GHz:**

![image](https://user-images.githubusercontent.com/94720207/236634900-c009c869-6122-4ac2-b7b0-c9d4f33790fc.png)

**📡 Ejemplos de adaptadores que capturan 1 solo canal en banda 2.4 GHz, 5 GHz y 5.9GHz (WiFi6):**

![image](https://user-images.githubusercontent.com/94720207/236635148-1e64a36d-7080-4167-9dff-c06d69ab02e9.png)

**⚙️ Configuración de adaptador para hacer capturar `1 solo canal` incluyendo la selección de canal para un solo adaptador:.**

````sh
# Activando Monitor Mode en un adaptador Fresh (wlan0) 
clear; airmon-ng start wlan0; iwconfig wlan0mon channel 6 && ifconfig wlan0mon down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0mon; ifconfig wlan0mon up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev
````

![image](https://user-images.githubusercontent.com/94720207/236589278-f7f86485-786e-402b-a781-50ec0d710210.png)

Utilizando armon-ng con la flag `-c` se puede ajustar la auditoría de red inalámbrica al canal deseado _(de caso contrario se utiliza el default o el que se ajustó al poner `Monitor Mode`, en mi caso CH 6)_, pero el truco del padrino ;) es también utilizarlo para capturar con wireshark. Con esta técnica se puede guardar por un lado el archivo .pcap, por otro el .cap, además de auditar la red desde las 2 plataformas (aircrack-ng + Blackshark) utilizando el canal 6 como canal fijo. 

![image](https://user-images.githubusercontent.com/94720207/236628039-fa60e710-7207-4d90-86f9-ffeae60aab32.png)

La captura en `Blackshark` se ve así:

- [Same Channel Capture PCAP](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11412513/fz3r0_same_channel.zip)

![image](https://user-images.githubusercontent.com/94720207/236629193-8a2b429a-b42a-4aed-8de4-b17fa53b77b6.png)

---

### ⭕ Capturando un Canal con Channel Hopping

- Cuando se escanean varios canales, se pierde tráfico transmitido en los canales que no se están escaneando durante el tiempo que se dedica a un solo canal mientras se ciclan por los diferentes canales. Es decir, si el ciclo dura 3 segundos por canal, dedicará 3 segundos en pasar por cada canal, en caso de 2.4 GHz recorrer los 14 canales llevaría 42 segundos para regresar al mismo canal, perdiendo toda esa ventana de captura. 
- Con esta técnica se recopila cierta información sobre todos los canales que se están escaneando y aunque no sea toda puede ser muy útil para tareas de auditorías de seguridad de red, pentesting, scanning y routing.
- **Para este tipo de captura solo se necesita `1 adaptador`**

Configuración de adaptador para hacer `Channel Hopping` (En realidad es la misma que capturar 1 solo canal)

![image](https://user-images.githubusercontent.com/94720207/236589255-2552be03-60c1-412e-a3b6-87227db47740.png)


Utilizando `armon-ng` por default la auditoría hace `Channel Hopping` y de hecho es muy útil para auditar la red en consola, pero el truco del padrino ;) es también utilizarlo para capturar con wireshark. Con esta técnica se puede guardar por un lado el archivo `.pcap`, por otro el `.cap`, además de auditar la red desde las 2 plataformas (`aircrack-ng` + `Blackshark`) mientras se realiza `channel hopping` con la capacidad de modificar el tiempo entre cada `hop`

![image](https://user-images.githubusercontent.com/94720207/236587738-a5745acb-e3ec-4633-9177-26cf60d92d17.png)

⚙️ **Configuración haciendo Channel Hopping cada 500ms:**

- [channel hopping capture .PCAP](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11410825/channel_hopping_capture.zip)

````sh
airodump-ng wlan0mon -f 500
````

![image](https://user-images.githubusercontent.com/94720207/236588774-b3f1106b-ea2a-47e8-a982-9b46777ebd67.png)

En Wireshark puedo ver los Beacons de **diferentes SSIDs en diferentes canales**, pero ojo!!! recordemos que NO son simultáneos, es con `Channel Hopping`:

![image](https://user-images.githubusercontent.com/94720207/236589174-b498a2bd-d932-4dcd-8e5f-3c1691cb89d0.png)

---

### ⭕ Capturando múltiples canales específicos 

- Cuando se requiere analizar el comportamiento de múltiples canales específicos simultáneamente, se debe capturar en cada canal utilizando varios adaptadores para capturar en cada canal al mismo tiempo, lo que aumenta el costo y la complejidad de la configuración.
- Capturar en múltiples canales específicos es necesario para analizar problemas de roaming y en otros casos para analizar canales específicos con alta densidad de tráfico o simplemente porque conocemos los canales específicos que se utilizan en la red que se analizará. Por ejemplo si nuestra red es una 2.4 GHz que utiliza únicamente los canales 1, 6, y 11 sabemos que debemos atacar estos canales principalmente, en esta caso se necesitaría utilizar 3 adaptadores, uno en cada canal respectivo. 
- Un agran ventaja es que permite observar el comportamiento de los dispositivos en diferentes canales de manera simultánea, lo que mejora la resolución temporal y proporciona una imagen más precisa de lo que está sucediendo en la red Wi-Fi.
- También se puede obtener más información sobre el uso y la congestión en cada canal, lo que es útil para identificar problemas de rendimiento y congestión. Además que ayuda a analizar la información de varias antenas o SSIDs en un mismo archivo de análisis _(O separar y filtrar la información a palcer)_ .
- Uno de los usos más comunes es para tener una mayor precisión en análisis de roaming. Capturando en múltiples canales se pueden observar los eventos de roaming en diferentes canales, lo que permite un análisis más preciso del comportamiento de roaming. Por ejemplo, se puede observar si un dispositivo se conecta a un AP que está emitiendo en un canal diferente del que estaba antes.
- Capturar en varios canales simultáneamente requiere más recursos de hardware, como CPU y memoria, lo que puede afectar el rendimiento del sistema.
- La captura en varios canales simultáneamente produce una cantidad mayor de datos, lo que puede requerir más tiempo para analizar y puede aumentar la posibilidad de perder información importante.

**📡 Para capturar en múltiples canales se deben utilizar múltiples adaptadores y software que permita capturar con varios adaptadores al mismo tiempo. A continuación, se muestra un ejemplo de configuración para capturar en los canales 1, 6 y 11 utilizando tres adaptadores diferentes:

![image](https://user-images.githubusercontent.com/94720207/233807729-6c0cd857-e134-4760-b47f-4b4bf80e0c2e.png)

**📡 Simular ocurre con los sistemas de Raspberry:** 

![image](https://user-images.githubusercontent.com/94720207/236657000-50dccd44-915a-4efc-982d-db4937b7200a.png)


**📡 Este ejemplo en específico es mi antena Fz3r0 para capturar 3 canales con los Adaptadores chinos baratos pero con Chipset Atheros 😉** 



- **⚙️ Primero utilizo mi one-liner validador Less is more GOD, por el momento veo los 3 adaptadores pero aún no están en modo monitor**

````sh
# GODs combined
clear;echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "" && echo -e "\033[32m$(airmon-ng)\033[0m" && echo -e ""; echo -e "\033[32m$(iw dev)\033[0m"
````

![image](https://user-images.githubusercontent.com/94720207/236647686-269be5b2-57b6-4fe9-b8b6-28b511fa7f6c.png)

- **⚙️ Después uso mi one-liner triple monitor:**

````sh
# Triple encendido de Adaptadores desde 0 (wlan0) 
# [Channels: 1, 6, 11]
clear;airmon-ng check kill && airmon-ng start wlan0; airmon-ng start wlan1; airmon-ng start wlan2 && iwconfig wlan0mon channel 1 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 11 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````

**⚙️ Mi one-liner para poner en monitor 3 adaptadores simultáneos, cada uno en nu respectivo canal (1,6,11), incluyendo un MAC spoofing de MACs consecutivas y validación es el siguiente:** 

````sh
# Triple encendido de Adaptadores desde 0 (wlan0) 
# [Channels: 1, 6, 11]
clear;airmon-ng check kill && airmon-ng start wlan0; airmon-ng start wlan1; airmon-ng start wlan2 && iwconfig wlan0mon channel 1 && iwconfig wlan1mon channel 6 && iwconfig wlan2mon channel 11 && ifconfig wlan0mon down; ifconfig wlan1mon down; ifconfig wlan2mon down && macchanger --mac=f0:f0:f0:00:00:00 wlan0mon && macchanger --mac=f0:f0:f0:00:00:01 wlan1mon && macchanger --mac=f0:f0:f0:00:00:02 wlan2mon && ifconfig wlan0mon up; ifconfig wlan1mon up; ifconfig wlan2mon up && clear; echo -e "\033[31m[+] AIR-SHARK by Fz3r0 💀 - Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m";echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m";echo "";echo -e "\033[97m[*] MULTIPLE WIRELESS CHANNEL MONITOR & CAPTURE\033[0m";echo ""; echo -e "\033[97m[*] TRIPLE WLAN ADAPTER START - [CHANNEL 1 | CHANNEL 6 | CHANNEL 11] - @ 2.4 GHz\033[0m";echo "";echo -e "\033[97m--- SYSTEM:\033[0m";echo "";echo -e "\033[32m$(uname -a)\033[0m" && echo "";echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions';iw dev
````
![image](https://user-images.githubusercontent.com/94720207/236647969-ea6302e1-013b-4604-83f8-32705a6ecb38.png)

Para capturar con airodump desde varios adaptadores hayq ue separarlos por coma "," recomiendo hacer fijado el canal deseado para cada una, como lo compartí en mi one-liner anterior. BONUS: También está el comando para hacer Channel Hopping con 3 adaptadores:

````sh
# 3 Adaptadores capturando CH 1, 6 y 11
airodump-ng wlan0mon,wlan1mon,wlan2mon -c 1,6,11

# Channel Hooping con 3 Adaptadores
airodump-ng wlan0mon,wlan1mon,wlan2mon
````

![image](https://user-images.githubusercontent.com/94720207/236648230-7accd246-1e58-42f1-afad-3973c79d56dc.png)

Para capturar los 3 adaptadores con `Blackshark` solo se tienen que seleccionar las 3, así de sencillo:

![image](https://user-images.githubusercontent.com/94720207/236648188-47889586-7905-4e73-9cfd-c1f77c85ef9d.png)

**Y se podría ver la captura de cada adaptador en su canal en un mismo archivo `.pcap`. Como nota curiosa notar como el Delta y Los tiempos están sumamente pegados el uno del otro, incluso el Delta marca negativos!!! Esto es porque al capturar al mismo tiempo hay frames que podrían llegar a la misma millonésima de segundo, esto ya es cuestión de aleatoriedad:**

![image](https://user-images.githubusercontent.com/94720207/236649240-b2ec7114-df07-40ae-8caa-222224adc397.png)



---

### ⭕ Capturando en todos los canales

- El mayor problema de esta técnica es la gran cantidad de información que se puede llegar a capturar, en una zona con alta densidad de APs en diferentes canales y clientes podría llegar a ser abrumante, también se necesita mayor cantidad de Memoria RAM en el dispositivo que esté capturando ya que el rate de captura y el buffer será más elevado que con menos canales o un solo canal. 
- La gran ventaja es que cuando se escanean todos los canales y cuanto más tiempo se dedica al escaneo, más probable es que se encuentren problemas e incidencias de seguridad no solo en los canales que se están utilizando, sino en todos los canales activos en el espacio aéreo.
- Por ejemplo, quizás un cliente se está tratando de conectar a un SSID incorrecto en una red completamente ajena a la nuestra, que port alguna razón, hace interferencia dentro del espacio geográfico de nuestra señal WiFi. En este escenario de puede capturar el intento de autenticación que hará a un SSID ajeno. 
- Otro ejemplo, es para capturar 4-way-handshakes en todos los canales y SSIDs disponibles de manera simultánea. 

Para este método se pueden fabricar adaptadores custom que utilicen hubs usb y varios adaptadores:

También existen adaptadores especializados construídos específicamente para este propósito como el `WiFi Coconut` de `Hak5`:

![image](https://user-images.githubusercontent.com/94720207/236649853-a4f59d2a-095e-4a82-8c58-91a018bf6c61.png)
![image](https://user-images.githubusercontent.com/94720207/236649882-659a49f6-0aab-42aa-aac3-8e5505086e65.png)

Y también se pueden contruír adaptadores custom:

![image](https://user-images.githubusercontent.com/94720207/236649892-93d12bbd-b0e7-48c1-bdb0-0e3def64457b.png)

---

### ❓ Selección correcta de canales de captura

- **¿Cómo decide uno qué hacer? ¿escanear todos los canales, un conjunto de canales o un solo canal?**

La elección debe basarse en las razones por las que se están capturando tramas. Por ejemplo, si una estación tiene problemas para conectarse, es posible que desee escanear todos los canales para capturar cualquier "solicitud de sondeo" de esa estación. Podría estar buscando SSID incorrectos. Al escanear todos los canales, se podrá recopilar más información sobre la forma en que esta estación intenta conectarse. También se debe decidir escanear solo los canales utilizados por los AP que se encuentran dentro de ese espacio para diagnosticar el problema de conectividad. También se podría decidir escanear solo el canal utilizado por el AP que se encuentra físicamente más cerca de la estación con problemas de conectividad. No hay una respuesta absoluta.

- **Para un mejor entendimiento hice una sencilla tabla para identificar y darse una idea de cada escenario:**

| **Escenario de Análisis**                                    	| **Canales Involucrados** 	| **Antenas Necesarias** 	|
|--------------------------------------------------------------	|--------------------------	|------------------------	|
| **Análsis de tráfico en un AP**                              	| 1                        	| 1                      	|
| **Búsqueda de retransmisiones en un canal**                  	| 1                        	| 1                      	|
| **Análisis de log-in en un SSID**                            	| 1                        	| 1                      	|
| **Análisis de log-in en todos los SSID y/o canales**         	| 2 - 14                    | 2 - 14                  |
| **Búsqueda de Beacons en un canal**                          	| 1                        	| 1                      	|
| **Búsqueda de Beacons en canales 2.4 GHz: 1, 6 y 11**        	| 3                        	| 1 _Hopping_            	|
| **Búsqueda de Beacons en todo el espectro 2.4 GHz**          	| 14                       	| 1 _Hopping_            	|
| **Análisis de Roaming entre 2 APs (en diferentes canales)**  	| 2                        	| 2                      	|
| **Análsiis de Roaming entre 3 APs (en diferentes canales)**  	| 3                        	| 3                      	|
| **Análsiis de todo lo que ocurre en el espectro de 2.4 GHz** 	| 14                       	| 14                     	|
| **Análisis o Auditoría de 10 Canales en la Banda de 5 GHz** 	 | 10                       	| 10                     	|
| **Análisis o Auditoría de 25 Canales en la Banda de 5 GHz** 	 | 25                       	| 25                     	|

---

### ⭕ Varios Canales con `Infraestructure` o `Dynamic`

Como se ha mencionado antes estos métodos no son los más accesibles, pero si son mucho más sencillos y presentan ventajas frente a los mobile. En este caso en su mayoría de veces no hay que pensar tanto y hacer tantas configuraciones como en sistemas custom, en cambio, ya todo está preparado para catpurar con un par de clicks. 

- En caso de `Infraestructure` como `Ruckus Smartzone` solo basta tener acceso al Dashboard y empezar la captura con todos los APs involucrados simultáneamente, incluso se puede crear una configuración avanzada donde se pueda hacer stream de todos los APs requeridos en tiempo real, sin importar la cantidad de canales o la banda.

**En el siguiente ejemplo se capturan 5 canales diferentes de la banda 5 GHz, los cuales se encuentran como vecinos y así poder capturar todos los eventos de esa red, incluyendo todos los eventos de roaming y autenticación:**

![image](https://user-images.githubusercontent.com/94720207/236650658-128c558d-7c54-4c65-a84e-72151aab2c48.png)

---

<!-- 

FIN DE CAPITULO :D

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## Capturando en Escenarios con roaming













![image](https://user-images.githubusercontent.com/94720207/236647132-f6c643ea-93c9-41ec-a472-03d260033d00.png)








































