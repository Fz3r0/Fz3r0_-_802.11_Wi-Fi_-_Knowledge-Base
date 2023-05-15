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

- **Su objetivo principal es permitir a los dispositivos descubrir y comunicarse entre sí sin necesidad de una infraestructura de servidor DNS (Domain Name System) centralizada.**  

En lugar de utilizar servidores DNS tradicionales, mDNS utiliza el envío de paquetes de tipo multicast para permitir que los dispositivos anuncien y descubran servicios disponibles en la red local.

El protocolo mDNS se basa en la resolución de nombres mediante el uso de nombres de host y el sufijo especial **`.local`**. Los dispositivos que implementan `mDNS` **anuncian sus servicios enviando mensajes de `Anouncment` a una dirección multicast específica `224.0.0.251`. Estos mensajes contienen información sobre los servicios que ofrecen y cómo acceder a ellos.

- **Cuando un dispositivo quiere descubrir servicios en la red local, envía consultas mDNS a la misma dirección multicast `224.0.0.251`. Los dispositivos que ofrecen servicios responden a estas consultas anunciando sus servicios y proporcionando la información necesaria para acceder a ellos.

### Puntos clave de los mDNS:

- `mDNS (Multicast DNS` es un protocolo `multicast` de descubrimiento de servicios en redes locales.
- Permite que los dispositivos descubran y se comuniquen entre sí sin un servidor DNS centralizado.
- Utiliza el puerto `UDP` `5353` para la comunicación.
- Los anuncios y consultas se envían y reciben a través de la **dirección multicast** `IPv4 224.0.0.251` y la **dirección multicast** `IPv6 FF02::FB`.
- Opera en `Layer 2 Data Link` y `Layer 3 Network` del modelo OSI.
- Se basa en mensajes `DNS` para la **resolución de nombres**.
- **Se utiliza principalmente en redes locales pequeñas y domésticas.**
- Facilita la detección automática de servicios y recursos en la red sin configuraciones manuales. Esto lo convierte en un protocolo cómodo, sin embargo, ** NO ES TAN EFICIENTE**
- Los dispositivos envían y reciben paquetes en el puerto 5353 para descubrir y comunicarse entre sí.

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

Cuando un celular se conecta a una red, utiliza el protocolo mDNS para buscar y descubrir dispositivos disponibles en esa red. La Chromecast, en este caso, anuncia sus servicios mediante anuncios mDNS.

Aquí está el proceso detallado:

1. La Chromecast, desde el instante que se se conecta a la red, envía anuncios mDNS anunciando sus servicios disponibles, en su query incluye sus servicios `_googlecast._tcp.local`.
2. El celular envía una consulta multicast utilizando `mDNS` para buscar servicios específicos, como `_googlecast._tcp.local`.
3. Estos anuncios son recibidos por **TODOS** los dispositivos en la red que estén escuchando en la dirección multicast correspondiente `224.0.0.251`. Es decir, prácticamente cualquier `Smartphone`, `PC`, `Macbook`, `IoT` o cualquier dispositivo moderno con aplicaciones multimedia como `Youtube`, `Netflix`, `Impresoras`, `Multimedia`, etc, etc...
4. El celular, al recibir los anuncios `mDNS` de la `Chromecast`, obtiene información sobre la Chromecast, como su `dirección IP`, `nombre de host` y los `servicios` que ofrece.
5. Con esta información, el celular sabe que existe una Chromecast en la red y tiene la dirección IP necesaria para **comunicarse directamente con ella.** Es decir: Para lo único que se usan los `mDNS` es para descubrir, después el tráfico es `unicast`
6. **A partir de ese momento, el celular puede establecer una conexión con la Chromecast utilizando su dirección IP y utilizarla para enviar contenido o controlarla.**
