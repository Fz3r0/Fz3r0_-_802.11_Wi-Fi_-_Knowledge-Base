<!-- 

Y ARRANCAN!!!

ejemplo centrar:

<p align="center"> <img src="solo el link" alt="Mac" height=600px/> </a> </p> 

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/223137182-929a5e71-1b1f-48c4-94b4-1553a386fefa.png" alt="Mac" height=600px/> </a> </p> 

 -->

# Protocols from hell: `DNS` <br> `Domain Name Service` 📡🦈💀 <br>  

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




## DNS


---

### Puntos clave del DNS:

---

### Ventajas y Desventajas del protocolo mDNS

---

### Consideraciones a tomar con DNS en redes Empresariales y Alta Densidad

---

### Consideraciones a tomar con DNS en redes Wireless 802.11 (WiFi)

---


## CATNO IV: Frame Exchange de DNS

### mDNS Technical Frame Exchange

### Fz3r0 Cheatsheet: mDNS

````java


````



## `Laboratiorio`: DNS

### `Laboratiorio`: Setup Inicial

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

Ahora que ya tengo el setup listo, ¡Es hora de capturar en `Blackshark`!

---

### Laboratiorio: DNS con Wireshark 
































































## Cheatsheet

````bat
:: Mostrar la ayuda del ipconfig
ipconfig /?

:: Purga la memoria caché del DNS
ipconfig /flushdns


:: Muestra el contenido de la memoria caché de resolución DNS
ipconfig /displaydns
````










## Recursos y Fuentes

- [Ivan Rodriguez - DNS con WireShark](https://www.youtube.com/watch?v=VEw2BqWzKOY)
