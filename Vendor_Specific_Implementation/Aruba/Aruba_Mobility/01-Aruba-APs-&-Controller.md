# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - Access Points (APs) and Wireless LAN Controller (WLC)`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility` `AP Provisioning` `PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba Mobility :: `Access Points (APs) and Wireless LAN Controllers (WLC)`

Aruba offers a wide portfolio of Access Points designed for **different environments and use cases**. Broadly, APs are categorized as **indoor** or **outdoor** models. While their Wi-Fi capabilities are often similar (support for 802.11a/b/g/n/ac/ax, multiple radios, MIMO chains), their **physical design, durability, uplink options, and cost** vary significantly depending on the deployment scenario.

## 🏠 Indoor APs

- **Purpose:** Designed for climate-controlled environments like offices, hospitals, schools, and retail spaces.  
- **Enclosure:** Lightweight plastic housing, aesthetic design, and ceiling/wall mounting.  
- **Antennas:** Can be **integrated** or **external** depending on the model (e.g., AP-325 internal vs AP-324 external).  
- **Power & Ports:** Usually dual copper Ethernet ports (1G or 2.5G), with **PoE-in** and sometimes **LACP**. Optional DC input.  
- **Cost:** Cheaper than outdoor APs because they don’t require ruggedization.  
- **Use Cases:** High-density office floors, classrooms, auditoriums, healthcare, or warehouses.

## 🌦️ Outdoor APs

- **Purpose:** Ruggedized for harsh environments: stadiums, ports, parking lots, outdoor campuses, industrial yards.  
- **Enclosure:** Weather-sealed **IP-rated chassis** with surge protection, UV resistance, and extended temperature range (**–40 °C to +65 °C**).  
- **Antennas:** Typically external or integrated into directional/omni outdoor housings.  
- **Power & Ports:** At least one copper **PoE-in** port, often complemented by an **SFP slot (1G fiber)** for longer uplinks.  
- **Cost:** Higher due to environmental certification, rugged chassis, and mounting hardware.  
- **Use Cases:** Long-distance mesh links, outdoor Wi-Fi coverage, stadium/arena density, mining/industrial connectivity.

## 💡 Aruba APs Design Notes

- **Regulatory Domains:** Aruba APs ship with domain codes (e.g., `-US` for United States, `-RW` for Rest of World, `-IL` for Israel, `-JP` for Japan). The domain defines allowed channels and Tx power.  
- **SSIDs:** Up to **16 per radio**, but best practice is ≤4 to minimize beacon overhead.  
- **Power Considerations:** With **802.3bt (PoE++)**, all features are enabled. With **802.3af (basic PoE)**, the AP may disable features like USB or a radio, managed by **IPM (Intelligent Power Monitoring)**.  
- **USB Port:** Typically USB 2.0; rarely used in enterprises except for 4G/LTE modems.  

### 🌍 Regulatory/Ordering Regions

Common suffixes on SKUs: **-US** (United States/FCC), **-RW** (Rest of World), **-JP** (Japan), **-IL** (Israel).  
> Region is enforced in hardware; **-RW cannot be used in the US**.

## 📦 Example Indoor Model — Aruba **AP-515** (510 Series)

**Platform:** Dual-radio Wi-Fi 6 (802.11ax); backward compatible with a/b/g/n/ac.  
**Radios/MIMO:** 2.4 GHz **2×2:2**, 5 GHz **4×4:4**.  
**Antenna Options:**  
- AP-514 → external antennas.  
- AP-515 → integrated antennas.  
**SSIDs:** Up to **16 per radio**.  
**IoT:** BLE + Zigbee built-in.  
**Ports:**  
- **E0:** 2.5G PoE-in (802.3af/at/bt).  
- **E1:** 1G, no PoE.  
- LACP supported on E0+E1.  
**Other:** DC input (priority over PoE), USB-A 2.0 (~5W), micro-USB console.  
**Power/IPM:**  
- With 802.3bt/at/DC → no restrictions.  
- With 802.3af → works with reduced features under IPM.  

