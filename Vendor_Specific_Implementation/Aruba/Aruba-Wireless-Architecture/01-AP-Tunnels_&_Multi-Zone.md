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

---

## **Aruba AP Tunnels**

### **How AP Tunnels Work**

#### **1. Tunnel Establishment**
- Aruba APs create **GRE tunnels** to connect to the Aruba controller.
- These tunnels enable secure communication and traffic forwarding.

#### **2. Traffic Flow**
1. APs send encrypted traffic to the controller via these tunnels.
2. The controller:
   - Decrypts the packets.
   - Processes them.
   - Applies **firewall policies**.
3. Packets are either:
   - Switched internally.
   - Routed externally, based on configuration.

#### **3. User Authentication**
- Before transmitting data, users must authenticate through **control traffic**, managed securely by the controller.

---

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

## **GRE Tunnels: Advanced Details**

### **1. Per-SSID Tunnels**
- Each AP creates:
  - **One GRE tunnel per SSID** for each radio (e.g., 2.4 GHz and 5 GHz).
  - **One keep-alive tunnel** for monitoring communication health.
- **Example**:
  - **AP with 3 SSIDs and 2 radios**:
    - \( (3 \text{ SSIDs}) \times (2 \text{ radios}) + 1 \text{ keep-alive tunnel} = 7 \text{ total tunnels} \).

### **2. Total Tunnel Calculation**
- **Formula**:  
  \[
  \text{Total Tunnels} = (\text{SSIDs per Radio}) \times (\text{Radios}) + 1 \text{ (Keep-Alive Tunnel)}
  \]

- **Example Calculations**:
  1. **Single AP with 3 SSIDs and 2 Radios**:
     \[
     3 \text{ SSIDs} \times 2 \text{ Radios} + 1 \text{ Keep-Alive} = 7 \text{ Tunnels}
     \]
  2. **10 APs, Each with 6 SSIDs and 2 Radios**:
     \[
     6 \text{ SSIDs} \times 2 \text{ Radios} + 1 \text{ Keep-Alive} = 13 \text{ Tunnels per AP}
     \]
     \[
     13 \text{ Tunnels per AP} \times 10 \text{ APs} = 130 \text{ Total Tunnels}
     \]

---

## **Bridge Mode Exception**
- APs in **bridge mode** do not forward user traffic through GRE tunnels.
- Instead, user traffic is routed directly to its destination by the AP.

---

## **Aruba MultiZone**

**MultiZone** enables a single AP to connect to multiple controllers simultaneously, segmenting traffic between zones. 

### **How it Works**
1. **Primary Zone**:
   - Default controller for AP management and primary traffic handling.
2. **Secondary Zones**:
   - Additional controllers for specific networks (e.g., guest networks).
3. **Traffic Segmentation**:
   - Isolates traffic between zones for enhanced security.

### **Example**:
- **Primary Zone**: Internal corporate network.
- **Secondary Zone**: Guest Wi-Fi for isolated internet access.

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





