# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - AOS 8x Architecture`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility``AP Provisioning``PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba Mobility :: `AOS 8x Architecture`

Aruba 8.x Architecture introduces a centralized and scalable design where the **Mobility Master (MM)** acts as the central brain for configuration, licensing, monitoring, and upgrades, while the **Mobility Controllers (MC)**, also known as **Managed Nodes (MN)** when under an MM, handle APs and client traffic. Using a **hierarchical configuration model**, all policies flow top-down from the MM, enabling flexibility across global, regional, and site levels, with deployment options ranging from a single MM with multiple MCs to redundant MMs for high availability.

## 🧠 Mobility Master (MM)

**Definition:** The central brain of the Aruba 8.x architecture. It does not handle client traffic but manages the configuration, licenses, monitoring, and upgrades of all Mobility Controllers (MC).  

**Functions:**  

- **Hierarchical Configuration Model:** Configuration flows top-down, from the MM to the MCs (Managed Nodes).  
- **Centralized Licensing:** The MM acts as a license server and distributes licenses to all MCs.  
- **Centralized Image Upgrades:** Software images are uploaded once to the MM and distributed to all MCs.  
- **Centralized Visibility & Monitoring:** A single dashboard for APs, clients, and network policies.  
- **Multi-Version Support:** An MM can manage MCs running different, but compatible, versions of ArubaOS.  

⚠️ **Note:** APs never connect directly to an MM. Only MCs terminate AP tunnels and handle client data (in case the AP is tunneled).

## 📦 Mobility Controller (MC) / Managed Node (MN)

**Definition:** The device that terminates AP tunnels, authenticates clients, and handles client traffic (if tunneled).  

- When standalone, it is simply called an **MC**.  
- When connected under an MM, it becomes a **Managed Node (MN)**.  
- In some Aruba documentation, you will also see the term **Managed Device (MD)**, which is used interchangeably with **Managed Node (MN)**.

**Role in the hierarchy:**  

- Inherits configuration from the MM.  
- Receives licenses from the MM.  
- Runs the control plane + data plane for APs and clients.

✅ **Key Point:** Every MN is an MC, but not every MC is an MN **(only when managed by an MM)**.  

## 🗂️ Hierarchical Configuration Model

**Concept:** Configuration is structured and flows from the top down.  

1. **Global (root at MM):** Policies and parameters applied to all nodes.  
2. **Folders (e.g., geo-loc1, geo-loc2):** Logical separation by region or function.  
3. **Groups (e.g., site1, site2):** Site-specific configuration.  
4. **MC/MN:** The final node that enforces configuration and serves APs and clients.  

**Advantages:**  

- Centralized and scalable management.  
- Flexibility to apply global, regional, or site-specific settings.  
- Reduces misconfiguration and improves consistency.

## 🏛️ Deployment Designs

### 1️⃣ One MM with Multiple MCs

- The most common enterprise design.  
- One MM at HQ, managing several MCs deployed at different data centers or branches.  
- All licenses, policies, and upgrades flow from the MM.  

### 2️⃣ Redundant MMs with Multiple MCs

- Recommended for high availability.  
- Two MMs in a cluster (Primary/Backup).  
- If one MM fails, the other continues managing licensing, configuration, and monitoring.  
- MCs remain operational, connected to APs and clients without disruption.  

### 3️⃣ Standalone MC

- A single MC without an MM.  
- Manages APs and clients directly.  
- Simpler, but lacks hierarchical configuration, centralized licensing, and unified upgrades.  

## 📊 MM vs MC (Summary)

| ⚙️ Feature               | 🧠 Mobility Master (MM)                     | 📦 Mobility Controller (MC) / Managed Node (MN) |
|--------------------------|----------------------------------------------|------------------------------------------------|
| Role                     | Centralized configuration, licensing, upgrades| Terminates AP tunnels, authenticates users, handles client traffic |
| Handles APs/Clients      | ❌ No                                        | ✅ Yes                                         |
| Visibility & Monitoring  | Global, centralized                          | Local (site-level)                             |
| Licenses                 | Acts as license server                       | Receives licenses from MM                      |
| Version Support          | Can manage MCs with different versions       | Must run a compatible ArubaOS version          |
| Hierarchy Name           | Root / Top node                              | Managed Node (MN) when under MM                |

## 🤔 What happens if you configure directly on the MC insteaf of MM?

In Aruba 8.x with Mobility Master, the **Hierarchical Configuration Model** rules.  

This means that any configuration made **directly on the MC (Managed Node)** will be **overwritten by the MM** the next time the config syncs.  

Configuring directly on a Mobility Controller (MC/MM) instead of the Mobility Master (MM) bypasses the centralized management, leading to configurations not being inherited by other controllers or the network, potentially causing inconsistencies and a loss of the benefits of the hierarchical architecture, such as simplified deployment and license management. While it may not immediately impact client traffic, it undermines the system's scalability and reliability by removing the single point of configuration for global policies and dynamic license allocation.

- **Note**: If you configure directly on an MC that’s managed by an MM, the MM will **push its own config down and override it**, unless that config is specifically allowed to be local.

### 🔎 Why?

- The MM is the **single source of truth** for configuration.  
- The MC is not meant to keep its own independent config once it’s registered to an MM.  
- When you try to configure something on the MC CLI, you’ll often see a warning like:  
  *“This node is managed by Mobility Master. Configuration must be done at the MM.”*  

### 🤔 What to do?

- Use the Mobility Master for all configurations: for the network's global policies and settings. 
- Manage individual devices (APs and controllers): through the Mobility Master to maintain consistency and leverage the system's full capabilities. 
- Implement redundancy: by using a backup Mobility Master with VRRP to ensure seamless connectivity and management in case of a primary MM failure. 

### 📝 Exceptions

Some local/site-specific commands can be executed on the MC, such as:  
- Debugging commands (`show`, `debug`).  
- Temporary troubleshooting tweaks (packet captures, logs).  

But **persistent configuration** (VLANs, SSIDs, roles, policies) must be done at the MM level.

## 🖼️ ADiagrams

### One MM with Multiple MCs

<img width="773" height="347" alt="image" src="https://github.com/user-attachments/assets/ab90ee75-d8f3-4a59-9afb-6cfb90b4add6" />

### Two MMs for HA with Multiple MCs

<img width="1024" height="791" alt="image" src="https://github.com/user-attachments/assets/0ff7472e-2870-4219-9b1d-c6fe932059b3" />


---

# 🗃️ Resources

- https://arubanetworking.hpe.com/techdocs/ArubaOS-8.x-Books/89/ArubaOS-8.9.0.0-User-Guide.pdf
- https://arubanetworking.hpe.com/techdocs/Archived/AOS-8/ArubaOS_85_Web_Help/Content/arubaos-solutions/rap/und-rap-modes.htm
- https://www.netprojnetworks.com/arubaos-8-x-configure-communication-between-mobility-master-and-managed-devices-md-controllers/

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
