
# 📡🛜🎯HT/VHT Capabilities: `Transmit Beamforming`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Networking` `Wireless Networking` `IEEE 802.11` `Wi-Fi` `CWNA` `CWAP` `CWNE` `CCNP` `HT/VHT Capabilities` `Beamforming` `Transmit Beamforming` `Implicit Beamforming` `Explicit Beamforming` `Beamformee` `Beamformer` `SU (Single User) Beamforming` `MU (Multi User) Beamforming`

---

<br>

# Index















# Transmit Beamforming (TxBF)

**Transmit Beamforming (TxBF)** is a wireless signal enhancement technique **introduced as an optional feature in 802.11n** and **later standardized in 802.11ac/ax**. 

- **“Beamforming gains are expected to be approximately `+ 3 dB` in the transmitted direction. In practice, this gain will typically be one step up in data rates (increasing one `+1 MCS` number) for a mid-range transmission.”**
- **Beamforming** uses a calibration process called **`Channel Sounding`** **between `APs` and client `STAs`** to determine if and how energy can be radiated in an optimal direction.

### Beamforming in 802.11ac Wi-Fi 5

- In 802.11ac, Explicit beamforming got fine-tuned, and only Null data packet (NDP) Explicit Beamforming is supported
- 802.11ac: enables single user (SU) and multi user (MU) beamforming which aims to improve SNR (and hence throughput) between a wireless client and AP. 

## Transmit Beamforming (TxBF): `3 main categories`

There are various forms of beamforming, some standards-based, most proprietary to certain vendors. The 3 main types are: 

### 1. `On-Chip Beamforming`

- **802.11n standards-based** transmit beamforming.
- The radio chipset coordinates the signal processing across multiple transmit radio chains, altering timing and phase alignment of each signal, in an attempt to have multiple signal copies arrive at the receiver "in-phase" to provide passive gain.
- **Signal gains are `3dB` maximum**, which is quite logical if you think about what's going on at the receiver - **two in-phase signals merge, potentially doubling the amplitude of the signal at the receiver**.

### 2. `Static Beamforming` 

- Semi-directional or directional antennas.
- Antennas don't change, or move, or dynamically adjust. They simply focus the signal in a specific direction.
- **Signal gains can potentially be very large `>10dB**`, based on the dBi rating of the antenna selected.

### 3. `Antenna Beamforming`

- **This is what Ruckus does best**.
- They have **multiple antenna elements (an antenna array if you will)**, some **polarized horizontally** and some **polarized vertically**.
- The radio chipset sends one signal and a complex formula selects the best possible antenna element combinations to transmit the signal to the client.
- **Signal gains max out around `9dB` in the Ruckus implementation**, _(it could be higher with different antenna array designs)_.



## Transmit Beamforming (TxBF): `Vendor Implementation`

Some WLAN vendors implement Transmit Beamforming (TxBF) in different proprietary ways:

### 802.11n: `Transmit Beamforming (TxBF)` _Original feature_

- Transmit Beamforming (TxBF) got introduced as an optional feature of the 802.11n amendment and later standardized in 802.11ac/ax.
- It uses multiple antennas to focus and direct the transmission toward a specific client, improving signal strength, range, and reliability.
- However, for TxBF to work, the client device must support Transmit Channel Feedback (TxCBF) to provide feedback to the access point.
- This dependency limits its effectiveness in environments with legacy or non-compliant devices.

### Cisco: `Client Link`

- While beamforming (TxBF) is effective, it has limitations tied to client-side capabilities.
- ClientLink would fit into the category of **on-chip beamforming**  using standards-based **transmit beamforming with implicit feedback**, since **the client is not required to support beamforming and explicit feedback mechanisms**.
- That's one of their big selling points, improvement of legacy clients by upgrading to 802.11n APs.
- Cisco ClientLink is a more versatile solution because it doesn’t depend on client support and works across all device types, ensuring better overall network performance, especially in mixed environments with legacy devices.

### Ruckus: `Beamflex`

