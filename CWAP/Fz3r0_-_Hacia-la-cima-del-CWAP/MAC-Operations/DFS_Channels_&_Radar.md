
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







# 802.11h - `DFS (Dynamic Frequency Selection)`

Dynamic Frequency Selection (DFS) is a channel allocation scheme specified for 802.11 WLANs (Wi-Fi). It was standardized in 2003 as part of IEEE 802.11h.

DFS is all about radar `detection` and `avoidance`. It is designed to prevent electromagnetic interference by avoiding co-channel operation with systems that predated Wi-Fi, such as: 

- Military radar
- Satellite communication
- weather radar

It also to provide on aggregate a near-uniform loading of the spectrum (uniform spreading).

## DFS: `Background Concepts & Terminologies`

Important background concepts and terminologies to understand `DFS`:

| **Concept**                     | **Description**                                                                                                                                                                                                                                  | **Max/Min Time**              |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| **`CAC (Channel Availability Check)`** | The time for which the system must monitor a channel for radar prior to any data being transmitted over the channel.                                                                                                                           | Normal DFS: _(max)_ **60 seconds**<br>Weather DFS: _(max)_ **600 seconds** |
| **`Channel Move Time`**            | The time taken by the system to vacate a channel. It's measured from the end of the radar burst to the end of the data transmission on that channel.                                                                                              | _(max)_ **10 seconds**                |
| **`NOP (Non-Occupancy Period)`**   | The period for which a radar-detected channel should not be used.                                                                                                                                                                               | _(at least)_ **30 minutes**          |
| **`NOL (Non-Occupancy List)`**     | A **list of channels** where the AP has detected radar presence within the last 30 minutes per timer.                                                                                                                                               | **Last 30 minutes**           |
| **`Channel Closing Time`**         | The time in which the AP must **cease data transmission** on the channel.                                                                                                                                                                           | **1 second**                  |
| **`In-Service Monitor`**           | AP monitors the operating channel for the presence of **ISM radar**.                                                                                                                                                                                | **Continuously**              |
| **`Master Device`**                | A device that **can detect** radar. (Typically an **AP**)                                                                                                                                                                                                | **AP**                        |
| **`Client Device`**                | A device that **cannot detect** radar. Instead, it relies on seeing valid data from the master device’s beacon frame.  (Typically a client **STA**)                                                                                                                             | **STA**                       |

## DFS: `5 GHz - UNNI & DFS Channels`

The 5 GHz band is a frequency range used for wireless communication, particularly in 802.11  (Wi-Fi) networks, offering multiple channels designated as **UNII channels (Unlicensed National Information Infrastructure)** for different uses. 

Introduced in the late 1990s and early 2000s, these channels provide wider bandwidth and less interference compared to the congested 2.4 GHz band. 

- However, **certain DFS (Dynamic Frequency Selection) channels within the UNII-2 Extended and UNII-2 bands are subject to radar detection due to their proximity to frequencies used by weather and aviation radars.**

These channels require devices to monitor for radar signals before transmitting to avoid interference, which can disrupt radar operations and compromise safety. The regulations were established to ensure that wireless devices could coexist with these critical radar systems.

