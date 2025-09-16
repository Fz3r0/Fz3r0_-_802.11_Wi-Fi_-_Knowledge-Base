# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - Remote 802.11 Frame Capture`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility` `AP Provisioning` `PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba Mobility :: `Remote 802.11 Frame Capture`

### `Step 1`: Setup Capture from MM

- Access Point > Packet Capture
- Add following data:

<img width="469" height="339" alt="image" src="https://github.com/user-attachments/assets/fc677056-c465-4e50-ab56-ae21456f85ca" />


### `Step 2`: Setup Wireshark with Aruba ERM Protocol

- Preferences > Protocols > Aruba_ERM
- Port: `5555` (default, or use any other)

<img width="814" height="592" alt="image" src="https://github.com/user-attachments/assets/9060a65e-18c1-4f41-9498-783514c9faf6" />

- Analyze > Decode As...

<img width="595" height="323" alt="image" src="https://github.com/user-attachments/assets/e5489432-e8d8-4986-9957-4734def43144" />

- Use capture filter: `udp port 5555` for get only tunneled capture packets

<img width="901" height="307" alt="image" src="https://github.com/user-attachments/assets/3d8df1ed-6f5b-4702-8070-770518f8c114" />

### Results

- You will see something like this (PCAP + RADIO):

<img width="1919" height="1034" alt="image" src="https://github.com/user-attachments/assets/b2983472-216f-44e7-8517-9517b6e4b919" />




---

# 🗃️ Resources

- https://youtu.be/o3CL5KLBWK0?si=bUMLPRBp9jBbw4_u
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
