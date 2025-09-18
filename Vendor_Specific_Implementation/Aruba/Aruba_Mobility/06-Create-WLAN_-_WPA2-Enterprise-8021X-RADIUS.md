# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - Create WLAN WPA2-Enterprise : 802.1X : RADIUS`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility` `AP Provisioning` `PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba Mobility :: `Create WLAN WPA2-Enterprise : 802.1X : RADIUS`

### IMPORTANT!!! 

ESTO NO ES CIERTO, NO ES NECESARIO PERO SI ES LA NUEBA PRACTICA TENERLA COMO TRUNK, PERO SI SIRVE CUALQUIER VLAN (ESCEPTO LA NATIVE m))BEFORE CONFIGURING AN SSID IN OTHER VLAN THAT DEFAULT 1, YOU NEED TO MAKE SURE THE MANAGEMENT INTERFACE OF THE MM IS SET TO TRUNK, ALLOWING THE VLANS WE WANT TO USE. EVEN IF THE MM IS LOCATED REMOTLY ON ANOTHER SUBNET, THIS BRINGS UP THE VLAN INTERFACE. 

<img width="1352" height="753" alt="image" src="https://github.com/user-attachments/assets/8df868af-dd53-4401-991d-2703be891492" />

Por alguna razon, con todas las VLANs fucniona el broisdge cuando las pongo dentro del trunk, por ejemplo la 30.... pero si intent con la vlan 300 radiarla, la cual ya es el mgmt de los APs, me sale solo el AP que esta tunneleado o algo asi, pero no users, o si se llega a conectar no tienen ip ni nada y depsues los vota, con la vlan 3'0 no tengo ese problema

ESTO PASA POR QUE LA NATIVE DEL VAP SIGUE SIENDO 1 POR DEFAULT, Y LAS TAGGED SERVIRAS AUN ASI, PERO LA NATIVE AHI SI NO, SI POR ALGUNA RAZON QUIERES RADIAR LA NATIVE TMB, HAY QUE CAMBAIR LA NATIVE DEL VAP: 

<img width="1890" height="905" alt="image" src="https://github.com/user-attachments/assets/e38186cb-d6ef-430b-8476-ede0587423ca" />

<img width="1256" height="457" alt="image" src="https://github.com/user-attachments/assets/60f17a69-e1a6-4a95-af20-b09bbc3dd841" />




## 1) NPS (Windows Server) :: Agregar los Aruba MC's como RADIUS clients

En el NPS:

1. **RADIUS Clients and Servers » RADIUS Clients » New…**

<img width="933" height="304" alt="image" src="https://github.com/user-attachments/assets/d209779d-cfc4-4b38-b29f-5d9874138aef" />

- **Friendly name:** `MGD-DEV::MC-Fz3r0-1`
- **Address (IP):** `192.168.1.196`
- **Shared secret:** `Cisco.12345`
- **Vendor:** RADIUS Standard.

Repite para el segundo MC: 

- **Friendly name:** `MGD-DEV::MC-Fz3r0-2`
- **Address (IP):** `192.168.1.197`
- **Shared secret:** `Cisco.12345`
- **Vendor:** RADIUS Standard.

<img width="919" height="590" alt="image" src="https://github.com/user-attachments/assets/2f7a47f5-048e-4e87-8e45-093e479b8ebf" />

<img width="939" height="290" alt="image" src="https://github.com/user-attachments/assets/3dda08ab-c115-44d8-a8f8-260a7f652c7c" />

2. Verifica tu **Network Policy** (PEAP/EAP-TLS, etc.), condición puede ser “NAS Port Type = Wireless – IEEE 802.11” y/o “Client Friendly Name = MGD-DEV::MC-Fz3r0-1 o MGD-DEV::MC-Fz3r0-2”.

<img width="936" height="924" alt="image" src="https://github.com/user-attachments/assets/be1d6544-74c0-4ecd-9a86-8fadfe04651b" />

> Si usas PEAP/EAP-TLS: el NPS debe tener cert de servidor válido y la hora sincronizada (NTP).








# 2) Aruba – apuntar al NPS y usarlo en el SSID 802.1X

CLI equivalente (ajusta nombres/IP/secret):