![image](https://github.com/user-attachments/assets/b725da15-06a5-4688-ace4-fafe6cee9a15)

| **UNII Band**            | **Channels**                                                                                                                                                     | **Frequency**                | **Bandwidth (MHz)**     | **DFS**             | **Usage**                                |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-------------------------|---------------------|------------------------------------------|
| **UNII-1**               | 36, 40, 44, 48                                                                                                                                                  | 5.150 GHz – 5.250 GHz         | 20/40/80                | No                  | Indoor, no DFS requirements              |
| **UNII-2**               | 52, 56, 60, 64                                                                                                                                                  | 5.250 GHz – 5.350 GHz         | 20/40/80                | Yes                 | Indoor/Outdoor with DFS requirements     |
| **UNII-2 Extended**      | 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144                                                                                                      | 5.470 GHz – 5.725 GHz         | 20/40/80/160            | Yes                 | Indoor/Outdoor with DFS requirements     |
| **UNII-2 Extended:** <br>**DFS Radar Channels**   | 116, **120, 124, 128**, 132                                                                                                                                         | 5.580 GHz – 5.660 GHz         | 20/40/80                | Yes (High interference) | Prone to meteorological radar interference |
| **UNII-3**               | 149, 153, 157, 161, 165                                                                                                                                         | 5.725 GHz – 5.850 GHz         | 20/40/80                | No                  | Outdoor/Indoor, no DFS requirements      |


![image](https://github.com/user-attachments/assets/3d937af5-aeb4-4162-ba1c-96cd57094c90)

![image](https://github.com/user-attachments/assets/59057ed3-8892-4628-a3e9-a35e5d427b58)

![image](https://github.com/user-attachments/assets/9b48da5a-a9f6-40bb-b30d-6203c01cf432)


## DFS: `Radars`

**Radar stands for **RAdio Detection And Ranging**. In the past, the Radars used to operate in frequency ranges where they were the only type of device operating there. **Now that regulatory agencies are opening those frequencies for other uses (like wireless LAN), there is a need for those devices to operate in accordance of the radars.** _(802.11a->DFS)_

There are 2 main types of Radars:

1. `Fixed`: Often **civilian airport** or **military base**, but also **weather radars**
2. `Mobile`: Ships 

### Radars: `Weather Signature` VS `Doppler Radar + Wi-Fi Interference`

The next screenshoot is from a typical weather Doppler Radar signature, it could be rain, snow etc. Meteorological Institutions are using these RADARs to detect atmospheric events in an area. So, for the below image, we can see some rain. This is a regular output for a rainy day(s):

![image](https://github.com/user-attachments/assets/204c1b5e-66ac-41b7-94e3-a4949a15948d)





![image](https://github.com/user-attachments/assets/6d8ebfac-fd1b-4ac8-9e24-b95bbef274a1)

![image](https://github.com/user-attachments/assets/df80aa0d-fdd7-496d-ba59-42cc90eb817f)

![image](https://github.com/user-attachments/assets/26ab851f-c4e1-48eb-8deb-d3ef4e17d06e)


However, RADARs are using very very high gain antennas and they can pick up your very weak WiFi transmission. So, if not DFS rules are used, literally "blinds" the RADAR and it cannot see the atmosphere, it cannot work as expected.

In the next picture some "unnatural straight lines" are seen, that's 802.11 Wi-Fi signal without using DFS rules and "blinding" the RADAR:

![image](https://github.com/user-attachments/assets/288352d5-8e95-44c5-8a14-8ec490c841dc)

![image](https://github.com/user-attachments/assets/738d0c96-dec6-41d4-9deb-dc2f93f04df5)


![image](https://github.com/user-attachments/assets/7c5274bb-66b5-4694-b00e-221b2a2fe5bd)

![image](https://github.com/user-attachments/assets/e5ceb6d6-c752-43a8-ab50-cfc592ccd49f)

![image](https://github.com/user-attachments/assets/a6c4fa0d-bc83-4fe1-aaf0-34e9b0156266)


### Radars: `How Radars and DFS work?`

**Radar typical operation:**

1. Radar measures the distance to the target from the time of arrival of the scattered pulse.
2. When it receives a signal from a device sending a continuous wave (CW), such as telecommunication links, we see a line oriented radially toward the center of the radar image.
3. If the interfering transmitter is near the radar, we see the disturbance in a sector that can be as much as several tens of degrees wide _(eg. Wi-Fi lines or real weather lines in the last pictures)_.


1. A Radar-STA will transmit a set of powerful pulses periodically and observe the reflections.
2. Because the energy reflected back to the radar is much weaker than the original signal, the radar has to transmit a very powerful signal.
3. Also, because the energy reflected back to the radar is very weak, it could confuse it with other radio signals (like a wireless LAN to give an example).

**The general behavior of a device complying with the DFS protocol is:**

1. Being able to **detect** when a radar is occupying the channel
2. **Stop using that occupied channel**.
3. **Monitor** another channel
4. **jump** on it if it is ok. (eg. no radar there as well).

`Important`: The **process for a radio to detect a radar** is a complicated task that **is actually not part of the standard**. Hence, wrong radar detections can occur.

`Note`: _DFS is required for ETSI devices working in the European Union in the ETSI 5ghz band. It can be not mandatory in other parts of the world._

## DFS: Frame Exchange

DFS operations use different ways of exchanging information between STAs. Information can be put in specific elements: 

1. Beacon
2. Probe Response
3. Action Frame (specific frame can also be used to report information) 



## DFS: 5 5ghz spectrum & radars



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
















# TPC 

![image](https://github.com/user-attachments/assets/600e3b64-e693-4305-8181-0a753d162e49)

nowday is used for toher things that interfere with satellites



































# Resources

- https://www.etsi.org/deliver/etsi_en/301800_301899/301893/01.08.01_60/en_301893v010801p.pdf
- https://journals.ametsoc.org/view/journals/bams/97/7/bams-d-15-00048.1.xml
- https://youtu.be/glqLGYaKU3g?si=I2iRcSIuO9ozLV4N
- https://mrncciew.com/2014/10/29/cwap-channel-switch-announcement/
- https://mrncciew.com/2014/10/09/802-11-mgmt-action-frames/
- https://community.cisco.com/t5/wireless-mobility-knowledge-base/tpc-and-dfs-overview/ta-p/3110379
- https://en.wikipedia.org/wiki/IEEE_802.11h-2003
- https://en.wikipedia.org/wiki/Dynamic_frequency_selection
- https://en.wikipedia.org/wiki/Power_control#Transmit_Power_Control
- https://www.youtube.com/watch?v=1x8odxiswz8
- https://oguzhaneren.com/2017/12/08/what-are-the-dfs-channels-and-how-are-they-dealing-with-radar-systems/
- https://www.researchgate.net/profile/Carmine-Massarelli/publication/358307051/figure/fig1/AS:1119418167898112@1643901497400/Weather-radar-principle-of-function-Weather-radar-image-reworked-from-source-7_Q320.jpg
- https://www.element.com/connected-technologies/dynamic-frequency-selection-dfs-testing-certification









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
