# Fz3r0 Wi-Fi Custom Model

## OSI is the map. Wi-Fi L1/L2 is the battlefield.

The **Fz3r0 Wi-Fi Custom Model** is a conceptual study model created to understand Wi-Fi from a more realistic **802.11 / CWNA / CWAP / protocol-analysis** perspective.

It does not replace the OSI model.

It does not replace the IEEE 802 model.

It does not pretend to create a new official standard.

Its purpose is to make visible what classic diagrams usually hide: the real relationship between **LLC/SNAP**, **802.11 MAC**, **PHY**, **PLCP**, **PMD**, **RF**, and the units **MSDU**, **MPDU**, **PSDU**, and **PPDU**.

The idea is simple:

> **OSI tells you where you are.**  
> **Fz3r0 shows you what is really happening in Wi-Fi.**

In a classic OSI diagram, Wi-Fi is normally reduced to two boxes:

| OSI Layer | Generic Name |
|---|---|
| **Layer 2** | Data Link |
| **Layer 1** | Physical |

That is correct, but it is not enough for real Wi-Fi study.

In Wi-Fi, most of the important analysis happens inside those two layers.

That is where we find:

| Wi-Fi Zone | Why it matters |
|---|---|
| **LLC/SNAP** | Identifies upper-layer protocols such as IPv4, IPv6, or ARP inside 802.11 data frames |
| **802.11 MAC** | Builds MPDUs, handles management/control/data frames, ACKs, retransmissions, QoS, FCS, and medium access |
| **PHY / PLCP / PMD** | Converts MAC output into a PPDU ready for physical transmission |
| **RF / Air** | Where RSSI, SNR, interference, airtime, MCS, retries, and physical medium behavior matter |

That is why the Fz3r0 model expands the lower part of OSI.

---

# 1. Main idea

The Fz3r0 Wi-Fi Custom Model starts from one practical observation:

**When studying Wi-Fi, the upper layers matter, but they are not the main battlefield.**

A user may be browsing a website, using HTTPS, sending SSH traffic, resolving DNS, playing a game, or using any other application. All of that is real.

But from the Wi-Fi point of view, most of that becomes **payload** carried inside an **802.11 data frame**.

Wi-Fi analysis usually asks questions like:

| Question | Most relevant area |
|---|---|
| Is the station associated? | **802.11 MAC** |
| Are beacons, probes, auth, or association frames present? | **802.11 Management** |
| Are ACKs present? | **802.11 Control / MAC** |
| Are there retries? | **802.11 MAC** |
| What MCS was used? | **PHY** |
| How bad is RSSI or SNR? | **RF / PHY** |
| Is this frame carrying IP, ARP, or is it management/control? | **MAC + LLC/SNAP** |
| Was the frame dropped because of FCS failure? | **MAC RX validation** |
| Is the payload protected/encrypted? | **MAC security processing** |
| What really goes over the air? | **PPDU / RF** |

The model keeps the full stack visible, but it pushes the student’s attention toward the layers where Wi-Fi behavior really lives:

```text
L2 Upper / LLC-SNAP
L2 Lower / 802.11 MAC
L1 / PHY / PLCP-PMD-RF
````

---

# 2. Quick comparison with OSI

The OSI model is a general-purpose conceptual map.

The Fz3r0 Wi-Fi Custom Model is a **Wi-Fi-focused zoom** into the lower part of that map.

| OSI 7-Layer Model   | Fz3r0 Wi-Fi Custom Model    | Focus                                                          |
| ------------------- | --------------------------- | -------------------------------------------------------------- |
| **L7 Application**  | L7 Application              | Application data and meaning. Visible, but not the Wi-Fi focus |
| **L6 Presentation** | L6 Presentation / Transform | Encoding, encryption, serialization, formatting                |
| **L5 Session**      | L5 Session / Context        | Session state, context, continuity                             |
| **L4 Transport**    | L4 Transport                | TCP/UDP, ports, segments, datagrams                            |
| **L3 Network**      | L3 Network                  | IP, ICMP, ARP context, routing                                 |
| **L2 Data Link**    | L2 Upper / LLC-SNAP         | Upper-protocol identification                                  |
| **L2 Data Link**    | L2 Lower / 802.11 MAC       | Wi-Fi frame behavior                                           |
| **L1 Physical**     | L1 / PHY / PLCP-PMD-RF      | PPDU, PLCP, PMD, RF transmission                               |

The big difference is here:

| Generic OSI view | Fz3r0 Wi-Fi view                                    |
| ---------------- | --------------------------------------------------- |
| **L2 Data Link** | **L2 Upper / LLC-SNAP** + **L2 Lower / 802.11 MAC** |
| **L1 Physical**  | **PHY / PLCP / PMD / RF**                           |

In other words:

```text
OSI:
L2 Data Link
L1 Physical