```bash
configure terminal

# Servidor RADIUS (tu NPS)
radius server NPS1
  host <IP_DEL_NPS>
  key <TU_SHARED_SECRET>
  timeout 5
  retransmit 3
exit

# Grupo AAA que usa ese RADIUS
aaa server-group NPS-SG
  auth-server NPS1
exit

# Perfil 802.1X
aaa authentication dot1x DOT1X-NPS
  server-group NPS-SG
  no cp-profile
exit

# Rol inicial (logon) y rol final
user-role dot1x-logon
  access-rule logon-control
exit

user-role employee-vlan30
  vlan 30
  access-rule allowall
exit

# AAA profile para el VAP 802.1X
aaa profile EMP-AAA
  initial-role dot1x-logon
  dot1x-auth-profile DOT1X-NPS
  # (opcional) enforce-vlan o defínelo en el VAP
exit

# SSID (enterprise 802.1X en bridge)
wlan ssid-profile EMP-8021X
  ssid EMP-8021X
  opmode wpa2-aes
  wpa-passphrase disable
  wpa-psk 0  # (no PSK)
  auth-server NPS-SG  # si tu versión lo pide en ssid-profile
  dot1x authentication-profile DOT1X-NPS
  forward-mode bridge
exit

wlan virtual-ap EMP-8021X-VAP
  ssid-profile EMP-8021X
  aaa-profile EMP-AAA
  vlan 30
exit

ap-group LAB
  virtual-ap EMP-8021X-VAP
  # recuerda: ya alineaste el native-vlan-id del AP system-profile a 300 (tu mgmt)
exit

write memory
```

> Si prefieres GUI: **Configuration » Authentication » Servers** (creas el RADIUS y server-group), luego **WLANs » tu SSID » Security** (802.1X/Enterprise) y seleccionas el **server-group**. En **Access**/Profiles estableces rol inicial y VLAN.

# 3) Validaciones rápidas

En el **MD**:

* Ver quién hace las peticiones y qué VLAN cae:

  ```
  show user-table verbose
  ```
* Probar reachability del NPS:

  ```
  ping <IP_DEL_NPS>
  ```
* Probar RADIUS con un usuario de prueba:

  ```
  aaa test-server radius NPS1 username <user> password <pass>
  ```
* Estadísticas RADIUS:

  ```
  show aaa authentication-server radius statistics
  show log security | include radius
  ```

En el **NPS**:

* Ver que ya **no** salga “invalid RADIUS client … 192.168.1.196”.
* Que aparezcan eventos de **Access-Accept/Reject** según credenciales/política.

# 4) Cosas que suelen romper 802.1X

* **Shared secret** distinto (NPS vs Aruba).
* **IP de origen** del MD distinta a la autorizada en NPS. Si quieres fijarla:

  ```
  ip radius source-interface vlan <ID_que_quieras>
  ```

  (si no, NPS debe aceptar la que realmente usa el MD — hoy ves 192.168.1.196).
* **Hora** desfasada si usas PEAP/EAP-TLS (certs).
* **Política NPS** demasiado estricta (por ejemplo, solo EAP-TLS y tu cliente usa PEAP-MSCHAPv2).

Con eso, al conectar al SSID 802.1X te debe dejar de pedir credenciales en loop y verás el cliente en **show user-table** con **Role** ≈ tu rol post-auth y **Vlan 30 (30)**.










































### `Step 1`: Crear la VLAN que llevará mi WLAN/SSID

- La VLAN será la que transporte esta red, del lado del backbone esta VLAN tiene que estar configurada en el DHCP en caso de estar en modo bridge, o existir en la controladora en caso de estar tunneled.
- Es decir, la VLAN debe coincidir ya sea con la controladora o la LAN

**Grupo > Sub-Grupo > Configuration > Interfaces > VLAN:**

<img width="1919" height="766" alt="image" src="https://github.com/user-attachments/assets/e0ee79f3-afbd-459a-90d5-410de97bfbec" />

Agregar el VLAN ID y un nombre identificador y hacer deplot de los cambios

- Nota: Mas adelante se podrá seleccionar la VLAN tanto por el nombre como por el número. 

<img width="1952" height="523" alt="image" src="https://github.com/user-attachments/assets/692b81e8-c4af-4cca-8d7b-d8d31525ff8d" />

### `Step 2`: Configurar WLAN (SSID)

- Al principio no existirá ninguna WLAN ya que no hemos creado ninguna

**Grupo > Sub-Grupo > Configuration > WLANs:**

<img width="1919" height="767" alt="image" src="https://github.com/user-attachments/assets/eed65a02-8b77-4dc1-ada4-07cb22236875" />

