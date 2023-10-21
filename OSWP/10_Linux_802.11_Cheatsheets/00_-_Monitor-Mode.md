<!-- 

Y ARRANCAN!!!


<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Hacia el Infierno del `OSWP`: <br> `Offensive Security Wireless Professional` 📡🦈💀  

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/7c94fd0b-296e-4884-a604-c6db7c386ca6) <br>
_Writeup y bitácora para la certificación **CWAP-402** de **CWNP (Certified Wireless Network Professional)**_ <br>
_por @ **Fz3r0 💀** (CWNA)_

---

<br><br>

## 🗂️ `ÍNDICE`

## 👹 `CANTO I:`  Monitor Mode

Las comunicaciones 802.11 Wireless y las 802.3 Ethernet, aunque similares, no son iguales. Por ejemplo, no hay un puerto solo del plano de `management` en un switch al cual conectarse y simplemente capturar cada `frame` que se envía al medio.

El tráfico inalámbrico no se segmenta utilizando un switch como en Ethernet 802.3, pero si se puede segmentar, por ejemplo utilizando una frecuencia diferente, más comúnmente llamada "un canal". En Wireless las transmisiones están en el aire "volando" y no están contenidas dentro de un conjunto de cables, switches y routers. **Este es el claro ejemplo de la diferencia entre una `LAN (Ethernet / IEEE 802.3)` y una `WLAN (WiFi / IEEE 802.11)`**

Para capturar transmisiones inalámbricas o `802.11 Frames`, se debe utilizar software de análisis de protocolo o `Protocol Analyzer` y un adaptador de red inalámbrico o `Network Adapter` que funcione con el software, es decir, `hardware` y `software` capaz de capturar y procesar la captura de 802.11 Frames. 

El `Network Adapter` debe estar en `Monitor Mode`. El modo monitor significa que el adaptador inalámbrico se ha configurado para **capturar el tráfico que está destinado a cualquier dirección MAC y no solo a la suya.** Esto se logra mediante el uso de un `driver` requerido que funciona no solo con el adaptador sino también con su software de análisis de protocolo.

## 💀 `Monitor Mode` & `Promiscous Mode`

Es importante entender que `Monitor Mode` y `Promiscous Mode` no son los mismos conceptos. Para la captura de `Ethernet` solo necesita activar `Promiscous Mode`, sin embargo, para capturar `WiFi` es más complejo y se necesita utilizar tanto `Monitor Mode` y `Promiscous Mode`.

### ⭕ `Promiscous Mode`

**Este modo se debe tener encendido siempre que se quiera capturar frames, ya sea `Ethernet` o `WiFi`** _(De hecho los sniffers como Wireshark lo tienen activado por default)_. Es un modo en el que un adaptador de red `inalámbrico` o `cableado` se configura para capturar todos los paquetes que se envían en la red, **independientemente de si están destinados al adaptador o no.** Esto significa que, **en el `Promiscuous Mode`, se pueden capturar paquetes que no están destinados a nuestro dispositivo**, lo que es útil para el análisis de red. 

El `Promiscuous Mode` permite a una interfaz o adaptador de red **"escuchar"** todo el tráfico que pasa por una interfaz _(puede ser Ethernet o una antena WiFi)_, aunque no esté dirigido específicamente a ese dispositivo o aunque no se pertenezca a esa subnet o VLAN, mientras haya tráfico pasando por esa interfaz se podrá escuchar. 

- **`IMPORTANTE`**: NO se puede usar el modo promiscuo para capturar `tráfico unicast` entre dos dispositivos que no son el dispositivo en modo promiscuo, ya que ese determinado tráfico no se transmite directamente por la interfaz donde se está escuchando, sino que en otras 2 interfaces aparte que están transmitiendo unicast ya sea por medio de un switch o directamente peer-to-peer (punto a punto), ya que es la "conversación" unicast entre 2 dispositivos ajenos.**

Existen diferencias de `Modo` entre capturar en WiFi o Ethernet:

- Para capturar `Ethernet 802.3` solo es necesario conectar el cable ethernet a la interfaz, encender `Promiscous Mode` y ya se podrá capturar tráfico ¡Así de fácil!
- Para capturar `WiFi 802.11` es un poco más complejo, ya que además de tener activado el `Promiscous Mode`, se necesitan herramientras de hardware adicional, también se deben confgurar los drivers para una función diferente, como el `Monitor Mode`. Tanto el Sistema Operativo, Hardware _(adaptadores WiFi)_ y Software _(Protocol Analyzers & Sniffers)_ deben ser compatibles con `Monitor Mode`

---

### ⭕ `Monitor Mode`

Es un modo especial en el que un adaptador de red inalámbrico se configura para capturar todo el tráfico de la red inalámbrica, incluyendo los paquetes dirigidos a direcciones MAC que no sean la del adaptador en sí _(Similar al concepto del `Promiscous Mode` pero en Wireless, ¡pero el `Promiscous Mode` sigue siendo requerido!)_

En otras palabras, en Monitor Mode, el adaptador de red inalámbrico captura todos los paquetes que se envían en la red inalámbrica, independientemente de si están destinados al adaptador o no. **Esto permite capturar paquetes que no están destinados a nuestro dispositivo, lo que es útil para analizar todo el tráfico de la red inalámbrica, incluyendo el tráfico que no está dirigido directamente a nuestro dispositivo.**

Es decir, si queremos capturar todos los frames que se envían en una red inalámbrica, necesitamos usar un adaptador de red inalámbrico WiFi 802.11 en Monitor Mode. Por otro lado, si queremos capturar todos los paquetes que se envían en una red cableada Ethernet 802.3, podemos usar un adaptador de red cableado en Promiscuous Mode. Sin embargo, si queremos capturar todos los paquetes que se envían en una red mixta inalámbrica y cableada, necesitaríamos usar tanto un adaptador de red inalámbrico en Monitor Mode como un adaptador de red cableado en Promiscuous Mode para asegurarnos de capturar todos los paquetes.

Hay que recordar que, el tráfico WiFi en el aire puede ser capturado por cualquiera que esté a su alcance y tenga las herramientas adecuadas _(por ello la importancia de la encriptación y otros procesos de seguridad)_

![image](https://user-images.githubusercontent.com/94720207/231614242-d43e9592-73e2-4a22-9417-b8d8e630fdd6.png)

---

<div align="center">

┌═════════════════════┐<br>
| [█ █ █   << BACK TO TOP >>   █ █ █](https://github.com/Fz3r0/Fz3r0_-_BlackShark/blob/main/OSWP/Hacia_el_infierno_del_OSWP.md#%EF%B8%8F-%C3%ADndice)                |<br>
└═════════════════════┘<br>

 </div> 

