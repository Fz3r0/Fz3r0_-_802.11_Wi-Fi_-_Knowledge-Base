








# Medium Access Methods & QoS

### ⌛💹🔢 Duration Values

The Duration Field determine the **time in microseconds (μs)** needed to complete the Frame Exchange. This is measured **AFTER the current frame**, this means: what is left after the current frame.

**There are 3 different main Duration Values types:**

1. **Data Exchange** _(AKA RTS Data Exchange)_ = `SIFS` + `Ack`
2. **RTS/CTS Data Exchange** = `x3 SIFS` + `CTS` + `Data` + `ACK`
3. **CTS-to-Self Data Exchange** = `x2 SIFS` + `Data` + `ACK`
   
# 👨🏻‍⚖️🚦 Arbitration & DCF: `Network Arbitration`
_In every 802.11 network there must be a set of rules to determine when stations can transmit. Arbitration is just deciding "who" is gonna talk "when", in WLAN Networks there are rules to determine when STA can transmit into the medium (RF) | There are 2 types of methods: Contention Methods & Contention Free Methods (Token Ring Legacy = Contention Free | CSM-CA & DCF (default Wi-Fi), CSMA-CD (eth) modern = Contention Method)_

### Contention Methods

- CSMA/CD: Ethernet 802.3 :: Carrier Sense Multiple Access/Collition Detection. <br><br>
- CSMA/CA: Wi-Fi 802.11 :: Carrier Sense Multiple Access/Collition Avoidance _(This method uses by default DCF (Distributed Coordination Function)._

### Contention Free Methods

- Token Passing: Obsolete / Not used :: for Token Ring puproses
- PCF (Point Coordination Function): Obsolete / Not used :: Alternative 802.11 Wireless method NOT implemented

### 👨🏻‍⚖️🚦 Arbitration Methods

- DCF – Distributed Coordination Function : Non-QoS WLAN
- HCF with EDCA – Hybrid Coordination Function : QoS WLAN
- EDCA – Enhanced Distributed Channel Access
- PCF – Point Coordination Function (not implemented practically)

### Arbitration & Contention Methods Summary

- `DCF`: is the fundamental, required contention-based access service for all networks :: **(Non-QoS)** <br><br>
- `PCF`: is an optional contention-free service, used for non-QoS STAs :: This coordination function is an optional method that is not used in real-world 802.11 APs. **Not implemented in 802.11** <br><br>
- `HCF Contention Access (EDCA)`: Based on DCF, is required for prioritized contention-based QoS services :: **(QoS)** <br><br>
- `HCF Controlled Access (HCCA)`: is required for parameterized contention-free QoS services :: 802.11e QoS channel access method that requires the QoS AP to take control of the wireless channel and manage service periods for associated stations **(QoS) - Not implemented in 802.11**

### CFB

`CFB (Contention-Free Burst)`: CFB refers to a burst of frames sent during a contention-free period, often associated with legacy 802.11 protocols.
