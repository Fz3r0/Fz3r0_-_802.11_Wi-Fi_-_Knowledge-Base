# 🔥🧱🛡️ Aruba Wireless: `Licencing`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Aruba` `MC` `Mobility Controller` `WLC` `IEEE 802.11` `Wireless`

---



<br>

# 📝❓📄 `Index`




# Aruba Wireless Licensing Overview

This document provides a detailed explanation of the types of licenses available for Aruba systems, their use, key concepts, and how to effectively manage licensing. Licenses are essential to enable features on mobility controllers and other devices within the Aruba infrastructure.

## Types of Aruba Licenses

### 1. **Evaluation Licenses**

Evaluation licenses are temporary and allow the testing of specific Aruba features for a limited period.

- **Duration**: Evaluation licenses are provided in 30-day increments and can be valid for up to a maximum of 90 days.
- **Use**: They are available in the license database until you decide to reset the controller.

**Characteristics**:

- Allows testing of specific features.
- The 90-day period can be extended within that limit.

---

### 2. **Permanent Licenses**

Permanent licenses are activated to enable software modules and features on mobility controllers.

- **Use**: These licenses are tied to software features that require activation for operation.

---

### 3. **Subscription-Based Licenses**

Subscription-based licenses are specific to features like WebRTC and other web content features.

- **Duration**: These licenses can be purchased for 1, 3, 5, 7, or 10 years.
- **Expiration Alert**: A 30-day warning is sent before the subscription expires on the Mobility Master.
- **Grace Period**: After expiration, there is a 120-day grace period to continue using the license before it fully expires.

| **License Type**           | **Duration**   | **Key Features**                                |
|----------------------------|----------------|-------------------------------------------------|
| Evaluation License          | Up to 90 days  | Test specific features at no cost               |
| Permanent License           | Unlimited      | Activates software features                    |
| Subscription-Based License  | 1-10 years     | WebRTC, advanced encryption, etc.               |

## License Usage

### 1. **Licenses for Mobility Master and Controllers**

Licenses for Mobility Master and Mobility Controllers are essential for managing and distributing licenses within the network.

| **License Type**           | **Required Quantity** |
|----------------------------|-----------------------|
| Mobility Master License    | 1 per Mobility Master |
| Controller License         | 1 per Mobility Controller |
| Access Point License (AP)  | 1 per Access Point    |

### 2. **Licenses for Specific Features**

The following licenses are required to enable additional features within the Aruba ecosystem:

- **Policy Enforcement Firewall (PEF) License**: Required for advanced policy management and application identification.
- **RF Protect**: A license required for intrusion protection, spectrum analysis, and multi-zone features.
- **Dynamic Segmentation**: Needed for dynamic segmentation, which is crucial for separating different types of traffic for security and performance.

| **Feature**                 | **Required License**             | **Description**                                                                 |
|-----------------------------|----------------------------------|---------------------------------------------------------------------------------|
| Policy Enforcement Firewall  | 1 per AP and enabled feature     | Controls traffic, smart policies, and firewall for applications                  |
| RF Protect                   | 1 per AP using the feature       | Protection from intrusions and spectrum analysis                                |
| Dynamic Segmentation         | Depends on configuration         | Traffic segmentation to improve network security and performance                |

### 3. **Subscription-Based Licenses (WebRTC and Others)**

Subscription-based licenses, such as WebRTC and advanced encryption, are additional licenses acquired on an annual or multi-year basis.

- **WebRTC License**: Enables real-time communication (audio, video, and data) over the network.
- **CR License**: Required for advanced encryption features.

## License Management with ArubaOS

ArubaOS offers a centralized licensing architecture that allows for the management of a group of devices with a shared set of licenses.

### 1. **Global and Dedicated Licenses**

- **Global Pool**: A single shared pool of licenses across all devices, utilized through the Mobility Master.
- **Dedicated Pools**: Specific license groups can be configured for certain devices or locations, ensuring flexibility.

| **License Type**           | **Description**                                                        |
|----------------------------|------------------------------------------------------------------------|
| Global License Pool         | A shared pool of licenses for all managed devices                       |
| Dedicated License Pool      | Licenses assigned specifically to certain devices or locations          |

### 2. **License Compatibility with Backup and Redundancy**

- **Primary and Backup Mobility Master**: Both can share a single set of licenses to avoid redundancy.
- **License Handling in Case of Disconnection**: Even if the connection between a managed device and the Mobility Master is lost, the devices continue functioning with the assigned licenses.

## Calculating Required Licenses

### License Calculation Example:

If you have 3 mobility controllers managed by 1 mobility master and 350 access points, the required licenses would be:

| **Resource**              | **Required Quantity** |
|--------------------------|-----------------------|
| Mobility Master Licenses  | 3                     |
| Access Point Licenses     | 350                   |
| Policy Enforcement Firewall Licenses | 350             |
| RF Protect Licenses       | 350                   |

**Note**: RF Protect, WebRTC, and Policy Enforcement Firewall licenses are optional but recommended based on network needs.

**Note 2:** The Mobility Master does not requiere additional Licence, just the Mobility Master licences for each Mobility Controller

## Summary

Aruba Wireless licenses are essential for effectively managing your network infrastructure. There are three main types of licenses: **Evaluation**, **Permanent**, and **Subscription-Based**, each designed to offer flexibility based on your network's requirements.

License usage is straightforward to manage through ArubaOS, with options for global or dedicated configurations. Additionally, licenses for advanced features such as **Policy Enforcement Firewall**, **RF Protect**, and **Dynamic Segmentation** may be critical for maintaining the security and optimal performance of your network.

Be sure to plan your license acquisition and management carefully to make the most out of your Aruba Wireless capabilities!

# Licensing procedure for Demo licenses

1. Ir a licensing

<img width="1492" height="427" alt="image" src="https://github.com/user-attachments/assets/21b84d22-e6ba-42c3-902a-a43bf7cbc7cc" />

2. Copiar passphrase para enviar a Aruba Suppor PArtner

<img width="531" height="345" alt="image" src="https://github.com/user-attachments/assets/f964688a-d8c3-4b7a-8a2f-e4a9bedf8758" />

3. Ellos se harán cargo de generar licencias como: 

- MM Virtual
- MC Virtual
- APs OJO!!! revisar si el AP es US, RW, etc!!!
- Firewall (optional)
- 





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





