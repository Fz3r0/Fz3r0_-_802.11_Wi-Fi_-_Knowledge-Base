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



### `Step 1`: Crear la VLAN que llevará mi WLAN/SSID

- La VLAN será la que transporte esta red, del lado del backbone esta VLAN tiene que estar configurada en el DHCP en caso de estar en modo bridge, o existir en la controladora en caso de estar tunneled.
- Es decir, la VLAN debe coincidir ya sea con la controladora o la LAN

**Grupo > Sub-Grupo > Configuration > Interfaces > VLAN:**

<img width="1919" height="766" alt="image" src="https://github.com/user-attachments/assets/e0ee79f3-afbd-459a-90d5-410de97bfbec" />

Agregar el VLAN ID y un nombre identificador y hacer deplot de los cambios

- Nota: Mas adelante se podrá seleccionar la VLAN tanto por el nombre como por el número. 

<img width="1269" height="530" alt="image" src="https://github.com/user-attachments/assets/118877f5-fd99-4bfe-a622-32bb1292aaf3" />

### `Step 2`: Configurar WLAN (SSID)

- Al principio no existirá ninguna WLAN ya que no hemos creado ninguna

**Grupo > Sub-Grupo > Configuration > WLANs:**










<img width="1919" height="767" alt="image" src="https://github.com/user-attachments/assets/eed65a02-8b77-4dc1-ada4-07cb22236875" />

### `Step 2`: Seleccionar el grupo de manera  jerarquica donde se quiere configurar







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