Llenar los campos según sea necesario, particularmente para este lab yo usaré: 

- Name (SSID): `V10-EMPLOYEE_ENTERPRISE_TUNNEL`
- Primary usage: `Employee`
- Select AP Groups Broadcast: `AP-GROUP1_office-branch-01`
- Forwarding mode: `Tunnel`

NOTA: La gran diferencia entr ebridged y tunnel es que bridged se comporta el AP como un "switch" todas las VLANs que vienen de los SSID saldrán trunkled con 802.1q y por ende el switch también debe ser trunked, uan vez que sale del AP los datos ya todo se pasa a la LAN y ahi se debe hacer cargo del DHCP y demas, tal cual como otro switch truinked. Por otro lado, si esta tunnel todo sera tunneleado por una misma VLAN hasta la controladora, y ya la controladora se harña cargo de DHCP y el control de datos. 

NOTA 2: la diferneci aen aruba con un Employee un y Guest es..... aqui pon que odna vektor. 

<img width="632" height="456" alt="image" src="https://github.com/user-attachments/assets/2c51137b-be52-4d3b-8ad9-56d207c76b95" />

Después, seleccionar la VLAN:

- Aquí podemos usar ya sea el VLAN ID "10" o el nombre completo de la VLAN.
- Podemos incluso ver las VLANs que ya hay creadas por si tenemos duda

<img width="1256" height="658" alt="image" src="https://github.com/user-attachments/assets/69c63a95-8042-4f6d-84c4-0b5f0f1d33fa" />

Ahora pasamos a la parte de seguridad:

- Aquí podemos seleccionar ya sea WPA2 o WPA3 Enterprise, yo usaré WPA2 para fines prácticos
- El reauth interval en aruba es...
- el mahcina authentication es.... por ahor alo dejare en disabled
- el deny listing se suma con el max authentication, aqui simplemente es el nuemro de beves que peudes bla bla... el máximo es 5 

<img width="1173" height="680" alt="image" src="https://github.com/user-attachments/assets/34cd8050-2f3a-43d5-8fcf-8de3f9de1881" />

Hacer click en "+" para agregar el authetnication server. 

- En este lab yo usaré mi Windows Server 2022 Data center, dodne tengo ya un NPS jalando. RADIUS: 192.168.1.86	shared secret:	Cisco.12345

<img width="642" height="491" alt="image" src="https://github.com/user-attachments/assets/0426c71e-ea46-4484-ad28-512c9400ab2b" />

En caso de un "Employee" el Default Role siempre será guest (esto confirmamelo porfa vektor)

<img width="1188" height="238" alt="image" src="https://github.com/user-attachments/assets/c4615fc9-fc75-4fe6-a6b2-5104d3e3a295" />

Y listo! simplemente hacer el deploy: 

<img width="1280" height="291" alt="image" src="https://github.com/user-attachments/assets/93b960cc-73f6-4476-aff2-9ab1807ff08d" />



---

## Instalar Certificado en cliente: 

<img width="372" height="401" alt="image" src="https://github.com/user-attachments/assets/da3fd53f-a609-431d-bf3c-dd156aed00e0" />



---

# 🗃️ Resources

- 
---

<span align="center"> <p align="center"> ![giphy](https://user-images.githubusercontent.com/94720207/166587250-292d9a9f-e590-4c25-a678-d457e2268e85.gif) </p> </span> 

&nbsp;

<span align="center"> <p align="center"> _I hope this information was useful for someone_ </p> </span> 
<span align="center"> <p align="center"> _and please, don't forget to enjoy your days..._ </p> </span> 
<span align="center"> <p align="center"> _...It is getting dark... so dark..._ </p> </span> 

&nbsp;

<span align="center"> <p align="center"> _In the mist of the night you could see me come, where shadows move and Demons lie..._ </p> </span> 
<span align="center"> <p align="center"> _I am [Fz3r0 💀](https://github.com/Fz3r0/) and the Sun no longer rises..._ </p> </span> 

---

---

> ![hecho en mexico 5](https://user-images.githubusercontent.com/94720207/166068790-fa1f243d-2db9-4810-a6e4-eb3c4ad23700.png)
>
> _- Hecho en México - by [Fz3r0 💀](https://github.com/Fz3r0/)_  
>
> _"In the mist of the night you could see me come, where shadows move and Demons lie..."_ 
