<!-- 

Y ARRANCAN!!!

ejemplo centrar:

<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Protocols from hell: `mDNS` <br> `Multicast DNS` 📡🦈💀 <br>  

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/7c94fd0b-296e-4884-a604-c6db7c386ca6) <br>
_Writeup y análisis de Protocolo para Seguridad y Troubleshooting**_ <br>
_por @ **Fz3r0 💀**_


## 🗂️ `ÍNDICE`

### 👹 `CANTO I`: Introducción

### 👹 `CANTO II`: Monitor Mode
- ⭕ [**Promiscous Mode**]()
- ⭕ [**Monitor Mode**]() <br><br>
- 💀📝 [**`Fz3r0 Cheatsheet`: ON/OFF Adapter & Network Services**]()
    - 🕵️📡 [ON/OFF Adapter: `x1 Adapter`]()
    - 🕵️📡 [ON/OFF Adapter: `x3 Adapters`]() <br><br>
- 💀📝 [**`Fz3r0 Cheatsheet`: Adapter Modes**]()




## mDNS

El protocolo mDNS (Multicast DNS) es un protocolo de descubrimiento de servicios utilizado en redes locales. 

- **Su objetivo principal es permitir a los dispositivos descubrir y comunicarse entre sí dentro de la `red local` _(dentro del segmento `link.local`)_ sin necesidad de una infraestructura dedicada de servidor `DNS (Domain Name System)` centralizada.**  

En lugar de utilizar `servidores DNS` tradicionales, ¡cosa que sería descabellado en una casa común y corriente!, **`mDNS` utiliza el envío de paquetes de tipo `multicast` para permitir que los dispositivos anuncien y descubran servicios disponibles en la `red local`.** Por eso este protocolo se ha vuelto muy utilizado en ambientes de redes caseras para facilitar el uso de dispositivos como `Chromecast` o `Apple TV`, ya que **cualquier smartphone los puede controlar sin necesidad de ninguna configuración previa por parte del usuario**. _(De ahí uno de sus sinónimos `"Zero-Conf"`)_

El protocolo `mDNS` se basa en la resolución de nombres mediante el uso de nombres de host y el sufijo especial **`.local`**. Los dispositivos que implementan `mDNS` **anuncian sus servicios enviando mensajes de `Anouncment` a una dirección multicast específica `224.0.0.251`. Estos mensajes contienen información sobre los servicios que ofrecen y cómo acceder a ellos.

- **Cuando un dispositivo quiere descubrir servicios en la red local, envía consultas `mDNS` a la misma dirección multicast `224.0.0.251`. 
- **Los dispositivos que ofrecen servicios _(como una Chromecast)_ responden a estas consultas anunciando sus servicios y proporcionando la información necesaria para acceder a ellos.**

---

### Puntos clave de los mDNS:

- `mDNS (Multicast DNS` es un protocolo `multicast` de descubrimiento de servicios en redes locales.
- Permite que los dispositivos descubran y se comuniquen entre sí sin un servidor `DNS` centralizado.
- Utiliza el puerto `UDP` `5353` para la comunicación.
- Los anuncios y consultas se envían y reciben a través de la **dirección multicast** `IPv4 224.0.0.251` y la **dirección multicast** `IPv6 FF02::FB`.
- Opera en `Layer 2 Data Link` y `Layer 3 Network` del modelo OSI.
- Se basa en mensajes `DNS` para la **resolución de nombres**.
- **Se utiliza principalmente en redes locales pequeñas y domésticas.**
- Facilita la detección automática de servicios y recursos en la red sin configuraciones manuales. Esto lo convierte en un protocolo cómodo, sin embargo, **NO ES TAN EFICIENTE**

### Ventajas y Desventajas del protocolo mDNS

---

### Consideraciones a tomar con mDNS en redes Empresariales y Alta Densidad

---

### Consideraciones a tomar con mDNS en redes Wireless 802.11 (WiFi)

---

## CANTO III: Diferentes nombres para mDNS

En ocasiones existen confusiones de este protcolo ya que diferentes vendors lo llaman de diferente manera, pero la finalidad siempre es muy similar en cuanto al descubrimiento de un servicio o dispositivo se refiere. 

Estos vendors implementan el protocolo mDNS en sus dispositivos y servicios para permitir el descubrimiento automático de servicios y recursos en redes locales, facilitando así la interoperabilidad y la configuración sin problemas de los dispositivos conectados en la red. Estos son algunos ejemplos de los más conocidos: 

