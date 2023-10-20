# 📡💊 Management Frames (802.11): `Probe Request & Response`

Descubrir la red escaneando todos los posibles canales y escuchando por `Beacon Frames` desde nuestro dispositrivo no se considera muy eficiente _(`Passive Scanning`)_. Para mejorar este proceso de descubrimiento, las `STA` a menudo utilizan `Active Scanning` y para este proceso se unas los Frames `Probe Request` & `Probe Response`.

- Los **`Probe Request`** los utilizan las `STA` para descubrir la WLAN de modo: **`Active Scanning`** _([Passive Scanning, Active Scanning & Roaming](https://www.youtube.com/watch?v=HPJonmd8z1c))_
- Los **`Probe Response`** simplemente es la respuesta desde un `AP` que escucho por el Probe Request enviado desde una STA. 

En el `Active Scanning`, las `STA` aún recorren cada canal uno por uno, pero en lugar de escuchar pasivamente las señales en esa frecuencia, la `STA` envía un `Probe Request` preguntando qué red está disponible en ese canal.

- NOTA: Las `STA` deben tener aprendida la red previamente. 

Los `Probe Request` se envían a la dirección `Broadcast`: 

- `DA (Destination Address)` :: `FF:FF:FF:FF:FF:FF`.

Una vez que se envía un `Probe Request`, la `STA` inicia un temporizador llamado `ProbeTimer Countdown` y espera respuestas (`Probe Response`) de un posible AP en el área. Cuando el temporizador del `ProbeTimer Countdown` termina, la `STA` procesa la respuesta que ha recibido. Si no se reciben respuestas, la `STA` pasa al siguiente canal y repite el proceso de descubrimiento.

Las `STA` que envían `Probe Request` pueden especificar el `SSID` que están buscando, a esto se le llama `Directed Probe Request`. Luego, solo los APs _(o IBSSS STAs)_ que admitan ese SSID responderán. El valor del SSID también se puede establecer en 0 (es decir, el campo del SSID está presente pero vacío).

- **Esto se llama `Wildcard SSID` o `Null Probe Request`.**

## PCAPs de Laboratiorio: `Probe Request & Response`

Los PCAPs utilizados para los ejemplos de este bloque son los siguientes:

- [Fz3r0_|_Probe Request & Probe Response_Full Authentication Process | PSK/WPA2](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/files/13050282/Fz3r0_-_Probe-Request%2BResponse_-_Full-Auth-Process.zip)

## 🦈 `BlackShark Filter`: Probe Request & Probe Response (802.11)

````py

##########################################################################
#                                                                        #
#   Fz3r0 - BlackShark Filter: Probe Request & Probe Response (802.11)   #
#                                                                        #
##########################################################################

##########################################################################
#                      ALL Probe Request Frames:                         #
##########################################################################

## Opción 1
wlan.fc.type_subtype == 4

## Opción 2
wlan.fc.type_subtype == 0x0004

##########################################################################
#                      ALL Probe Response Frames:                        #
##########################################################################

## Opción 1
wlan.fc.type_subtype == 5

## Opción 2
wlan.fc.type_subtype == 0x0005 

##########################################################################
#              ALL Probe Request + Probe Response Frames:                #
##########################################################################

## Opción 1
(wlan.fc.type_subtype == 4 || wlan.fc.type_subtype == 5) && !wlan.fc.retry ==1

## Opción 2
(wlan.fc.type_subtype == 0x0004 || wlan.fc.type_subtype == 0x0005) && !wlan.fc.retry ==1

##########################################################################
#     Specific STA <--> AP :: Probe Request + Probe Response Frames:     #
##########################################################################

## Ejemplo    ::    STA(Request) <--> AP(Response)

# STA (Probe Request Transmiter/Source): Fz3r0 PC Wi-Fi Adapter:
## MAC :: 44:E5:17:06:E4:60
wlan.ta == 44:e5:17:06:e4:60

# AP (Probe Response Transmiter/Source): AP - Telmex Casero:
## MAC :: 50:4e:dc:90:2e:b8
wlan.ta == 50:4e:dc:90:2e:b8

# STA (Probe Response Receiver/Destination): Fz3r0 PC Wi-Fi Adapter:
## MAC :: 44:E5:17:06:E4:60
wlan.ra == 44:e5:17:06:e4:60

## Salida Fácil: Filtrar solo la conversación entre AP <--> STA (Ajustar Receiver Address RA | Transmitter Address TA)
!wlan.fc.retry == 1 && (wlan.ta == 50:4e:dc:90:2e:b8 || wlan.ta == 44:E5:17:06:E4:60 || wlan.ra == 50:4e:dc:90:2e:b8 || wlan.ra == 44:E5:17:06:E4:60)

## ACKs ida y vuelta
(wlan.fc.type_subtype == 0x001d && wlan.ta == 44:E5:17:06:E4:60 || wlan.fc.type_subtype == 0x001d && wlan.ta == 50:4e:dc:90:2e:b8)

## Action Frames ida y vuelta
(wlan.fc.type_subtype == 0x000d && wlan.ta == 44:E5:17:06:E4:60 || wlan.fc.type_subtype == 0x000d && wlan.ta == 50:4e:dc:90:2e:b8)

# Fz3r0: Super command for searching specific Probe Request & Response Between STA <--> AP  || SUPREME VICTORY
    ## Se deben cambiar 3 direcciones en total para que funcione
    ## 1. Probe Request   ::   wlan.TA(transmiter) (STA)
    ## 2. Probe Response  ::   wlan.TA(transmiter) (AP)
    ## 3. Probe Response  ::   wlan.RA(receiver)   (STA)
(wlan.fc.type_subtype == 4 && wlan.ta == 44:E5:17:06:E4:60) || (wlan.fc.type_subtype == 5 && wlan.ta == 50:4e:dc:90:2e:b8 && wlan.ra == 44:e5:17:06:e4:60) && !wlan.fc.retry ==1

##########################################################################
#    Specific STA <--> AP :: Probe Request & Response + Authentication   #
##########################################################################

# Fz3r0: Super command for searching specific Probe Request & Response Between STA <--> AP  || SUPREME VICTORY
#  +
# Fz3r0: 4-way-handshake Authentication Process (SUPREME VICTORY PERFECT!!! Sin Probes & Sin Actions - IT'S DANGEROUS!!!)
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol) || (wlan.fc.type_subtype == 4 && wlan.ta == 44:E5:17:06:E4:60) || (wlan.fc.type_subtype == 5 && wlan.ta == 50:4e:dc:90:2e:b8 && wlan.ra == 44:e5:17:06:e4:60)

# Fz3r0: Super command for searching specific Probe Request & Response Between STA <--> AP  || SUPREME VICTORY
#  +
# Fz3r0: 4-way-handshake Authentication Process (SUPREME VICTORY PERFECT!!! Sin Probes & Sin Actions - IT'S DANGEROUS!!!)
#  +
# Fz3r0: ACKs + Action Frames!!! + Todo lo anterior - ambos lados STA<-->AP (Supreme Victory + Ultra Ultra Ultra!!!)
# 
!wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 ||  wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol) || (wlan.fc.type_subtype == 4 && wlan.ta == 44:E5:17:06:E4:60) || (wlan.fc.type_subtype == 5 && wlan.ta == 50:4e:dc:90:2e:b8 && wlan.ra == 44:e5:17:06:e4:60) || (wlan.fc.type_subtype == 0x001d && wlan.ra == 50:4e:dc:90:2e:b8 || wlan.fc.type_subtype == 0x001d && wlan.ra == 44:E5:17:06:E4:60) || (wlan.fc.type_subtype == 0x001d && wlan.ta == 44:E5:17:06:E4:60 || wlan.fc.type_subtype == 0x001d && wlan.ta == 50:4e:dc:90:2e:b8) || (wlan.fc.type_subtype == 0x000d && wlan.ta == 44:E5:17:06:E4:60 || wlan.fc.type_subtype == 0x000d && wlan.ta == 50:4e:dc:90:2e:b8)
````

