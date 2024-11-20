

# Architecture

## DS Devices

- WLAN controller	
- Mesh Access point
- Autonomous access point
- Switch


## STA Devices

- Smartphone
- Laptop client radio
- VoWiFi Phone










# Physical Layer

### Guard Interval

| **Wi-Fi Standard** | **Guard Intervals (GIs)**                          | **Explanation**                                                                                   |
|--------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **802.11n**        | 400 ns (short), 800 ns (long)                      | The 800 ns GI was chosen to accommodate the maximum multipath echo time in indoor environments.    |
| **802.11ac**       | 400 ns (short), 800 ns (long)                      | Same as 802.11n, offering 400 ns for short and 800 ns for long to optimize performance.            |
| **802.11ax**       | 800 ns (normal), 1600 ns (double), 3200 ns (quadruple) | Supports multiple GIs to handle higher frequencies and minimize interference in more complex environments. |


## Channels & Spectrum

### 2.4 GHz

![image](https://github.com/user-attachments/assets/96b5c4d4-3661-4e7d-a803-2c16e23d9642)

### 5 GHz

![image](https://github.com/user-attachments/assets/d7ee7e60-fe4c-4042-b521-3ce9b943e67e)

## OFDM Subcarriers

### Subcarrier Arrangement in 802.11n/ac 20MHz Channel

![image](https://github.com/user-attachments/assets/73b89035-dc47-4206-8f89-313a5c9a9ad8)

### Subcarrier Arrangement in 802.11n/ac 40MHz Channel

![image](https://github.com/user-attachments/assets/97692cb5-115d-450d-833d-bb61d54773a2)

### Subcarrier Arrangement in 802.11ac 80MHz Channel

![image](https://github.com/user-attachments/assets/14f9ab23-565b-4e79-9264-411880a5f4a7)

### Subcarrier Arrangement in 802.11ac 160MHz Channel 

![image](https://github.com/user-attachments/assets/c8c96917-3045-4e36-95fd-2ae39a9b1e3e)


### 802.11ax OFDMA Subcarriers

https://www.cleartosend.net/802-11ax-ofdma-subcarriers/

- Full:

![image](https://github.com/user-attachments/assets/692a3207-ff6e-45a3-9ef0-c278cd762321)

- Zoom:
  
![image](https://github.com/user-attachments/assets/1af41848-1f31-49ef-9615-3787227669dd)









## Addresses

- https://excalidraw.com/#room=5e34d48995724e4effe4,bOzzxMz520Zl-6fU124PjA

![image](https://github.com/user-attachments/assets/668f8296-5831-4e62-9ed7-3a94747b2c9f)














## QoS & EDCA

### AIFS & CW

![image](https://github.com/user-attachments/assets/789900e1-0a3b-4781-ad52-bf420a2550af)

- When an 802.11n station begins the arbitration process after a failed frame transmission = `AIFS`

# Security

## MTU Sizes

| **Process**                                          | **Size (bytes)**   | **Adds (bytes)**  |
|------------------------------------------------------|--------------------|-------------------|
| **Maximum MSDU size** (Before encryption or when a packet is passed from the Network layer to the Data-Link layer for transmission) | 2304               | 0                 |
| **WEP**                                              | 2312               | 8                 |
| **WPA-TKIP**                                          | 2324               | 20                |
| **WPA2-CCMP**                                         | 2320               | 16                |



















## Protection Mechanisms

### ERP

- 802.11/802.11b station `associated` to the AP = `NonERP Present`













## Interference

### Retransmission can caused by:

- RF interference	
- Low SNR
- Multipath
- Adjacent cell interference (ACI)
- Co-channel interference (CCI)

### Effects of retransmission:

- Excessive MAC sublayer overhead
- Latency
- Jitter

















# Protocol Analysisis

## 🛜🪤🎣 Frame Capture: `802.11 Frame Capture Devices & Methods`
_Devices and methods for capturing 802.11 WiFi frames can be categorized into three main types. At the end, it mostly depends on the resources and needs_

| **Capture Method**        | **Description**                                                                                                                                               | **Pros**                                                                                       | **Cons**                                                                                          | **Accessibility and Cost**                                                                       | **Examples**                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Mobile Capture**        | Uses mobile devices like laptops with Linux and USB Wi-Fi adapters that support "monitor mode" to capture traffic.                                                                          | Portable and flexible, relatively low cost, no specialized hardware needed                    | Limited range and capacity, requires extensive setup and configuration, potential driver issues  | Most accessible, can be cost-effective, range from simple setups (e.g., Raspberry Pi) to complex systems with high-end computers   | Linux with adapters like Alfa and tools like airmon, macOS internal adapter, devices like Wi-Pi, WiFi Pineapple, Wi-Spy |
| **Infrastructure Capture**| Utilizes professional wireless devices to capture traffic while providing network connectivity. Note that some vendors like Ruckus allow simultaneous capture and network traffic, while others like Cisco may not support this capability. | Scalable, efficient, centralized management, real-time streaming to tools like Wireshark      | High cost due to specialized hardware, complexity in setup and management                        | More expensive due to specialized devices, standalone APs like Ubiquiti or Ruckus Unleashed can be more affordable alternatives   | Ruckus APs and SmartZone, Cisco AirMarshal and APs, Meraki APs |
| **Distributed Capture**   | Employs specialized sensors (e.g., Multi-Sensor Wireless Overlay Systems, WIPS) placed at various points to capture traffic on multiple channels simultaneously.     | Detailed network activity analysis, captures traffic from different locations                 | Very high cost, complex setup and management, requires specialized knowledge and equipment       | Most expensive and complex, requires specialized sensors and systems, less accessible for general use                              | Omnipeek, Cisco Adaptive wIPS, Arista WIPS, Fortinet WIPS |



## 🎛️⚙️ Frame Capture: `Capture Options`
_When capturing network traffic, setting appropriate capture options ensures you collect the most relevant data efficiently. Key capture options include:_

- 🎛️ **`Capture Title`**: Always name your captures with much details as possible like where, when, why (ex. 2024-06-06_13-25hrs_802-11_AP-Room-1_Authentication_iphone-f0-f0-f0-f0-f0-f0_-_01.pcap) <br> <br>
- 🎛️ **`Continious Capture`**: Recycle the capture buffer, which is a temporary buffer where the captured packets are stored. 
 (Buffer becomes a FIFO buffer) (ex. each 10mb of capture the buffer will reset). <br> <br>
- 🎛️ **`Save to Disk`**: Save all packets to disk, specify the name, size and save/stop criteria (ex. Set Title + 512mb file size + Stop After 2048mb captured + Keep Most Recent 3 files + New File every 1 hour) <br> <br>
- 🎛️ **`Packet Slicing`**: Limits the portion of the packet to be captured, used to save disk space or ensure confidentiality. (Warning: Avoid cutting off header information, checksums may become invalid)(ex. Limit each packet to 4500 bytes, this will allow to capture whole beacon frames, but cut large data frames payload that is non critical for analysis) <br> <br>
- 🎛️ **`Capture Buffer`**: The amount of memory allocated to hold packets (ex. Buffer Size = 10mb) <br> <br>
- 🎛️ **`Capture Filter`**: Used to define which packets the sniffer should capture. By setting capture filters, you can limit the captured traffic to only the frames of interest, reducing the amount of data collected and focusing on relevant information. This is not recomended because sometimes you may lose some information. <br> <br>
- 🎛️ **`Dwell Time Capturing`**: The dwell time is the amount of time a wireless network adapter will stay on a specific RF channel before moving the next channel that the device is capable of or is set to scan within the software. A shorter dwell time will capture less information on a specific channel but will allow the device to scan all channels at a quicker rate. <br> <br>
- 🎛️ **`Event Trigger Capturing`**: Event triggers can be set to start and end packet captures based on a specific event. This will allow a protocol analyzer to capture frames that may be helpful in troubleshooting intermittent problems when a specific event happens. Event triggers can be very granular to allow for complex captures to be used with troubleshooting WLAN problems.

## 📻⚙️ Frame Capture: `Channel Capture & Configuration`
_When capturing network traffic, proper channel capture and configuration are essential to collect the relevant data. Capturing on the wrong channel means missing the traffic you need to analyze. Since there are many channels, it's crucial to know which specific channel or channels to target for your troubleshooting needs._

- 📻 **`Fixed Channel`**: Capture in one single channel :: For troubleshooting a particular device that is using a particular channel. Some adapters can be configured even with channel bandwith, primary or secondary channel, etc. (ex. capturing only channel 11 of 2.4 GHz because AP and STA are using that channel) <br> <br>
- 📻 **`Channel Scan`**: Capture the whole picture of the BSA channels and bands :: Select every single channel to do a channel hopping method, some adapters can go from 2.4 GHz to 5 GHz hopping. The tradeoff of this capture technique is that you will miss what is happening in others channels while you are hopping from one channel to another. <br> <br>
- 📻 **`Channel Aggregation (Multiple adapters + Multiple fixed channels)`**: If you have more than 1 adapter you can capture on different channels at same time and you won't miss anything. (ex. with 3 adapters you can capture channel 1, 6 & 11 of 2.4 GHz at same time)

## 🤳🏾🪤📡 802.11 Frame Capture: `Location for Capture`
_In 802.11 Frames Capture is very important the physical location of the adapter that will capture 802.11 Frames depending on what are we tring to capture, it's important to remember that we are capturing on wireless medium (RF flying through the air)_

- 🪤 **`Near the AP`**: Capture that AP sees :: This location is ideal for capturing all the traffic within the Basic Service Area (BSA) and the communications between the Access Point (AP) and its connected clients. It helps in analyzing the overall network performance and the interaction between the AP and multiple clients. Generally, to troubleshoot a channel-wide problem, you will start with a capture near the AP. <br> <br>
- 🪤 **`Near the Client`**: Capture that Client sees :: This setup is useful for diagnosing issues specific to a particular client. By capturing frames from the client's perspective, you can identify problems related to that client’s connection, such as connectivity issues, interference, or performance bottlenecks. <br> <br>
- 🪤 **`In the middle of Client & AP`**: For getting the whole picture of whats happening inside the BSA :: Capture a comprehensive view of the communication. Positioning the adapter between the client and the AP provides a balanced perspective of the entire interaction. This location allows for capturing both the client and AP transmissions, offering a full picture of the communication flow within the BSA.

## 📡🪤🖧 802.11 Frame Catpure: `802.3 Wired Ethernet` + `802.11 Wireless Wi-Fi` at same time
_Capturing and troubleshooting both wired (802.3 Ethernet) and wireless (802.11 Wi-Fi) traffic simultaneously is sometimes necessary. This dual approach provides a complete view of network interactions, especially for complex troubleshooting scenarios._

- 🖧📡 **`EAP over LAN exchanges & RADIUS`**: Simultaneous capture of Wi-Fi and Ethernet is crucial for analyzing authentication exchanges. By capturing both the wireless and wired sides of the network, you can ensure that authentication processes, such as those using EAP and RADIUS, are functioning correctly and efficiently. <br> <br>
- 🖧📡 **`DHCP exchanges`**: Capturing DHCP traffic on both Wi-Fi and Ethernet helps in diagnosing issues related to IP address assignment. It ensures that DHCP requests and responses are correctly handled across both mediums, providing a comprehensive view of the DHCP process. <br> <br>
- 🖧📡 **`QoS`**: Analyzing QoS tags and markings across the entire network, including both wireless and wired segments, is essential for applications like VoIP. This ensures that QoS configurations are consistent throughout the network, maintaining optimal performance and prioritization of critical traffic. It's important when troubleshooting QoS in wireless networks be sure that the QoS is working correctly in wired medium and the whole Distribution System. <br> <br>
- 🖧📡 **`VLAN Tagging`**: Capturing VLAN tags on both Wi-Fi and Ethernet is necessary for verifying correct VLAN VS SSIDs configurations. This helps in ensuring that VLANs are properly propagated and handled across the entire network, facilitating accurate traffic segregation and management. For example when you configure a VLAN for specific SSID. 

## 📦👀📄 Frame Analysis: `Packet Views`
_Understanding network traffic through packet views is crucial for effective analysis. Here are the key packet views used in protocol analyzers._

### 📄👀 General Views:

- Packet List View: This is the main view of a protocol analyzer and shows the columns/list of all the packets captured. (ex. Wireshark has this in the top of a default configuration.) <br> <br>
- Packet Decode View: Very important view in protocol analyzers for packet analysis. It shows a "human read" format organized from lower layers to upper layers bits/bytes information in a "directory style". This contains all the packet information, elements, payloads, radiotap header, PPI, flags, fields names & values (ex. control field), etc. (ex .Wireshark has this in the bottom left of a default configuration.) <br> <br> 
- HEX / Binary / ASCII encoding views: This is the HEX or binary version of the decode view. It shows a "machine read" format of the packet. Wireshark has this in the bottom right of a default configuration.  <br> <br>
- Wireless Views: This is only available in Wireless packet analysis tools and make easier to see information about channel utilization, retries, authenticatins, top channels, top APs, top STAs, etc. 

### 🔎👀 Display, Filter & Profiles Views:

- Display Filter: Used to refine the view of captured data in the Protocol Analyzer. They help isolate specific packets within a capture file based on various criteria, making it easier to focus on the relevant traffic during analysis. This is more recommended than using a capture filter, because you can capture all the data without losing data and then isolate only the packets you want to see. <br> <br>
- Color Filter: highlight specific types of packets in the Wireshark interface. By applying color filters, you can quickly identify different kinds of traffic, making it easier to spot patterns and anomalies during analysis. <br> <br>
- Custom Colors: Custom colors allow you to set specific colors for different types of packets. This customization enhances visual analysis and helps in quickly distinguishing between various traffic types. <br> <br>
- Custom Columns: Enable you to add specific fields to the packet list pane. This feature allows you to display the most relevant information directly in the main view, making it easier to analyze the captured data. <br> <br>
- Custom Profiles: Let you save different configurations of Wireshark settings, including filters, color schemes, and columns. This is useful for switching between different analysis setups quickly and efficiently. For example, you can use a profile to troubleshoot DHCP in ethernet captures and other profile to troubleshooit association in 802.11 Wi-Fi. 

### 📊👀 Advanced Features & Graphic Views:

- 📊 Statistics & Graphics: Some Protocol Analyzers provides various statistical tools and graphical representations to summarize and visualize the captured data. These tools can help identify trends, anomalies, and potential issues in the network traffic. For example, in 802.11 Wi-Fi you can analyze the airtime utilization filter and identify high utilization over the time, the top talking APs, the top talking STAs, etc. <br> <br>
- 📊 Expert Analysis: The automatic detection of network events, errors, and problems by an analyzer. For example: Heuristic-based expert analysis looks for patterns in the traffic flow and compares them to a set of rules configured by default in the analysis software (in wireshark you can see sometimes a colored indicator with "expert" quote, showing some relevant information). <br> <br>
- 📊 Endpoints / Protocol List: This window shows statistics about the endpoints captured. For each supported protocol, a tab is shown in this window. Each tab label shows the number of endpoints captured (e.g., the tab label “Ethernet · 4” tells you that four ethernet endpoints have been captured). If no endpoints of a specific protocol were captured, the tab label will be greyed out (although the related page can still be selected). <br> <br>
- 📊 Node Lists / Conversations: The conversations window is similar to the endpoint Window. Along with addresses, packet counters, and byte counters the conversation window adds four columns: the start time of the conversation (“Rel Start”) or (“Abs Start”), the duration of the conversation in seconds, and the average bits (not bytes) per second in each direction. A timeline graph is also drawn across the “Rel Start” / “Abs Start” and “Duration” columns. <br> <br>
- 📊 Peer Map: A peer map is used to show frame exchanges between stations (STA’s) that are communicating within a WLAN BSS. This can be a valuable visual representation that may be very useful in troubleshooting WLAN problems.

## 📦⏳🎣 Frame Analysis: `Time Metric Columns`
_Various time metric columns provide insights into different aspects of packet timing._

- ⏳ **`Absolute time`** / **`Arrival Time`**: Display the time the packet was captured based on the system clock in the computer, this is the actual capture date and time based on the time zone of the capture device, this means, the time when the packet was captured, provides the real-world time of packet capture for example date and hour. This metric is useful for correlating captured data with real-world events and time-based troubleshooting. <br> <br>
- ⏳ **`Delta time`**: Measures the time difference between two consecutive packets in a capture file. In other words, it is the elapsed time from the previous packet to the current packet. This metric helps in understanding the time intervals between packet transmissions, which can be useful for performance analysis. <br> <br>
- ⏳ **`Relative time`**: This is the time from the first packet in a capture file, but it can be also similar to the Seconds Since Beginning of Capture option. Cumulative time from a selected packet to another selected packet, it can be used to identify how long it takes for a frame exchange to occur. Some protocol analyzer software programs make this a very simple task. This information is valuable in determining problems such as latency or contention with specific frame exchanges. (ex. in a 4-way-handshake you can select the first frame, and then look how many time does the 4th frame took)