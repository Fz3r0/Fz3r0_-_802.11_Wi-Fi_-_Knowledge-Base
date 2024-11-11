


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
