# 🔥🧱🛡️ Aruba: `Wireless Deployment Types`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Aruba` `MC` `Mobility Controller` `WLC` `IEEE 802.11` `Wireless`

---



<br>

# 📝❓📄 `Index`


#  Aruba: `Wireless Deployment Types`

In this guide, we will discuss three different wireless deployment types that are essential for building scalable, secure, and high-performing Aruba wireless networks. These deployment types are **Campus Deployment**, **Remote Deployment (VR)**, and **Branch Deployment**. Each has its specific use case, benefits, and architecture.

---

## **1. Campus Deployment**

### Overview

**All Aruba Infraestructure is on-site**. Campus deployments are typically used in large enterprise environments where multiple access points (APs) need to be centrally managed. Aruba uses a **Mobility Controller** and a **Mobility Master** to manage these APs, providing scalable and efficient wireless network operations.

![image](https://github.com/user-attachments/assets/61e40a57-9f88-4eb5-87d5-c38da5b58330)

### Key Components:

- **Campus Access Points (CAPs)**: These are the standard access points used in campus networks. They connect to the mobility controllers to manage traffic and security policies.
- **Mobility Controller**: Handles local AP traffic and policies. It can be distributed across the network.
- **Mobility Master**: The centralized controller that manages the mobility controllers. It ensures configuration consistency, simplifies management, and handles large-scale network needs.
  
### Architecture

- **Centralized Management**: The Mobility Master controls multiple mobility controllers. All APs within the campus deployment connect to these controllers.
- **No Internet Dependency**: APs do not require an internet connection to communicate with the Mobility Master. Instead, they rely on local network connectivity.
- **Integration with Aruba Solutions**: The architecture can integrate with additional Aruba solutions like **ClearPass** (for policy enforcement) and **AirWave** (for network management and monitoring).
  
### Benefits:
- **Scalability**: Easily scale the network by adding new APs and mobility controllers.
- **High Availability**: Distributed mobility controllers ensure network uptime and reliability.
- **Centralized Security and Policy Management**: Aruba’s centralized architecture ensures consistent security policies and network configurations across the campus.

---

## **2. Remote Deployment (VR - Virtual Remote Access)**

### Overview

**Some Aruba Infraestructure is in the Cloud, for example, the Mobility Master or Mobility Controller**. Remote deployments are designed for situations where employees or branch offices are located away from the central campus. In these scenarios, Aruba's **Remote Access Points (RAPs)** provide a seamless way to extend the corporate network to remote locations.

#### Normal Remote Deployment:



#### VIA Remote Deployment:

![image](https://github.com/user-attachments/assets/0a4ab90d-143d-4992-ac86-912c8dbacbe1)

VIA: Virtual Intranet Access (VIA) is part of the Aruba remote networks solution targeted for teleworkersand mobile users. VIA detects the users network environment (trusted and un-trusted) and automatically connects the user to their enterprise network. Trusted networks typically refers to a protected office network that allows users to directly access corporate intranet. Un-trusted networks are public Wi-Fi hotspots like airports, cafes, or home network. The VIA solution comes in two parts— VIA Windows desktop application and the controller configuration. VIA Windows Application—Teleworkers and mobile users can install a light weight application on their Microsoft Windows computers to connect to their enterprise network from remote locations (see “VIAWindows Application”). Controller Configuration—To set up virtual intranet access for remote users, you must configure your controller to include setting up user roles, authentication, and connection profiles. You can use either WebUI or Command Line to configure your controller (see “Configuring the VIAController” ).

### Key Components:

- **Remote Access Points (RAPs)**: These APs are deployed in remote offices or home offices and are connected to the corporate network over the internet.
- **Internet Connectivity**: RAPs rely on internet connections to connect to the central Mobility Master or Mobility Controller.
- **Virtual Remote Access (VR) Client Software**: Users can install client software on their devices to create a **VPN tunnel** to the corporate network, providing secure access to internal resources.

### Architecture

- **Centralized Configuration**: RAPs automatically pull configurations from the central Mobility Master through the VPN tunnel. This ensures that remote offices have the same network policies as the corporate campus.
- **Security**: The VR solution ensures that all communication between remote users and the corporate network is encrypted and secure.
- **Split Tunnel**: The split tunnel feature allows remote clients to access corporate resources through the VPN tunnel while allowing non-corporate internet traffic to go directly to the internet without routing through the corporate network.

### Benefits:

- **Simplified Deployment**: No need to deploy physical controllers or complex infrastructure at remote sites, only APs and any device to route traffic to Internet (Router/Firewall/Edge/etc).
- **Consistency in Security and Policies**: Remote offices or employees have the same network experience as those in the campus.
- **Optimized Traffic Flow**: With split tunneling, non-corporate traffic is offloaded directly to the internet, improving efficiency.

---

## **3. Branch Deployment**

### Overview

**Mobity Master is in the Cloud, and the Mobility Controllers are on-site or virtualized.** Branch deployments are used to extend the corporate network to smaller locations, such as regional offices, that may not require the full complexity of a campus deployment. This deployment typically uses smaller, cost-effective branch office controllers.

### Key Components:

- **Branch Office Controllers**: These controllers are deployed at remote branch locations and manage local APs. They can be small, hardware-efficient controllers such as the **Aruba 7000 Series** or **cloud-managed controllers**.
- **Access Points (APs)**: These connect directly to the branch office controller, terminating the connection locally.
- **Secure Tunnel to Mobility Master**: Branch controllers establish a secure tunnel to the Mobility Master for configuration synchronization and network management.

### Architecture

- **Local AP Termination**: Access points at the branch office connect to the local branch controller, reducing reliance on the central campus infrastructure.
- **Centralized Configuration via Tunnel**: The branch office controller tunnels back to the Mobility Master to retrieve and apply network configurations.
- **Authentication and Authorization**: The branch controller can also handle client authentication locally, ensuring that remote workers and devices can securely connect to the network, even if the central authentication servers are temporarily unavailable.

### Benefits:

- **Cost-Effective**: Small branch controllers are affordable and provide dedicated management for remote sites.
- **High Availability**: Even if the connection to the central Mobility Master is lost, branch office controllers can maintain local operations, ensuring continuous network service.
- **Redundancy**: Branch controllers can use multiple uplink methods such as **DSL**, **4G**, or **LTE** for backup internet connections. If the primary link goes down, traffic is automatically rerouted to the secondary connection.

---

## **Comparison of Deployment Types**

| **Feature**                 | **Campus Deployment**         | **Remote Deployment (VR)**     | **Branch Deployment**          |
|-----------------------------|-------------------------------|--------------------------------|--------------------------------|
| **AP Type**                  | Campus Access Points (CAP)    | Remote Access Points (RAP)     | Campus/Branch Access Points    |
| **Controller Type**          | Mobility Controller & Master  | Centralized via Mobility Master| Branch Office Controller       |
| **Network Access**           | Local network connectivity    | VPN tunnel over internet       | Direct or tunneled to HQ        |
| **Security & Policy**        | Centralized control           | Consistent with campus policies| Local branch policies + HQ sync|
| **Uplink Method**            | Local network                 | Internet connection            | DSL, 4G, LTE (failover)        |
| **Redundancy**               | High availability             | Split tunneling for efficiency | Failover uplinks               |

---

## **Conclusion**

Aruba's wireless deployment types—**Campus**, **Remote (VR)**, and **Branch**—are designed to meet the needs of different organizations and their network topologies. 

- **Campus deployments** are ideal for large enterprises that require a high degree of centralization and scalability.
- **Remote deployments (VR)** provide flexibility for home offices or smaller locations by using VPN tunnels, ensuring secure access to corporate networks from anywhere.
- **Branch deployments** offer a cost-effective solution for extending network services to remote offices while maintaining centralized control over configurations.

By leveraging Aruba’s deployment models, businesses can build reliable, scalable, and secure wireless networks that meet the needs of their distributed workforce and remote locations.







# 📚🗂️🎥 Resources

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