- The "normal" Beamforming in 802.11ac is a **radio based technology**. Whereas BeamFlex engages adaptive antennas so this is an **antenna based technology**.
- What Ruckus does is use beamforming (which is radio based) and combines it with adaptive antennas (BeamFlex which antenna based) to maximize the performance.
- **BeamFlex is not client dependent**. It can work with any 802.11 standard client. Whereas beamforming requires a 802.11ac client. Just to add, not all 802.11ac standard clients come with TxBF built-in.
- **Because of this... you will not see NPS Announcements or HT/VHT Sounding Feedback Matrix/SNR frame exchange between APs & STAs**




## Transmit Beamforming (TxBF): `Beamformer` & `Beamformee`

Beamforming (TxBF) relies on two key entities: 

The beamformer is the transmitter, and beamformee is the receiver.

1. `Beamformer`: Which actively shapes the transmission pattern. (Typical = AP)
2. `Beamformee`: Which receives and provides feedback to facilitate optimization. (Typical = client STA)

|                   	|                                                                                                                                         **Beamformer**                                                                                                                                         	|                                                                                             **Beamformee**                                                                                            	|                                                                                                                                        **Beamforming**                                                                                                                                        	|
|:-----------------:	|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
| **Device**        	| `AP`<br>Generates the directional transmission pattern to optimize the signal                                                                                                                                                                                                                  	| `Client STA`<br>Receiving device interpreting signals optimized by the beamformer (AP)                                                                                                                	| `Unidirectional` <br>Typical in setups where only the AP optimizes the link toward clients                                                                                                                                                                                                    	|
| **Device**        	| `AP & client STA` <br>In advanced MU-MIMO systems where both entities can mutually optimize                                                                                                                                                                                                    	| `AP & client STA` <br>Receivers that provide channel state information to the beamformer (AP/STA).                                                                                                    	| `Bidirectional`<br>Implemented in advanced setups like 802.11ax with downlink and uplink MU-MIMO                                                                                                                                                                                              	|
| _**Description**_ 	| _The beamformer uses antenna arrays and beamforming algorithms to compute signal weights based on the channel response matrix (CSI). <br>This enables focusing the signal toward a specific receiver, enhancing the signal-to-noise ratio (SNR) and minimizing interference to other devices._ 	| _The beamformee measures channel characteristics and provides feedback to the beamformer via the Compressed Beamforming Report, containing spatial matrix data (CSI Feedback) for link optimization._ 	| _Beamforming is a signal processing technique using MIMO antennas to steer transmissions toward specific receivers. <br>In Wi-Fi, its main purpose is to maximize spectral efficiency by reducing propagation losses and improving overall network capacity, critical in dense environments._ 	|




## Transmit Beamforming (TxBF) Methods: `Explicit` & `Implicit`

which has two methods `Implicit` and `Explicit` beamforming.

### `Explicit Beamforming (TxBF)` - Commonly Used

- **Requires feedback from the stations in order to determine the amount of phase-shift required for each signal.**

**How it works?**

1. The Transmitter (e.g., AP) sends a sounding frame (like a Null Data Packet, NDP)
2. the Receiver (e.g., STA) calculates channel characteristics. It then sends feedback to the transmitter, including the required phase-shift and amplitude adjustments for beamforming.

**Explicit Beamforming (TxBF) Characteristics**

- Requires feedback from the client (receiver).
- Achieves higher accuracy since the transmitter has detailed channel information.
- Common in modern Wi-Fi standards like 802.11ac (VHT) and 802.11ax (HE).

### `Implicit Beamforming (TxBF)` - Not Commonly Used

- **Uses an implicit channel-sounding process to optimize the phase differentials between the transmit chains.**

**How it works?**

1. The transmitter estimates the channel state by analyzing incoming signals from the receiver, like regular traffic frames or ACKs. It uses these estimations to calculate beamforming parameters without explicit feedback.

**Implicit Beamforming (TxBF) Characteristics**

- May be used in simpler or **legacy** systems
- No explicit feedback is required from the receiver.
- Less accurate because channel estimation relies on indirect observations.

## Transmit Beamforming (TxBF): `SU (Single User)` & `MU (Multi User)`

### `In Multi-User Beamforming`

- only Access Point can be a Beamformer. (Most Commonly Used)

**MU (Multi User) Beamforming Characteristics:**
 
### `In Single User beamforming`

