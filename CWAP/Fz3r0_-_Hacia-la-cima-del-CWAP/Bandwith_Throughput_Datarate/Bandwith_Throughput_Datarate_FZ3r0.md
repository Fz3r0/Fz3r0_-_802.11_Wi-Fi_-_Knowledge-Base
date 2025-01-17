









![image](https://github.com/user-attachments/assets/711ec53d-b5c1-4a2b-b222-de98cb0747da)


IMPRTANT: The IEEE-802.11_2020 standard states that an 802.11n Wi-Fi 4 (HT) STA can support 100 Mbps and greater of throughput. Keep in mind that throughput is how much data is actually moving between stations and signaling/data/MCS rate is how much the system is capable of.

# Data Rate in 802.11 Wi-Fi




## 802.11 Data Rate Categories

- **`PHY Frames Data Rates`**: The **PHY header** and **Preamble** are always sent out at the **lowest rate even if that data rate is disabled on the device**. IEEE 802.11ac operates only in the 5 GHz band and the minimum data rate is 6 Mbps for 5 GHz. <br><br>
- **`MAC Frames Data Rates`**: A client STA device **must support ALL Basic/Mandatory date rates** or it will not associate to the AP. eg. If 6 Mbps is configured in the BSS, 802.11b/HR-DSSS/Wi-Fi 1/legacy devices will not associate to the BSS and it will be an **Association error**.


| **Category**                          	| **Purpose**                                                                                                                                                                                                                                                              	| **Examples (General)**                	| **Examples (Per PHY)**                                                                                                                      	| **Configured by Admin?**                  	|
|---------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|---------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------	|-------------------------------------------	|
| **Mandatory Rates**                   	| Standard-defined **minimum rates required** for protocol compliance.<br>**ALL Management Frames** allways are transmitted at **Mandatory/Basic** rates                                                                                                                   	| 802.11b 1, 2 Mbps<br>802.11a/g 6 Mbps 	| - 802.11b: 1, 2 Mbps<br>- 802.11a/g: 6, 12, 24 Mbps<br>- 802.11n/ac/ax: typically fallback to OFDM rates like 6 Mbps                        	| No<br>(Defined by protocol standards)     	|
| **Basic Rates<br>(Mandatory Config)** 	| **Based on Mandatory Rates**, but sometimes 1, 2 , 5.5 & 11 Mbps can be exluded (**OFDM-only data rates**). <br>If **OFDM** & **HR-DSSS** (802.11b) are included, ensure legacy devices can associate and decode management/control frames at data rate efficiency cost. 	| 802.11b 1, 2 Mbps<br>802.11a/g 6 Mbps 	| - 802.11b: 1, 2 Mbps<br>- 802.11a/g: 6, 12, 24 Mbps<br>- 802.11n/ac/ax: typically fallback to OFDM rates like 6 Mbps                        	| Yes                                       	|
| **Extended Rates**                    	| Enable optional, higher-speed data transfer after association.                                                                                                                                                                                                           	| 9, 18, 36, 48, 54 Mbps                	| - 802.11b: 5.5, 11 Mbps<br>- 802.11a/g: 9, 18, 36, 48, 54 Mbps<br>- 802.11n: MCS 0–15<br>- 802.11ac: MCS 0–9<br>- 802.11ax: HE-MCS 0–11     	| Yes                                       	|
| **Supported Rates**                   	| Advertised rates that the device can use for transmission/reception of **Data Frames** or **QoS Data Frames**.                                                                                                                                                           	| Combination of all above rates.       	| - 802.11b: 1, 2, 5.5, 11 Mbps<br>- 802.11a/g: 6–54 Mbps<br>- 802.11n/ac/ax: All MCS rates supported by the device                           	| No<br>(Device-defined during association) 	|
| **Configured Rates**                  	| Administrator-set rates, may exclude lower or legacy rates to optimize performance.<br>Admin can configure **Basic Rates** (based on mandatory rates) & **Extended Rates**                                                                                               	| Typically 6–54 Mbps                   	| - 802.11b: Can disable 1, 2 Mbps for better performance<br>- 802.11a/g: Often only 12 or 24 Mbps enabled<br>- 802.11n/ac/ax: Custom MCS set 	| Yes                                       	|




### Basic Rates:

These rates are used for `Management frames` and `Control frames`, such as `beacons` and `probe responses`. 

- **SO, IF THE CLIENT STA DOESN'T SUPPORT THE REQUIRED BASIC RATES (E.G., 802.11b IN "`OFDM ONLY - (802.1b exclude)`" MODE WITH `6/12/24 MBPS DATA RATES`), IT WILL NOT BE ABLE TO AUTHENTICATE TO THE BSS. (BECAUSE 802.11b ONLY SUPPORTS `1, 2, 5.5, 11 MBPS DATA RATES`**

Example:

- In an 802.11g (ERP-OFDM) network, the administrator might configure **6 Mbps** as a **Basic Rate** to ensure all devices can receive critical frames and having the best performance possible. _(this configuration is also known as **"OFDM Only"** because only supports 6, 12, 24 Mbps; excluding 802.11b HR-DSSS data rates of 1, 2, 5.5, 11 Mbps)_.

#### Basic rates `Layer 1 PHY (PHY Preamble & PHY Header)` & `Layer 2 MAC (MAC Frames)`:

- The **PHY header and Preamble are always sent out at the lowest rate possible**, **even if that data rate is disabled on the device)**.

Example: 

- IEEE 802.11ac operates only in the 5 GHz band and the minimum data rate is **6 Mbps** for **5 GHz**.
- If the administrator manually set the **Supported Rates** to **24mbps**: <br><br>
    - The **PHY Preamble & Header** will be transmitted at **`6mbps` (minimum data rate)**
    - The **MAC Frames** like Management and Control will be transmitted at **`24mbps` (supported data rate)**


### Mandatory Rates:

Devices must support these rates for compliance with their respective PHY standards.

- Example: 802.11b requires 1 and 2 Mbps; without these, devices cannot claim 802.11b compliance.

### Extended Rates:

Optional, higher data rates allow for better throughput if both the AP and the client device support them.

- Example: In 802.11g, rates like 36 and 54 Mbps are extended and used only when compatible devices negotiate them.
Supported Rates:

This is the full list of rates a device advertises during association, including both basic and extended rates.
Example: A modern 802.11ax device might support rates from 6 Mbps to HE-MCS 11, though the AP may limit which rates are allowed.
Configured Rates:

Administrators can adjust rates to balance backward compatibility and performance.
Example: On a network primarily used by 802.11n clients, the admin might disable 1 and 2 Mbps to avoid legacy devices and reduce airtime overhead.


## Basic Rates

### Understanding Basic Rates and Compatibility

- In 802.11 WLANs, basic rates are data rates that are mandatory for all devices in the network to support. 
- When a device attempts to associate with an AP (Access Point), it must confirm that it can handle all the basic rates configured on that AP. If it cannot, the device will fail to associate.

802.11 standards specify different data rates based on the supported protocols and frequency bands. Here’s a breakdown of common basic rates:











#

- 802.11n HT Wi-Fi 4 station can support 100 Mbps 






# Resources

- https://www.netally.com/wifi-solutions/differences-between-wi-fi-throughput-bandwidth-and-data-rates/
- https://www.rcti.com.mx/index.php/blog/item/41-data-rate
