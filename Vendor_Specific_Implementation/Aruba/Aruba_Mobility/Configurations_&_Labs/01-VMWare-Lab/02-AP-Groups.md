# 🔥🧱🛡️ Aruba: `Lab - AP Groups`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Aruba` `MC` `Mobility Controller` `WLC` `IEEE 802.11` `Wireless`

---



<br>

# 📝❓📄 `Index`


# Aruba Mobility Controller: `AP Groups`

**AP Groups** within the Aruba Mobility Controller which plays a crucial role in simplifying the management and deployment of large wireless networks. 

An **AP Group** is a collection of access points (APs) managed under a single configuration set, which allows you to apply uniform settings to all the APs in the group. This concept significantly reduces the complexity of managing individual AP configurations, making it easier to scale and optimize your network.

Aruba's **AP Groups** offer a powerful and flexible way to manage large wireless networks by grouping access points and applying centralized configurations. This simplifies management, improves scalability, and enhances network performance. With features such as **Virtual APs (VAPs)**, **Client Match**, and **RF Management**, Aruba provides the tools necessary to optimize wireless networks for various use cases and environments.

By utilizing **AP Groups**, network administrators can easily scale their Aruba wireless infrastructure while maintaining a high level of control and customization over the wireless experience for different user groups.

An **AP Group** in Aruba refers to a logical collection of access points (APs) managed by a Mobility Controller. All APs within a group share the same configuration settings, meaning you can apply wireless configurations to the group as a whole, rather than individually configuring each AP. This approach simplifies network management and enhances consistency across your wireless infrastructure.

### Key Points About Aruba Mobility Controller AP Groups:

| Feature                             | Benefit                                                       |
|-------------------------------------|---------------------------------------------------------------|
| **Centralized Configuration**       | Apply radio power levels, channels, SSIDs, security profiles, and more at the group level, which applies to all APs within the group. This saves time and ensures uniformity across your network. |
| **Simplified Management**           | By grouping similar APs, network administrators can manage large wireless networks more efficiently, reducing the need for individual configuration of each AP. |
| **Flexible Deployment**             | You can create multiple AP groups with different configurations to suit various areas or use cases within your network (e.g., guest networks, employee networks, or specific departments). |
| **Accessing AP Groups**             | AP groups can be accessed and managed through the Aruba Mobility Controller's GUI or by using the command line interface (CLI). For example, the command `show ap-group` can be used to display the list of available AP groups. |

## Virtual APs (VAPs) and AP Groups

A **Virtual AP (VAP)** allows a physical access point (AP) to broadcast multiple SSIDs (Service Set Identifiers). In an Aruba network, each VAP corresponds to a **Basic Service Set Identifier (BSSID)**, which is unique to the SSID. This enables each AP to support multiple WLANs through separate VAP profiles, with each profile representing a unique SSID and associated configuration.

