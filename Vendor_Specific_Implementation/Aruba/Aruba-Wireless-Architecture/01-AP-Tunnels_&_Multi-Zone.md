# 🔥🧱🛡️ Aruba: `Tunnels & MultiZone`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Aruba` `MC` `Mobility Controller` `WLC` `IEEE 802.11` `Wireless`

---



<br>

# 📝❓📄 `Index`



# **Aruba: Tunnels & MultiZone**

Before discussing **MultiZone**, let’s first understand the tunneling mechanisms used by Aruba Access Points (APs) to communicate with controllers.

---

## **Aruba AP Tunnels**

Aruba APs establish **two main tunnels** with the controller:

1. **Control Traffic Tunnel**:
   - Responsible for transmitting **management and control traffic** between the AP and the controller.
   - Uses **CPSec (Control Plane Security)** to encrypt communication, ensuring secure delivery.
   - The protocol used is **PaPi (Protocol for Access Points)**, which operates on:
     - **UDP Port 8211**.

2. **Data Traffic Tunnel**:
   - Carries **user data traffic** from the AP to the controller.
   - Uses **GRE (Generic Routing Encapsulation)** for encapsulation.
   - GRE operates using **Protocol 47**.

---

### **Summary of Traffic Tunnels**

| **Tunnel Type**         | **Purpose**                     | **Protocol** | **Port/Protocol**       |
|--------------------------|----------------------------------|--------------|--------------------------|
| **Control Traffic**      | AP management and configuration | PaPi         | UDP Port 8211 (CPSec)    |
| **Data Traffic**         | User data forwarding            | GRE          | Protocol 47 (Data GRE)   |

![image](https://github.com/user-attachments/assets/11c341c3-fedc-4c19-a74d-27c79c112c1a)

---

### **Key Points About Tunnels**

- **Dual Tunnels**:
   Each AP creates **two primary tunnels**:
   - One for **control traffic** to manage configurations, authentication, and policies.
   - Another for **data traffic** to carry user payloads.

- **Separation of Roles**:
   - Control and data traffic are processed independently.
   - The control tunnel ensures **management traffic is secure**, while the data tunnel handles **high-throughput user traffic**.

- **CPSec (Control Plane Security)**:
   - Encrypted communication for the control tunnel is provided by CPSec.
   - This ensures sensitive information, such as authentication and configuration, is protected.

- **GRE for Data Traffic**:
   - User traffic is encapsulated in GRE to allow routing and switching through the controller.
   - GRE supports scalability, enabling multiple SSIDs and APs to share the same encapsulation framework.

---


# 📚🗂️🎥 Resources

- https://www.arubanetworks.com/assets/matrix/matrix_WLAN-platforms-software-support-matrix.pdf
- https://www.arubanetworks.com/products/wireless/gateways-and-controllers/9200-series/
- https://www.hpe.com/psnow/doc/a00121209enw
  
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





