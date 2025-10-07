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

3. En el NPS se verá un aviso:

<img width="1893" height="473" alt="image" src="https://github.com/user-attachments/assets/748e1436-2c7a-4d10-aa33-dd71b5d69e90" />


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















































### `Step 0`: Planeación rápida de direcciones

En el modo "Tunnel", el AP encapsula todo hacia la controladora usando la VLAN de management, por ejemplo 300. La VLAN del SSID, por ejemplo 702, no sale del AP en el cable. La controladora termina el túnel y “desempaca” en la VLAN 702, donde puede ser gateway y servidor DHCP. **En la LAN solo necesitas el puerto del AP en access a la 300. Solo usarías trunk si mezclas con algún SSID en Bridged.**

- VLAN de management: `300`  (APs llegan por aquí, túnel viaja por aquí)
- VLAN de usuarios (SSID): `702`
- SVI de la controladora (MM/MC) para VLAN 702: `172.20.2.1/24`
- Scope DHCP para VLAN 702: `172.20.2.10 - 172.20.2.200`
- DNS: `8.8.8.8`,`1.1.1.1`
- Default route de la controladora hacia tu core/Internet: `0.0.0.0/0 - <next-hop-en-VLAN300>`

---

### `Step 1`: Crear la VLAN de usuarios en la controladora

**Group > Sub-Group > Configuration > Interfaces > VLANs**

1. Add
   - VLAN ID: `702`
   - Name: `VLAN-702-EMP-TUNNEL`
2. Save / Deploy

> Aunque el tráfico irá “tunneleado” por la VLAN 300, necesitas definir la VLAN 702 para que la controladora la “desempaque” y haga L3/DHCP.

<img width="1357" height="628" alt="image" src="https://github.com/user-attachments/assets/a51039c2-2ed1-48a0-a20c-169ee3f15bb8" />

---

### `Step 2`: Crear la SVI (gateway) para esa VLAN

**Group > Sub-Group > Configuration > Interfaces > VLANs >>> Select Tunnel 702 > 702 > IPv4**

<img width="1913" height="775" alt="image" src="https://github.com/user-attachments/assets/75703bf4-08e1-4e2b-bf62-f1158cbe1a7e" />

- IP assignment: `Static`
- IP address: `10.70.2.254`
- Netmask: `255.255.255.0`
- IP DHCP settings: `Act as server`
- Network: `10.70.2.0`
- Netmask: `255.255.255.0`
- Pool name: `vlan_702`
- Default router: `10.70.2.254`
- DNS server: `8.8.8.8`
- Netbios name `server: 
- MTU:
- Suppress ARP:

> Esta SVI convierte a la controladora en el default gateway de los clientes del SSID.

<img width="428" height="657" alt="image" src="https://github.com/user-attachments/assets/dccc8fd8-093a-4e90-bb73-8e83f46158ad" />


---

### `Step 3`: Configurar DHCP en la controladora para la VLAN 702

**Grupo > Sub-Grupo > Configuration > Services > DHCP**

* DHCP Server: Enable
* Add Scope

  * Scope name: `DHCP-702`
  * VLAN: `702`
  * Network: `10.70.2.0`
  * Mask: `255.255.255.0`
  * Default gateway: `10.70.2.1`
  * DNS servers: `10.10.10.10`  (o el que uses)
  * Lease time: `8h`  (o tu valor)
  * Address range: `10.70.2.10 – 10.70.2.200`
* Save / Deploy

> Si prefieres DHCP externo, omite esto y en su lugar prepara el enrutamiento o IP helpers. Para este tutorial usamos DHCP local.

---

### `Step 4`: Asegurar enrutamiento de salida de la controladora

**Grupo > Sub-Grupo > Configuration > Routing > Static Routes**

* Add

  * Destination: `0.0.0.0/0`
  * Next hop: `<IP del gateway en VLAN 300>`  (por ejemplo `10.70.0.1`)
* Save / Deploy

> Esto permite que el tráfico de la VLAN 702 salga a tu LAN/Internet. Si tu red usa enrutamiento dinámico puedes omitir y usar OSPF/BGP, pero con default route es suficiente para el lab.

---

### `Step 5`: Crear el SSID en modo Tunnel

**Grupo > Sub-Grupo > Configuration > WLANs**

* Add

  * Name (SSID): `V10-EMPLOYEE_ENTERPRISE_TUNNEL`
  * Primary usage: `Employee`
  * Forwarding mode: `Tunnel`
  * VLAN: `702`  (puedes seleccionar por ID o por nombre)
  * Broadcast to AP Groups: `AP-GROUP1_office-branch-01`
* Security

  * Key management: `WPA2-Enterprise`  (o WPA3 si lo deseas)
  * Authentication server / Server group: selecciona tu RADIUS ya existente
  * Reauth interval: `8h`
  * Machine authentication: `Disabled` por ahora
* Save / Deploy

> “Tunnel” hace que todo el tráfico cliente-AP viaje encapsulado hasta la controladora por la VLAN 300. La controladora actúa como gateway y DHCP para la VLAN 702.

---

### `Step 6`: Asignar el SSID al AP Group y verificar perfiles

**Grupo > Sub-Grupo > Configuration > AP Groups > AP-GROUP1_office-branch-01**

* WLANs: agrega `V10-EMPLOYEE_ENTERPRISE_TUNNEL`
* Verifica que el AP Group tenga RF profiles y AP system profile correctos
* Save / Deploy

> Si tus APs quedan en “Pending”, valida conectividad a management VLAN 300 y reachability hacia la controladora.

---

### `Step 7`: Verificación rápida

CLI de la controladora:

```bash
# Asociaciones y usuarios
show user-table
show aaa authentication sessions

# BSS y radios
show ap bss-table

# DHCP (leases)
show ip dhcp binding
show ip dhcp statistics

# Enrutamiento y reachability
show ip route
ping 10.70.2.10   # IP de un cliente
```

En el cliente:

* Conéctate al SSID `V10-EMPLOYEE_ENTERPRISE_TUNNEL`
* Debe recibir IP en `10.70.2.0/24` con gateway `10.70.2.1` y DNS configurado
* Debe autenticar vía 802.1X contra tu RADIUS ya existente

---

### `Step 8` (Opcional): Políticas mínimas de rol

Si usas roles por defecto, asegúrate de permitir DNS, DHCP, y el tráfico necesario hacia tu red o Internet. Lo más simple para validar el lab es permitir salida a Internet y bloquear inter-user si lo deseas.

---

### Checklist final

* VLAN `702` creada
* SVI `10.70.2.1/24` Up en VLAN 702
* DHCP scope activo para VLAN 702
* Default route configurada hacia el core por VLAN 300
* SSID `V10-EMPLOYEE_ENTERPRISE_TUNNEL` en modo `Tunnel` con VLAN 702
* SSID asignado al `AP-GROUP1_office-branch-01`
* Cliente obtiene IP, gateway y navega

Con esto tienes el SSID en modo Tunnel, con la controladora funcionando como gateway y servidor DHCP para la VLAN del SSID. Si quieres, luego afinamos roles, ACLs y ya metemos Machine Auth/EAP-TLS.


---

## Instalar Certificado en cliente: 

<img width="372" height="401" alt="image" src="https://github.com/user-attachments/assets/da3fd53f-a609-431d-bf3c-dd156aed00e0" />

<img width="1894" height="994" alt="image" src="https://github.com/user-attachments/assets/67c6e527-967e-4d00-903f-63c945a8cce7" />



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
