# 👹 `CANTO IV`: Physical Layer = PHY

El término `PHY` se utiliza comúnmente como una abreviatura de `physical layer` en el ámbito de las redes y las telecomunicaciones. La capa física o `physical layer` es la capa más baja en el modelo de referencia OSI y se encarga de **la transmisión y recepción de señales físicas a través del medio de comunicación, como cables o el aire en el caso de las redes inalámbricas.**

La `physical layer` es fundamental para un análisis 802.11 completo y de hecho muchos olvidan esta capa, hay que recordar que el WiFi se basa principalmente en las capas 1 y 2 del modelo OSI. La `physical layer` es responsable de cosas como:

- Modulación de la señal
- Potencia de transmisión
- Ancho de banda
- Frecuencia
- Codificación
- y otros aspectos relacionados con la transmisión y recepción de datos... 

Un ingeniero CWAP necesita entender y analizar estos parámetros físicos para diagnosticar problemas de rendimiento, interferencias, cobertura deficiente y otros problemas relacionados con las redes inalámbricas.

La palabra `PHY` en sí misma se refiere a la capa física en general, pero en el contexto de las redes inalámbricas, **se utiliza más comúnmente para hacer referencia a las especificaciones y estándares de comunicación física inalámbrica, como el estándar `IEEE 802.11` como:**

- 802.11a
- 802.11b
- 802.11g
- 802.11n
- 802.11ac
- 802.11ax

Estos estándares definen aspectos técnicos como las frecuencias utilizadas, las tasas de transmisión, los métodos de modulación, las técnicas de acceso al medio y otros detalles relacionados con la transmisión inalámbrica.

## 💀 `PHY Layer`: Services

Las comunicaciones `Wireless 802.11` son similares a las comunicaciones encontradas en `Ethernet 802.3` en el sentido de que utilizan `Frames` en la `MAC Sublayer` de la `Data Link Layer 1` y utilizan servicios y señalización `PHY` en la `Physical Layer 1 (PHY)`. Sin embargo, debido a la naturaleza ilimitada y compartida del medio utilizado por WiFi, que son `Radiofrencuencias (RF)` en el aire, existen algunas diferencias con Ethernet.

Muchas personas asumen que lo único que necesitan entender acerca de la transmisión inalámbrica es la `contención / contention` y el `ruido / noise`, pero esto no es cierto.

- **El uso de las sublayers `MAC` y `PHY` en las comunicaciones WiFi está definido dentro del `estándar 802 en la parte 11 : MAC & PHY Specifications`, también conocido como `802.11-2020` en su versión más reciente.**

Existen muchas funciones en la capa física que se necesitan comprender para ser un `CWAP Engineer` exitoso. Los `PHY Services` se explican en la `cláusula 9 de 802.11-2020`, especificaciones de `PHY Services` y los detalles de las `PHY Operations` para cada `PHY` específico se definen en las `cláusulas 15 a 23`, que incluyen:

- **`DSSS PHY`**
- **`HR/DSSS PHY`**
- **`OFDM PHY`**
- **`ERP PHY`**
- **`HT PHY`**
- **`VHT PHY`**
- **`HE PHY`**
- **`DMG PHY`**
- **`TVHT PHY`**
- **`S1G PHY`**

Para entender el funcionamiento de un `PHY` específico, es necesario comprender los `PHY Services` definidos en la `cláusula 8` y los detalles del PHY en la **cláusula correspondiente.** Por ejemplo, el `PHY VHT = 802.11ac : WiFi5` se encuentra en la `cláusula 21 del estándar 802.11-2020`. Para entenderlo completamente, es necesario comprender los `PHY Services` definidos en la `cláusula 8` y los detalles específicos del `PHY `definidos en la `cláusula 21`.

- Según el estándar `802.11-2020`:

    - Los servicios `PHY` proporcionados a la `MAC Layer` se describen en esta cláusula. Se definen diferentes `PHY` como parte de este estándar. Cada `PHY` puede consistir en las siguientes funciones de protocolo:

        - a) Una función que define un **método para mapear los `MPDU` en un formato de enmarcado adecuado para enviar y recibir datos de usuario e información de gestión entre dos o más `STAs`** (Estaciones de Trabajo Inalámbricas).
        - b) Una función que **define las características y un método para transmitir y recibir datos a través de un medio inalámbrico entre dos o más STAs.**

La siguiente sección de este CANTO III se revisan más a detalle los servicios especificados en la cláusula 8 y utilizados en los servicios WiFi.

---

### 🟢 `PHY Services` a fondo!


Cuando una STA necesita transmitir, prepara la transmisión comenzando en la parte superior del modelo OSI y pasa la información a través de varias capas y subcapas, formateándola y encriptándola en el proceso. Cuando esa información llega a la capa 2, se le agrega la información de la subcapa MAC, como la dirección MAC. La subcapa MAC se refiere a los tramas 802.11 como la Unidad de Datos del Protocolo MAC o MPDU que se pasará a la capa PHY. Cuando se recibe un trama, cambiando la direccionalidad de los tramas, estos viajan hacia arriba en el modelo OSI en lugar de hacia abajo. La capa física se refiere al trama MAC (MPDU) como una Unidad de Datos del Servicio de la Capa Física o PSDU. Ambos términos son correctos.

- El término que debes usar para describir la carga útil encapsulada debe reflejar la subcapa desde la cual se recibe el tráfico y la dirección de recepción.

