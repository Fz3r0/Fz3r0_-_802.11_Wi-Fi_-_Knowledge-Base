
# 🙋🛜🚦MAC Operations: `802.11h` - `DFS` & `TPC`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)  || 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Networking` `Wireless Networking` `IEEE 802.11` `Wi-Fi` `CWNA` `CWAP` `CWNE` `CCNP` `MAC Operations` `DFS` `DFS Protection`

---

<br>

# Index




# `802.11h` - `DFS` & `TPC`


802.11h was meant to bring two main features : `DFS` and `TPC`.

1. `DFS (Dynamic Frequency Selection)`: Based on **Spectrum** management to ensures that channels containing **Radar** are avoided by the **AP** // Energy is spread across the band to reduce interference to **Satellites** 
2. `TPC (Transmit Power Control)`: Ensures that the average power on the 802.11 device (AP/STA) is less than the regulatory domain maximun to reduce interference to satellites. This means that the TPC mechanism "limit the overall RF power/gain of 802.11 devices".

# DFS & TPC: `Background Concepts`

Important background concepts and terminologies to understand before `DFS` and `TPC` topics are:

## Background Concepts: `CAC (Channel Availability Check)`

CAC (Channel Availability Check) is the time for which the system must monitor a channel for radar prior to any data being transmitted over the channel. 

- `Normal DFS channel CAC` = _max:_ **`60 seconds`**
- `Weather DFS channel CAC` = _max:_**`600 seconds`**

## Background Concepts: `Channel Move Time`

The time taken by the system to vacuate a channel, it's measured from the end of the radar burst to the end of the data transmission on that channel. 

- `Channel move time` = _max:_**`10 seconds`**

## Background Concepts: `NOP (Non-Ocupancy Period)`

The period for which a radar detected channel should not be used

-  `NOP (Non-Ocupancy Period)` = _min:_**`30 minutes`**

## Background Concepts: `NOL (Non-Ocupancy List)`

A list of channels, the AP has seen radar presence within 30 minutes per timer. 

-  `NOL (Non-Ocupancy List)` = _within per radar/timer:_**`last 30 minutes`**

## Background Concepts: `Channel Closing Time`

The time in which the AP has to cease data transmission in the channel.

- `Channel Closing Time` = **`1 second`**

## Background Concepts: `In-Service Monitor`

AP monitors the operating channel for the presence of **ISM Radar**

- `In-Service Monitor` = **`Continously`**




The period


# 802.11h - `DFS (Dynamic Frequency Selection)`

Dynamic Frequency Selection (DFS) is a channel allocation scheme specified for 802.11 WLANs (Wi-Fi). It was standardized in 2003 as part of IEEE 802.11h.

DFS is all about radar `detection` and `avoidance`. It is designed to prevent electromagnetic interference by avoiding co-channel operation with systems that predated Wi-Fi, such as: 

- Military radar
- Satellite communication
- weather radar

It also to provide on aggregate a near-uniform loading of the spectrum (uniform spreading).

`Radar` stands for `Radio detection and ranging`. In the past, the radars used to operate in frequency ranges where they were the only type of device operating there. **Now that regulatory agencies are opening those frequencies for other uses (like wireless LAN), there is a need for those devices to operate in accordance of the radars.** _(802.11a->DFS)_

**The general behavior of a device complying with the DFS protocol is:**

1. Being able to **detect** when a radar is occupying the channel
2. **Stop using that occupied channel**.
3. **Monitor** another channel
4. **jump** on it if it is ok. (eg. no radar there as well).

`Important`: The **process for a radio to detect a radar** is a complicated task that **is actually not part of the standard**. Hence, wrong radar detections can occur.

`Note`: _DFS is required for ETSI devices working in the European Union in the ETSI 5ghz band. It can be not mandatory in other parts of the world._

## DFS: Frame Exchange

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

## DFS: 5 5ghz spectrum & radars

![image](https://github.com/user-attachments/assets/b725da15-06a5-4688-ace4-fafe6cee9a15)

## DFS: Radar detection mechanism

When AP starts operation:

1. The AP automatically selects channels with low interference levels in a phase known as `Channel Availability Check (CAC)`.
2. During this phase, the access point is in a passive state scanning for radar signals _(This commonly takes one to two minutes, but could take up to ten minutes)_.
3. hereafter, the access point performs In-Service Monitoring (ISM) to detect active radar signals

If radar is detected by the AP:

1. AP broadcasts a `Action Frame: switch-channel event` to its clients and follows by switching the channel.
1. When the radio detects a radar, it must **stop using the channel** for **30 minutes at least** to protect that service.
2. It then **monitors another channel**
3. AP **start using that channel** **after at least 1 minute if no radar was detected**.

## DFS and 5 GHz band

Because the 2.4Ghz band is free of radar, the DFS rules only apply to the 5.250 ->5.725 Ghz band.

## DFS: Rules

An AP, when moving to a new DFS channel, has to listen silently to the medium for one minute before it is allowed to transmit anything (like a beacon) in order to make sure that  no radar is currently operating on that channel. Clients do not have such a responsibility and are allowed to send wifi frames if an AP is already present and beaconing on the channel, this leaves all the responsibilit

y on the shoulders of the AP. Certain channels like 120,124 and 128 have specific rules where an AP even has to wait 10 minutes before being able to use those channels.

## Examples: 

![image](https://github.com/user-attachments/assets/0eeabed0-02b9-43c0-8099-d7268012f259)




















































# Resources


- https://mrncciew.com/2014/10/29/cwap-channel-switch-announcement/
- https://mrncciew.com/2014/10/09/802-11-mgmt-action-frames/
- https://community.cisco.com/t5/wireless-mobility-knowledge-base/tpc-and-dfs-overview/ta-p/3110379
- https://en.wikipedia.org/wiki/IEEE_802.11h-2003
- https://en.wikipedia.org/wiki/Dynamic_frequency_selection
- https://en.wikipedia.org/wiki/Power_control#Transmit_Power_Control
- https://www.youtube.com/watch?v=1x8odxiswz8









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
