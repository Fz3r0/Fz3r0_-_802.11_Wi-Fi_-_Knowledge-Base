<!-- 

Y ARRANCAN!!!

ejemplo centrar:

<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Protocols from hell: `DNS` <br> `Domain Name Service` 📡🦈💀 <br>  

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/7c94fd0b-296e-4884-a604-c6db7c386ca6) <br>
_Writeup y análisis de Protocolo para Seguridad y Troubleshooting de Redes_ <br>
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




## DNS


---

### Componentes del DNS


Para la operación práctica del sistema DNS se utilizan tres componentes principales:

1. DNS Client
2. DNS Server
3. Authoritative Zone

### DNS Client

Un programa cliente DNS es un fostware que se ejecuta en la computadora del usuario y genera peticiones DNS de resolución de nombres a un servidor DNS. Por lo general vienen instalador por default en cualquier tipo de dispositivo de red como `smartphones`, `tablets`, `PCs`, `IoT`, etc. Y por lo general un usuario no suele configurarlo manualmente, sino que suele ser otorgapo via `DHCP` justo con la `IP Address`, `Gateway Address` y `Subnet Mask`.

### DNS Server

Es el software ejecutado dentro de otra máquinma que contesta las peticiones de los clientes. Los servidores recursivos tienen la capacidad de reenviar la petición a otro servidor si no disponen de la dirección solicitada. Es decir, **un servidor DNS puede depender de otos servidores DNS.** 

Authoritative Server

Es una parte del espacio de nombre de dominios sobre la que es responsable un servidor DNS, que puede tener autoridad sobre varias zonas. (Por ejemplo: subdominio.Wikipedia.ORG, subdominio.COM, etc.)

---

## Operación del DNS en la vida real



![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a594d0a5-ed5b-4f0d-ac30-28afe2f069b1)












### Ventajas y Desventajas del protocolo mDNS

---

### Consideraciones a tomar con DNS en redes Empresariales y Alta Densidad

---

### Consideraciones a tomar con DNS en redes Wireless 802.11 (WiFi)

---






## rDNS - Búsqueda DNS inversa




## CATNO IV: Frame Exchange de DNS

### mDNS Technical Frame Exchange

### Fz3r0 Cheatsheet: mDNS

````java


````



## `Laboratiorio`: DNS

### `Laboratiorio DNS`: Parte 1 - Setup Inicial

El ejercicio es muy sencillo, solo basta de 2 pasos:

1. Lanzar un ping a cualquer URL _(de preferencia IPv4 para que sea más sencilla la lectura, pero puede ser también IPv6)_

    - De esta manera se activará nuestro cliente DNS. 
    - Esto pasa porque los clientes Web necesitan "traducir" un simple string en una `IP Address.` 
    - Este es un proceso `transpartente`, que quiere decir que el usuario no se da cuenta de su ejecución por detrás. 

En el comando se puede notar como inmediatamente después de la URL muestra la IP, esto porque el protocolo DNS ya ha resuelto ese Dominio: 

````bat
:: Lanza ping a github.com
ping github.com
````

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/1cbf9b13-1524-472b-a95e-f39d3d5321c9)

2. Si revisaemos el `cache DNS` de nuestro sistema se puede encontrar el registro:

````bat
:: Muestra el contenido de la memoria caché de resolución DNS
ipconfig /displaydns
````

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/3a5373f2-a083-430a-90ea-a678be58f8c3)

- En caso de querer borrar el `DNS Cache` para poder resolver nuevamente la URL y no leerla directamente de nuestro registro, solo hay que hacer un flush. 

````bat
:: Purga la memoria caché del DNS
ipconfig /flushdns
````

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/e520f1c5-dfa9-4879-9c8a-07fd55696fe2)

OJO!!! Se puede utilizar tanto `IPv4` como `IPv6`, normalmente en un escenario real con Internet casero sea muy probable todo responda con `IPv6` en caso de hacer peticiones al `DNS` público, ya sea el que nos proporciona el `ISP`, o los siempre usados de Google `8.8.8.8` & `8.8.4.4` o CloudFlare `1.1.1.1` & `1.0.0.1`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/67ccb513-2df0-42ad-9595-4e290ddcd2e4)

Esto es importante, ya que el query cambia según el tipo de direccionamiento, eso se puede notar en los querys, más adelante se explica esto a detalle: 

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/74428777-b5db-4d3c-b0b1-583c7b811a2c)

