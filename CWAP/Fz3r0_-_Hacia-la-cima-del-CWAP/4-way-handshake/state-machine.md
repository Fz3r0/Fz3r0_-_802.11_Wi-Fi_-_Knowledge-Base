# 🪆🛜⚙️ 802.11 State Machine: `Discovery`, `Authentication`, `Association`, `Transition` & `Disconnection`

The 802.11 state machine describes the process a client (STA) undergoes when connecting to a wireless network, with four key states: Discovery, Authentication, Association, and Transition, concluding with Disconnection. maintain connections.

- It consists of the **four states** of client connectivity during a session, from disconnected to fully authorized/associated via secure authentication.
- Considered as "The discovery/connection/transition/disconnection process" of a client in a BSS at a protocol level (Frame exchange process).
- Any Client Station or Access Point (STA or AP) can be in some "state" within this state machine at any given time (State 1, State 2, State 3, State 4).
- Each client and Access Point (AP) follows this state machine to manage and maintain connections.

Most common issues to torubleshoot are Connectivity Problems, this means: 

- STAs/Clients either can't connect, can't maintain it's connection, it's not roaming well between APs, it can't connect to the SSID, and so on...

Understanding this kind of Frame Exchanges help to analyze step by step the process for BSS Discovery & Joining, Analyze Roaming Behavior, etc.

## Open System Authentication

Modern networks does not "authenticate" clients, instead uses "open system authentication". 

Open System Authentication is when STA send Auth Req & AP responds with Auth Res, then the same with Asso Res/Res at this point they are at "state 3" (where open authentication reach), then is where we use RSN method is used (like 802.1X EAP or WPA2 PSK) to make a "real authentication", and that take us finally to state 4 "Fully connected to the network" 


## 802.11 State Machine: Authentication & Association

The 802.11 station keeps two variables for tracking the **authentication state** and the **association state**. The states that are tracked are as follows:

1. `Authentication state`: unauthenticated or authenticated
2. `Association state`: unassociated or associated

Together, these two variables create three possible states for the stations.

- `State 1`: initial start state :: unauthenticated and unassociated
- `State 2`: Authentication state :: authenticated and unassociated
- `State 3`: Association state :: and associated _(pending security mechanisms / RSNA)_

**Note:** Because a station must authenticate before it can associate, it can never be unauthenticated and associated. 

Since the introduction of 802.11i security mechanisms, the IEEE 802.11-2012 standard now considers there to a forth state in the connection state machine (State 4: authenticated and associated – PSK or 802.1X security mechanisms completed.):

## ⛔➡️✅ 802.11 State Machine: `4 States`

| **State #**        | **State Name**                 | **Description**                                                  | **Frame Classes**      | **RSNA**                    |
|--------------------|--------------------------------|---------------------------------------------------------------------|------------------------|-----------------------------|
| ⛔ **State 1**     | Unauthenticated, Unassociated |  Client STA NOT Connected                                           | Class 1               | /                           |
| ❓ **State 2**     | `Authenticated`, Unassociated |  Client STA Authenticated to AP _(AP validating STA capabilities)_  | Class 1 & 2           | /                           |
| ✅ **State 3**     | `Authenticated`, `Associated` |  Client STA Associated to AP _(open-auth)_                          | Class 1, 2 & 3        | RSNA: Blocked (Pending RSNA) |
| 🔓 **State 4**     | `Authenticated`, `Associated`   |  Client STA Associated to AP _(RSNA)_                               | Class 1, 2 & 3        | RSNA: Un-Blocked (RSNA OK!)  |

### 🥇🥈🥉 802.11 State Machine: `Frame Classes` `1`, `2`, `3`

**🥇🖽 `Class1 Frames`**

- [**Control**: `RTS & CTS`, `ACK`, `CF-End+CF-Ack & CF-End`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Management**: `Beacon`, `Probe Req/Res`, `Auth/Deauth`, `ATIM`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Data**: `Any frame with ToDS & FromDS false(0)`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)<br><br>

**🥈🖽 `Class2 Frames`

- [**Control**: _None_](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Management**: `Association Req/Res`, `Re-Association Req/Res`. `Disassociation`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Data**: _None_](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)<br><br>

**🥉🖽 `Class3 Frames`

