# Hotspot 2.0 (Passpoint)

- Hotspot 2.0 (also known as Passpoint®, the trademarked name of the Wi-Fi Alliance solution) aims to improve the experience of mobile users when selecting and joining a Wi-Fi hotspot by providing information to the station prior to association.
- Hotspot 2.0 is focused on enabling a mobile device to automatically discover APs that have a roaming arrangement with the user’s home network (or cellular carrier service) and then securely connect.
- Hotspot 2.0 can be leveraged to set up a guest hotspot service, offering public access to users through its Wi-Fi networks. It streamlines the process of accessing Wi-Fi networks by a variety of devices that have Wi-Fi capabilities, such as APs, smartphones, and so on.
- Hotspot 2.0 networks are created by Wi-Fi operators and identity providers.
- A Wi-Fi operator deploys and operates an access network of publicly accessible or guest access APs.
- An Identity Provider provides network services and operates the AAA infrastructure required to authenticate subscribers.
- The Wi-Fi Operator and Identity Provider may be the same or different entities.
- The Service Providers (SPs) that can be accessed at a hotspot are referred to as the roaming partners for that hotspot.
- The Identity Provider performing the authentication can provide its subscribers with AAA connectivity to its network through the hotspot.
- Identity Providers are advertised using 3GPP cellular network information, an NAI realm list, or a roaming consortium list.
- There can be one or more identity providers per Hotspot 2.0 access network.
- Wi-Fi roaming would apply anytime a mobile device does not see an AP belonging to its home network provider.
- A user could roam on a Wi-Fi network that is across town or on the other side of the world.
- Roaming partners can include MSOs, MNOs, wireline operators, public venues, enterprises, and basically any other entity that has Wi-Fi assets.
- Roaming can be accomplished with dual mode devices (smartphones) or Wi-Fi-only devices like tablets and laptops.

Hotspot 2.0 networks offer accessibility and mobility, enabling internet access in public areas with secure authentication and roaming capabilities, ensuring safe access and connectivity.

- **With Hotspot 2.0, the client device is equipped by an authentication provider with one or more credentials, such as a SIM card, username/password pair, or X.509 certificate. The device can then query Hotspot 2.0 capable APs to see if it belongs to a visited network that supports roaming with the devices home network.**

Hotspot 2.0 is a program of the Wi-Fi Alliance, and is supported by the Passpoint(™) certification program which ensures APs and client devices comply with the technical specifications. Hotspot 2.0 capabilities are emerging in a series of releases:

1. Hotspot 1.0 came out in June 2012 and was focused on automating network discovery/selection, authentication, and over-the-air security. Other releases will follow in the coming years that will add additional capabilities.
2. Mobile devices with Hotspot 2.0 support are now available in the market. While vendors may choose to introduce new models to enable Hotspot 2.0, these capabilities can be added via software updates in most cases.

"The hassles and risks of connecting to public Wi-Fi will soon be a thing of the past, thanks to Hotspot 2.0."

## Hotspot 2.0 benefits:

- Automates the connection experience at hotspots, providing a secure encrypted airlink for public Wi-Fi networks
- Supports multiple roaming partners over a single SSID

## Hotspot 2.0 Release 1

- Release 1 is focused squarely on over-the-air security and network discovery and selection.
- The key enabling protocols are IEEE 802.11u, along with IEEE 802.1X, selected EAP methods, and IEEE 802.11i. The latter three are part of the WPA2- Enterprise certification program in the Wi-Fi Alliance, and are standard on all smartphones. While the certification is called "WPA2-Enterprise", the end result is a process that is every bit as secure and easy to use as what exists in the cellular world.
- The IEEE 802.11u protocol enables a mobile device to have a dialog with a Wi-Fi AP "pre-association" to determine the capabilities that the network can support.

The two protocols that 802.11u uses to make this happen are:

1. the generic advertisement service (GAS)
2. the access network query protocol (ANQP). 

hese protocols run on top of 802.11 and enable the Hotspot 2.0 experience

![image](https://github.com/user-attachments/assets/69318ac2-bad7-4a1a-a05c-52a96fd08786)


# Resources

- https://www.netwifistore.com/HotSpot-2-0.asp
- https://www.arubanetworks.com/techdocs/ArubaOS_80_Web_Help/Content/ArubaFrameStyles/hotspot/predepoyment_overview.htm
- https://docs.cloud.ruckuswireless.com/ruckusone/userguide/GUID-DD35201E-111A-41D7-B5E8-70AC6F8B00F8.html
- https://www.netwifistore.com/HotSpot-2-0.asp
- https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-1/config-guide/b_wl_17_11_cg/hotspot2.pdf
- https://www.ironwifi.com/help/ruckus-wireless-lan-controller-passpoint-configuration
- https://support.alcadis.nl/Support_files/Ruckus/SmartZone//Manuals/SmartZone%206.0.x/Smartzone%206.0.0.0.1331/SmartZone-6.0.0-Hotspot2.0-Guide-RevA-20210406.pdf
- https://higherlogicdownload.s3.amazonaws.com/HPE/MigratedAttachments/63AF17E3-09CD-4369-A476-CD91D4FA888B-1-WP_PasspointWiFi_062912.pdf
