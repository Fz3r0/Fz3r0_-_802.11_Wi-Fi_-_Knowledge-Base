# 🛜🔋🛑 MAC Operations: `Protection Mechanisms`

There are 2 types of MAC Operations: **Power Management** & **Protection Mechanisms**:

1. **`Power Management`** is allow the radio to go to sleep (just few microseconds), because if the antenna/adapter keeps awake all the time is consuming battery all the time, in a movile device can degrade battery life. Power management it's just turning on the antenna, send/recieve the frame, then "doze" or "sleep" the antenna and so on. The hint here is, that the STA does not lose any frame even if it's sleeping <br><br>
2. **`Protection Mechanisms`** allow newer devices to communicate and "exist" in a world where older devices also exists (eg. devices using 802.11b(HR-DSSS) can coexist with newer devices using 802.11g(ERP) or even newest devices like 802.11n/ac/ax(OFDM)).

# 🛑🛜🚦 MAC Operations: `Protection Mechanisms`
_HR/DSSS STAs (802.11b legacy) does not understand OFDM Modulation used by ERP STAs. But, HT/ERP/OFDM (802.11n modern) STAs are backwards compatible with HR/DSSS STAs & can transmit & understand HR/DSSS modulation | The way to acomplish that is using RTS/CTS mechanisms in case that legacy STAs are using the same AP of modern devices | RTS/CTS are the most used mechanism in Wi-Fi, there's also a mechanism called CTS-to-self that is not a frame defined in the standard, this frame is a CTS frame without a preciding RTS frame, this is usually done by the AP | ERP element is present only on 2.4GHz network supporting 802.11g & it is present in beacon & probe responses. The non-ERP_Present bit set to 1 in following conditions a. A nonERP station (legacy 802.11 or 802.11b) associate to the cell, b. A neighboring cell is detected, allowing only nonERP data rates, c. Any other management frame (except probe request) is received from neighboring cell supporting only nonERP data rates. | To ensure backward compatibility with older 802.11a/b/g radios, 802.11n (HT) access points may signal to other 802.11n stations when to use one of four HT protection modes.| A field in the beacon frame called the HT Protection field has four possible settings of 0–3._

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

- [802.11 Protection Mechanisms _@ Nayarasi_](https://mrncciew.com/2014/11/02/cwap-802-11-protection-mechanism/) _`Nayarasi`_
- [Protection Ripple in ERP 802.11 WLANs](https://www.cwnp.com/uploads/protection_ripple_in_erp_802-11_wlans.pdf) _`whitepaper`_
- [802.11n Protection Mechanisms: Part 1 @ _CWNP_](https://www.cwnp.com/802-11n-protection-mechanisms-part-1/) _`whitepaper`_
- [802.11n Protection Mechanisms: Part 2 @ _CWNP_](https://www.cwnp.com/802-11n-protection-mechanisms-part-2/) _`whitepaper`_
- [Protection Ripple in ERP 802.11 WLANs @ _CWNP_](https://www.cwnp.com/uploads/protection_ripple_in_erp_802-11_wlans.pdf) _`whitepaper`_
- [HT Protection Mechanisms](https://dot11ap.wordpress.com/ht-protection-mechanisms/) _`definitions`_