- Access Point or client STA can be a Beamformer.
- Beamforming is applied to improve the signal quality for a single device (STA) at a time

**SU (Single User) Beamforming Characteristics:**


## Transmit Beamforming (TxBF): `SU (Single User)` & `MU (Multi User)` VS `Explicit` & `Implicit`

- Explicit vs. Implicit Beamforming: Describes **`HOW`** the beamforming parameters are determined.
    - `Explicit` relies on client feedback
    - `Implicit` uses estimated data. <br><br>
- Single-User vs. Multi-User Beamforming: Describes **`WHO`** the target of the beamforming is.
    - `SU` focuses on one device at a time
    - `MU` optimizes streams for multiple devices simultaneously.

|     **Beamforming Type**    	|   **Key Method**   	| **Beamformer** 	| **Beamformee** 	|                      **Primary Use Case**                      	|
|:---------------------------:	|:------------------:	|----------------	|:--------------:	|:--------------------------------------------------------------:	|
| **Explicit Beamforming**    	| Feedback-based     	| AP             	| STA            	| Mostly Used<br>High-performance networks, precise tuning       	|
| **Implicit Beamforming**    	| Estimation-based   	| AP or STA      	| AP or STA      	| Less used (only for 802.11n)<br>Simpler systems, less overhead 	|
| **Multi-User Beamforming**  	| Multi-device focus 	| AP             	| STA            	| Mostly Used<br>High-density networks with many devices         	|
| **Single-User Beamforming** 	| Per-device focus   	| AP or STA      	| AP or STA      	| Less used<br>Individual device optimization                    	|




## Transmit Beamforming (TxBF) Methods: `Frames` & `Elements`

There are different 802.11 frames involved in transmit beamforming:

---

### `Beacon Frames & Probe Responses` : `AP Beamforming Capabilities`

- Sent from the `Beamformer / AP` to `Broacast`
- Beacon frames include the HT Capabilities and VHT Capabilities tags, which signal beamforming capabilities and support in 802.11n/ac networks. 
- These fields indicate whether an AP (Access Point) can perform transmit beamforming, receive beamforming, and related operations.

#### This Beacon Frame es showing that the AP `SU Single User`  beamformer:

````java


