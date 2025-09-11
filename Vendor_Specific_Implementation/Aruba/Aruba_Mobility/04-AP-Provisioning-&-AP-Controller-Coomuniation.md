# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - AOS 8x Architecture`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility` `AP Provisioning` `PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba AP Discovery & Provisioning towards Mobility Controller (MC) / Mobility Master (MM)

## 📡 P Discovery & Provisioning: `CAP` vs `RAP` vs `IAP`

Aruba delivers Access Points (APs) in different operating modes depending on the deployment architecture. For this discussion, we’ll focus on **CAPs/RAPs**, which operate under controller management (MC/MM).

| Type                 | Mode             | Key Characteristics                                                                                                 | Use Case                                              |
| -------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **CAP (Campus AP)**  | Controller-based | Boots with ArubaOS-CAP image. Always establishes a tunnel (GRE/IPsec) to MC/MM for management and data forwarding.  | On-premises enterprise deployments (campus networks). |
| **RAP (Remote AP)**  | Controller-based | Similar to CAP, but designed for remote/home users. Establishes secure IPsec tunnel to MC/MM across the internet.   | Remote workforce, branch offices.                     |
| **IAP (Instant AP)** | Controller-less  | Boots with Aruba InstantOS (IAP) image. Functions autonomously or can form a cluster of IAPs. No controller needed. | Small/medium sites without dedicated controllers.     |

- For **controller-based (CAP/RAP)** deployments, the AP cannot operate standalone, **it must discover and register with an MC/MM before becoming operational.**

Nota: UN AP Aruba (e.g. AP-515) puede ser IAP o CAP según el firmware que tenga cargado. Como lo compraste usado/por internet, lo primero es ver en qué modo viene.

### Primer acceso al AP via IP

1. Conéctalo a tu switch con PoE (mínimo 802.3at PoE+ porque el 515 es hungry).
2. Dale conectividad en una VLAN con DHCP (más fácil al inicio), busca la IP con algún scanner o en la pool del DHCP.
3. Si es IAP, va a pedir IP vía DHCP y puedes buscarla:
    - show arp en tu switch/router
    - scanner tipo nmap o arp-scan.
    - Default login: `admin`/`(serial_number)`

<img width="734" height="349" alt="image" src="https://github.com/user-attachments/assets/0a1117f6-304d-4f6e-9b74-5d3b367f62e0" />

Nota: Si es CAP, al bootear intentará llegar a un MC/MM. Sin controlador, suele quedarse con IP DHCP y página mínima que dice que necesita controller.

### Primer acceso al AP via Console

1. Consola serial: conéctale un cable micro-USB (los Aruba 5xx traen puerto console micro-USB) o adaptador RJ-45 console si aplica.
2. Durante boot verás si carga como ArubaOS Instant (IAP) o como CAP.

Si ya trae config vieja de otra red, puedes hacer factory reset:

1. Botón reset en la parte trasera, déjalo presionado unos 10-15s hasta que parpadee el LED.
2. Al soltar, regresa a defaults (IAP o CAP según firmware instalado).

### 🔄 Cambiar firmware entre IAP ↔ CAP

**De IAP a CAP (para usarlo con un Mobility Controller):**

Listo Carlos, investigué a fondo. Hay matices importantes que corregir/modificar respecto a lo que te decía, especialmente para AP-515 y versiones modernas de Aruba. Aquí la versión actualizada:

---

## 🔍 Datos reales sobre IAP ↔ CAP para Aruba APs como el 515

* El AP-515 **trae código Instant/AP por defecto** en muchas entregas. Si al encenderlo **no encuentra un controller**, arranca como IAP. ([Airheads Community][1])
* Sin embargo, **no todos los AP son “modelos totalmente Instant-only”**. Aruba soporta la conversión de Instant APs a Campus AP (CAP) o Remote AP (RAP) si el firmware y modelo lo permiten. ([HPE Aruba Networking][2])
* El comando CLI `convert-aos-ap <mode> <Controller-IP>` sirve para convertir un Instant AP (IAP) a CAP o RAP, siempre que el controller esté corriendo una versión de ArubaOS compatible. ([HPE Aruba Networking][2])

  * Ejemplo: `convert-aos-ap CAP 10.10.31.208` lo convierte a CAP apuntando al controller con esa IP. ([Airheads Community][3])