## 📊 Side-by-Side Comparison of Three Aruba APs

| Feature | **AP-325** (Indoor 320 Series) | **AP-515** (Indoor 510 Series) | **AP-375** (Outdoor 370 Series) |
|---------|--------------------------------|--------------------------------|--------------------------------|
| Wi-Fi Gen | 802.11ac Wave 2 | **802.11ax (Wi-Fi 6)** | 802.11ac Wave 2 |
| Radios/MIMO | 2.4 GHz 4×4:4 / 5 GHz 4×4:4 | 2.4 GHz 2×2:2 / 5 GHz 4×4:4 | 2.4 GHz 2×2:2 / 5 GHz 4×4:4 |
| Antennas | AP-324 external / AP-325 internal | AP-514 external / AP-515 internal | AP-374 external / AP-375 internal |
| Max PHY | 1.73 Gbps | **2.69 Gbps** | 1.73 Gbps |
| Clients (per radio) | 256 | **512** | 256 |
| SSIDs (per radio) | 16 | 16 | 16 |
| Uplinks | 2×1G, PoE on both | 1×2.5G (PoE), 1×1G (no PoE) | 1×1G PoE, 1×SFP fiber |
| Power | PoE/802.3at, DC input | PoE/802.3bt, DC input | PoE (802.3at/bt), DC input |
| Environment | Indoor (office, schools) | Indoor (dense enterprise, Wi-Fi 6) | Outdoor (harsh env, stadiums) |
| Min. AOS | 6.4.4.0 | 8.4.4.0 | 8.3.0.0 |

## 🔔 LED Status

_AP-510 Series Installation Guide; AP-510 datasheet/brief._

**System LED**

| State | Meaning |
|---|---|
| **Off** | AP powered off |
| **Green (solid)** | Ready, fully functional |
| **Green (blinking)** | Booting, not ready |
| **Green (fast flash)** | Ready; uplink negotiated **< 1 Gbps** |
| **Amber (solid)** | Ready in **restricted power** (PoE/IPM) |
| **Amber (blinking)** | Restricted power **and** uplink < 1 Gbps |
| **Red** | System error — attention required |

**Radio LED**

| State | Meaning |
|---|---|
| **Off** | Radios off/disabled |
| **Green (solid)** | Both radios in **access** mode |
| **Green (blinking)** | One radio access, other disabled |
| **Amber (solid)** | Both radios in **monitor** mode |
| **Amber (blinking)** | One radio monitor, other disabled |
| **Alt Green/Amber** | One radio access, one monitor |


## 🛠️ Controllers — MM & MC (Virtual vs Hardware Controllers)

Aruba offers both **virtual** and **hardware** appliances for its controller architecture. The choice depends on **scale, resiliency, and deployment model**. Both support the same ArubaOS 8.x features (MM hierarchy, licensing, configuration model), but they differ in **performance, form factor, and scaling capacity**.

- **Mobility Master (MM):** Top of the **hierarchical configuration model**; centralizes **configuration**, **licensing**, **image upgrades**, and **visibility/monitoring**. Supports **multi-version** domains. **APs do not join the MM**.  
- **Mobility Controller (MC):** Terminates AP tunnels and handles **client control/data plane** (roles/ACL/AAA, VLANs, DHCP relay, etc.). _(Also known as Managed Node/Device (MN/MD))_

## 📂 Mobility Master (MM)

The **Mobility Master** is always at the top of the hierarchy. It centralizes **configuration, licensing, and monitoring**, and manages one or more **Mobility Controllers (MCs)** (which become Managed Nodes under MM).

### ☁️ Virtual MM (MM-VA)

- Deployed on VMware ESXi, Microsoft Hyper-V, or KVM.
- Scales based on SKU: `MM-VA-50 / 500 / 1K / 5K / 10K`.
- Licensing defines capacity in **number of devices (MCs)** and **clients**.

Example:  

