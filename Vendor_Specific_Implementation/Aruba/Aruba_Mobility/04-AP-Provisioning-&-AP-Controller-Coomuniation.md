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
    - Default login: `admin`/`(SERIAL_NUMBER_MAYUS)`

<img width="734" height="349" alt="image" src="https://github.com/user-attachments/assets/0a1117f6-304d-4f6e-9b74-5d3b367f62e0" />

<img width="902" height="541" alt="image" src="https://github.com/user-attachments/assets/1f5438f3-8603-4275-8f00-7231714710c1" />

Una vez dentro, el dashboard se verá así:

<img width="1919" height="702" alt="image" src="https://github.com/user-attachments/assets/fb46733e-99c8-4c80-9453-e91263af1a8c" />

Notas:

- Si el AP no deja hacer login debido a credenciales incorrectas, es posible ya venga con un user y password personalizados, en ese caso hay que hacer Factory Reset.
- Si el AP viene como CAP, al bootear intentará llegar a un MC/MM y no tendrá acceso por GUI. Sin controlador, suele quedarse con IP DHCP y solo puede accederse por SSH, en ese caso hay que hacer Factory Reset.
- Primer acceso al AP via Console: conéctale un cable micro-USB (los Aruba 5xx traen puerto console micro-USB) o adaptador RJ-45 console si aplica.

### Factory Reset

1. Botón reset en la parte trasera, déjalo presionado unos 10-15s hasta que parpadee el LED.
2. Al soltar, regresa a defaults (IAP o CAP según firmware instalado).
3. Entrar con credenciales default `admin`/`(SERIAL_NUMBER_MAYUS)`
4. Hacer reset de password

<img width="302" height="223" alt="image" src="https://github.com/user-attachments/assets/463e6f05-4c3f-49f0-8326-a580d660055f" />


### 🔄 Cambiar firmware entre IAP ↔ CAP

* El AP-515 **trae código Instant/AP por defecto** en muchas entregas. Si al encenderlo **no encuentra un controller**, arranca como IAP. 
* Sin embargo, **no todos los AP son “modelos totalmente Instant-only”**. Aruba soporta la conversión de Instant APs a Campus AP (CAP) o Remote AP (RAP) si el firmware y modelo lo permiten. 
* El comando CLI `convert-aos-ap <mode> <Controller-IP>` sirve para convertir un Instant AP (IAP) a CAP o RAP, siempre que el controller esté corriendo una versión de ArubaOS compatible. 
    
    * Ejemplo: `convert-aos-ap CAP 192.168.1.196` lo convierte a CAP apuntando al controller con esa IP. 

1. El AP y el Controller deben estar en el **mismo dominio regulatorio** (regulatory domain). Si no, la conversión puede fallar. 
2. El firmware del controller debe ser lo suficientemente nuevo (por ejemplo, ArubaOS versión ≥ cierta release) para soportar la operación `convert-aos-ap`. 
3. Compatibilidad de imagen: si conviertes, el AP descargará la imagen (firmware) desde el controller automáticamente al hacer `convert-aos-ap`. 
4. Es necesario que la red permita que el AP llegue al controller (que la IP del controller sea accesible, que haya ruta, DNS si aplica, etc.). 

El AP descargará automáticamente el firmware adecuado desde el controller, hará reboot, y al reiniciar operará como CAP / Remote AP apuntando al Controller.

#### IAP to CAP: GUI

Instant AP to Campus AP conversion:

1. Go to the Maintenance > Convert page.
2. Select Campus APs managed by a Mobility Controller from the Convert one or more Access Points to drop-down list.
3. Enter the host name, FQDN, or the IP address of the controller in the Hostname or IP Address of Mobility Controller text box. Contact your local administrator to obtain these details.
4. Click Convert to complete the conversion.
5. Click OK to confirm the conversion. The Instant AP reboots and begins operating in the Campus AP mode. After conversion, the Instant AP is managed by the Mobility Controller.

<img width="1919" height="825" alt="image" src="https://github.com/user-attachments/assets/8f06b185-51aa-4b38-931a-550f9ecdbdf0" />

<img width="671" height="222" alt="image" src="https://github.com/user-attachments/assets/ec0cbe77-3a1d-434a-b19b-2d3304a3ad28" />

<img width="269" height="170" alt="image" src="https://github.com/user-attachments/assets/cfe4357f-3189-4630-b5a7-4b738865cc6c" />

El Ap aparecerá automáticamente en la controladorA: 


**OJO!!!** Si por alguna razon no aparece, entrar por SSH a la MC (no a la MM!!) y lanzar el comando, por ejemplo aqui el error es porque aún no cargo ninguna licencia, y no aparece en GUI, pero en CLI aparece como "denied". 

````
(MGD-DEV::MC-Fz3r0-1) #show ap database

AP Database
-----------
Name               Group    AP Type  IP Address     Status  Flags  Switch IP      Standby IP
----               -----    -------  ----------     ------  -----  ---------      ----------
f4:2e:7f:c8:30:f4  default  515      10.10.130.101  Denied         192.168.1.196  0.0.0.0           <<<<<<<<<<-------------------- OJO!!!!

Flags: 1 = 802.1x authenticated AP use EAP-PEAP;   1+ = 802.1x use EST;    1- = 802.1x use factory cert
       2 = Using IKE version 2;                    4 = WiFi Uplink
       B = Built-in AP;                            C = Cellular RAP;       D = Dirty or no config
       E = Regulatory Domain Mismatch;             F = AP failed 802.1x authentication
       G = No such group;        I = Inactive;     J = USB cert at AP;     L = Unlicensed
       M = Mesh node
       N = Duplicate name;       P = PPPoe AP;     R = Remote AP;          R- = Remote AP requires Auth
       S = Standby-mode AP;      T = Thermal ShutDown;    U = Unprovisioned;    X = Maintenance Mode
       Y = Mesh Recovery
       b = bypass of AP1x timeout;    c = CERT-based RAP;    e = Custom EST cert;    f = No Spectrum FFT support
       i = Indoor;                    o = Outdoor;           l = LAG 802.3ad;        m = Protocol Mismatch
       p = In deep-sleep status;      r = Power Restricted;  s = LACP striping;      t = Temperature Restricted
       u = Custom-Cert RAP;           z = Datazone AP

Total APs:1
(MGD-DEV::MC-Fz3r0-1) #
````

Yo tuve que meterlo a la whitelist a mano (aunque ya me pare´cia dentro pero aun asi apliqye el comando)
Y además poner el certificado yo como valido:

````py
! # Crear whitelist (quizás ya esté creada)
whitelist-db cpsec add mac-address f4:2e:7f:c8:30:f4 ap-group default ap-name Lab-AP515

! # approved manual
whitelist-db cpsec modify mac-address f4:2e:7f:c8:30:f4 state approved-ready-for-cert
````


### De CAP a IAP (modo standalone / Instant lab):**

1. Verifica que el modelo/AP tenga soporte para modo IAP (AP-515 lo tiene en muchas entregas).
2. Si el AP no detecta un controller o ha sido reseteado, al arrancar puede volver a levantarse en modo IAP (especialmente si lo traías configurado como Instant anteriormente). 
3. Si necesitas forzar la conversión, busca en la GUI del controller la opción “Convert to Instant mode” para ese AP, si tu versión la tiene. También podría requerirse un preload de la imagen Instant si el AP no tiene ya esa parte de firmware.




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

- https://arubanetworking.hpe.com/techdocs/Archived/Instant-AOS-8/Instant_83_WebHelp/Content/Instant_UG/IAP_maintenance/ConvertingIAPtoCAP.htm

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