802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (334 bytes)
        Tag: SSID parameter set: "Fz3r0 💀🎩"

        Tag: HT Capabilities (802.11n D1.10)
            Tag Number: HT Capabilities (802.11n D1.10) (45)
            Tag length: 26
            HT Capabilities Info: 0x19ef
            A-MPDU Parameters: 0x17
            Rx Supported Modulation and Coding Scheme Set: MCS Set
            HT Extended Capabilities: 0x0000
            Transmit Beam Forming (TxBF) Capabilities: 0x19810418
                .... .... .... .... .... .... .... ...0 = Transmit Beamforming: Not supported                                                                         <<<<-----||
                .... .... .... .... .... .... .... ..0. = Receive Staggered Sounding: Not supported                                                                   <<<<-----||
                .... .... .... .... .... .... .... .0.. = Transmit Staggered Sounding: Not supported                                                                  <<<<-----||
                .... .... .... .... .... .... .... 1... = Receive Null Data packet (NDP): Supported
                .... .... .... .... .... .... ...1 .... = Transmit Null Data packet (NDP): Supported
                .... .... .... .... .... .... ..0. .... = Implicit TxBF capable: Not supported                                                                        <<<<-----||
                .... .... .... .... .... .... 00.. .... = Calibration: incapable (0x0)                                                                                <<<<-----||
                .... .... .... .... .... ...0 .... .... = STA can apply TxBF using CSI explicit feedback: Not supported                                               <<<<-----||
                .... .... .... .... .... ..0. .... .... = STA can apply TxBF using uncompressed beamforming feedback matrix: Not supported                            <<<<-----||
                .... .... .... .... .... .1.. .... .... = STA can apply TxBF using compressed beamforming feedback matrix: Supported                                  <<<<-----||
                .... .... .... .... ...0 0... .... .... = Receiver can return explicit CSI feedback: not supported (0x0)                                              <<<<-----||
                .... .... .... .... .00. .... .... .... = Receiver can return explicit uncompressed Beamforming Feedback Matrix: not supported (0x0)                  <<<<-----||
                .... .... .... ...1 0... .... .... .... = STA can compress and use compressed Beamforming Feedback Matrix: immediate feedback capable (0x2)           <<<<-----||
                .... .... .... .00. .... .... .... .... = Minimal grouping used for explicit feedback reports: No grouping supported (0x0)                            <<<<-----||
                .... .... ...0 0... .... .... .... .... = Max antennae STA can support when CSI feedback required: 1 TX antenna sounding (0x0)                        <<<<-----||
                .... .... .00. .... .... .... .... .... = Max antennae STA can support when uncompressed Beamforming feedback required: 1 TX antenna sounding (0x0)   <<<<-----||
                .... ...1 1... .... .... .... .... .... = Max antennae STA can support when compressed Beamforming feedback required: 4 TX antenna sounding (0x3)     <<<<-----||
                .... .00. .... .... .... .... .... .... = Maximum number of rows of CSI explicit feedback: 1 row of CSI (0x0)                                         <<<<-----||   
                ...1 1... .... .... .... .... .... .... = Maximum number of space time streams for which channel dimensions can be simultaneously estimated: 4 space time streams (0x3)
                000. .... .... .... .... .... .... .... = Reserved: 0x0

            Antenna Selection (ASEL) Capabilities: 0x00
        Tag: HT Information (802.11n D1.10)

        Tag: VHT Capabilities
            Tag Number: VHT Capabilities (191)
            Tag length: 12
            VHT Capabilities Info: 0x43c179b1
                .... .... .... .... .... .... .... ..01 = Maximum MPDU Length: 7 991 (0x1)
                .... .... .... .... .... .... .... 00.. = Supported Channel Width Set: Neither 160MHz nor 80+80 supported (0x0)
                .... .... .... .... .... .... ...1 .... = Rx LDPC: Supported
                .... .... .... .... .... .... ..1. .... = Short GI for 80MHz/TVHT_MODE_4C: Supported
                .... .... .... .... .... .... .0.. .... = Short GI for 160MHz and 80+80MHz: Not supported
                .... .... .... .... .... .... 1... .... = Tx STBC: Supported
                .... .... .... .... .... .001 .... .... = Rx STBC: 1 Spatial Stream Supported (0x1)
                .... .... .... .... .... 1... .... .... = SU Beamformer Capable: Supported        <<<<-----|| SINGLE USER (SU) BEAMFORMER CAPABLE
                .... .... .... .... ...1 .... .... .... = SU Beamformee Capable: Supported        <<<<-----|| SINGLE USER (SU) BEAMFORMER CAPABLE
                .... .... .... .... 011. .... .... .... = Beamformee STS Capability: 4 (0x3)    
                .... .... .... .001 .... .... .... .... = Number of Sounding Dimensions: 2 (0x1)  <<<<-----|| 2 sounding dimentions
                .... .... .... 0... .... .... .... .... = MU Beamformer Capable: Not supported    <<<<-----|| MULTI USER (MU) BEAMFORMER NON-CAPABLE
                .... .... ...0 .... .... .... .... .... = MU Beamformee Capable: Not supported    <<<<-----|| MULTI USER (MU) BEAMFORMER NON-CAPABLE
                .... .... ..0. .... .... .... .... .... = TXOP PS: Not supported
                .... .... .1.. .... .... .... .... .... = +HTC-VHT Capable: Supported
                .... ..11 1... .... .... .... .... .... = Max A-MPDU Length Exponent: 1 048 575 (0x7)
                .... 00.. .... .... .... .... .... .... = VHT Link Adaptation: No Feedback (0x0)
                ...0 .... .... .... .... .... .... .... = Rx Antenna Pattern Consistency: Not supported
                ..0. .... .... .... .... .... .... .... = Tx Antenna Pattern Consistency: Not supported
                01.. .... .... .... .... .... .... .... = Extended NSS BW Support: 0x1

            VHT Supported MCS Set
        Tag: VHT Operation
````

---

### `Probe Request & (Re)Association Request` : `STA Beamforming Capabilities`