- En caso de querer desactivar el o activar `IPv6` como hice en este laboratorio solo se debe desactivar de las propiedades del sistema: 

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/844824ff-2079-42c4-b55d-6941a9c0c8fb)

- **Ahora que ya tengo el setup listo, ¡Es hora de capturar en `Blackshark`!**


---

### `Laboratiorio DNS`: Parte 2 - Captura con Wireshark

`Recordatorio`: Antes de empezar la captura hay que borrar el `DNS cache` con el `ipconfig /flushdns`.

1. `Paso 1` - Comenzar a capturar en Wireshark
2. `Paso 2` - Hacer el proceso de ping _(Laboratiorio Parte 1)_ para resolver alguna dirección
3. `Paso 3` - Guardar el `.pcap` para su análisis. 
- [Descargar `.pcap` de ejemplo `DNS Lab IPv4` & `DNS Lab IPv4 + IPv6`](https://github.com/Fz3r0/Fz3r0_-_BlackShark/files/11493982/Fz3r0_DNS_Lab.zip)

---

### `Laboratiorio DNS`: Parte 3 - Análisis con Wireshark

Al realizar el proceso de la Parte 2, solo es necesario abrir `Wireshark` y comenzar a revisar por filtros, frame exchanges y análisis más a fondo: 

1. Analizando el DNS Query realizado desde la PC hacia el DNS server, una opción para aislar el frame exchange es con el `Transaction ID`

````java
# Filtrar por un DNS Transaction ID en particular
dns.id == 0x72ca
````

- **Punto de vista desde `Client` - `DNS Query`**

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/ac7d4e64-1be2-47fd-9a55-a28fedff6a79)

- **Punto de vista desde `Server` - `DNS Response`**

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/3d6afdee-851a-4b19-8b1d-8e19119f5786)

2. Si quiero ver un `Transaction ID` en particular seguido de algún otro tipo de tráfico referente a esa IP una idea podría ser esta: 

````java
# Filtrar por una IP (ya sea src o dst) con una Transaction ID en específico, pero también por protocolo icmp
(ip.addr == 192.168.1.67 &&  dns.id == 0x72ca) or icmp
````

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/56ca5d4a-26e8-480d-8977-6d9a38e91cee)

- Esto equivale exactamente al proceso de ping del laboratiorio:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/a0c822fb-2ed0-4d81-b3a7-ed7e85dba63b)






































































## Cheatsheet

### Comandos de Windows CMD: DNS

````bat
:: Mostrar la ayuda del ipconfig
ipconfig /?

:: Purga la memoria caché del DNS
ipconfig /flushdns


:: Muestra el contenido de la memoria caché de resolución DNS
ipconfig /displaydns



:: Entrar a linea de comando de nslookup (dentro se puede escribir un domain name)
nslookup

:: Muestra el resgistro DNS para 1.1.1.1
nslookup google.com
````

### Filtros Wireshark DNS

````java
# Transaction ID única de DNS
dns.id == 0x72ca

# DNS Type A (IPv4 Address)
dns.qry.type == 1

# DNA Cass IN
dns.qry.class == 0x0001
````








## Recursos y Fuentes

- [How DNS Work CloudFlare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Ivan Rodriguez - DNS con WireShark](https://www.youtube.com/watch?v=VEw2BqWzKOY)
- [GNS3 Talks: Easy DNS Server for GNS3 Topologies: Dnsmasq Docker Appliance Part 1](https://www.youtube.com/watch?v=86MIuxQ-LtI)
- [GNS3 Talks: Easy DNS Server for GNS3 Topologies: Dnsmasq Docker Appliance Part 2](https://www.youtube.com/watch?v=sTEKHzfX5Fc)
- [Configuración de DNS con Dnsmasq y Ubuntu Server (video)](https://www.youtube.com/watch?v=uV-OauHhKgA)
- [DNS Config on a Cisco Roputer - The Role of DNS within the Network | Lab Session in GNS3 | CCNA 200-301](https://www.youtube.com/watch?v=RYrnRZtjAxo)
- [Wikipedia: Tipos de registros DNS](https://es.wikipedia.org/wiki/Anexo:Tipos_de_registros_DNS)
- [rDNS - Búsqueda DNS inversa](https://es.wikipedia.org/wiki/B%C3%BAsqueda_DNS_inversa)