![image](https://github.com/user-attachments/assets/376c9037-0da2-433f-b37e-aee04f7c0029)

### VAP Configuration in AP Groups

You can configure **Virtual APs (VAPs)** for each AP group, ensuring that different wireless networks can be managed within the same group of APs. For example, an AP group could be configured to broadcast an **Enterprise WLAN**, **Guest WLAN**, and **Management WLAN**, each with its own set of policies and security protocols. These configurations allow for easy segmentation of network traffic and tailored wireless experiences for different user groups.

| VAP Profile        | SSID                   | Associated Network Role       |
|--------------------|-------------------------|-------------------------------|
| **VAP 1**          | Enterprise WLAN         | Corporate users               |
| **VAP 2**          | Guest WLAN              | Guest users                   |
| **VAP 3**          | Management WLAN         | Admin access                  |
| **VAP 4**          | Finance WLAN            | Secure, high-priority access  |

### Example of AP Group and VAP Configuration

Consider a multi-floor office setup with different user groups and needs:

#### **Floor 1**: **Enterprise & Guest WLANs**
- **AP Group 1** contains APs that broadcast the **Enterprise WLAN** and **Guest WLAN** SSIDs using different VAPs.

#### **Floor 2**: **Management & Finance WLANs**
- **AP Group 2** contains APs that broadcast the **Management WLAN**.
- **AP Group 3** contains APs that broadcast the **Finance WLAN**.

By grouping APs in this way, you ensure that only the necessary SSIDs are broadcast in each area, improving airtime utilization and reducing network congestion.

## Advanced Features in AP Groups

### 1. **Client Match**  

Aruba’s **Client Match** technology automatically directs wireless clients to the optimal access point based on signal strength, load balancing, and other factors. This reduces the chances of congestion and ensures that clients are connected to the best AP.

### 2. **RF Management**  

Aruba’s **RF management** dynamically adjusts channel selection, transmit power, and other RF parameters to minimize interference and ensure optimal network performance. These adjustments can be configured at the **AP Group** level to suit specific network requirements for each area.

### 3. **Mesh Networking**  

AP Groups can be configured to support **mesh networking**, where APs wirelessly connect to each other to extend coverage without requiring physical cabling. Mesh network settings can be managed at the AP group level, allowing for consistent wireless performance across all connected APs.

### 4. **Policy Configuration**  

You can configure **network policies** (e.g., bandwidth limits, access control) for each VAP within an AP group. This ensures that critical traffic, like VoIP or video conferencing, is prioritized, while less critical traffic, such as guest access, is handled differently.

## Accessing and Managing AP Groups

To access and manage AP Groups, Aruba Mobility Controllers provide both a **Graphical User Interface (GUI)** and a **Command Line Interface (CLI)**.

- **GUI**: The Aruba Mobility Controller’s web-based interface provides an intuitive way to configure and monitor AP groups.
- **CLI**: Use commands like `show ap-group` to view the current AP groups and `configure ap-group <name>` to enter configuration mode for a specific AP group.








# Aruba Mobility Controller: `AP Group Configuration`

To access AP groups, go to **Configuration** and click on **Access Point Groups** (also known as "AP Groups"). You will see two default AP groups:

1. **Default** – We strongly recommend not modifying this, as changing its settings could interfere with other configurations.
2. **Node Group** – The second default group.

## Creating AP Group

Click on the **plus icon** to create one. Let’s name this group "Hockey" and click **Submit**.

![image](https://github.com/user-attachments/assets/6eb9375e-db11-4f00-82cc-21a372c77b63)

Once created, click on the group name to explore various options like **Apps**, **Wireless**, **LANs**, **Radio**, **Mesh**, **LMS**, and **Multi-zone**. Let's take a look at each one:

![image](https://github.com/user-attachments/assets/9dad262f-98d5-4a5a-b10c-ed207dc6050f)

## APs

Here, you will find details such as:

- The AP's name
- IP address 
- MAC address
- AP type
- Serial number

![image](https://github.com/user-attachments/assets/277c9278-82ef-4a7f-9bf1-8e09676c443c)

## WLANs

You can create a new wireless LAN by clicking the **plus icon** (at the bottom). Choose a **Virtual AP**. We'll use the default for now, but you can customize it later. When you select the Virtual AP, you can choose the AP group and set various limits, including airtime per user and per radio.

![image](https://github.com/user-attachments/assets/04c55294-686a-4ae1-9661-139a724d173e)

![image](https://github.com/user-attachments/assets/a0a51ab1-3928-4c57-b479-47f8f8b92976)

To delete an AP, simply click the **trash icon**.

![image](https://github.com/user-attachments/assets/4f699eb3-8a6c-450f-8d13-57e0cd87e8a9)

### Virtual AP

The **Virtual AP** is essentially what we call a **Wireless LAN**. It includes the SSID name and Triple-A (authentication, authorization, and accounting) settings. Let’s break these down:

- **SSID Profile**: Defines the SSID, encryption, and authentication requirements.
- **Triple-A Profile**: Specifies the authentication method, user roles, and servers for Triple-A functionality.

You can have multiple Virtual APs, but it’s recommended to limit them to 3-4 SSIDs per AP. Too many SSIDs could overwhelm the radio's bandwidth with management frames, reducing airtime for data transmission. The maximum limit for SSIDs per AP is 16, but beyond 3-4 SSIDs can cause issues.

## Radio Settings

Under the **Radio** section, you'll find settings for both **2.4 GHz** and **5 GHz** bands:

- Select the **mode** (AP or spectrum mode).
- Enable **spectrum monitoring**.
- Adjust the **transmit power**.

![image](https://github.com/user-attachments/assets/6690e8b4-e6c3-465e-b8e8-10916e69983e)

There are different values for the 2.4 GHz and 5 GHz bands, and you can also select **valid channels**. The **Advanced tab** offers additional options, such as interference immunity.

### Basic Settings:

![image](https://github.com/user-attachments/assets/4201edf9-86fe-4dd9-916a-09f4bbb05bef)

---

### Advanced Settings:

![image](https://github.com/user-attachments/assets/c8df57fc-b47b-4323-b1cb-f11c97ae7c0a)


| **Parameter**                     | **Description**                                                                                                                                                                                                                                         |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**                           | Enter a name for the 2.4 GHz or 5 GHz radio profile.                                                                                                                                                                                                     |
| **Zone**                           | Enter the zone name for configuration. The same zone name can be configured on both 2.4 GHz and 5 GHz profiles, but not on two 2.4 GHz or two 5 GHz profiles.                                                                                           |
| **Legacy only**                    | Toggle to run the radio in non-802.11n mode (disabled by default).                                                                                                                                                                                      |
| **802.11d / 802.11h**              | Toggle to allow the radio to advertise 802.11d (Country Information) and 802.11h TPC capabilities (disabled by default).                                                                                                                                |
| **Beacon interval**                | Enter the Beacon period in milliseconds (range: 60-500, default 100 ms). Specifies how often the 802.11 beacon frames are transmitted.                                                                                                                   |
| **Interference immunity level**    | Select immunity level to improve performance in high-interference environments (default level is 2).                                                                                                                                                      |
| **Channel switch announcement count** | Specify the number of announcements before switching to a new channel to help clients recover gracefully from the channel change.                                                                                                                       |
| **Background spectrum monitoring** | Toggle to allow Instant APs to monitor RF interference while continuing normal access service, including monitoring non-Wi-Fi sources (e.g., microwaves, cordless phones).                                                                               |
| **Customize ARM power range**      | Enable to select minimum and maximum power range for 2.4 GHz and 5 GHz frequencies (default 3 dBm).                                                                                                                                                       |
| **Very high throughput (VHT)**     | Ensure VHT is enabled for 5 GHz radio on 802.11ac devices. Clear to disable VHT, making the AP function as 802.11n.                                                                                                                                      |
| **Smart antenna**                  | Select Enabled for smart antenna polarization on IAP-335 access points to optimize antenna selection based on collected data. This feature helps improve signal reception and performance. (Disabled by default).                                       |

- **Note:** In Aruba networking, "split radio" refers to a feature on certain access points that essentially divides a single 5GHz radio band into two separate, smaller 5GHz radios, allowing the AP to operate with three distinct radio bands (one 2.4GHz and two separate 5GHz) - effectively giving the AP "tri-radio" functionality

### Interference Immunity

Aruba’s interference immunity features enhance network performance by mitigating interference from other devices. Aruba’s Adaptive Radio Management (ARM) leverages multiple tools to optimize the network:

- **RFProtect Spectrum Analyzer** detects and classifies interference.
- **Noise immunity** boosts performance in environments with non-802.11 noise.
- **Transmit Power Control (TPC)** lowers RF output to minimize interference.

ARM dynamically monitors and adjusts the network to provide optimal access for all users. The system has five levels of interference immunity, with each level offering increased protection against different types of interference, but higher levels may reduce the AP's range. Increasing the immunity level improves performance but can limit coverage.

---

### Client Control

You can enable **Client Match**.

In the **Elements Settings**, you can define the IP addresses for backup options and local mobility switches. You can also configure IPv6 addresses here if needed.

### Multi-zone
If the **Multi-zone** feature is enabled, you’ll see profiles for it. This feature requires a license, and here you can set the **primary zone** and **number of controllers** associated with it. If you're not focusing on Multi-zone, you can disable this feature for now.

### Right Panel Options
On the right-hand side, you can manage changes to the group, such as setting a **group time limit** or other constraints. If you don’t need these options, you can remove them. You can also see **pending changes** that have been made to the AP group.

To deploy changes to the Mobility Controller, click **Deploy Changes**. If you wish to discard them, click **Discard Changes**.

### Summary
In this video, we covered:
- AP groups and how to configure them.
- Virtual AP settings and their elements.
- Radio and other configuration options for the AP group.

I hope this video has been helpful. Thank you for watching!


































# 📚🗂️🎥 Resources

- https://www.arubanetworks.com/techdocs/Instant_83_WebHelp/Content/Instant_UG/ARM/Configuring_Radio_Settings.htm
  
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