- [**Control**: `PS-Poll`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Management**: `Deauthentication`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)
- [**Data**: `Any frame with ToDS or FromDS true(1)`](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)

     
![image](https://github.com/user-attachments/assets/ca557eaf-fda8-431e-aca5-9c393fff14b4)

![image](https://github.com/user-attachments/assets/45325a13-68b4-409a-84c3-8a11b4fe9ed4)

![WPA2-PSK-Association-Fz3r0_Password123](https://github.com/user-attachments/assets/12639f76-8ecd-4096-a7c3-52873ae38532)

      


# 🤳🏾🛸📡 IEEE 802.11: `BSS Discovery` 

To join any network first client or station needs to find it the network. In the wired network, just plugging the cable or jack will find the network. In the wireless world, this requires identification of the compatible network before joining process can begin. This identification process of the network is referred as `scanning` and its part of the `BSS Discovery` process.

## 🛸🔍 BSS Discovery: `Scanning`

Several parameters are needed in the scanning process. These parameters are: 

- BSSType
- BSSID
- channel list
- scantype
- MinChannelTime
- MaxChannelTime.

The parameters are set as default depending upon manufacturer Wi-Fi driver, but it can be modified by the user i.e. if the requirement is for hidden network then we can set scantype parameter as passive scan because the active scan is not useful for the hidden network (networks that do not broadcast their SSID).

There are two scanning methods: `passive scanning` and `active scanning`.

- By default, radios perform both the types of scanning on all the channels allowed by the country of operation.
- While both the types of scanning are available by default, active scanning is performed only by those channels that are allowed to transmit by regional government regulations.
- Channels that are not authorized for unlicensed use are excluded from active scanning.

### 🛸📡 BSS Discovery Scanning Methods: `Passive Scanning`

The **beacon** is broadcasted periodically by the AP to advertise its presence and SSID without requiring any action from the client device. STAs listen to these beacons to discover available networks.

- `AP`: **init effort of finding a STA, sending the announcement of a SSID**
- `AP`: Broadcast: `Beacon` (Only one channel) : AP send a beacon frame to the BSA announcing the SSID, waiting for a directed probe request from any STA who "heard" the beacon.
- `client STA`: Unicast: `Probe Request` (Directed Probe) : If any STA used the beacon in passive scanning mode, will answer with a `Directed Probe Response` 
- Not so used today by smartphones or computers, but still in use. 

### 🛸🤳🏾 BSS Discovery Scanning Methods: `Active Scanning`

The **probe response** frame is used in active scanning. In this case, the **STA initiates the discovery process by sending a probe request (often as a broadcast)** to inquire about available networks. **The AP responds with a probe response**, which provides detailed information about the network, often including more specific details about vendor-specific capabilities.

- `client STA`: **init effort of finding an AP**
- `client STA`: Broadcast: `Probe Request` (All Channels) : STA trying to find any SSID broadcasting around with any name. 
- `client STA`: Unicast: `Probe Request` (Directed Probe) : If any AP answers the first broadcast probe with a `Directed Probe Response` (or the STA already knows the SSID)
- The most used method today by client STAs like smartphones or computers. 

## 🛸📢 BSS Discovery: `Beacon` VS `Probe Response`

The beacon and probe response frames are sent by the AP to start/continue the dicovery process (depending on the scanning method: Passive (beacon) or Active (probe response)):

**The beacon frame and the probe response at the protocol level (e.g., as seen in Wireshark) are almost identical**, with the main differences being:

- **The `beacon frame` contains a `Traffic Indication Map (TIM)` element, which is used for power management (PS)**. **`Probe responses` will NEVER contain a TIM**. The TIM element informs client STAs if there is buffered traffic waiting for them at the AP, using the beacon frame. **This is the most important differente between a beacon and a probe response at protocol perspective**. <br><br>
- The content of `vendor-specific elements` can vary depending on the vendor or deployment. However, in general, **`probe responses` tend to include more detailed vendor-specific information compared to `beacons`**. This is because probe responses are tailored to a specific request from a client device (STA), while beacons are more generic. For example, in the next probe response screenshoot, it is noticeable that there is much more information in the vendor-specific elements than in the beacon. Most of this data comes from the WPS announcement _(even though we will not be using WPS authentication for this lab)_.

### 📢🔎 Beacon (From: AP):

![beacon_frame](https://github.com/user-attachments/assets/44e72191-5f7e-42be-a95e-5aa1310adbcb)

### 🛸🔎 Probe Request (From: AP):

![probe_response_frame](https://github.com/user-attachments/assets/e5edabdb-45a0-4eba-81ff-48d3bf4f9838)

🛸📢 BSS Discovery: `Probe Request` VS `Directed Probe Request`

A Probe Request is a broadcast frame sent by a client STA when it actively searches for available networks in its vicinity. This can happen when a client device wants to discover networks without having a specific one in mind. Probe Requests are utilized in both active scanning and passive scanning scenarios:

- Active Scanning: The client STA actively sends a Probe Request frame without specifying a particular SSID (Service Set Identifier). This request is essentially a query to all APs within the Basic Service Area (BSA) for available networks. <br><br>
- Passive Scanning: Alternatively, if the STA has been using passive scanning—listening to beacon frames broadcast by APs—it may still send a Probe Request if it has yet to receive sufficient network information. <br><br>

Probe Request

- The Probe Request typically does not contain an SSID field or uses a wildcard SSID (null SSID), signaling to all APs in the area that the client is seeking any available network.
- Upon receiving a broadcast Probe Request, any AP within range may respond with a Probe Response, providing the client STA with details such as the network’s SSID, supported data rates, and security configurations.

Probe Request (Directed)

## 🪪🛡️🔐 State 1 to State 2: `Authentication`
_| _

### 🛡️🔐 Authentication Methods

IEEE Std 802.11 defines five 802.11 authentication methods that a STA can use to access to a BSS:

1. 🔓 Open System authentication: Admits any STA to the DS || Used for modern RSNA: `802.11i`(**PSK**, **802.1X**) _(after association state)_
2. 🔑 Shared Key authentication: Relies on WEP (LEGACY) to demonstrate knowledge of a WEP encryption key
3. 🔄 FT authentication: Authenticates STAs using a key derived from previous authentication (keys derived during the initial mobility domain association) as defined in Clause 12 (Fast BSS transition) || For `802.11r` FT 
4. 🌉 SAE Authentication: Uses finite field cryptography to prove knowledge of a shared password || For `WPA3` or `802.11s` (Diffie-Hellman/Mesh)
5. 🚀 FILS Authentication: Uses three alternative procedures. (Minimize the time required for the initial link setup (for high density networks))




These are the Authentication Methods a STA can use to access to a BSS: 

- [802.11 Authentication Methods](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/46509dcd-047a-4529-b4c5-c9cad8b88760) _`table`_
- [IEEE	Access control and data confidentiality services: Open System, Shared Key, FT, SAE & FILS ](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/files/13836501/11-13-1488-02-00ai-comment-resolution-for-section-4.docx) _`word report`_ <br><br>
    - [🔓 `Open System` :: `0`](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/da6135ed-352d-42c1-a73a-736112c79650) No authentication | Every client is allowed || used for modern: `802.11i`(`PSK`, `802.1X`) (after association state)
    - [🔑 `Shared Key` :: `1`]() Authenticates via WEP demonstrating a key :: Legacy Networks (modern uses open system)
    - [🔄 `FT - Fast Transition` :: `2`]() `802.11r` Authenticates using a key derived from previous authentication
    - [🌉 `SAE`:`Simultaneous Authentication of Equals` :: `3`]() `WPA3` || `802.11s-mesh` Diffie-Hellman / Mesh
    - [🚀 `FILS`: `Fast Inistial Link Setup:: `4`](https://mrncciew.com/2023/09/25/fils-fast-initial-link-setup/) Minimize the time required for the initial link setup (for high density)

### 📡🪪 Wi-Fi Connection Manager Protocols
_To facilitate Wi-Fi connectivity, the industry introduced WISPr 1.0, a protocol which automated the exchange of user name/password credentials with public Wi-Fi HotSpots. | In 2010, Accuris introduced WISPr 1+ extensions to the WISPr protocol which overcame the security flaws and subscriber management complexity of the initial specification. | Today WISPr 1+ is used by Wi-Fi roaming service providers worldwide to offer seamless, secure access and authentication on WISPr-enabled Wi-Fi networks. | Wi-Fi Hotspots need to support 802.1X technology as part of a HotSpot 2.0 upgrade. While many do, WISPr continues to be the predominant access mechanism. With WISPr 1+, service providers are able to bring a SIM-like authentication to non-SIM devices and non-802.1X Wi-Fi alike, and to an installed base of Smartphones which doesn’t support EAP-SIM/AKA today._
- [Connection Manager Protocols Differences :: WISPr 1.0 VS 802.1X VS Passpoint Release 2 VS WISPr 1+](https://info.accuris-networks.com/hubfs/Documents/WISPr1_DS-07Jan16.pdf)

# 🛡️🔓🪪 Authentication Method: `Open System`
_Once a client station is discover a SSID (Probe Request/Response or listening to Beacons) it move to Join phase. This exchange comprise of at least 4 frames || Open System authentication should never fail || Init method of authentication used by most modern WLANs || RSN like 802.1X or PSK is performed later (state 3 > 4) || There is no "authentication response frame", it's just an "autentication frame" with another status code value || Association process is similar to authentication, in this caso we do have "authentication request" & "authentication response" (both ACKed) ||_

### Open System Authentication: `No RSN`

````py
######################################################################################################################
                                 🏁 STATE MACHINE = 1 :: client STA disconnected from AP 🏁
######################################################################################################################

🛸 BROADCAST   :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛸 Beacon ]}  (optional/passive scanning) 

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊❓ Probe Request ]}   (active scanning)   <<<=== START 🏁

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊❓ Probe Response ]}  

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]} 

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚪 Authentication SeqNum=1 (request) ]} 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🚪 Authentication SeqNum=2 (success) ]} 

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊🆗 ACK ]}                                 <<<=== FINISH 🏁

######################################################################################################################
                                🏁 STATE MACHINE = 2 :: client STA authenticated to AP 🏁
######################################################################################################################

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🛜 Association Request ]}                 <<<=== START 🏁

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Association Response ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]}                                 <<<=== FINISH 🏁

######################################################################################################################
                               🏁 STATE MACHINE = 3 :: client STA associated to AP
                                Open System Authentication/Association Complete!!!
######################################################################################################################

````

---

### Open System Authentication: `RSN :: WPA2`

````py
######################################################################################################################
                                 🏁 STATE MACHINE = 1 :: client STA disconnected from AP 🏁
######################################################################################################################

🛸 BROADCAST   :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛸 Beacon ]}  (optional/passive scanning) 

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊❓ Probe Request ]}   (active scanning)   <<<=== START 🏁

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊❓ Probe Response ]}  

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]} 

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚪 Authentication SeqNum=1 (request) ]} 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🚪 Authentication SeqNum=2 (success) ]} 

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊🆗 ACK ]}                                 <<<=== FINISH 🏁

######################################################################################################################
                                🏁 STATE MACHINE = 2 :: client STA authenticated to AP 🏁
######################################################################################################################

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🛜 Association Request ]}                 <<<=== START 🏁

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Association Response ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]}                                 <<<=== FINISH 🏁

######################################################################################################################
                                 🏁 STATE MACHINE = 3 :: client STA associated to AP 🏁
######################################################################################################################

# - BOTH CLIENTS (AP & STA) HAVE PMK's (From PSK (WPA2/WPA3) or EAP (WPA2/WPA3 Enterprise))

# - PTK Components = PMK + Supplicant (STA) MAC Address + Authenticator (AP) MAC Address + Snonce (Supplicant) + Anonce (Authenticator)

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    AP Pick Random Anonce                       |  send M1 : ( 💊 🗝️ EAPOL Key | Anonce ) 

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    STA Generates PTK + Pick Random Snonce      |  send M2 : ( 💊 🔑 EAPOL Key | Snonce + MIC )

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    AP Generates PTK + Generates GTK            |  send M3 : ( 💊 🔑 EAPOL Key | Install PTK + MIC + Anonce + Encrypted GTK )

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    Decrypt GTK sent from AP + answer with MIC  |  send M4 : ( 💊 🗝️ EAPOL Key | MIC ) 

######################################################################################################################
                                🏁 STATE MACHINE = 4 :: client STA associated via RSNA 🏁
                              Open System Authentication/Association + WPA2 RSNA  Complete!!!
######################################################################################################################

````
---

### 🔓🪪 Open System Authentication: `Authentication` 
_The initial purpose of the authentication frame is to validate the device type (verify that the requesting station has proper 802.11 capability to join the cell). This exchanged is based on simple two-frame (Auth Request &  Auth Response) called Open System._
- [`Authentication` :: Frame Exchange :: `Open System`](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/bb52ef07-7502-435c-844d-9b32f7f7b43a) _`frame exchange`_
- [`Authentication` :: Frame Decode @ Nayanajith](https://mrncciew.com/2014/10/10/802-11-mgmt-authentication-frame/) _`frame decode`_

### 🔄📡 Frame Exchange: `Authentication` 

````py
######################################################################################################################
                                 🏁 STATE MACHINE = 1 :: client STA disconnected from AP 🏁
######################################################################################################################

🛸 BROADCAST   :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛸 Beacon ]}  (optional/passive scanning) 

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊❓ Probe Request ]}   (active scanning)   <<<=== START 🏁

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊❓ Probe Response ]}  

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]} 

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🚪 Authentication SeqNum=1 (request) ]} 

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🚪 Authentication SeqNum=2 (success) ]} 

🤳🏾 Client STA  :: --------->>>  ➡️ :: AP  📡    ||    {[ 💊🆗 ACK ]}                                 <<<=== FINISH 🏁

######################################################################################################################
                                🏁 STATE MACHINE = 2 :: client STA authenticated to AP 🏁
######################################################################################################################
.
.
.
(Next: Association Processs [State 3])
````

---

### 🔓🪪 Open System Authentication: `Association` :: From:`State 2` ➡️ To:`State 3` 
_When 802.11 authentication (not the RSN-WPA/WPA2 authentication) completes, a STA move to Association phase to the BSS. The purpose of this exchange is to join the cell & obtain an Association Identifier (AID). If the network is "Open" (no WPA/2-PSK, 802.1X or other kind of RSN authentication) then this is the last state and the client completes it's connection, else, the client is ready to start with the **RSNA** process to reach the state 4 Fully Connected & Authenticated._ <br>
- [`Association Req` & `Association Res` :: Frame Exchange :: `Open System`](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/64b10b5f-ba1a-4885-9141-c94e317f9ac9) _`frame exchange`_
- [`Association Req` & `Association Res` :: Frame Decode @ Nayanajith](https://mrncciew.com/2014/10/28/802-11-mgmt-association-reqresponse/) _`frame decode`_
    - [`Association Res` :: `Status Codes` :: Responses]() _`0=successful`_

### 🔄📡 Frame Exchange: `Association` 

````py
(Previous: Authentication Process [State 2)
.
.
.
######################################################################################################################
                             🏁 STATE MACHINE = 2 :: client STA authenticated to AP 🏁
######################################################################################################################

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🛜 Association Request ]}                 <<<=== START 🏁

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🆗 ACK ]}

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||    {[ 💊🛜 Association Response ]}

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡    ||    {[ 💊🆗 ACK ]}                                 <<<=== FINISH 🏁

######################################################################################################################
                               🏁 STATE MACHINE = 3 :: client STA associated to AP
                                Open System Authentication/Association Complete!!!
######################################################################################################################
.
.
.
(Next: RSNA Process (Only with RSNA Secure Authentication) [State 4])
````

---

### 🔓🪪 Open System Authentication: `Deauthentication` & `Disassociation` :: From:`ANY` ➡️ To:`State 1`
_**Station or AP can send a Deauthentication Frame** when all communications are terminated (When disassociated, still a station can be authenticated to the cell). || Once a station associated to an AP, **either side can terminate the association at any time by sending a disassociation frame**. It has the same frame format as deauthentication frame. A station can send a disassociation frame because it leave the current cell to roam to another cell. An AP could send disassociation frame because station try to use invalid parameters._ <br>
- [`Deauthentication` :: Frame Exchange :: `Open System` :: Sent by any side AP<-->STA](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/1c1c8c86-769c-4954-8913-5eea07468401) _`frame exchange`_
- [`Disassociation` :: Frame Exchange :: `Open System` :: Sent by any side AP<-->STA](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/1c1c8c86-769c-4954-8913-5eea07468401) _`frame exchange`_
- [`Deauthentication` & `Disassociation` :: Frame Decode @ Nayanajith](https://mrncciew.com/2014/10/11/802-11-mgmt-deauth-disassociation-frames/) _`frame decode`_
    - [`Deauthentication` :: `Status Codes` :: Responses]() 
    - [`Disassociation` :: `Status Codes` :: Responses]()
 
### 🔄📡 Frame Exchange: `Deauthentication`

````py
(Previous: STA Associated to AP [State 3 or 4])
.
.
.
######################################################################################################################
                         🏁 STATE MACHINE = 3 or 4 (RSNA) :: client STA associated to AP 🏁
######################################################################################################################

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||     {[ 💊🛜 Deauthentication :: Code X,Y,Z ]}             

                                                   - or -

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡     ||    {[ 💊🛜 Deauthentication :: Code X,Y,Z ]}             

######################################################################################################################
                        🏁 STATE MACHINE = 1 :: client STA disconncted from AP                                              
######################################################################################################################
.
.
.
retrun to STATE 1 - DISCONNECTED
````

### 🔄📡 Frame Exchange: `Disassociation`

````py
(Previous: STA Associated to AP [State 3 or 4])
.
.
.
######################################################################################################################
                         🏁 STATE MACHINE = 3 or 4 (RSNA) :: client STA associated to AP 🏁
######################################################################################################################

🤳🏾 Client STA  :: ⬅️  <<<--------- ::  AP 📡    ||     {[ 💊🛜 Disassociation :: Code X,Y,Z ]}             

                                                   - or -

🤳🏾 Client STA  :: --------->>>  ➡️ ::  AP 📡     ||    {[ 💊🛜 Disassociation :: Code X,Y,Z ]}             

######################################################################################################################
                        🏁 STATE MACHINE = 2 :: client STA authenticated to AP                                              
######################################################################################################################
.
.
.
retrun to STATE 2 - AUTHENTICATED (for roaming / re-connections)
````






![image](https://github.com/user-attachments/assets/a1e747ab-bfc4-43e8-ad0d-387519957a73)

![image](https://github.com/user-attachments/assets/34295be6-fa9b-48a6-9554-7c6ce9f12b4e)



## 🤳🏾🔁📡 IEEE 802.11 State Machine: `Resources`

- [IEEE 802.11 Wi-Fi Discovey, Connection, Roaming & Disconnection process](https://community.nxp.com/t5/Wireless-Connectivity-Knowledge/802-11-Wi-Fi-Connection-Disconnection-process/ta-p/1121148) _`info`_
- [802.11 State Machine :: `Diagram 1`](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/c8715d19-fe2f-42e6-914a-144d3fb4e70d) _`diagram`_
- [802.11 State Machine :: `Diagram 2`](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/5826a51b-eb23-4fba-bdeb-73ba23295819)
- [Understanding 802.11 State Machine @ Aruba Networks](https://blogs.arubanetworks.com/industries/understanding-802-11-state-machine/)
- [802.11 State Machine @ Noticias Inalámbricas](https://notasinalambricas.wordpress.com/tag/802-11-state-machine/) _`español`_
- [Los 4 pasos/estados de la máquina de estados, ¡En 2 minutos!](https://www.youtube.com/watch?v=u3dkoPrdOdE) _`video`_
- [802.11 Frame Exchanges](https://howiwifi.com/2020/07/16/802-11-frame-exchanges/)
- [802.11 Association Process Explained @ Meraki](https://documentation.meraki.com/MR/Wi-Fi_Basics_and_Best_Practices/802.11_Association_Process_Explained)
- https://dot11ap.wordpress.com/the-ieee-802-11-state-machine/
- https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html
- [802.11 WLAN States: Difference between WLAN class1 class2 and class3](https://www.rfwireless-world.com/Terminology/WLAN-class1-class2-class3-frames.html)<br><br>

- [Wireless association: active vs passive scanning, & roaming @ Sunny](https://youtu.be/HPJonmd8z1c?si=g47qTqJ5ma4iF3c0)
- [A study of the discovery process in 802.11 networks](https://www.researchgate.net/publication/215502402_A_study_of_the_discovery_process_in_80211_networks) _`pdf study`_
- https://community.nxp.com/t5/Wireless-Connectivity-Knowledge/802-11-Wi-Fi-Connection-Disconnection-process/ta-p/1121148