| **mDNS (sinónimo)** | **Vendor** | **Descripción**                                                                                                                                                                                                                                                                                                                                         |
|---------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Bonjour**         | Apple      | Bonjour es el nombre del servicio de descubrimiento y resolución de nombres de Apple. Se utiliza en entornos de red de Apple para descubrir y configurar servicios como impresoras, dispositivos de red y otros recursos compartidos.                                                                                                                   |
| **Google Cast**     | Google     | Chromecast, Google Home, Googlecast... son dispositivos de transmisión de contenido multimedia fabricados por Google. Utiliza el protocolo mDNS para descubrir y configurar dispositivos Chromecast/Google en la red local. Una vez descubiertos, los usuarios pueden transmitir contenido desde sus dispositivos a través de la red al Chromecast.                                        |
| **Zero-conf**       | Variados   | Zero-conf (configuración cero) es un término general utilizado para describir la configuración automática de dispositivos en una red sin necesidad de una configuración manual. Varios vendedores, como Apple, Google y otros, implementan mDNS y DNS-SD (Service Discovery) para lograr la funcionalidad de zero-conf en sus dispositivos y servicios. |
| **Avahi**           | Variados   | Avahi es una implementación del protocolo mDNS y DNS-SD en sistemas basados en Linux. Se utiliza comúnmente en distribuciones de Linux, como Ubuntu, para permitir la detección automática de servicios y recursos en redes locales.                                                                                                                    |
| **AirPrint**        | Variados   | AirPrint es una tecnología desarrollada por Apple que permite imprimir de forma inalámbrica desde dispositivos iOS y macOS a impresoras compatibles. Utiliza mDNS para descubrir impresoras disponibles en la red local y proporcionar una experiencia de impresión fácil y sin configuración adicional.                                                |
| **UPnP**            | Variados   | UPnP (Universal Plug and Play) es un conjunto de protocolos y tecnologías que permiten que los dispositivos en una red doméstica se descubran y configuren automáticamente. mDNS se utiliza a menudo junto con UPnP para el descubrimiento de dispositivos y servicios en redes locales.                                                                |
| **SLP**             | Variados   | SLP (Service Location Protocol) es un protocolo de descubrimiento de servicios utilizado en varios sistemas operativos y aplicaciones. En algunas implementaciones, como Novell NetWare, se utiliza mDNS como uno de los métodos de descubrimiento en redes locales.                                                                                    |
| **IoT**             | Variados   | IoT (Internet of Things) es un término general para describir dispositivos conectados a Internet que recopilan y comparten datos. En muchos casos, los dispositivos IoT utilizan mDNS como parte de su infraestructura de descubrimiento y comunicación en redes locales para permitir la interoperabilidad entre diferentes dispositivos.              |

## CATNO IV: Frame Exchange de mDNS

La explicación sencilla de cómo funcionan los mDNS con por ejemplo, una Chromecast es la siguiente: 

Voy a proporcionarte una descripción paso a paso del proceso de descubrimiento y reproducción de video entre un celular y un Chromecast, utilizando mDNS y otros protocolos relevantes. Sin embargo, ten en cuenta que la descripción será una representación simplificada y puede haber variaciones dependiendo de las implementaciones específicas de los dispositivos y las configuraciones de red. Aquí está el proceso general:

1. El celular, que está en la misma red local que el Chromecast, envía una consulta mDNS de tipo A para buscar dispositivos Chromecast en la red. La consulta se envía a la dirección multicast 224.0.0.251 con el nombre de dominio "_googlecast._tcp.local".
2. El Chromecast, al recibir la consulta mDNS, responde con un mensaje mDNS de anuncio que contiene su nombre de dominio completo y su dirección IP. El mensaje de anuncio es enviado directamente al celular que realizó la consulta.
3. El celular, ahora con la dirección IP del Chromecast, establece una conexión TCP con el Chromecast utilizando la dirección IP y un puerto específico para la comunicación.
4. El celular envía una solicitud de reproducción de video al Chromecast a través de la conexión TCP establecida. La solicitud puede incluir detalles como la URL del video a reproducir.
5. El Chromecast, al recibir la solicitud de reproducción, procesa la solicitud y establece una conexión UDP con el celular para transmitir el video.
6. El Chromecast envía paquetes de video a través de la conexión UDP al celular, que los recibe y reproduce en su pantalla.
7. En cuanto a los tipos de paquetes y protocolos utilizados en este proceso, aquí tienes una descripción general:

### Proceso de descubrimiento y tranmsisión:

1. Descubrimiento mDNS:
    1. Celular: Envía una consulta mDNS de tipo A con el nombre de dominio "_googlecast._tcp.local" (paquete mDNS de tipo PTR).
    2. Chromecast: Responde con un mensaje mDNS de anuncio que contiene el nombre de dominio completo y la dirección IP del Chromecast.

2. Establecimiento de conexión TCP:
    1. Celular: Establece una conexión TCP con el Chromecast utilizando la dirección IP y un puerto específico.
    2. Chromecast: Responde la conexión TCP y los dispositivos hacen handshake. 

3. Reproducción de video:
    1. Celular: Envía una solicitud de reproducción de video al Chromecast a través de la conexión TCP establecida (paquete TCP).
    2. Chromecast: Procesa la solicitud y establece una conexión UDP con el celular.
    3. Chromecast: Envía paquetes de video a través de la conexión UDP al celular (paquetes UDP).

En cuanto al tráfico posterior al descubrimiento y reproducción, el envío de video en sí mismo generalmente utiliza UDP, ya que este protocolo es adecuado para transmitir datos en tiempo real, como el video. Sin embargo, ten en cuenta que otros protocolos pueden estar involucrados en la comunicación adicional, como TCP para el control de la reproducción, intercambio de metadatos, etc. La combinación de protocolos utilizados dependerá de la implementación específica y los requisitos del servicio o aplicación que se está utilizando.

Es importante mencionar que esta descripción es una simplificación y puede haber variaciones en el proceso real según las implementaciones específicas y las configuraciones de red utilizadas.

### mDNS Technical Frame Exchange

### Fz3r0 Cheatsheet: mDNS

````java
# mDNS wireshark filter: by Port
udp port 5353


````

## Recursos y Fuentes

- [Tall Paul Tech - Multicast Domain Name System (mDNS)](https://youtu.be/v8poeqoeRgE)
- [Networking Institute - Multicast DNS(mDNS) Wireshark Introduction](https://youtu.be/srVklzhATXE)
- [Alberto Lopez - ¿Qué es el DNS (Sistema de Nombres de Dominio)? Servidor y servicio DNS](https://www.youtube.com/watch?v=SRfU9meXlC8)
- [IETF - Multicast Considerations over IEEE 802 Wireless Media
RFC 9119](https://datatracker.ietf.org/doc/rfc9119/)
- [Wikipedia - Multicast DNS](https://en.wikipedia.org/wiki/Multicast_DNS)