## Generador de Filtro Super Pro Entre STA y AP específicos

````py
while True:
    print("Este script te ayudará a generar un filtro de Wireshark para capturar paquetes entre una STA (cliente) y un AP (Access Point).")
    mac_sta = input("¿Cuál es la MAC de la STA (cliente, dispositivo móvil, laptop, tablet, etc)? ")
    mac_ap = input("¿Cuál es la MAC del AP (Access Point, Antena, Módem Wi-Fi casero, etc)? ")
    
    filter_text = f"""
        !wlan.fc.retry == 1 && (wlan.fc.type_subtype == 0 || wlan.fc.type_subtype == 1 || wlan.fc.type_subtype == 2 || wlan.fc.type_subtype == 3 || wlan.fc.type_subtype == 11 || wlan.fc.type_subtype == 12 || wlan.fc.type_subtype == 10 || eapol) ||
        (wlan.fc.type_subtype == 4 && wlan.ta == {mac_sta}) ||
        (wlan.fc.type_subtype == 5 && wlan.ta == {mac_ap} && wlan.ra == {mac_sta}) ||
        (wlan.fc.type_subtype == 0x001d && wlan.ra == {mac_ap} || wlan.fc.type_subtype == 0x001d && wlan.ra == {mac_sta}) ||
        (wlan.fc.type_subtype == 0x000d && wlan.ta == {mac_sta} || wlan.fc.type_subtype == 0x000d && wlan.ta == {mac_ap})
    """
    
    print("\nCopia el siguiente filtro y pégalo en Wireshark:\n")
    print(filter_text)
    
    another_filter = input("¿Deseas generar otro filtro? (Y/N): ")
    
    if another_filter.strip().lower() != 'y':
        break
