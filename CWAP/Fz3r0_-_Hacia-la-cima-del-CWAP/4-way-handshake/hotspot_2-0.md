# Hotspot 2.0 (Passpoint)

### Información Clave de HS2.0:

- La `Wi-Fi Alliance (WFA)` lanzó la especificación `IEEE 802.11u` (también conocida como `Hotspot 2.0`) en febrero de 2011. 
- Uno de los principales objetivos de la tecnología Hotspot 2.0 es **simplificar el acceso de los dispositivos móviles a las redes Wi-Fi de manera segura**.

### Componentes principales de la tecnología son:

- Descubrimiento y selección automática de redes
- Autenticación segura
- Online sign-up (OSU)
- Gestión de políticas

### Diferencia entre releases:

- `Hotspot 2.0 Release 1` se centra en los componentes de descubrimiento y selección automática de redes, y autenticación segura.
- `Hotspot 2.0 Release 2` abarca la especificación de los componentes de Online sign-up y gestión de políticas.

### Detalles de Hotspot 2.0:

La especificación de HotSpot 2.0 proporciona un descubrimiento automático de redes para Wi-Fi, una funcionalidad que ya es familiar en las redes móviles. Esta funcionalidad automatiza el descubrimiento correcto de SSID y simplifica la autenticación, lo que incrementa el uso de Wi-Fi y la descarga de datos (data offloading).

HS2.0 utiliza métodos EAP para la autenticación y WPA2 para el cifrado de los datos.

La funcionalidad se basa en que el AP (punto de acceso) anuncia o transmite una lista de dominios NAI Realm de socios de roaming con los que el AP/Proveedor de Servicios tiene un acuerdo de roaming. La funcionalidad es similar a la de las redes móviles. Cuando un dispositivo compatible con HS2.0 intenta conectarse a una red Wi-Fi, lee la lista de dominios NAI Realm anunciada por el AP y busca el dominio NAI Realm de su proveedor de Wi-Fi doméstico (Home Wi-Fi SP NAI Realm). Si encuentra el dominio NAI de su proveedor, el dispositivo móvil empareja la lista NAI Realm con el de su proveedor y comienza el proceso de autenticación con el método EAP correcto.

HS2.0 también requiere cambios en el dispositivo. Las principales funcionalidades son escanear diferentes SSID anunciados con sus dominios NAI Realm, emparejarlos con el dispositivo, incluyendo el NAI Realm, y luego iniciar la autenticación. Además, HS2.0 requiere cifrado WPA2-Enterprise para el AP y el dispositivo, en lugar de TKIP o WEP. De hecho, HS2.0 no permite el uso de WPA o WEP.

Aunque HS2.0 soporta todo tipo de dominios NAI Realm, se recomienda que los operadores móviles (MNOs) utilicen el dominio NAI Realm definido por 3GPP para el uso de Wi-Fi (FQDN: wlan.mnc.mcc.3gppnetwork.org), ya que la generación de este dominio NAI puede crearse automáticamente a partir de la tarjeta (U)SIM en el dispositivo móvil. Esto facilita el uso, ya que no se necesita interacción del usuario para completar esta tarea.

La especificación de HS2.0 incluye soporte para EAP-SIM y EAP-AKA, mencionados anteriormente, así como EAP-TTLS y EAP-TLS. La especificación exige que un proveedor de HotSpot 2.0 (MNO) con infraestructura SIM/USIM soporte credenciales SIM/USIM y los métodos EAP asociados, y deberá soportar al menos uno de los siguientes: credenciales de nombre de usuario/contraseña o certificado, y su método EAP asociado.

Lo más importante de HS2.0 es que eleva el Wi-Fi al mismo nivel que las redes móviles en términos de seguridad y facilidad de uso. Esto incrementará enormemente el uso de Wi-Fi.



## Operación Básica de Hotspot 2.0

Un dispositivo móvil compatible con Hotspot 2.0 se comunica con la infraestructura Wi-Fi compatible con Hotspot 2.0 (Access Points) para descubrir el SSID (Service Set Identifier) de la red y asociarse a él.

