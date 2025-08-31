# 🧠🏗️🌐 Cisco Nexus: `NX-OS - VXLAN/EVPN @ Tier 3 Fabric - PT2 : PIM + Multicast + Final Underlay`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility``AP Provisioning``PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`

[🏗️ Cisco Nexus :: `NX-OS - VXLAN/EVPN @ Tier 3 Fabric - PT1 : OSPF Underlay + Essentials`](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#%EF%B8%8F-cisco-nexus--nx-os---vxlanevpn--tier-3-fabric---pt1--ospf-underlay--essentials-1)
- [🎯 Objectives, Features & Protocols Covered](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#-objectives-features--protocols-covered)
- [🎥 Lab Proof of Concept (PoC) - Video](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#-lab-proof-of-concept-poc---video)
- [🗺️ Network Topology](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#%EF%B8%8F-network-topology)
- [📋 Network Device Inventory, Interfaces & IP Addressing](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#-network-device-inventory-interfaces--ip-addressing)
- [📝 Lab Notes](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#-lab-notes)

[⚙️ Devices Configurations](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#%EF%B8%8F-devices-configurations)
- [👑🥇 `NX9-BGW-1A` - (Border Gateway - VPC-A)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-Nexus_3Tier-VXLAN-PT1_OSPF-Underlay+vPCs.md#-nx9-bgw-1a---border-gateway---vpc-a)
- [👑🥈 NX9-BGW-1B - (Border Gateway - VPC-B)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay%2BEssentials.md#-nx9-bgw-1b---border-gateway---vpc-b)
- [🩻🥇 NX9-SPINE-1 - (SPINE 1)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay%2BEssentials.md#-nx9-spine-1---spine-1)
- [🩻🥈 NX9-SPINE-2 - (SPINE 2)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay%2BEssentials.md#-nx9-spine-2---spine-2)
- [🌿🥇 NX9-LEAF-1A - (LEAF 1 - VPC-A)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay%2BEssentials.md#-nx9-leaf-1a---leaf-1---vpc-a)
- [🌿🥈 NX9-LEAF-1B - (LEAF 1 - VPC-B)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay%2BEssentials.md#-nx9-leaf-1b---leaf-1---vpc-b)
- [🌿🥇 NX9-LEAF-2A - (LEAF 2 - VPC-A)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay+Essentials.md#-nx9-leaf-2a---leaf-2---vpc-a)
- [🌿🥈 NX9-LEAF-2B - (LEAF 2 - VPC-B)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay+Essentials.md#-nx9-leaf-2b---leaf-2---vpc-b)
- [🔀🔑 IOS-SWITCH-MGMT - (Switch Layer 2 - Management)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay+Essentials.md#-ios-switch-mgmt---switch-layer-2---management)
- [🔄🌐 IOS-RT-WAN - (Router WAN)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay+Essentials.md#-ios-rt-wan---router-wan)
- [🌎🖧 WAN-1 - (Internet Circuit)](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay+Essentials.md#-wan-1---internet-circuit)

[**🗃️ Resources**](https://github.com/Fz3r0/Fz3r0_-_Cisco/blob/main/Cisco_Nexus/Cisco_Nexus_Labs/03.1-F0-NXOS_-_VXLAN-EVPN_Tier3-Fabric-PT1_OSPF%20Underlay+Essentials.md#%EF%B8%8F-resources)

# 🏗️ Cisco Nexus :: `NX-OS - VXLAN/EVPN @ Tier 3 Fabric - PT1 : OSPF Underlay + Essential Configs`

This lab represents **Phase 2** of a 4-part VXLAN/EVPN deployment built on a **3-tier Nexus fabric architecture** (Border Gateways, Spines, and Leafs). While it's based on a Tier 3 model, the concepts and configurations also apply to **Tier-2 topologies (Leaf-Spine)** with minimal adjustments.

While **Part 1** focused on bringing up the **UNICAST UNDERLAY** using **OSPF** routing across the fabric, in **Lab 2** we complete the underlay by introducing **MULTICAST support** using **PIM Sparse-Mode**, a key requirement to handle **VXLAN BUM (Broadcast, Unknown Unicast, and Multicast)** traffic. Key Concepts Introduced in This Lab will be: 

1. **`PIM Sparse-Mode`**: configured on **physical interfaces (ETH 1/x)** and **loopback0**  
  → `ip pim sparse-mode` <br><br>
2. **`Rendezvous Point (RP)`**: **Static-RP** or **Anycast-RP (used on this lab)**  
  → RP Assignment (for PIM Joiners): `ip pim rp-address <Loopback0-IP(Spine-1) or Anycast-IP(Both Spines for HA)>`  
  → Anycast (Only RPs (Spines)): `ip pim anycast-rp <loopback1-IP(Spine-2)> <loopback0-IP(Spine-1)>` 

## 👇 Underlay Components and Phases for configuration:

To build a reliable VXLAN underlay, you need two main components/phases, and this lab is structured accordingly:

### 1️⃣🛠️ **`Phase 1`** : Dynamic Routing for Unicast - OSPF Underlay 

This was already done in Lab 1. OSPF takes care of routing all unicast traffic across the fabric. This provides stable unicast IP routing between all Leafs, Spines, and BGWs

- **`OSPF underlay`**: For **unicast routing**. All devices (BGWs, Spines, Leafs) participate in OSPF (UNDERLAY-F0). <br><br>
- **`/31`**: /31 P2P OSPF with point-to-point links between all tier Nexus Switches. **End-to-end unicast connectivity** <br><br>
- **`loopback0 advertised in OSPF`**: Used for **RPF (Reverse Path Forwarding)** & accesibility. Ensure that traffic is forwarded along the correct path, preventing loops and improving network stability. <br><br> 
- **`Extras`**: Optional extra configs (ssh, hostnames, vPC, VRF, WAN/NAT, etc)

### 2️⃣🛠️ **`Phase 2`** : Multicast Routing for BUM Traffic - PIM Sparse Mode 

This is the focus of **Lab 2**. PIM enables VXLAN to replicate **BUM traffic** using multicast groups. This is essential for VXLAN to support unknown destination flooding in flood-and-learn environments.

> ⚠️ **Important**: Unlike unicast routing, multicast does *not* flood by default.  
> PIM handles discovery, group membership, and multicast routing between VTEPs.

These are the mandatory steps to accomplish phase 2 of the underlay network configuration:

1. `feature pim`: Enable PIM feature in Nexus switches. <br><br>
2. `ip pim sparse-mode` _(ALL Nexus)_: Enable **ip pim sparse-mode** on ALL routed interfaces participating in the fabric (**physical** + **loopback0**).
    - This complement the OSPF unicast underlay by enabling multicast routing with PIM Sparse Mode. <br><br>
3. `Anycast RP` / `loopback1` _(RPs = Spines Only)_: Anycast RP (using both spines as RPs) provides High Availability (HA/Redundancy).
   -  2 devices are set as **RPs (both Spines)**, using **loopback1** to set the **Anycast IP** (same IP for both Spines)
   -  **Loopback1** is also anounced in **OSPF UNDERLAY-FO Area0**, as part of the OSPF Underlay Network <br><br> 
4. Validate configuration checking for the nighbors and rp:
   - `show ip pim neighbor`
   - `show ip pim rp`

⚠️ **Important**: We will use 2 different loopbacks for this lab:

- **`loopback0`** used for RPF and as Router-ID.
- **`loopback1`** used for Anycast RP and must have the same IP on both Spines.

## 💦 How Multicast Flooding Works in VXLAN

Unlike simpler routed networks (e.g. Catalyst/CCNA-style labs), **VXLAN fabrics require multicast** to handle BUM traffic effectively.

🔄 Here’s how it works:

- Each **VTEP** (usually a Leaf) maps a **multicast group** to a VXLAN segment (VNID)  
- When a VTEP receives BUM traffic, it sends it to the multicast group  
- **PIM Sparse Mode** ensures all other VTEPs subscribed to that group receive the traffic  
- A **Rendezvous Point (RP)** coordinates delivery

> 💡 Spines are ideal RPs since they’re centrally located and always reachable

### 💻 Example VXLAN Flooding Flow:

1. **Leaf1** wants to flood BUM traffic for a VXLAN segment  
2. It maps that VXLAN to a **multicast group** (e.g. `239.1.1.10`)  
3. It sends the packet to the **RP** (e.g. Spine1)  
4. The RP checks which VTEPs are subscribed (e.g. Leaf2, Leaf3)  
5. Multicast replication happens, and **VXLAN tunnels** are formed  
6. All VTEPs in the group share **MAC learning and traffic reachability**
   
## 🤹‍♂️ `PIM (Protocol Independent Multicast)`

**PIM (Protocol Independent Multicast)** is the multicast routing protocol used by **VXLAN** to handle **BUM (Broadcast, Unknown Unicast, and Multicast)** traffic. In any VXLAN fabric, **PIM must be enabled in the underlay** using `PIM Sparse Mode`.

Originally developed in the mid-1990s by Cisco and other industry contributors, PIM is defined in **RFC 7761** (maintained by the IETF) and is fully **vendor-neutral**, supported by Cisco, Juniper, Arista, and more. It operates at **Layer 3** and is independent of any specific unicast routing protocol (hence the name *Protocol Independent*).

- PIM is enabled **per-interface**, just like OSPF or other IP-based protocols, and allows multicast packets to be routed across the fabric in a scalable and efficient way.

---

VXLAN encapsulates Layer 2 Ethernet frames into Layer 3 IP packets and requires a mechanism to replicate **flooded traffic** i.e., **BUM (Broadcast, Unknown Unicast, and Multicast)** across all **VTEPs (Virtual Tunnel Endpoints)** within the same **VXLAN segment (VNID - Virtual Network Identifier)**.

To enable this behavior, VXLAN traditionally uses **Multicast-based Flood-and-Learn**, where:

- Each VNID is mapped to a **unique multicast group IP**.
- When one VTEP receives a BUM frame, it replicates it to the multicast group.
- All other VTEPs subscribed to that group will receive the packet.

For this model to work properly, the underlay must include:

1. **✅ `Functional multicast control plane`**: Provided by **PIM Sparse-Mode**.  
2. **📡 `Multicast routing between all Nexus devices`**: Handled via **PIM** + **RPF (Reverse Path Forwarding)**.  
3. **🧭 `Rendezvous Point (RP)`**: Typically assigned to one or both **Spine switches**.

### 🧠 How it works in VXLAN:

- Each VXLAN segment (**VNID**) maps to a **multicast group**.
- All VTEPs (Leaf switches) must **join** these multicast groups to receive BUM traffic.
- PIM Sparse Mode manages the delivery of multicast packets only to interested receivers.
- A **central RP (Rendezvous Point)** acts as the coordinator to build the multicast tree.

## 🔀 PIM Operating Modes

![image](https://github.com/user-attachments/assets/bda33f95-5d88-4bfc-a555-2967452443f8)

### 1. 🚫 `Dense Mode`

- 🚫 Floods multicast traffic out **all interfaces**, even if no receivers exist.
- It does **not verify interest** — it just floods. Receivers can then respond and join the multicast group.

⚠️ **Not used in VXLAN**, this mode causes excessive traffic and poor scalability.

### 2. ✅ `Sparse Mode`

- Instead of flooding, one or more **Rendezvous Points (RPs)** are defined — usually on Spine switches.
- When a Leaf wants to send traffic to a multicast group (e.g., `239.1.1.1`), it queries the RP.
- The RP keeps track of interested receivers and builds the multicast distribution tree accordingly.

✅ **Sparse Mode is the recommended mode for VXLAN**, as it only forwards multicast traffic where needed, making it scalable, efficient, and optimized for large fabrics.

### PIM Configuration: RP Anycast (for High Availability RP)

### 🌐 PIM Configuration: Anycast RP (High Availability)

For high availability in VXLAN multicast deployments, it is common to configure two **Rendezvous Points (RPs)** — typically both Spine switches — using the **Anycast RP** technique.

In this model, both RPs share the **same IP address**, assigned to a dedicated loopback interface (commonly `loopback1`). 

- When a multicast join request is initiated by a Leaf or other PIM-enabled device, the traffic is routed to the closest available RP, based on the unicast routing topology. The device does not differentiate which Spine receives the request, as both advertise the same RP address.

This approach ensures **load sharing** and **seamless RP failover**, presenting a unified logical RP to the entire fabric.

![image](https://github.com/user-attachments/assets/3a463d24-5ea6-4185-9581-517240e0f795)

With the **Anycast RP** technique, **both Spine switches act as active Rendezvous Points** and share the **same IP address**. This IP is assigned to a dedicated loopback interface on each Spine.

- Since `loopback0` is typically already used for OSPF Underlay Network, it is recommended to use a different loopback interface, (e.g. `loopback1`), exclusively for Anycast RP functionality.

The configuration steps are:

1. **Create a new loopback** interface (e.g., `loopback1`).
2. **Assign the same IP address** to this interface on both Spine switches (e.g., `10.10.255.255/32`).
3. Ensure `loopback1` is **advertised via OSPF in the underlay** so it is reachable by all multicast-enabled devices in the fabric.

````py
# Create Loopback1 for RP Anycast Technique (both Spines)

configure terminal

interface loopback 1
    description ** PIM - RP Anycast (RP Redundant) **
        ip address 10.10.255.255/32
            ip router ospf UNDERLAY-F0 area 0.0.0.0
exit

!
!    

````

### 🎨👋 PIM Configuration: `PIM on interfaces` (PIM JOINERS (Fabic))

These are the steps to enable PIM on the joiner devices, **ALL devices in the fabric are joiners** _(e.g. **BGWs** and **Leafs**. **Spines** are joiners too, but they are also RPs)_. PIM joiners query the Rendezvous Point (RP) for multicast group information. 

1. `feature pim` _(Fabric)_: Enable the PIM feature on each Nexus inside the Fabric.
2. `pim sparse-mode` _(Eth)_: Enable **PIM Sparse-Mode** on all routed physical interfaces (**Eth1/x**)
3. `pim sparse-mode` _(Lo0)_: Enable **PIM Sparse-Mode** on **loopback0**.
4. `ip pim rp-address` _(All PIM joiners)_: Define the shared RP IP using for Anycast (**10.10.255.255**).


````py
# Configure PIM on supplicants (leafs)

configure terminal

!# Step 1.  Enable the "PIM" feature.

feature pim

!# Step 2. Add PIM to physical interfaces

interface ethernet1/1
   description ** OSPF Peer @ SPINE-1 **
      ip address 10.10.1.109/31
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
             !# PIM Underlay Multicast <<<<<<<<<<<<<<<<<<<<<<<
             ip pim sparse-mode    
exit
interface ethernet1/2
   description ** OSPF Peer @ SPINE-2 **
      ip address 10.10.1.117/31
         !# OSPF Underlay Unicast
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
             !# PIM Underlay Multicast <<<<<<<<<<<<<<<<<<<<<<<
             ip pim sparse-mode    
exit

!# Step 3. Add PIM to loopback0

interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.15/32
         !# OSPF Underlay Unicast
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# PIM Underlay Multicast <<<<<<<<<<<<<<<<<<<<<<<
             ip pim sparse-mode    

!# Step 4.  Indicarle quien es el RP, agregando la IP loopback1 de los psines.

             ip pim rp-address 10.10.255.255


!
!


````

### 🎨👋 PIM Configuration: `PIM on interfaces` (RP NODES (Spines))

These are the **Rendezvous Point (RP)** nodes, typically the **Spine switches**. They require the **same base configuration as joiners**, plus the additiona **Step 5** command to support **Anycast RP** on both Spines.

> With **Anycast RP**, both Spines share the same virtual IP on `loopback1`, while `loopback0` provides a **unique Router-ID to distinguish each RP**.

The configuration steps are:

1. `feature pim` _(Fabric)_: Enable the PIM feature on each Nexus inside the Fabric.
2. `pim sparse-mode` _(Eth)_: Enable **PIM Sparse-Mode** on all routed physical interfaces (**Eth1/x**)
3. `pim sparse-mode` _(Lo0)_: Enable **PIM Sparse-Mode** on **loopback0**.
4. `ip pim rp-address` _(All PIM joiners)_: Define the shared RP IP using for Anycast (**10.10.255.255**). <br><br>
5. `ip pim anycast-rp` _(RP Only)_: Configure **ip pim anycast-rp** bindings for **HA**, using the `loopback1` addresses of both Spines.***

````py
# Configure PIM

configure terminal

!# Step 1. 

feature pim

!# Step 2. Add PIM to physical interfaces

interface ethernet1/1
   description ** OSPF Peer @ BGW-1A **
      ip address 10.10.1.101/31
         !# OSPF Underlay Unicast
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
             !# PIM Underlay Multicast <<<<<<<<<<<<<<<<<<<<<<<
             ip pim sparse-mode    
exit
interface ethernet1/3
   description ** OSPF Peer @ LEAF-1A **
      ip address 10.10.1.108/31
         !# OSPF Underlay Unicast
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
             !# PIM Underlay Multicast <<<<<<<<<<<<<<<<<<<<<<<
             ip pim sparse-mode    
exit

!# Step 3. Add PIM to loopback0

interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.13/32
         !# OSPF Underlay Unicast
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# PIM Underlay Multicast <<<<<<<<<<<<<<<<<<<<<<<
             ip pim sparse-mode

!# Step 4.  Indicarle quien es el RP, agregando la IP loopback1 de los psines.

             ip pim rp-address 10.10.255.255

!# Step 5.  Inform the router that it’s part of an Anycast RP setup, sharing a virtual IP with another RP.
            !# The loopback0 on each Spine provides the unique Router-ID for PIM to distinguish them.
            !# The loopback1 uses the same IP on both Spines for HA
!# Spine 1 - RP-1 <Loopback1> <Loopback0>
ip pim anycast-rp 10.10.255.255 10.10.10.13
!# Spine 2 - RP-2 <Loopback1> <Loopback0>
ip pim anycast-rp 10.10.255.255 10.10.10.14

!
!


````

## 🎯 Objectives, Features & Protocols Covered 

This is the Summary of What We’ll Do in This Lab

- Enable `PIM features` and `PIM Sparse-Mode` on all routed interfaces across **BGWs, Spines, and Leafs**.
- Advertise `Loopback0` (used as RPF source) in OSPF.
- Configure `Anycast RP` using `Loopback1` on both Spines
- Validate PIM configuration routing using:
   - `show ip pim neighbor`
- Prepare the fabric to support VXLAN flood-and-learn for the next stage.

Once the underlay is fully multicast-enabled, we’ll move on to Lab 3, where we’ll:

- Enable feature nv overlay
- Start building VXLAN tunnels
- Map VNIs to multicast groups
- Begin bridging L2 segments across the fabric


## 🎥 Lab Proof of Concept (PoC) - Video

- [**👉 Click here to go to the PoC video 👈**](https://youtu.be/RL9hBT0H7UE)

## 🗺️ Network Topology

<img width="771" height="915" alt="image" src="https://github.com/user-attachments/assets/36f18009-dccc-4ded-ba93-a48c959a4bec" />



## 📋 Network Device Inventory, Interfaces & IP Addressing

| 💻 Device            | **🛠️ Function**         | **🔌 Interface / VLAN**     | **🌐 IP / CIDR** | **🎯 Gateway** | **_🗺️ Network_** | **_📡 Broadcast_** | **🔐 VRF**     | **📘 Main Description**                      |
|----------------------|--------------------------|-----------------------------|-------------------|-----------------|------------------|---------------------|----------------|-----------------------------------------------|
| **`NX9-BGW-1A`**     | Border Gateway (vPC A)   | mgmt0                       | 10.10.66.11/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Ethernet1/5                 | 10.10.255.1/30  | 10.10.255.2   | _10.10.255.0_   | _10.10.255.3_     | vpc-keepalive | vPC Keepalive to BGW-1B                     |
|                      |                          | port-channel100 (Eth1/6-7)  | –               | –             | _–_             | _–_               | default       | vPC Peer-Link trunk                         |
|                      |                          | loopback0                   | 10.10.1.11/32   | –             | _–_             | _–_               | default       | OSPF Router ID (UNDERLAY-F0)                |
|                      |                          | Vlan10 (SVI)                | 10.10.1.211/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | SVI OSPF underlay to spines                 |
|                      |                          | Ethernet1/1                 | 10.10.1.100/31  | 10.10.1.101   | _10.10.1.100_   | _10.10.1.101_     | default       | OSPF to Spine-1                             |
|                      |                          | Ethernet1/2                 | 10.10.1.102/31  | 10.10.1.103   | _10.10.1.102_   | _10.10.1.103_     | default       | OSPF to Spine-2                             |
|                      |                          | Ethernet1/3.10              | 10.10.2.102/30  | 10.10.2.101   | _10.10.2.100_   | _10.10.2.103_     | default       | OSPF P2P to WAN Router (subinterface)       |
| **`NX9-BGW-1B`**     | Border Gateway (vPC B)   | mgmt0                       | 10.10.66.12/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Ethernet1/5                 | 10.10.255.2/30  | 10.10.255.1   | _10.10.255.0_   | _10.10.255.3_     | vpc-keepalive | vPC Keepalive to BGW-1A                     |
|                      |                          | port-channel100 (Eth1/6-7)  | –               | –             | _–_             | _–_               | default       | vPC Peer-Link trunk                         |
|                      |                          | loopback0                   | 10.10.1.12/32   | –             | _–_             | _–_               | default       | OSPF Router ID (UNDERLAY-F0)                |
|                      |                          | Vlan10 (SVI)                | 10.10.1.212/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | SVI OSPF underlay to spines                 |
|                      |                          | Ethernet1/1                 | 10.10.1.106/31  | 10.10.1.107   | _10.10.1.106_   | _10.10.1.107_     | default       | OSPF to Spine-2                             |
|                      |                          | Ethernet1/2                 | 10.10.1.104/31  | 10.10.1.105   | _10.10.1.104_   | _10.10.1.105_     | default       | OSPF to Spine-1                             |
|                      |                          | Ethernet1/3.10              | 10.10.2.106/30  | 10.10.2.105   | _10.10.2.104_   | _10.10.2.107_     | default       | OSPF P2P to WAN Router (subinterface)       |
| **`NX9-SPINE-1`**    | Spine Switch             | mgmt0                       | 10.10.66.13/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Loopback0                   | 10.10.1.13/32   | -             | _-_             | _-_               | default       | OSPF Router ID                              |
|                      |                          | loopback1                   | 10.10.255.255/32| –             | _-_             |  _-_              | default       | Anycast RP (shared with Spine-2)            |
|                      |                          | Vlan10                      | 10.10.1.213/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | OSPF SVI to Leafs/BGWs                      |
|                      |                          | Ethernet1/1                 | 10.10.1.101/31  | 10.10.1.100   | _10.10.1.100_   | _10.10.1.101_     | default       | OSPF to BGW-1A                              |
|                      |                          | Ethernet1/2                 | 10.10.1.105/31  | 10.10.1.104   | _10.10.1.104_   | _10.10.1.105_     | default       | OSPF to BGW-1B                              |
|                      |                          | Ethernet1/3                 | 10.10.1.108/31  | 10.10.1.108   | _10.10.1.108_   | _10.10.1.109_     | default       | OSPF to LEAF-1A                             |
|                      |                          | Ethernet1/4                 | 10.10.1.110/31  | 10.10.1.110   | _10.10.1.110_   | _10.10.1.111_     | default       | OSPF to LEAF-1B                             |
|                      |                          | Ethernet1/5                 | 10.10.1.112/31  | 10.10.1.112   | _10.10.1.112_   | _10.10.1.113_     | default       | OSPF to LEAF-2A                             |
|                      |                          | Ethernet1/6                 | 10.10.1.114/31  | 10.10.1.114   | _10.10.1.114_   | _10.10.1.115_     | default       | OSPF to LEAF-2B                             |
| **`NX9-SPINE-2`**    | Spine Switch             | mgmt0                       | 10.10.66.14/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Loopback0                   | 10.10.1.14/32   | -             | _-_             | _-_               | default       | OSPF Router ID                              |
|                      |                          | loopback1                   | 10.10.255.255/32| –             | _-_             |  _-_              | default       | Anycast RP (shared with Spine-1)            |
|                      |                          | Vlan10                      | 10.10.1.214/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | OSPF SVI to Leafs/BGWs                      |
|                      |                          | Ethernet1/1                 | 10.10.1.107/31  | 10.10.1.106   | _*10.10.1.106v_ | _10.10.1.107_     | default       | OSPF to BGW-1B                              |
|                      |                          | Ethernet1/2                 | 10.10.1.103/31  | 10.10.1.102   | _10.10.1.102_   | _10.10.1.103_     | default       | OSPF to BGW-1A                              |
|                      |                          | Ethernet1/3                 | 10.10.1.116/31  | 10.10.1.116   | _10.10.1.116_   | _10.10.1.117_     | default       | OSPF to LEAF-1A                             |
|                      |                          | Ethernet1/4                 | 10.10.1.118/31  | 10.10.1.118   | _10.10.1.118_   | _10.10.1.119_     | default       | OSPF to LEAF-1B                             |
|                      |                          | Ethernet1/5                 | 10.10.1.120/31  | 10.10.1.120   | _10.10.1.120_   | _10.10.1.121_     | default       | OSPF to LEAF-2A                             |
|                      |                          | Ethernet1/6                 | 10.10.1.122/31  | 10.10.1.122   | _10.10.1.122_   | _10.10.1.123_     | default       | OSPF to LEAF-2B                             |
| **`NX9-LEAF-1A`**    | Leaf vPC-A               | mgmt0                       | 10.10.66.15/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Loopback0                   | 10.10.1.15/32   | -             | _-_             | _-_               | default       | OSPF Router ID                              |
|                      |                          | Vlan10                      | 10.10.1.215/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | SVI – OSPF Peer Reachability                |
|                      |                          | Ethernet1/1                 | 10.10.1.109/31  | 10.10.1.108   | _10.10.1.108_   | _10.10.1.109_     | default       | OSPF to Spine-1                             |
|                      |                          | Ethernet1/2                 | 10.10.1.117/31  | 10.10.1.116   | _10.10.1.116_   | _10.10.1.117_     | default       | OSPF to Spine-2                             |
|                      |                          | Ethernet1/5                 | 10.10.255.1/30  | 10.10.255.2   | _10.10.255.0_   | _10.10.255.3_     | vpc-keepalive | vPC KeepAlive physical link                 |
|                      |                          | Po100 (Eth1/6-7)            | –               | –             | _–_             | _–_               | default       | vPC Peer-Link trunk (VLAN 10)               |
| **`NX9-LEAF-1B`**    | Leaf vPC-B               | mgmt0                       | 10.10.66.16/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Loopback0                   | 10.10.1.16/32   | -             | _-_             | _-_               | default       | OSPF Router ID                              |
|                      |                          | Vlan10                      | 10.10.1.216/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | SVI – OSPF Peer Reachability                |
|                      |                          | Ethernet1/1                 | 10.10.1.111/31  | 10.10.1.110   | _10.10.1.110_   | _10.10.1.111_     | default       | OSPF to Spine-1                             |
|                      |                          | Ethernet1/2                 | 10.10.1.119/31  | 10.10.1.118   | _10.10.1.118_   | _10.10.1.119_     | default       | OSPF to Spine-2                             |
|                      |                          | Ethernet1/5                 | 10.10.255.2/30  | 10.10.255.1   | _10.10.255.0_   | _10.10.255.3_     | vpc-keepalive | vPC KeepAlive physical link                 |
|                      |                          | Po100 (Eth1/6-7)            | –               | –             | _–_             | _–_               | default       | vPC Peer-Link trunk (VLAN 10)               |
| **`NX9-LEAF-2A`**    | Leaf vPC-A               | mgmt0                       | 10.10.66.17/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Loopback0                   | 10.10.1.17/32   | -             | _-_             | _-_               | default       | OSPF Router ID                              |
|                      |                          | Vlan10                      | 10.10.1.217/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | SVI – OSPF Peer Reachability                |
|                      |                          | Ethernet1/1                 | 10.10.1.113/31  | 10.10.1.112   | _10.10.1.112_   | _10.10.1.113_     | default       | OSPF to Spine-1                             |
|                      |                          | Ethernet1/2                 | 10.10.1.121/31  | 10.10.1.120   | _10.10.1.120_   | _10.10.1.121_     | default       | OSPF to Spine-2                             |
|                      |                          | Ethernet1/5                 | 10.10.255.1/30  | 10.10.255.2   | _10.10.255.0_   | _10.10.255.3_     | vpc-keepalive | vPC KeepAlive physical link                 |
|                      |                          | Po100 (Eth1/6-7)            | –               | –             | _–_             | _–_               | default       | vPC Peer-Link trunk (VLAN 10)               |
| **`NX9-LEAF-2B`**    | Leaf vPC-B               | mgmt0                       | 10.10.66.18/24  | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | management    | OOB Management interface                    |
|                      |                          | Loopback0                   | 10.10.1.18/32   | -             | _-_             | _-_               | default       | OSPF Router ID                              |
|                      |                          | Vlan10                      | 10.10.1.218/24  | 10.10.1.254   | _10.10.1.0_     | _10.10.1.255_     | default       | SVI – OSPF Peer Reachability                |
|                      |                          | Ethernet1/1                 | 10.10.1.115/31  | 10.10.1.114   | _10.10.1.114_   | _10.10.1.115_     | default       | OSPF to Spine-1                             |
|                      |                          | Ethernet1/2                 | 10.10.1.123/31  | 10.10.1.122   | _10.10.1.122_   | _10.10.1.123_     | default       | OSPF to Spine-2                             |
|                      |                          | Ethernet1/5                 | 10.10.255.2/30  | 10.10.255.1   | _10.10.255.0_   | _10.10.255.3_     | vpc-keepalive | vPC KeepAlive physical link                 |
|                      |                          | Po100 (Eth1/6-7)            | –               | –             | _–_             | _–_               | default       | vPC Peer-Link trunk (VLAN 10)               |
| **`IOS-SWITCH-MGMT`**| MGMT Switch              | VLAN66 (SVI)                | 10.10.66.250/24 | 10.10.66.254  | _10.10.66.0_    | _10.10.66.255_    | default       | SVI Gateway for the management network (SW) |
|                      |                          | Eth0/0-3,1/0-3,2/1-3        | -               | -             | _-_             | _-_               | default       | Access ports for network devices (VLAN 66)  |
|                      |                          | Eth2/0                      | -               | -             | _-_             | _-_               | default       | Trunk link to WAN Router (VLAN 66)          |
| **`IOS-RT-WAN`**     | WAN Router               | Loopback0                   | 10.10.1.254/32  | -             | _-_             | _-_               | default       | Router ID for OSPF process 10               |
|                      |                          | Eth0/0.66                   | 10.10.66.254/24 | -             | _10.10.66.0_    | _10.10.66.255_    | management    | Gateway for Management VRF                  |
|                      |                          | Eth0/1.10                   | 10.10.2.101/30  | -             | _10.10.2.100_   | _10.10.2.103_     | default       | OSPF peer with BGW-1                        |
|                      |                          | Eth0/3.10                   | 10.10.2.105/30  | -             | _10.10.2.104_   | _10.10.2.107_     | default       | OSPF peer with BGW-2                        |
|                      |                          | Eth0/2                      | 123.1.1.2/30    | 123.1.1.1     | _123.1.1.0_     | _123.1.1.3_       | default       | WAN interface with NAT to Internet          |
| **`WAN-1`**          | Internet ISP             | Eth0/0                      | 123.1.1.1/30    | -             | _123.1.1.0_     | _123.1.1.3_       | -             | ISP Interface receiving NAT traffic         |
|                      |                          | Loopback0                   | 8.8.8.8/32      | -             | _-_             | _-_               | -             | Google DNS Loopback #1                      |
|                      |                          | Loopback1                   | 8.8.4.4/32      | -             | _-_             | _-_               | -             | Google DNS Loopback #2                      |




## 📝 Lab Notes

Credentials:

- Admin: `admin`
- Pass: `Adm1n.C1sc0`

Notes:

- During Nexus Switches start-up, select `skip` during "Abort Power On Auto Provisioning (yes - continue with normal setup, skip - bypass password and basic configuration, no - continue with Power On Auto Provisioning) (yes/skip/no)[no]: `skip`"
- The NX9-1 and NX9-2 must be powered on and configured before the edge routers, otherwise OSPF process 1 could bug/error.
- hay comandos que nececitan `terminal width 500` para que se vea correcto todo
- Se deben utilizar imagenes nexus 9k como minimo para soportar los vPC y VXLAN, minimo 8gb de RAM cada uno.
- en caso que el nexus al iniciar que quede en un prompt de "loader>" quiere decir que no inicio el Segundo Sistema operativo, recordar que nxos arranca con 2 , primero el kicks start y luego el SO, en caso de que se quede en `loader>` solo escribir "dir" y despues "boot NXOS.9.34234234" o la verison que se este usando. 
- Check that all virtual NX devices are powered on and have no CLI issues; sometimes they can hang or freeze when too many sessions are open or multiple processes are running. <br><br>
- Overlapping subnet warning (e.g. between Lo0 and VLAN10 `overlapping network for ipv4 address: 10.10.1.211/24 on vlan10, 10.10.1.11/32 already configured on lo0`) **is expected**.  It’s safe to ignore Loopback uses /32 for OSPF RID and can coexist with SVI in the same subnet.


# **⚙️ Devices Configurations**

- Copy & Paste the configuration in each device CLI

## 👑🥇 `NX9-BGW-1A` - (Border Gateway - VPC-A)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-BGW-1A                                                        #
#    ROLE         : Border Gateway (A)                                                #
#                                                                                     #
#    MGMT         : 10.10.66.11/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#    - *vpc-keepalive                                                                 #
#                                                                                     #
#    VPCs:                                                                            #
#    - vPC Domain 666 (BGW-1A <==> BGW-1B)                                            #
#      * PeerLink  @ Po100                                                            #
#      * KeepAlive @ Eth5                                                             #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY                                                                   #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.11/32                                                     #
#    - RID        : 10.10.1.11                                                        #
#    - Peer-SVI   : 10.10.1.211/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-BGW-1A
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.11/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Port Channel & vPC:
feature vpc
feature lacp

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  vPC CONFIGURATION                                                                  #
!#######################################################################################

!# vPC Configuration: << vPC Domain 666 >> 

!# 1 - Create VRF "vpc-keepalive"
vrf context vpc-keepalive
   description ** Keepalive path for vPC control-plane **
exit

!# 2 - Create new "vpc-keepalive" physical interface for P2P link
interface Ethernet 1/5
   description ** vPC KeepAlive Link (A) **
   no shutdown
      no switchport
         vrf member vpc-keepalive
         ip address 10.10.255.1/30
exit

!# 3 - Create vPC Domain "666" and configure KeepAlive-Link (Primary = 100 (lower))
vpc domain 666
   peer-keepalive destination 10.10.255.2 source 10.10.255.1 vrf vpc-keepalive
      role priority 100              
      auto-recovery
      auto-recovery reload-delay 60
      delay restore 1             
      system-priority 1000             
exit

!# 4 - Configure vPC Peer Link - Port Channel 100 (Eth6 & Eth7)
interface ethernet 1/6
   description ** (Po100) vPC Peer-Link - Interface 1of2 **
   no shutdown
      channel-group 100 mode active
exit
interface ethernet 1/7
   description ** (Po100) vPC Peer-Link - Interface 2of2 **
   no shutdown
      channel-group 100 mode active
exit
interface port-channel 100
   description ** (Po100) vPC Peer-Link Port-Channel **
   no shutdown
      switchport
      switchport mode trunk
      switchport trunk allowed vlan 10
         vpc peer-link     
exit

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.11
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.11/32
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255 
!# << AUTO EXIT >>

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.211/24 
exit
#! Static default route (Default Gateway) for OSPF underlay in default VRF
! ip route 0.0.0.0/0 10.10.1.254
ip route 0.0.0.0/0 10.10.2.101

!# INTERFACE :: ETH 1/1 @ SPINE-1 
interface ethernet1/1
   description ** OSPF Peer @ Spine-1 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.100/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ SPINE-2
interface ethernet1/2
   description ** OSPF Peer @ Spine-2 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.102/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#######################################################################################
!#  WAN INTERFACE + L3 SUB-INTERFACE @ OSPF 10                                         #
!#######################################################################################

!# OSPF 10
router ospf 10
   router-id 10.10.1.11
exit

!# INTERFACE :: ETH 1/3 @ WAN ROUTER (OSPF 10)
interface Ethernet1/3
   description *** Link → WAN ROUTER Eth0/1 ***
   no shutdown
   speed 1000
   duplex full
      no switchport
exit
!# SUB-INTERFACE
interface Ethernet1/3.10
   description *** Link → WAN ROUTER Eth0/1 ***
   no shutdown
      encapsulation dot1q 10
      ip address 10.10.2.102/30
         ip router ospf 10 area 0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-BGW-1A
copy running-config startup-config

!
!


````

## 👑🥈 `NX9-BGW-1B` - (Border Gateway - VPC-B)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-BGW-1B                                                        #
#    ROLE         : Border Gateway (B)                                                #
#                                                                                     #
#    MGMT         : 10.10.66.12/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#    - *vpc-keepalive                                                                 #
#                                                                                     #
#    VPCs:                                                                            #
#    - vPC Domain 666 (BGW-1B <==> BGW1A)                                             #
#      * PeerLink  @ Po100                                                            #
#      * KeepAlive @ Eth5                                                             #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY                                                                   #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.12/32                                                     #
#    - RID        : 10.10.1.12                                                        #
#    - Peer-SVI   : 10.10.1.212/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-BGW-1B
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.12/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Port Channel & vPC:
feature vpc
feature lacp

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  vPC CONFIGURATION                                                                  #
!#######################################################################################

!# vPC Configuration: << vPC Domain 666 >> 

!# 1 - Create VRF "vpc-keepalive"
vrf context vpc-keepalive
   description ** Keepalive path for vPC control-plane **
exit

!# 2 - Create new "vpc-keepalive" physical interface for P2P link
interface Ethernet 1/5
   description ** vPC KeepAlive Link (B) **
   no shutdown
      no switchport
         vrf member vpc-keepalive
         ip address 10.10.255.2/30
exit

!# 3 - Create vPC Domain "666" and configure KeepAlive-Link (Secondary = 200 (higher))
vpc domain 666
   peer-keepalive destination 10.10.255.1 source 10.10.255.2 vrf vpc-keepalive
      role priority 200              
      auto-recovery
      auto-recovery reload-delay 60
      delay restore 1             
      system-priority 1000             
exit

!# 4 - Configure vPC Peer Link - Port Channel 100 (Eth6 & Eth7)
interface ethernet 1/6
   description ** (Po100) vPC Peer-Link - Interface 1of2 **
   no shutdown
      channel-group 100 mode active
exit
interface ethernet 1/7
   description ** (Po100) vPC Peer-Link - Interface 2of2 **
   no shutdown
      channel-group 100 mode active
exit
interface port-channel 100
   description ** (Po100) vPC Peer-Link Port-Channel **
   no shutdown
      switchport
      switchport mode trunk
      switchport trunk allowed vlan 10
         vpc peer-link     
exit

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.12
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.12/32
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255 
!# << AUTO EXIT >>

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.212/24 
exit
!# Static default route (Default Gateway) for OSPF underlay in default VRF
! ip route 0.0.0.0/0 10.10.1.254
ip route 0.0.0.0/0 10.10.2.105

!# INTERFACE :: ETH 1/1 @ SPINE-2
interface ethernet1/1
   description ** OSPF Peer @ SPINE-2 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.106/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ SPINE-1
interface ethernet1/2
   description ** OSPF Peer @ SPINE-1 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.104/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#######################################################################################
!#  WAN INTERFACE + L3 SUB-INTERFACE @ OSPF 10                                         #
!#######################################################################################

!# OSPF 10
router ospf 10
   router-id 10.10.1.12
exit

!# INTERFACE :: ETH 1/3 @ WAN ROUTER (OSPF 10)
interface Ethernet1/3
   description *** Link → WAN ROUTER Eth0/1 ***
   no shutdown
   speed 1000
   duplex full
      no switchport
exit
!# SUB-INTERFACE
interface Ethernet1/3.10
   description *** Link → WAN ROUTER Eth0/1 ***
   no shutdown
      encapsulation dot1q 10
      ip address 10.10.2.106/30
         ip router ospf 10 area 0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-BGW-1B
copy running-config startup-config

!
!


````

## 🩻🥇 `NX9-SPINE-1` - (SPINE 1 - PIM : RP-1)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-SPINE-1                                                       #
#    ROLE         : SPINE 1 (Rendezvous Point RP #1 for PIM {Anycast})                #
#                                                                                     #
#    MGMT         : 10.10.66.13/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#                                                                                     #
#    VPCs:                                                                            #
#    - None                                                                           #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY (Unicast)                                                         #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.13/32                                                     #
#    - RID        : 10.10.1.13                                                        #
#    - Peer-SVI   : 10.10.1.213/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#     PIM UNDERLAY (Multicast)                                                        #
#    - Lo0        : 10.10.1.13/32      (same used for unicast)                        #
#    - Lo1        : 10.10.255.255/32  (anycast RP)                                    #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-SPINE-1
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.13/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.13
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.13/32
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255
!# << AUTO EXIT >>

!# ++++ 3 - Set Router as Rendezvous Point (RP) - Inform the router that it’s part of an Anycast RP setup, sharing a virtual IP with another RP. ++++ 
   !# ++++ Spine 1 - RP-1 <Loopback1>(shared) <Loopback0>(unique ID) ++++ 
ip pim anycast-rp 10.10.255.255 10.10.10.13
   !# ++++ Spine 2 - RP-2 <Loopback1>(shared) <Loopback0>(unique ID) ++++ 
ip pim anycast-rp 10.10.255.255 10.10.10.14

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.213/24 
exit
#! Static default route (Default Gateway) for OSPF underlay in default VRF
ip route 0.0.0.0/0 10.10.1.254

!# INTERFACE :: ETH 1/1 @ BGW-1A
interface ethernet1/1
   description ** OSPF Peer @ BGW-1A **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.101/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ BGW-1B
interface ethernet1/2
   description ** OSPF Peer @ BGW-1B **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.105/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/3 @ LEAF-1A
interface ethernet1/3
   description ** OSPF Peer @ LEAF-1A **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.108/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/4 @ LEAF-1B
interface ethernet1/4
   description ** OSPF Peer @ LEAF-1B **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.110/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/5 @ LEAF-2A
interface ethernet1/5
   description ** OSPF Peer @ LEAF-2A **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.112/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/6 @ LEAF-2B
interface ethernet1/6
   description ** OSPF Peer @ LEAF-2B **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.114/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!#+  PIM - Rendezvous Point (RP) Anycast (HA) - PIM Sparse-Mode (UNDERLAY - Multicast) +
!#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

!# Create Loopback1 for RP Anycast Technique (both Spines) - Add OSPF Underlay to it
interface loopback 1
    description ** PIM - RP Anycast (RP Redundant) **
        ip address 10.10.255.255/32
            ip router ospf UNDERLAY-F0 area 0.0.0.0
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-SPINE-1
copy running-config startup-config

!
!


````

## 🩻🥇 `NX9-SPINE-2` - (SPINE 2 - PIM : RP-2)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-SPINE-2                                                       #
#    ROLE         : SPINE 2 (Rendezvous Point RP #2 for PIM {Anycast})                #
#                                                                                     #
#    MGMT         : 10.10.66.14/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#                                                                                     #
#    VPCs:                                                                            #
#    - None                                                                           #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY (Unicast)                                                         #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.14/32                                                     #
#    - RID        : 10.10.1.14                                                        #
#    - Peer-SVI   : 10.10.1.214/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#     PIM UNDERLAY (Multicast)                                                        #
#    - Lo0        : 10.10.1.14/32      (same used for unicast)                        #
#    - Lo1        : 10.10.255.255/32  (anycast RP)                                   #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-SPINE-2
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.14/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.14
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.14/32
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255 
!# << AUTO EXIT >>

!# ++++ 3 - Set Router as Rendezvous Point (RP) - Inform the router that it’s part of an Anycast RP setup, sharing a virtual IP with another RP. ++++ 
   !# ++++ Spine 1 - RP-1 <Loopback1>(shared) <Loopback0>(unique ID) ++++ 
ip pim anycast-rp 10.10.255.255 10.10.10.13
   !# ++++ Spine 2 - RP-2 <Loopback1>(shared) <Loopback0>(unique ID) ++++ 
ip pim anycast-rp 10.10.255.255 10.10.10.14

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.214/24 
exit
#! Static default route (Default Gateway) for OSPF underlay in default VRF
ip route 0.0.0.0/0 10.10.1.254

!# INTERFACE :: ETH 1/1 @ BGW-1B
interface ethernet1/1
   description ** OSPF Peer @ BGW-1B **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.107/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ BGW-1A
interface ethernet1/2
   description ** OSPF Peer @ BGW-1A **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.103/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/3 @ LEAF-1A
interface ethernet1/3
   description ** OSPF Peer @ LEAF-1A **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.116/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/4 @ LEAF-1B
interface ethernet1/4
   description ** OSPF Peer @ LEAF-1B **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.118/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/5 @ LEAF-2A
interface ethernet1/5
   description ** OSPF Peer @ LEAF-2A **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.120/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/6 @ LEAF-2B
interface ethernet1/6
   description ** OSPF Peer @ LEAF-2B **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.122/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!#+  PIM - Rendezvous Point (RP) Anycast (HA) - PIM Sparse-Mode (UNDERLAY - Multicast) +
!#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

!# Create Loopback1 for RP Anycast Technique (both Spines) - Add OSPF Underlay to it
interface loopback 1
    description ** PIM - RP Anycast (RP Redundant) **
        ip address 10.10.255.255/32
            ip router ospf UNDERLAY-F0 area 0.0.0.0
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-SPINE-2
copy running-config startup-config

!
!


````






## 🌿🥇 `NX9-LEAF-1A` - (LEAF 1 - VPC-A)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-LEAF-1A                                                       #
#    ROLE         : LEAF                                                              #
#                                                                                     #
#    MGMT         : 10.10.66.15/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#    - *vpc-keepalive                                                                 #
#                                                                                     #
#    VPCs:                                                                            #
#    - vPC Domain 666 (LEAF-1A <==> LEAF-1B)                                          #
#      * PeerLink  @ Po100                                                            #
#      * KeepAlive @ Eth5                                                             #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY                                                                   #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.15/32                                                     #
#    - RID        : 10.10.1.15                                                        #
#    - Peer-SVI   : 10.10.1.215/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-LEAF-1A
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.15/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Port Channel & vPC: (tba)
feature vpc
feature lacp

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  vPC CONFIGURATION                                                                  #
!#######################################################################################

!# vPC Configuration: << vPC Domain 666 >> 

!# 1 - Create VRF "vpc-keepalive"
vrf context vpc-keepalive
   description ** Keepalive path for vPC control-plane **
exit

!# 2 - Create new "vpc-keepalive" physical interface for P2P link
interface Ethernet 1/5
   description ** vPC KeepAlive Link (A) **
   no shutdown
      no switchport
         vrf member vpc-keepalive
         ip address 10.10.255.1/30
exit

!# 3 - Create vPC Domain "666" and configure KeepAlive-Link (Primary = 100 (lower))
vpc domain 666
   peer-keepalive destination 10.10.255.2 source 10.10.255.1 vrf vpc-keepalive
      role priority 100              
      auto-recovery
      auto-recovery reload-delay 60
      delay restore 1             
      system-priority 1000             
exit

!# 4 - Configure vPC Peer Link - Port Channel 100 (Eth6 & Eth7)
interface ethernet 1/6
   description ** (Po100) vPC Peer-Link - Interface 1of2 **
   no shutdown
      channel-group 100 mode active
exit
interface ethernet 1/7
   description ** (Po100) vPC Peer-Link - Interface 2of2 **
   no shutdown
      channel-group 100 mode active
exit
interface port-channel 100
   description ** (Po100) vPC Peer-Link Port-Channel **
   no shutdown
      switchport
      switchport mode trunk
      switchport trunk allowed vlan 10
         vpc peer-link     
exit

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.15
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.15/32
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255 
!# << AUTO EXIT >>

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.215/24 
exit
#! Static default route (Default Gateway) for OSPF underlay in default VRF
ip route 0.0.0.0/0 10.10.1.254

!# INTERFACE :: ETH 1/1 @ SPINE-1
interface ethernet1/1
   description ** OSPF Peer @ SPINE-1 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.109/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ SPINE-2
interface ethernet1/2
   description ** OSPF Peer @ SPINE-2 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.117/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-LEAF-1A
copy running-config startup-config

!
!


````

## 🌿🥈 `NX9-LEAF-1B` - (LEAF 1 - VPC-B)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-LEAF-1B                                                       #
#    ROLE         : LEAF                                                              #
#                                                                                     #
#    MGMT         : 10.10.66.16/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#    - *vpc-keepalive                                                                 #
#                                                                                     #
#    VPCs:                                                                            #
#    - vPC Domain 666 (LEAF-1B <==> LEAF-1A)                                          #
#      * PeerLink  @ Po100                                                            #
#      * KeepAlive @ Eth5                                                             #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY                                                                   #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.16/32                                                     #
#    - RID        : 10.10.1.16                                                        #
#    - Peer-SVI   : 10.10.1.216/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-LEAF-1B
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.16/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Port Channel & vPC: (tba)
feature vpc
feature lacp

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  vPC CONFIGURATION                                                                  #
!#######################################################################################

!# vPC Configuration: << vPC Domain 666 >> 

!# 1 - Create VRF "vpc-keepalive"
vrf context vpc-keepalive
   description ** Keepalive path for vPC control-plane **
exit

!# 2 - Create new "vpc-keepalive" physical interface for P2P link
interface Ethernet 1/5
   description ** vPC KeepAlive Link (B) **
   no shutdown
      no switchport
         vrf member vpc-keepalive
         ip address 10.10.255.2/30
exit

!# 3 - Create vPC Domain "666" and configure KeepAlive-Link (Secondary = 200 (higher))
vpc domain 666
   peer-keepalive destination 10.10.255.1 source 10.10.255.2 vrf vpc-keepalive
      role priority 200              
      auto-recovery
      auto-recovery reload-delay 60
      delay restore 1             
      system-priority 1000             
exit

!# 4 - Configure vPC Peer Link - Port Channel 100 (Eth6 & Eth7)
interface ethernet 1/6
   description ** (Po100) vPC Peer-Link - Interface 1of2 **
   no shutdown
      channel-group 100 mode active
exit
interface ethernet 1/7
   description ** (Po100) vPC Peer-Link - Interface 2of2 **
   no shutdown
      channel-group 100 mode active
exit
interface port-channel 100
   description ** (Po100) vPC Peer-Link Port-Channel **
   no shutdown
      switchport
      switchport mode trunk
      switchport trunk allowed vlan 10
         vpc peer-link     
exit

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.16
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.16/32
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255 
!# << AUTO EXIT >>

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.216/24 
exit
#! Static default route (Default Gateway) for OSPF underlay in default VRF
ip route 0.0.0.0/0 10.10.1.254

!# INTERFACE :: ETH 1/1 @ SPINE-1
interface ethernet1/1
   description ** OSPF Peer @ SPINE-1 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.111/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ SPINE-2
interface ethernet1/2
   description ** OSPF Peer @ SPINE-2 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.119/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-LEAF-1B
copy running-config startup-config

!
!


````

## 🌿🥇 `NX9-LEAF-2A` - (LEAF 2 - VPC-A)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-LEAF-2A                                                       #
#    ROLE         : LEAF                                                              #
#                                                                                     #
#    MGMT         : 10.10.66.17/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#    - *vpc-keepalive                                                                 #
#                                                                                     #
#    VPCs:                                                                            #
#    - vPC Domain 666 (LEAF-2A <==> LEAF-2B)                                          #
#      * PeerLink  @ Po100                                                            #
#      * KeepAlive @ Eth5                                                             #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY                                                                   #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.17/32                                                     #
#    - RID        : 10.10.1.17                                                        #
#    - Peer-SVI   : 10.10.1.217/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-LEAF-2A
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.17/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Port Channel & vPC: (tba)
feature vpc
feature lacp

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  vPC CONFIGURATION                                                                  #
!#######################################################################################

!# vPC Configuration: << vPC Domain 666 >> 

!# 1 - Create VRF "vpc-keepalive"
vrf context vpc-keepalive
   description ** Keepalive path for vPC control-plane **
exit

!# 2 - Create new "vpc-keepalive" physical interface for P2P link
interface Ethernet 1/5
   description ** vPC KeepAlive Link (A) **
   no shutdown
      no switchport
         vrf member vpc-keepalive
         ip address 10.10.255.1/30
exit

!# 3 - Create vPC Domain "666" and configure KeepAlive-Link (Primary = 100 (lower))
vpc domain 666
   peer-keepalive destination 10.10.255.2 source 10.10.255.1 vrf vpc-keepalive
      role priority 100              
      auto-recovery
      auto-recovery reload-delay 60
      delay restore 1             
      system-priority 1000             
exit

!# 4 - Configure vPC Peer Link - Port Channel 100 (Eth6 & Eth7)
interface ethernet 1/6
   description ** (Po100) vPC Peer-Link - Interface 1of2 **
   no shutdown
      channel-group 100 mode active
exit
interface ethernet 1/7
   description ** (Po100) vPC Peer-Link - Interface 2of2 **
   no shutdown
      channel-group 100 mode active
exit
interface port-channel 100
   description ** (Po100) vPC Peer-Link Port-Channel **
   no shutdown
      switchport
      switchport mode trunk
      switchport trunk allowed vlan 10
         vpc peer-link     
exit

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.17
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.17/32
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255 
!# << AUTO EXIT >>

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.217/24 
exit
#! Static default route (Default Gateway) for OSPF underlay in default VRF
ip route 0.0.0.0/0 10.10.1.254

!# INTERFACE :: ETH 1/1 @ SPINE-1
interface ethernet1/1
   description ** OSPF Peer @ SPINE-1 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.113/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ SPINE-2
interface ethernet1/2
   description ** OSPF Peer @ SPINE-2 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.121/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-LEAF-2A
copy running-config startup-config

!
!


````

## 🌿🥈 `NX9-LEAF-2B` - (LEAF 2 - VPC-B)

````py
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : NX9-LEAF-2B                                                       #
#    ROLE         : LEAF                                                              #
#                                                                                     #
#    MGMT         : 10.10.66.18/24                                                    #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    VRFs:                                                                            #
#    - default                                                                        #
#    - management                                                                     #
#    - *vpc-keepalive                                                                 #
#                                                                                     #
#    VPCs:                                                                            #
#    - vPC Domain 666 (LEAF-2A <==> LEAF-2B)                                          #
#      * PeerLink  @ Po100                                                            #
#      * KeepAlive @ Eth5                                                             #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#     OSPF UNDERLAY                                                                   #
#    - OSPF ID    : UNDERLAY-F0                                                       #
#    - OSPF AREA  : 0.0.0.0 (Backbone)                                                #
#    - Lo0        : 10.10.1.18/32                                                     #
#    - RID        : 10.10.1.18                                                        #
#    - Peer-SVI   : 10.10.1.218/24 (VLAN 10 - OSPF-PEER)                              #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname NX9-LEAF-2B
no password strength-check
username admin password admin.cisco role network-admin
cdp enable

!# MANAGEMENT INTERFACE & VRF (IP/GATEWAY)

!# Add DNS and Default Gateway to MGMT VLAN/VRF
vrf context management
   ip name-server 8.8.8.8 8.8.4.4
   ip route 0.0.0.0/0 10.10.66.254
!# Configure mgmt0 interface
interface mgmt0
   description ** MGMT INTERFACE **
   no shutdown
   vrf member management
   ip address 10.10.66.18/24
exit

!#######################################################################################
!#  FEATURES                                                                           #
!#######################################################################################

!# Port Channel & vPC: (tba)
feature vpc
feature lacp

!# Interface VLAN (for SVI)
feature interface-vlan

!# OSPF (Unicast Underlay)
feature ospf

!# +++ PIM (Multicast Underlay) +++
feature pim

!# Remote Connection
feature telnet
feature ssh

!# Discovery
feature lldp

!#######################################################################################
!#  vPC CONFIGURATION                                                                  #
!#######################################################################################

!# vPC Configuration: << vPC Domain 666 >> 

!# 1 - Create VRF "vpc-keepalive"
vrf context vpc-keepalive
   description ** Keepalive path for vPC control-plane **
exit

!# 2 - Create new "vpc-keepalive" physical interface for P2P link
interface Ethernet 1/5
   description ** vPC KeepAlive Link (B) **
   no shutdown
      no switchport
         vrf member vpc-keepalive
         ip address 10.10.255.2/30
exit

!# 3 - Create vPC Domain "666" and configure KeepAlive-Link (Secondary = 200 (higher))
vpc domain 666
   peer-keepalive destination 10.10.255.1 source 10.10.255.2 vrf vpc-keepalive
      role priority 200              
      auto-recovery
      auto-recovery reload-delay 60
      delay restore 1             
      system-priority 1000             
exit

!# 4 - Configure vPC Peer Link - Port Channel 100 (Eth6 & Eth7)
interface ethernet 1/6
   description ** (Po100) vPC Peer-Link - Interface 1of2 **
   no shutdown
      channel-group 100 mode active
exit
interface ethernet 1/7
   description ** (Po100) vPC Peer-Link - Interface 2of2 **
   no shutdown
      channel-group 100 mode active
exit
interface port-channel 100
   description ** (Po100) vPC Peer-Link Port-Channel **
   no shutdown
      switchport
      switchport mode trunk
      switchport trunk allowed vlan 10
         vpc peer-link     
exit

!#######################################################################################
!#  OSPF (UNDERLAY UNICAST) + PIM SPARSE (UNDERLAY MULTICAST)                          #
!#######################################################################################

!# 1 - Activate OSPF Process
router ospf UNDERLAY-F0
   router-id 10.10.1.18
      log-adjacency-changes
exit

!# 2 - Configure Loopback 0 Interface
interface loopback 0
   description ** Loopback 0 - OSPF UNDERLAY **
      ip address 10.10.1.18/32
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode
             !# ++++ PIM pointing to RP (Anycast = Both Spines) ++++ 
             ip pim rp-address 10.10.255.255 
!# << AUTO EXIT >>

!# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

!# 4 - OSPF Peer Interfaces @ OSPF Neighbors: 

#! SVI for VLAN 10 - OSPF Reachability
vlan 10
   name VLAN10-OSPF-PEER-GW
exit
interface vlan 10
   description ** SVI-V10-OSPF-UNDERLAY-GW **
   no shutdown
      ip address 10.10.1.218/24 
exit
#! Static default route (Default Gateway) for OSPF underlay in default VRF
ip route 0.0.0.0/0 10.10.1.254

!# INTERFACE :: ETH 1/1 @ SPINE-1
interface ethernet1/1
   description ** OSPF Peer @ SPINE-1 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.115/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!# INTERFACE :: ETH 1/2 @ SPINE-2
interface ethernet1/2
   description ** OSPF Peer @ SPINE-2 **
   no shutdown
   speed 1000
   duplex full
      no switchport
      ip address 10.10.1.123/31
         !# OSPF Underlay (Unicast)
         ip router ospf UNDERLAY-F0 area 0.0.0.0
         ip ospf network point-to-point
         ip ospf cost 1
         ip ospf hello-interval 1
         ip ospf dead-interval 4
             !# ++++ PIM Underlay Multicast ++++
             ip pim sparse-mode  
exit

!#######################################################################################
!#  SAVE CHECKPOINT & CONFIGURATION                                                    #
!#######################################################################################

end
checkpoint fz3r0-2025-3tier-OSPF_base-NX9-LEAF-2B
copy running-config startup-config

!
!


````

## 🔀🔑 `IOS-SWITCH-MGMT` - (Switch Layer 2 - Management) 

````py
enable
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : IOS-SWITCH-MGMT                                                   #
#    ROLE         : L3 SWITCH - MANAGEMENT SWITCH                                     #
#                                                                                     #
#    MGMT         : 10.10.66.250/24 (V66 NETWORK GATEWAY-1)                           #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    TRUNK:                                                                           #
#                                                                                     #
#    ACCESS:                                                                          #
#    - none                                                                           #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname IOS-SWITCH-MGMT 
username admin password admin.cisco role network-admin

!#######################################################################################
!#  VLANS                                                                              #
!#######################################################################################

vlan 66
   name V66-MGMT-VRFmgmt
exit

!#######################################################################################
!#  MANAGEMENT SVI & INTERFACE                                                         #
!#######################################################################################

!# INTERFACE :: SVI @ MGMT

interface vlan 66
   description ** SVI-V66-MGMT **
   no shutdown
      ip address 10.10.66.250 255.255.255.0 
exit
#! Default GW for mgmt @ MGMT switch (ONLY FOR LAN TRAFFIC!!!)
! ip default-gateway 10.10.66.254
#! IP Routing + IP Route = To get to Internet
ip routing
ip route 0.0.0.0 0.0.0.0 10.10.66.254

!#######################################################################################
!#  ALL INTERFACES = ACCESS VLAN 66 MANAGEMENT                                         #
!#######################################################################################

!# INTERFACE :: ALL @ SWITCH-L2 & LAN (Access) :: VRF management
interface range ethernet0/0-3,ethernet1/0-3,ethernet2/1-3
   description ** Access MGMT @ Network Devices - VRF: management **
   no shutdown
   duplex full
      switchport
      switchport mode access
      switchport access vlan 66
exit

!#######################################################################################
!#  TRUNK INTERFACES (VRF: management) ==>> @ ROUTER-WAN                               #
!#######################################################################################

!# INTERFACE :: Eth 2/0 @ ROUTER-WAN 
interface ethernet 2/0
   description ** Trunk @ ROUTER-WAN **
   no shutdown
   duplex full
      switchport
      switchport trunk encapsulation dot1q
      switchport mode trunk
      switchport trunk allowed vlan 66
exit

!#######################################################################################
!#  SAVE CONFIGURATION                                                                 #
!#######################################################################################

end
write memory


!
!

````







## 🔄🌐 `IOS-RT-WAN` - (Router WAN) 

````py
enable
configure terminal
banner motd $


#######################################################################################
#                                                                                     #
#                        - Fz3r0 :: Cisco Nexus Data Center -                         #
#                                                                                     #
#   * Github      : Fz3r0                                                             #
#   * Twitter     : @fz3r0_OPs                                                        #
#   * Youtube     : @fz3r0_OPs                                                        #
#                                                                                     #
# -._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-._.-=-._.-=-._.-=-.#
#                                                                                     #
#    NEXUS        : IOS-RT-WAN                                                        #
#    ROLE         : WAN ROUTER / NAT GATEWAY                                          #
#                                                                                     #
#    MGMT         : 10.10.66.254/24 (V66 NETWORK GATEWAY-1)                           #
#    LOGIN        : admin / admin.cisco                                               #
#                                                                                     #
#    TRUNK:                                                                           #
#                                                                                     #
#    ACCESS:                                                                          #
#    - none                                                                           #
#                                                                                     #
#    PORT CHANNELS:                                                                   #
#    - None                                                                           #
#                                                                                     #
#######################################################################################


$

!# NAMINGS, USERS, LICENSES, DISCOVERY
hostname IOS-RT-WAN

!#######################################################################################
!#  ENABLE IP ROUTING                                                                  #
!#######################################################################################

!# Enables the router to forward packets BETWEEN DIFFERENT NETWORKS (turns on Layer 3 routing between management & default VRFs)
ip routing

!#######################################################################################
!#  L3 INTERFACE & SUB-INTERFACE @ LAN - VRF: management / VLAN 66                     #
!#######################################################################################

#! L3 PHYSICAL INTERFACE @ GATEWAY FOR LAN - VRF: management / VLAN 66
#! Gateway Sub-Interfaces @ LAN
interface Ethernet 0/0
   description ** Physical Link to -> IOS-SW-WAN **
   no shutdown
   duplex full
exit
#! L3 SUB-INTERFACE @ GATEWAY FOR LAN - VRF: management / VLAN 66
interface Ethernet 0/0.66
   description ** V66 Sub-Interface for -> IOS-SW-WAN **
   no shutdown
      encapsulation dot1Q 66
      ip address 10.10.66.254 255.255.255.0
         ip nat inside
exit

!#######################################################################################
!#  OSPF Peer-Links to BGW1 & BGW2                                                     #
!#######################################################################################

router ospf 10 
   router-id 10.10.1.254
      !# OSPF Peers
      network 10.10.2.100 0.0.0.3 area 0
      network 10.10.2.104 0.0.0.3 area 0
      !# mgmt network routing trick!
      network 10.10.66.0 0.0.0.255 area 0    
exit

interface Loopback 0
   description ** Loopback for OSPF 10 **
   no shutdown 
      ip address 10.10.1.254 255.255.255.255
exit

!#  L3 INTERFACE & SUB-INTERFACE @ LAN - VRF: default / VLAN 10 (BGW1 link)    

#! L3 PHYSICAL INTERFACE @ OSPF PEER-LINK @ BGW-1
interface Ethernet0/1
   description ** Physical Link to -> BGW-1 **
   no shutdown
   duplex full
exit
#! L3 SUB-INTERFACE @ GATEWAY FOR LAN - VRF: management / VLAN 66
interface Ethernet0/1.10
   description ** V10 Sub-Interface for -> BGW-1 **
   no shutdown
      encapsulation dot1Q 10
      ip address 10.10.2.101 255.255.255.252
         ip nat inside
            ip ospf network point-to-point
            ip ospf cost 1
            ip ospf hello-interval 1
            ip ospf dead-interval 4
exit

!#  L3 INTERFACE & SUB-INTERFACE @ LAN - VRF: default / VLAN 10 (BGW2 link)          

#! L3 PHYSICAL INTERFACE @ OSPF PEER-LINK @ BGW-2
interface Ethernet0/3
   description ** Physical Link to -> BGW-2 **
   no shutdown
   duplex full
exit
#! L3 SUB-INTERFACE @ GATEWAY FOR LAN - VRF: management / VLAN 66
interface Ethernet0/3.10
   description ** V10 Sub-Interface for -> BGW-2 **
   no shutdown
      encapsulation dot1Q 10
      ip address 10.10.2.105 255.255.255.252
         ip nat inside
            ip ospf network point-to-point
            ip ospf cost 1
            ip ospf hello-interval 1
            ip ospf dead-interval 4
exit

!#######################################################################################
!#  L3 INTERFACE @ WAN + NAT TRANSLATION / INTERNET // OUTSIDE                         #
!#######################################################################################

!# WAN INTERFACE (NAT OUTSIDE) [Default Route @ Internet]
interface Ethernet 0/2
   description ** Link-to-WAN-1_INTERNET **
   no shutdown
   duplex full
      ip address 123.1.1.2 255.255.255.252
         ip nat outside
exit
!# Ruta por defecto hacia la nube Google
ip route 0.0.0.0 0.0.0.0 123.1.1.1

!#######################################################################################
!#  NAT TRANSLATION CONFIGURATION, INSIDE-OUTSIDE                                      #
!#######################################################################################

!# ACL que define el trafico interno a traducir
ip access-list extended NAT_INSIDE
   permit ip 10.10.0.0 0.0.255.255 any


!# Overload all matching inside traffic to the WAN interface address
ip nat inside source list NAT_INSIDE interface Ethernet 0/2 overload

!#######################################################################################
!#  SAVE CONFIGURATION                                                                 #
!#######################################################################################

end
write memory

!
!


````

## 🌎🖧 `WAN-1` - (Internet Circuit)

````py
!###############
!# WAN-1 (IOS) #
!###############

!# Namings
enable
configure terminal
hostname WAN-1

!# WAN Interface
interface Ethernet 0/0
  no shutdown
  duplex full  
  description LINK-TO-NETWORK
  ip address 123.1.1.1 255.255.255.252

exit

!# Loopbacks (Google)
interface loopback 0
  description ** GOOGLE-DNS-1 **
  ip address 8.8.8.8 255.255.255.255
exit
interface Loopback1
  description ** GOOGLE-DNS-2 **
  ip address 8.8.4.4 255.255.255.255
exit

!# Default Route (opcional si usas default-route en el otro router)
ip route 0.0.0.0 0.0.0.0 123.1.1.2

end
write memory

!
!


````


Future use: 

   - `show ip mroute`
   - `show ip igmp groups`




# 🗃️ Resources

- https://www.youtube.com/watch?v=lADK3STwwAM&list=PLwAU7bA502wFB5j6RnpDPNG5xwb5JEbq8
- https://www.youtube.com/watch?v=LOAgbGk6FOQ
- https://www.youtube.com/watch?v=fWCH39T-_fU
- https://arubanetworking.hpe.com/techdocs/VSG/docs/040-dc-design/esp-dc-design-020-network-design/

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
