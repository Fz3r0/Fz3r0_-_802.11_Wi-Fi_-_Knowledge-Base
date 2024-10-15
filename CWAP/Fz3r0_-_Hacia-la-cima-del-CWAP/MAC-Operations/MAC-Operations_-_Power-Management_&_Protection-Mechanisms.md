# 🛜🔋🛑 MAC Operations: `Power Management` & `Protection Mechanisms`

There are 2 types of MAC Operations: **Power Management** & **Protection Mechanisms**:

1. **`Power Management`** is allow the radio to go to sleep (just few microseconds), because if the antenna/adapter keeps awake all the time is consuming battery all the time, in a movile device can degrade battery life. Power management it's just turning on the antenna, send/recieve the frame, then "doze" or "sleep" the antenna and so on. The hint here is, that the STA does not lose any frame even if it's sleeping <br><br>
2. **`Protection Mechanisms`** allow newer devices to communicate and "exist" in a world where older devices also exists (eg. devices using 802.11b(HR-DSSS) can coexist with newer devices using 802.11g(ERP) or even newest devices like 802.11n/ac/ax(OFDM)).

# 🔋🛜🪫 MAC Operations: `Power Management`

Many mechanisms that are described in the IEEE 802.11 standard allow a wireless device to reduce its power consumption, to turn off its radios and to wake up at the correct time to retrieve its traffic. 

While the APs are generally connected to an external power source, the wireless clients are often running on batteries. The purpose of power saving features is to increase the battery life and to allow longer performance. This battery life extension can be significant for low-powered devices such as smartphones, Voice over IP phones or handheld barcodes scanners.

## 🔋⚙️🔀 Power Management: `Modes`

A client STA can be in one of two Power Management modes:

- ⭕🐓 **`Active mode`**: the client is awake all the time. The AP immediately transmits the frames to the client. <br> <br>
- ⭕💤 **`Power Save (PS) mode`**: the client is mostly in doze power state, but can also be awake to transmit and receive now and then. In this mode, the AP buffers the eligible frames destined for the client.

⚠️ **`IMPORTANT`**: Nowdays most wireless devices (eg. smartphones, tablets, computers, etc) by default use `Power Save (PS) mode` to increase the battery life.

## 🔋🐓💤 Power States

A wireless client STA enters **Power Save (PS) mode** in which the radio power state can transition **between awake and doze** according to the 802.11 power management rules. 

**A radio STA can be in one of two Power states:**

- 💤 **Doze/Asleep State:** The client STA cannot receive or transmit any frames and operates in a very low power state to conserve power. STA is allowed to go to "Doze" state after an AP has been notified that station is about to enter Power Save (PS) mode. STA will use `Null Data Frame` or `QoS Null Data Frame` with bit `Power Management / Power Save Mode = 1` to inform the AP that it will going to "Doze" state. In this state, the station significantly reduces its power consumption by not actively listening for data, only waking up periodically to check for new packets from the AP. <br><br> 
- 🐓 **Iddle/Awake State:** The client STA radio is constantly powered and able to receive and transmit. Does not necessarily imply power saving, as a station can be in an idle/awake state while still actively listening for data. <br><br>
- 📡 **Receive & Transmit states**: station is actively sending or receiving data when in these states.

**STA will go from `Doze` to `Awake` state for one of two reasons:** 

1. If STA have a frame to send.
2. Based on the STA internal timing mechanism. <br> <br>

## 🔋⚡🪫 Power Consumption Activities

When a STA is capable of Power Save Mode, a wireless radio can perform one of 4 activities, better known as **"Power State"**.

Power consumed by each activity increases in the given order (1-4). In power save mode, the client STA would set the power management flag to `1` to indicate it might go into the **Doze state to save power**, otherwise the client STA would set the power management flag to `0` to indicate that the station is **NOT in power save mode.**

1. ➖`⚡󠀠󠀠󠀠󠀠󠀠󠁪󠁪󠁪󠁪󠁪󠀵󠀵🔘🔘🔘`➕ | `Power Management = 1` :: State: **Asleep / Doze**
2. ➖`⚡⚡🔘🔘`➕ | `Power Management = 0` :: State: **Awake / Iddle** 
3. ➖`⚡⚡⚡🔘`➕ | `Power Management = 0` :: State: **Receiving** 
4. ➖`⚡⚡⚡⚡`➕ | `Power Management = 0` :: State: **Transmitting** 

## 📬⚡📪 Power Management Flag:

- 📬💤 **`Power Management = 1`**: Indicates the STA device is entering **Power Save (PS) mode** also known as **"Doze"** state, meaning it can transition into a low-power state where it is not actively transmitting or receiving data, **only waking up periodically to check for new information**. <br><br>
- 📪🐓 **`Power Management = 0`**: Indicates to the AP that the STA device is ready to Tx/Rx and is entering to any other of the power save states, eg. **Awake/Iddle**, **Receiving**, **Transmitting**. 

## 🚫💾📦 `Null Data Frame` & `QoS Null Data Frame`

**Null Data Frame** VS **QoS Null Data Frame**:

- ⭕ Null Data Frames are special Wi-Fi frames that contain no data payload. They are primarily used for signaling purposes, particularly in Power Save mode. A device sends a Null Data Frame to inform the access point (AP) about its power management status. <br><br>
- ⭕ QoS Null Data Frames are similar to standard Null Data Frames but **include additional fields for Quality of Service (QoS) control**, which helps manage the prioritization of traffic in the network. <br><br>

### 🦈 Wireshark Filters: `Power Management` > `Null Data Frame` & `QoS Null Data Frame`

| **Field**                                   | **Description**                                         | **Wireshark Filter**                              |
|---------------------------------------------|---------------------------------------------------------|---------------------------------------------------|
| **⭕ Null Data Frame**                       | Identifies a Null Data Frame                            | `wlan.fc.type_subtype == 36`                        |
| **💤 Null Data Frame & PM = 1**             | Null Data Frame with Power Save mode (Doze)                   | `wlan.fc.type_subtype == 36 && wlan.fc.pwrmgt == 1` |
| **🐓 Null Data Frame & PM = 0**             | Null Data Frame with Awake mode                         | `wlan.fc.type_subtype == 36 && wlan.fc.pwrmgt == 0` |
| **⭕ QoS Null Data Frame**                   | Identifies a QoS Null Data Frame                        | `wlan.fc.type_subtype == 44`                        |
| **💤 QoS Null Data Frame & PM = 1**         | QoS Null Data Frame with Power Save mode (Doze)               | `wlan.fc.type_subtype == 44 && wlan.fc.pwrmgt == 1` |
| **🐓 QoS Null Data Frame & PM = 0**         | QoS Null Data Frame with Awake mode                     | `wlan.fc.type_subtype == 44 && wlan.fc.pwrmgt == 0` |
| **⭕ QoS Data Frame or QoS Null Data Frame** | Either QoS Data Frame or QoS Null Data Frame            | `wlan.fc.type_subtype == 36`                       |
| **💤 Null or QoS Null Data Frame & PM = 1** | Either Null Data or QoS Null Data Frame with PS mode (Doze)    | `wlan.fc.type_subtype == 36`                       |
| **🐓 Null or QoS Null Data Frame & PM = 0** | Either Null Data or QoS Null Data Frame with Awake mode | `wlan.fc.type_subtype == 36`                       |
  
