
# 🙋🛜🚦MAC Operations: `Protection Mechanisms`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)  || 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Networking` `Wireless Networking` `IEEE 802.11` `Wi-Fi` `CWNA` `CWAP` `CWNE` `CCNP` `MAC Operations` `Protection Mechanisms` `RTS/CTS` `CTS-to-Self`

---

<br>

# Index

### [🙋🛜🚦MAC Operations: `Protection Mechanisms`]()

### [🙋🛜🚦 `Protection Mechanisms`]()

- [Background Concepts: `Hidden Node`]()
- [Background Concepts: `Duration Field`]()


# 🙋🛜🚦MAC Operations: `Protection Mechanisms`

There are 2 types of MAC Operations: **Power Management** & **Protection Mechanisms**:

1. **`Power Management`** is allow the radio to go to sleep (just few microseconds), because if the antenna/adapter keeps awake all the time is consuming battery all the time, in a movile device can degrade battery life. Power management it's just turning on the antenna, send/recieve the frame, then "doze" or "sleep" the antenna and so on. The hint here is, that the STA does not lose any frame even if it's sleeping <br><br>
2. **`Protection Mechanisms`** Allow newer devices to communicate and "exist" in a world where older devices also exists (eg. devices using 802.11b(HR-DSSS) can coexist with newer devices using 802.11g(ERP) or even newest devices like 802.11n/ac/ax(OFDM)) || Protect from the "Hidden Node" problems in 802.11 Wi-Fi Networks. || Determine when the Wi-Fi Channel is available for access using CSMA/CA. 

# 🙋🛜🚦 `Protection Mechanisms`

In IEEE 802.11 Wi-Fi Networks, the **Protection Mechanisms** are used for 3 main purposes: 

### 1. `Backward Compatibility`

802.11 (Wi-Fi) networks are designed to support backward compatibility across different generations (e.g., Wi-Fi 4 (802.11n) is backward compatible with Wi-Fi 1 or Wi-Fi 3 (802.11b/g)). This feature is a significant reason for the technology's popularity, as it allows users to upgrade their devices at their own pace without compromising the functionality of older ones.

Legacy HR/DSSS (802.11b, Wi-Fi 1) STAs are incapable of interpreting the OFDM modulation used by ERP (802.11g, Wi-Fi 3) devices. However, modern HT/ERP/OFDM stations (802.11n, Wi-Fi 4) are designed with backward compatibility in mind, enabling them to communicate using HR/DSSS modulation to support legacy devices. 

This backward compatibility is managed through Protection Mechanisms (eg. RTS/CTS or CTS-to-Self), which are utilized when both legacy and modern STAs are connected to the same AP. These mechanisms help ensure that legacy devices, which are unable to understand modern modulations, can coexist and communicate efficiently without causing interference or transmission collisions.

**`Important`**: Backward compatibility in Wi-Fi has traditionally been a source of inefficiencies for modern STAs sharing the same BSS with legacy devices, causing issues such as RTS/CTS overhead, increased airtime usage, and connectivity degradation. However, with Wi-Fi 6E and the introduction of the 6 GHz band, backward compatibility is no longer required. Legacy protection mechanisms like RTS/CTS are unnecessary _(at least for backward compatibility, hidden node problem still persist)_, as there are no legacy devices operating in this band, eliminating the inefficiencies caused by slower data rates. Although future generations (e.g., Wi-Fi 7, Wi-Fi 8) may reintroduce backward compatibility if they continue to utilize the 6 GHz band, the current environment remains free from legacy constraints.

### 2. `Hidden Node Problem Protection`

In wireless networking, the hidden node problem or hidden terminal problem occurs when a node can communicate with a wireless access point (AP), but cannot directly communicate with other nodes that are communicating with that AP.[1] This leads to difficulties in medium access control sublayer since multiple nodes can send data packets to the AP simultaneously, which creates interference at the AP resulting in no packet getting through.

Practical protocol solutions exist to the hidden node problem. For example, Request To Send/Clear To Send (RTS/CTS) mechanisms where nodes send short packets to request permission of the access point to send longer data packets. Because responses from the AP are seen by all the nodes, the nodes can synchronize their transmissions to not interfere. However, the mechanism introduces latency, and the overhead can often be greater than the cost, particularly for short data packets.

### 3. `Determine wireless Channel availability`

RTS (Request to Send) and CTS (Clear to Send) signals are mainly used in CSMA/CA to have co-ordinate access to the channel, and making sure that only one node or device sends data at a time to prevent the collisions

Steps demonstrating in a basic manner how RTS/CTS mechanism is used to avoid collision in CSMA/CA

- Step 1: Channel Checking - Firstly, before sending the data, the device using CSMA/CA first checks if the channel is idle or not.
- Step 2: RTS Frame - When the channel becomes in the idle state, the actual transmission device sends the RTS frame to the destination receiving devices. This RTS frame includes the actual length of the data packet, which is to be send.
- Step 3: CTS Response - When the ITS frame is received, the CTS frame back since this receiving signal back to the RTS frame.
- Step 4: Data Transmission - RTS data is been received to the CTS frame. The transmitting device processes to send the actual data packet. These transmission occurs without encountering any collisions on the other devices have been informed to defer their transmission during this transmission time.
- Step 5: Backoff Mechanism - If there is any collision, then the pack of mechanism is used in. this mechanism, the colliding devices wait for the random duration of time before attempting to retransmit the data.
- Step 6: Repeat Process -  The RTS and CTS processes are repeated till each of the data transmission is completed and also helps in minimizing the collisions in CSMA/CA based networks.

**`Important`**: RTS/CTS is the most used mechanism in Wi-Fi, there's also a mechanism called CTS-to-self that is not a frame defined in the standard, this frame is a CTS frame without a preciding RTS frame.

## 🙋🛜🚦 Background Concepts: `Hidden Node`

**RTS/CTS (Request-to-Send / Clear-to-Send)** is the most used mechanism in Wi-Fi; this mechanism is an optional method that is used in `Virtual Carrier Sense` to avoid `hidden node` problems. So... To understand RTS/CTS we must understand what is `hidden node` problems first.

**The diagram below explain the Hidden Node Problem:**

- `AP Node`: Represent the **AP** in the center of the BSA/BSS where all the other nodes (STA) connect for Tx/Rx.
- `Alice Node`: Represent the **client STA "A"** within the AP wireless network.
- `Bob Node`: Represent the **client STA "B"** within the AP wireless network.

**Hidden Node Problem:**

- The `AP` can hear `Alice` within the BSA/BSS network cell. 
- The `AP` can hear `Bob` within the BSA/BSS network cell.
- The `AP` can hear `Carl` within the BSA/BSS network cell. 
- But, `Bob` & `Carl` **CAN'T HEAR** `Alice` due to network congestion or because she is outside of other's radio cell. **In this scenario, `Alice` is the hidden node**.

