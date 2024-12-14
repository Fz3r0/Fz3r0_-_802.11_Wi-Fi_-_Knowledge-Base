

## 🚨🆘 WLAN Troubleshooting Methodology: `CWAP`
_CWAP methodology provide comprehensive methodologies that include problem identification, data analysis, and thorough documentation._

1. **Identify the problem**: What is happening? Example: Some users are reporting very slow speeds since the new APs were installed. 
2. **Discover the scale of the problem**: How many clients are impacted? Example: Only clients connected to the 5 GHz network where new APs were installed. 
3. **Identify possible causes of the problem**: Probable causes based on experience and knowledge: There was a recent change (new APs installation) and all the configurations are the same as always. Something with new APs... 
4. **Capture and Analyze the Data**: Select apropiate method of capture, channel, width, location, ttime, etc. Analyzing Spectrum and MAC Frames: The QBSS Load Element is always to 90% and airtime utilization in always red. 
5. **Observe the Problem**: Reproduce the problem and understand the sequence of events :: Example: Install another driver on the device experimenting issues either client (eg. Smartphone) or network related (eg. Access Point). The airtime went down wen downgrading the firmware to the AP. 
6. **Choose appropiate remediation steps**: Since it's a device bug related, document the whole process until now and escalate the issue to Ruckus TAC Engineering Team. They came up with a solution
7. **Document the problem and resolution**: Documentation can be a daunting task and therefore is often put off to a later time or sometimes not done at all. This part of the troubleshooting process plays an important role as it allows for streamlined troubleshooting when a similar problem appears.






---

| **Standard** 	| **Ratification Period** 	| **Wi-Fi Version** 	|       **PHY Type**      	|   **Frequency Bands**   	| **Maximum Speed** 	|      **802.11-2012**     	|      **802.11-2016**     	|      **802.11-2020**     	|
|:------------:	|:-----------------------:	|:-----------------:	|:-----------------------:	|:-----------------------:	|:-----------------:	|:------------------------:	|:------------------------:	|:------------------------:	|
| **802.11**   	| 1997 original           	| "Prime"           	| DSSS /<br>FHSS          	| 2.4 GHz                 	| 2 Mbps            	| Clause 14 /<br>Clause 15 	| Clause 14 /<br>Clause 15 	| Clause 14 /<br>Clause 15 	|
| **802.11b**  	| 1999 r1.1999->2007      	| Wi-Fi 1           	| HR-DSSS                 	| 2.4 GHz                 	| 11 Mbps           	| Clause 17                	| Clause 16                	| Clause 16                	|
| **802.11a**  	| 1999 r1.1999->2007      	| Wi-Fi 2           	| OFDM                    	| 5 GHz                   	| 54 Mbps           	| Clause 18                	| Clause 17                	| Clause 17                	|
| **802.11g**  	| 2003 r1.2003->2007      	| Wi-Fi 3           	| ERP-OFDM & ERP-DSSS/CCK 	| 2.4 GHz                 	| 54 Mbps           	| Clause 19                	| Clause 18                	| Clause 18                	|
| **802.11n**  	| 2009 r2.2009->2012      	| Wi-Fi 4           	| HT-OFDM (SU-MIMO)       	| 2.4 & 5 GHz             	| 600 Mbps          	| Clause 20                	| Clause 19                	| Clause 19                	|
| **802.11ac** 	| 2013 r3.2013->2016      	| Wi-Fi 5           	| VHT-OFDM (MU-MIMO)      	| 5 GHz                   	| 7 Gbps            	| Clause 22                	| Clause 22                	| Clause 22                	|
| **802.11ax** 	| 2021 r5.2021->2020      	| Wi-Fi 6 & 6E      	| HE-OFDMA (MU-MIMO)      	| 2.4, 5 & 6 GHz          	| 9.6 Gbps          	| N/A                      	| N/A                      	| Clause 27                	|
| **802.11be** 	| 2023 r5.2023->2024      	| Wi-Fi 7           	| EHT                     	| 5 & 6 GHz               	| 40 Gbps           	| N/A                      	|                          	|                          	|
| **802.11ad** 	| 2012 r3.2012->2016      	| _non Wi-Fi_       	| DMG                     	| 60 GHz (WiGig Networks) 	| 7 Gbps            	| //                       	|                          	|                          	|
| **802.11af** 	| 2013 r3.2013->2016      	| _non Wi-Fi_       	| TVHT                    	| TV White Space (TVWS)   	| 570 Mbps          	| //                       	|                          	|                          	|
| **802.11ah** 	| 2016 r4.2016->2020      	| _non Wi-Fi_       	| S1G                     	| < 1 GHz (IoT & M2M)     	| 350 Mbps          	| //                       	|                          	|                          	|
| **802.11ay** 	| 2021 r5.2021-><<DRAFT>> 	| _non Wi-Fi_       	| Enhanced DMG            	| > 45 GHz                	| //                	| //                       	|                          	|                          	|
| **802.11bb** 	| 2023 r5.2023-><<DRAFT>> 	| _non Wi-Fi_       	| Li-Fi                   	| Light Waves             	| //                	| //                       	|                          	|                          	|