- Sent from the `Beamformer / Beamformee / STA` to `AP`
- Probe Request & (Re)Association Request include the HT Capabilities and VHT Capabilities tags, which signal beamforming capabilities and support in 802.11n/ac networks. 
- These fields indicate whether a STA (Station) can perform transmit beamforming, receive beamforming, and related operations.

````java

802.11 radio information
IEEE 802.11 Association Request, Flags: ........
IEEE 802.11 Wireless Management
    Fixed parameters (4 bytes)
    Tagged parameters (204 bytes)
        Tag: SSID parameter set: "Fz3r0 💀🎩"

        Tag: HT Capabilities (802.11n D1.10)
            Tag Number: HT Capabilities (802.11n D1.10) (45)
            Tag length: 26
            HT Capabilities Info: 0x096f
            A-MPDU Parameters: 0x13
            Rx Supported Modulation and Coding Scheme Set: MCS Set
            HT Extended Capabilities: 0x0000
            Transmit Beam Forming (TxBF) Capabilities: 0x00000000
                .... .... .... .... .... .... .... ...0 = Transmit Beamforming: Not supported
                .... .... .... .... .... .... .... ..0. = Receive Staggered Sounding: Not supported
                .... .... .... .... .... .... .... .0.. = Transmit Staggered Sounding: Not supported
                .... .... .... .... .... .... .... 0... = Receive Null Data packet (NDP): Not supported
                .... .... .... .... .... .... ...0 .... = Transmit Null Data packet (NDP): Not supported
                .... .... .... .... .... .... ..0. .... = Implicit TxBF capable: Not supported
                .... .... .... .... .... .... 00.. .... = Calibration: incapable (0x0)
                .... .... .... .... .... ...0 .... .... = STA can apply TxBF using CSI explicit feedback: Not supported
                .... .... .... .... .... ..0. .... .... = STA can apply TxBF using uncompressed beamforming feedback matrix: Not supported
                .... .... .... .... .... .0.. .... .... = STA can apply TxBF using compressed beamforming feedback matrix: Not supported
                .... .... .... .... ...0 0... .... .... = Receiver can return explicit CSI feedback: not supported (0x0)
                .... .... .... .... .00. .... .... .... = Receiver can return explicit uncompressed Beamforming Feedback Matrix: not supported (0x0)
                .... .... .... ...0 0... .... .... .... = STA can compress and use compressed Beamforming Feedback Matrix: not supported (0x0)
                .... .... .... .00. .... .... .... .... = Minimal grouping used for explicit feedback reports: No grouping supported (0x0)
                .... .... ...0 0... .... .... .... .... = Max antennae STA can support when CSI feedback required: 1 TX antenna sounding (0x0)
                .... .... .00. .... .... .... .... .... = Max antennae STA can support when uncompressed Beamforming feedback required: 1 TX antenna sounding (0x0)
                .... ...0 0... .... .... .... .... .... = Max antennae STA can support when compressed Beamforming feedback required: 1 TX antenna sounding (0x0)
                .... .00. .... .... .... .... .... .... = Maximum number of rows of CSI explicit feedback: 1 row of CSI (0x0)
                ...0 0... .... .... .... .... .... .... = Maximum number of space time streams for which channel dimensions can be simultaneously estimated: 1 space time stream (0x0)
                000. .... .... .... .... .... .... .... = Reserved: 0x0
            Antenna Selection (ASEL) Capabilities: 0x00

        Tag: VHT Capabilities
            Tag Number: VHT Capabilities (191)
            Tag length: 12
            VHT Capabilities Info: 0x33807132
                .... .... .... .... .... .... .... ..10 = Maximum MPDU Length: 11 454 (0x2)
                .... .... .... .... .... .... .... 00.. = Supported Channel Width Set: Neither 160MHz nor 80+80 supported (0x0)
                .... .... .... .... .... .... ...1 .... = Rx LDPC: Supported
                .... .... .... .... .... .... ..1. .... = Short GI for 80MHz/TVHT_MODE_4C: Supported
                .... .... .... .... .... .... .0.. .... = Short GI for 160MHz and 80+80MHz: Not supported
                .... .... .... .... .... .... 0... .... = Tx STBC: Not supported
                .... .... .... .... .... .001 .... .... = Rx STBC: 1 Spatial Stream Supported (0x1)
                .... .... .... .... .... 0... .... .... = SU Beamformer Capable: Not supported
                .... .... .... .... ...1 .... .... .... = SU Beamformee Capable: Supported        <<<<-----|| SINGLE USER (SU) BEAMFORMER CAPABLE
                .... .... .... .... 011. .... .... .... = Beamformee STS Capability: 4 (0x3)
                .... .... .... .000 .... .... .... .... = Number of Sounding Dimensions: 1 (0x0)  <<<<-----|| 1 sounding dimention
                .... .... .... 0... .... .... .... .... = MU Beamformer Capable: Not supported   
                .... .... ...0 .... .... .... .... .... = MU Beamformee Capable: Not supported    <<<<-----|| MULTI USER (MU) BEAMFORMER NON-CAPABLE
                .... .... ..0. .... .... .... .... .... = TXOP PS: Not supported
                .... .... .0.. .... .... .... .... .... = +HTC-VHT Capable: Not supported
                .... ..11 1... .... .... .... .... .... = Max A-MPDU Length Exponent: 1 048 575 (0x7)
                .... 00.. .... .... .... .... .... .... = VHT Link Adaptation: No Feedback (0x0)
                ...1 .... .... .... .... .... .... .... = Rx Antenna Pattern Consistency: Supported
                ..1. .... .... .... .... .... .... .... = Tx Antenna Pattern Consistency: Supported
                00.. .... .... .... .... .... .... .... = Extended NSS BW Support: 0x0
            VHT Supported MCS Set