* Enverso contrario, hay opciones para convertir CAP → IAP en modelos soportados, usualmente mediante interfaz web o mediante “Convert to Instant” desde el Controller GUI, si el modelo/AP tiene soporte, versión de firmware correcta, etc. ([Art of RF][4])
* Otras condiciones importantes que encontré:

  1. El AP y el Controller deben estar en el **mismo dominio regulatorio** (regulatory domain). Si no, la conversión puede fallar. ([HPE Aruba Networking][2])
  2. El firmware del controller debe ser lo suficientemente nuevo (por ejemplo, ArubaOS versión ≥ cierta release) para soportar la operación `convert-aos-ap`. ([HPE Aruba Networking][2])
  3. Compatibilidad de imagen: si conviertes, el AP descargará la imagen (firmware) desde el controller automáticamente al hacer `convert-aos-ap`. ([Airheads Community][5])
  4. Es necesario que la red permita que el AP llegue al controller (que la IP del controller sea accesible, que haya ruta, DNS si aplica, etc.). ([Airheads Community][5])

---

## ✅ Versión corregida del bloque para ti

Aquí cómo quedaría mejor explicado con la información real:

---

### 🔄 Cambiar entre IAP ↔ CAP (AP-515 / Aruba modelos recientes)

**De IAP a CAP (usar con Mobility Controller / Controller-based network):**

1. Verifica que tu controller corre una versión de ArubaOS compatible con la conversión de Instant APs (por ejemplo versiones 6.x+, ArubaOS que soporte el comando `convert-aos-ap`).
2. Asegúrate de que AP y controller estén en el mismo dominio regulatorio y que el controller sea accesible desde el AP.
3. En la consola del AP Instant, ejecuta:

   ```
   enable
   convert-aos-ap CAP <IP-del-Controller>
   ```

4. El AP descargará automáticamente el firmware adecuado desde el controller, hará reboot, y al reiniciar operará como CAP / Remote AP apuntando al Controller.

**De CAP a IAP (modo standalone / Instant lab):**

1. Verifica que el modelo/AP tenga soporte para modo IAP (AP-515 lo tiene en muchas entregas).
2. Si el AP no detecta un controller o ha sido reseteado, al arrancar puede volver a levantarse en modo IAP (especialmente si lo traías configurado como Instant anteriormente). 
3. Si necesitas forzar la conversión, busca en la GUI del controller la opción “Convert to Instant mode” para ese AP, si tu versión la tiene. También podría requerirse un preload de la imagen Instant si el AP no tiene ya esa parte de firmware.

---




---

¿Quieres que te arme también la **lista de comandos CLI** típica para hacer el upgrade por consola (los `copy`, `boot system`, etc.), para que lo tengas listo en tu lab sin depender de la GUI?




## First Connection of an AP to the LAN

When a new AP is connected to the LAN for the first time, it requires basic **L3 connectivity** to reach the controller. This can be achieved via:

### **DHCP (Recommended)**

- The AP sends a DHCP Discover.
- Receives an IP address, subnet mask, default gateway, and DNS server from a DHCP Server.
- Optionally, DHCP option 43/60 can provide the MC/MM IP directly.

### **Static IP**

- The AP is manually configured with IP, subnet mask, gateway, and controller address.
- Useful in networks without DHCP or where static addressing is a policy requirement or for testing purposes.

✔️ In both cases, the AP must know how to reach the controller’s IP address. If using DNS, the AP resolves `aruba-master` to the MC/MM IP.

## Connection Diagram & Discovery Process

The diagram below illustrates a typical **first-boot scenario** for an Aruba AP (CAP):

<img width="985" height="376" alt="image" src="https://github.com/user-attachments/assets/c1bf6d0a-7c51-4432-9a34-2bccfadcea54" />

### Scenario A: `DHCP-based Discovery`

1. AP powers up via PoE or injector ⚡.
2. Sends DHCP Discover through the L2 switch.
3. DHCP server provides:

   * IP address & subnet mask
   * Default gateway
   * DNS server
   * Optionally, Controller IP (DHCP option 43/60)
4. AP uses this info to initiate secure communication with the controller.