## 🪪🆔🤳 PS Field: `AID (Association Identifier)`

AID is a unique number which identifies a particular Association between an AP (Access Point) and a STA (wireless Station).

Every 802.11 Power Management Method starts begin with the client STA associates to the BSS. When AP sends "Association Response" or "Re-Association Response" frame to the STA, an `AID` value is present in the AID parameter field (16-bit).

### 🦈 Wireshark Filters: `AID (Association Identifier)`

| **Field**                          | **Description**                                                  | **Wireshark Filter** |
|------------------------------------|------------------------------------------------------------------|----------------------|
| **⭕ AID (Association Identifier)** | Sent by the AP (Association Response or Re-Association Response) | `wlan.fixed.aid`       |
| **AID = 3**           | Filter for AID 3 (specific association identifier | eg. STA # 3)               | `wlan.fixed.aid == 3`  |
| **AID = 0**           | Filter for AID 0 (broadcast or multicast frames)                 | `wlan.fixed.aid == 0`  |


## 👂⏳🐓 PS Field: `Listen Interval`

- Listen Interval: **Sent by the STA** (`Association Request` or `Re-Association Request`)
- The client STA will go to `awake` state in a timing period called "Listen Interval".
- The "Association Request" or "Re-Association Request" frame includes a Listen Interval subfield within the Capabilities Information field.
- It is an integer between 0 and 65535 expressed in **units of Beacon Interval** (ex. 250 = Listen every 250 beacons).
- It indicates to the AP how often a client in PS mode wakes up to listen to the Beacon frames.
- In the AP, the Aging Time of the buffered frames bound to the client is implemented differently by each vendor but must not be shorter than the Listen Interval (or the WNM Sleep Interval in a WNM Sleep Mode Request frame).

The Listen Interval from the client is also vendor specific // In other words, **this is an unicast frame used for power management purposes sent from the STA to the AP, this value informs the AP of how many Beacons the STA will be dozing when in a power save state.** For example if a STA has a listen interval of 15 that means it will doze for 15 Beacons and if the Beacon interval is 100 time units the STA will doze for approximately 1.5 seconds. <br> <br>

### 🦈 Wireshark Filters: `Listen Interval`

| **Field**                              | **Description**                                                                       | **Wireshark Filter**             |
|----------------------------------------|---------------------------------------------------------------------------------------|----------------------------------|
| **⭕ Listen Interval**                  | Indicates to the AP how often a client in PS mode wakes up to listen to Beacon frames | wlan.fixed.listen_ival           |
| **🦈 Listen Interval = 250 (HEX)**     | Every 250 beacons (in hexadecimal representation)                                     | wlan.fixed.listen_ival == 0x00fa |
| **🦈 Listen Interval = 250 (Decimal)** | Every 250 beacons (in decimal representation)                                         | wlan.fixed.listen_ival == 250    |


---

### 📫📩📬 PS Information Element: `TIM (Traffic Indication Map)`

- **TIM (Traffic Indication Map)** is a IE (Information Element) present **only in `Beacon` frames** sent by an Access Point (AP). 
- It serves to indicate to power-saving devices which are connected to the network whether there are buffered frames (data packets) waiting for them at the AP.
- The TIM contains a **bitmap** where each bit corresponds to a particular device associated with the AP. If a bit is set to 1, it indicates that there are frames queued at the AP for that specific device.

TIM contains 2 Sub-Fields:

- `Bitmap Control` (AID = 0 and Bitmap Control = 1 indicates if any **Broadcast or Multicast** packets are buffered at the AP)
- `PVB (Partial Virtual Map` (Series of flags indicating whether each associated STA has **Unicast** frames buffered at the AP) _Because the bitmap is never transmitted in its entirety, it is referred to as a virtual bitmap, and the portion that is actually transmitted is referred to as a partial virtual bitmap._

⚠️ **`IMPORTANT`**: **The minimum value of the Length field of the Traffic Indication Map (TIM) information element is 4**. This value includes the length of the **Partial Virtual Bitmap**, which is at least one octet, along with the other **required fields (DTIM Count, DTIM Period, and Bitmap Control)**.

| **Field**                 | **Description**                                                                                              | **Wireshark Filter**            |
|---------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------|
| **⭕ Element ID = 5**     | Element ID value Of 5 Indicates Is A TIM.                                                                      | `wlan.tag.number == 5`            |
| **⭕ Length**              | Length Of The Information Carrying Fields (DTIM Count, DTIM Period, Bitmap Control, Partial Virtual Bitmap). | `wlan.tag.length`                 |
| **Tag Length = 4**     |  Lenght = 4 bits                                                                                              | `wlan.tag.length == 4`            |
| **⭕ DTIM Count**          | Incremental Beacon Frames Until The Next DTIM.                                                               | `wlan.tim.dtim_count`             |
| **DTIM = 0**           | Beacon Is A DTIM                                                                                             | `wlan.tim.dtim_count == 0`        |
| **DTIM = 1**           | 1 Beacon Left Until Next DTIM                                                                                | `wlan.tim.dtim_count == 1`        |
| **DTIM = 2**           | 2 Beacons Left Until Next DTIM                                                                               | `wlan.tim.dtim_count == 2`        |
| **⭕ DTIM Period**         | Number Of Beacon Frames Between DTIM Beacon.                                                                 | `wlan.tim.dtim_period`            |
| **DTIM Period = 1**    | Every Beacon Will Be A DTIM (ex. Ruckus_default_SSID)                                                        | `wlan.tim.dtim_period == 1`       |
| **DTIM Period = 2**    | Every 2nd Beacon Will Be A DTIM (ex. Fz3r0_CWAP_SSID)                                                        | `wlan.tim.dtim_period == 2`       |
| **DTIM Period = 3**    | Every 3rd Beacon Will Be A DTIM (ex. Muegahouse_SSID)                                                        | `wlan.tim.dtim_period == 3`       |
| **⭕ Bitmap Control**               | Indicates if Multicast/Broadcast traffic are buffered at the AP & also uses Bitmap Offset (0-127). | `wlan.tim.bmapctl`                |
| **Bitmap Control = 1**          | Multicast/broadcast frame buffering for any STA                                                        | `wlan.tim.bmapctl.multicast == 1`       |
| **Bitmap Control = 0**          | No multicast/broadcast frames buffering                                                                | `wlan.tim.bmapctl.multicast == 0`       |
| **Bitmap Offset = 0**           | How many bytes are Zero in Partial Virtual Bitmap (PVB)                                                | `wlan.tim.bmapctl.offset == 0`          |
| **Bitmap Offset > 0**           | How many bytes are Zero in PVB                                                                         | `wlan.tim.bmapctl.offset > 0`           |
| **⭕ PVB (Partial Virtual Bitmap)** | Series of flags indicating whether each associated STA has Unicast frames buffered at the AP.          | `wlan.tim.partial_virtual_bitmap`       |
| **PVB = 0**                     | No unicast frames are buffered                                                                         | `wlan.tim.partial_virtual_bitmap == 00` |
| **PVB more than 0**             | Unicast frames are buffered                                                                            | `wlan.tim.partial_virtual_bitmap > 00`  |

## 🚨📩📬 PS Information Element: `DTIM (Delivery Traffic Indication Map)`

`DTIM (Delivery Traffic Indication Map)`: **Sent by the AP** (`Beacon`)

- DTIM **is not present in all beacons** (or all TIMs inside a becon), it depends on the DTIM period (field inculded in the TIM)
- DTIM is a Information Element inside a TIM carried by a beacon frame (identical in structure to any other Beacon Frame).
- The only difference with a common Beacon Frame is that the content of the DTIM IE (Information Element) will give information about broadcast/multicast traffic that is buffered at the AP, in addition to the typical information about buffered unicast frames that is always present in the TIM. <br> <br>
    - ⭕ DTIM Count = 0: means that the current TIM (beacon) frame is a DTIM
    - ⭕ DTIM Count = 1: means 1 Beacon left until next DTIM
    - ⭕ DTIM Count = 2: means 2 Beacons left until next DTIM <br> <br>
    - ⭕ DTIM Delivery Period = 3: means every 3rd frame a beacon will be a DTIM
    - ⭕ DTIM Delivery Period = 2: means every 2nd frame a beacon will be a DTIM
    - ⭕ DTIM Delivery Period = 1: All the beacons will be a DTIM <br> <br>
    - ⭕ DTIM Bitmap Control = 1: There's a multicast/broadcast frame buffering in the AP for any STA
    - ⭕ DTIM Bitmap Control = 0: No multicast/broadcast frame buffering in the AP for any STA <br> <br>
    - ⭕ DTIM Partial Virtual Map (PVM) = 0: No unicast frame buffering in the AP
    - ⭕ DTIM Partial Virtual Map (PVM) > 0: Unicast frame(s) buffering in the AP for 1 or more STAs
---

### 📋🙋‍♂️🐓 Control Frame: `PS-Poll`

PS-POLL is the **legacy** PS mode mechanism is based on the PS-Poll frame to retrieve the buffered frames in the AP. 

- The PS-Poll frame is a short Control Frame containing the AID value of the client. 

PS-Poll have the following Sub-Fields:

| **Field**        | **Description**                           | **Wireshark Filter**                                            |
|------------------|-------------------------------------------|-----------------------------------------------------------------|
| **Type/Subtype** | Control Frame (01) / PS-Poll (1010)       | `wlan.fc.type == 1 && wlan.fc.type_subtype == 26`               |
| **AID**          | AID of the STA requesting buffered frames | `wlan.fc.type_subtype == 26 && wlan.aid == 3`                   |
| **BSSID**        | BSSID where the STA is associated         | `wlan.fc.type_subtype == 26 && wlan.bssid == f0:f0:f0:f0:f0:f0` |
| **Transmitter**  | MAC of the STA requesting buffered frames | `wlan.fc.type_subtype == 26 && wlan.ta == f1:f1:f1:f1:f1:f1`    |
| **Receiver**     | MAC of the AP buffering frames            | `wlan.fc.type_subtype == 26 && wlan.ra == f0:f0:f0:f0:f0:f0`    |

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


## 802.11 Power Save (Legacy power save mode)

- Less Efficient Power Save Mode.
- There are 2 Types of Legacy Power Save Mode _(Clients can support either one of the two legacy power save mechanisms at one time)_: <br><br>
1. **Power save Poll: `PS Poll**
2. **Non Power save Poll: `Non PS Poll`** 

---

### 802.11 Power Save (Legacy power save mode): `PS-Poll Mode`:

- As the name suggests `PS-Poll` stands for `Power Save Polling`.
- In this mode the client STA uses `PS-Poll`, this is a control frame the STA sends to an AP after receiving a beacon containing the STAs association ID (AID) in the TIM. The STA will send PS-Poll frames to the AP until it receives a frame from the AP with the `More Data bit set to 0`. A STA may not go back to sleep until its AID is clear from the TIM whereas APs may choose to delay response to the PS-Poll frame; this is vendor specific.
- The Access point uses the TIM information element to indicate to the station that there is unicast data buffered for the WLAN client STA to the AP.
- In PS Poll mode, the device may wake up at intervals to check for incoming data or to initiate data transmission, which can result in lower power consumption compared to the Non PS Poll mode.

````py

## 802.11 Power Save (Legacy power save mode): PS-Poll Mode

    # - In this example, the AP have 3 buffered unicast frames for the STA

######################################################################################################################
                           🏁🔋 STA Associates to the AP (BSS), indicating Listen Interval = 250 🔋🏁
                         🏁🔋 AP Resopond the Association setting the AID for the STA using AID = 5 🔋🏁
######################################################################################################################

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🛜 Association Request / Listen Interval = 250 ]}                 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Association Response / AID = 5 ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚫 Null Function No Data (Power Management = 1) ]} [Doze State] 🤳🏾💤 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} [Doze State] 🤳🏾💤 

######################################################################################################################
                        ⚡🔋 STA wakes up after a TIM indicating buffered frames for AID 5 (our STA) 🔋⚡
######################################################################################################################

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊⏰ Beacon with TIM announcing AID = 5 (STA identifier)                   

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🔋 PS-Poll (Power Management = 0) [STA Wake up] 🤳🏾🐓   

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} (PS-Poll ACK)

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Send Buffered Unicast Frame 1/3 (More Data = 1) {Buffered Frame 1/3}           

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊 ACK ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🔋 PS-Poll (Power Management = 0) [STA Wake up] 🤳🏾🐓    

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} (PS-Poll ACK)

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Send Buffered Unicast Frame 2/3 (More Data = 1) {Buffered Frame 2/3}            

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊 ACK ]}  

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🔋 PS-Poll (Power Management = 0) [STA Wake up] 🤳🏾🐓    

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} (PS-Poll ACK)

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Send Buffered Unicast Frame 3/3 (More Data = 0) {Buffered Frame 3/3}            

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊 ACK ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚫 Null Function No Data (Power Management = 1) ]} [Doze State] 🤳🏾💤 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} [Doze State] 🤳🏾💤

````

1. The **client STA** sends an `association request` to the AP, indicating it wants to associate and providing its `Listen Interval` value (e.g., **Listen Interval = 250**). The Listen Interval tells the AP how often the STA will wake up to listen to beacons., ex. a Listen Interval of 250 means that the STA will wake up every 250th beacon). AP uses the Listen Interval to determine the lifetime of buffered frames. // Then, **the AP acknowledges the reception of the association request** from the client STA by sending an `ACK` (acknowledgment) frame. <br><br>
    - 🦈 Listen Interval of 250 :: `wlan.fixed.listen_ival == 250` <br><br>
2. The **AP** responds with an `association response` frame, which includes the `Association ID (AID)` assigned to the client STA (e.g., **AID = 5**). // Then, the **client STA acknowledges the association response** from the AP by sending an ACK frame back to the AP. <br><br>
    - 🦈 AID os the STA assigned by the AP (ex. AID = 3) `wlan.fixed.aid == 3` <br><br>
3. The **client STA** sends a `Null Function` Frame with the `Power Management bit set to 1`, indicating that it is **entering the doze state (power save mode)** and has no data to send. // Then, the **AP acknowledges the Null Function Frame** from the client STA by sending an ACK frame, confirming that it knows the STA is now in doze state (power save mode). <br><br>
    - 🦈 Null Function with Power Management bit set to 1 ::  `wlan.fc.type_subtype == 36 && wlan.fc.pwrmgt == 1` <br><br>
4. AP send beacons normally, until the AP sends Beacon with TIM announcing AID = 5 ==>> Periodically, the AP sends a Beacon frame with a Traffic Indication Map (TIM) that indicates which STAs have buffered frames waiting for them. The TIM will include the AID of the client STA (e.g., AID = 3) when there are buffered frames for it. <br> <br>
    - ⭕ DTIM (Delivery-TIM) Count (1 byte / 8 bits): Incremental `Beacon Frames` until the next DTIM. <br> <br>
        - 🦈 DTIM = 0 ==>> **Beacon is a DTIM** :: `wlan.tim.dtim_count == 0`
        - 🦈 DTIM = 1 ==>> **1 Beacon left until next DTIM** :: `wlan.tim.dtim_count == 1`
        - 🦈 DTIM = 2 ==>> **2 Beacons left until next DTIM** :: `wlan.tim.dtim_count == 2` <br> <br>
    - ⭕ DTIM (Delivery-TIM) Period (1 byte / 8 bits): Number of `Beacon Frames` between DTIM beacon. <br> <br>
        - 🦈 DTIM period = 1 ==>> **Every beacon will be a DTIM** _(ex. Ruckus_default_SSID)_ :: `wlan.tim.dtim_period == 1`
        - 🦈 DTIM period = 3 ==>> **Every 2nd beacon will be a DTIM** _(ex. Fz3r0_CWAP_SSID)_ :: `wlan.tim.dtim_period == 2`
        - 🦈 DTIM period = 3 ==>> **Every 3rd beacon will be a DTIM** _(ex. Muegahouse_SSID)_ :: `wlan.tim.dtim_period == 3` <br> <br>
    - ⭕ Element ID (1 byte / 8 bits): Value of 5 indicates is a TIM // Tim Beacon is a DTIM, icluding the AID of our STA //  <br> <br>
        - 🦈 Tim beacon (Element ID = 5) :: `wlan.tag.number == 5`
        - 🦈 Current TIM beacon is a DTIM :: `wlan.tim.dtim_count == 0`
        - 🦈 Current TIM contains the Association ID (AID) = 3 :: `wlan.tim.aid == 3`
        - 🦈 **Tim beacon is a DTIM with Association ID (AID) = 3 :: `wlan.tag.number == 5 && wlan.tim.dtim_count == 0 && wlan.tim.aid == 3`** <br> <br>
5. **Client STA** sends `PS-Poll` with `Power Management = 0` indicating wake up ==>> Upon receiving a beacon with its AID (eg. AID = 3) indicated in the TIM, the client STA wakes up and sends a `PS-Poll (Power Save Poll)` frame to the AP to request the buffered data with `Power Management bit set to 0` indicating wake up. <br> <br>
    - ⭕ PS-Poll with Association ID (AID) = 3 and Power Management bit set to 0 :: ``  <br> <br>
        - PS-Poll Frame with PS Management set to 0 (awake) `wlan.fc.type_subtype == 26 && wlan.fc.pwrmgt == 0`
        - PS-Poll Frame with Association ID (AID) = 3 `wlan.fc.type_subtype == 26 && wlan.aid == 3 && wlan.fc.pwrmgt == 0` <br><br>
6. AP sends the **first** buffered unicast frame (`1/3`, `More Data = 1`) ==>> The AP responds to the PS-Poll by sending the **first** buffered unicast frame to the client STA. This frame has the "More Data" bit set to 1, indicating that there are more buffered frames waiting for the STA. // Then, the **client STA acknowledges the Data Frame with the "More Data" bit set to 1** from the AP by sending an ACK frame back to the AP. <br><br>
    - 🦈 More data for STA buffered at AP ::  `wlan.fc.moredata == 1` <br><br>
7. AP sends the **second** buffered unicast frame (`2/3`, `More Data = 1`) ==>> The AP responds to the PS-Poll by sending the **second** buffered unicast frame to the client STA. This frame has the "More Data" bit set to 1, indicating that there are more buffered frames waiting for the STA. // Then, the **client STA acknowledges the Data Frame with the "More Data" bit set to 1** from the AP by sending an ACK frame back to the AP. <br><br>
    - 🦈 More data for STA buffered at AP ::  `wlan.fc.moredata == 1` <br><br>
8. AP sends the **third and LAST** buffered unicast frame (`3/3`, `More Data = 0`) ==>> The AP responds to the PS-Poll by sending the **third and last** buffered unicast frame to the client STA. This frame has the "More Data" bit set to 0, indicating that there are NO MORE buffered frames waiting for the STA. // Then, the **client STA acknowledges the Data Frame with the "More Data" bit set to 0** from the AP by sending an ACK frame back to the AP. <br><br>
    - 🦈 More data for STA buffered at AP ::  `wlan.fc.moredata == 0` <br><br>
9. The **client STA** sends a `Null Function` Frame with the `Power Management bit set to 1`, indicating that it is **entering the doze state (power save mode)** and has no data to send or receive. // Then, the **AP acknowledges the Null Function Frame** from the client STA by sending an ACK frame, confirming that it knows the STA is now in doze state (power save mode). <br><br>
    - 🦈 Null Function with Power Management bit set to 1 ::  `wlan.fc.type_subtype == 36 && wlan.fc.pwrmgt == 1` <br><br>

---

### 802.11 Power Save (Legacy power save mode): `Non PS-Poll Mode`:

- The `Non PS Poll` mechanism refers to situations where a device **does not use the PS Poll mechanism** to wake up from its power saving mode and instead relies on other mechanisms to wake up and communicate with the AP.
- In this mode the client simply exits the PS mode and switches back to active mode. `Null Data` frames or `QoS Null Data` frames are generally used for this purpose.
- The device may wake up more frequently to check for incoming data or to initiate data transmission, which can result in higher power consumption compared to the PS Poll mode. However, it provides more flexibility and responsiveness for the device to communicate when needed.

````py

## 802.11 Power Save (Legacy power save mode): No PS-Poll Mode

    # - In this example, the AP have 3 buffered unicast frames for the STA

######################################################################################################################
                           🏁🔋 STA Associates to the AP (BSS), indicating Listen Interval = 250 🔋🏁
                         🏁🔋 AP Resopond the Association setting the AID for the STA using AID = 5 🔋🏁
######################################################################################################################

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🛜 Association Request / Listen Interval = 250 ]}                 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Association Response / AID = 5 ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚫 Null Function No Data (Power Management = 1) ]} [Doze State] 🤳🏾💤 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} [Doze State] 🤳🏾💤 

######################################################################################################################
                        ⚡🔋 STA wakes up after a TIM indicating buffered frames for AID 5 (our STA) 🔋⚡
######################################################################################################################

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊⏰ Beacon with TIM announcing AID = 5 (STA identifier)                   

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚫 Null Function No Data (Power Management = 0) ]} [STA Wake up] 🤳🏾🐓

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} [STA Wake up] 🤳🏾🐓

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Send Buffered Unicast Frame 1/3 (More Data = 1) {Buffered Frame 1/3}           

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊 ACK ]}
 
🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Send Buffered Unicast Frame 2/3 (More Data = 1) {Buffered Frame 2/3}            

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊 ACK ]}  

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Send Buffered Unicast Frame 3/3 (More Data = 0) {Buffered Frame 3/3}            

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊 ACK ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚫 Null Function No Data (Power Management = 1) ]} [Doze State] 🤳🏾💤 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]} [Doze State] 🤳🏾💤

````

1. The **client STA** sends an `association request` to the AP, indicating it wants to associate and providing its `Listen Interval` value (e.g., **Listen Interval = 250**). The Listen Interval tells the AP how often the STA will wake up to listen to beacons., ex. a Listen Interval of 250 means that the STA will wake up every 250th beacon). AP uses the Listen Interval to determine the lifetime of buffered frames. // Then, **the AP acknowledges the reception of the association request** from the client STA by sending an `ACK` (acknowledgment) frame. <br><br>
    - 🦈 Listen Interval of 250 :: `wlan.fixed.listen_ival == 250` <br><br>
2. The **AP** responds with an `association response` frame, which includes the `Association ID (AID)` assigned to the client STA (e.g., **AID = 5**). // Then, the **client STA acknowledges the association response** from the AP by sending an ACK frame back to the AP. <br><br>
    - 🦈 AID os the STA assigned by the AP (ex. AID = 3) `wlan.fixed.aid == 3` <br><br>
3. The **client STA** sends a `Null Function` Frame with the `Power Management bit set to 1`, indicating that it is **entering the doze state (power save mode)** and has no data to send. // Then, the **AP acknowledges the Null Function Frame** from the client STA by sending an ACK frame, confirming that it knows the STA is now in doze state (power save mode). <br><br>
    - 🦈 Null Function with Power Management bit set to 1 ::  `wlan.fc.type_subtype == 36 && wlan.fc.pwrmgt == 1` <br><br>
4. AP send beacons normally, until the AP sends Beacon with TIM announcing AID = 5 ==>> Periodically, the AP sends a Beacon frame with a Traffic Indication Map (TIM) that indicates which STAs have buffered frames waiting for them. The TIM will include the AID of the client STA (e.g., AID = 3) when there are buffered frames for it. <br> <br>
    - ⭕ DTIM (Delivery-TIM) Count (1 byte / 8 bits): Incremental `Beacon Frames` until the next DTIM. <br> <br>
        - 🦈 DTIM = 0 ==>> **Beacon is a DTIM** :: `wlan.tim.dtim_count == 0`
        - 🦈 DTIM = 1 ==>> **1 Beacon left until next DTIM** :: `wlan.tim.dtim_count == 1`
        - 🦈 DTIM = 2 ==>> **2 Beacons left until next DTIM** :: `wlan.tim.dtim_count == 2` <br> <br>
    - ⭕ DTIM (Delivery-TIM) Period (1 byte / 8 bits): Number of `Beacon Frames` between DTIM beacon. <br> <br>
        - 🦈 DTIM period = 1 ==>> **Every beacon will be a DTIM** _(ex. Ruckus_default_SSID)_ :: `wlan.tim.dtim_period == 1`
        - 🦈 DTIM period = 3 ==>> **Every 2nd beacon will be a DTIM** _(ex. Fz3r0_CWAP_SSID)_ :: `wlan.tim.dtim_period == 2`
        - 🦈 DTIM period = 3 ==>> **Every 3rd beacon will be a DTIM** _(ex. Muegahouse_SSID)_ :: `wlan.tim.dtim_period == 3` <br> <br>
    - ⭕ Element ID (1 byte / 8 bits): Value of 5 indicates is a TIM // Tim Beacon is a DTIM, icluding the AID of our STA //  <br> <br>
        - 🦈 Tim beacon (Element ID = 5) :: `wlan.tag.number == 5`
        - 🦈 Current TIM beacon is a DTIM :: `wlan.tim.dtim_count == 0`
        - 🦈 Current TIM contains the Association ID (AID) = 3 :: `wlan.tim.aid == 3`
        - 🦈 **Tim beacon is a DTIM with Association ID (AID) = 3 :: `wlan.tag.number == 5 && wlan.tim.dtim_count == 0 && wlan.tim.aid == 3`** <br> <br>
5. Upon receiving a beacon with its AID indicated in the TIM, the client STA wakes up and sends a Null Function Frame with the Power Management bit set to 0, indicating that it is now active and ready to receive data.
AP sends ACK. // The AP acknowledges the Null Function Frame from the client STA by sending an ACK frame, confirming that the STA is now awake.
6. AP sends the first buffered unicast frame (1/3, More Data = 1) ==>> The AP sends the first buffered unicast frame to the client STA. This frame has the "More Data" bit set to 1, indicating that there are more buffered frames waiting for the STA. // The client STA acknowledges the reception of the first buffered unicast frame by sending an ACK frame to the AP.
7. AP sends the second buffered unicast frame (2/3, More Data = 1) ==>> The AP sends the first buffered unicast frame to the client STA. This frame has the "More Data" bit set to 1, indicating that there are more buffered frames waiting for the STA. // The client STA acknowledges the reception of the first buffered unicast frame by sending an ACK frame to the AP.
8. AP sends the third buffered unicast frame (3/3, More Data = 0): ==>> The AP sends the third and final buffered unicast frame to the client STA, with the "More Data" bit set to 0, indicating that there are no more buffered frames for the STA. // The client STA acknowledges the reception of the first buffered unicast frame by sending an ACK frame to the AP.
9. Client STA sends Null Function Frame indicating No Data (Doze State): ==>> The client STA sends another Null Function Frame with the Power Management bit set to 1, indicating that it is entering the doze state (power save mode) again. // The AP acknowledges the Null Function Frame from the client STA by sending an ACK frame, confirming that it knows the STA is now in doze state (power save mode) once more.































## 802.11e
_The 802.11e standard is being designed to be backward compatible with the legacy 802.11 standard, which implies that DCF and PCF mode stations can work without restrictions in the new QoS enable environment. In fact, the traffic of a station working in DCF mode is treated as traffic belonging to AC1 of the new EDCA mode with TXOP equal to zero. Hence, from DCF point of view this coexistence is quite fair as DCF is a Best Effort traffic oriented. On the other hand, PCF mode stations in the new standard are managed by HC as if it were PC, which provides schedule for them. Therefore, there is hardly any change in system behaviour.     However, from 802.11e standpoint the introduction of legacy 802.11 stations in a QBSS system pose a risk to the QoS guarantees. Direct cooperation of both types of stations without any restriction on the legacy 802.11 traffic will penalize all QoS guarantees provided by standalone IEEE 802.11e network [3][4] due to previously mentioned 802.11 limitations. Therefore, to be able to provide real QoS support in wireless LAN with coexistence of 802.11 and 802.11e stations it will be necessary to consider some QoS mechanism for legacy stations._


## 802.11e-2005: `WMM` & `U-APSD`
_802.11e introduced **Wi-Fi Multimedia (WMM)** and also introduced Automatic Power Save Delivery (APSD) in two varieties, scheduled and unscheduled. **Unscheduled (U-APSD)** gets all the attention, it is the method that **WMM-PS** is based on | scheduled (S-APSD) is not in the objectives of either the CWNA or CWAP exam | The goal of APSD is to be more efficient than the PS-Poll method used previously. This is accomplished by replacing PS-Poll frames with **trigger frames**. The trigger frame can be ANY data frame; this increases the efficiency of the entire BSS by avoiding the use of the PS-Poll control frame altogether. || Wi-Fi Multimedia (WMM) uses different and more efficient ways for power save mode for client device (STA’s) than the original power save mode that introduced with the 802.11 standard also known as legacy power save mode. U-APSD (Unscheduled Automatic Power Save Delivery) uses what is known as a trigger and delivery method for devices that are enabled for power save. With this method a client device will only doze when not sending or receiving frames. The trigger frame is an event that will inform the client device not to doze until it has received the buffered frames. This eliminates the PS-Poll frame that is used with legacy power save mode._
- [802.11e-2005: Wi-Fi Multimedia (WMM) and Automatic Power Save Delivery (APSD) | QoS & PS_@ español_](https://es.wikipedia.org/wiki/IEEE_802.11e-2005)
- [802.11e-2005: Wi-Fi Multimedia (WMM) and Automatic Power Save Delivery (APSD) | QoS & PS _@ inglés_](https://en.wikipedia.org/wiki/IEEE_802.11e-2005)
- [`WWM Power Save` **(U-ASPD)** :: Frame Exchange](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/873ccc0d-708b-42c5-83b6-d0e4d27347a7) _`frame exchange`_
- [WMM & QoS Profile _@ Nayarasi_](https://mrncciew.com/2013/07/30/wmm-qos-profile/)

**WMM (U-APSD) power save mode uses `Trigger` to wake and transmit or receive frames** - This is accomplished by replacing PS-Poll frames with **trigger frames**. The trigger frame can be ANY data frame; this increases the efficiency of the entire BSS by avoiding the use of the PS-Poll control frame altogether._


## Offchannel Scanning


## IBSS Power Management
_In an IBSS configuration, no full-time AP exists and all systems may desire to enter sleep mode, the problem is there is no AP to send TIM or DTIM.  So in IBSS, **Announcement Traffic Indication Message (ATIM)** is use for power management._

- In IBSS (ad hoc network) there is no AP to send TIM or DTIM. So if a STA goes into power save mode multiple other STAs has to buffer its data for specific STA.
- So in IBSS, Announcement Traffic Indication Message (ATIM) is use for power management.
- ATIM is a management frame with no frame body.
- When a STA receives ATIM, that formally dozing station must begin the process of retrieving buffered frame from the stations that transmitted the ATIM.









































## 🛑🛜🚦 MAC Operations: `Protection Mechanisms`
_HR/DSSS STAs (802.11b legacy) does not understand OFDM Modulation used by ERP STAs. But, HT/ERP/OFDM (802.11n modern) STAs are backwards compatible with HR/DSSS STAs & can transmit & understand HR/DSSS modulation | The way to acomplish that is using RTS/CTS mechanisms in case that legacy STAs are using the same AP of modern devices | RTS/CTS are the most used mechanism in Wi-Fi, there's also a mechanism called CTS-to-self that is not a frame defined in the standard, this frame is a CTS frame without a preciding RTS frame, this is usually done by the AP | ERP element is present only on 2.4GHz network supporting 802.11g & it is present in beacon & probe responses. The non-ERP_Present bit set to 1 in following conditions a. A nonERP station (legacy 802.11 or 802.11b) associate to the cell, b. A neighboring cell is detected, allowing only nonERP data rates, c. Any other management frame (except probe request) is received from neighboring cell supporting only nonERP data rates. | To ensure backward compatibility with older 802.11a/b/g radios, 802.11n (HT) access points may signal to other 802.11n stations when to use one of four HT protection modes.| A field in the beacon frame called the HT Protection field has four possible settings of 0–3._

- [802.11 Protection Mechanisms _@ Nayarasi_](https://mrncciew.com/2014/11/02/cwap-802-11-protection-mechanism/) _`Nayarasi`_
- [Protection Ripple in ERP 802.11 WLANs](https://www.cwnp.com/uploads/protection_ripple_in_erp_802-11_wlans.pdf) _`whitepaper`_
- [802.11n Protection Mechanisms: Part 1 @ _CWNP_](https://www.cwnp.com/802-11n-protection-mechanisms-part-1/) _`whitepaper`_
- [802.11n Protection Mechanisms: Part 2 @ _CWNP_](https://www.cwnp.com/802-11n-protection-mechanisms-part-2/) _`whitepaper`_
- [Protection Ripple in ERP 802.11 WLANs @ _CWNP_](https://www.cwnp.com/uploads/protection_ripple_in_erp_802-11_wlans.pdf) _`whitepaper`_
- [HT Protection Mechanisms](https://dot11ap.wordpress.com/ht-protection-mechanisms/) _`definitions`_

## Protection Mechanisms: `CTS`, `CTS-to-Self`, `Dual CTS`

- `RTS/CTS` :: (802.11g or newer) :: The most used mechanism in Wi-Fi
- `CTS-to-self` :: (802.11g or newer) :: that is not a frame defined in the standard, this frame is a CTS frame without a preciding RTS frame, this is usually done by the AP 
- `Dual CTS` Protection is used by the AP to set a NAV at STAs that do not support STBC and at STAs that can associate solely through the STBC beacon. (0 – dual CTS protection is not required, 1 – dual CTS protection is required)

## Protection Modes: `Important Concepts`

Protection mechanisms cause a STA that is a potential interferer to defer any transmission for a known period of time. When these mechanisms are used:

1. non-ERP STAs do not interfere with frame exchanges using ERP PPDUs between ERP STAs.
2. non-HT STAs do not interfere with frame exchanges using HT PPDUs between HT STAs.

As a result, non-ERP and/or non-HT STAs are allowed to coexist with ERP and/or HT STAs.



### `Protection Modes Elements`

- **Protection Modes Elements** are present in `Beacons` & `Probes` <br><br>
    - `ERP Information Element`: Present in 2.4 GHz Beacons & Probes
    - `HT Information Element`: Present in 2.4 & 5 GHz Beacons & Probes

### Protection Modes: Difference Between `802.11g (ERP)` & `802.11n (HT)`

When 802.11g was introduced, we had RTS/CTS and CTS-to-Self protection mechanisms.  What do we get with 802.11n so that it's backwards compatible with 802.11a and 802.1b/g? First, there's a couple of new things I'd like to introduce, and then we'll get to the protection rules.

- **`802.11g` = `ERP`**: In an **ERP Beacon**, ERP stations look at the **ERP Information Element** to determine whether or not protection is necessary in the BSS
- **`802.11n` = `HT`**: In an **HT Beacon**, HT stations use the **Operating Mode** and **Non-greenfield STAs Present** fields in the **HT Information Element** to determine whether or not to use protection.

## Non-ERP protection mechanisms

- IEEE 802.11-2007 standard mandate support for both DSSS (Direct Sequence Spread Spectrum) & OFDM (Orthogonal Frequency Division Multiplexing) technologies for clause 19 ERP (802.11g) radios.
- When clause 18 (HR-DSSS) & clause 15 DSSS (802.11) coexisting in ERP BSS, 802.11g devices need to provide compatibility for slower 802.11/802.11b devices.
- In this **mixed mode** (801.11 + 802.11b) 802.11g devices enable “Protection mechanism” also known as **`802.11g Protected mode`**.

### ERP Information Element

ERP Information Element (IE) contains information about Claue15 (802.11 Prime) or Clause 18 (802.11b) stations in the BSS that are not capable of communicating Clause 19 (ERP-OFDM) data rates. It also identifies whether AP should use protection mechanism & whether to use long or short preambles. 

````py
## Beacon or Probe :: ERP Information Element

<----------------------------------- ERP Information ------------------------------>
|--------------|------------|-----------|-----------------|----|----|----|----|----|
|  Element ID  | Lenght (1) |  Non-ERP  | Barker Preamble | r3 | r4 | r5 | r6 | r7 |
|              |            |  present  |       Mode      |    |    |    |    |    |
|--------------|------------|-----------|-----------------|----|----|----|----|----|
       8             8            1              1           1    1    1    1    1

````

- Element ID : ERP Infomration Element = 42 :: `wlan.tag.number == 42`
- Tag Lenght = 1 ::  `wlan.tag.length == 1` <br><br>
- ERP Information HEX combination: `wlan.erp_info == 0x00` <br><br>
    - Non-ERP Present : = 1 when non-ERP station is associated to the BSS :: `wlan.erp_info.erp_present == 1`
    - Use Protection : = 1 when non-ERP station is associated to the BSS :: `wlan.erp_info.use_protection == 1`
    - Barker Preamble : = 1 if one or more associated non-ERP stations are not capable of using short preambles. :: `wlan.erp_info.barker_preamble_mode == 1`
    - Reserved (HEX) :: `wlan.erp_info.reserved == 0x00`

**How it works?**

ERP STAs shall use protection mechanisms (such as RTS/CTS or CTS-to-self) for ERP-OFDM MPDUs of type Data or an MMPDU when the Use_Protection field of the ERP element is equal to 1. Note that when using the Clause 19 options, ERP-PBCC or DSSS-OFDM, there is no need to use protection mechanisms, as these frames start with a DSSS header.

In following scenarios that can trigger protection in an ERP basic service set:

1. **An HR-DSSS (802.11b) client association will trigger protection.**:
    - If a non-ERP STA associates with an ERP AP, the ERP AP will enable the **NonERP_Present** bit in its own beacons, enabling protection mechanisms in its BSS. <br><br>
2. **If an 802.11g AP hears a beacon frame from an 802.11 or 802.11b access point or ad hoc client, the protection mechanism will be triggered.**:
    - If an ERP AP hears a beacon from an AP where the supported data rates contain only 802.11b or 802.11 DSSS rates, it will enable the **NonERP_Present** bit in its own beacons, enabling protection mechanisms in its BSS. <br><br>
3. **If an ERP AP hears a management frame (other than a probe request) where the supported rate includes only 802.11 or 802.11b rates**: 
    - If an ERP AP hears a management frame (other than a probe request) where the supported rate includes only 802.11 or 802.11b rates the **NonERP_Present** bit may be set to 1.

**So, the 3 scenarios than can trigger the protections are:**

1. HR-DSSS (802.11b) client association, in the ERP (802.11g) WLAN.
2. ERP (802.11g) WLAN AP "hear" sorrounding Beacons of 802.11-Prime, 802.11b or Ad-Hoc Networks.
2. ERP (802.11g) WLAN AP "hear" sorrounding Management Frames (except probe request) using 802.11 or 802.11b data rates.

## HT protection mechanisms

- HT transmissions, are protected if there are other STAs present that cannot interpret HT transmissions correctly.
- The HT Protection and Nongreenfield HT STAs Present fields in the HT Operation element within Beacon and Probe Response frames are used to indicate the protection requirements for HT transmissions.
- To ensure backward compatibility with older 802.11a/b/g radios, 802.11n (HT) access points may signal to other 802.11n stations when to **use one of four HT protection modes**.
- A field in the beacon frame called the HT Protection field has four possible settings of 0–3.
- Much like an ERP (802.11g) access point, the protection modes may change dynamically depending on devices that are nearby or associated to the HT (802.11n) access point.
- The protection mechanisms that are used are RTS/CTS, CTS-to-Self, Dual-CTS, or other protection methods.

### HT: `no protection mode / Greenfield`

The HT Protection field may be set to **no protection mode / Greenfield** only if the following are true:

1. All STAs detected in the primary or the secondary channel are HT STAs, and:
2. All STAs that are known by the transmitting STA to be a member of this BSS are either:
    1. 20/40 MHz HT STAs in a 20/40 MHz BSS, or:
    2. 20 MHz HT STAs in a 20 MHz BSS.

### HT: `non-member protection mode`

The HT Protection field may be set to **non-member protection mode** only if the following are true:

- A **non-HT STA is detected in either the primary or the secondary channel or in both the primary and secondary channels**, that is not known by the transmitting STA to be a member of this BSS, and
- All STAs that are known by the transmitting STA to be a member of this BSS are HT STAs.

### HT: `20 MHz protection mode`

The HT Protection field may be set to **20 MHz protection mode** only if the following are true:

- All STAs detected in the primary channel and all STAs detected in the secondary channel are HT STAs and all STAs that are members of this BSS are HT STAs, and
- This BSS is a 20/40 MHz BSS, and
- There is at least one 20 MHz HT STA associated with this BSS.

### HT: `non-HT mixed mode`

The HT Protection field may be set to **20 MHz protection mode** only if non of any 3 other protection mechanisms (`no protection mode / Greenfield`, `non-member protection mode`, `20 MHz protection mode`) are used. 






## HT Protection Mechanisms: `Operating Mode`

The **Operating Mode** field has 4 possible settings: `0`,`1`,`2` & `3`:

- **`Mode 0`**: **No Protection Mode** / **Greenfield Mode**: <br><br>
    - All STAs detected in primary or secondary channel are HT STAs
    - If all stations in the BSS are 20/40 MHz HT capable
    - or if the BSS is 20/40 MHz capable
    - or if all stations in the BSS are 20 MHz HT stations in a 20 MHz BSS. <br><br>
- **`Mode 1`**: **HT non-member protection mode**: <br><br>
    - A non-HT STA or AP that is not member of this BSS, is detected using primary or secondary channels.
    - All STAs that are members of this BSS are HT STAs <br><br>
- **`Mode 2`**: **20 MHz protection mode**: <br><br>
    - Only HT STAs are associated in the BSS either the primary or secondary channel.
    - This BSS is a 20/40 MHz BSS
    - There is at least one 20 MHz STA associated in this BSS  <br><br>
- **`Mode 3`**: **non-HT Mixed Mode**: <br><br>
    - Used if one or more non-HT stations are associated in the BSS (All other cases).

## Protection Mechanisms: `HT Greenfield` & `Non-greenfield` 

There are two kinds of HT stations: 

1. HT STAs capable of using greenfield format.
2. HT STAs NON-capable of using greenfield format (eg. legacy devices).

The "Non-greenfield STAs Present" bit is set to 0 if **all HT STAs that are associated are greenfield capable**:  

The "Non-greenfield STAs Present" bit is set to 1 if **one or more HT STAs that are not greenfield capable are associated**:

HT APs use this bit to tell greenfield capable STAs to use protection when non-greenfield-capable STAs are present. Greenfield transmissions are to be protected by setting the duration/ID value in all frames sent during a TXOP to the time remaining in the TXOP.



## Protection Mechanisms: `Protection Modes`

### HT Mixed Mode: `HR/DSSS (Legacy)` & `HT/OFDM (Modern)`
_Most Common Protection Mechanism | Assumes that there are 802.11a/b/g stations using the same channel. | RTS/CTS Protection Mechanism with 802.11b backward compatibility activated_
- [Protection Mechanism: Mixed Mode](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/a894e9c6-8a67-4080-9a97-75eb4fd51f44) 

### HT No Protection Greenfield Mode: `No protection set`
_Assumes that there are NO 802.11a/b/g stations using the same channel. | No protection mechanisms are active_
- [What is 802.11n "Greenfield" mode?](https://www.computerweekly.com/news/2240101850/What-is-80211n-Greenfield-mode)

### HT 20 MHz Protection Set: `All STAs are HT`
_All STAs detected in the primary or the secondary channel are HT STAs, and All STAs that are known by the transmitting STA to be a member of this BSS are either: 20/40 MHz HT STAs in a 20/40 MHz BSS, or 20 MHz HT STAs in a 20 MHz BSS._
- [Protection Mechanism: Mixed Mode](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/a894e9c6-8a67-4080-9a97-75eb4fd51f44) 












## Resources

- [802.11 Power Management with packet captures](https://dot11zen.blogspot.com/2018/02/80211-power-management-with-packet.html) _`dot11zen`_
- [802.11 Power Save Methods](https://howiwifi.com/2020/06/25/power-save-methods/) _`how to Wi-fi`_
- [PS Poll & Non PS Poll :: Legacy Power Management](https://aletheatech.com/legacy-power-save-test-using-managed-client/) _`ale the teach`_
- [Unscheduled Automatic Power Save Delivery (U-APSD)](https://aletheatech.com/uapsd-wmm-powersave/)
- [802.11 Power Management explained super easy! | Diagrams & PCAP](https://www.mdpi.com/2079-9292/11/23/3914)
- [802.11 Power Save Modes & Power Management](https://www.youtube.com/watch?v=m363xe-fia8) _`video`_
- [802.11 WLAN Power Management](https://www.youtube.com/watch?v=M_RpvOeiqp0) _`short video`_
- [802.11 Power Management](https://mrncciew.com/2014/10/14/cwap-802-11-power-management/) _`nayarasi`_
- [Understanding SMPS Method for Wi-Fi Power Management](https://www.cwnp.com/smps/) _`cwnp`_
- [Power Save Mechanisms for 802.11ax](https://balramdot11b.com/2020/06/03/power-save-mechanisms-802-11ax/) _`ale the teach`_
- [Coexistence of IEEE 802.11b & 802.11e STAs in QoS enabled WLAN](https://www.researchgate.net/publication/221278781_Coexistence_of_IEEE_80211B_and_IEEE_80211E_Stations_in_QoS_Enabled_Wireless_Local_Area_Network)
- [IEEE 802.11e :: DEVx](https://www.devx.com/terms/ieee-802-11e/) _`devx`_ <br><br>
- [802.11 Power Save Methods :: CWAP training :: PCAPs Analysis :: Legacy + 802.11e + 802.11n + VHT TXOP PS – 802.11ac-2013](https://howiwifi.com/2020/06/25/power-save-methods/) _`howtowifi`_
- [Legacy Power Save Mode VS Wireless Multimedia Power Save mode VS Extended Power Save mode](https://academy.nordicsemi.com/courses/wi-fi-fundamentals/lessons/lesson-6-wifi-fundamentals/topic/power-save-modes-2/#:~:text=But%20if%20the%20More%20Data%20field%20is,back%20to%20sleep.%20Extended%20Power%20Save%20mode.)
- [802.11 Power Management with packet capture examples _@ dot11zen_](https://dot11zen.blogspot.com/2018/02/80211-power-management-with-packet.html)
- [What are the benefits and drawbacks of WiFi power saving modes (PSM and U-APSD)?](https://www.linkedin.com/advice/1/what-benefits-drawbacks-wifi-power-saving-modes-psm-u-apsd)
- [Power Save basic/legacy standard](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/c1ce9269-5dd2-4cf3-93ac-5db322f1ea72) _`diagram`_
- [STA Power Save Notification :: Frame Analysis](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/fd0d1066-fadd-4ee5-9ad8-e5eed0c510cd) _`Frame Decode`_
   - [**(Re)Association Request**: `Listen Interval`]() How often STA wakes up & listen beacons | In units of Beacon Interval | Determine lifetime of buffered frames
   - [**(Re)Association Response**: `Association Identifier (AID)`]() The ID the STA will get | Useful when AP buffer Data for STA using PS Poll
   - [**Null Data** or **QoS Null Data**: `Power Management 1/0`]() PS Mode (Power Save / Sleep) = 1 | Active Mode (Wake up) = 0 | 0x0001 = 1 | 0x0002 = 2 | 0x000a = 10
   - [**Beacon Frame**: `TIM` & `DTIM` ((Delivery) Traffic Indicator Map)](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/df02f9f6-05a8-4e93-9083-4b0db11899d2) Advice is there's buffered data for STAs in low-power mode | DTIM for Mulitcast & Broadcast
   - [TIM: Traffic Indication Map](https://en.wikipedia.org/wiki/Traffic_indication_map) _`wiki`_
   - [TIM: Traffic Indication Map: `Header`](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/8caa7780-0199-4265-8fe3-d01e58a5f8cb) _`header frame`_
   - [TIM PCAP Decode](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/7f25e49e-937c-41e5-a60a-834138cd3fe1) _`pcap decode`_
   - [`Off-Channel Scanning`: PCAP Decode](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/ed85dd9d-25a9-42e2-99f5-7563ee511dd2) PS Mode can be used by STA to scan other APs/CHs in miliseconds for roaming
- [QoS - Understanding ADD Traffic Stream (ADDTS) for U-APSD](https://www.hitchhikersguidetolearning.com/2017/09/17/understanding-add-traffic-stream-addts-for-u-apsd/)


https://telcomatraining.com/what-is-tim-traffic-indication-map/