![image](https://github.com/user-attachments/assets/92e90cf0-ffb4-4876-b241-c5308904c55a)

Due to this, `Physical Carrier Sense` (CSMA/CA) by `Alice` & `Bob/Carl` **will never indicate that medium is busy** when either one of them is transmitting in the air and could result in corruption and distortion of signal. **To avoid this situation, we can use `RTS/CTS` mechanism:**

![image](https://github.com/user-attachments/assets/8aa1ca74-2c87-438e-ae6f-66deac50d1d0)

- Any 802.11 device that wishes to transmit in the medium should send `RTS (Request to Send)` frame **requesting for medium access to the AP**.
- When the `RTS` sent by **Alice STA** is received by the **AP**, it will respond with a `CTS` _(if the medium is idle)_, to indicate to **Alice STA** that she can transmit the data frame.
- The `CTS` frame includes the `Duration/ID` field, which helps other STAs (eg. **Bob & Carl STAs**) within the BSS to set its `NAV` timer. 
- If **Bob & Carl STAs** or another STA in the BSS could not "hear" the original `RTS` sent by **Alice STA**, **it may hear the `CTS` broadcasted by the AP** which includes a `Duration/ID` field, then, they can **adjust its `NAV` timer to the `Duration` set in `CTS` frame**.

## 🙋🛜🚦 Background Concepts: `RTS/CTS MAC Frames`

An 802.11 `RTS (Request to Send)` and `CTS (Clear to Send)` frame are `Control Frames` used in Wi-Fi networks to **prevent collisions**. These frames are part of the Distributed Coordination Function (DCF) which uses **CSMA/CA**. 

- `RTS` is sent by a device to **request access to the medium**.
- `CTS` **is the response, granting permission**. 

Since these `RTS/CTS` are **broadcast**, all STAs within the BSS can "hear" them, which helps manage medium access. STAs that "hear" the `RTS/CTS` frames update their `NAV (Duration)` timers to stay silent, while the transmitting STA proceeds with its transmission.

### RTS/CTS MAC Frames: `RTS (Request to Send)`

- An 802.11 RTS (Request to Send) frame is a control frame used to **reserve the medium before transmitting data**.
- This process helps avoid collisions by signaling the intention to transmit data into the channel.
- It includes the `Duration` of the upcoming transmission **AFTER the RTS**.

#### RTS (Request to Send): `Addresses`

- `Receiver Address`: (eg. **F0:F0:F0:F0:F0:F0**) :: The device **being asked to access** the medium (eg. **AP**)
- `Transmiter Address`: (eg. **AA:AA:AA:AA:AA:AA**) :: The device **requesting the access** to the medium. (eg. **Alice STA**)  

### RTS (Request to Send): `Frame`

````sh
# Request-to-Send Frame

802.11 radio information
IEEE 802.11 Request-to-send, Flags: ........
    Type/Subtype: Request-to-send (0x001b)
    Frame Control Field: 0xb400
        .... ..00 = Version: 0
        .... 01.. = Type: Control frame (1)  <<<---| Type:    Control Frame   = 01
        1011 .... = Subtype: 11              <<<---| SubType: Request-to-Send = 11
        Flags: 0x00
    .000 0000 1011 1000 = Duration: 184 microseconds            <<<<<-----|| Duration/ID field
    Receiver address: f0:f0:f0:f0:f0:f0 (f0:f0:f0:f0:f0:f0)     <<<<<-----|| Receiver Address (AP)
    Transmitter address: aa:aa:aa:aa:aa:aa (aa:aa:aa:aa:aa:aa)  <<<<<-----|| Transmitter Address (Alice)
    [WLAN Flags: ........]
````
| **Field**                        	| **Description**                                                                                                                           	| **Wireshark Filter**                                                           	|
|----------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------	|
| **Request-to-Send (RTS Frames)** 	| Control frame used by a STA to request access to the medium, preventing collisions.                                                       	| `wlan.fc.type == 1 && wlan.fc.subtype == 11`                                   	|
| **RTS Duration**                 	| Indicates the time (in microseconds) other STAs within the channel should remain silent during the transmission period **AFTER the RTS**. 	| `wlan.fc.type == 1 && wlan.fc.subtype == 11 && (wlan.duration == 140)`         	|
| **RTS Receiver Address (RA)**    	| WLAN Address of the **STA being requested** for medium access, **usually the AP**.                                                        	| `wlan.fc.type == 1 && wlan.fc.subtype == 11 && (wlan.ra == f0:f0:f0:f0:f0:f0)` 	|
| **RTS Transmitter Address (RA)** 	| Wlan Address of the **STA requesting** access to transmit, **typically a client STA**. (eg. **Alice**, **Bob** or **Carl**)               	| `wlan.fc.type == 1 && wlan.fc.subtype == 11 && (wlan.ta == aa:aa:aa:aa:aa:aa)` 	|

### RTS/CTS MAC Frames: `CTS (Clear to Send)`

- Sent by a 802.11 device (typically AP) in **response to a RTS frame from another device** _(it can also be sent by the own device in a **CTS-to-self** enviorment)_.
- Its primary purpose is to indicate that the medium is clear and that the requesting device can transmit its data without interference.
- This process helps avoid collisions by signaling the intention to transmit data into the channel.
- It includes the `Duration` of the upcoming transmission **AFTER the CTS**.

#### CTS (Request to Send): `Addresses`

- `Receiver Address`: (eg. **AA:AA:AA:AA:AA:AA**) :: STA that **sent the RTS in first place requesting access** to transmit, and **is now being granted access to transmit**.(eg. **Alice STA**)

**`Important`**: Just like an `ACK` frame, the `CTS` frame **only includes the Receiver Address** because its sole purpose is to grant permission for the **requesting device** to transmit. The `CTS` frame is sent by the device that received the RTS (e.g., the `AP`) and is broadcast to inform all other stations within the BSS to stay silent (eg. `Bob` or `Carl`). Since the **CTS is a response to the RTS**: **the receiver of the CTS is the same device that sent the original RTS**, so only the Receiver Address (the requester) is needed in the CTS frame.

The CTS frame functions similarly to an ACK frame, (both only include the Receiver Address and do not contain a Transmitter Address). Therefore, there is no need for an ACK frame after an RTS; in other words: 

- **The `CTS` serves as the `ACK` for an `RTS`**.

### CTS (Request to Send): `Frame`

````sh
# Clear-to-Send Frame

802.11 radio information
IEEE 802.11 Clear-to-send, Flags: ........
    Type/Subtype: Clear-to-send (0x001c)
    Frame Control Field: 0xc400
        .... ..00 = Version: 0
        .... 01.. = Type: Control frame (1)  <<<---| Type:    Control Frame = 01
        1100 .... = Subtype: 12              <<<---| SubType: Clear-to-Send = 12
        Flags: 0x00
    .000 0000 1000 1100 = Duration: 140 microseconds          <<<<<------|| Duration/ID field
    Receiver address: aa:aa:aa:aa:aa:aa (aa:aa:aa:aa:aa:aa)   <<<<<------|| Receiver Address (Alice)
    [WLAN Flags: ........]

````
| **Field**                      | **Description**                                                                                                                                        | **Wireshark Filter**                                                           |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Clear-to-Send (CTS Frames)** | Control frame used to clear the medium for the requesting 802.11 node **AFTER receiving an RTS**.                                                      | `wlan.fc.type == 1 && wlan.fc.subtype == 12`                                   |
| **CTS Duration**               | Indicates the time (in microseconds) other STAs within the channel should remain silent during the transmission period **AFTER the CTS**.              | `wlan.fc.type == 1 && wlan.fc.subtype == 12 && (wlan.duration == 140)`         |
| **CTS Receiver Address (RA)**  | WLAN Address of the **STA that sent the RTS in first place requesting access to transmit, and is now being granted access to transmit**. (eg. Alice)   | `wlan.fc.type == 1 && wlan.fc.subtype == 12 && (wlan.ra == aa:aa:aa:aa:aa:aa)` |




## 🙋🛜🚦 Background Concepts: `ACK`

An **ACK (Acknowledgment)** frame is a `Control Frame` used in wireless networks (like 802.11 Wi-Fi) to confirm the **successful receipt** of **unicast**: `data`, `management`, `PS-Poll` and `fragmented` frames.

- **The primary purpose of an `ACK` frame is to notify the `Transmitter (TA)` that their transmitted data frame has been successfully received by the intended `Receiver (RA)`.**
- **If the `CRC` check of the data frame fails because the frame is corrupted or the data frame is not received, the `Receiver (RA)` will not send an `ACK`.
- **If the `Transmitter (TA)` of the data frame does not receive an `ACK` from the `Receiver (RA)`, it will `retransmit` the data frame until is ACKed _(or reach max transmission attempts)_.****

### ACK: `Frame Exchange`

![image](https://github.com/user-attachments/assets/cf632b58-bdd1-4b2a-bd24-0d2f53852ae5)

1. When a 802.11 device (eg. `Alice (STA)`) wants to send data to another device (eg. `AP`), it first transmits the `data frame`.
2. Once the `AP` receives the data frame, it checks the integrity of the received data (using `CRC` error-checking methods).
3. If the data frame is received correctly, the `AP` sends an `ACK` frame back to `Alice`.
4. Process repeats until the end of the transmission.
5. `Timeout`: If `Alice (STA)` does not receive an `ACK` within a certain timeframe from the `AP` _(eg. due to network issues or collisions)_, she will assume that the data frame was lost and will `retransmit` the data.

### ACK: `Address` 

The ACK frame only includes the Receiver Address because its sole purpose is to acknowledge the successful reception of a data frame. The ACK frame is sent by the device that successfully received the data (e.g., the AP or Bob) and is transmitted directly back to the original sender (e.g., Carl). Since the ACK is a response to the data frame, the receiver of the ACK is the same device that sent the original data frame, so only the Receiver Address (the sender) is needed in the ACK frame.

- **The `Receiver Address (RA)` is copied from the `Transmitter` of the frame being ACKed. Technically, it is copied from the `Address 2 (Transmitter Address TA)` field of the frame being acknowledged _(eg. Alice STA)_.**

### ACK: `Duration`

The time required to transmit the ACK and its short interframe space is subtracted from the duration in the most recent fragment. The duration calculation in nonfinal ACK frames is similar to the CTS duration calculation. In fact, the 802.11 specification refers to the duration setting in the ACK frames as a virtual CTS.

Duration **BEFORE** an `ACK` frame (eg. a Data Frame) use to be `44 μS` or  `304 μS` (time for a `ACK` + `SIFS`) depending on the PHY.  The `Duration` field of an `ACK` frame **will always be = `0 μS`**

- **802.11b = `1 Mbps` Data Rate = `304 μS`** 
- **802.11a/g/n/ac/ax = `6 Mbps` Data Rate = `44 μS`**
- **ACK =  `0 μS`**

### ACK: `QoS & EDCA`

Quality-of-service enhancements relax the requirement for a single acknowledgment per Data frame.

### ACK: `Frame`

````sh
# ACK Frame

802.11 radio information
IEEE 802.11 Acknowledgement, Flags: ........C
    Type/Subtype: Acknowledgement (0x001d)
    Frame Control Field: 0xd400
        .... ..00 = Version: 0
        .... 01.. = Type: Control frame (1)  <<<---| Type:     Control Frame = 01
        1101 .... = Subtype: 13              <<<---| SubType:  ACK Frame = 13
        Flags: 0x00
    .000 0000 0000 0000 = Duration: 0 microseconds           <<<<<------|| Duration = 0 μS
    Receiver address: f0:f0:f0:f0:f0:f0 (f0:f0:f0:f0:f0:f0)  <<<<<------|| Receiver Address (AP)
    Frame check sequence: 0x011125d9 [correct]               <<<<<------|| CRC Check Sequence
    [FCS Status: Good]                                       <<<<<------|| CRC Check = OK! (wireshark auto calculation)
    [WLAN Flags: ........C]
````
| **Field**                              	| **Description** 	| **Wireshark Filter**                                                            	|
|----------------------------------------	|-----------------	|---------------------------------------------------------------------------------	|
| **Acknowledgement Frame**              	|                 	| `wlan.fc.type == 01 && wlan.fc.subtype == 13`                                   	|
| **ACK Duration**                       	|                 	| `wlan.fc.type == 01 && wlan.fc.subtype == 13 && (wlan.duration == 0)`           	|
| **ACK Receiver Address (RA)**          	|                 	| `wlan.fc.type == 01 && wlan.fc.subtype == 13 && (wlan.ra == aa:aa:aa:aa:aa:aa)` 	|
| **ACK FCS (Frame Check Sequence)**     	|                 	| `wlan.fc.type == 01 && wlan.fc.subtype == 13 && (wlan.fcs == 0x011125d9)`       	|
| **Good CRC (Cyclic Redundancy Check)** 	|                 	| `wlan.fc.type == 01 && wlan.fc.subtype == 13 && (wlan.fcs.status == "Good")`    	|
| **Bad CRC (Cyclic Redundancy Check)**  	|                 	| `wlan.fc.type == 01 && wlan.fc.subtype == 13 && (wlan.fcs.status == "Bad")`     	|





## 🙋🛜🚦 Background Concepts: `Duration/ID`

**The `Duration/ID` field in a Mac Header has a two different purposes:**

1. `Duration`: <br><br>
    - Determine the **time in microseconds (μs)** needed to complete the Frame Exchange. This is measured **AFTER the current frame**, this means: what is left after the current frame.
    - This field is used to reset NAV (Network Allocation Vector) timers for all other 802.11 Wi-Fi devices (STAs) on the same channel.
    - This is used a lot and it's important to know that this is not the duration of the current frame, **it is the duration of the exchanges after the current frame requeried to actually complete the transaction**. <br><br>
2. `ID`:  <br><br>
    - Used in **legacy PS-poll** Frame to indicate the **AID (Association ID)** of the **STA** to send the buffered frame in the AP when using `Legacy 802.11 Power Management`. _(This is not used for Protection Mechanisms)._

**There are 3 different main `Duration` values types:**

| **Type**                                             | **Duration Value**            | **Description**                                                                 |
|------------------------------------------------------|-------------------------------|---------------------------------------------------------------------------------|
| 1. **Data Exchange / Block ACK / RTS Data Exchange** _(No protection)_   | `SIFS`+`Ack`                  | Involves a SIFS followed by an ACK. **No Protection Mechanism in use.**         |
| 2. **RTS/CTS Data Exchange**                         | `x3 SIFS`+`CTS`+`Data`+`ACK`  | Uses **RTS/CTS** frame exchange, which involves: RTS +: three SIFS, CTS, Data & ACK frames.  |
| 3. **CTS-to-Self Data Exchange**                     | `x2 SIFS`+`Data`+`ACK`        | Uses **CTS-to-Self** frame exchange, which involves: CTS +: two SIFS, CTS, Data & ACK frames.|

### Duration Value Types: 1. `Data Exchange / Block ACK / RTS Data Exchange (No protection)`

In a `Data Exchange` scenario the `Duration` is equal the exchange **AFTER** the `Data Frame`.

- **Duration** = **`SIFS` + `ACK`**

![image](https://github.com/user-attachments/assets/e1a2f979-ce09-4592-9a13-98d9ebaa5584)

### Duration Value Types: 2. `RTS/CTS Data Exchange`

In a `Data Exchange` where `RTS/CTS` is used, Duration is equal the exchange **AFTER** the `RTS Frame`:

- **Duration** = **`x3 SIFS` + `CTS` + `Data` + `ACK`**

![image](https://github.com/user-attachments/assets/9dc5f45c-9da8-4e79-8ae3-89d6be50e69a)

### Duration Value Types: 3. `CTS-to-Self Data Exchange`

In a `Data Exchange` where `CTS-to-Self` is used, Duration is equal the exchange **AFTER** the `CTS Frame`:

- **Duration** = **`x2 SIFS` + `Data` + `ACK`**

![image](https://github.com/user-attachments/assets/2585151a-849f-47b9-a42d-dc39edf940be)


Once the medium is free, the client STA can access the medium for wireless transmissions. For every frame transmitted in air, there should be an ACK from the AP. There is a SIFs delay between each frame: RTS, CTS, DATA and ACK frames. At times, this mechanism can create a lot of overhead in the network leading to a lot of congestion. And hence, this can be enabled only if the frame size is equal or above a specific configured threshold that depends on the network.

## 🙋🛜🚦 Background Concepts: `Virtual Carrier Sense` : `NAV`

**Virtual Carrier Sense** is a mechanism used in IEEE 802.11 (Wi-Fi) networks to **avoid collisions** and **ensure efficient use of the medium** using information of the MAC Frame Headers: `Duration` field **(NAV)**. 

Unlike **Physical Carrier Sense**, which relies on detecting actual transmissions at the physical layer, **Virtual Carrier Sense** uses information contained in the `MAC Frame Header > Duration` to predict future traffic on the medium. 

The two key components of Virtual Carrier Sense are:

1. **`Duration Field`** <br><br>
    - **Purpose**: Indicates the amount of time (in microseconds) that the channel will be occupied by the current frame exchange sequence. 
    - **Mechanism**: The Duration Field is included in the **Frame Control of the MAC header**. It specifies how long the transmitting station expects to use the medium, including any acknowledgment frames that may be sent in response. **The Duration Field indicated how much time on the medium is going to be requerid to transmit THE REST of the frames requiered in a 802.11 frame exchange. (eg. if it is a CTS frame the duration field will be THE REST of the exchange: 2 SIFS, Data Frame, 3 ACKs).**
    - **Usage**: Other stations in the network demodulate the 802.11 frame and **read the Duration Field in the MPDU** and update their **NAV Timer** accordingly to avoid transmitting during the specified period. The stations will update the timer until it reach 0, **when NAV = 0 then stations will try to comunicate _(but before stations need to complete IFS & Backoff timer processes)_. If a station can't demodulate the MPDU, then they will measure the medium using Physical Carrier Sense.** 
    - **Important**: **NAV is only updated when the Duration value is greater than the current NAV value.** <br><br>
2. **`Network Allocation Vector (NAV)`** <br><br>
    - **Purpose**: Acts as a timer that represents the period during which the medium is expected to be busy, based on the Duration Field values from received frames.
    - **Mechanism**: When a station receives a frame with a Duration Field, it sets its NAV timer to the value specified in the Duration Field if this value is greater than the current NAV value. This prevents the station from attempting to access the medium until the NAV timer expires.
    - **Impact**: The NAV helps manage medium access by providing a way for stations to reserve the medium for a certain period, reducing the likelihood of collisions.
    - **Important**: **While NAV is not equal to "0", stations presume that the medium is busy and will not transmit.**

Important Notes on Duration Field:

- 802.11 management frames that are sent to a broadcast address of FF:FF:FF:FF:FF:FF will have a duration value of zero. The duration is a time value that STA’s will use to reserve the medium informing other STA’s in the BSS how long it will take for the frame exchange to complete. In this case since these frames are no acknowledged by a receiver they have a duration value of zero. The duration field is still in the MAC header but it is not used.

**⭕ Duration Field Filter:**

- 🦈 **Duration Field = 0** :: NAV 0 : `wlan.duration == 0`
- 🦈 **Duration Field more than 0** :: NAV > 0 : `wlan.duration > 0`
  
**IMPORTANT:** In Wireshark (or any other protocol analyzer), the Network Allocation Vector (NAV) is not directly displayed as a single field because it is a conceptual timer maintained by each station based on the Duration Field found in the MAC header of 802.11 frames. However, you can infer the NAV by examining the Duration Field of the frames. By inspecting the Duration Field, you can understand the NAV that stations would use. The Duration Field value indicates how long the medium will be busy, and stations use this value to set their NAV timers. While Wireshark doesn't explicitly show the NAV, the Duration Field provides the necessary information to infer it.

**How Virtual Carrier Sense Works?**

- `Frame Transmission`: A station wishing to transmit sends a frame with a Duration Field indicating how long it will use the medium. <br><br>
- `NAV Update`: Other stations that receive this frame read the Duration Field and set their NAV timers accordingly if the Duration value is greater than their current NAV value. <br><br>
- `Medium Access`: These stations refrain from accessing the medium until their NAV timers expire, allowing the transmitting station to complete its transmission without interference.

![image](https://github.com/user-attachments/assets/9d346dea-82e4-4069-84c2-d5acea5c7da8)

````py

## Virtual Carrier Sense Example Scenario:

1. # Station A wants to send data to Station B.
   # It calculates the total time needed for the transmission, including any necessary SIFS, Data & Acks.

2. # Station A sets the Duration Field in its frame to this calculated time and transmits the frame.

3. # Station C and Station D, which are within range, receive the frame from Station A.
   # They read the Duration Field and set their NAV timers to this value if it is greater than their current NAV value.

4. # Station C and Station D refrain from transmitting until their NAV timers expire,
   # allowing Station A to complete its transmission to Station B without collision.

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


Station A                                                                       Station B
+===============+          +---------------------------------+          +===============+ 
| transmitting  |------->>>| {{ Frame with Duration Field }} |------->>>|   receiving   |  
+===============+          +---------------------------------+          +===============+                              
                           \
                             \
                               \
                                V
                             Stations C and D (or other stations):
                             +------------------------------------------------------------------+
                             |   1. Read Duration Field                                         |
                             |   2. Set NAV timers:                                             |
                             |      if NAV > current NAV value, then STA will update their NAV  |
                             |      while NAV ≠ 0, STA will presume medium is busy              |
                             |   3. Wait from transmitting                                      |
                             +------------------------------------------------------------------+

````





## 🙋🛜🚦 Background Concepts: ` IFS (Interframe spaces)`

Interframe Spaces (IFS) are periods of time between frames or "time gaps on the medium"; they are used to allow frames to be processed in a timely manner, avoid interference by ensuring frames are received, and prioritize transmission of certain frames. This means that after each frame transmission, 802.11 protocol require an idle period on the medium called IFS 

IFS is defined in the 802.11-2007 standard as: 

- **“The time from the end of the last symbol of the previous frame to the beginning of the first symbol of the preamble of the subsequent frame as seen at the air interface.”**_

IFS are needed for both: 

1. Keep buffer between the frames to avoid interference.
2. Add control and to prioritize frame transmissions _(in case of QoS)_.

### IFS (Interframe spaces): `Lenght / Duration`

- IFS unit of time is measured in microseconds (μs)
- The length of the IFS is depend on previous frame type, following frame type, access category, coordination function in use & PHY type as well. 
- All types of IFS has fixed time for each PHY except AIFS  

## ⌛📏🔠 Types of IFS:

There are multiple types of IFS, some defined by the original standard and others added to in 802.11e-2005 & 802.11n-2009.

- The type of IFS is dependent on the frame that will come after it.
- Using a shorter duration IFS gives certain frames priority over others, such as an ACK frame using a short IFS (SIFS).

### Types of IFS: `IFS First time transmission`

- **`No QoS Scenario`**: BSS that do not support QoS will use the legacy `DCF IFS (DIFS)`.
- **`QoS (EDCA) Scenario`**: All IFS are sent as `Arbitration IFS (AIFS)`. 

---


### ⌛👨‍⚖️ IFS Priotirty:

````py

## IFS Priority

"Higher Priority"                                 "Lower Priority"

        RIFS >>> SIFS >>> PIFS >>> DIFS/AIFS >>> EIFS 

````

### ⌛📅 All in one IFS table:

| **PHY**                 | **Slot Time**                                                                    | **SIFS**                                                                   | **RIFS**         | **EIFS**                                                                            | **PIFS**                                                       | **DIFS**                                                    | **AIFS**                                  |
|-------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------|
| **Name**                | /                                                                                | Short IFS                                                                  | Reduced IFS      | Extended IFS                                                                        | PCF IFS                                                        | Distributed IFS                                             | Arbitration IFS                           |
| **Uses**                | /                                                                                | Between all frames transmitted within a TxOP                               | Only for 802.11n | Corrupt CRC Frames and Retries                                                      | _PCF_<br>_Unused in 802.11_                                    | Only for Non-QoS<br>Prior to Data or RTS in DCF             | Only for QoS (EDCA)<br>802.11e            |
| **Duration Formula**    | aCCATime <br>+aRxRxTurnAroundTime <br>+aAirPropagation <br>+aMACProcessingDelay  | aRxRFDelay+aRxPLCPDelay <br>+aMACProcessingDelay <br>+aRxTxTurnAroundTime  | RIFS = 2μS       | EIFS (in DCF) = SIFS+DIFS+ACK_Tx_Time<br>EIFS (in EDCA) = SIFS+AIFS[AC]+ACK_Tx_Time | PIFS = SIFS+DIFS+ACK_Tx_Time                                   | DIFS = SIFS + 2x SlotTime<br>_SlotTime depends on each PHY_ | AIFS[AC] = AIFSN[AC]*SlotTime+SIFSTime    |
| **HR/DSSS <br>802.11b** | 20μS                                                                             | 10μS                                                                       | _N/A_            | 364μS <br>(Depends on ACK Time)                                                     | _30μS_                                                         | 50μS                                                        | Variable:<br>Depending Access Method / CW |
| **ERP<br>802.11g**      | Long = 20μS<br>Short = 9μS                                                       | Long = 10μS<br>Short = 10μS                                                | _N/A_            | Long = 364μS<br>Short = 342μS<br>(Depends on ACK Time)                              | _Long = 30μS_<br>_Short = 19μS_                                | Long = 50μS<br>Short = 28μS                                 | Variable:<br>Depending Access Method / CW |
| **OFDM <br>802.11a**    | 9μS                                                                              | 16μS                                                                       | _N/A_            | 94μS <br>(Depends on ACK Time)                                                      | _25μS_                                                         | 34μS                                                        | Variable:<br>Depending Access Method / CW |
| **HT<br>802.11n**       | 2.4GHz Long = 20μS<br>2.4GHz Short = 9μS<br>5GHz = 20μS                          | 2.4GHz = 10μS<br>5GHz = 16μS                                               | 2μS              | 2.4GHz = 342μS<br>5GHz = 94μS                                                       | _2.4GHz Long = 30μS_<br>_2.4GHz Short = 19μS_<br>_5GHz = 25μS_ | 2.4GHz Long = 50μS<br>2.4GHz Short = 28μS<br>5GHz = 34μS    | Variable:<br>Depending Access Method / CW |
| **VHT<br>802.11ac**     | 9μS                                                                              | 16μS                                                                       | _N/A_            | 94μS <br>(Depends on ACK Time)                                                      | _25μS_                                                         | 34μS                                                        | Variable:<br>Depending Access Method / CW |






## `Backoff Timer` & `Contention Window`

"Operation"

- **`Contention Window`**: A range of numbers netween CWmin and CWmax from which a STA picks a random backoff value. <br><br>
- **`Backoff`**: A random backoff value is counted down in a number of slots. If the medium becomes busy, pause the backoff time, and defer. 

![image](https://github.com/user-attachments/assets/a96b731b-936c-45b9-bf4e-b148736108ed)

### Random Backoff Values

There are different Random Backoff Values for each PHY. There are also different Random Backoff Values for each QoS categories in EDCA

- `802.11b` can be a Random Backoff Value between 0 and 31 slots:

![image](https://github.com/user-attachments/assets/64cf6202-08b9-451e-a65a-8bc07e5efe94)

- `802.11/g` can be a Random Backoff Value between 0 and 15 slots:

![image](https://github.com/user-attachments/assets/af0525e1-9fcb-4c87-992d-f04e66f8499a)

![image](https://github.com/user-attachments/assets/c1c904a5-39bc-46b2-b435-1aaf5fcabca7)










`---






![image](https://github.com/user-attachments/assets/afaff3ba-fab7-4542-b2b7-55d10069c5f8)

![image](https://github.com/user-attachments/assets/82d8eea1-2a95-4a2f-99df-32b8aa82ee25)

![image](https://github.com/user-attachments/assets/c6854024-7d55-4293-9514-6dcbdbfd161d)

![image](https://github.com/user-attachments/assets/089ba06f-0d89-42a4-8527-3f87884c4a09)

---


















![image](https://github.com/user-attachments/assets/d888e1f2-ae93-4596-aa87-9c9af58ed0ab)

![image](https://github.com/user-attachments/assets/b028afca-bc55-4d1a-b832-d245b314f327)

![image](https://github.com/user-attachments/assets/ea262c58-874d-4bba-a2a2-3d8f881a058d)

![image](https://github.com/user-attachments/assets/e7ddd2d3-dc75-4c9a-8814-56fb7172cb2a)

![image](https://github.com/user-attachments/assets/d2831450-8eed-45a6-a706-0ce351f1d6ee)

![image](https://github.com/user-attachments/assets/3c8372c3-4f27-49d8-8ef4-e8275ea5c2da)

![image](https://github.com/user-attachments/assets/ab487fe0-1252-499d-9ddc-1339bea2300c)

![image](https://github.com/user-attachments/assets/372ca4ca-05a2-4b03-bc19-6586a09b0933)

![image](https://github.com/user-attachments/assets/4cb51216-e3be-46f5-a7ef-c3ee136d2bb4)

![image](https://github.com/user-attachments/assets/07eec27c-e6c4-4d50-bd61-dbbcbeeb3417)

![image](https://github.com/user-attachments/assets/f943584c-f1a5-4c43-ac7e-0c7ec7f0010c)

![image](https://github.com/user-attachments/assets/4a80bd24-2f14-4044-bbad-630810937ec0)

![image](https://github.com/user-attachments/assets/c94dbdb0-e99d-42d4-932c-96a1853dce9a)

![image](https://github.com/user-attachments/assets/15dc8c90-41c3-4230-bda6-fded024f399d)

![image](https://github.com/user-attachments/assets/5af685fb-2783-4ba9-bea7-3e02449f005e)


---

![image](https://github.com/user-attachments/assets/a04cf0e2-e0c6-4e8f-a20e-17056d97d60a)

![image](https://github.com/user-attachments/assets/5d25afa9-57af-409f-b343-fa94296fe200)

![image](https://github.com/user-attachments/assets/237dee3e-51e1-4ab0-9b11-0aba49add796)

![image](https://github.com/user-attachments/assets/eb735500-65ed-46eb-af00-01f926c33860)




---

QoS & EDCA

![image](https://github.com/user-attachments/assets/f18d671c-ae17-440b-a242-348a7b97b2c6)

![image](https://github.com/user-attachments/assets/bcb6ce10-cbb0-4569-b6d7-00a89129b2b3)

![image](https://github.com/user-attachments/assets/8a747fa9-d09c-466e-a0dc-2332ddf85a4e)

![image](https://github.com/user-attachments/assets/d3ad57d1-89f3-407b-8a49-f2f65e51a989)

![image](https://github.com/user-attachments/assets/da374694-8858-4865-861a-3bce6559a42c)

![image](https://github.com/user-attachments/assets/29a28ce7-1d83-4177-ae21-c3b760e45f3e)

![image](https://github.com/user-attachments/assets/6671aa09-366c-4208-8e69-14a421d51e6e)


**How Backoff Timer and CW works?**

- After a STA has observed an idle wireless medium with carrier sense (CS) for the appropriate IFS interval (DIFS, EIFS, or AIFS).
- To contend for medium access after the IFS, each station selects a backoff value called random backoff period and is selected at random by the STA from a window of possible values called a contention window (CW) calculated using the below formula where x is a value increments with each failed frame.

**Contention Window (CW) Formula:**

- `CW` = **2^x -1** 

**CW in DSS & OFDM:**

- `DSS` (x) **starts at 5** which resulting CW of `31`. 
- `OFDM` (x) **starts at 4** which result in a CW of `15`. <br><br>
- In both DSS & OFDM (x) values stops incrementing at 10 which result CW of `1023`. 

**Table:**

| **PHY**      | **Contention Window Min<br>(aCWmin)** | **Contention Window Max<br>(CWmax)** |
|--------------|---------------------------------------|--------------------------------------|
| **802.11b**  | 31                                    | 1023                                 |
| **802.11a**  | 15                                    | 1023                                 |
| **802.11g**  | DSSS(0) = 31<br>OFDM(1) = 15          | 1023                                 |
| **802.11n**  | 15                                    | 1023                                 |
| **802.11ac** | 15                                    | 1023                                 |

### Retries and Backoff

````py

## Retries and Backoff

# If there's a retry in the transmission, the CWmax is doubled + 1 for every retry (until it reached the CWmax)

## Example:

    # If a STA chooses a Random Backoff Value of 15 (eg. the largest Value/Number of an OFDM tranmission) and there are retries,
    # it will look like this: 


       CWmin                                                                                                                            CWmax
         0                                                                                                                               1023

         |                                                                                                                                |
Initial  |-| CW = 15                                                                                                                      |
Attempt  |-|                                                                                                                              |
         |                                                                                                                                |
1st      |---| CW = 31                                                                                                                    |
Retry    |---|                                                                                                                            |
         |                                                                                                                                |
2nd      |-------| CW = 63                                                                                                                |
Retry    |-------|                                                                                                                        |
         |                                                                                                                                |
3rd      |---------------| CW = 127                                                                                                       |
Retry    |---------------|                                                                                                                |
         |                                                                                                                                |                    
4th      |-------------------------------| CW = 255                                                                                       |
Retry    |-------------------------------|                                                                                                |
         |                                                                                                                                |
5th      |---------------------------------------------------------------| CW = 511                                                       |
Retry    |---------------------------------------------------------------|                                                                |
         |                                                                                                                                |
6th      |-------------------------------------------------------------------------------------------------------------------------------|| CW = 1023
Retry    |-------------------------------------------------------------------------------------------------------------------------------||
         |                                                                                                                                |
More     |-------------------------------------------------------------------------------------------------------------------------------|| CW = 1023
Retries  |-------------------------------------------------------------------------------------------------------------------------------||
...      |                                                                                                                                |
         |________________________________________________________________________________________________________________________________|


````














## 🙋🤳🏻📡 Protection Mechanisms: `No Protection` - 

### No Protection: `Description` 

- This is the most basic type of data exchange in Wi-Fi networks and involves a simple transmission of data followed by an acknowledgment (ACK). 
- The duration value only accounts for the Short Interframe Space (SIFS), which is the brief waiting period between transmissions, and the ACK frame.

### No Protection: `Characteristics`

- There is no protection mechanism in place, meaning that no extra steps are taken to prevent collisions or interference.
- This method is used when the network conditions are good, and there is little risk of other devices transmitting simultaneously and causing collisions.

- 
Real-life Example: In a home network with only a few devices and minimal interference, a device like a smartphone or laptop might use this type of data exchange to send a file or stream media. Because there’s little congestion, additional protection is unnecessary.
Duration Value: SIFS + Ack

### No Protection: `Frame Exchange`

![image](https://github.com/user-attachments/assets/b486b3fa-4fc7-4820-8a88-198e186a63e8)

### No Protection: `Configuration`

Some devices can be configured for `No protection` mode. _(eg. Ruckus vSZ Virtual Smartzone Controller v6)_

- **`Important`**:  **It is not a good practice turning off the RTS/CTS or CTS-to-Selft Protection Mechanisms!!!**

![image](https://github.com/user-attachments/assets/623dffb3-2c3b-45a8-bf98-b16ab7c45ff8)

## 🙋🤳🏻📡 Protection Mechanisms: `RTS/CTS` VS `CTS-to-self`

| **Feature**                      | **Normal RTS/CTS**                             | **CTS-to-Self**                                |
|-----------------------------------|------------------------------------------------|------------------------------------------------|
| **Description**                   | A medium access control mechanism to avoid collisions. The **RTS (Request to Send)** is sent to reserve the channel, followed by a **CTS (Clear to Send)**. Used in networks with interference or long distances. | Used to protect transmissions on **wide channels** in **802.11n/ac**. The **CTS-to-Self** is sent by a device to the AP to protect the channel during the transmission. |
| **Primary Use**                   | Collision avoidance, especially in environments with interference or long distances. | Protects transmission on wide channels in **802.11n/ac** networks. |
| **Supported PHY**                 | **802.11a/b/g/n/ac**                           | **802.11n (HT)**, **802.11ac (VHT)**            |
| **When to Use**                   | In **802.11a/b/g/n/ac** networks to avoid collisions on 20 MHz channels, in interference-prone environments or long distances. | In **802.11n (HT)** and **802.11ac (VHT)** networks to protect transmission on high-speed wide channels. |
| **Real-Life Example**             | In an environment with multiple APs, **RTS/CTS** is used to prevent stations from interfering with each other when attempting to transmit data simultaneously. | In an **802.11ac** network, a device sends a **CTS-to-Self** before transmitting to ensure the channel is clear of interference and collisions. |
| **Supported Bandwidth**           | **20 MHz**, **40 MHz**, **80 MHz** (depending on the environment and configuration) | **20 MHz**, **40 MHz**, **80 MHz**, **160 MHz** (in **802.11ac (VHT)** networks) |

## 🙋🤳🏻📡 Protection Mechanisms: `RTS/CTS` _(802.11g or newer)_ 

2. RTS/CTS Data Exchange
Description: This method introduces a protection mechanism called Request to Send/Clear to Send (RTS/CTS), which is used to avoid collisions, especially in environments with hidden nodes (devices that cannot detect each other but share the same access point). Before sending data, a device sends an RTS frame to reserve the channel. The receiver responds with a CTS frame to confirm that the channel is clear for transmission. After this exchange, data is sent, followed by an acknowledgment (ACK).
Characteristics: RTS/CTS is a more robust method for ensuring that data transmission happens without interference. It’s effective in high-traffic networks or in networks with hidden nodes, as it reduces the chance of collisions.
Real-life Example: In a large office building or public Wi-Fi environment where many devices are connected, RTS/CTS may be used to prevent devices that are far apart (and cannot sense each other) from transmitting at the same time and causing a collision.
Duration Value: x3 SIFS + CTS + Data + ACK
3. CTS-to-Self Data Exchange
Description: The CTS-to-Self mechanism is another form of protection but is simpler than RTS/CTS. Instead of sending an RTS frame to initiate the transmission, the device sends a CTS frame to itself, indicating that it is about to transmit data. This is followed by the actual data transmission and an acknowledgment (ACK). It’s quicker than RTS/CTS but not as robust in handling interference.
Characteristics: CTS-to-Self is more efficient in terms of reducing overhead because it eliminates the need for an RTS frame, but it’s not as effective at preventing collisions as RTS/CTS. It’s generally used in mixed-mode environments where older devices might interfere with newer ones, but the risk of hidden nodes is lower.
Real-life Example: In a mixed environment where a Wi-Fi network has both older and newer devices (e.g., 802.11g and 802.11n devices), CTS-to-Self might be used to ensure that older devices don’t interfere with newer ones. This protection method reduces overhead while still offering some level of protection.
Duration Value: x2 SIFS + Data + ACK
Key Differences:
Protection:

Data Exchange / Block ACK: No protection, most basic.
RTS/CTS: Strong protection against hidden nodes and collisions.
CTS-to-Self: Moderate protection, quicker but less robust than RTS/CTS.
Overhead:

Data Exchange / Block ACK: Lowest overhead.
RTS/CTS: Highest overhead due to multiple frame exchanges (RTS + CTS).
CTS-to-Self: Moderate overhead, no RTS frame needed.
Use Cases:

Data Exchange / Block ACK: Simple, low-congestion networks.
RTS/CTS: High-traffic or hidden node environments.
CTS-to-Self: Mixed-mode environments with lower risk of hidden nodes.


![image](https://github.com/user-attachments/assets/63d3aed3-1c7b-4aa0-822e-9426a60f3fc2)





![image](https://github.com/user-attachments/assets/fc8d7516-dc1d-453f-a7eb-45bd1a8440bc)


![image](https://github.com/user-attachments/assets/20a9ebb3-8ab3-42b0-a5f1-f4ffb0085f75)


![image](https://github.com/user-attachments/assets/1c169f74-c3ac-4905-b794-b8ce05f86b29)

![image](https://github.com/user-attachments/assets/ee96db40-2db9-4049-9357-8e98111d2aa2)



![image](https://github.com/user-attachments/assets/1813bbd1-9ef0-4c55-b719-32e3fcbaffc7)



## 🙋📡📡 Protection Mechanisms: `CTS-to-self` _(802.11g or newer)_ 

![image](https://github.com/user-attachments/assets/9f19711c-98df-4be3-960b-5122a078ddc6)

CTS-to-Self is not a frame explicitly defined in the IEEE 802.11 standard, but it is commonly used in Wi-Fi networks as a protection mechanism. Essentially, it involves sending a Clear to Send (CTS) frame without the usual preceding Request to Send (RTS) frame, typically initiated by the AP.

The primary function of CTS-to-Self is to distribute the Network Allocation Vector (NAV) using only CTS frames. This allows devices on the network to be informed that the wireless channel is reserved, reducing the chances of interference during data transmission. By signaling to itself, the AP tells all devices that it is about to transmit data, effectively reserving the channel for its own use.

CTS-to-Self is mainly used as a protection mechanism in mixed-mode environments. These are scenarios where devices that use different Wi-Fi standards (for example, 802.11g and 802.11n) coexist on the same network. In such environments, older devices that may not support newer protocols are alerted that the channel is in use, preventing them from causing interference.

- **One of the key advantages of CTS-to-Self is that it has lower overhead compared to the RTS/CTS mechanism.** RTS/CTS involves sending an RTS frame, waiting for a CTS response, and only then proceeding with data transmission. This adds more steps and consumes more airtime. In contrast, CTS-to-Self skips the RTS step, making it quicker and more efficient in terms of network overhead. <br><br>

However, **this method is not as robust against `hidden nodes` or `collisions` as RTS/CTS**. 

- Since **CTS-to-Self doesn't account for `hidden nodes` (other STAs) trying to transmit at the same time**, it may be less effective in preventing collisions in complex network environments.

Devices (STAs) should choose between **CTS-to-Self** and **RTS/CTS** depending on the network conditions: 

- `CTS-to-Self`: In environments with **fewer hidden nodes** and **less potential for interference** _(because of CTS-to-Self efficiency)_. <br><br>
- `RTS/CTS`: If **hidden nodes or frequent collisions are detected**, switching to the more robust mechanism _(eg. RTS/CTS)_ may be necessary to ensure reliable communication.

![image](https://github.com/user-attachments/assets/586d805b-ea07-479c-b3f4-6a55abd1cf49)


## 🙋📡📡 Protection Mechanisms: `Dual CTS` _(802.11n only : STBC)_ 

Protection is used by the AP to set a NAV at STAs that do not support STBC (Space-time block coding) and at STAs that can associate solely through the STBC beacon. 

- 0 – dual CTS protection is not required
- 1 – dual CTS protection is required

STBC Beacon indicates whether the beacon containing this element is a primary or an STBC beacon. The STBC beacon has half a beacon period shift relative to the primary beacon. Defined only in a Beacon transmitted by an AP. Otherwise reserved.

- 0 – primary beacon
- 1 – STBC beacon

When implementing STBC, the received signal may be improved by up to 8 dB, resulting in greater range shown in the below figure (CWAP- Page 423). An 8 dB increase in signal strength can yield up to 69 percent more range. This increased range will only apply to STBC frames and therefore does not automatically mean an increased BSS size for all STAs.

![image](https://github.com/user-attachments/assets/e177b13b-a7cc-4eeb-8ede-01679eef168b)


# Protection Types: `ERP Protection` & `HT Protection`

Protection mechanisms cause a STA that is a potential interferer to defer any transmission for a known period of time. When these mechanisms are used:

1. `ERP Protection`: non-ERP STAs do not interfere with frame exchanges using ERP PPDUs between ERP STAs.
2. `HT Protection`: non-HT STAs do not interfere with frame exchanges using HT PPDUs between HT STAs.

As a result, non-ERP and/or non-HT STAs are allowed to coexist with ERP and/or HT STAs.

## ERP Protection & HT Protection: `Protection Elements`

ERP (802.11g) & HT (802.11n) **Protection Modes Information Elements** are present in `Beacons` & `Probe Responses`:

- `ERP Information Element`: Present in **2.4 GHz** Beacons & Probe Responses
- `HT Information Element`: Present in **2.4 GHz** & **5 GHz** Beacons & Probe Responses

### Information Elements: `2.4 GHz` : `ERP` & `HT`

````sh
# Beacon Frame @ 2.4 GHz
# ERP & HT Information Elements

Frame 1: 356 bytes on wire (2848 bits), 356 bytes captured (2848 bits)
PPI version 0, 84 bytes
802.11 radio information
IEEE 802.11 Beacon frame, Flags: .........
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (232 bytes)
        Tag: SSID parameter set: "Fz3r0 @ CWAP"
        Tag: Supported Rates 12(B), 18, 24(B), 36, 48, 54, [Mbit/sec]
        Tag: DS Parameter set: Current Channel: 1    <<<<<-------------------------------|||| Channel 1 (2.4 GHz Transmission)
        Tag: Traffic Indication Map (TIM): DTIM 0 of 1 bitmap
        Tag: Country Information: Country Code MX, Environment Global operating classes
        Tag: ERP Information                         <<<<<-------------------------------|||| ERP Information Element (2.4 GHz Only)
        Tag: Vendor Specific: Microsoft Corp.: WMM/WME: Parameter Element
        Tag: RSN Information
        Tag: RM Enabled Capabilities (5 octets)
        Tag: HT Capabilities (802.11n D1.10)
        Tag: HT Information (802.11n D1.10)          <<<<<-------------------------------|||| HT Information Element  (2.4 & 5 GHz)
        Tag: QBSS Load Element 802.11e CCA Version
        Tag: Interworking
        Tag: Advertisement Protocol
        Tag: Extended Capabilities (8 octets)
        Tag: Vendor Specific: Ruckus Wireless: Unknown
        Tag: Vendor Specific: Ruckus Wireless
        Tag: Vendor Specific: Wi-Fi Alliance: Hotspot 2.0 Indication
        Tag: Vendor Specific: Wi-Fi Alliance: Multi Band Operation - Optimized Connectivity Experience
        Tag: Vendor Specific: Wi-Fi Alliance: P2P
````
````sh
# ERP & HT Information Element (Beacons & Probe Responses)
# @ 2.4 GHz 
# Wireshark Filter:

wlan.erp_info
wlan.ht.info.delim2
````

### Information Elements: `5 GHz` : `HT`

````sh
# Beacon Frame @ 5 GHz
# HT Information Element

Frame 1: 383 bytes on wire (3064 bits), 383 bytes captured (3064 bits)
PPI version 0, 84 bytes
802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (263 bytes)
        Tag: SSID parameter set: "Fz3r0 @ CWAP"
        Tag: Supported Rates 12(B), 18, 24(B), 36, 48, 54, [Mbit/sec]
        Tag: DS Parameter set: Current Channel: 104  <<<<<-------------------------------|||| Channel 104 (5 GHz Transmission)
        Tag: Traffic Indication Map (TIM): DTIM 0 of 1 bitmap
        Tag: Country Information: Country Code MX, Environment Global operating classes
        Tag: Vendor Specific: Microsoft Corp.: WMM/WME: Parameter Element
        Tag: RSN Information
        Tag: RM Enabled Capabilities (5 octets)
        Tag: HT Capabilities (802.11n D1.10)
        Tag: HT Information (802.11n D1.10)          <<<<<-------------------------------|||| HT Information Element  (2.4 & 5 GHz)
        Tag: QBSS Load Element 802.11e CCA Version
        Tag: Interworking
        Tag: Advertisement Protocol
        Tag: Extended Capabilities (8 octets)
        Tag: VHT Capabilities
        Tag: VHT Operation
        Tag: Tx Power Envelope
        Tag: Vendor Specific: Ruckus Wireless: Unknown
        Tag: Vendor Specific: Ruckus Wireless
        Tag: Vendor Specific: Wi-Fi Alliance: Hotspot 2.0 Indication
        Tag: Vendor Specific: Wi-Fi Alliance: Multi Band Operation - Optimized Connectivity Experience
        Tag: Vendor Specific: Wi-Fi Alliance: P2P
````
````sh
# HT Information Element (Beacons & Probe Responses)
# @ 5 GHz 
# Wireshark Filter:

wlan.ht.info.delim2
````

## ERP & HT Protection: Difference Between `802.11g (ERP)` & `802.11n (HT)`

When 802.11g was introduced, we had RTS/CTS and CTS-to-Self protection mechanisms.  What do we get with 802.11n so that it's backwards compatible with 802.11a and 802.1b/g? First, there's a couple of new things I'd like to introduce, and then we'll get to the protection rules.

- **`802.11g` = `ERP`**: In an **ERP Beacon**, ERP stations look at the **ERP Information Element** to determine whether or not protection is necessary in the BSS
- **`802.11n` = `HT`**: In an **HT Beacon**, HT stations use the **Operating Mode** and **Non-greenfield STAs Present** fields in the **HT Information Element** to determine whether or not to use protection.





# Protection Mechanisms: `ERP Protection` 

An ERP `Mixed Mode` enviorment means that a **802.11g (ERP)** device is sharing the air/channel with any of both legacy devices: **802.11-prime (DSSS)** or **802.11b (HR-DSSS)** in the 2.4 GHZ band _(ERP only exists in 2.4 GHz)_.

- **Mixed Mode** =  `ERP (802.11g)` + `DSSS or/and HR-DSSS (802.11prime or/and 802.11b)`

In a mixed mode enviorment, when an **802.11g (ERP) STA** wants to transmit data it will:

1. Perform a **NAV distribution** by transmitting `RTS/CTS` exchange with the AP, or by transmitting `CTS-to-Self` using a `Data Rate` and `Modulation Method` that the **802.11b (HR-DSSS) STAs** can understand.
2. The `RTS/CTS` or `CTS-to-Self` will hopefully be "heard" and "understood" by all the **802.11b/g (HR-DSSS & ERP) STAs** inside the BSA. 
3. The `RTS/CTS` or `CTS-to-Self` will contain a `Duration/ID` value that will be used by all od the **listening STAs** to set their `NAV Timers`. 




- IEEE 802.11-2007 standard mandate support for both DSSS (Direct Sequence Spread Spectrum) & OFDM (Orthogonal Frequency Division Multiplexing) technologies for clause 19 ERP (802.11g) radios.
- When clause 18 (HR-DSSS) & clause 15 DSSS (802.11) coexisting in ERP BSS, 802.11g devices need to provide compatibility for slower 802.11/802.11b devices.
- In this **mixed mode** (801.11 + 802.11b) 802.11g devices enable “Protection mechanism” also known as **`802.11g Protected mode`**.

## ERP Protection: `ERP Information Element`

**ERP nformation Element** is present in `beacons` & `probe responses` **only on 2.4 GHz band**.

ERP Information Element (IE) contains information about Claue15 (802.11 Prime) or Clause 18 (802.11b) stations in the BSS that are not capable of communicating Clause 19 (ERP-OFDM) data rates. It also identifies whether AP should use protection mechanism & whether to use long or short preambles. 

![image](https://github.com/user-attachments/assets/2a7889c6-2de2-4431-80e1-4a07876a89ec)

````sh
# ERP Information Element
# Beacon & Probe Responses

        Tag: ERP Information
            Tag Number: ERP Information (42)
            Tag length: 1
            ERP Information: 0x00
                .... ...0 = Non ERP Present: Not set
                .... ..0. = Use Protection: Not set
                .... .0.. = Barker Preamble Mode: Not set
                0000 0... = Reserved: 0x00
````

| **Field**                 | **Description**                                                                     | **Wireshark Filter**                      |
|---------------------------|-------------------------------------------------------------------------------------|-------------------------------------------|
| ERP Element ID            | ERP Information Element = 42                                                        | `wlan.tag.number == 42`                   |
| Tag Length                | Indicates the length of the ERP Information Element (1 byte)                        | `wlan.tag.length == 1`                    |
| ERP Information           | ERP Information HEX combination                                                     | `wlan.erp_info == 0x00`                   |
| ⚠️**non-ERP Present**      | **= 1 when a non-ERP station is associated with the BSS**                           | `wlan.erp_info.erp_present == 1`          |
| ⚠️**Use Protection**       | **= 1 when a non-ERP station is associated with the BSS OR is within the same cell associated to another BSS OR using Ad-Hoc, enabling protection mode** //  | `wlan.erp_info.use_protection == 1`       |
| ⚠️**Barker Preamble Mode** | **= 1 if one or more associated non-ERP stations cannot use short preambles**       | `wlan.erp_info.barker_preamble_mode == 1` |
| _Reserved (HEX)_          | _Reserved bits within the ERP Information Element, typically set to 0x00_           | _`wlan.erp_info.reserved == 0x00`_        |


## ERP Protection: `No Protection`

The `ERP Protection` field may be set to **No Protection Mode / Greenfield** only if the following are true:

1. All STAs detected in the channel are ERP (802.11g) STAs, and:
2. All STAs that are known by the transmitting STA to be a member of this BSS are **Short Preamble capable**:

![image](https://github.com/user-attachments/assets/a1937756-a9a3-46cb-937a-1b3a693e847a)

````sh
# ERP Protection: No Protection

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........C
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (184 bytes)
        Tag: ERP Information
            Tag Number: ERP Information (42)
            Tag length: 1
            ERP Information: 0x00                                       # No protection:
                .... ...0 = Non ERP Present: Not set       # <<<<<-----|| All STAs are ERP
                .... ..0. = Use Protection: Not set        # <<<<<-----|| No protection enabled
                .... .0.. = Barker Preamble Mode: Not set  # <<<<<-----|| No Barker Long Preamble Needed
                0000 0... = Reserved: 0x00
````
````py
# Barker Preamble Mode Wireshark Filter
# Option 2: AP configuration or architecture

wlan.erp_info.erp_present == 0 && wlan.erp_info.use_protection == 0 && wlan.erp_info.barker_preamble_mode == 0
````

## ERP Protection: `Mixed Mode` = `non-ERP_Present` + `Use Protection`

ERP (802.11g) STAs shall use protection mechanisms (such as RTS/CTS or CTS-to-self) for ERP-OFDM MPDUs of type Data or an MMPDU when the `Use_Protection` field of the ERP Element is equal to `1`. Note that when using the Clause 19 options, ERP-PBCC or DSSS-OFDM, there is no need to use protection mechanisms, as these frames start with a DSSS header.

- If a non-ERP (802.11prime or 802.11b) device/transmission is detected in the cell, both: `non-ERP Present` &  `Use Protection` will set to `1`.
- **Only** if a non-ERP  (802.11prime or 802.11b)STAs cannot use short preambles the `Barker Preamble Mode` will set to `1`.

The following **3 scenarios** can trigger ERP `Use Protection` and `non-ERP_Present` bit set to 1 (beacons & probes) in an ERP Basic Service Set (BSS):

### 1. DSSS (802.11-prime) or HR-DSSS (802.11b) `client association`, in the ERP (802.11g) WLAN. 

- If a **non-ERP STA** associates with an **ERP AP**, the **ERP AP** will: <br><br>
    - enable the `NonERP_Present` bit = **`1`** in its own beacons.
    - enable the `Use Protection` bit = **`1`** in its own beacons. <br><br>
![image](https://github.com/user-attachments/assets/ce062156-9ae9-490e-9570-70ee821e54a6) 

### 2. **ERP (802.11g) WLAN AP "hear" `sorrounding Beacons or Ad-Hoc Networks` of DSSS (802.11-prime) or HR-DSSS (802.11b).** 

- If an **ERP AP hears** a beacon from a neighbor AP where the supported data rates contain only 802.11b HR-DSSS or 802.11 DSSS rates, the **ERP AP** will: <br><br>
    - enable the `NonERP_Present` bit = **`0`** in its own beacons.
    - enable the `Use Protection` bit = **`1`** in its own beacons. <br><br>
![image](https://github.com/user-attachments/assets/b3182d4b-373c-48dc-8beb-1606150cd5bb)

### 3. **ERP (802.11g) WLAN AP "hear" `sorrounding Management Frames (except probe request)` using DSSS (802.11-prime) or HR-DSSS (802.11b) data rates.** <br><br>

- If an ERP AP hears a management frame (other than a probe request) where the supported rate includes only 802.11 or 802.11b rates, the **ERP AP** will: <br><br>
    - enable the `NonERP_Present` bit = **`0`** in its own beacons.
    - enable the `Use Protection` bit = **`1`** in its own beacons. <br><br>
![image](https://github.com/user-attachments/assets/dfb232f0-a6e4-4691-a0c0-d404d99b8e02) 

## ERP Protection: `Barker Preamble Mode`

The `Barker_Preamble_Mode` is used mostly in `Mixed Mode` and the bit shall be set to `1` by the `ERP Information Element` sender AP if:

- `Option 1`: One or more **associated Non-ERP STAs** are **not short preamble capable** as indicated in their `Capability Information` field.
- `Option 2`: AP configuration or architecture; the ERP Information Element of the sender `dot11ShortPreambleOptionImplemented` MIB variable is set to `0`.
- `Option 3`: AP "hears" **non-ERP STA** within the cell that are **not short preamble capable** OR AP "hears" **non-ERP STA** within the cell and AP configuration or architecture has the `dot11ShortPreambleOptionImplemented` MIB variable is set to `0`.

In a 802.11g network, if all STAs are capable of short preambles, Barker Preamble Mode should be disabled and all stations will use short preambles for efficiency.

### Barker Preamble Mode: `Option 1` - `not short preamble capable STA`

````sh
# Barker Preamble Mode
# Option 1: Associated Non-ERP STA are not short preamble capable

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........C
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (213 bytes)
        Tag: ERP Information
            Tag Number: ERP Information (42)
            Tag length: 1
            ERP Information: 0x07                                   # Mixed Mode:  
                .... ...1 = Non ERP Present: Set       # <<<<<-----|| Non ERP Associated to BSS
                .... ..1. = Use Protection: Set        # <<<<<-----|| ERP Protection Mode Set
                .... .1.. = Barker Preamble Mode: Set  # <<<<<-----|| Barker Pramble Mode Set
                0000 0... = Reserved: 0x00
````
````py
# Barker Preamble Mode Wireshark Filter
# Option 1: Associated Non-ERP STA are not short preamble capable

wlan.erp_info.erp_present == 1 && wlan.erp_info.use_protection == 1 && wlan.erp_info.barker_preamble_mode == 1
````

### Barker Preamble Mode: `Option 2` - `AP configuration or architecture`

````sh
# Barker Preamble Mode
# Option 2: AP configuration or architecture

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........C
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (184 bytes)
        Tag: ERP Information
            Tag Number: ERP Information (42)
            Tag length: 1
            ERP Information: 0x04
                .... ...0 = Non ERP Present: Not set
                .... ..0. = Use Protection: Not set
                .... .1.. = Barker Preamble Mode: Set  # <<<<<-----|| Barker Pramble Mode Set by device Configuration or Architecture
                0000 0... = Reserved: 0x00
````
````py
# Barker Preamble Mode Wireshark Filter
# Option 2: AP configuration or architecture

wlan.erp_info.erp_present == 0 && wlan.erp_info.use_protection == 0 && wlan.erp_info.barker_preamble_mode == 1
````

### Barker Preamble Mode: `Option 3` - `Non-ERP STA + not short preamble capable` or `Non-ERP STA + Config/Architecture`

````sh
# Barker Preamble Mode
# Option 3: Non-ERP STA + not short preamble capable or Non-ERP STA + Config/Architecture

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........C
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (284 bytes)
        Tag: ERP Information
            Tag Number: ERP Information (42)
            Tag length: 1
            ERP Information: 0x06
                .... ...0 = Non ERP Present: Not set
                .... ..1. = Use Protection: Set        # <<<<<-----|| Non-ERP STA Associated OR Non-ERP within the same BSS
                .... .1.. = Barker Preamble Mode: Set  # <<<<<-----|| Barker Pramble Mode Set by device Configuration or Architecture OR Non-ERP STA + not short preamble capable
                0000 0... = Reserved: 0x00
````
````py
# Barker Preamble Mode Wireshark Filter
# Option 3: Non-ERP STA + not short preamble capable or Non-ERP STA + Config/Architecture

wlan.erp_info.erp_present == 0 && wlan.erp_info.use_protection == 1 && wlan.erp_info.barker_preamble_mode == 1
````



### ERP Information Element












# Protection Mechanisms: `HT Protection` 

HT transmissions, are protected if there are other STAs present that cannot interpret HT transmissions correctly. The HT Protection and Nongreenfield HT STAs Present fields in the HT Operation element within Beacon and Probe Response frames are used to indicate the protection requirements for HT transmissions.

To ensure backward compatibility with older 802.11a/b/g radios, 802.11n (HT) access points may signal to other 802.11n stations when to use **one of four HT protection modes**. 

- **A field in the `beacon` frame, inside the `HT Information` element, called the `HT Protection` field has four possible settings of `0–3`**.

Much like an ERP (802.11g) AP, the protection modes may change dynamically depending on devices that are nearby or associated to the HT (802.11n) AP.

The protection mechanisms that are used are **RTS/CTS**, **CTS-to-Self**, **Dual-CTS**, or other protection methods.

## HT Protection: `HT Information Element`

**HT Information Element** is present in `beacons` & `probe responses` in both: **2.4 GHz band** and **5 GHz band**.

HT Information Element (IE) contains information about 802.11b/a/g stations in the BSS that are not capable of communicating HT-OFDM (802.11n) data rates. 

It also identifies if there's an adjacent Non-Greenfield BSS/AP and if Legacy Non-Greenfield device detected within the cell.

![image](https://github.com/user-attachments/assets/5f1c7ebd-7aa1-4392-bf03-075fad3b9e50)

````sh
# HT Information Element
# Beacon & Probe Responses

        Tag: HT Information (802.11n D1.10)
            Tag Number: HT Information (802.11n D1.10) (61)
            Tag length: 22
            Primary Channel: 11
            HT Information Subset (1 of 3): 0x0f
            HT Information Subset (2 of 3): 0x0000
                .... .... .... ..00 = HT Protection: No protection mode (0x0)
                .... .... .... .0.. = Non-greenfield STAs present: All associated STAs are greenfield capable
                .... .... .... 0... = Reserved: 0x0
                .... .... ...0 .... = OBSS non-HT STAs present: Use of protection for non-HT STAs by overlapping BSSs is not needed
                ...0 0000 000. .... = Channel Center Frequency Segment 2: 0
                000. .... .... .... = Reserved: 0x0
            HT Information Subset (3 of 3): 0x0000
            Rx Supported Modulation and Coding Scheme Set: Basic MCS Set
````

| **Field**                                                    | **Description**                                                                                                                                                                                                                      | **Wireshark Filter**                       |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Element ID                                                   | HT Information Element = 61                                                                                                                                                                                                          | `wlan.tag.number == 61`                    |
| Tag Length                                                   | Indicates the length of the HT Information Element (1 byte)                                                                                                                                                                          | `wlan.tag.length == 22`                    |
| Primary Channel                                              | Defines the primary operating channel                                                                                                                                                                                                | `wlan.ht.info.primarychannel == 11`        |
| HT Info Subset #1                                            | HEX combination for the HT Info Subset # 1                                                                                                                                                                                           | `wlan.ht.info.delim1 == 0x0f`              |
| **HT Info Subset #2**                                        | **HEX combination for the HT Info Subset # 2 - HT Protection**                                                                                                                                                                       | `wlan.ht.info.delim2 == 0x0000`            |
| HT Info Subset #3                                            | HEX combination for the HT Info Subset # 3                                                                                                                                                                                           | `wlan.ht.info.delim3 == 0x0000`            |
| ⚠️**HT Protection Mode 0: <br>No Protection / Greenfield**    | All STAs within the cell in primary or secondary channel are HT STAs and 20MHz/40MHz _(for 40MHz WLANs)_                                                                                                                             | `wlan.ht.info.ht_protection == 0x0`        |
| ⚠️**HT Protection Mode 1: <br>HT Non-Member Protection Mode** | **Non-HT STA is detected** in either the primary or the secondary channel (or both). **Not member of the same BSS**.                                                                                                                 | `wlan.ht.info.ht_protection == 0x1`        |
| ⚠️**HT Protection Mode 2: <br>20 MHz Protection Mode**        | The BSS is **20/40 MHz** & there is at least one **20 MHz HT STA associated** with this BSS                                                                                                                                          | `wlan.ht.info.ht_protection == 0x2`        |
| ⚠️**HT Protection Mode 3: <br>Non-HT Mixed Mode**             | **One ore more STAs Associated in the BSS are not HT (802.11n)**. _(Set only if non of any 3 other protection mechanisms (no protection mode / Greenfield, non-member protection mode, 20 MHz protection mode) are used.)_           | `wlan.ht.info.ht_protection == 0x3`        |
| 🍏**Non-greenfield STAs present**                             | **Legacy Non-Greenfield device detected within the cell**. One or more STAs detected in the primary or the secondary channel are **NOT** : HT STAs, either: 20/40 MHz HT STAs in a 20/40 MHz BSS, or 20 MHz HT STAs in a 20 MHz BSS. | `wlan.ht.info.greenfield == 1`             |
| _Reserved (bit)_                                             | _Reserved bit within the HT Information Element_                                                                                                                                                                                     | `wlan.ht.info.reserved_b11 == 0`           |
| 📊**Overlapping BSS Non-HT STAs Present**                     | a non-HT BSS is overlapping (eg. adjacent Wi-Fi Network). Beacons show 802.11b/g supported data rates.                                                                                                                               | `wlan.ht.info.obssnonht == 1`              |
| Channel Center Frequency Segment 2                           | For 802.11ac only. Center Frequency of the secondary segment for 80+80 MHz bandwidths. For 20, 40, 80, or 160 MHz bandwidths, is undefined.                                                                                          | `wlan.ht.info.chan_center_freq_seg_2 == 0` |
| _Reserved (HEX)_                                             | _Reserved bits within the HT Information Element_                                                                                                                                                                                    | `wlan.ht.info.reserved_b21_b23 == 0x0`     |
| Rx Supported Modulation and Coding Scheme (Basic MCS Set)    | Indicates supported MCS values for HT operation                                                                                                                                                                                      | `wlan.ht.mcsset`                           |


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
    - There is at least one 20 MHz HT (802.11n) STA associated in this BSS  <br><br>
- **`Mode 3`**: **non-HT Mixed Mode**: <br><br>
    - Used if one or more non-HT stations are associated in the BSS (All other cases).

### Operating Mode 0: `No Protection Mode / Greenfield Mode`

#### Analysis: `No Protection Mode / Greenfield Mode`

````sh
# Beacon Frame > Tagged Parameters > HT Information (subset 2)
# Mode 0 : No Protection Mode / Greenfield Mode

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (285 bytes)
        Tag: HT Information (802.11n D1.10)
            Tag Number: HT Information (802.11n D1.10) (61)
            Tag length: 22
            Primary Channel: 40
            HT Information Subset (1 of 3): 0x00
            HT Information Subset (2 of 3): 0x0000
                .... .... .... ..00 = HT Protection: No protection mode (0x0)                                  # <<<<<--------  Mode 0 : No Protection Mode / Greenfield Mode
                .... .... .... .0.. = Non-greenfield STAs present: All associated STAs are greenfield capable  # <<<<<--------  All STAs are Greenfield capable
                .... .... .... 0... = Reserved: 0x0
                .... .... ...0 .... = OBSS non-HT STAs present: Use of protection for non-HT STAs by overlapping BSSs is not needed
                ...0 0000 000. .... = Channel Center Frequency Segment 2: 0
                000. .... .... .... = Reserved: 0x0
            HT Information Subset (3 of 3): 0x0000
````

### Operating Mode 1:

#### Analysis Option 1: `HT non-Member` + `All associated STAs = Greenfield`

````sh
# Beacon Frame > Tagged Parameters > HT Information (subset 2)
# Mode 1 : HT non-member Protection Mode 

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (317 bytes)
            Tag Number: HT Information (802.11n D1.10) (61)
            Tag length: 22
            Primary Channel: 11
            HT Information Subset (1 of 3): 0x00
            HT Information Subset (2 of 3): 0x0001
                .... .... .... ..01 = HT Protection: HT non-member protection mode (0x1)                      # <<<<<--------  Mode 1 : HT non-member Protection Mode 
                .... .... .... .0.. = Non-greenfield STAs present: All associated STAs are greenfield capable # <<<<<--------  All associated STAs = Greenfield
                .... .... .... 0... = Reserved: 0x0
                .... .... ...0 .... = OBSS non-HT STAs present: Use of protection for non-HT STAs by overlapping BSSs is not needed
                ...0 0000 000. .... = Channel Center Frequency Segment 2: 0
                000. .... .... .... = Reserved: 0x0
            HT Information Subset (3 of 3): 0x0000
````

#### Analysis Option 2: `HT non-Member` + `1 or more associated STAs = non-Greenfield`

````sh
# Beacon Frame > Tagged Parameters > HT Information (subset 2)
# Mode 1 : HT non-member Protection Mode 

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (317 bytes)
            Tag Number: HT Information (802.11n D1.10) (61)
            Tag length: 22
            Primary Channel: 11
            HT Information Subset (1 of 3): 0x00
            HT Information Subset (2 of 3): 0x0005
                .... .... .... ..01 = HT Protection: HT non-member protection mode (0x1)                      # <<<<<--------  Mode 1 : HT non-member Protection Mode 
                .... .... .... .1.. = Non-greenfield STAs present: Non-greenfield STAs present                # <<<<<--------  Non Greenfield
                .... .... .... 0... = Reserved: 0x0
                .... .... ...0 .... = OBSS non-HT STAs present: Use of protection for non-HT STAs by overlapping BSSs is not needed
                ...0 0000 000. .... = Channel Center Frequency Segment 2: 0
                000. .... .... .... = Reserved: 0x0
            HT Information Subset (3 of 3): 0x0000
````


### Operating Mode 2: `20 MHz protection mode`

#### Analysis: `20 MHz protection mode` + `1 or more associated STAs = non-Greenfield`

````sh
# Beacon Frame > Tagged Parameters > HT Information (subset 2)
# Mode 2 : 20 MHz protection mode

802.11 radio information
IEEE 802.11 Beacon frame, Flags: ........
IEEE 802.11 Wireless Management
    Fixed parameters (12 bytes)
    Tagged parameters (317 bytes)
            Tag Number: HT Information (802.11n D1.10) (61)
            Tag length: 22
            Primary Channel: 11
            HT Information Subset (1 of 3): 0x00
            HT Information Subset (2 of 3): 0x0006
                .... .... .... ..10 = HT Protection: 20 MHz protection mode (0x2)
                .... .... .... .1.. = Non-greenfield STAs present: One or more associated STAs are not greenfield capable
                .... .... .... 0... = Reserved: 0x0
                .... .... ...0 .... = OBSS non-HT STAs present: Use of protection for non-HT STAs by overlapping BSSs is not needed
                ...0 0000 000. .... = Channel Center Frequency Segment 2: 0
                000. .... .... .... = Reserved: 0x0
            HT Information Subset (3 of 3): 0x0000
````


### Operating Mode 3: `non-HT Mixed Mode`












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





## HT Protection: Overlapping BSS



The OBSS Non-HT STAs Present field allows HT devices to report the presence of other non-HT STAs that cannot interpret the HT transmissions correctly. See 9.13.3 (Protection mechanisms for different HT PHY options).
A second HT AP that detects a first HT AP’s beacon with the OBSS Non-HT STAs Present field set to 1 may, in conjunction with radio resource measurements and/or heuristics, cause greenfield and RIFS sequence transmissions of the second AP’s BSS to be protected by setting the Operating Mode field to 3. If the NonERP_Present bit is set to 1 in the first AP’s beacon, then the Use_Protection bit to 1 may also be set to 1 by the second AP.  See Annex n061818

HT STAs may also scan for the presence of non-HT devices either autonomously or after the STA’s AP transmits a HT Information element with the Operating Mode field set to 1. Non-HT devices may be detected as follows :
•	one or more non-HT STAs are associated 
•	a non-HT BSS is overlapping (a non-HT BSS may be detected by the reception of a Beacon where the supported rates only contain clause 15, 17, 18 or 19 rates)
•	management frame (excluding a Probe Request) is received where the supported rate set includes only Clause 15, 17, 18 and 19 rates. 
•	or when a HT Information element with OBSS Non-HT STAs Present field equal to 1 is received. 


When non-HT devices are detected, the STA may enable protection of its Greenfield and RIFS sequence transmissions.


Set to 1 if the use of protection for non-HT STAs by overlapping BSSs is determined to be desirable. Examples of when this bit may be set to 1 include, but are not limited to, when 

•	one or more non-HT STAs are associated 
•	a non-HT BSS is overlapping (a non-HT BSS may be detected by the reception of a Beacon where the supported rates only contain clause 15, 17, 18 or 19 rates)
•	a management frame (excluding a Probe Request) is received where the supported rate set includes only Clause 15, 17, 18 and 19 rates. 
Set to 0 otherwise. 





# Protection Mechanisms: `VHT`

Since 802.11ac does not operate on the 2.4 GHz bands, it does not have to worry about 802.11b, 802.11g, or 2.4 GHz 802.11n radios. 802.11a and 802.11n radios all all PHYs use the OFDM preamble. When a transmission is performed using any of these PHYs, the other radios hear the preamble and can calculate how long to wait before they can transmit.

But for hidden node problems and to determine when channels are available, 802.11ac defines an enhanced Request to Send/Clear to Send (RTS/CTS) mechanism. The mechanism is as follows:

An 802.11ac device sends an RTS. Basic 802.11a transmission, which is 20 MHz wide, is replicated another three times to fill the 80 MHz or another seven times to fill 160 MHz. Each nearby device, regardless of whether the primary channel is the 20 MHz channel over the 80 MHz or 160 MHz channel, can receive the RTS. Each device that receives the RTS sets virtual sub-channels in busy state.

The device that receives the RTS checks whether the primary channel or sub-channels of the 80 MHz channel are busy. If some channel bandwidth is used, the receiver replies with a CTS with available bandwidth and reports repeated bandwidth.
A CTS is sent over each available 20 MHz sub-channel.

The sender can learn available and unavailable channels. Then data is sent only over available sub-channels.

![image](https://github.com/user-attachments/assets/d1b18b0a-755e-44da-89e1-54e367744550)
_Comparation between 802.11n and 802.11ac. In 802.11n, if a sub-channel is unavailable, the entire bandwidth is unavailable. In 802.11ac, if some sub-channels are unavailable, other sub-channels can still be used to send data._



# Protection Mechanisms: `HE`

Wi-Fi 6 requires backward compatibility with 802.11/a/b/g/n/ac, which means that RTS/CTS protection mechanisms must be used. RTS/CTS creates overhead and consumes airtime.



## Resources

- [802.11 Protection Mechanisms _@ Nayarasi_](https://mrncciew.com/2014/11/02/cwap-802-11-protection-mechanism/) _`Nayarasi`_
- [Protection Ripple in ERP 802.11 WLANs](https://www.cwnp.com/uploads/protection_ripple_in_erp_802-11_wlans.pdf) _`whitepaper`_
- [802.11n Protection Mechanisms: Part 1 @ _CWNP_](https://www.cwnp.com/802-11n-protection-mechanisms-part-1/) _`whitepaper`_
- [802.11n Protection Mechanisms: Part 2 @ _CWNP_](https://www.cwnp.com/802-11n-protection-mechanisms-part-2/) _`whitepaper`_
- [Protection Ripple in ERP 802.11 WLANs @ _CWNP_](https://www.cwnp.com/uploads/protection_ripple_in_erp_802-11_wlans.pdf) _`whitepaper`_
- [HT Protection Mechanisms](https://dot11ap.wordpress.com/ht-protection-mechanisms/) _`definitions`_

- https://myknowledgebits.com/chapter-2-rts-to-cts-and-cts-to-self/

- https://www.extremenetworks.com/resources/blogs/backward-compatibility-the-double-edged-sword-of-wi-fi-performance-and-connectivity


- https://davidhoglund.typepad.com/files/white_paper_c11-713103.pdf


- https://dot11ap.wordpress.com/cwna/radio-frequency-rf-technologies/space-time-block-coding-stbc/

- [ERP in WiFi](https://www.youtube.com/watch?v=gfUyMj_xYMU)
- [ERP Prtection MEchanisms](https://www.youtube.com/watch?v=MxJPNrOftEs)
- [HT operation modes in WiFi](https://www.youtube.com/watch?v=hjYJkQbXss0)
- [HT Prtection MEchanisms](https://www.youtube.com/watch?v=n9d9Q-M70_k)




- https://dot11ap.wordpress.com/vht-protection-mechanisms/


- [Wi-Fi 6 for dummies](https://www.redwaynetworks.com/wp-content/uploads/Wi-Fi-6-FD_-Extreme-Networks-Special-Edition-_1_.pdf)

- https://support.huawei.com/enterprise/en/doc/EDOC1100081215


- https://gjermundsblog.wordpress.com/wp-content/uploads/2019/08/mu-rts_cts_final.pdf
- https://gjermundraaen.com/2019/08/23/he-mu-rts-and-cts-deep-dive/


- https://www.youtube.com/watch?app=desktop&v=hjYJkQbXss0

- https://www.youtube.com/watch?v=twiOOo8LI9w

rts cts attack
- https://arxiv.org/pdf/1811.11128

- https://www.youtube.com/watch?v=-B9_4zQLwyo&t=2381s


- https://networkengineering.stackexchange.com/questions/58588/why-is-there-no-contention-window-after-a-difs-interval-on-the-first-transmissio


- https://mrncciew.com/2014/10/26/cwap-802-11-ctrl-rtscts/

- https://www.oreilly.com/library/view/80211-wireless-networks/0596100523/ch04.html

- https://www.geeksforgeeks.org/how-rts-and-cts-are-used-to-avoid-collision-in-csma-ca/

- https://wiki.sj.ifsc.edu.br/index.php/PJI11103:_Redes_sem-fio_IEEE_802.11


Buena presentaicon
- https://slideplayer.com/slide/14020063/

SIFS bueno:
- https://telcomatraining.com/what-is-sifs-short-interframe-space/


MAC Frames and formats:

- https://howiwifi.com/2020/07/13/802-11-frame-types-and-formats/



backoff con el indian

- https://www.youtube.com/watch?v=sK1wxkDXzEo

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


