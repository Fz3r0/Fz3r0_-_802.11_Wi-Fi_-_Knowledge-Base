# 🙋🛜🚦MAC Operations: `Protection Mechanisms`

There are 2 types of MAC Operations: **Power Management** & **Protection Mechanisms**:

1. **`Power Management`** is allow the radio to go to sleep (just few microseconds), because if the antenna/adapter keeps awake all the time is consuming battery all the time, in a movile device can degrade battery life. Power management it's just turning on the antenna, send/recieve the frame, then "doze" or "sleep" the antenna and so on. The hint here is, that the STA does not lose any frame even if it's sleeping <br><br>
2. **`Protection Mechanisms`** allow newer devices to communicate and "exist" in a world where older devices also exists (eg. devices using 802.11b(HR-DSSS) can coexist with newer devices using 802.11g(ERP) or even newest devices like 802.11n/ac/ax(OFDM)).

# 🙋🛜🚦 `Protection Mechanisms`

802.11 (Wi-Fi) networks allows for backward compatibility with previous generations (eg. Wi-Fi 4 (802.11n) is backward compatible with Wi-Fi 1 or Wi-Fi 3 (802.11b/g)). This is one reason the technology is so popular, people can upgrade their devices at their own pace, without worrying about whether their old ones will still work. 

HR/DSSS (802.11b legacy Wi-Fi-1) STAs does not understand OFDM Modulation used by ERP (802.11g Wi-Fi-3) STAs, but HT/ERP/OFDM (802.11n Wi-Fi-4 {modern}) STAs are backwards compatible with HR/DSSS STAs & can transmit & understand HR/DSSS modulation. The way to acomplish that is using RTS/CTS mechanisms in case that legacy STAs are using the same AP of modern devices.

RTS/CTS are the most used mechanism in Wi-Fi, there's also a mechanism called CTS-to-self that is not a frame defined in the standard, this frame is a CTS frame without a preciding RTS frame, this is usually done by the AP.

**`Important`**: Wi-Fi backward compatibility has long been a double-edged sword because backward copatibility brings some drawbacks for newer STAs using the same BSS witn legacy STAs nearby llike **RTS/CTS Overhead**, **Airtime Consumption** or **Connectivity Problems**. But, for the first time in 20 years, Wi-Fi does not require backward compatibility. This is because Wi-Fi 6E and the 6 GHz frequency band. There is no need for RTS/CTS protection mechanisms for legacy Wi-Fi devices in 6 GHz, legacy clients do not consume airtime while transmitting using slow data rates.  This is because Wi-Fi is brand new to 6 GHz, and there are no legacy clients. Altough in the future maybe we will need backward compatibility again in Wi-Fi 7, Wi-Fi 8, and Wi-Fi 9 if they still using 6 GHz band. 


## 🙋🛜🚦 Protection Mechanisms: `Hidden Node`

**RTS/CTS (Request-to-Send / Clear-to-Send)** is the most used mechanism in Wi-Fi; this mechanism is an optional method that is used in `Virtual Carrier Sense` to avoid `hidden node` problems. 



Tu understand RTS/CTS we must understand what is `hidden node` problems first. In the below diagram, there is an access point node A indicated by blue. Nodes B and C are wireless devices within the AP – A’s BSS. However, B and C cannot hear each other due to network congestion or they are outside each other’s BSS and are called hidden nodes. Due to this, physical carrier sensing by B and C will never indicate that medium is busy when either one of them is transmitting in the air and could result in corruption and distortion of signal. To avoid this situation, we can use RTS-CTS mechanism.

