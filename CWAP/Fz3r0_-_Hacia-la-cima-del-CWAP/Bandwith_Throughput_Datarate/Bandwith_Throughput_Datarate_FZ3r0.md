














# Data Rate in 802.11 Wi-Fi









|     **Category**     	|                                     **Purpose**                                     	|         **Examples (General)**        	|                                                               **Examples (Per PHY)**                                                              	|          **Configured by Admin?**          	|
|:--------------------:	|:-----------------------------------------------------------------------------------:	|:-------------------------------------:	|:-------------------------------------------------------------------------------------------------------------------------------------------------:	|:------------------------------------------:	|
| **Basic Rates**      	| Ensure all devices can associate and decode management/control frames.              	| 1, 2, 6, 12, 24 Mbps                  	| - 802.11b: 1, 2, 5.5, 11 Mbps<br>- 802.11a/g: 6, 12, 24 Mbps<br>- 802.11n/ac/ax: Configurable, typically fallback to lower OFDM rates like 6 Mbps 	| Yes                                        	|
| **Mandatory Rates**  	| Standard-defined minimum rates required for protocol compliance.                    	| 802.11b 1, 2 Mbps<br>802.11a/g 6 Mbps 	| - 802.11b: 1, 2 Mbps<br>- 802.11a/g: 6, 12, 24 Mbps<br>- 802.11n: None (no specific mandatory rates in the standard)<br>- 802.11ac/ax: None       	| No <br>(Defined by protocol standards)     	|
| **Extended Rates**   	| Enable optional, higher-speed data transfer after association.                      	| 9, 18, 36, 48, 54 Mbps                	| - 802.11b: 5.5, 11 Mbps<br>- 802.11a/g: 9, 18, 36, 48, 54 Mbps<br>- 802.11n: MCS 0–15<br>- 802.11ac: MCS 0–9<br>- 802.11ax: HE-MCS 0–11           	| Yes                                        	|
| **Supported Rates**  	| Advertised rates that the device can use for transmission/reception.                	| Combination of all above rates.       	| - 802.11b: 1, 2, 5.5, 11 Mbps<br>- 802.11a/g: 6–54 Mbps<br>- 802.11n/ac/ax: All MCS rates supported by the device                                 	| No <br>(Device-defined during association) 	|
| **Configured Rates** 	| Administrator-set rates, may exclude lower or legacy rates to optimize performance. 	| Typically 6–54 Mbps                   	| - 802.11b: Can disable 1, 2 Mbps for better performance<br>- 802.11a/g: Often only 12 or 24 Mbps enabled<br>- 802.11n/ac/ax: Custom MCS set       	| Yes                                        	|
