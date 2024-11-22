
# 📡🛜🎯802.11n features - `Transmit Beamforming`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Networking` `Wireless Networking` `IEEE 802.11` `Wi-Fi` `CWNA` `CWAP` `CWNE` `CCNP` `Beamforming` `Transmit Beamforming` `Implicit Beamforming` `Explicit Beamforming` `Beamformee` `Beamformer`

---

<br>

# Index















# Transmit Beamforming (TxBF)

Transmit Beamforming (TxBF) is a wireless signal enhancement technique introduced as an optional feature in 802.11n and later standardized in 802.11ac/ax. 

802.11ac enables single user (SU) and multi user (MU) beamforming which aims to improve SNR (and hence throughput) between a wireless client and AP.  

Some WLAN vendors implement Transmit Beamforming (TxBF) in different proprietary ways.

### 802.11n: `Transmit Beamforming (TxBF)`

Transmit Beamforming (TxBF) got introduced as an optional feature of the 802.11n amendment. It uses multiple antennas to focus and direct the transmission toward a specific client, improving signal strength, range, and reliability. However, for TxBF to work, the client device must support Transmit Channel Feedback (TxCBF) to provide feedback to the access point. This dependency limits its effectiveness in environments with legacy or non-compliant devices.

### Cisco: `Client Link`

While beamforming (TxBF) is effective, it has limitations tied to client-side capabilities. Cisco ClientLink is a more versatile solution because it doesn’t depend on client support and works across all device types, ensuring better overall network performance, especially in mixed environments with legacy devices.

### Ruckus: `Beamflex`

Beamforming in 802.11ac is a radio based technology. Whereas BeamFlex engages adaptive antennas so this is an antenna based technology.

What Ruckus does is use beamforming (which is radio based) and combines it with adaptive antennas (BeamFlex which antenna based) to maximize the performance.





## Transmit Beamforming (TxBF) Methods: `Explicit` & `Implicit`



which has two methods `Implicit` and `Explicit` beamforming.


As you may know beamforming was introduced,  (i.e. Cisco ClientLink)


















Can be used when there are more transmitting antennas than there are spatial data streams.
A digital signal processing technology on the transmitting device that duplicates the transmitted signal on more than one antenna to optimize a combined signal at the client.
Carefully controlling the phase of the signals transmitted from multiple antennas has the effect of improving gain, thus emulating a higher-gain unidirectional antenna.
Is adjusting the phase of the transmissions.
Result in greater range for individual clients communicating with an access point.
When utilizing transmit beamforming the transmitter will not be sending multiple unique spatial streams but will instead be sending multiple streams of the same data with the phase adjusted for each RF signal.
Types of transmit beamforming:

Implicit TxBF: Uses an implicit channel-sounding process to optimize the phase differentials between the transmit chains.
Explicit TxBF: Requires feedback from the stations in order to determine the amount of phase-shift required for each signal.
The 802.11n amendment defined transmit beamforming:

Optional PHY capability
Can use Implicit TxBF or Explicit TxBF 
The 802.11ac amendment defined transmit beamforming:

Uses Explicit TxBF
requiring the use of channel measurement frames
both the transmitter and the receiver must support beamforming.

## 

## VHT/HE NDP Announcement

- Null data packet (NDP) announcement frames **notify the recipient that an NDP will follow**.

The figure below shows the frame exchange process. The beamformer (AP) will request that the station send an NDP sounding frame by setting the training request (TRQ) value in the Link Adaption Control subfield of the HT Control Field. The information gathered from the sounding frame can be used to calculate a steering matrix for the purpose of using beamforming for future transmissions to the same station.


### NDP Announcement Frame Exchange:

![image](https://github.com/user-attachments/assets/2afe6b10-9a8f-4c9e-928a-a9c07a8ff589)

### NDP Announcement Frame Format:

![image](https://github.com/user-attachments/assets/320d9c8d-d3e6-43cf-9e0a-45c903814c69)


### Link Adaption Control Subfield Format:

![image](https://github.com/user-attachments/assets/db71346c-aade-4a1f-97e5-31bc5f9f4763)


### Announcement Frame:

![image](https://github.com/user-attachments/assets/16b2bb09-f5ff-47ae-ae99-f9b35286e11b)


# Key concepts

- When looking at an 802.11n packet decode in a protocol analyzer, you notice the NDP Announcement subfield set: An **NDP will follow the current frame but will not be seen by a protocol analyzer.**
- During a VHT Transmit Beamforming sounding exchange, the beamformee transmits a Compressed Beamforming frame to the beamformer: **Feedback Matrix is communicated within this Compressed Beamforming frame**



# Resources

- https://revolutionwifi.blogspot.com/2010/07/beamforming-clientlink-and.html
- https://wificoops.com/2018/01/14/beam-me-up-scotty/
- https://community.fs.com/blog/beamforming.html
- https://dot11ap.wordpress.com/cwna/radio-frequency-rf-technologies/transmit-beam-forming-txbf-as-defined-in-the-802-11-standard/
- https://www.wirelessnewbies.com/post/transmit-beamforming
- https://howiwifi.com/2020/07/13/802-11-frame-types-and-formats/
- https://www.oreilly.com/library/view/80211ac-a-survival/9781449357702/ch04.html
- https://www.mathworks.com/help/wlan/ug/802-11ac-transmit-beamforming.html
- https://www.commscope.com/globalassets/digizuite/923965-ruckus-beamflex-pa-115628-en.pdf
- https://www.cisco.com/c/en/us/td/docs/wireless/technology/5760_deploy/CT5760_Controller_Deployment_Guide/Mobility_Design_and_Configuration.pdf



























In


<p align="center"> <img src="https://github.com/user-attachments/assets/807020b5-82bd-4313-8213-99a4a646f226" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/288352d5-8e95-44c5-8a14-8ec490c841dc" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/a6c4fa0d-bc83-4fe1-aaf0-34e9b0156266" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/738d0c96-dec6-41d4-9deb-dc2f93f04df5" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/e5ceb6d6-c752-43a8-ab50-cfc592ccd49f" width="300" height="300">
<img src="https://github.com/user-attachments/assets/bbe05510-5d98-4fcb-ba25-a5110ccf78da" width="300" height="300"> </p>






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