![image](https://github.com/user-attachments/assets/f8fe7a9f-6dc1-47f1-906b-afca7c174f81)

Any 802.11 device that wishes to transmit in the medium should send `RTS (Request to Send)` frame – **requesting for medium access to the AP**. The latter then responds with `CTS (Clear to Send)` frame that includes the `Duration field`, which helps the station to set its `NAV timer`. 

## 🙋🛜🚦 Protection Mechanisms: `Duration Field`

The `Duration Field` determine the **time in microseconds (μs)** needed to complete the Frame Exchange. This is measured **AFTER the current frame**, this means: what is left after the current frame.

**There are 3 different main Duration Values types:**

1. **Data Exchange** _(AKA RTS Data Exchange)_ = `SIFS` + `Ack`
2. **RTS/CTS Data Exchange** = `x3 SIFS` + `CTS` + `Data` + `ACK`
3. **CTS-to-Self Data Exchange** = `x2 SIFS` + `Data` + `ACK`


````py
## Duration Values >> Data Exchange (AKA RTS Data Exchange):

   # In a Data Exchange scenario the Duration is equal the exchange AFTER the Data Frame:
   
       #   SIFS + Ack:

                                      ._______________________________.        ._______.
                                DIFS  |             Data              |  SIFS  |  Ack  |
                              __________________________________________________________  
                                                                       <--------------->  <<<--- Data Duration =  SIFS + Ack
                                                                                      <>  <<<--- Ack Duration  =  0

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Duration Values >> RTS/CTS Data Exchange:

   # In a Data Exchange where RTS/CTS is used, Duration is equal the exchange AFTER the RTS Frame:
   
       #   x3 SIFS + CTS + Data + ACK:
                              
        ._____.        ._____.        ._______________________________.        ._______.
  DIFS  | RTS |  SIFS  | CTS |  SIFS  |             Data              |  SIFS  |  Ack  |
________________________________________________________________________________________
               <----------------------------------------------------------------------->  <<<--- RTS Duration  =  x3 SIFS + CTS + Data + ACK
                              <-------------------------------------------------------->  <<<--- CTS Duration  =  x2 SIFS + Data + ACK
                                                                       <--------------->  <<<--- Data Duration =  SIFS + Ack
                                                                                      <>  <<<--- Ack Duration  =  0

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Duration Values >> CTS-to-Self Data Exchange:

   # In a Data Exchange where CTS-to-Self is used, Duration is equal the exchange AFTER the CTS Frame:
   
       #   x2 SIFS + Data + ACK:

                       ._____.        ._______________________________.        ._______.
                       | CTS |  SIFS  |             Data              |  SIFS  |  Ack  |
                       _________________________________________________________________
                              <-------------------------------------------------------->  <<<--- CTS Duration  =  x2 SIFS + Data + ACK
                                                                       <--------------->  <<<--- Data Duration =  SIFS + Ack
                                                                                      <>  <<<--- Ack Duration  =  0
````

![image](https://github.com/user-attachments/assets/21ce6e81-e16b-4591-869e-72d037dcd388)

![image](https://github.com/user-attachments/assets/62cdb44f-c40d-4a5c-97d0-19f777722445)

![image](https://github.com/user-attachments/assets/27f321f3-46d8-44a9-b4f3-5c555192c51d)


Once the medium is free, the client STA can access the medium for wireless transmissions. For every frame transmitted in air, there should be an ACK from the AP. There is a SIFs delay between each frame: RTS, CTS, DATA and ACK frames. At times, this mechanism can create a lot of overhead in the network leading to a lot of congestion. And hence, this can be enabled only if the frame size is equal or above a specific configured threshold that depends on the network.








## 🙋🤳🏻📡 Protection Mechanisms: `RTS/CTS` _(802.11g or newer)_ 





![image](https://github.com/user-attachments/assets/fc8d7516-dc1d-453f-a7eb-45bd1a8440bc)


![image](https://github.com/user-attachments/assets/20a9ebb3-8ab3-42b0-a5f1-f4ffb0085f75)


![image](https://github.com/user-attachments/assets/1c169f74-c3ac-4905-b794-b8ce05f86b29)




## 🙋📡📡 Protection Mechanisms: `CTS-to-self` _(802.11g or newer)_ 

It is not a frame defined in the standard, this frame is a CTS frame without a preciding RTS frame, this is usually done by the AP 

- CTS-to-Self is simply another method of performing NAV distribution & that use only CTS frames.

- It is used strictly as protection mechanism for mixed mode environment.

- The CTS-to-self NAV distribution mechanism is lower in network overhead cost than is the RTS/CTS NAV distribution mechanism, but CTS-to-self is less robust against hidden nodes and collisions than RTS/CTS.

- STAs employing a NAV distribution mechanism should choose a mechanism such as CTS-to-self or RTS/CTS that is appropriate for the given network conditions.

- # If errors occur when employing the CTS-to-self mechanism, STAs should switch to a more robust mechanism.

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

**Protection Modes Information Elements** are present in `Beacons` & `Probes`:

- `ERP Information Element`: Present in 2.4 GHz Beacons & Probes
- `HT Information Element`: Present in 2.4 & 5 GHz Beacons & Probes

### Information Elements: `2.4 GHz`

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

### Information Elements: `5 GHz`

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

## ERP & HT Protection: Difference Between `802.11g (ERP)` & `802.11n (HT)`

When 802.11g was introduced, we had RTS/CTS and CTS-to-Self protection mechanisms.  What do we get with 802.11n so that it's backwards compatible with 802.11a and 802.1b/g? First, there's a couple of new things I'd like to introduce, and then we'll get to the protection rules.

- **`802.11g` = `ERP`**: In an **ERP Beacon**, ERP stations look at the **ERP Information Element** to determine whether or not protection is necessary in the BSS
- **`802.11n` = `HT`**: In an **HT Beacon**, HT stations use the **Operating Mode** and **Non-greenfield STAs Present** fields in the **HT Information Element** to determine whether or not to use protection.





# Protection Mechanisms: `ERP Protection` - 

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

**ERP element** is present in `beacon` & `probe responses` **only on 2.4GHz band**.

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


## HT protection mechanisms

HT transmissions, are protected if there are other STAs present that cannot interpret HT transmissions correctly. The HT Protection and Nongreenfield HT STAs Present fields in the HT Operation element within Beacon and Probe Response frames are used to indicate the protection requirements for HT transmissions.


To ensure backward compatibility with older 802.11a/b/g radios, 802.11n (HT) access points may signal to other 802.11n stations when to use one of four HT protection modes. A field in the beacon frame called the HT Protection field has four possible settings of 0–3.

Much like an ERP (802.11g) access point, the protection modes may change dynamically depending on devices that are nearby or associated to the HT (802.11n) access point.

The protection mechanisms that are used are RTS/CTS, CTS-to-Self, Dual-CTS, or other protection methods.



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


rts cts attack
- https://arxiv.org/pdf/1811.11128
