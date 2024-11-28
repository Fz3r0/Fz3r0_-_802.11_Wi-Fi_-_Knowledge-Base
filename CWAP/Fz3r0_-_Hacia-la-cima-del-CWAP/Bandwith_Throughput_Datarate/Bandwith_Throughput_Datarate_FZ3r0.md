









![image](https://github.com/user-attachments/assets/711ec53d-b5c1-4a2b-b222-de98cb0747da)





# Data Rate in 802.11 Wi-Fi




## 802.11 Data Rate Categories


|     **Category**     	|                                     **Purpose**                                     	|         **Examples (General)**        	|                                                               **Examples (Per PHY)**                                                              	|          **Configured by Admin?**          	|
|:--------------------:	|:-----------------------------------------------------------------------------------:	|:-------------------------------------:	|:-------------------------------------------------------------------------------------------------------------------------------------------------:	|:------------------------------------------:	|
| **Basic Rates**      	| Ensure all devices can associate and decode management/control frames.              	| 1, 2, 6, 12, 24 Mbps                  	| - 802.11b: 1, 2, 5.5, 11 Mbps<br>- 802.11a/g: 6, 12, 24 Mbps<br>- 802.11n/ac/ax: Configurable, typically fallback to lower OFDM rates like 6 Mbps 	| Yes                                        	|
| **Mandatory Rates**  	| Standard-defined minimum rates required for protocol compliance.                    	| 802.11b 1, 2 Mbps<br>802.11a/g 6 Mbps 	| - 802.11b: 1, 2 Mbps<br>- 802.11a/g: 6, 12, 24 Mbps<br>- 802.11n: None (no specific mandatory rates in the standard)<br>- 802.11ac/ax: None       	| No <br>(Defined by protocol standards)     	|
| **Extended Rates**   	| Enable optional, higher-speed data transfer after association.                      	| 9, 18, 36, 48, 54 Mbps                	| - 802.11b: 5.5, 11 Mbps<br>- 802.11a/g: 9, 18, 36, 48, 54 Mbps<br>- 802.11n: MCS 0–15<br>- 802.11ac: MCS 0–9<br>- 802.11ax: HE-MCS 0–11           	| Yes                                        	|
| **Supported Rates**  	| Advertised rates that the device can use for transmission/reception.                	| Combination of all above rates.       	| - 802.11b: 1, 2, 5.5, 11 Mbps<br>- 802.11a/g: 6–54 Mbps<br>- 802.11n/ac/ax: All MCS rates supported by the device                                 	| No <br>(Device-defined during association) 	|
| **Configured Rates** 	| Administrator-set rates, may exclude lower or legacy rates to optimize performance. 	| Typically 6–54 Mbps                   	| - 802.11b: Can disable 1, 2 Mbps for better performance<br>- 802.11a/g: Often only 12 or 24 Mbps enabled<br>- 802.11n/ac/ax: Custom MCS set       	| Yes                                        	|


### Basic Rates:

These rates are used for `Management frames` and `Control frames`, such as `beacons` and `probe responses`. 

- **SO, IF THE CLIENT STA DOESN'T SUPPORT THE REQUIRED BASIC RATES (E.G., 802.11b IN "`OFDM ONLY - (802.1b exclude)`" MODE WITH `6/12/24 MBPS DATA RATES`), IT WILL NOT BE ABLE TO AUTHENTICATE TO THE BSS. (BECAUSE 802.11b ONLY SUPPORTS `1, 2, 5.5, 11 MBPS DATA RATES`**



- Example: In an 802.11g network, the admin might configure 6 Mbps as a basic rate to ensure all devices can receive critical frames.

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