````

## 📡 Probe Request & Response Frames: Descripción


















## 🧪 Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/bbad67e2-6f8e-4b27-9ee8-68152e0972f1)

### Action Frame Durante Auth

La aparición de un "action frame" entre un EAPOL (Extensible Authentication Protocol over LAN) message 1 de 4 y un EAPOL message 2 de 4 no es una coincidencia. En un proceso de autenticación WPA/WPA2 (Wi-Fi Protected Access) o WPA3, los mensajes EAPOL son parte integral de la autenticación entre una estación (STA) y un punto de acceso (AP). Los mensajes EAPOL se utilizan para negociar y establecer una clave de cifrado compartida que se utilizará para proteger la comunicación entre la STA y el AP.

Los "action frames" en este contexto se utilizan para gestionar y coordinar la autenticación, el intercambio de claves y otros aspectos del proceso de autenticación. Pueden indicar que se están llevando a cabo acciones específicas relacionadas con la autenticación y la seguridad, como la solicitud de un mensaje EAPOL, la aprobación o confirmación de un mensaje EAPOL, entre otros.

Por lo tanto, no es una coincidencia que haya "action frames" entre EAPOL message 1 de 4 y EAPOL message 2 de 4. Estos "action frames" están directamente relacionados con el proceso de autenticación y seguridad en una red Wi-Fi protegida. Su presencia indica que la red está gestionando y coordinando adecuadamente la autenticación entre la STA y el AP, lo que es esencial para garantizar una conexión segura.

## Beacon Frame: `Frame Format`

Este es el Frame Format de un Beacon Frame:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/2ac8ca5b-c2c8-4fe2-9fea-764ff9e57f77)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 📡 Beacon Frame: `Frame Body`

- En la sección del `Frame Body`, hay algunos **campos obligatorios** y algunos **campos opcionales**. 

Estos son los campos obligatorios en un `Beacon Frame`:

1. **`Timestamp`** (8 byte)
2. **`Beacon Interval`** (2 byte)
3. **`Capability info`** (2 byte)
4. **`SSID`** (variable size)
5. **`Supported Rates`** (variable size)

---

### Ejemplo 1: `Ruckus R850` + `SmartZone`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/1c129e19-63c3-465a-9423-f48420682ea6)

### Ejemplo 2: `Telmex Generic Home Wi-Fi Router`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/8fd599f5-5773-440f-97c8-608bec4977ab)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

# 📡🕵️ Beacon Frame Body: `Mandatory Fields`

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/df5d86c3-ff5a-4453-9554-c6b4e5b29067)

## 01 - `Timestamp` - 8 byte

### BlackShark Filter:

````py
## 01 - Timestamp - 8 byte
wlan.fixed.timestamp == 2078442701205
````

---

### Descripción:

- Un valor que representa el tiempo en el que el AP ha estado activo, que es el número de **microsegundos que el AP ha estado en funcionamiento**.
- Cuando el timestamp alcanza su máximo (2^64 microsegundos o ~580,000 años), se reinicia a 0. 

---

### Disponible en Frames:

- `Beacon` 
- `Probe Response`    

---

### Ejemplo:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/f5f9fcbb-cbf5-4056-90aa-a1c79f16eabd)

---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## 📡 02 - 



























---

<!-- 

CAMBIO DE BLOQUE --------------------------------------------------------------------------------------------------

 -->

<p align="center"> <img src="https://user-images.githubusercontent.com/94720207/228101704-c07ced92-e331-446c-aa7e-5d00018e2429.gif" alt="Encapsula" height=110px/> </a> </p> 

<br>
<br>
<br>

## Recursos

[CWNE#153 (Rasika Nayanajith) - 802.11 Mgmt : Probe Request & Response Frame](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/)