Fz3r0:
L2 Upper / LLC-SNAP
L2 Lower / 802.11 MAC
L1 / PHY / PLCP-PMD-RF
```

That zoom is what makes the model useful for Wi-Fi.

---

# 3. Why L7 to L3 are visually muted

In the Fz3r0 Wi-Fi Custom Model, layers **L7, L6, L5, L4, and L3** may appear visually muted.

This does not mean they are useless.

It means they are not the main battlefield of this model.

| Layer                           | What it does                                      | Why it is muted here                                               |
| ------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| **L7 Application**              | Creates application meaning                       | Wi-Fi does not interpret HTTP, SSH, DNS, or game logic             |
| **L6 Presentation / Transform** | Encodes, serializes, compresses, or encrypts data | Wi-Fi carries the resulting bytes as payload                       |
| **L5 Session / Context**        | Maintains session or conversation state           | Wi-Fi does not interpret session meaning                           |
| **L4 Transport**                | TCP/UDP, ports, segments, datagrams               | 802.11 MAC does not forward based on TCP/UDP ports                 |
| **L3 Network**                  | IP, ICMP, ARP, routing context                    | Important as payload/context, but Wi-Fi-specific behavior is below |

The model does not remove these layers. It keeps the map complete.

But visually, it pushes attention toward:

```text
LLC/SNAP
802.11 MAC
PHY / PLCP / PMD / RF
```

---

# 4. The core concept: SDU vs PDU

One of the main reasons this model exists is to make the difference between **SDU** and **PDU** clear.

These terms are easy to confuse.

A simple way to think about them is:

| Term    | Analogy   | Meaning                                                   |
| ------- | --------- | --------------------------------------------------------- |
| **SDU** | Cargo     | What a layer receives from above                          |
| **PDU** | Container | What a layer builds by adding its own control information |

A layer receives an **SDU**.

Then it adds its own control information, headers, trailers, or protocol structure.

The result is its **PDU**.

That PDU is passed downward.

From the next lower layer’s perspective, the same information may receive a different name.

The central idea is:

> **The name changes because the layer perspective changes.**

The bytes do not always change.

The viewpoint changes.

---

# 5. The core Wi-Fi chain

The foundational non-aggregated path in this model is:

```text
MSDU -> MPDU -> PSDU -> PPDU
```

This is the main chain of the Fz3r0 Wi-Fi Custom Model.

| Unit     | Full Name                     | Perspective      | What it represents                                   |
| -------- | ----------------------------- | ---------------- | ---------------------------------------------------- |
| **MSDU** | MAC Service Data Unit         | Input toward MAC | Service data delivered to the 802.11 MAC             |
| **MPDU** | MAC Protocol Data Unit        | MAC view         | The 802.11 MAC frame built by MAC                    |
| **PSDU** | PHY Service Data Unit         | PHY input view   | The MPDU octets as seen by PHY                       |
| **PPDU** | PLCP / PHY Protocol Data Unit | PHY / PLCP view  | The physical-layer unit prepared for RF transmission |

The most important sentence in the model is:

> **The exact same MPDU octets cross the PHY service interface and are renamed the PSDU from the physical layer’s perspective.**

That is the key.

MAC does not create one thing and PHY magically creates a different copy.

MAC builds the **MPDU**.

PHY receives those same octets as the **PSDU**.

Then PLCP builds the **PPDU**.

---

# 6. L2 Upper / LLC-SNAP

## 📦 Conceptual role

**L2 Upper** represents **LLC/SNAP**.

This part of the model bridges upper-layer protocols into the 802.11 data-frame path.

In many 802.11 data frames, LLC/SNAP identifies what upper-layer protocol is being transported, such as:

| Upper protocol | Example                                |
| -------------- | -------------------------------------- |
| **IPv4**       | IP traffic                             |
| **IPv6**       | IPv6 traffic                           |
| **ARP**        | Address resolution                     |
| **EAPOL**      | 802.1X / WPA handshake traffic context |

## What happens here

| Field                  | L2 Upper / LLC-SNAP                        |
| ---------------------- | ------------------------------------------ |
| **Receives**           | Layer 3 packet, such as IPv4, IPv6, or ARP |
| **Builds**             | LLC/SNAP framing or LLC PDU behavior       |
| **Identifies**         | The upper-layer protocol being carried     |
| **Passes downward as** | **MSDU** toward 802.11 MAC                 |

Visually, this layer should remain simple.

It does not need the heavy nested **PDU/SDU** visual treatment.

That is intentional.

The strongest learning moment is not LPDU/LSDU. The strongest learning moment is:

```text
MSDU -> MPDU -> PSDU -> PPDU
```

That is why L2 Upper uses a simple marker:

```text
PASSES DOWN AS MSDU
```

## Important note

LLC/SNAP is not “the MSDU” as a separate layer.

A more precise explanation is:

```text
LLC/SNAP identifies or frames upper-layer protocol data.
The result is delivered downward to the 802.11 MAC as MSDU.
```

In deeper IEEE 802 terminology, LLC can be discussed as building an **LPDU** containing service data. In this Wi-Fi-focused model, that detail stays secondary because the main focus is the MAC/PHY boundary.

---

# 7. L2 Lower / 802.11 MAC

## ⚔️ The Wi-Fi battlefield starts here

**L2 Lower** represents the **802.11 MAC** sublayer.

This is where the Wi-Fi frame is built.

For a normal 802.11 data frame, MAC receives an **MSDU** from above and builds an **MPDU**.

```text
MSDU
  ↓