**Configuration Steps:**

#### STEP 1 :: Create WLAN VLAN (Native Bridge or Combined / Access Tunnel Only)

vlan 300
   name v300-ARUBA-WIRELESS-MGMTandTUNNEL
exit

#### STEP 2 :: Create SVI (v300 Gateway)

- Local DHCP Server method

````py
interface Vlan300
   description *** ARUBA WIRELESS SVI - LOCAL DHCP ***
   ip address 10.10.130.254 255.255.255.0
   ip ospf 1 area 0
exit
````

- DHCP helper method:

````py
interface Vlan300
   description *** ARUBA WIRELESS SVI - DHCP HELPER ***
   ip address 10.10.130.254 255.255.255.0
   ip helper-address 10.10.66.185
   ip helper-address 10.10.66.186
   ip pim sparse-mode
   ip ospf 1 area 0
exit
````

#### STEP 3 :: Add VLAN to AP interfaces:

````py
! # ACCESS INTERFACE (TUNNEL)
interface GigabitEthernet 1/0/11
   *** v300 Wi-Fi :: TUNNEL (ACCESS) ***
   switchport mode access
   switchport access vlan 300
      spanning-tree portfast edge 
      no shutdown 
exit 

!


````

or

````py
! # ACCESS INTERFACE (BRIDGE OR COMBINED)
interface GigabitEthernet 1/0/19
   *** v300 Wi-Fi :: BRIDGE (TRUNK) ***
   switchport access vlan 300
   switchport mode trunk
   ! # Management/Tunnel VLAN 300 as Native 
   switchport trunk native vlan 300 
   ! # SSIDs allowed & pruned, e.g VLAN 300 (or others)
   switchport trunk allowed VLAN 300
      spanning-tree portfast trunk 
      no shutdown
exit 

!

 
````

#### 4. Create DHCP server or DHCP helper (v300 DHCP pool)

- Local DHCP Server:

````py
! # Excluded IPs v300
ip dhcp excluded-address 10.10.130.1 10.10.130.100
ip dhcp excluded-address 10.10.130.201 10.10.130.254
!
! # DHCP pool v300
ip dhcp pool v300-ARUBA-WIRELESS
   network 10.10.130.0 255.255.255.0
   default-router 10.10.130.254
   dns-server 8.8.8.8 1.1.1.1
   domain-name fz3r0.dojo
   lease 0 8 0
      ! # OPTION 60: 
      option 60 ascii ArubaAP
      ! # OPTION 43: ARUBA MC IP (WLC controller)
      option 43 ip 192.168.1.196
         ! # Fixed IPs (if needed) 
         address 10.10.130.101 client-id 01f0.f0f0.f0f0.f0
exit  

!

````

- DHCP Helper (eg. for external DHCP server or DDI service):

_Just add the IP helper on SVI, see Step 2, no more config is needed._

---

### Scenario B: `Static IP (No DHCP)`

* Same topology, but DHCP server is not required.
* Admin pre-configures on the AP:

  * Static IP & mask
  * Gateway
  * DNS (optional)
  * Controller IP address

👉 In both scenarios, once basic IP reachability is established, the AP downloads its image (if mismatch), provisions itself according to the group profile from MM/MC, and transitions to **“operational”** state.













---

# 🗃️ Resources

- https://community.arubanetworks.com/discussion/how-to-convert-ap-515-to-iap?utm_source=chatgpt.com "HOW TO CONVERT AP-515 to IAP | Controllerless Networks"
- https://arubanetworking.hpe.com/techdocs/CLI-Bank/Content/instant/convert-aos-ap.htm?utm_source=chatgpt.com "convert-aos-ap"
- https://community.arubanetworks.com/discussion/converting-instant-aps-to-campus-aps-the-struggle-is-real?utm_source=chatgpt.com "Converting instant APs to campus APs -- the struggle is real"
- https://artofrf.com/2022/02/20/aruba-convert-cap-to-iap/?utm_source=chatgpt.com "Aruba – Convert CAP to IAP - artofrf.com"
- https://community.arubanetworks.com/discussion/convert-iap-to-cap-issue-on-ap-515?utm_source=chatgpt.com "Convert IAP to CAP issue on AP-515 | Controllerless Networks"

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

