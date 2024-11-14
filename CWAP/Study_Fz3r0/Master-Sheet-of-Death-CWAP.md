

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
