# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - AP Groups`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility` `AP Provisioning` `PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba Mobility :: `AP Groups`

Aruba WLAN AP-Groups are a central feature that allows administrators to manage, configure, and optimize large numbers of Access Points (APs) simultaneously. AP-groups are one of the most important mechanisms for managing large wireless environments. 

- **Instead of configuring each AP individually, AP-Groups provide a logical container where common settings are applied and inherited, ensuring consistency across the network. This model greatly simplifies wireless operations in both small and large deployments.**

These groups share configuration profiles, which ensures consistency, scalability, and centralized management across hundreds or even thousands of APs.

## ❓ Definition and Purpose

- An **AP-Group** is a logical collection of Aruba Access Points that share the same configuration profile.  
- Key idea: **configure once, apply to many**.  

This design streamlines deployment and ensures that all APs within a group follow the same settings, making WLAN management predictable and efficient.

When an AP boots up and joins the controller, it automatically inherits all policies, SSIDs, VLANs, and RF settings from its assigned AP-Group.  

- Think of an AP-Group as the "template" for multiple APs.  
- Changes applied at the AP-Group level instantly propagate to all APs inside it.  
- Each AP belongs to exactly **one AP-Group**.  

## 🌟 Benefits of Using AP-Groups

- **Simplified management** – manage multiple APs as a single unit.  
- **Consistent configuration** – apply the same SSIDs, VLANs, and radio settings to all APs in the group.  
- **Scalability** – easily add or remove APs without redefining settings.  
- **Flexibility** – create specific groups for different sites, floors, or user types.  
- **Performance optimization** – fine-tune RF, QoS, and security policies per group.

| 🌟 Benefit                   | 📝 Description                                     |
|-------------------------------|----------------------------------------------------|
| **Simplified management**     | Manage multiple APs as one unit                    |
| **Consistent configuration**  | Apply uniform settings across grouped APs          |
| **Scalability**               | Add/remove APs from groups easily                  |
| **Flexibility**               | Tailor configs for specific areas or user types    |
| **Performance optimization**  | Optimize SSIDs, RF, and QoS settings per group     |

## ⚙️ Components of an AP-Group

Each AP-group in Aruba can include multiple configuration layers:

- 📡 **`WLAN & SSID assignments`** (one or many per group, up to 16 per radio)  
- 🛜 **`RF Radio Management Settings`** (channel, power, band steering, airtime fairness)  
- 🔐 **`Security policies`** (encryption, 802.1X, PSK, firewall rules)  
- 🚦 **`QoS and Bandwidth Control`** (traffic shaping, bandwidth limits, voice prioritization)  
- 🛣️ **`VLANs and Segmentation`** (network segmentation and logical traffic separation)  

These components define how APs in the group operate and what services they provide.

### 📡 `WLAN & SSID assignments`

- ⭕ Multiple SSIDs per AP-Group (up to 16 per radio).  
- ⭕ Example: `Corp-WiFi` (WPA3-Enterprise) + `Guest-WiFi` (Captive Portal).  

### 🛜 `RF Radio Management Settings

RF management is critical for wireless performance. Aruba allows per-group tuning:

- ⭕ **Channel selection** : Channel planning   
- ⭕ **Transmit power** : Optimize coverage 
- ⭕ **Band steering** : Encourage 5 GHz clients for better capacity
- ⭕ **Airtime fairness** : (balance resources between fast and slow clients)

### 🔐 `Security policies`

- ⭕ WPA2/WPA3 encryption  
- ⭕ 802.1X or PSK authentication  
- ⭕ Firewall rules at the AP level  
- ⭕ IDS/IPS intrusion protection  

### 🚦`QoS and Bandwidth Control`

- ⭕ Prioritize applications (voice, video, business-critical traffic)  
- ⭕ Limit bandwidth per SSID or per user  
- ⭕ Ap plication-aware policies  
- ⭕ Call admission control for VoIP  

### 🛣️ `VLANs and Segmentation`

- ⭕ Logical traffic separation  
- ⭕ Enhanced security via isolation  
- ⭕ Easier management of resources  

## ✅ Aruba AP Groups :: `Best Practices`

- ⭕ **Logical grouping**: create AP-groups by building, floor, department, or user type (e.g., employee vs guest).  
- ⭕ **Scalability**: plan ahead for growth using templates and hierarchical groups.  
- ⭕ **Consistency**: apply baseline settings across all groups, then customize where needed.  
- ⭕ **Centralization**: always manage from Mobility Master (MM) when in use, never directly on MCs.

## 🔒 Advanced AP-Group Features

- **Role-Based Access Control (RBAC)** – apply roles/policies per user, device, or location.  
- **Adaptive Radio Management (ARM)** – auto-optimization of channels, power, and load.  
- **AP Load Balancing** – distribute clients to prevent AP overload.  
- **Captive Portal Integration** – custom login pages, external auth servers, usage tracking.  










<img height="250" alt="image" src="https://github.com/user-attachments/assets/86749933-9ba6-4a63-b4fb-cca3519acf19" />

<img height="250" alt="image" src="https://github.com/user-attachments/assets/aed4c470-7e07-4b67-9cea-988241454fce" />




# ⚙️ How to Set Up an AP-Group

1. Log in to the Aruba controller (MM/MC) interface.  
2. Navigate to **Configuration → AP Groups**, and click ++"+"++.
3. 
<img height="250" alt="image" src="https://github.com/user-attachments/assets/e25abbe8-5d0d-4e85-bf2b-e43ca299cc8a" />

4. Create a new AP-Group, assign a descriptive name, and push the changes. _For this point, the AP group **"ORION"** will already have been created, specifically within the sub-group **ALFA**, which in turn is inside the group **Site Controllers1.** In other words, the configurations will only be applied to the two MCs that are inside **ALFA**_

<img height="200" alt="image" src="https://github.com/user-attachments/assets/d79067c6-3150-4a25-b405-ad270b9f79ed" />

5. Configure WLANs, VLANs, and RF profiles for that group:

- **IMPORTANT!!! FIRST OF ALL YOU NEED TO ACTIVATE THE "SHOW ADVANCED PROFILE" OPTION AT TOP RIGHT CORNER**

<img height="150" alt="image" src="https://github.com/user-attachments/assets/dc787146-802d-4744-995b-b6ce19a52994" />

Then you can see the advanced profile tab:

<img width="2309" height="624" alt="image" src="https://github.com/user-attachments/assets/87cf4e02-0a26-4188-b577-47e8fb22b1b0" />



7. Assign APs to the group under **Access Points → Change Group**.  
8. Save and apply changes → APs reboot and adopt the new config.  














---

# 🗃️ Resources

- https://arubanetworking.hpe.com/techdocs/CLI-Bank/Content/aos8/sh-ap-ap-grp.htm
- https://networkwords.com/aruba-wlan-ap-group/

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