````

---

### `NDP Announcement` (VHT/HE/EHT/RANGING)

- Sent from the `Beamformer / AP` to the `Beamformee / client STA`
- An NDP (Null Data Packet) Announcement Frame is a control frame (Type/Subtype 0x0015) used to prepare for beamforming measurements.
- The NDP Announcement is sent by the AP and signals the client STAs to prepare for transmitting feedback based on a Null Data Packet, which is sent immediately after the announcement. 
- It initiates the sounding process for channel state information (CSI) feedback.

````java
Frame 6407: 75 bytes on wire (600 bits), 75 bytes captured (600 bits)
Radiotap Header v0, Length 56
802.11 radio information
IEEE 802.11 VHT/HE/EHT/RANGING NDP Announcement, Flags: ........
    Type/Subtype: VHT/HE/EHT/RANGING NDP Announcement (0x0015)
    Frame Control Field: 0x5400
        .... ..00 = Version: 0
        .... 01.. = Type: Control frame (1)
        0101 .... = Subtype: 5
        Flags: 0x00
    .000 0000 0111 0100 = Duration: 116 microseconds
    Receiver address: Android.local (3c:13:5a:f2:46:88)
    Transmitter address: AP-Huawei (50:4e:dc:90:2e:bd)
    Sounding Dialog Token: 0x84 VHT NDP Announcement                       
        .... ..00 = NDP Announcement Variant: VHT NDP Announcement (0x0)    <<<<----|| VHT NDP Announcement
        1000 01.. = Sounding Dialog Token: 0x21
    STA list
        STA 0
            .... 0000 0000 0010 = AID12: 0x002                              <<<<----|| Association ID for each STA
            ...0 .... .... .... = Feedback Type: SU feedback requested      <<<<----|| SU Feedback requested @ the client STA)
            .... .... .... .... 000. .... .... .... = Reserved: 0x0
    [WLAN Flags: ........]

````

- NDP Announcement (VHT/HE/EHT/RANGING) // `wlan.fc.type_subtype == 0x0015`

---

### `Action No ACK - VHT 802.11ax` - `VHT Compressed Beamforming` : `Average SNR` & `Feedback Matrcies`

- Sent from the `Beamformee / client STA` to the `Beamformer / AP`
- The Action No ACK frame with VHT Compressed Beamforming is a management frame (Type/Subtype 0x000e) that conveys `CSI feedback` from a STA to the AP.
- This frame **enables the AP to adjust beamforming** based on the `CSI feedback`, improving signal strength and spatial multiplexing efficiency.

````java

