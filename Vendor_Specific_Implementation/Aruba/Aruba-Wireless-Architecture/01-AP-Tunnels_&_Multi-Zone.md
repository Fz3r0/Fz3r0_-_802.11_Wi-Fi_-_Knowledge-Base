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

Before exploring **MultiZone**, it’s essential to understand the tunneling mechanisms used by Aruba Access Points (APs) to communicate with their controllers.

![image](https://github.com/user-attachments/assets/11c341c3-fedc-4c19-a74d-27c79c112c1a)







# **Aruba AP Tunnels**

Let's get this party started:

## **How AP Tunnels Work**

### **1. Tunnel Establishment**
- Aruba APs create **GRE tunnels** to connect to the Aruba controller.
- These tunnels enable secure communication and traffic forwarding.

### **2. Traffic Flow**
1. APs send encrypted traffic to the controller via these tunnels.
2. The controller:
   - Decrypts the packets.
   - Processes them.
   - Applies **firewall policies**.
3. Packets are either:
   - Switched internally.
   - Routed externally, based on configuration.

### **3. User Authentication**
- Before transmitting data, users must authenticate through **control traffic**, managed securely by the controller.



## **Types of Tunnels**

Aruba uses **two main types of tunnels**:

### **1. Control Traffic Tunnel**
- Transmits **management and control traffic** between the AP and the controller.
- Features:
  - Utilizes **CPSec (Control Plane Security)** for encrypted communication.
  - Based on the **PaPi protocol**, which operates on **UDP Port 8211**.

### **2. Data Traffic Tunnel**
- Carries **user data traffic** from the AP to the controller.
- Features:
  - Uses **GRE (Generic Routing Encapsulation)** with **Protocol 47**.
  - Each SSID on the AP creates a separate GRE tunnel.

---

## **Real-World Example of Tunnel Usage**

### **Scenario: University Campus**
- **Setup**: Hundreds of APs across multiple buildings.
- **SSIDs**: 
  - **EduNet** (students), **GuestNet** (guests), and **StaffNet** (faculty).
  
#### Traffic Behavior:
1. **EduNet**:
   - Student devices connect to the SSID.
   - Traffic is tunneled through a **GRE data tunnel** to the controller.
   - The controller enforces policies like bandwidth control and content filtering.
2. **GuestNet**:
   - Traffic may bypass the controller (if in **bridge mode**) and route directly to the internet.
3. **Control Traffic**:
   - Device registration and AP management traffic use **PaPi protocol** over UDP Port 8211.

---

## **Traffic Tunnels Overview**

| **Tunnel Type**         | **Purpose**                     | **Protocol** | **Port/Protocol**       |
|--------------------------|----------------------------------|--------------|--------------------------|
| **Control Traffic**      | AP management and configuration | PaPi         | UDP Port 8211 (CPSec)    |
| **Data Traffic**         | User data forwarding            | GRE          | Protocol 47 (Data GRE)   |

---

## **GRE Tunnels: Number of Tunnels**

### **1. Per-SSID Tunnels**
- Each AP creates:
  - **One GRE tunnel per SSID** for each radio (e.g., 2.4 GHz and 5 GHz).
  - **One keep-alive tunnel** for monitoring communication health.
- **Example**:
  - **AP with 3 SSIDs and 2 radios**:
    - To calculate the total tunnels: (3 SSIDs) x (2 radios) + 1 keep-alive tunnel = 7 total tunnels.

### **2. Total Tunnel Calculation**
- To calculate the total tunnels for an AP:
  - **Total Tunnels = (SSIDs per Radio) x (Radios) + 1 (Keep-Alive Tunnel)**

- **Example Calculations**:
  1. **Single AP with 3 SSIDs and 2 Radios**:
     - (3 SSIDs) x (2 Radios) + 1 Keep-Alive = **7 Tunnels** <br><br>
  2. **10 APs, Each with 3 SSIDs and 2 Radios**:
     - (3 SSIDs) x (2 Radios) + 1 Keep-Alive = **7 Tunnels _(per AP)_**
     - 7 Tunnels per AP x 10 APs = **70 Total Tunnels**

---

## **Bridge Mode Exception**
- APs in **bridge mode** do not forward user traffic through GRE tunnels.
- Instead, user traffic is routed directly to its destination by the AP.

---

## **Controller Responsibilities**

The Aruba controller manages:

| **Task**                 | **Description**                                        |
|--------------------------|-------------------------------------------------------|
| **AP Configuration**      | Distributes settings like SSIDs and radio parameters. |
| **User Authentication**   | Ensures secure access through validated credentials.  |
| **Firewall Policies**     | Enforces user roles and traffic rules.               |
| **Traffic Handling**      | Routes or switches packets as configured.            |

---

## **Best Practices for GRE Tunnels**

1. **Limit SSIDs**:
   - Aruba recommends **no more than 5 SSIDs per AP**.
   - Reduces tunnel creation and overhead.

2. **Monitor Performance**:
   - Use Aruba monitoring tools to check tunnel health and performance.

3. **Optimize Bandwidth**:
   - Minimize broadcast/multicast traffic to prevent tunnel congestion.

---

## **Key Takeaways**
- Aruba APs create **two main tunnels**:
  - **Control Traffic Tunnel**: Uses CPSec over UDP Port 8211.
  - **Data Traffic Tunnel**: Uses GRE over Protocol 47.
- **MultiZone** allows one AP to connect to multiple controllers for traffic segmentation.
- Proper tunnel management ensures efficient and secure network operations.
---




















# **Aruba Multi-Zone**

- **MultiZone enables a single AP to connect to multiple controllers simultaneously, segmenting traffic between zones.** 

The **Multi-Zone** feature allows an Aruba Access Point (AP) to connect to multiple controllers, thereby segmenting traffic between different zones. Each zone operates independently, meaning controllers in one zone cannot manage the devices in another zone.

![image](https://github.com/user-attachments/assets/ea081264-efe0-4de4-8139-035f2a903182)

### **How Multi-Zone Works**

1. **Primary Zone**: 
   - The **primary zone** is where the AP initially connects.
   - The **primary zone device** will provide configuration details to the AP.

2. **Secondary Zones**:
   - Secondary zones enable APs to communicate with multiple controllers for different network segments or needs.
   - Only traffic/data from SSID in secondary MC will be forwarded to that controller.
   - These zones allow for isolated configurations, ensuring that devices in one zone don’t interfere with those in another.

4. **Traffic Segmentation**: 
   - By using Multi-Zone, different wireless networks can be broadcast from the same AP without interference. For example, an AP in an airport may serve multiple airlines, each with their own wireless LANs (WLANs).
   - Each airline’s wireless network operates independently, allowing admins to control their own network settings without impacting others.

## **Mobility Controllers and Their Role in Multi-Zone**

In Multi-Zone setups, **mobility controllers** play a central role. They can either be standalone or managed by **mobility masters**:

- **Primary Controllers**: Manage the initial connection and provide basic configuration.
- **Secondary Controllers**: Handle the additional zones, ensuring that each zone operates independently, with its own set of wireless LANs.
  
Controllers in different zones cannot manage each other directly, thus ensuring complete separation between network zones.



## **Real-World Example of Multi-Zone Use**

### Basic Example:

- **Primary Zone**: Internal corporate network.
- **Secondary Zone**: Guest Wi-Fi for isolated internet access.

### Real-Life Scenario:

Imagine an airport where several airlines need separate wireless connections. By utilizing Multi-Zone:

- **Airline 1** uses one AP to connect to its **primary zone** for its own wireless LAN.
- The same AP then connects to a **secondary zone** managed by another mobility controller, handling another set of wireless networks for **Airline 2**.
- Each airline can manage its own wireless network independently, avoiding interference even though they share the same physical AP.

This type of network setup works not only for airlines but also for any scenario where different entities need isolated but shared wireless access points, such as bus companies at a terminal or different corporate entities within the same building.

---

### **Benefits of Multi-Zone**:

- **Improved Traffic Separation**: Each zone manages its own wireless LANs, preventing cross-network interference.
- **Independent Management**: Multiple teams (e.g., airline administrators) can manage their own settings without affecting others.
- **Flexibility**: One AP can connect to multiple mobility controllers, allowing for flexible deployments in environments with multiple networks or clients.




## **Use Cases for Multi-Zone**:

1. **Airports**: Airlines can control their own networks without affecting others, while still using the same AP hardware.
2. **Public Transport Terminals**: Different bus companies or services can deploy their own networks independently.
3. **Corporate Campuses**: Separate corporate networks can be deployed across different zones to avoid traffic interference.



## **Key Takeaways**

- The **Multi-Zone feature** in Aruba allows an AP to connect to multiple controllers in different zones, ensuring isolated configurations and independent traffic management.
- **Multi-Zone** is beneficial in environments where different entities need to share AP hardware but require separate network management, such as airports or corporate campuses.
- By using this feature, Aruba provides flexibility and improved traffic separation without compromising on performance or network security.









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





