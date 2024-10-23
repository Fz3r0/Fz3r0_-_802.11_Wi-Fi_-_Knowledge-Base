
# 🙋🛜🚦MAC Operations: `802.11h` - `DFS` & `TPC`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)  || 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Networking` `Wireless Networking` `IEEE 802.11` `Wi-Fi` `CWNA` `CWAP` `CWNE` `CCNP` `MAC Operations` `DFS` `DFS Protection`

---

<br>

# Index




# `802.11h` - `DFS` & `TPC`


802.11h was meant to bring two main features : DFS and TPC. DFS, Dynamic Frequency Selection as spectrum management (mainly to co-operate with radars) and TPC, Transmit Power Control, to limit the overall RF “pollution” of wireless devices.



# DFS: Dynamic Frequency Selection

DFS is all about radar detection and avoidance. `Radar` stands for `Radio detection and ranging`. In the past, the radars used to operate in frequency ranges where they were the only type of device operating there. **Now that regulatory agencies are opening those frequencies for other uses (like wireless LAN), there is a need for those devices to operate in accordance of the radars.**

`Note`: _DFS is required for ETSI devices working in the European Union in the ETSI 5ghz band. It can be not mandatory in other parts of the world._

**The general behavior of a device complying with the DFS protocol is:**

1. Being able to **detect** when a radar is occupying the channel
2. **Stop using that occupied channel**.
3. **Monitor** another channel
4. **jump** on it if it is ok. (eg. no radar there as well).

`Important`: The **process for a radio to detect a radar** is a complicated task that **is actually not part of the standard**. Hence, wrong radar detections can occur.

DFS operations use different ways of exchanging information between STAs. Information can be put in specific elements: 

1. beacon
2. probe response but a : the
3. action frame (specific frame can also be used to report information). 

## DFS: `Radars`

There are 2 main types of Radars:

1. fixed (often civilian airport or military base, but also weather radar)
2. mobile (ships). 

### How it works

1. A Radar-STA will transmit a set of powerful pulses periodically and observe the reflections.
2. Because the energy reflected back to the radar is much weaker than the original signal, the radar has to transmit a very powerful signal.
3. Also, because the energy reflected back to the radar is very weak, it could confuse it with other radio signals (like a wireless LAN to give an example).

### DFS in action

1. When the radio detects a radar, it must **stop using the channel** for **30 minutes at least** to protect that service.
2. It then **monitors another channel**
3. AP **start using that channel** **after at least 1 minute if no radar was detected**.

### DFS and 5 GHz band

Because the 2.4Ghz band is free of radar, the DFS rules only apply to the 5.250 ->5.725 Ghz band.





















































# Resources

https://community.cisco.com/t5/wireless-mobility-knowledge-base/tpc-and-dfs-overview/ta-p/3110379










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