802.11 radio information
IEEE 802.11 Action No Ack, Flags: ........
    Type/Subtype: Action No Ack (0x000e)
    Frame Control Field: 0xe000
        .... ..00 = Version: 0
        .... 00.. = Type: Management frame (0)
        1110 .... = Subtype: 14
        Flags: 0x00

    Receiver address:     AP-Huawei 
    Destination address:  AP-Huawei 
    Transmitter address:  STA-Android 
    Source address:       STA-Android 
    BSS Id:               AP-Huawei

IEEE 802.11 Wireless Management
    Fixed parameters
        Category code: VHT (21)
        VHT Action: VHT Compressed Beamforming (0)                <<<<----||

        VHT MIMO Control: 0x848488, Nc Index: 1 Column, Nr Index: 2 Rows, Channel Width: 80 MHz, Grouping (Ng): 1 (No Grouping), Feedback Type: SU
            .... .... .... .... .... .000 = Nc Index: 1 Column (0x0)
            .... .... .... .... ..00 1... = Nr Index: 2 Rows (0x1)
            .... .... .... .... 10.. .... = Channel Width: 80 MHz (0x2)
            .... .... .... ..00 .... .... = Grouping (Ng): 1 (No Grouping) (0x0)
            .... .... .... .1.. .... .... = Codebook Information: 0x1
            .... .... .... 0... .... .... = Feedback Type: SU (0x0)
            .... .... .000 .... .... .... = Remaining Feedback Segments: 0x0
            .... .... 1... .... .... .... = First Feedback Segments: 0x1
            .... ..00 .... .... .... .... = Reserved: 0x0
            1000 01.. .... .... .... .... = Sounding Dialog Token Number: 0x21

        VHT Compressed Beamforming Report […]: 4ff3c8324f3cf3cc238f3cf3cc33cf3cf3cc330f3df3cc33cf3cf4d0430f4d34d144134d34d154534d35d554535d75d555575d75d555575d75d555976db6d5569b6db6d9669b6db6d9669b7df6d9679f7df6d9779f7df6d968a38d36da68a38d37da69
            Average Signal to Noise Ratio                        <<<<----|| Average SNR sent fron the STA to the AP
                Stream 1 - Signal to Noise Ratio:  41.75dB
            Feedback Matrices                                    <<<<----|| Feedback Matrices sent fron the STA to the AP
                SCIDX: -122, φ11:51, ψ21:3
                SCIDX: -121, φ11:50, ψ21:2
                SCIDX: -120, φ11:51, ψ21:3
                SCIDX: -119, φ11:49, ψ21:3
                SCIDX: -118, φ11:51, ψ21:3
                SCIDX: -117, φ11:51, ψ21:3
                SCIDX: -113, φ11:51, ψ21:3
                SCIDX: -112, φ11:51, ψ21:3
                SCIDX: -111, φ11:51, ψ21:3
                SCIDX: -110, φ11:51, ψ21:3
                SCIDX: -109, φ11:51, ψ21:3
                SCIDX: -108, φ11:51, ψ21:3
                SCIDX: -101, φ11:52, ψ21:3
                SCIDX: -100, φ11:52, ψ21:3
                SCIDX: -99, φ11:52, ψ21:3
                SCIDX: -98, φ11:52, ψ21:4
                SCIDX: -97, φ11:52, ψ21:4
                SCIDX: -96, φ11:52, ψ21:4
                SCIDX: -95, φ11:52, ψ21:4
                SCIDX: -88, φ11:53, ψ21:4
                SCIDX: -87, φ11:53, ψ21:4
                SCIDX: -86, φ11:53, ψ21:5
                SCIDX: -85, φ11:53, ψ21:5
                .
                .
                .
                .
      
````

- wlan.vht.action == 0






## Steps for Beamforming

A summary of the steps to enable beamforming is:

1. The `beamformer` transmits a `Null Data Packet (NDP) Announcement` frame which identifies `beamformees`.
2. This is then followed by another `NDP` frame which is a `sounding frame` used by the receiver to analyse training fields for various subcarriers and calculates a response.
3. This `response` from the `beamformee` contains a `feedback matrix`.
4. The `beamformer` uses the `feedback matrix` to calculate a steering matrix to direct RF energy toward the beamformee.

































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