Luego se conecta de manera segura a ese SSID presentando sus credenciales de acceso. Tras una autenticación exitosa, el dispositivo se conecta de forma segura a Wi-Fi con Hotspot 2.0 habilitado. Si un dispositivo móvil no tiene credenciales preexistentes, no se asociará automáticamente a la red WLAN de Hotspot 2.0. En su lugar, el usuario será notificado de los servicios de Online Signup (OSU) si están disponibles. Si el usuario elige inscribirse en uno de estos servicios OSU, será dirigido a un portal de registro a través de la red Hotspot 2.0 onboarding WLAN. Después de una autenticación exitosa, al usuario se le proporcionará un objeto de gestión basado en los estándares de Hotspot 2.0, conocido como Per-Provider Subscription Management object (PPS-MO). El usuario será desconectado de la red onboarding WLAN y reconectado a la red de acceso segura de Hotspot 2.0.

La tecnología Hotspot 2.0 permite a los usuarios hacer roaming sin interrupciones entre la red Wi-Fi del proveedor en casa y la red Wi-Fi visitada en ubicaciones remotas. Un proveedor de Wi-Fi puede asociarse con varios socios de roaming para proporcionar acceso Wi-Fi a los suscriptores de los socios. Los socios de roaming pueden incluir MSOs, MNOs, operadores de línea fija, lugares públicos, empresas y básicamente cualquier entidad que tenga activos Wi-Fi, como se muestra en el siguiente diagrama.