MAC builds MPDU
```

## What an MPDU contains

| MPDU part             | Purpose                                                                 |
| --------------------- | ----------------------------------------------------------------------- |
| **MAC Header**        | Frame Control, addresses, duration, sequence control, QoS if applicable |
| **Frame Body**        | Where the MSDU or protected payload is carried                          |
| **FCS**               | Frame Check Sequence for integrity validation                           |
| **Security overhead** | May exist with WPA2/WPA3, such as CCMP/GCMP-related fields              |

Visual relationship:

```text
MPDU
└── contains MSDU
```

The **MPDU** is the MAC container.

The **MSDU** is the service data MAC received from above.

## TX behavior in MAC

During transmission:

| Step | What happens                                 |
| ---- | -------------------------------------------- |
| 1    | MAC receives an **MSDU**                     |
| 2    | MAC adds MAC-layer structure                 |
| 3    | MAC builds an **MPDU**                       |
| 4    | The MPDU is handed downward toward PHY       |
| 5    | PHY views those same MPDU octets as **PSDU** |

Compact visual wording:

```text
RECEIVES AS MSDU
BUILDS MPDU
HANDS OFF AS PSDU
```

The small technical note should be:

```text
MPDU = PSDU
same octets, different layer view
```

More precise wording:

```text
MPDU octets = PSDU octets
basic non-aggregated path
```

---

# 8. L1 / PHY / PLCP-PMD-RF

## 📡 Where the frame becomes a physical transmission

**L1** represents **PHY / PLCP / PMD / RF**.

It is not just “the air”.

Wi-Fi Layer 1 has its own structure and behavior.

| Component | Role                                                                                      |
| --------- | ----------------------------------------------------------------------------------------- |
| **PHY**   | General physical layer                                                                    |
| **PLCP**  | Physical Layer Convergence Procedure, the bridge between MAC service and PMD transmission |
| **PMD**   | Physical Medium Dependent sublayer, tied to actual medium transmission                    |
| **RF**    | Radio-frequency energy transmitted through the wireless medium                            |

PHY receives a unit from MAC called the **PSDU**.

In the basic non-aggregated path, that PSDU is the same MPDU octets, now seen from the physical layer’s perspective.

Then PLCP builds the **PPDU**.

```text
PSDU
  ↓
PLCP builds PPDU
  ↓
