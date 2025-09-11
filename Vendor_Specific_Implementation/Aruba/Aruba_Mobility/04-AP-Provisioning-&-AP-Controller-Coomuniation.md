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

👉 For **controller-based (CAP/RAP)** deployments, the AP cannot operate standalone, **it must discover and register with an MC/MM before becoming operational.**

## 2. First Connection of an AP to the LAN

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