![image](https://github.com/user-attachments/assets/2b9e5930-e352-4a4c-a3c6-8962ba76df1c)

La red onboarding WLAN para Hotspot 2.0 puede ser una WLAN abierta o una WLAN segura. La onboarding WLAN habilita solo la autenticación del lado del servidor, mientras que el lado del cliente permanece anónimo. El proveedor de servicios OSU utiliza PPS-MO para aprovisionar los parámetros de política necesarios, como el intervalo de actualización de la suscripción, el límite de uso de datos, etc. 

En una topología de red basada en Hotspot 2.0, cualquier entidad que opere la infraestructura Wi-Fi puede denominarse Wi-Fi operator, mientras que la entidad que posee la base de datos de usuarios puede denominarse Identity Provider. Un Wi-Fi operator también puede actuar como Identity Provider y puede asociarse con uno o más Identity Providers externos.

## Key points de Hotspot 2.0 

Hotspot 2.0 (también conocido como Passpoint®, el nombre registrado de la solución de la Wi-Fi Alliance) tiene como objetivo mejorar la experiencia de los usuarios móviles al seleccionar y unirse a un Wi-Fi hotspot proporcionando información a la estación antes de la asociación.
Hotspot 2.0 está enfocado en permitir que un dispositivo móvil descubra automáticamente APs que tienen un acuerdo de roaming con la red de origen del usuario (o con el servicio del operador celular) y luego se conecte de manera segura.
Hotspot 2.0 puede aprovecharse para configurar un servicio de guest hotspot, ofreciendo acceso público a los usuarios a través de sus redes Wi-Fi. Esto simplifica el proceso de acceso a redes Wi-Fi para una variedad de dispositivos con capacidades Wi-Fi, como APs, smartphones, entre otros.
Las redes Hotspot 2.0 son creadas por operadores de Wi-Fi y proveedores de identidad.
Un operador de Wi-Fi despliega y opera una red de acceso de APs accesibles al público o para invitados.
Un Identity Provider proporciona servicios de red y opera la infraestructura AAA requerida para autenticar a los suscriptores.
El operador de Wi-Fi y el Identity Provider pueden ser la misma entidad o entidades diferentes.
Los Service Providers (SPs) que se pueden acceder en un hotspot se denominan socios de roaming para ese hotspot.
El Identity Provider que realiza la autenticación puede proporcionar a sus suscriptores conectividad AAA a su red a través del hotspot.
Los Identity Providers se anuncian utilizando información de la red celular 3GPP, una lista de NAI realm, o una lista de consorcio de roaming.
Puede haber uno o más Identity Providers por red de acceso Hotspot 2.0.
El roaming Wi-Fi se aplica en cualquier momento en que un dispositivo móvil no vea un AP perteneciente a su proveedor de red de origen.
Un usuario podría hacer roaming en una red Wi-Fi que esté al otro lado de la ciudad o del mundo.
Los socios de roaming pueden incluir MSOs, MNOs, operadores de línea fija, lugares públicos, empresas y básicamente cualquier otra entidad que posea activos Wi-Fi.
El roaming puede realizarse con dispositivos de modo dual (smartphones) o dispositivos solo Wi-Fi como tablets y laptops.










# Operator y Service Provider.

Cada AP que proporciona Hotspot 2.0 debe estar configurado con los parámetros del **service profile** y del **operator** correspondiente. No obstante, **un solo "Operator" puede ofrecer simultáneamente su servicio a múltiples "Service Providers"**, lo que permite que diferentes providers utilicen la misma infraestructura de red para ofrecer servicios a sus usuarios. 

- Es decir, el administrador de la red WLAN físicamente dentro del Venue es el **"Operator"** (ej. `Fz3r0 Wi-Fi Corp.`) quien es capaz de ofrecer el servicio de Hotspot 2.0 a diferentes "Service Providers" (ej. `Telmex`, `Pillo fon`, `Telcel`, `Movistar`, etc...).

### Operator 

- Son los dueños de un conjunto de APs/infraestructura WLAN compatible con Hotspot 2.0. 
- Los Operators son responsables de la gestión de los elementos físicos de la red, como la implementación, administración y mantenimiento de los APs
- Un operator puede revender su servicio Hotspot 2.0 a varios Service Providers.
- Ejemplo de Operator: `Fz3r0 Wi-Fi Corp.`

### Service Provider 

- Se encargan de gestionar las subscriptions de los usuarios y la facturación.
- Mientras que los operators manejan la infraestructura física de la red, los service providers se centran en los aspectos relacionados con los usuarios, como la autenticación y la administración de las cuentas de sus subscribers.
- Ejemplo de Service Provider: `Telmex`, `Pillo fon`, `Telcel`, `Movistar`, etc...





















# 3GPP : Identity Provider Network Identifier

El dominio WLAN.mnc480.mcc311.3gppnetwork.org es parte de la arquitectura de red de 3GPP (3rd Generation Partnership Project), específicamente relacionada con redes móviles. 

Aquí tienes un desglose de sus componentes:

- WLAN: Esto indica que el dominio está asociado con Wireless Local Area Networks, que a menudo se refiere a redes Wi-Fi.
- mnc480: Esto se refiere al Mobile Network Code (MNC), que se utiliza para identificar a un operador de red móvil específico dentro de un país. El número "480" indica un operador específico.
- mcc311: Esto representa el Mobile Country Code (MCC), que identifica el país de la red móvil.

---

### smartzone 3gpp

El controller soporta dos flujos de llamadas diferentes para la authentication y authorization:

Una solución basada en el estándar 3GPP, donde la authentication y la service authorization se realizan por separado.
Una solución propietaria donde la authentication y authorization están combinadas. Esta guía enumera todos los interface messages y los RADIUS VSAs utilizados entre el controller y el AAA.


---




## Key points of Hotspot 2.0

- Hotspot 2.0 (also known as Passpoint®, the trademarked name of the Wi-Fi Alliance solution) aims to improve the experience of mobile users when selecting and joining a Wi-Fi hotspot by providing information to the station prior to association.
- Hotspot 2.0 is focused on enabling a mobile device to automatically discover APs that have a roaming arrangement with the user’s home network (or cellular carrier service) and then securely connect.
- Hotspot 2.0 can be leveraged to set up a guest hotspot service, offering public access to users through its Wi-Fi networks. It streamlines the process of accessing Wi-Fi networks by a variety of devices that have Wi-Fi capabilities, such as APs, smartphones, and so on.
- Hotspot 2.0 networks are created by Wi-Fi operators and identity providers.
- A Wi-Fi operator deploys and operates an access network of publicly accessible or guest access APs.
- An Identity Provider provides network services and operates the AAA infrastructure required to authenticate subscribers.
- The Wi-Fi Operator and Identity Provider may be the same or different entities.
- The Service Providers (SPs) that can be accessed at a hotspot are referred to as the roaming partners for that hotspot.
- The Identity Provider performing the authentication can provide its subscribers with AAA connectivity to its network through the hotspot.
- Identity Providers are advertised using 3GPP cellular network information, an NAI realm list, or a roaming consortium list.
- There can be one or more identity providers per Hotspot 2.0 access network.
- Wi-Fi roaming would apply anytime a mobile device does not see an AP belonging to its home network provider.
- A user could roam on a Wi-Fi network that is across town or on the other side of the world.
- Roaming partners can include MSOs, MNOs, wireline operators, public venues, enterprises, and basically any other entity that has Wi-Fi assets.
- Roaming can be accomplished with dual mode devices (smartphones) or Wi-Fi-only devices like tablets and laptops.

Hotspot 2.0 networks offer accessibility and mobility, enabling internet access in public areas with secure authentication and roaming capabilities, ensuring safe access and connectivity.

- **With Hotspot 2.0, the client device is equipped by an authentication provider with one or more credentials, such as a SIM card, username/password pair, or X.509 certificate. The device can then query Hotspot 2.0 capable APs to see if it belongs to a visited network that supports roaming with the devices home network.**

Hotspot 2.0 is a program of the Wi-Fi Alliance, and is supported by the Passpoint(™) certification program which ensures APs and client devices comply with the technical specifications. Hotspot 2.0 capabilities are emerging in a series of releases:

1. Hotspot 1.0 came out in June 2012 and was focused on automating network discovery/selection, authentication, and over-the-air security. Other releases will follow in the coming years that will add additional capabilities.
2. Mobile devices with Hotspot 2.0 support are now available in the market. While vendors may choose to introduce new models to enable Hotspot 2.0, these capabilities can be added via software updates in most cases.

"The hassles and risks of connecting to public Wi-Fi will soon be a thing of the past, thanks to Hotspot 2.0."

## Hotspot 2.0 benefits:

- Automates the connection experience at hotspots, providing a secure encrypted airlink for public Wi-Fi networks
- Supports multiple roaming partners over a single SSID

## Hotspot 2.0 Release 1

- Release 1 is focused squarely on over-the-air security and network discovery and selection.
- The key enabling protocols are IEEE 802.11u, along with IEEE 802.1X, selected EAP methods, and IEEE 802.11i. The latter three are part of the WPA2- Enterprise certification program in the Wi-Fi Alliance, and are standard on all smartphones. While the certification is called "WPA2-Enterprise", the end result is a process that is every bit as secure and easy to use as what exists in the cellular world.
- The IEEE 802.11u protocol enables a mobile device to have a dialog with a Wi-Fi AP "pre-association" to determine the capabilities that the network can support.

The two protocols that 802.11u uses to make this happen are:

1. the generic advertisement service (GAS)
2. the access network query protocol (ANQP). 

hese protocols run on top of 802.11 and enable the Hotspot 2.0 experience

![image](https://github.com/user-attachments/assets/69318ac2-bad7-4a1a-a05c-52a96fd08786)


# Resources

- https://www.netwifistore.com/HotSpot-2-0.asp
- https://www.wi-fi.org/discover-wi-fi/passpoint
- https://www.arubanetworks.com/techdocs/ArubaOS_80_Web_Help/Content/ArubaFrameStyles/hotspot/predepoyment_overview.htm
- https://docs.cloud.ruckuswireless.com/ruckusone/userguide/GUID-DD35201E-111A-41D7-B5E8-70AC6F8B00F8.html
- https://www.netwifistore.com/HotSpot-2-0.asp
- https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-1/config-guide/b_wl_17_11_cg/hotspot2.pdf
- https://www.ironwifi.com/help/ruckus-wireless-lan-controller-passpoint-configuration
- https://support.alcadis.nl/Support_files/Ruckus/SmartZone//Manuals/SmartZone%206.0.x/Smartzone%206.0.0.0.1331/SmartZone-6.0.0-Hotspot2.0-Guide-RevA-20210406.pdf
- https://higherlogicdownload.s3.amazonaws.com/HPE/MigratedAttachments/63AF17E3-09CD-4369-A476-CD91D4FA888B-1-WP_PasspointWiFi_062912.pdf
- https://support.alcadis.nl/Support_files/Ruckus/SmartZone//Manuals/SmartZone%206.0.x/Smartzone%206.0.0.0.1331/SmartZone-6.0.0-Hotspot2.0-Guide-RevA-20210406.pdf
- https://docs.commscope.com/bundle/sz-700-accessservicesguide-sz300vsz/page/GUID-99D65A79-6B5F-4A16-895D-3593EA67DA2D.html
- http://repo.darmajaya.ac.id/4779/1/The%20Telecommunications%20Handbook_%20Engineering%20Guidelines%20for%20Fixed%2C%20Mobile%20and%20Satellite%20Systems%20%28%20PDFDrive%20%29.pdf
- https://en.wikipedia.org/wiki/IEEE_802.11u
- https://www.wi-fi.org/system/files/Wi-Fi_CERTIFIED_Passpoint_Deployment_Guidelines_v1.3.3.pdf
- https://support.alcadis.nl/Support_files/Ruckus/SmartZone//Manuals/SmartZone%205.1.x/SmartZone%205.1.2.0.302/SZ100vSZE-5.1.2-AAA-RADIUS-InterfaceGuide-RevA-20190830.pdf
- 
