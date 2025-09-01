# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - AP Modes: CAP, RAP, IAP, Mesh, AM, SA`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility` `AP Provisioning` `PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba Mobility :: `AP Modes: CAP, RAP, IAP, Mesh, AM, SA`

Aruba APs can operate in multiple modes depending on the network design, site requirements, and whether a controller is present. Each mode changes how the AP discovers its configuration, how client traffic is handled, and what level of dependency it has on centralized infrastructure.  

Understanding the differences between CAP, RAP, IAP, Mesh, AM, and SA is essential to deploying Aruba WLANs correctly. Choosing the right mode ensures that security, roaming, performance, and resiliency align with the use case—whether it’s a large campus with centralized controllers, a small branch office, or a fully remote user setup.

<img width="942" height="428" alt="image" src="https://github.com/user-attachments/assets/007666c6-aaed-47d3-92d6-c0c7b437ea89" />

## 📡 Campus AP (CAP)

- **Definition:** A Campus AP operates in a *controller-dependent* mode. 
- **Location:** Same LAN / site as the Mobility Controller (MC/MM).
- **Process:**
   - Discovers the Controller via DHCP Option 43, DNS, or broadcast.
   - Downloads its configuration directly from the Controller.
   - Client traffic is typically tunneled to the Controller (GRE/IPSec).
- **Services:** Security, roles, AAA profiles, firewall policies, and VLAN assignments are centrally enforced by the Controller.
- **Cisco Equivalent:** Lightweight AP (LAP).
- **Ruckus Equivalent:** Ruckus AP managed by **SmartZone** on-premise (on-site).

### ✅ Campus AP (CAP) :: **Advantages**

- Centralized management, easier troubleshooting, and consistent policy enforcement.
- Supports fast roaming (802.11r/k/v) since mobility is managed by the Controller.

### ⚠️ Campus AP (CAP) :: **Limitations**

- Full dependency on the Controller—if it's down, CAPs cannot service clients.
- Requires reliable, low-latency connectivity to Controller.

## 🌐 Remote AP (RAP)

- **Definition:** Extends WLAN services to a *remote location* without a local Controller.
- **Location:** Remote branches, home offices, or non-campus sites.
- **Process:**
   - Connects to the Controller over WAN, Internet, or MPLS.
   - Establishes an IPSec tunnel to the Controller.
   - Downloads configuration and offers the same SSIDs as a campus-controlled environment.
- **Services:** Roles, VLANs, and policies are centrally managed—same as CAP.
- **Cisco Equivalent:** REAP / FlexConnect (legacy).
- **Ruckus Equivalent:** Ruckus AP managed by a remote vSZ High Scale.

### ✅ Remote AP (RAP) :: **Advantages:**

- Enables a full corporate wireless experience in remote locations.
- Centralized security/policy enforcement without need for local Controller.
- Supports **split-tunnel**, sending corporate traffic back to Controller, while Internet traffic exits locally.

### ⚠️ Remote AP (RAP) :: **Limitations:**

- Depends heavily on stable WAN or Internet connectivity.
- Latency and bandwidth limitations can impact performance.

## 🔌 Instant AP (IAP)

- **Definition:** Works in an autonomous or controller-less mode—no Controller needed.
- **Virtual Controller (VC):** Within a cluster, one IAP becomes the VC and manages the rest.
- **Use Cases:** Small offices or sites where deploying a Controller isn't cost-effective.
- **Cisco Equivalent:** Autonomous AP (older IOS APs running standalone).
- **Ruckus Equivalent:** **Ruckus Unleashed APs** (cluster elects a Master AP that manages others).

## 📶 Other Modes

**Mesh Portal / Mesh Point:** Extend WLAN via wireless backhaul (no Ethernet).  

- **Cisco Equivalent**: Mesh AP (MAP/RAP).  
- **Ruckus Equivalent**: Mesh APs under SmartZone or Unleashed mesh topology.  

**Air Monitor (AM):** RF sensor AP to scan for rogue APs and perform IDS/IPS.  

- **Cisco Equivalent:** AP in Monitor Mode.
- **Ruckus Equivalent:** Packet Catpure Option or AP Monitor Mode.

**Spectrum AP (SA):** Dedicated to spectrum analysis—detects RF interference sources like microwaves and Bluetooth.  

- **Cisco Equivalent:** CleanAir Spectrum Expert Mode.  
- **Ruckus Equivalent:** Spectrum Analysis tool in SZ/Unleashed.  

## 📊 Aruba AP Modes :: CAP vs RAP

| ⚙️ Feature               | 🏠 CAP (Campus AP)                | 🌍 RAP (Remote AP)                          |
|--------------------------|-----------------------------------|----------------------------------------------|
| Location                 | Same LAN / same site as Controller| Remote site via WAN/Internet/MPLS            |
| Controller Discovery     | DHCP / DNS / Broadcast            | IPsec tunnel to Controller                   |
| Configuration Source     | Downloads config from Controller  | Downloads config from Controller             |
| User Traffic Handling    | Fully tunneled to Controller      | Tunneled to Controller or Split-Tunnel       |
| Cisco Equivalent         | LAP (Lightweight AP)              | REAP / FlexConnect                           |
| Ruckus Equivalent        | ZoneFlex AP (SmartZone-managed)   | Flex Mode / GRE Tunnel to DC                 |
| WAN Dependency           | Low (local LAN)                   | High (stable WAN required)                   |
| Installation Flexibility | At campus site                    | Anywhere with Internet connectivity          |
| Latency Impact           | Minimal (LAN latency <1–2 ms)     | Higher (WAN/Internet latency can affect users)|
| Roaming Support          | Controller-based fast roaming     | Limited by WAN delay; roaming not optimal    |
| Scalability              | High – thousands of CAPs per MC   | Lower – limited by WAN bandwidth & tunnels   |

---

# 🗃️ Resources

- https://arubanetworking.hpe.com/techdocs/ArubaOS-8.x-Books/89/ArubaOS-8.9.0.0-User-Guide.pdf
- https://arubanetworking.hpe.com/techdocs/Archived/AOS-8/ArubaOS_85_Web_Help/Content/arubaos-solutions/rap/und-rap-modes.htm

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