PMD transmits over RF
```

Visual relationship:

```text
PPDU
└── contains PSDU
```

## What a PPDU contains

| PPDU part                    | Purpose                                               |
| ---------------------------- | ----------------------------------------------------- |
| **PLCP preamble**            | Synchronization and detection                         |
| **PLCP header / signaling**  | PHY information needed to interpret the transmission  |
| **PSDU**                     | Service data received from MAC                        |
| **RF transmission behavior** | The physical transmission through the wireless medium |

The exact PPDU structure depends on the PHY family.

| PHY family | Example   |
| ---------- | --------- |
| **DSSS**   | 802.11b   |
| **OFDM**   | 802.11a/g |
| **HT**     | 802.11n   |
| **VHT**    | 802.11ac  |
| **HE**     | 802.11ax  |
| **EHT**    | 802.11be  |

The Fz3r0 model does not try to draw every PPDU variant.

It teaches the foundational relationship:

```text
PHY receives PSDU
PLCP builds PPDU
PMD transmits RF
```

---

# 9. TX path: transmission

The model is easiest to understand first in **TX** direction.

TX means the information moves downward through the stack and is prepared for RF transmission.

```text
L3 packet
-> LLC/SNAP
-> MSDU
-> MPDU
-> PSDU
-> PPDU
-> RF
```

| Stage          | What happens                                |
| -------------- | ------------------------------------------- |
| **L3**         | A packet exists, such as IPv4, IPv6, or ARP |
| **L2 Upper**   | LLC/SNAP identifies the upper protocol      |
| **Handoff**    | The data is passed toward MAC as **MSDU**   |
| **L2 Lower**   | MAC builds the **MPDU**                     |
| **MAC to PHY** | MPDU octets are viewed by PHY as **PSDU**   |
| **L1 / PLCP**  | PLCP builds the **PPDU**                    |
| **PMD / RF**   | The PPDU is transmitted over RF             |

Compact version:

```text
TX ↓
LLC/SNAP passes down as MSDU
MAC builds MPDU
MPDU octets become PSDU
PLCP builds PPDU
PMD transmits RF
```

---

# 10. RX path: reception

The model can also be read in **RX** direction.

RX is the reverse operation: the receiver gets RF energy, processes the PPDU, extracts the PSDU, passes the octets to MAC, MAC interprets them as an MPDU, validates the frame, extracts the MSDU, and passes it upward.

```text
RF
-> PPDU
-> PSDU
-> MPDU
-> MSDU
-> LLC/SNAP
-> L3 packet
```

| Stage                 | What happens                                             |
| --------------------- | -------------------------------------------------------- |
| **RF**                | The radio receives energy from the wireless medium       |
| **PMD**               | PMD handles the medium-dependent receive behavior        |
| **PLCP**              | PLCP processes the preamble/header and extracts the PSDU |
| **MAC handoff**       | MAC interprets those octets as an MPDU                   |
| **L2 Lower**          | MAC validates FCS and processes the frame                |
| **Normal data frame** | MAC extracts MSDU                                        |
| **L2 Upper**          | LLC/SNAP identifies the upper protocol                   |
| **L3**                | The packet is delivered upward                           |

Compact version:

```text
RX ↑
PHY receives PPDU over RF
PLCP extracts PSDU
MAC receives as MPDU
MAC validates FCS
MAC extracts MSDU
LLC/SNAP passes up L3 PDU
```

---

# 11. TX vs RX summary

| Direction | Meaning                                    |
| --------- | ------------------------------------------ |
| **TX**    | Build, encapsulate, prepare, transmit      |
| **RX**    | Receive, validate, extract, deliver upward |

| Layer                      | TX                                                | RX                                             |
| -------------------------- | ------------------------------------------------- | ---------------------------------------------- |
| **L2 Upper / LLC-SNAP**    | Passes down as **MSDU**                           | Receives MSDU and passes up L3 PDU             |
| **L2 Lower / 802.11 MAC**  | Receives MSDU, builds **MPDU**, hands off as PSDU | Receives as MPDU, validates FCS, extracts MSDU |
| **L1 / PHY / PLCP-PMD-RF** | Receives PSDU, builds **PPDU**, transmits RF      | Receives PPDU over RF, extracts PSDU           |

This teaches that the stack does not only build frames for transmission.

It also receives, validates, processes, and delivers data upward.

---

# 12. The golden rule: MPDU and PSDU

One of the most important parts of the model is this:

```text
MPDU octets = PSDU octets
same bytes, different layer view
```

In TX:

```text
MAC builds MPDU
PHY receives those octets as PSDU
```

In RX:

```text
PHY extracts PSDU
MAC receives/interprets those octets as MPDU
```

The relationship is:

| Perspective  | Name |
| ------------ | ---- |
| **MAC view** | MPDU |
| **PHY view** | PSDU |

This is not a contradiction.

It is a perspective shift.

The same sequence of octets crosses the MAC/PHY service boundary, and its name changes depending on who is looking at it.

This is one of the most important CWAP-style concepts in the model.

---

# 13. RX MAC Verification Rule

## ⚠️ MAC is not a passive pipe

On the RX path, MAC does not simply receive bytes and pass them upward.

It must validate the received frame first.

When PHY delivers the received PSDU octets upward, MAC interprets those octets as an **MPDU**.

Before MAC can extract and deliver a clean **MSDU** upward, it must validate the frame.

| RX validation                          | Meaning                                                   |
| -------------------------------------- | --------------------------------------------------------- |
| **FCS validation**                     | Verifies that the frame was not corrupted                 |
| **Address / frame processing**         | Checks whether the frame applies to this receiver/context |
| **Security processing**                | If protected, WPA2/WPA3-related processing is applied     |
| **Cryptographic integrity validation** | Protected frames must pass integrity checks               |

If the FCS fails, the frame is dropped.

If cryptographic integrity fails, the frame is dropped.

If validation fails, there is no clean MSDU to deliver upward.

Important rule:

```text
Not every received MPDU becomes an MSDU.
```

For a normal valid data frame:

```text
RX MPDU
-> validate FCS
-> decrypt / verify integrity if protected
-> extract MSDU
-> pass upward
```

If validation fails:

```text
RX MPDU
-> FCS fail or integrity fail
-> drop
-> no LLC/SNAP
-> no L3 packet
```

This is one of the reasons the model must include RX, not only TX.

---

# 14. Management and Control frame exceptions

The base chain:

```text
MSDU -> MPDU -> PSDU -> PPDU
```

is excellent for normal data frames.

But Wi-Fi is not only data frames.

Some frames are generated directly by the MAC layer.

| Frame type           | Examples                                                                                             |
| -------------------- | ---------------------------------------------------------------------------------------------------- |
| **Management**       | Beacon, Probe Request, Probe Response, Authentication, Association, Deauthentication, Disassociation |
| **Control**          | ACK, RTS, CTS, Block ACK                                                                             |
| **Special behavior** | Null function frames                                                                                 |

These frames are still MPDUs.

But they may not contain an upper-layer MSDU.

A beacon is not an IP packet.

A Wi-Fi ACK is not a TCP ACK.

RTS/CTS does not carry HTTP, TCP, UDP, or IP.

They are native 802.11 MAC mechanisms.

So the model must teach:

```text
Data frames often carry MSDU.
Management and Control frames may start directly at MAC.
```

---

# 15. WPA2/WPA3 overhead

In protected networks, the MSDU does not always remain a clean, simple payload all the way through.

The MAC layer may add security overhead.

| Mechanism                    | What may be added                     |
| ---------------------------- | ------------------------------------- |
| **CCMP**                     | Header, packet number, integrity data |
| **GCMP**                     | Header, integrity data                |
| **Protected frame behavior** | Encrypted and authenticated payload   |

The point is not to memorize every byte here.

The point is:

```text
Original MSDU size != final protected MPDU payload size
```

Security may add information around the protected payload.

On RX, MAC must also decrypt and validate integrity before delivering a clean MSDU upward.

---

# 16. Fragmentation and Aggregation

The Fz3r0 Wi-Fi Custom Model shows the basic non-aggregated path:

```text
MSDU -> MPDU -> PSDU -> PPDU
```

But modern Wi-Fi can make this relationship more complex.

| Topic                    | What changes                                                |
| ------------------------ | ----------------------------------------------------------- |
| **Fragmentation**        | One MSDU may be split into multiple MPDUs                   |
| **A-MSDU**               | Multiple MSDUs may be aggregated inside one MPDU            |
| **A-MPDU**               | Multiple MPDUs may be aggregated into a larger transmission |
| **Block ACK**            | A block of MPDUs can be acknowledged together               |
| **Padding / delimiters** | Additional structures may appear in aggregation behavior    |

This model does not attempt to visualize all of that yet.

Aggregation and fragmentation are real, but they deserve their own focused module.

Possible future module:

```text
Doctor Fz3r0 Aggregation Lab
```

That module could explain:

* **A-MSDU**
* **A-MPDU**
* **MPDU delimiters**
* **Block ACK**
* **padding**
* **QoS / TID**
* **airtime efficiency**
* **Wi-Fi 5 / 6 / 7 efficiency behavior**

The base model stays clean so the student understands the main anatomy first.

---

# 17. Why LLC/SNAP does not use heavy nesting

A key design decision in the Fz3r0 model is that **L2 Upper / LLC-SNAP** does not use the same heavy nested visual treatment as MAC and PHY.

That is intentional.

| Layer                      | Visual treatment                      |
| -------------------------- | ------------------------------------- |
| **L2 Upper / LLC-SNAP**    | Simple badge: **passes down as MSDU** |
| **L2 Lower / 802.11 MAC**  | **MPDU containing MSDU**              |
| **L1 / PHY / PLCP-PMD-RF** | **PPDU containing PSDU**              |

Reason:

> If everything is visually emphasized, nothing is emphasized.

The key learning moment is the MAC/PHY relationship:

```text
MPDU from MAC
=
PSDU from PHY
```

So LLC/SNAP stays simple.

Its message is:

```text
I identify upper-layer protocol data
and pass it down as MSDU.
```

---

# 18. How to read the complete model

## TX reading

```text
Upper layers create meaning.
L3 provides packet behavior.
LLC/SNAP identifies the upper protocol.
MAC receives MSDU.
MAC builds MPDU.
PHY sees MPDU octets as PSDU.
PLCP builds PPDU.
PMD transmits RF.
```

## RX reading

```text
PMD receives RF.
PHY/PLCP processes PPDU.
PHY extracts PSDU.
MAC receives those octets as MPDU.
MAC validates FCS and security integrity.
MAC extracts MSDU for normal data frames.
LLC/SNAP identifies the upper protocol.
L3 receives the packet.
```

## Conceptual reading

```text
Service data becomes protocol data.
Protocol data becomes service data for the next layer.
The bytes continue.
The perspective changes.
```

---

# 19. Complete model table

| Fz3r0 Layer                     | Role                                | TX                                           | RX                                          | Key point                             |
| ------------------------------- | ----------------------------------- | -------------------------------------------- | ------------------------------------------- | ------------------------------------- |
| **L7 Application**              | Application meaning                 | Creates message or intent                    | Receives app-meaningful data                | Visible, but not the Wi-Fi focus      |
| **L6 Presentation / Transform** | Encoding, serialization, encryption | Transforms data                              | Interprets or reverses transformation       | May not exist as a visible header     |
| **L5 Session / Context**        | Session state                       | Maintains context                            | Maintains continuity                        | Wi-Fi does not interpret this session |
| **L4 Transport**                | TCP/UDP                             | Builds segment/datagram                      | Delivers to process/socket                  | Upper payload for Wi-Fi               |
| **L3 Network**                  | IP/ICMP/ARP context                 | Sends packet toward LLC/SNAP                 | Receives packet from LLC/SNAP               | Important for identification          |
| **L2 Upper / LLC-SNAP**         | Upper-protocol identification       | Passes down as **MSDU**                      | Receives MSDU, passes up L3 PDU             | Logical bridge toward MAC             |
| **L2 Lower / 802.11 MAC**       | Wi-Fi frame behavior                | Receives MSDU, builds **MPDU**               | Receives MPDU, validates FCS, extracts MSDU | MAC battlefield                       |
| **L1 / PHY / PLCP-PMD-RF**      | Physical transmission               | Receives PSDU, builds **PPDU**, transmits RF | Receives PPDU, extracts PSDU                | PHY/RF battlefield                    |

---

# 20. Short version

The **Fz3r0 Wi-Fi Custom Model** is an educational Wi-Fi model that expands OSI L1/L2 to show how **LLC/SNAP**, **802.11 MAC**, **PHY**, **PLCP**, **PMD**, **RF**, **SDU/PDU**, **MSDU**, **MPDU**, **PSDU**, and **PPDU** relate during 802.11 transmission and reception.

Shorter:

> **OSI tells you where you are.**
> **Fz3r0 shows you what is happening in Wi-Fi.**

---

# 21. Final summary

The OSI model is still useful.

But for Wi-Fi, OSI is too broad.

Saying **Data Link** and **Physical** is not enough to understand 802.11.

The Fz3r0 Wi-Fi Custom Model opens those two boxes.

It shows that:

* **LLC/SNAP** identifies upper-layer protocols.
* **MAC** receives MSDU and builds MPDU.
* **MPDU contains MSDU.**
* **The MPDU octets become PSDU from the PHY perspective.**
* **PLCP builds PPDU.**
* **PMD transmits RF.**
* **RX is not passive.**
* **MAC validates FCS and security integrity before delivering data upward.**
* **Management and Control frames can start directly at MAC.**
* **Aggregation and fragmentation exist, but belong to deeper modules.**

This model does not replace OSI.

It focuses it.

It brings OSI closer to the real behavior of 802.11.

It turns the lower layers into something visible, clickable, explainable, and useful for real Wi-Fi study.

> **OSI is the map.**
> **Wi-Fi L1/L2 is the battlefield.**