Las transmisiones deben ser referidas como MSDU a medida que pasan a través de la subcapa MAC de la Capa 2 y se convierten en un MPDU, y como PSDU al pasar por la Capa PHY.
Puede ser confuso, solo recuerda: ambos términos se refieren a las cargas útiles de la capa 3 en adelante, ya que están encapsuladas en la transmisión o recepción por la Capa 1 y la Capa 2.
Cuando la Capa PHY recibe el MPDU de la subcapa MAC, se agregan el preámbulo adecuado y el Encabezado PHY a los materiales para crear la Unidad de Datos del Protocolo de la Capa Física o PPDU. La Capa MAC se comunica con la Capa PHY a través de "primitivas" a través de un Punto de Acceso de Servicio (SAP).

- Primitivas: Un conjunto de "comandos instructivos" o "instrucciones fundamentales".

Cuando la subcapa MAC indica que así se haga, la Capa PHY prepara los MPDU para la transmisión. La Capa PHY también pasa los tramas recibidos a la subcapa MAC al recibirlos del medio inalámbrico y determinar que el trama está destinado a la estación local.































































PHY

802.11 Radio information 



El campo "802.11 radio information" que aparece en los frames capturados en modo monitor en Wireshark no está en el contenido de los frames de manera explícita en formato HEX, sino que es información que se obtiene de las capas físicas y de enlace de la red inalámbrica.

Cuando un adaptador de red está en modo monitor, es capaz de capturar todas las tramas que se transmiten a través del medio inalámbrico en un determinado canal. El adaptador de red recibe estas tramas y las transfiere a Wireshark para su análisis y decodificación.

La información contenida en el campo "802.11 radio information" es información que se obtiene de las señales inalámbricas transmitidas por los dispositivos de la red, como el nivel de señal, la frecuencia del canal, la modulación utilizada, la velocidad de transmisión, entre otros.

Es importante tener en cuenta que esta información no se transmite en el cuerpo del frame de manera explícita, sino que se obtiene a partir del análisis de las señales de radio. Por lo tanto, la capacidad de capturar y analizar esta información depende de la capacidad del adaptador de red y de la calidad de la señal recibida.




El frame contiene información que se utiliza para transportar los datos, como la dirección de origen y destino, la información de control, el contenido de los datos, entre otros. Sin embargo, la información que se muestra en el campo "802.11 radio information" en Wireshark no se transmite explícitamente en el cuerpo del frame.

En cambio, esta información se obtiene a partir del análisis de las señales de radio que se utilizan para transmitir el frame. Cada vez que se transmite una señal de radio, esta contiene información sobre la frecuencia, la potencia, la modulación, entre otros parámetros que se utilizan para transmitir la señal. Estos parámetros se pueden analizar y utilizar para determinar información adicional sobre la transmisión.

Por ejemplo, el nivel de señal (RSSI) se puede medir midiendo la potencia de la señal recibida. La relación señal-ruido (SNR) se puede calcular midiendo la relación entre la potencia de la señal recibida y el nivel de ruido en el canal. La duración de la transmisión se puede medir midiendo el tiempo que dura la señal de radio transmitida... Es decir, este cáclulo lo hace directamente el software, no es que viaje por el aire con la demás información.

es importante tener en cuenta que algunos de los parámetros que se muestran en el campo "802.11 radio information" se basan en información que se transmite en la señal de radio. Por ejemplo, la frecuencia y el canal en el que se está transmitiendo la señal se transmiten en la señal de radio y se pueden obtener directamente de la señal capturada por el adaptador de red en modo monitor.


Otros parámetros, como el SNR, la potencia de la señal, la modulación, entre otros, se obtienen a partir del análisis de las señales de radio. Estos parámetros no se transmiten explícitamente en la señal de radio, pero se pueden calcular a partir de la información contenida en la señal, como la forma de onda, el patrón de modulación, entre otros.

El campo "802.11 radio information" en Wireshark es un conjunto de datos que se muestra en la sección de detalles de los frames capturados en modo monitor en redes inalámbricas 802.11. Esta información se obtiene de la capa física de la red, es decir, de las señales de radio que se transmiten entre los dispositivos de la red inalámbrica.

El campo "802.11 radio information" incluye información como el canal utilizado para la transmisión, la tasa de transmisión, la modulación utilizada, el nivel de señal recibido (RSSI), la relación señal-ruido (SNR), la calidad de la señal (Signal Quality), el tiempo de duración de la transmisión (Duration), entre otros.

La información contenida en este campo puede ser muy útil para analizar el rendimiento de la red inalámbrica, detectar problemas de interferencia, identificar dispositivos en la red, entre otros. Sin embargo, es importante tener en cuenta que esta  información no se transmite explícitamente en el cuerpo del frame, sino que se obtiene a partir del análisis de las señales de radio.



### Radiotap Header

- [Display Filter Reference: IEEE 802.11 Radiotap Capture header](https://www.wireshark.org/docs/dfref/r/radiotap.html)


### 802.11 Radio Information




- [Display Filter Reference: 802.11 radio information](https://www.wireshark.org/docs/dfref/w/wlan_radio.html)




















































































https://wiki.wireshark.org/SampleCaptures














































WiFi beacon pollution, overhead per SSID

![image](https://user-images.githubusercontent.com/94720207/236646936-83418391-38a4-4d86-b337-c5459ded967b.png)