![image](https://github.com/user-attachments/assets/cb3c5ab7-42d6-4234-9d7f-1e460c722bfc)


















# Architecture

## 🏗️ DS Devices

- WLAN Controller	
- Mesh Access point
- Autonomous access point
- Switch
- Router
- Firewall

## 🤳🏾 STA Devices

Everything that can understand and Tx/Rx IEEE 802.11 Wi-Fi transmissions

- Smartphone
- Laptop client radio
- VoWiFi Phone
- Access Point
- QAP

## 🤳🏾 client-STA Devices

Better known just as "client STA"

- Smartphone
- Laptop client radio
- VoWiFi Phone

## 📡 AP-STA Devices

Better known just as "AP"

- Access Point
- QAP (QoS AP)
  
## 🤳🏾🏗️📡 802.11 Services: `The 3 Categories`

The architecture categorizes services into three primary types, each serving distinct purposes.

1. **`SS`**: Station Service
2. **`DSS`**: Distribution System Service
3. **`PCPS`**: BSS Control Point Service _(CWAP out of Scope)_

## 🤳🏾📡 `SS (Station Services)` 

A Station Service (SS) exists in all 802.11 stations, including client stations (STAs) and access points (APs).

### 🤳🏾📡 SS (Station Services): `Types`
_There are two diffenet type of STAs (APs & Client STA), the third type is the same as APs or STAs but with QpS support._
- [**`STA`** = Client STA](https://en.wikipedia.org/wiki/Station_(networking)) :: Any device containing IEEE 802.11 MAC & PHY interface to the WM `Does NOT act as AP`
- [**`AP`** = Access Point STA](https://en.wikipedia.org/wiki/Wireless_access_point) :: Networking device that allows other Wi-Fi devices to connect to a network `Act as an AP` <br> <br>
- [_**`QSTA`** & **`QAP`** = STA/AP-QoS_](https://www.redalyc.org/pdf/6380/638067265006.pdf) :: Any AP or STA that supports Wi-Fi Multimedia 802.11e QoS  _(Any modern device)_

---

### 🟣🤳🏾 Client STA: `Modes`

STAs can have any of the following modes:

- 🤳🏾[**`Infrastructure Mode`**](https://www.lifewire.com/infrastructure-mode-in-wireless-networking-816539) :: Device that needs an AP to connect to the Network
- 🤳🏾[**`Ad-Hoc Mode`**](https://www.ii.pwr.edu.pl/~kano/course/module8/8.1.3.2/8.1.3.2.html#:~:text=An%20ad%20hoc%20wireless%20network,device%20to%20connect%20to%20it.) :: 2 wireless devices communicate in a peer-to-peer (P2P) manner without using APs

### 🟣📡 AP: `Modes`

APs can have any of the following modes:

- 📡[**`Root Mode`**](http://webhelp.zyxel.com/wohView/help_docs/NWA5123-AC_V4.22_AAZY/Book/Wireless/h_Wireless.htm) Radio acts as AP & bring Wi-Fi connectivity to client STAs (supports connections with other APs in repeater mode)
- 📡[**`Repeater Mode`**]() Extends the wireless coverage of an existing network by amplifying the signal from another AP.
- 📡[**`Mesh Mode`** (Gateway / Repeaters)]() Multiple APs communicate over wireless interfaces to form a single network
- 📡[**`Bridge Mode`**]() Dedicated ethernet P2P replacement (Trunk), but cannot communicate with STA clients
- 📡[**`Workgroup Bridge Mode`**](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/RolesWGB.html) Device associates to another AP as a client & provides a network connection for the equipment connected to its Ethernet port
- 📡[**`Monitor Mode`**]() Capture 802.11 Frames // Check for IDS events, Rogues APs, Determine Position,e tc
- 📡[**`Sensor Mode`** / **`Sniffer Mode`**]() Dedicates its time to Capture 802.11 frames
- 📡[**`Rogue Detector Mode`**]() Detect rogues within the BSS area

---

### 🟣🛜 802.11 SS (Station Services): `Services`

APs or client STAs can manage any of the next services:

- **`Authentication`** - Validates the identity of devices trying to join the WLAN.
- **`Deauthentication`** - Removes authenticated status of devices from the WLAN.
- **`Data confidentiality (encryption)`** - Ensures that transmitted data is secure and cannot be intercepted.
- **`MSDU delivery`** - Delivers MAC service data units (MSDUs) between stations.
- **`DFS (Dynamic Frequency Selection)`** - Manages frequency usage to avoid interference.
- **`TPC (Transmit Power Control)`** - Regulates the transmit power of devices to optimize performance and reduce interference.
- **`Time Synchronization with higher layers (QoS only)`** - Synchronizes time between STAs and higher layer protocols for QoS management.
- **`QoS traffic scheduling (QoS only)`** - Prioritizes and schedules traffic based on quality of service requirements.
- **`Radio Measurement`** - Collects and reports radio metrics for network optimization.
- **`DSE (Dynamic STA Enablement)`** - Enables dynamic stations based on network requirements.

## 🏘️📡🖧 `DSS (Distribution System Service)`

Distribution System Service (DSS) according to IEEE 802.11 is a functionality that allows the interconnection of several WLAN networks, thus creating a larger and more efficient network. This service allows several workstations to connect to the same network, regardless of their physical location. The DSS service is used in business and public environments, such as airports, shopping malls, and train stations. It allows a fluid and uninterrupted connection to users who move from one coverage area to another. The DSS service provides a scalable and flexible infrastructure, allowing companies and organizations to adapt to the changing needs of their users. Additionally, the DSS service is compatible with a wide range of devices, making it easy to deploy and maintain.

| **Service Name**                                            | **Network Type**                                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Example**                                                                                                                     |
|-------------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **`DSS`**<br>**Distribution System Service**                | Centralization of the whole Network Infraestructure | **The DSS is used to manage client station associations, reassociations, disassociations and more and operates only within AP and Mesh Portals.** // The infrastructure that interconnects the APs in an ESS. It typically consists of a wired network but can also include wireless backhaul connections.                                                                                                                                                                                                                                                                         | The centralized network connecting all APs and controllers in an office building                                                |
| **`DS`** <br>**Distribution System**                        | Infrastructure                                      | **It is used to connect a set of basic service sets (BSS) via integrated LANs to create an extended service (ESS). The two components of the DS are the DSS and the DSM** // The backbone that connects multiple APs to a network, forming an ESS. It allows communication between APs and provides the path for data exchange.                                                                                                                                                                                                                                                    | The wired network (Router, Switches and Cables) connecting multiple APs across different floors or buildings                    |
| **`DSM`** <br>**Distribution System Media/Medium**          | Infrastructure                                      | **The logical physical medium used to connect APs.  The most common would be 802.3 ethernet (copper/fiber)** // The backbone that connects multiple APs to a network, forming an ESS. It allows communication between APs and provides the path for data exchange.                                                                                                                                                                                                                                                                                                                 | The medium that connects the LAN/WLAN (wired medium or RF/air medium)                                                           |
| **`ESS`**<br>**Extended Service Set**                       | Infrastructure                                      | **It is when you have two or more identically configured BSSs connected by a DS medium** // You can think if this as all of the APs and clients that are united by a DSM.  The coverage area of the ESS in the which the clients can communicate and roam is called the extended service area (ESA).  Just because you have an ESS, does not mean you have guaranteed roaming.                                                                                                                                                                                                     | A corporate wireless network with multiple Switches and APs across different floors, where clients can roam using the same SSID |
| **`BSS`** <br>**Basic Service Set**                         | Infrastructure or Independent                       | **The coverage area produced by a BSS, this means the coverage provided by a single AP.** // The size and shape of this coverage vary depending on AP placement, transmit power, antenna gain, environment, and receive sensitivity. The basic building block of an 802.11 Network. If at home you have a single wireless router and no other wireless access points, this would be considered a BSS.                                                                                                                                                                              | One AP covering an office / One AP covering a house                                                                             |
| **`QBSS`** <br>**QOS Basic Service Set**                    | Infrastructure or Independent                       | **Simply QoS implementation in a BSS** // Every new enterprise APs will have QoS capabilities                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | One AP covering an office / One AP covering a house (with QoS)                                                                  |
| **`MBSS`** <br>**Mesh Basic Service Set**                   | Mesh                                                | **BSS using wireless mesh networking** // Multiple radios Mesh Network One radio (CH1) of the AP is used for a Bridge wireless traffic from one AP to another AP, The other Radio (CH2) is used Transmitt & Recieve Traffic Betweet AP & client STAs.                                                                                                                                                                                                                                                                                                                              | A mesh network used in a large office campus without ethernet connections                                                       |
| **`SSID`** <br>**Service Set Identifier**                   | Infrastructure or Independent                       | **Logical (human read) name of the network (Every SSID will have its own BSSID)** // It is the logical name given to an 802.11 network to identify it.                                                                                                                                                                                                                                                                                                                                                                                                                             | "Corporate_Wi-Fi"                                                                                                               |
| **`ESSID`** <br>**(Extended) Service Set Identifier**       | Infrastructure                                      | **Logical (human read) name of the network extended with 2 or more APs: Every SSID will have its own BSSID** // It is the logical name given to an 802.11 network to identify it. For proper roaming, the SSID and security must be exactly the same.                                                                                                                                                                                                                                                                                                                              | "Corporate_Wi-Fi"                                                                                                               |
| **`BSSID`**<br>**Basic Service Set Identifier**             | Infrastructure or Independent                       | **Logical (machine read) unique identifier for each BSS** // It is a 48-bit identifier, usually the MAC address of the AP or the first client that started the BSS. Each SSID will have a unique BSSID in a multi-AP network.                                                                                                                                                                                                                                                                                                                                                      | "00:14:22:01:23:45"                                                                                                             |
| **`MBSSID`** <br>**Multiple Basic Service Set Identifiers** | Infrastructure                                      | **Multiple SSIDs on a single AP** // It is recommended to keep this to a minimum. Ideally, limit it to three if possible. That said, when you have more than one, you will need a unique L2 BSSID identifier. When this occurs, the AP will create a unique MAC in increments of its hardware-coded MAC, each assigned to a unique L3 VLAN network. Each additional SSID adds overhead in the form of beacons, probe responses, and other management and control frame overheads.                                                                                                  | One AP with separate networks: "Corporate_Wi-Fi" (00:14:22:01:23:45) and "Guest_Wi-Fi" (00:14:22:01:23:46)                      |
| **`AP`** <br>**Access Point**                               | Infrastructure or Independent                       | **Access Point** // A device that allows wireless devices to connect to a wired network using Wi-Fi. The AP creates a wireless local area network (WLAN) by connecting to a router.**                                                                                                                                                                                                                                                                                                                                                                                              | An AP on the ceiling of an office                                                                                               |
| **`STA`** <br>**Station (client)**                          | Infrastructure or Independent                       | **Client Station** // Any device that is able to use the 802.11 protocol to communicate wirelessly. It can be a client device like a laptop, smartphone, or an AP.                                                                                                                                                                                                                                                                                                                                                                                                                 | Laptops, smartphones, and tablets used by employees                                                                             |
| **`BSA`** <br>**Basic Service Area**                        | Infrastructure or Independent                       | **Physical area which is covered by one Access Point (AP)** // It's common to name the BSA as "the cell of coverage of an AP"                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Single AP cell Coverage                                                                                                         |
| **`IBSS`** <br>**Independent Basic Service Set**            | Independent                                         | **Ad-Hoc Peer to Peer Wireless Network** // Most basic type of IEEE 802.11 LAN, no APs or Routers in use, only Ad-Hoc/Peer-to-Peer devices // Clients communicate directly. Also known as peer-to-peer or ad-hoc. All clients must share the medium time and respect the same channel. The first client that connects creates the BSSID. In High Scale or Enterprise WLAN Networking is not recomended to use IBSS Independent WLANs because in this kind of enviorments can cost a lot of problems of interference, the best practice is only allow Infraestructure (BSS or ESS)  | Direct communication between laptops in a meeting room without using an AP (ex. Wi-Fi DIRECT screen share)                      |
| **`PBSS`** <br>**Personal Basic Service Set**               | Independent                                         | **Similar to the IBSS, the PBSS is a type of IEEE 802.11 LAN in which STAs communicate directly with each other** // Used for direct communication between 802.11ad stations in the 60GHz band. A client assumes the role of PBSS control point (PCP) and synchronizes communication between all clients.                                                                                                                                                                                                                                                                          | Wireless communication between devices in a high-frequency, sometimes used for IoT wireless devices                             |

## 🖧⚖️⚙️ Network Planes: `Control`, `Data`, `Management`
_**Control, Management, and Data Planes are conceptual planes that include different types of communications. The control plane is about network control protocols like routing protocols and switching protocols. In WLANs it includes things like radio resource management (RRM) and adaptive radio management (ARM). The management plane is focused on managing the devices and monitoring them, such as WLAN configuration and monitoring. The data plan is focused on user data transfer. The users care about the data plane, but the control and management planes allow the network administrators to ensure that the users get the performance they require out of the data plane.** Consider RRM as an example and how it relates to the different planes. In the control plane, radio resource management (RRM) operates. In the management plane, radio resource management (RRM) is configured. In the user plane, data is sent on a WLAN that uses radio resource management (RRM) for radio configuration management. In the end, that which occurs in the control and management planes impacts the data plane functionality and performance._

- [CWNP: The Plane Truth](https://www.cwnp.com/the-plane-truth/)
- [The foundation of WLAN architecure: Network Planes](https://techimike.com/cwna-chapter-11-wlan-architecture/)
- [Control, Management & Data Plane: Wireless Networks](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/blob/main/Fz3r0_-_802.11_Wi-Fi/802.11_Design/802.11_Network_Architecture/Network_Planes/Wireless_Control-Management-%26-Data-Planes.md)

---

### ⚙️🖧🥪 Network Planes: `Management Plane`
_The management plane is defined by administrative network management, administration and monitoring.  Here we would have a network-management solution used to monitor network devices.  Within 802.11 the functions of the management plane are: WLAN Configuration, WLAN Monitoring and Reporting, WLAN Firmware Management._

- This operation set addresses network configuration, monitoring, and administration.    In the early days of autonomous APs, management was performed uniquely on an AP-by-AP basis, and this was a major scalability drawback.  Initially, WLANs did not have a shared management plane, which meant that admins had to login to and manage each device independently.  The Wireless Network Management System (WNMS) came into play for management and monitoring of autonomous APs and were mostly usurped when WLAN controllers were introduced.  WLAN controllers were ushered in to centralize network management as well as to take on other roles that are part of the control and data planes.  At some point, multiple WLAN controllers become unwieldy, so a management solution is needed for them as well.  The WNMS comes back into play for that purpose.  Some devices exist solely to perform management functions.  Example functions of the management plane include firmware upgrades, device configuration, and network and status reporting and monitoring. <br> <br>
    - **`Example`**: APs configured and managed from the WLC, for example: SSIDs configuration (name, security, min data rates, bandwith control, max clients per AP, etc) 

---

### 🎮🖧🥪 Network Planes: `Control Plane`
_The control plane consists of control or signaling information and is often defined as network intelligence or protocols.  An example would be CAM tables and STP used by L2 switches for data forwarding.  Within 802.11 we have the following examples: | Adapative RF or RRM: Where coordinated channel and power settings for multiple APs are provided. |  Roaming Mechanisms:  This provides support for roaming handoffs between APs. | Client and Load Balancing:  Client load and performance metrics are collected and shared between APs to improve the WLAN experience | Mesh Protocols:  WLAN vendors use either L2 or L3 routing protocols to move user data between mesh APs._

- This plane includes the “control” functions related to effective cooperation and interaction between devices within a network.  Similar to the management functions, early networks with autonomous APs didn’t share a control plane.  They shared an Ethernet network for connectivity, but the APs did not communicate with each other to coordinate network control operations.  WLAN ‘control’lers are now the de facto solution to address the needs of the control plane, where many of these operations are centralized into one device (a controller) that communicates with all of the APs.  Again, similar to the management plane, multiple controllers pose new challenges, because controllers need a protocol for communications between one another.  In any case, graceful control of a WLAN is necessary for scalability of any kind.  Example functions include RRM (channel and power settings for automated networks) coordination, mobility management (such as fast secure roaming and uninterrupted policy and security management during transitions), and load balancing.  These operations are usually performed within a WLAN controller, though protocols may be used between APs to perform the same. <br> <br>
    - **`Example`**: Adaptive RF, load balancing, band balancing, roaming handoff, AP neighbor report, rogue AP report and other mechanisms exist on the WLC 

---
  
### 💾🖧🥪 Network Planes: `Data Plane`
_Also known as the user plane, the data plane is where the user traffic is actually forwarded in a network.  An example is an individual router where IP packets are forwarded.  The two wireless devices that typically participate here are the AP and the WLC._

- This plane includes the handling of data within a network.  The two devices that usually participate in the data plane are the AP and the WLAN controller.  Autonomous APs obviously handle all data forwarding operations locally, but controller-based APs may have some variation of data handling.  Centralized data forwarding, where all data is forwarded from the AP to the WLAN controller for processing, may be used in many cases, especially when the WLAN controller manages encryption/decryption or applies security policies.  Distributed forwarding, where the AP performs data forwarding locally, may be used in situations where it is advantageous to perform forwarding at the edge and to avoid a central location in the network for all data, which may require significant Ethernet capacity.  As with the management and control planes, each vendor has a unique method for handling data forwarding, with pros and cons for each.  Other functions that are a part of the data plane are VLAN tagging, QoS classification and queuing, and policy enforcement. <br> <br>
    - **`Example`**: Data traffic from/to client STA <==> AP <==> WLC // The WLC exists as a data distribution point for user traffic. APs tunnel all user traffic to the controller.     

  














## Load Balanding and Band Balancing

- `Load Balancing`: **Moves already associated STA from AP-A to AP-B**. In Load Balancing an access point to request client stations to transition to a specific access point or to indicate to a client device a set of preferred access points. Load balancing is the process of moving associated stations to other access points in order to lessen the possibility of overloading an access point. <br><br>

- `Band Balancing`: **Ignore probe request on 2.4 GHz & wait for probe request on 5 ghz from new STA associations**. Band steering is a proprietary technology that is used to encourage dual band client STA’s to associate to the less crowded 5 GHz band instead of the 2.4 GHz band. One method that may be used is for the access point to ignore Probe Request frames that were sent from the client STA with the thought it will use 5 GHz. If the STA does not get an association to the 5 GHz it will end up connecting to the 2.4 GHz band during a later scan of the 2.4 GHz band.











# PHY Frames


# MAC Frames


- Presudo Header: Information not included in the MAC frame but captured by the PHY layer or added by capture tools. Examples include additional metadata about the transmission.
    - Radiotap header: Provides detailed transmission parameters (e.g., channel, RSSI, data rate).
    - Per PAcket Information (PPI): An older header format similar to Radiotap, providing metadata about packets. <br><br>
- Radio Information: Captured at the PHY layer but not part of the actual MAC frame. This data is used for analysis but isn't transmitted over the air. Examples include: Signal strength (RSSI, dBm Antenna Signal). Noise level (dBm Antenna Noise). Channel and frequency details. Modulation and coding schemes (MCS). <br><br>

- MAC Header: 

- Information Elements (IE): The information inside Management Frames

- Fixed Parameters

- Tagged Parameters:

- Data: Data inside data or QoS data frames, commonly coming from/to the DS. like a ping. 

- HT/VHT Capabilities

- HT/VHT Operation

## Management - Beacon

TBTT

- The target beacon transmission time (TBTT) determines the rate at which Beacon management frames are sent.
- This value is 1,024 microseconds
- 102.4 milliseconds = 100 TU (time units)

Listen Interval

- The listen interval information element in some 802.11 management frames is used for **unicast** power management purposes
- This value informs the access point of how many Beacons the STA will be dozing when in a power save state.
- For example if a STA has a listen interval of 15 that means it will doze for 15 Beacons and if the Beacon interval is 100 time units the STA will doze for approximately 1.5 seconds.



## Management - Association Request

- The Association Request frame from a client station contains the capabilities of the device.
- If the capabilities match those of the access point the STA is connecting to will become associated to the access point and part of the BSS.







## IEEE 802.11: `Action Frames`

- Action Frames are management frames used to trigger specific actions in a wireless cell.

Below is a detailed breakdown of the **Category Codes** and their respective **Action Codes**, along with Wireshark filters for each:

| **Category Code** | **Category Description**            | **Action Code**                                                                                      | **Wireshark Filter (Category)**           | **Wireshark Filter (Action)**              |
|--------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------|
| **0**             | Spectrum Management                | 0: Measurement Request<br>1: Measurement Report<br>2: TPC Request<br>3: TPC Report<br>4: Channel Switch Announcement<br>5-255: Reserved | wlan.fixed.category_code == 0            | wlan.fixed.action_code == {Action Code}    |
| **1**             | QoS                                | 0: ADDTS Request<br>1: ADDTS Response<br>2: DELTS<br>3: Schedule<br>4: QoS Map Configure<br>5-255: Reserved | wlan.fixed.category_code == 1            | wlan.fixed.action_code == {Action Code}    |
| **2**             | DLS                                | 0: DLS Request<br>1: DLS Response<br>2: DLS Teardown<br>3-255: Reserved                            | wlan.fixed.category_code == 2            | wlan.fixed.action_code == {Action Code}    |
| **3**             | Block ACK                          | 0: ADDBA Request<br>1: ADDBA Response<br>2: DELBA<br>3-255: Reserved                               | wlan.fixed.category_code == 3            | wlan.fixed.action_code == {Action Code}    |
| **4**             | Public                             | Action codes vary (refer to specific implementations)                                              | wlan.fixed.category_code == 4            | wlan.fixed.action_code == {Action Code}    |
| **5**             | Radio Measurement                  | 0: Radio Measurement Request<br>1: Radio Measurement Report<br>2: Link Measurement Request<br>3: Link Measurement Report<br>4: Neighbor Report Request<br>5: Neighbor Report Response<br>6-255: Reserved | wlan.fixed.category_code == 5            | wlan.fixed.action_code == {Action Code}    |
| **6**             | Fast BSS Transition                | 0: Reserved<br>1: FT Request<br>2: FT Response<br>3: FT Confirm<br>4: FT ACK<br>5-255: Reserved   | wlan.fixed.category_code == 6            | wlan.fixed.action_code == {Action Code}    |
| **7**             | High Throughput (HT)               | 0: Notify Channel Width<br>1: SM Power Save<br>2: PMSP<br>3: Set PCO Phase<br>4: CSI<br>5: Noncompressed Beamforming<br>6: Compressed Beamforming<br>7: ASEL Indices Feedback<br>8-255: Reserved | wlan.fixed.category_code == 7            | wlan.fixed.action_code == {Action Code}    |
| **8**             | SA Query                           | 0: SA Query Request<br>1: SA Query Response                                                       | wlan.fixed.category_code == 8            | wlan.fixed.action_code == {Action Code}    |
| **9**             | Protected Dual of Public Action    | Action codes vary (refer to specific implementations)                                              | wlan.fixed.category_code == 9            | wlan.fixed.action_code == {Action Code}    |
| **10-125**        | Reserved/Unused                    | N/A                                                                                               | wlan.fixed.category_code == {Category}   | wlan.fixed.action_code == {Action Code}    |
| **126**           | Vendor Specific Protected          | Action codes vary (proprietary use)                                                               | wlan.fixed.category_code == 126          | wlan.fixed.action_code == {Action Code}    |
| **127**           | Vendor Specific                    | Action codes vary (proprietary use)                                                               | wlan.fixed.category_code == 127          | wlan.fixed.action_code == {Action Code}    |
| **128-255**       | Error                              | N/A                                                                                               | wlan.fixed.category_code == {Category}   | wlan.fixed.action_code == {Action Code}    |

























# Important Elements to Remember

## MAC Header

## MAC Frame Sections :: `MAC Header` + `Frame Body` + `FCS`
_All MAC frames contain the first three header fields and the FCS. The frame type and subtype determine the additional fields that are contained in the frame. | The HT Control field is a part of the 802.11n amendment which is added to the MAC header || **IEEE-802.11-2020 :: 9.2.3 General frame format :: page 756**_

- [`MAC Header`](https://mrncciew.com/2014/09/27/cwap-mac-header-frame-control/) _`nayarasi`_ <br><br>
    - [MAC Header: `Frame Control`](https://mrncciew.com/2014/09/27/cwap-mac-header-frame-control/)
    - [MAC Header: `Duration` / `ID`](https://mrncciew.com/2014/10/25/cwap-mac-header-durationid/)
    - [MAC Header: `Addresses`](https://mrncciew.com/2014/09/28/cwap-mac-headeraddresses/)
    - [MAC Header: `Sequence Control`](https://mrncciew.com/2014/11/01/cwap-mac-header-sequence-control/)
    - [MAC Header: `QoS Control`](https://mrncciew.com/2014/10/03/cwap-mac-header-qos-control/)
    - [MAC Header: `HT Control`](https://mrncciew.com/2014/10/20/cwap-ht-control-field/) <br><br>

````py
## MAC Frame Sections :: MAC Header + Frame Body + FCS

|---------|-----------|---------|---------|---------|----------|---------|---------|---------||-------------||----------|
|  Frame  | Duration/ | Address | Address | Address | Sequence | Address |  QoS    |  HT     ||    Frame    ||    FCS   |
| Control |    ID     |    1    |    2    |    3    |  Control |    4    | Control | Control ||     Body    ||          |
|---------|-----------|---------|---------|---------|----------|---------|---------|---------||-------------||----------|
|    2         2           6       0 or 6    0 or 6    0 or 2     0 or 6    0 or 2    0 or 4 ||                               <<== Bytes
|____________________________________________________________________________________________||_____________||__________|
 \                                                                                          /   \          /  \        /
   \                                                                                      /       \      /      \    /
     \__________________________________________________________________________________/           \__/          \/
                                   MAC HEADER                                                   FRAME BODY        FCS
                              - Addressing                                                     - Var Lenght      - 32-Bit CRC:
                                 - Transmiter, Receiver, Source, Destination, BSSID               - Data /          - Check Sequence
                              - Control:                                                          - Payload         - Integrity
                                 - Frame Control
                                 - Duration                      
                                 - Sequence Control                                                   
                                 - QoS Control
                                 - HT Control

````

### 💊📦 `Frame Control` :: _2 Bytes / 16 Bits_

- Protocol Version
- Type
- Subtype
- To DS
- From DS
- More Fragments
- Retry
- Power Management
- More Data
- Protected Frame
- Order

---

### 💊📦 `Duration / ID` :: _2 Bytes / 16 Bits_
_2 Bytes / 16 bits long AKA 2 Octates | The duration field in a mac header has a two different purposes: 1 ) Duration: This field is used to reset NAV timers for devices on channel. Time in microseconds needed to complete the frame exchange, used to update STAs NAV (Network Allocation Vector). This is used a lot and it's important to know that this is not the duration of the current frame, it is the duration of the exchanges after the current frame requeried to actually complete the transaction 2) ID: Used in legacy PS-poll Frame to indicate the AID (Association ID) of the STA (AKA: ID of the Client Station given to the AP) to send the buffered frame in the AP | Expected duration of current transmission. Stations waiting for the medium use this to estimate when the channel will be free. | The contents of this field vary with frame type and subtype, with whether the frame is transmitted during the CFP, and with the QoS capabilities of the sending STA. | Omni peek shows this as duration, however it really is a duration / id field._ 

- IMP'ORTANT: the duration of the current wireless frame derived from The PHY header length field. The PHY header length field determines the amount of time it take to transmit the PPDU frame.

- 802.11 management frames that are sent to a broadcast address of FF FF FF FF FF FF will **have a duration value of zero**. The duration is a time value that STA’s will use to reserve the medium informing other STA’s in the BSS how long it will take for the frame exchange to complete. In this case since these frames are no acknowledged by a receiver they have a duration value of zero. The duration field is still in the MAC header but it is not used.

````py
## MAC Frame Sections :: MAC Header + Frame Body + FCS

## Duration (actual) :: Reset NAV timers for devices on channel STAs waiting for the medium use this to estimate when the channel will be free. Expected duration of current transmission after current frame
## ID (legacy)       :: STA send PS-poll Frame to AP to indicate the AID (Association ID) of the STA

|---------|-----------|---------|---------|---------|----------|---------|---------|---------|
|  Frame  | Duration/ | Address | Address | Address | Sequence | Address |  QoS    |  HT     |
| Control |    ID     |    1    |    2    |    3    |  Control |    4    | Control | Control |
|---------|-----------|---------|---------|---------|----------|---------|---------|---------|
               ||
               \/
        |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
        |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  |
        |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
           1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     <<== 2 Bytes / 16 Bits

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## ID (legacy)

#  Legacy Power Management – PS Poll frames use this field as an association identifer (AID)

        |-----|-----||-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
        |  1  |  1  ||     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        |     |     ||     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        |-----|-----||-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
           1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     <<== 2 Bytes / 16 Bits
                      |_________________________________________________________________________________|
                                                       Values:  0 - 2007

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Duration (Actual)

#  Virtual Carrier Sense – This is the main purpose which used to reset the NAV timer of the other stations

        |-----||-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
        |  0  ||     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        |     ||     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        |-----||-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
           1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     <<== 2 Bytes / 16 Bits
                |________________________________________________________________________________________|
                                                    Values:  0 - 32767

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## CFP Duration (PCF - Never Implemented in 802.11 Wi-Fi)

# Contention-Free Period (CFP) – This field is used as an indicator that a point coordination function (PCF) process has begun.

        |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
        |  1  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
        |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
        |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
           1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     1     <<== 2 Bytes / 16 Bits
         |_____________________________________________________________________________________________|
                                         23768  Transmitted by PC during CFP

````

- 📦 [**`Duration`** / **`ID`**](https://mrncciew.com/2014/10/25/cwap-mac-header-durationid/)  <br> <br>
    - ⭕ [ID (legacy)](https://mrncciew.com/2014/10/25/cwap-mac-header-durationid/) :: Legacy Power Management <br> <br>
        - PS-Poll (Legacy) :: AID 41 (ID of Station = 41) = `wlan.aid == 41`
        - PS-Poll (Legacy) :: AID 1723 (ID of Station = 1723) = `wlan.aid == 1723`
        - PS-Poll (Legacy) :: AID 2007 (ID of Station = 2007 [maximum value]) = `wlan.aid == 2007` br> <br>
    - ⭕ [Duration (Actual)](https://mrncciew.com/2014/10/25/cwap-mac-header-durationid/) :: Virtual Carrier Sense <br> <br>
        - Duration (Actual) :: ACK = 0 microseconds = `wlan.fc.type_subtype == 29 && wlan.duration == 0`
        - Duration (Actual) :: ACK > 0 microseconds = `wlan.fc.type_subtype == 29 && wlan.duration > 0` <br> <br>
        - Duration (Actual) :: Duration more that 0 microseconds = `wlan.duration > 0`
        - Duration (Actual) :: Maximum duration possible (32767) = `wlan.duration == 32767`
        - Duration (Actual) :: Duration more that 0 microseconds, without control frames = `wlan.duration > 0 && !wlan.fc.type == 1` <br> <br>
    - ⭕ [CFP Duration (PCF) - Not implemented in 802.11 Wi-Fi)](https://mrncciew.com/2014/10/25/cwap-mac-header-durationid/) :: Point Coordination Function (PCF) process has begun. <br><br>
        - _I can't find a CFP duration captured in the wild yet :(_
---













































# Physical Layer

### Integrity Check

- CRC (cyclic redundancy check) Errors : Layer 1 : Spectrum
    - A CRC error indicates a potential problem at the Physical Layer (PHY).
    - If a frame is received and indicates a CRC error the rest of the frame is ignored.
    - Protocol analyzers will use this information differently and in some cases will show a misrepresentation of the information that was received vs. the information that was transmitted.

- FCS Errors : Layer 2 : MAC Frame
    - The Frame Check Sequence is a checksum added to the end of a data frame at the Layer 2 level (MAC layer) to verify data integrity during transmission. (A calculation over all fields in an 802.11 MAC frame).
    - When a device receives a frame, it calculates its own FCS based on the data received and compares it to the FCS included in the frame. If they don't match, an FCS error is flagged, and the frame is discarded.
   

### Guard Interval

| **Wi-Fi Standard** | **Guard Intervals (GIs)**                          | **Explanation**                                                                                   |
|--------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **802.11n**        | 400 ns (short), 800 ns (long)                      | The 800 ns GI was chosen to accommodate the maximum multipath echo time in indoor environments.    |
| **802.11ac**       | 400 ns (short), 800 ns (long)                      | Same as 802.11n, offering 400 ns for short and 800 ns for long to optimize performance.            |
| **802.11ax**       | 800 ns (normal), 1600 ns (double), 3200 ns (quadruple) | Supports multiple GIs to handle higher frequencies and minimize interference in more complex environments. |


### 📡📏🤏 `HR-DSSS` / `802.11b` Short Preamble VS Long Preamble PPDU's:

|                                 | **Long Preamble PPDU**  | **Short Preamble PPDU** |
|---------------------------------|-------------------------|-------------------------|
| **Preamble lenght**             | 144 bits                | 72 bits                 |
| **SYNC lenght**                 | 128 bits                | 56 bits                 |
| **SFD lenght**                  | 16 bits                 | 16 bits                 |
| **SFD bits content**            | 1111 0011 0101 0000     | 0000 0101 1100 1111     |
| **Preamble Tx Rate**            | DBPSK (1 Mbps)          | DBPSK (1 Mbps)          |
| **PLCP-Header Tx Rate**         | DBPSK (1 Mbps)          | DQPSK (2 Mbps)          |
| **PSDU Tx Rate**                | 1, 2, 5.5 or 11 Mbps    | 2, 5.5 or 11 Mbps       |
| **(Preamble + Header) Tx Time** | 192 μs                  | 96 μs                   |


### PLCP Headers & Preamble

**PLCP `Preamble`:**

- Gives the time for the synchronizer (the reciever of the transmission) to synchronize with the transmission of the BSS. 
- Indicated to all nearby STAs that a frame is forthcoming.
- Includes a known pattern of 1's and 0's, when seen by other STAs they will know that a frame is coming. 
- Provides time for the receiver to detect the signal and synchronise with the signal.
    - Sent at the most robust Data Rate (lowest Data Rate in the band):
        - 2.4 GHz = 1 Mbps / 2 Mbps
        - 5 GHz   = 6 Mbps

**PLCP `Header`:**

- Communicates important information about the forthcoming PSDU such as Lenght and Data Rate.
- Information of the PLCP-Header is often shown in the Radio Tap Header or PPI section of a protocol decode.
    - Sent the Data Rate speciefied by the PHY:
        - HR-DSSS = Long Preamble  :: 1 Mbps
        - HR-DSSS = Short Preamble :: 2 Mbps
        - ERP, OFDM (HT/VHT/HE)    :: 6 Mbps

### 📡📏🦒 `HR-DSSS` / `802.11b` Long Preamble PPDU:

- 🔁 `Preamble`: <br><br>
    - **144 bits lenght** Preamble, includes fields: `SYNC` & `SFD`
    - The oldest PPDU format, supports 802.11 legacy technology <br><br>
        - ⭕ `SYNC` (128 bits) :: Gives the time for the synchronizer (the reciever of the transmission) to synchronize with this. **128 bits scrambled ones (1s)** <br><br>
        - ⭕ `SFD (Start Frame Delimiter)` (16 bits) :: Inform that the Preamble is ending and it's time to start to send the PLCP-Header using a unique sequence **1111 0011 1010 0000** <br><br>
- 🏷️ `PLCP-Header`: <br><br>
    - 48 bits lenght PLCP-Header (PHY-Header), includes fields: `Signal / Rate`, `Service`, `Lenght` & `CRC` <br><br>
        - ⭕ `Signal Rate` (8 bits) :: The Speed / Data Rate at which the PSDU (PMDU) is going to be transmited. Wether this value is, is going to be multiplied by * 100 Kbits/s <br><br>
        - ⭕ `Service` (8 bits) :: Defines High Rate Extensions for HR-DSSS: **0 = Barker Code Coding = 1/2 Mbps** / **1 = CCK Coding = 5.5 Mbps** 
        - ⭕ `Lenght` (16 bits) :: Defines how many microsecods (μs) are requiered to transmit the PSDU (MPDU)  <br><br>
        - ⭕ `CRC (Cyclic Redundancy Check)` (16 bits) :: 16 CRC Frame check to validate the PLCP-Header Information: Signal, Service & Lenght fields

---

### 📡📏🤏 `HR-DSSS` / `802.11b` Short Preamble PPDU:

- 🔁 `Preamble`: <br><br>
    - **72 bits lenght** Preamble **(half lenght VS long preamble because the SYNC is shorter)**, includes fields: `SYNC` & `SFD` <br><br>
        - ⭕ `SYNC` (56 bits) :: Gives the time for the synchronizer (the reciever of the transmission) to synchronize with this. **56 bits scrambled zeros (0s)** <br><br>
        - ⭕ `SFD (Start Frame Delimiter)` (16 bits) :: Inform that the Preamble is ending and it's time to start to send the PLCP-Header using a unique sequence **0000 0101 1100 1111** <br><br>
- 🏷️ `PLCP-Header`: <br><br>
    - 48 bits lenght PLCP-Header (PHY-Header), includes fields: `Signal / Rate`, `Service`, `Lenght` & `CRC` <br><br>
        - ⭕ `Signal Rate` (8 bits) :: The Speed / Data Rate at which the PSDU (PMDU) is going to be transmited. Wether this value is, is going to be multiplied by * 100 Kbits/s <br><br>
        - ⭕ `Service` (8 bits) :: Defines High Rate Extensions for HR-DSSS: **0 = Barker Code Coding = 1/2 Mbps** / **1 = CCK Coding = 5.5 Mbps** 
        - ⭕ `Lenght` (16 bits) :: Defines how many microsecods (μs) are requiered to transmit the PSDU (MPDU)  <br><br>
        - ⭕ `CRC (Cyclic Redundancy Check)` (16 bits) :: 16 CRC Frame check to validate the PLCP-Header Information: Signal, Service & Lenght fields

### PLCP Header & Preamble : 802.11b

- Long = 802.11b - 1mbps min Data Rate
- Short = 802.11b - 2mbps min Data Rate

````py

## PLCP Header & Preamble :: The PPDU is formed by the PSDU + PLCP Header + Preamble (short or long)

PCLP Layer (upper layer 1):

    - Long Preamble PPDU Format:

<-------------------------------------------- PPDU ------------------------------------------->
|-----------------|-----------------||--------------------------------------------------------|
|    Preamble     |   PLCP-Header   ||                        PSDU (MPDU)                     |
|                 |   (PHY Header)  ||     (1 Mbps - DBPSK | 2 Mbps - DQPSK | 5.5 or 11)      |
|-----------------|-----------------||--------------------------------------------------------|
<-------------- 192 μs ------------->
   ||                          || 
   \/                          \/
|--------|--------|          |----------|----------|----------|----------|
|  SYNC  |  SFD   |          |  Singal  |  Service |  Lenght  |   CRC    |
|  (1s)  |        |          |  / Rate  |          |          |          |
|--------|--------|          |----------|----------|----------|----------|
   128       16                   8          8          16         16        <<== 144 bits (Preamble) + 48 bits (PLCP-Header) 
<--- 144 bits --->           <------------ 48 bits @ 1 Mbps ------------->

- Long SFD :   1111 0011 1010 0000
  

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    - Short Preamble PPDU Format:

<-------------------------------------------- PPDU ------------------------------------------->
|-----------------|-----------------||--------------------------------------------------------|
|    Preamble     |   PLCP-Header   ||                        PSDU (MPDU)                     |
|                 |   (PHY Header)  ||           (Variable: 2 Mbps, 5 Mbps or 11 Mbps)        |
|-----------------|-----------------||--------------------------------------------------------|
<--------------- 96 μs ------------->
   ||                          || 
   \/                          \/
|--------|--------|          |----------|----------|----------|----------|
|  SYNC  |  SFD   |          |  Singal  |  Service |  Lenght  |   CRC    |
|  (0s)  |        |          |  / Rate  |          |          |          |
|--------|--------|          |----------|----------|----------|----------|
   56       16                   8          8          16         16        <<== 72 bits (Preamble) + 48 bits (PLCP-Header) 
<---  72 bits --->           <------------ 48 bits @ 2 Mbps ------------->

- Long SFD :   0000 0101 1100 1111

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Note: # The MAC Layer 2 uses the FCS (Frame Check Sequence) for error check validation, while the PHY Layer 1 uses the CRC (Cyclic Redundancy Check).

````

### PLCP Header & Preamble : OFDM 

````py

## PLCP OFDM PPDU (802.11a/g) :: The PPDU is formed by the Data + Sugnal + Training Field (Preamble)

PCLP Layer (upper layer 1):

    - OFDM Preamble PPDU Format:

<-------------------------------------------- PPDU ------------------------------------------->
|-----------------|-----------------||--------------------------------------------------------|
| Training Field  |      Signal     ||                            Data                        |
|   (Preamble)    |                 ||                                                        |
|-----------------|-----------------||--------------------------------------------------------|
<-- 12 Symbols -->
   ||                          || 
   \/                          \/
|--------|--------|          |----------|----------|----------|----------|----------|----------||----------|----------|----------|
|   STF  |   LTF  |          |   Rate   | Reserved |  Lenght  |  Parity  |   Tail   |  Service ||   PSDU   |   Tail   |    Pad   |
|        |        |          |          |          |          |          |      
|--------|--------|          |----------|----------|----------|----------|----------|----------||----------|----------|----------|
    10        2                                                              
  Short      Long            <---------------------------- 24 bits ---------------------------->
 Symbols   Symbols
 


````


## MTU Sizes

- the frame body **lenght** in bytes of an 802.11 `MPDU` is **variable**, however the maximum size of the `MSDU` (payload of a data frame) must be **2304** (plus encryption)

| **Process**                                          | **Size (bytes)**   | **Adds (bytes)**  |
|------------------------------------------------------|--------------------|-------------------|
| **802.11 MPDU lenght**                                      | Variable           | 0                 |
| **Maximum MSDU size** (Before encryption or when a packet is passed from the Network layer to the Data-Link layer for transmission) | 2304               | 0                 |
| **WEP**                                              | 2312               | 8                 |
| **WPA-TKIP**                                          | 2324               | 20                |
| **WPA2-CCMP**                                         | 2320               | 16                |














# OFDM


## MIMO

- SU-MIMO: (single-user MIMO) :: the AP transmits one at a time to each client.
- MU-MIMO: (multi-user MIMO) :: allows the access point to send multiple data packets to multiple clients over the same frequency. allows for multiple client STA’s to communicate with an access point simultaneously. This technology uses different spatial streams on the same RF channel to allow for the simultaneous sessions.





















## Channels & Spectrum

### 2.4 GHz

![image](https://github.com/user-attachments/assets/96b5c4d4-3661-4e7d-a803-2c16e23d9642)

````sh

Channel 01 (First Freq)        = 2.412 GHz
Channel 11 (Last Freq)         = 2.462 GHz

Jump from 1 channel to another = .005

From Channel 01 to Channel 06  = .035
From Channel 06 to Channel 11  = .035
From Channel 01 to Channel 11  = .070

---

Channel 01 : 2.412 GHz

   Channel 02 : 2.417 GHz
   Channel 03 : 2.422 GHz
   Channel 04 : 2.427 GHz
   Channel 05 : 2.432 GHz

Channel 06 : 2.437 GHz

   Channel 07 : 2.442 GHz
   Channel 08 : 2.447 GHz
   Channel 09 : 2.452 GHz
   Channel 10 : 2.457 GHz

Channel 11 : 2.462 GHz

   Channel 12 : 2.467 GHz
   Channel 13 : 2.472 GHz
   Channel 14 : 2.477 GHz

````

### 5 GHz

![image](https://github.com/user-attachments/assets/d7ee7e60-fe4c-4042-b521-3ce9b943e67e)


````

Channel 36  (First Freq)        = 5.180 GHz
Channel 165 (Last Freq)         = 5.825 GHz

Jump from 1 channel to another = .020

From Channel 36 to Channel 165  = .645

---

   # U-NNI-1:

Channel 36  : 5.180 GHz
Channel 40  : 5.200 GHz
Channel 44  : 5.220 GHz
Channel 48  : 5.240 GHz

   # U-NNI-2a:

Channel 52  : 5.260 GHz
Channel 56  : 5.280 GHz
Channel 60  : 5.300 GHz
Channel 64  : 5.320 GHz

   # U-NNI-2c (extended):

Channel 100 : 5.500 GHz
Channel 104 : 5.520 GHz
Channel 108 : 5.540 GHz
Channel 112 : 5.560 GHz
Channel 116 : 5.580 GHz
Channel 120 : 5.600 GHz
Channel 124 : 5.620 GHz
Channel 128 : 5.640 GHz
Channel 132 : 5.660 GHz
Channel 136 : 5.680 GHz
Channel 140 : 5.700 GHz
Channel 144 : 5.720 GHz

   # U-NNI-3:

Channel 149 : 5.745 GHz
Channel 153 : 5.765 GHz
Channel 157 : 5.785 GHz
Channel 161 : 5.805 GHz
Channel 165 : 5.825 GHz


````

## OFDM Subcarriers

### Subcarrier Arrangement in 802.11n/ac 20MHz Channel

![image](https://github.com/user-attachments/assets/73b89035-dc47-4206-8f89-313a5c9a9ad8)

### Subcarrier Arrangement in 802.11n/ac 40MHz Channel

![image](https://github.com/user-attachments/assets/97692cb5-115d-450d-833d-bb61d54773a2)

### Subcarrier Arrangement in 802.11ac 80MHz Channel

![image](https://github.com/user-attachments/assets/14f9ab23-565b-4e79-9264-411880a5f4a7)

### Subcarrier Arrangement in 802.11ac 160MHz Channel 

![image](https://github.com/user-attachments/assets/c8c96917-3045-4e36-95fd-2ae39a9b1e3e)


### 802.11ax OFDMA Subcarriers

https://www.cleartosend.net/802-11ax-ofdma-subcarriers/

- Full:

![image](https://github.com/user-attachments/assets/692a3207-ff6e-45a3-9ef0-c278cd762321)

- Zoom:
  
![image](https://github.com/user-attachments/assets/1af41848-1f31-49ef-9615-3787227669dd)



















## Addresses

- https://excalidraw.com/#room=5e34d48995724e4effe4,bOzzxMz520Zl-6fU124PjA

![image](https://github.com/user-attachments/assets/668f8296-5831-4e62-9ed7-3a94747b2c9f)

- 📍 **To DS** and **From DS** fields are `both 0`: <br> <br>
    - 🛈 The frame is part of an `ad-hoc network` / The frame is `Management` or `Control` frame.
    - 🛈 The frame is **not intended to leave the wireless environment**: `Management` and `Control` frames will always have the To DS and From DS fields set to 0 and are never sent to the distribution system network. (eg. an `Association Response` or `Beacon` will have **To DS** = 0 and **From DS** = 0) <br> <br>
        - `Address 1` = Destination
        - `Address 2` = Source
        - `Address 3` = BSSID <br> <br>
- 📍 **To DS** field is `1` and **From DS** field is `0`: <br> <br>
    - 🛈 The frame **is leaving the wireless environment** and is intended for a computer on the distribution system network.
    - 🛈 For example after a wireless station authenticates it will **need to obtain an IP address and that request will be forwarded by the AP to the DHCP server** that resides on the distribution system network. <br> <br>
        - `Address 1` = BSSID
        - `Address 2` = Source
        - `Address 3` = Destination <br> <br>
- 📍 **To DS** field is `0` and **From DS** field is `1`: <br> <br> 
    - 🛈 The packet **is entering the wireless environment coming from the DS.**
    - 🛈 For example it could be a `Data` frame **coming from the DS to the client STA via the AP.** <br> <br>
        - `Address 1` = Destination
        - `Address 2` = BSSID
        - `Address 3` = Source <br> <br>
- 📍 **To DS** and **From DS** fields are `both 1`: <br> <br>
    - 🛈 The frame is involved with a `wireless distribution system (WDS)` network.
    - 🛈 WDS networks are used to connect multiple networks together, typically for building-to-building connectivity, or a WDS can connect access points together to from a wireless mesh network. <br> <br>
        - `Address 1` = Receiver
        - `Address 2` = Transmitter
        - `Address 3` = Source
        - `Address 4` = Destination

**Important notes on `Addresses`:**

- `Management` frames **use three of the four available address fields** in an 802.11 frame `Addresses 1 to 3`. A management frame is also known as MAC Management Protocol Data Unit (MMPDU) and they do not use the Address 4 field which is only used with a mesh basic service set. <br> <br>
- `Address 4` field is only present in a `mesh network` for infrastructure device communication. <br> <br>
- `Address 4` is the **source address** when both the **To DS** and **From DS** fields are `1`. <br> <br>
- `RTS` frames **uses only two available address fields** in an 802.11 frame `Addresses 1 to 2`. <br> <br>
- `CTS` frames **uses only one address field** in an 802.11 frame `Address 1`. <br> <br>
- `Address 1` is always the `receiver address (RA)`.
- `Address 2` is always the `transmitter address (TA)`. <br> <br>
- If `To DS` and `From DS` are `both set to 0` then the frame can be `Management`, `Control` or `Ad-Hoc` Netowrk


**Each of the four 802.11 Address Fields may have one of 5 different interpretations:**

1. ⭕ `Destination Address` : **`DA`** :: Final Destination of Transmission <br> <br>
    - DA (F0:F0:F0:F0:F0:F0) = `wlan.da == F0:F0:F0:F0:F0:F0` <br> <br>
2. ⭕ `Source Address` : **`SA`** :: Starting Point of the Transmission <br> <br>
    - SA (F0:F0:F0:F0:F0:F0) = `wlan.sa == F0:F0:F0:F0:F0:F0` <br> <br>
3. ⭕ `Receiver Address` : **`RA`** :: Next Wireless Destination of the Transmission <br> <br>
    - RA (F0:F0:F0:F0:F0:F0) = `wlan.ra == F0:F0:F0:F0:F0:F0` <br> <br>
4. ⭕ `Transmitter Address` : **`TA`** :: STA/AP that transmitted the frame onto the WM (Wireless Medium)  <br> <br>
    - TA (F0:F0:F0:F0:F0:F0) = `wlan.ta == F0:F0:F0:F0:F0:F0` <br> <br>
5. ⭕ `Basic Service Set Identifier` : **`BSSID`** :: ID of the BSS (Similar to MAC Address) <br> <br>
    - TA (F0:F0:F0:F0:F0:F0) = `wlan.bssid == F0:F0:F0:F0:F0:F0` <br> <br>

**Filter specific MAC of any hardware address (AP or STA) of any 5 Addresses:**

- ⭕ `Any AP or STA client traffic` : **`WLAN Address`** :: ID of any hardware antenna transmission <br> <br>
    - STA or AP (F0:F0:F0:F0:F0:F0) = `wlan.addr == F0:F0:F0:F0:F0:F0` <br> <br>
- ⭕ `Any AP or STA client traffic` : **`WLAN Address OUI`** :: Filter only for the OUI MAC "F0:F0:F0: _xx:xx:xx_" <br> <br>
    - STA or AP (F0:F0:F0: _xx:xx:xx_) = `  wlan.addr [0:3] == F0:F0:F0`

































# State Machine

## 802.11 State Machine: Authentication & Association

The 802.11 station keeps two variables for tracking the **authentication state** and the **association state**. The states that are tracked are as follows:

1. `Authentication state`: unauthenticated or authenticated
2. `Association state`: unassociated or associated

Together, these two variables create three possible states for the stations.

- `State 1`: initial start state :: unauthenticated and unassociated
- `State 2`: Authentication state :: authenticated and unassociated
- `State 3`: Association state :: and associated _(pending security mechanisms / RSNA)_

**Note:** Because a station must authenticate before it can associate, it can never be unauthenticated and associated. 

Since the introduction of 802.11i security mechanisms, the IEEE 802.11-2012 standard now considers there to a forth state in the connection state machine (State 4: authenticated and associated – PSK or 802.1X security mechanisms completed.):

## ⛔➡️✅ 802.11 State Machine: `4 States`

| **State #**        | **State Name**                 | **Description**                                                  | **Frame Classes**      | **RSNA**                    |
|--------------------|--------------------------------|---------------------------------------------------------------------|------------------------|-----------------------------|
| ⛔ **State 1**     | Unauthenticated, Unassociated |  Client STA NOT Connected                                           | Class 1               | /                           |
| ❓ **State 2**     | `Authenticated`, Unassociated |  Client STA Authenticated to AP _(AP validating STA capabilities)_  | Class 1 & 2           | /                           |
| ✅ **State 3**     | `Authenticated`, `Associated` |  Client STA Associated to AP _(open-auth)_                          | Class 1, 2 & 3        | RSNA: Blocked (Pending RSNA) |
| 🔓 **State 4**     | `Authenticated`, `Associated`   |  Client STA Associated to AP _(RSNA)_                               | Class 1, 2 & 3        | RSNA: Un-Blocked (RSNA OK!)  |

### 🥇🥈🥉 802.11 State Machine: `Frame Classes` `1`, `2`, `3`

**🥇🖽 `Class1 Frames`**

- [**Control**: `RTS & CTS`, `ACK`, `CF-End+CF-Ack & CF-End`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Management**: `Beacon`, `Probe Req/Res`, `Auth/Deauth`, `ATIM`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Data**: `Any frame with ToDS & FromDS false(0)`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)<br><br>

**🥈🖽 `Class2 Frames`

- [**Control**: _None_](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Management**: `Association Req/Res`, `Re-Association Req/Res`. `Disassociation`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Data**: _None_](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)<br><br>

**🥉🖽 `Class3 Frames`

- [**Control**: `PS-Poll`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Management**: `Deauthentication`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Data**: `Any frame with ToDS or FromDS true(1)`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)

**All management frames including the  authentication/association proccess are sent in lowest mandatory data rate supported eg 802.11b 1mbps or 802.11ac 6mbps**

|          **Frame**          	|     **Phase & State**    	|                                                                                                      **Purpose**                                                                                                     	|                                                                                                                         **Key Characteristics**                                                                                                                         	|
|:---------------------------:	|:------------------------:	|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
| **Beacon**                  	| Discovery / State 1      	| Communicates **BSS characteristics** to client STA                                                                                                                                                                   	| Sent by APs during passive scanning. <br>- **Mandatory Fields** : Timestamp, Beacon Interval, Capability Info, SSID, Supported Rates. <br>- **Optional Fields** : Country Code, Transmit Power, QBSS Load Element, HT/VHT Info & Capabilities, RSN Information Element. 	|
| **Probe Request**           	| Discovery / State 1      	| Allows client STA to **actively scan and discover** APs                                                                                                                                                              	| Sends broadcast and directed probes. <br>May request additional information from APs, such as supported capabilities.                                                                                                                                                   	|
| **Probe Response**          	| Discovery / State 1      	| Communicates **BSS characteristics** to client STA & Provides **additional information** to client STA (if requested)                                                                                                	| **Similar to a Beacon frame** but **without a TIM and QoS Capability** fields. <br>Can include additional requested elements from STA in the Probe Request.                                                                                                             	|
| **Authentication Request**  	| Authentication / State 2 	| Initiates authentication process between client STA & AP<br>client STA send basic information about **device type & authentication**                                                                                 	| Validates **device type** & availability to join. <br>Indicates **Open System** or **Shared Key** (legacy WEP) authentication type.                                                                                                                                     	|
| **Authentication Response** 	| Authentication / State 2 	| Confirms or denies authentication request.<br>**if client STA device is compatible it can proceed to association phase.**                                                                                            	| Contains Auth Seq Number (2) and status code: 0 for success, 1 for failure. <br>Matches device type and validates compatibility with AP.                                                                                                                                	|
| **Association Request**     	| Association / State 3    	| Association process allow client STA to: **join** the cell, obtain an **AID**, STA shares its **Listen Interval** & compare client STA & BSS **capabilities**.<br>**Association Request** is used to **advertise to the AP the client STA capabilities** 	| Includes STA’s listen interval, SSID to join, and capabilities <br>(e.g., supported rates, power/channel capabilities, RSN, QoS, HT, VHT). Allows comparison of STA and AP compatibility.                                                                               	|
| **Association Response**    	| Association / State 3    	| Assigns an **AID**, Learn the **Listen Interval** from STA & **Confirms successful association** or denies access if **client STA capabilities** are incompatible                                                                                            	| Verifies fields in the request. If successful, provides an AID and AP parameters. <br>Denies access with a status code (e.g., 1 for rejection) if capabilities are incompatible.                                                                                        	|
















































# Roaming

## FT Fast Transition

### Over the Air:

- Do not use action frame

### Over the DS:

- Use FT Action Frame

























## Random Backoff Values

````py

### Random Backoff Values:

    # There are different Random Backoff Values for each PHY

    # There are also different Random Backoff Values for each QoS categories in EDCA

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# 802.11b can be a Random Backoff Value between 0 and 31 slots
                     
802.11b   = |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| 
            0                                                             31

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# 802.11/g can be a Random Backoff Value between 0 and 15 slots

802.11/g  = |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
            0                             15      

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

````

## Contention Window (CW): total of slots per PHY

| **PHY**      | **Contention Window Min<br>(aCWmin)** | **Contention Window Max<br>(CWmax)** |
|--------------|---------------------------------------|--------------------------------------|
| **802.11b**  | 31                                    | 1023                                 |
| **802.11a**  | 15                                    | 1023                                 |
| **802.11g**  | DSSS(0) = 31<br>OFDM(1) = 15          | 1023                                 |
| **802.11n**  | 15                                    | 1023                                 |
| **802.11ac** | 15                                    | 1023                                 |

## Contention Window (CW): Using QoS EDCA :: AIFS & CW

![image](https://github.com/user-attachments/assets/789900e1-0a3b-4781-ad52-bf420a2550af)

- When an 802.11n station begins the arbitration process after a failed frame transmission = `AIFS`



### Retries and Backoff

````py

## Retries and Backoff

# If there's a retry in the transmission, the CWmax is doubled + 1 for every retry (until it reached the CWmax)

## Example:

    # If a STA chooses a Random Backoff Value of 15 (eg. the largest Value/Number of an OFDM tranmission) and there are retries,
    # it will look like this: 


       CWmin                                                                                                                            CWmax
         0                                                                                                                               1023

         |                                                                                                                                |
Initial  |-| CW = 15                                                                                                                      |
Attempt  |-|                                                                                                                              |
         |                                                                                                                                |
1st      |---| CW = 31                                                                                                                    |
Retry    |---|                                                                                                                            |
         |                                                                                                                                |
2nd      |-------| CW = 63                                                                                                                |
Retry    |-------|                                                                                                                        |
         |                                                                                                                                |
3rd      |---------------| CW = 127                                                                                                       |
Retry    |---------------|                                                                                                                |
         |                                                                                                                                |                    
4th      |-------------------------------| CW = 255                                                                                       |
Retry    |-------------------------------|                                                                                                |
         |                                                                                                                                |
5th      |---------------------------------------------------------------| CW = 511                                                       |
Retry    |---------------------------------------------------------------|                                                                |
         |                                                                                                                                |
6th      |-------------------------------------------------------------------------------------------------------------------------------|| CW = 1023
Retry    |-------------------------------------------------------------------------------------------------------------------------------||
         |                                                                                                                                |
More     |-------------------------------------------------------------------------------------------------------------------------------|| CW = 1023
Retries  |-------------------------------------------------------------------------------------------------------------------------------||
...      |                                                                                                                                |
         |________________________________________________________________________________________________________________________________|


````

## QoS & EDCA

### ⌛📅 All in one IFS table:

| **PHY**                 | **Slot Time**                                                                    | **SIFS**                                                                   | **RIFS**         | **EIFS**                                                                            | **PIFS**                                                       | **DIFS**                                                    | **AIFS**                                  |
|-------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------|
| **Name**                | /                                                                                | Short IFS                                                                  | Reduced IFS      | Extended IFS                                                                        | PCF IFS                                                        | Distributed IFS                                             | Arbitration IFS                           |
| **Uses**                | /                                                                                | Between all frames transmitted within a TxOP                               | Only for 802.11n | Corrupt CRC Frames and Retries                                                      | _PCF_<br>_Unused in 802.11_                                    | Only for Non-QoS<br>Prior to Data or RTS in DCF             | Only for QoS (EDCA)<br>802.11e            |
| **Duration Formula**    | aCCATime <br>+aRxRxTurnAroundTime <br>+aAirPropagation <br>+aMACProcessingDelay  | aRxRFDelay+aRxPLCPDelay <br>+aMACProcessingDelay <br>+aRxTxTurnAroundTime  | RIFS = 2μS       | EIFS (in DCF) = SIFS+DIFS+ACK_Tx_Time<br>EIFS (in EDCA) = SIFS+AIFS[AC]+ACK_Tx_Time | PIFS = SIFS+DIFS+ACK_Tx_Time                                   | DIFS = SIFS + 2x SlotTime<br>_SlotTime depends on each PHY_ | AIFS[AC] = AIFSN[AC]*SlotTime+SIFSTime    |
| **HR/DSSS <br>802.11b** | 20μS                                                                             | 10μS                                                                       | _N/A_            | 364μS <br>(Depends on ACK Time)                                                     | _30μS_                                                         | 50μS                                                        | Variable:<br>Depending Access Method / CW |
| **ERP<br>802.11g**      | Long = 20μS<br>Short = 9μS                                                       | Long = 10μS<br>Short = 10μS                                                | _N/A_            | Long = 364μS<br>Short = 342μS<br>(Depends on ACK Time)                              | _Long = 30μS_<br>_Short = 19μS_                                | Long = 50μS<br>Short = 28μS                                 | Variable:<br>Depending Access Method / CW |
| **OFDM <br>802.11a**    | 9μS                                                                              | 16μS                                                                       | _N/A_            | 94μS <br>(Depends on ACK Time)                                                      | _25μS_                                                         | 34μS                                                        | Variable:<br>Depending Access Method / CW |
| **HT<br>802.11n**       | 2.4GHz Long = 20μS<br>2.4GHz Short = 9μS<br>5GHz = 20μS                          | 2.4GHz = 10μS<br>5GHz = 16μS                                               | 2μS              | 2.4GHz = 342μS<br>5GHz = 94μS                                                       | _2.4GHz Long = 30μS_<br>_2.4GHz Short = 19μS_<br>_5GHz = 25μS_ | 2.4GHz Long = 50μS<br>2.4GHz Short = 28μS<br>5GHz = 34μS    | Variable:<br>Depending Access Method / CW |
| **VHT<br>802.11ac**     | 9μS                                                                              | 16μS                                                                       | _N/A_            | 94μS <br>(Depends on ACK Time)                                                      | _25μS_                                                         | 34μS                                                        | Variable:<br>Depending Access Method / CW |

### TXOP

- 802.11e standard defines default TXOP limit value for each AC, but values can be configured on AP.

**TXOP limit** are set in intervals of `32µs` (microseconds).

- Default TXOP is `47` for `AC_VO` (47×32 = `1504µs`) for OFDM.
- Default TXOP is `94` for `AC_VI` (94×32 = `3008µs`) for OFDM.
- Default TXOP for `AC_BE` & `AC_BK` always TXOP set to `0`. (in other words those traffic category always has to send one frame at at time (no CFB).)

Here is the default settings (AIFSN, CW_min, CW_max, x value, TXOP, AIFS) of those four access categories:

![image](https://github.com/user-attachments/assets/d72fcfdd-9c20-401e-9bf5-50e7e8fb8334)





























# Security




















## Protection Mechanisms

### ERP

- 802.11/802.11b station `associated` to the AP = `NonERP Present`













## Interference

### Retransmission can caused by:

- RF interference	
- Low SNR
- Multipath
- Adjacent cell interference (ACI)
- Co-channel interference (CCI)

### Effects of retransmission:

- Excessive MAC sublayer overhead
- Latency
- Jitter

















# Protocol Analysisis

## 🛜🪤🎣 Frame Capture: `802.11 Frame Capture Devices & Methods`
_Devices and methods for capturing 802.11 WiFi frames can be categorized into three main types. At the end, it mostly depends on the resources and needs_

| **Capture Method**        | **Description**                                                                                                                                               | **Pros**                                                                                       | **Cons**                                                                                          | **Accessibility and Cost**                                                                       | **Examples**                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Mobile Capture**        | Uses mobile devices like laptops with Linux and USB Wi-Fi adapters that support "monitor mode" to capture traffic.                                                                          | Portable and flexible, relatively low cost, no specialized hardware needed                    | Limited range and capacity, requires extensive setup and configuration, potential driver issues  | Most accessible, can be cost-effective, range from simple setups (e.g., Raspberry Pi) to complex systems with high-end computers   | Linux with adapters like Alfa and tools like airmon, macOS internal adapter, devices like Wi-Pi, WiFi Pineapple, Wi-Spy |
| **Infrastructure Capture**| Utilizes professional wireless devices to capture traffic while providing network connectivity. Note that some vendors like Ruckus allow simultaneous capture and network traffic, while others like Cisco may not support this capability. | Scalable, efficient, centralized management, real-time streaming to tools like Wireshark      | High cost due to specialized hardware, complexity in setup and management                        | More expensive due to specialized devices, standalone APs like Ubiquiti or Ruckus Unleashed can be more affordable alternatives   | Ruckus APs and SmartZone, Cisco AirMarshal and APs, Meraki APs |
| **Distributed Capture**   | Employs specialized sensors (e.g., Multi-Sensor Wireless Overlay Systems, WIPS) placed at various points to capture traffic on multiple channels simultaneously.     | Detailed network activity analysis, captures traffic from different locations                 | Very high cost, complex setup and management, requires specialized knowledge and equipment       | Most expensive and complex, requires specialized sensors and systems, less accessible for general use                              | Omnipeek, Cisco Adaptive wIPS, Arista WIPS, Fortinet WIPS |



## 🎛️⚙️ Frame Capture: `Capture Options`
_When capturing network traffic, setting appropriate capture options ensures you collect the most relevant data efficiently. Key capture options include:_

- 🎛️ **`Capture Title`**: Always name your captures with much details as possible like where, when, why (ex. 2024-06-06_13-25hrs_802-11_AP-Room-1_Authentication_iphone-f0-f0-f0-f0-f0-f0_-_01.pcap) <br> <br>
- 🎛️ **`Continious Capture`**: Recycle the capture buffer, which is a temporary buffer where the captured packets are stored. 
 (Buffer becomes a FIFO buffer) (ex. each 10mb of capture the buffer will reset). <br> <br>
- 🎛️ **`Save to Disk`**: Save all packets to disk, specify the name, size and save/stop criteria (ex. Set Title + 512mb file size + Stop After 2048mb captured + Keep Most Recent 3 files + New File every 1 hour) <br> <br>
- 🎛️ **`Packet Slicing`**: Limits the portion of the packet to be captured, used to save disk space or ensure confidentiality. (Warning: Avoid cutting off header information, checksums may become invalid)(ex. Limit each packet to 4500 bytes, this will allow to capture whole beacon frames, but cut large data frames payload that is non critical for analysis) <br> <br>
- 🎛️ **`Capture Buffer`**: The amount of memory allocated to hold packets (ex. Buffer Size = 10mb) <br> <br>
- 🎛️ **`Capture Filter`**: Used to define which packets the sniffer should capture. By setting capture filters, you can limit the captured traffic to only the frames of interest, reducing the amount of data collected and focusing on relevant information. This is not recomended because sometimes you may lose some information. <br> <br>
- 🎛️ **`Dwell Time Capturing`**: The dwell time is the amount of time a wireless network adapter will stay on a specific RF channel before moving the next channel that the device is capable of or is set to scan within the software. A shorter dwell time will capture less information on a specific channel but will allow the device to scan all channels at a quicker rate. <br> <br>
- 🎛️ **`Event Trigger Capturing`**: Event triggers can be set to start and end packet captures based on a specific event. This will allow a protocol analyzer to capture frames that may be helpful in troubleshooting intermittent problems when a specific event happens. Event triggers can be very granular to allow for complex captures to be used with troubleshooting WLAN problems.

## 📻⚙️ Frame Capture: `Channel Capture & Configuration`
_When capturing network traffic, proper channel capture and configuration are essential to collect the relevant data. Capturing on the wrong channel means missing the traffic you need to analyze. Since there are many channels, it's crucial to know which specific channel or channels to target for your troubleshooting needs._

- 📻 **`Fixed Channel`**: Capture in one single channel :: For troubleshooting a particular device that is using a particular channel. Some adapters can be configured even with channel bandwith, primary or secondary channel, etc. (ex. capturing only channel 11 of 2.4 GHz because AP and STA are using that channel) <br> <br>
- 📻 **`Channel Scan`**: Capture the whole picture of the BSA channels and bands :: Select every single channel to do a channel hopping method, some adapters can go from 2.4 GHz to 5 GHz hopping. The tradeoff of this capture technique is that you will miss what is happening in others channels while you are hopping from one channel to another. <br> <br>
- 📻 **`Channel Aggregation (Multiple adapters + Multiple fixed channels)`**: If you have more than 1 adapter you can capture on different channels at same time and you won't miss anything. (ex. with 3 adapters you can capture channel 1, 6 & 11 of 2.4 GHz at same time)

## 🤳🏾🪤📡 802.11 Frame Capture: `Location for Capture`
_In 802.11 Frames Capture is very important the physical location of the adapter that will capture 802.11 Frames depending on what are we tring to capture, it's important to remember that we are capturing on wireless medium (RF flying through the air)_

- 🪤 **`Near the AP`**: Capture that AP sees :: This location is ideal for capturing all the traffic within the Basic Service Area (BSA) and the communications between the Access Point (AP) and its connected clients. It helps in analyzing the overall network performance and the interaction between the AP and multiple clients. Generally, to troubleshoot a channel-wide problem, you will start with a capture near the AP. <br> <br>
- 🪤 **`Near the Client`**: Capture that Client sees :: This setup is useful for diagnosing issues specific to a particular client. By capturing frames from the client's perspective, you can identify problems related to that client’s connection, such as connectivity issues, interference, or performance bottlenecks. <br> <br>
- 🪤 **`In the middle of Client & AP`**: For getting the whole picture of whats happening inside the BSA :: Capture a comprehensive view of the communication. Positioning the adapter between the client and the AP provides a balanced perspective of the entire interaction. This location allows for capturing both the client and AP transmissions, offering a full picture of the communication flow within the BSA.

## 📡🪤🖧 802.11 Frame Catpure: `802.3 Wired Ethernet` + `802.11 Wireless Wi-Fi` at same time
_Capturing and troubleshooting both wired (802.3 Ethernet) and wireless (802.11 Wi-Fi) traffic simultaneously is sometimes necessary. This dual approach provides a complete view of network interactions, especially for complex troubleshooting scenarios._

- 🖧📡 **`EAP over LAN exchanges & RADIUS`**: Simultaneous capture of Wi-Fi and Ethernet is crucial for analyzing authentication exchanges. By capturing both the wireless and wired sides of the network, you can ensure that authentication processes, such as those using EAP and RADIUS, are functioning correctly and efficiently. <br> <br>
- 🖧📡 **`DHCP exchanges`**: Capturing DHCP traffic on both Wi-Fi and Ethernet helps in diagnosing issues related to IP address assignment. It ensures that DHCP requests and responses are correctly handled across both mediums, providing a comprehensive view of the DHCP process. <br> <br>
- 🖧📡 **`QoS`**: Analyzing QoS tags and markings across the entire network, including both wireless and wired segments, is essential for applications like VoIP. This ensures that QoS configurations are consistent throughout the network, maintaining optimal performance and prioritization of critical traffic. It's important when troubleshooting QoS in wireless networks be sure that the QoS is working correctly in wired medium and the whole Distribution System. <br> <br>
- 🖧📡 **`VLAN Tagging`**: Capturing VLAN tags on both Wi-Fi and Ethernet is necessary for verifying correct VLAN VS SSIDs configurations. This helps in ensuring that VLANs are properly propagated and handled across the entire network, facilitating accurate traffic segregation and management. For example when you configure a VLAN for specific SSID. 

## 📦👀📄 Frame Analysis: `Packet Views`
_Understanding network traffic through packet views is crucial for effective analysis. Here are the key packet views used in protocol analyzers._

### 📄👀 General Views:

- Packet List View: This is the main view of a protocol analyzer and shows the columns/list of all the packets captured. (ex. Wireshark has this in the top of a default configuration.) <br> <br>
- Packet Decode View: Very important view in protocol analyzers for packet analysis. It shows a "human read" format organized from lower layers to upper layers bits/bytes information in a "directory style". This contains all the packet information, elements, payloads, radiotap header, PPI, flags, fields names & values (ex. control field), etc. (ex .Wireshark has this in the bottom left of a default configuration.) <br> <br> 
- HEX / Binary / ASCII encoding views: This is the HEX or binary version of the decode view. It shows a "machine read" format of the packet. Wireshark has this in the bottom right of a default configuration.  <br> <br>
- Wireless Views: This is only available in Wireless packet analysis tools and make easier to see information about channel utilization, retries, authenticatins, top channels, top APs, top STAs, etc. 

### 🔎👀 Display, Filter & Profiles Views:

- Display Filter: Used to refine the view of captured data in the Protocol Analyzer. They help isolate specific packets within a capture file based on various criteria, making it easier to focus on the relevant traffic during analysis. This is more recommended than using a capture filter, because you can capture all the data without losing data and then isolate only the packets you want to see. <br> <br>
- Color Filter: highlight specific types of packets in the Wireshark interface. By applying color filters, you can quickly identify different kinds of traffic, making it easier to spot patterns and anomalies during analysis. <br> <br>
- Custom Colors: Custom colors allow you to set specific colors for different types of packets. This customization enhances visual analysis and helps in quickly distinguishing between various traffic types. <br> <br>
- Custom Columns: Enable you to add specific fields to the packet list pane. This feature allows you to display the most relevant information directly in the main view, making it easier to analyze the captured data. <br> <br>
- Custom Profiles: Let you save different configurations of Wireshark settings, including filters, color schemes, and columns. This is useful for switching between different analysis setups quickly and efficiently. For example, you can use a profile to troubleshoot DHCP in ethernet captures and other profile to troubleshooit association in 802.11 Wi-Fi. 

### 📊👀 Advanced Features & Graphic Views:

- 📊 Statistics & Graphics: Some Protocol Analyzers provides various statistical tools and graphical representations to summarize and visualize the captured data. These tools can help identify trends, anomalies, and potential issues in the network traffic. For example, in 802.11 Wi-Fi you can analyze the airtime utilization filter and identify high utilization over the time, the top talking APs, the top talking STAs, etc. <br> <br>
- 📊 Expert Analysis: The automatic detection of network events, errors, and problems by an analyzer. For example: Heuristic-based expert analysis looks for patterns in the traffic flow and compares them to a set of rules configured by default in the analysis software (in wireshark you can see sometimes a colored indicator with "expert" quote, showing some relevant information). <br> <br>
- 📊 Endpoints / Protocol List: This window shows statistics about the endpoints captured. For each supported protocol, a tab is shown in this window. Each tab label shows the number of endpoints captured (e.g., the tab label “Ethernet · 4” tells you that four ethernet endpoints have been captured). If no endpoints of a specific protocol were captured, the tab label will be greyed out (although the related page can still be selected). <br> <br>
- 📊 Node Lists / Conversations: The conversations window is similar to the endpoint Window. Along with addresses, packet counters, and byte counters the conversation window adds four columns: the start time of the conversation (“Rel Start”) or (“Abs Start”), the duration of the conversation in seconds, and the average bits (not bytes) per second in each direction. A timeline graph is also drawn across the “Rel Start” / “Abs Start” and “Duration” columns. <br> <br>
- 📊 Peer Map: A peer map is used to show frame exchanges between stations (STA’s) that are communicating within a WLAN BSS. This can be a valuable visual representation that may be very useful in troubleshooting WLAN problems.

## 📦⏳🎣 Frame Analysis: `Time Metric Columns`
_Various time metric columns provide insights into different aspects of packet timing._

- ⏳ **`Absolute time`** / **`Arrival Time`**: Display the time the packet was captured based on the system clock in the computer, this is the actual capture date and time based on the time zone of the capture device, this means, the time when the packet was captured, provides the real-world time of packet capture for example date and hour. This metric is useful for correlating captured data with real-world events and time-based troubleshooting. <br> <br>
- ⏳ **`Delta time`**: Measures the time difference between two consecutive packets in a capture file. In other words, it is the elapsed time from the previous packet to the current packet. This metric helps in understanding the time intervals between packet transmissions, which can be useful for performance analysis. <br> <br>
- ⏳ **`Relative time`**: This is the time from the first packet in a capture file, but it can be also similar to the Seconds Since Beginning of Capture option. Cumulative time from a selected packet to another selected packet, it can be used to identify how long it takes for a frame exchange to occur. Some protocol analyzer software programs make this a very simple task. This information is valuable in determining problems such as latency or contention with specific frame exchanges. (ex. in a 4-way-handshake you can select the first frame, and then look how many time does the 4th frame took)

























# HT/VHT Operations & Capabilites


### HT Reverse Direction (RD) Protocol

Before the RD protocol, each uni-directional data transfer required the initiating station to capture (and possibly reserve time on) a contention-based RF medium.  With RD, once the transmitting station has obtained a TXOP, it may essentially grant permission to the other station to send information back during its TXOP.

- **Upon receipt of a reverse direction grant (RDG), the receiving station may Transmit data back to the source of the RDG within the current TXOP**



















# Power Management

## Power Management: `Types`
_From the original version in 1997 to now, many features that reduce power consumption have been added to the standard. Some of them have fallen into disuse (PS-Poll), some have been granted certifications (WMM-Power Save) and others relate to specific technologies (MIMO PSPM, 11ac VHT TXOP PS). And there are many other mechanisms related to power-saving that are not discussed in this article (PSMP, TIM Broadcast, Proxy ARP, etc.). Future amendments (802.11ax, 802.11ah) will also introduce new and enhanced power saving techniques._

- **`802.11–1997 prime Power Management`**: 802.11 Power Management (Legacy Power Save Mode)
- **`802.11e-2005 Power Management`**: Wi-Fi Multimedia (WMM) using Automatic Power Save Delivery (APSD) (Scheduled & Unscheduled (S-APSD / U-APSD)). U-APSD is the main Power Save used in 802.11e.
- **`802.11n-2009 Power Management`**: Power Save Multi-Poll (PSMP) & _Spatial Multiplexing Power Save (SMPS)_ 
- **`802.11ac-2013 Power Management`**: VHT TXOP (Transmit Opportunity) Power Save
- **`802.11ax-2019 Power Management`**: Target Wake Time (TWT)

---

### 802.11 Wi-Fi Power Management: `Methods` 

The 5 main methods of power management used in 802.11, the others mentioned before are not used or are very limited for Wi-Fi

1. `Legacy Power Management` 802.11 Power Management (Legacy Power Save Mode)
2. `802.11e-2005 Power Management`: Unscheduled Automatic Power Save Delivery (U-APSD) from 802.11e amendment
3. `802.11n-2009 Power Management`: Power Save Multi-Poll (PSMP) from 802.11n amendment
4. `802.11ac-2013 Power Management`: VHT TXOP (Transmit Opportunity) Power Save  
5. `802.11ax-2019 Power Management`: Target Wake Time (TWT)

### Power Management: `PHY PS types`

| **Standard**  | **Year**   | **Power Saving Modes**                                                                                      |
|---------------|------------|-------------------------------------------------------------------------------------------------------------|
| 802.11 prime  | 1997       | 802.11 Power Save (Legacy Power Save Mode)                                                                  |
| 802.11b/a     | 1999       | Legacy Power Save Mode ;; _can utilize enhancements from 802.11e if driver & hardware support it_           |
| 802.11g       | 2003       | Legacy Power Save Mode ;;  _can utilize enhancements from 802.11e if driver & hardware support it_          |
| _802.11e_       | _2005_   | _Wi-Fi Multimedia (WMM) - Unscheduled Automatic Power Save Delivery (U-APSD)_                               |
| 802.11n       | 2009       | Power Save Multi-Poll (PSMP) & Spatial Multiplexing Power Save (SMPS)                                       |
| 802.11ac      | 2013       | VHT TXOP (Transmit Opportunity) Power Save                                                                  |
| 802.11ax      | 2019       | Target Wake Time (TWT)                                                                                      |

### Power Management: Frames Used

| **Feature**                        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Frame Type**             | **Transmitter**           | **Receiver**            |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|--------------------------|
| **AID (Association Identifier)**   | Enviado por el AP en un frame "Association Response" o "Re-Association Response". Incluye el valor AID en el campo del parámetro AID (16 bits).                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Association Response       | Access Point (AP)         | Station (STA)           |
| **Listen Interval**                | Valor que indica al AP con qué frecuencia una STA en modo Power Save (PS) se despierta para escuchar los beacons. Expresado como un entero entre 0 y 65535 en intervalos de beacon.                                                                                                                                                                                                                                                                                                                                                                                                              | Association Request        | Station (STA)            | Access Point (AP)       |
| **TIM (Traffic Indication Map)**   | Bitmap utilizado para indicar a las STA en estado Power Save que el AP tiene datos almacenados para ellas. Este bitmap se envía periódicamente en los beacons como un elemento de información.                                                                                                                                                                                                                                                                                                                                                                                                | Beacon                     | Access Point (AP)         | Station (STA)           |
| **DTIM (Delivery Traffic Indication Map)** | Elemento de información dentro de un TIM enviado en un frame Beacon. Proporciona información sobre tráfico broadcast/multicast almacenado en el AP, además de los datos unicast típicos presentes en el TIM.                                                                                                                                                                                                                                                                                                                                                                          | Beacon                     | Access Point (AP)         | Station (STA)           |
| **PS-Poll**                        | Frame corto utilizado para solicitar tramas almacenadas en el AP. Contiene el valor AID del cliente y subcampos adicionales como BSSID y direcciones MAC.                                                                                                                                                                                                                                                                                                                                                                                                                                    | PS-Poll                    | Station (STA)            | Access Point (AP)       |
| **Null Data Frame & QoS Null Data Frame** | Frames especiales utilizados para señalizar estados de administración de energía. - **PM bit = 1:** Indica que el dispositivo entra en modo Power Save. - **PM bit = 0:** Indica que el dispositivo está despierto y listo para transmitir/recibir. Los QoS Null Data Frames incluyen campos adicionales para control de calidad de servicio (QoS).                                                                                                                                                                                                                      | Null Data / QoS Null Data  | Station (STA)            | Access Point (AP)       |












































---













1.0 Protocol Analysis – 15%
1.1    Capture 802.11 frames using the appropriate methods


1.1.1                       Select capture devices

Laptop protocol analyzers
APs, controllers, and other management solutions
Specialty devices (hand-held analyzers and custom-built devices)
1.1.2                       Install monitor mode drivers

1.1.3                       Select capture location(s)

1.1.4                       Capture sufficient data for analysis

1.1.5                       Capture all channels or capture on a single channel as needed

1.1.6                       Capture roaming events


1.2    Understand and apply the common capture configuration parameters available in protocol analysis tools


1.2.1                       Save to disk

1.2.2                       Packet slicing

1.2.3                       Event triggers

1.2.4                       Buffer options

1.2.5                       Channels and channel widths

1.2.6                       Capture filters

1.2.7                       Channel scanning and dwell time

 

1.3    Analyze 802.11 frame captures to discover problems and find solutions


1.3.1                       Use appropriate display filters to view relevant frames and packets

1.3.2                       Use colorization to highlight important frames and packets

1.3.3                       Configure and display columns for analysis purposes

1.3.4                       View frame and packet decodes and understand the information shown and apply it to the analysis process

1.3.5                       Use multiple adapters and channel aggregation to view captures from multiple channels

1.3.6                       Implement protocol analyzer decryption procedures

1.3.7                       View and use a capture’s statistical information for analysis

1.3.8                       Use expert mode for analysis

1.3.9                       View and understand peer maps as they relate to communications analysis


1.4    Utilize additional tools that capture 802.11 frames for analysis and troubleshooting


1.4.1                       WLAN scanners and discovery tools

1.4.2                       Protocol capture visualization and analysis tools

1.4.3                       Centralized monitoring, alerting and forensic tools


1.5    Ensure appropriate troubleshooting methods are used with all analysis types


1.5.1                       Define the problem

1.5.2                       Determine the scale of the problem

1.5.3                       Identify probable causes

1.5.4                       Capture and analyze the data

1.5.5                       Observe the problem

1.5.6                       Choose appropriate remediation steps

1.5.7                       Document the problem and resolution

 

2.0 Spectrum Analysis – 10%
2.1    Capture RF spectrum data and understand the common views available in spectrum analyzers


2.1.1                       Install, configure and use spectrum analysis software and hardware

2.1.2                       Capture RF spectrum data using handheld, laptop-based and infrastructure spectrum capture solutions

2.1.3                       Understand and use spectrum analyzer views

Real-time FFT
Waterfall, swept spectrogram, density and historic views
Utilization and duty cycle
Detected devices
WLAN integration views


2.2    Analyze spectrum captures to identify relevant RF information and issues


2.2.1                       RF noise floor in an environment

2.2.2                       Signal-to-Noise Ration (SNR) for a given signal

2.2.3                       Sources of RF interference and their locations

2.2.4                       RF channel utilization

2.2.5                       Non-Wi-Fi transmitters and their impact on WLAN communications

2.2.6                       Overlapping and non-overlapping adjacent channel interference

2.2.7                       Poor performing or faulty radios


2.3    Analyze spectrum captures to identify various device signatures


2.3.1                       Identify various 802.11 PHYs

DSSS
OFDM
OFDMA
Channel widths
Primary channel
2.3.2                       Identify non-802.11 devices based on RF behaviors and signatures

 Frequency hopping devices
 IoT devices
 Microwave ovens
 Video devices
 RF Jammers
 Cordless phones


2.4    Use centralized spectrum analysis solutions


2.4.1                       AP-based spectrum analysis

2.4.2                       Sensor-based spectrum analysis

3.0 PHY Layers and Technologies – 10%
3.1    Understand and describe the functions of the PHY layer and the PHY protocol data units (PPDUs)


3.1.1                       DSSS (Direct Sequence Spread Spectrum)

3.1.2                       HR/DSSS (High Rate/Direct Sequence Spread Spectrum)

3.1.3                       OFDM (Orthogonal Frequency Division Multiplexing)

3.1.4                       ERP (Extended Rate PHY)

3.1.5                       HT (High Throughput)

3.1.6                       VHT (Very High Throughput)

3.1.7                       HE (High Efficiency)


3.2    Apply the understanding of PHY technologies (including PHY headers, preambles, training fields, frame aggregation and data rates) to captured data


3.3    Identify and use PHY information provided in pseudo-headers within protocol analyzers


3.3.1                          Pseudo-header formats

Radiotap
Per Packet Information (PPI)
3.3.2                          Key pseudo-header content

Guard intervals
Resource units allocation
PPDU formats
Signal Strength
Noise
Data rate and MCS index
Length information
Channel center frequency or received channel
Channel properties


3.4    Recognize the limits of protocol analyzers in capturing PHY information including NULL data packets and PHY headers


3.5    Use appropriate capture devices based on an understanding of PHY types


3.5.1                          Supported PHYs

3.5.2                          Supported spatial streams


4.0 MAC Sublayer and Functions – 25%
4.1    Understand frame encapsulation and frame aggregation


4.1.1                       Frame aggregation (A-MSDU and A-MPDU)


4.2    Identify and use MAC information in captured data for analysis


4.2.1                       Management, Control, and Data frames

4.2.2                       MAC frame formats and contents

Frame Control Field
To DS and From DS
Address Fields
Frame Check Sequence (FCS)
4.2.3                       802.11 Management Frame Formats

Information Elements
Authentication
Association and Reassociation
Beacon
Probe Request and Probe Response
4.2.4                       Data and QoS Data Frame Formats

4.2.5                       802.11 Control Frame Formats

Acknowledgement (Ack)
Request to Send/Clear to Send (RTS/CTS)
Block Acknowledgement and related frames
Trigger frames
VHT/HE NDP announcements
Multiuser RTS


4.3    Validate BSS configuration through protocol analysis


4.3.1                       Country code

4.3.2                       Minimum basic rate

4.3.3                       Supported rates and coding schemes

4.3.4                       Beacon interval

4.3.5                       WMM settings

4.3.6                       RSN settings

4.3.7                       HT/VHT/HE operations

4.3.8                       Channel width

4.3.9                       Primary channel

4.3.10                    Hidden or non-broadcast SSIDs


4.4    Identify and analyze CRC error frames and retransmitted frames


5.0 WLAN Medium Access – 10%
5.1    Understand 802.11 contention algorithms in-depth and know how they impact WLANs


5.1.1                       Distributed Coordination Function (DCF)

Carrier Sense (CS) and Energy Detect (ED)
Network Allocation Vector (NAV)
Contention Window (CW) and random backoff
Interframe Spacing
5.1.2                       Enhanced Distributed Channel Access (EDCA)

EDCA Function (EDCAF)
Access Categories and Queues
Arbitration Interframe Space Number (AIFSN)
5.1.3                       Wi-Fi Multimedia (WMM)

WMM parameters
WMM-Power Save
WMM-Admission Control


5.2    Analyze QoS configuration and operations


5.2.1                       Verify QoS parameters in capture files

5.2.2                       Ensure QoS is implemented end-to-end


6.0 802.11 Frame Exchanges – 30%
6.1    Capture, understand, and analyze BSS discovery and joining frame exchanges


6.1.1                       BSS discovery

6.1.2                       802.11 Authentication and Association

6.1.3                       802.1X/EAP exchanges

6.1.4                       Pre-shared key authentication

6.1.5                       Four-way handshake

6.1.6                       Group key exchange

6.1.7                       Simultaneous Authentication of Equals (SAE)

6.1.8                       Opportunistic Wireless Encryption (OWE)

6.1.9                       WPA2 and WPA3

6.1.10                    Fast secure roaming mechanisms

Fast BSS Transition (FT) roaming exchanges
Pre-FT roaming exchanges
6.1.11                    Hotspot 2.0 protocols and operations from the client access perspective (ANQP and initial access)


6.2    Analyze roaming behavior and resolve problems related to roaming


6.2.1                       Sticky clients

6.2.2                       Excessive roaming

6.2.3                       Channel aggregation for roaming analysis


6.3    Analyze data frame exchanges


6.3.1                       Data frames and acknowledgement frames

6.3.2                       RTS/CTS data frame exchanges

6.3.3                       QoS data frame exchanges

6.3.4                       Block Acknowledgement exchanges


6.4    Analyze MIMO and multiuser-specific transmission methods


6.4.1                       MIMO

Transmit Beamforming (TxBF)
MU-MIMO
6.4.2                       OFDMA

Scheduling and trigger frames

6.5    Analyze behavior and resolve problems related to MAC layer operations


6.5.1                       Power Save operations

6.5.2                       Protection mechanisms

6.5.3                       Load balancing

6.5.4                       Band steering
















---


















- https://robinwifi.eu/cwnp/cwap-404-chapter-1-802-11-the-protocol/
- https://robinwifi.eu/category/cwnp/