- `MM-VA-50`: supports 50 devices, ~500 clients, 5 controllers.  
- `MM-VA-1K`: supports 1,000 devices, ~10,000 clients, 100 controllers.  
- `MM-VA-10K`: supports 10,000 devices, ~100,000 clients, 1,000 controllers.

### 🪨 Hardware MM (MM-HW)

- Purpose-built appliance with console, management, and **10G SFP+ ports**.
- Models: `MM-HW-1K / 5K / 10K`.

Example:  

- `MM-HW-1K`: 1,000 devices, 10,000 clients, ~100 controllers.  
- `MM-HW-10K`: 10,000 devices, 100,000 clients, ~1,000 controllers.
- Offers **dedicated compute power** and avoids shared virtualization overhead.

## 📦 Mobility Controller (MC)

The **Mobility Controller** terminates AP tunnels, authenticates clients, and enforces policies. When connected to an MM, it is called a **Managed Node (MN)**. MCs can be either **virtual** or **hardware appliances**.

### ☁️ Virtual MC (MC-VA)

- Deployed on the same hypervisors as MM-VA (ESXi, Hyper-V, KVM).
- SKU depends on license and compute resources.
- Ideal for **lab environments**, **small branches**, or **cloud-first strategies**.

### 🪨 Hardware MC

- **7000 Series:** Compact branch/SMB controllers.  
  - Examples: 7005, 7008, 7010, 7024, 7030.  
  - Scale: up to ~4,096 users, with PoE ports for small sites.

- **7200 Series:** High-performance enterprise controllers.  
  - Examples: 7205, 7210, 7220, 7240XM, 7280.  
  - Scale: up to ~32,768 concurrent users.  
  - Multiple 10G SFP+ uplinks, larger session handling, high-density support.

## 📊 Virtual vs Hardware — Quick Comparison

| Feature | **Virtual MM/MC** | **Hardware MM/MC** |
|---------|-------------------|--------------------|
| **Deployment** | Runs on hypervisors (ESXi, KVM, Hyper-V). | Dedicated appliance with ArubaOS preloaded. |
| **Performance** | Scales with compute (CPU/RAM); overhead of virtualization. | Predictable throughput with optimized hardware. |
| **Networking** | Uses VM NICs (limited by host capabilities). | 1G/10G/40G ports, hardware acceleration. |
| **Scale** | MM-VA up to 10k devices / 100k clients. | MM-HW up to 10k devices / 100k clients. |
| **Use Case** | Labs, small/medium enterprises, cloud-centric. | Large campuses, DC hubs, high-density enterprise. |
| **Cost** | Lower upfront (reuse existing virtualization). | Higher upfront, but dedicated and robust. |

## 🏗️ Deployment Hierarchies

- **Single MM + multiple MCs** → centralized config/licensing with scalability.  
- **Dual (redundant) MMs + multiple MCs** → high availability, config/state sync.  
- **Standalone MCs** (no MM) → simpler, but lose centralized licensing and hierarchy.

## ✅ Key Takeaways

- **Same ArubaOS**: Both virtual and hardware platforms run the same ArubaOS 8.x features.  
- **MM = brains** (hierarchy, licensing, visibility); **MC = muscle** (tunnel termination, client handling).  
- **Virtual = flexibility & cost efficiency**, **Hardware = predictable performance & scale**.  

---

# 🗃️ Resources

- https://arubanetworking.hpe.com/techdocs/ArubaOS-8.x-Books/89/ArubaOS-8.9.0.0-User-Guide.pdf
- https://www.hpe.com/psnow/doc/PSN1011094558WWEN
- https://www.manual.pe/aruba/ap-515/manual?p=3
- https://arubanetworking.hpe.com/techdocs/hardware/aps/ap510/ig/AP-510_Install_Guide_EN.pdf
- https://www.hpe.com/us/en/aruba-access-points.html
- https://community.arubanetworks.com/discussion/virtual-mobility-controller-vmc-vs-hardware-mobility-controller
- https://community.arubanetworks.com/discussion/arubaos-8x-mm-virtual-vs-hardware

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
