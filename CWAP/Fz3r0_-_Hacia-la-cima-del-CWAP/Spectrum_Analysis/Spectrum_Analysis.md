
# 📡📻📊 `Spectrum Analysis`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Networking` `Wireless Networking` `IEEE 802.11` `Wi-Fi` `CWNA` `CWAP` `CWNE` `CCNP` `Spectrum` `Spectrum Analysis` `Layer 1` 

---

<br>

# Index




# 📡📻📊 `Spectrum Analysis`

Sometimes there's something in the enviorment that is not 802.11 MAC Layer signal, and there's no way to capture this kind of interference with a protocol analyzer or Wi-Fi analyzer. 

Spectrum Analyzers are tools that help to find something based on the existance of RF Energy. This tools have different features and capabilities to help to find RF signatures, The RF signature can be consider as a fingerprint of a electromagnetic radiation signal.

## Spectrum Analyzers

Spectrum analyzers are frequency measuring devices. They measure electromagnetic radiation, analyze the frequency spectrum and help with EMC tests or frequency monitoring and analysis, for example.


## `Oscilloscope - Time Domain` VS `Spectrum Analyzer - Frequency Domain`
_Spectrum analyzers are **frequency domain tools** used to measure amplitude in a finite frequency space. Wireless Engineers use spectrum analyzers to locate sources of interference that may have a negative impact on the 802.11 network as well as other protocols that operate in the same frequency, 2.4 or 5GHz._

### Difference between a spectrum analyzer and an oscilloscope:

- `Oscilloscope`: Used to measure the **TIMING** information around a signal. 
- `Spectrum Analyzer`: is used to measure **FREQUENCY** information on a signal

### Difference between Time Domain & Frequency Domain

- `Time Domain`: Seen by a **Osciloscope** :: The RF in a time domain is where you can see the sine waves (or any other form) being generated.
- `Frequency Domain`: Seen by a **Spectrum Analyzer** :: Is like see the wave "coming at us". This means, signal strenghts on a frequency, and this is achieved using the FFT (Fast Fourier Transform)

# Spectrum Analyzer: `Types`

Spectrum Analyzers can be classified in 3 basic categories in reference to their architecture: 

| **Type**                    | **Example**                                        | **Info**                                                                                                                                         | **Key Differentiator**                                                                                  |
|-----------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Real-time Spectrum Analyzers (RSA or RSTA)**  | Aaronia: SPECTRAN V6 series                        | Real-time analyzers capture the spectrum continuously, providing immediate feedback on signal events and interference, ideal for detecting transient signal issues. These analyzers can display live, real-time spectral data. | **Real-time analysis**: Displays continuous, live spectrum data, ideal for detecting quick, transient events. |
| **Swept Spectrum Analyzers (SA)** | Wifisurveyor @ RF Explorer Digital Handheld Spectrum Analyzer 6G Combo Plus - Slim (waterfall view) | Swept spectrum analyzers measure the spectrum by sweeping through frequencies over time. They provide a frequency vs time (waterfall) view, which helps visualize signal behavior over a given period. | **Frequency sweeping**: Provides a time-frequency waterfall view, ideal for monitoring signal variations over time. |
| **Vector Signal Analyzers (VSA)** | PXI Vector Signal Analyzer                          | Error Vector Magnitude (EVM) is a measure used in wireless communications to quantify the performance of a transmitted signal compared to its ideal or reference signal. It essentially evaluates how much the actual signal deviates from the expected signal, which helps to assess the quality of the transmission. Especially relevant in systems that use advanced modulation schemes (like 802.11ac/ax, LTE, and 5G), where small errors can significantly impact performance.  | **Signal integrity**: Measures both amplitude and phase, offering in-depth analysis of modulation accuracy and signal quality (EVM). |


# Spectrum Analyzer: `Spectrum Views`

It is very important to understand what information can be understood from the different views:

- RF signal can represent in either `time domain` or `frequency domain`.
- Once you do `Fast Fourier Transformation (FFT)` for a time domain signal you can get the Frequency domain signal.
- In RF, mostly `Frequency Domain` representation is more useful.

Here are some different views available in a spectrum analyzer:

<p align="center"> <img src="https://github.com/user-attachments/assets/36e79a62-f080-43ae-b32c-e47618e843b9" height="580"> </p>

<p align="center"> <img src="https://github.com/user-attachments/assets/e536e616-b057-45f8-870b-81ad2803da09" height="550"> </p>

![image](https://github.com/user-attachments/assets/c0ba9372-750f-493f-a253-f93f5373320e)

![image](https://github.com/user-attachments/assets/bccb2df6-3646-40c2-9a00-a47dfdfe8f0e)

![image](https://github.com/user-attachments/assets/b821d960-f640-4a0a-b739-c2a7307f06df)



## 📈📏 Spectrum Views: `Real time FFT (Fast Fourier Transform)`

- `Frequency` represented in **horizontal** axis
- `Energy` represented in **`dBm defined`** in **vertical** axis

<p align="center"> <img src="https://github.com/user-attachments/assets/a66c4bfa-b413-4c6a-954c-58ca4ded148f" height="450"> </p>

<p align="center"> <img src="https://github.com/user-attachments/assets/115dafa3-ff0d-4811-9209-fcccb386aff5" height="170"> </p>

![image](https://github.com/user-attachments/assets/46b32017-540b-450d-9f4d-83ea1055344c)


- `Type:` **Real-time Spectrum Analyzer (RSA).** <br><br>
- The key words of FFT are **`real-time`**; **the information shown is live.**. That's why the FFT graphics are common named as **Real Time FFT**. 
- FFT is an algorithm that samples a signal over a period of time or space divides it into its frequency components. This means, the FFT decomposes a signal into its component frequencies and their amplitudes.
- The spectrum analyzer captures the RF energy within the time domain and converts the information to the frequency domain using the FFT process which is then viewable without gaps. 
- FFT can be explained as: "Measurments of points in the time of the spectrum". Each "point" es marked at the midde of each "FFT bin"

### Concepts used in FFT:

- **`FFT Bin`**:  <br><br>
    - The resolution bandwidth (RBW) is dictated by the size of the FFT Bin
    - Folowwing statistics are gathered for each bin: Average Power, Max Power, Duty Cicle  <br><br>
- **`Sampling Rate`**: <br><br>
    - How often the spectrum analyzer takes measurments  <br><br>
- **`Dwell time`**: <br><br>
    - The amount of time spent measuring each sample    



## 📈💯 Spectrum Views: `Duty Cycle` / `Channel Utilization`

❗ Show the **`percent (%)`** of channel utilization

![image](https://github.com/user-attachments/assets/8e8d1535-85b6-4b6a-b909-65eb69df8b0e)

![image](https://github.com/user-attachments/assets/8f541f6e-5116-4da8-a687-83f00da60c77)

![image](https://github.com/user-attachments/assets/d2b9d2c7-36e5-4dbf-8c70-0a9be00ffd81)

![image](https://github.com/user-attachments/assets/a7ef848d-6a68-47e9-b2ba-bac539a60b23)


- In this veiw you can see whether a device is constantly using a frequency (100% duty cycle on a particular channel mean it is not usable & caused by sort of jammers)
- Displays a measurement of the amount of time a received signal amplitude is above the noise floor or another arbitrary threshold
- Although the term duty cycle can be subjective based on the context in which it is used within WLAN technology, it is commonly identifies the percentage of time an RF signal is above a specific threshold. A high duty cycle such as 95-100% can indicate a problem such as an RF jammer or other devise that is causing high utilization of the RF channel.
- Channel utilization shows the percentage of time that the frequency is in use over a period of time. The software in use determines the threshold, some may use the noise floor where others may use a higher value.
- For example, Aruba documentation states “The spectrum analysis feature considers a frequency bin to be utilized if the detected power in that bin is at least 20 dB higher than the nominal noise floor on that channel.” This is a general measure of how busy the network is.
- Channel utilization measures both Wi-Fi and non-Wi-Fi devices.
- Duty cycle percentage is used to identify the amount of time a single device is active. Ekahau shows utilization percentages per channel in real time. Spectrum XT shows “Duty Cycle” percentage but doesn’t reference any single device (this is channel utilization labeled as duty cycle.)

---

### 📈⏳ Spectrum Views: `Swept Spectrogram` & `Waterfall View`

❗ In this view vertical/horizontal axis shows the **`historical data (similar to a waterfall rectangle from Up-to-Down or Left-to-Right)`**

- Swept / Waterfall: This is the same information as the real-time FFT but often in a different view and tracked over a longer period. These views can often be configured within software to specify the length of time
- Waterfall: The information from the swept spectrogram showing time, frequency, and power but viewed vertically.



![image](https://github.com/user-attachments/assets/21a3c49a-33f2-47db-9dad-bf99953247d1)

![image](https://github.com/user-attachments/assets/98fe65eb-4904-43ce-b82a-c9207899d709)

![image](https://github.com/user-attachments/assets/b9985589-e1a3-42f4-b534-ff94315d311c)

![image](https://github.com/user-attachments/assets/890563d0-ce20-4f64-a315-65834993846b)

![image](https://github.com/user-attachments/assets/756e48bf-a7af-47d2-9af5-7212337e93fe)

![image](https://github.com/user-attachments/assets/e7242689-bf1f-42e6-8b7d-08274a2b598f)




- This view is considered a **Swept Spectrum Analyzer (SA).**
- This is the **same information as the real-time FFT** but often in a different view and tracked over a longer period.
- These views can often be configured within software to specify the length of time.
- The **Waterfall View** is the information from the **swept spectrogram** showing: time, frequency, and power but viewed vertically.

---

### 📈🌈 Spectrum Views: `Power Spectral Density` / `Density View`

❗ Horizontal axis represent frequency & vertical axis represent energy in dBm with **`brightness of color`** being determined by how many times that specific bit of information has been captured.

![image](https://github.com/user-attachments/assets/d883bebd-43f0-46a6-acfc-c82245b3d719)

![image](https://github.com/user-attachments/assets/2e19ae70-850f-4679-8836-2534293e4931)

![image](https://github.com/user-attachments/assets/92fc8055-15eb-4e42-97f9-4b8ba2dd992c)

![image](https://github.com/user-attachments/assets/39e18fcc-e0c0-440c-8c1f-20f56ad56f05)

![image](https://github.com/user-attachments/assets/5d067904-94b8-4f2b-90eb-97ab1c15bf03)



- **Power Spectral Density** can be also referred to as **spectrum density**
- Useful for find repetition of **data points** over time to help locate the interferer.
- The density view in a spectrum analyzer will show the data points that a specific frequency is hit within a channel or band. Choosing a color scheme will help to show these events. This can be used to help identify an RF transmitter and interferer.
- It shows where detected RF energy variations are stronger and where variations are weaker.
- This is the primary view in Ekahau; you can add the real-time FFT average or max sweep to show overtop of the density view as well.
- Spectrum density views use colors to indicate the channel utilization. (eg. Ekahau uses green to represent low utilization and red/black to show high/very high utilization.)

---

### 📈🛜 Spectrum Views: WLAN Integration

❗ Spectrum Analysis + Information of WLANs similar to a **`Wi-Fi analyzer tool (SSIDs name, RSSI, etc)`**

![image](https://github.com/user-attachments/assets/58e58b23-730f-4847-9367-c739b233b574)

![image](https://github.com/user-attachments/assets/0a65699f-7e3d-4121-bd8b-d74047af6279)

![image](https://github.com/user-attachments/assets/ca4d9783-d349-4231-bfd3-3ffb4396969e)

![image](https://github.com/user-attachments/assets/ab67d025-cc06-4a15-8ba5-31aba86c91f6)

![image](https://github.com/user-attachments/assets/601057a7-a20f-4911-98b8-f06d4f2dc108)


- When spectrum analyzer has WiFi integration capability, it can combined those views. WiFi NIC can scan other channels & report that information to give a overall view on a particular band.
- Spectrum analyzers show layer one information. It is frequently useful to view information from layer 2 within the same views. WLAN integration with spectrum analysis software enables this feature. The images below show the SSIDs and number of APs in Spectrum XT. We can also see detailed information in Ekahau about the APs, the SSIDs they broadcast, along with operating and capability information.


## SNR and Noise Floor

The amount of background energy, Wi-Fi and non, is the noise floor. It is always important to know the amount of noise in an area because wireless networks are designed around devices and applications. For example, Voice-grade wireless expects a signal-to-noise ratio (SNR) of 25dB. To calculate the SNR of a signal, we take the received signal strength indicator (RSSI) and noise floor value (-92dBm in the example below). The difference between these two values is the SNR. Each device has a unique receive sensitivity and will perceive the RSSI and noise floor differently than others. This results in newer devices, with higher receive sensitivity, being able to demodulate the same data rates at greater distances than older devices. Know that a large percentage of noise comes from access points and client devices. To fully understand what the noise floor is in a given area, you should survey or perform spectrum analysis during a time of normal usage.


## Spectrum Analyzer: `Analyzers Options`

- Laptop based Spectrum Analyzers: Used very common to analyze wireless networks ::
- Smartphone / Tablet based Spectrum Analyzers: Used very common to analyze wireless networks ::
- Handheld Spectrum Analyzers: Used very common to analyze wireless networks ::
- AP based Spectrum Analyzers: Used very common to analyze wireless networks ::
- Overlay Sensor Spectrum Analyzers: Used tuoanalyze wireless networks ::
- Desktop Spectrum Analyzer: Not very used to analyze wireless networks :: Instead of connecting the radio of the AP to an antenna, you can use that radio to connect it to a PC, tablet, or any other device which support it. This is achieved using a cable. 






## Spectrum Analyzers

### Laptop based:
- Netscout Airmagnet Spectrum Adapter (previously Fluke Networks) used with Spectrum XT,
- [Metageek’s Wi-Spy Spectrum Analyzer for use with Chanalyzer](https://wifinigel.blogspot.com/2019/06/metageek-wi-spy-air-review.html)
- Ekahau Sidekick for use with Ekahau Pro.
- [Wifi Surveyor](https://rfexplorer.com/wifisurveyor/)

### Access Point Based
_Centralized infrastructure allows for coordinated RBW adjustments across multiple access points (APs). This can ensure that spectrum analysis is performed optimally across the network, minimizing interference and maximizing signal clarity. In contrast, laptop-based analyzers may not have this coordinated control and optimization capability._
- [Ruckus AP Spectrum Analysis]()

## Spectrum Analysis Views / Displays



## Spectrum Analysis Displays:

- Real-time FFT: Phase Domain - Frequency represent in horizontal axis and the energy in dBm defined in vertical axis
- FFT Duty Cycle - This view displays the percentage of time the ambient RF signal is higher than the noise floor or other predefined signal threshold. In this veiw you can see whether a device is constantly using a frequency (100% duty cycle on a particular channel mean it is not usable & caused by sort of jammers)
- Spectrogram Graph (Waterfall plot) - This use the same data from Real Time FFT, but with the addition of time dimension. In this view vertical axis shows the historical data. In this case energy in dB values represent in colors (Blue to RED to represent weaker to stronger energy).
- Spectrum Density - Horizontal axis represent frequency & vertical axis represent energy in dBm with brightness of color being determined by how many times that specific bit of information has been captured.
- WiFi integration - When spectrum analyzer has WiFi integration capability, it can combined those views. WiFi NIC can scan other channels & report that information to give a overall view on a particular band.



### Spectrum Analysis: `Duty Cicle`
_Spectrum analyzer displays a measurement of the amount of time a received signal amplitude is above the noise floor or another arbitrary threshold. Although the term duty cycle can be subjective based on the context in which it is used within WLAN technology, it is commonly identifies the percentage of time an RF signal is above a specific threshold. A high duty cycle such as 95-100% can indicate a problem such as an RF jammer or other devise that is causing high utilization of the RF channel._
- [Low Duty Cicle VS High Duty Cicle :: Channel Utilization]()

### Spectrum Analysis: `FFT Plot`

### Spectrum Analysis: `Device Finder`
- [Omnidirectional VS Directional Antenna]()
- [It Took MONTHS to Solve This WiFi Problem but I DID!](https://www.youtube.com/watch?v=f-dGcs6bb5U&t=537s)

### Spectrum Analysis: `waterfall view`
_In some cases RF related problems may not be consistent. The best way to identify these problems would be to view the RF over a period of time. The waterfall view allows you to view a RF channel or band over a period of time._




## Spectrum Analysis: `Device Signatures` & `Non-WiFi Interference`
- [Metageek :: Wi-Fi & No-Wi-Fi Interference examples](https://www.metageek.com/training/resources/wifi-and-non-wifi-interference/)
- [Metageek :: Interference Identification Guide](https://www.4gon.co.uk/documents/meetageek_interference_identification_guide.pdf)
- [Ekahau :: Identifying Wi-Fi Interference with Ekahau Analyzer](https://www.ekahau.com/blog/identifying-wi-fi-interference-with-ekahau-analyzer/)
- [Aruba :: No-Wi-Fi interference examples](https://www.arubanetworks.com/techdocs/ArubaOS_8.11.0_Web_Help/Content/arubaos-solutions/spectrum-analysis/non-wifi-inte.htm) <br> <br>
- [Wideband Jammer]() `Ultra high & Wide Duty Cicle`
- [Bluetooth]() `Low Duty Cicle`
- [Cordless Phone]() `Low Duty Cicle` | 2 or more channels
- [Wireless Camera]() `High Duty Cicle`




## Spectrum Analysis: `Find non RF Device`

two systematic methods for dividing and locating or tracking unknown RF devices are:

	
- Triangulation
- Quadrants







# Device Signartures

## 802.11 Wi-Fi Singatures

802.11 has two basic shapes: 

1. 802.11b - **HR-DSSS** (PSK/BPSK/QPSK) :: Transmissions look like a **bell curve**. 
2. 802.11g/n/ac/ax - **OFDM** (MCS Table) :: Transmissions has faster data rates with **flat across the top**.

Note: The noise floor can be seen at the bottom around -90db

- **`TRICK`: IN SOME SCENARIOS IT IS POSSIBLE TO KNOW THE DIFFERENCE BETWEEN `OFDM` AND `HT` SPECTRUM SIGNATURE**. The OFDM (Orthogonal Frequency Division Multiplexing) and VHT (Very High Throughput) Physical Layers (PHYs) are **only available in the 5 GHz frequency band**. The HT (High Throughput) PHY is **available in both 2.4 GHz and 5 GHz**. So, when a "OFDM" signature is located on 2.4GHz band, it may be an HT signature. 

![image](https://github.com/user-attachments/assets/db7c8990-a181-4ae7-aeca-2071c7d870d6)

---

### Signatures: `2.4 GHz` : `802.11b` / `Wi-Fi 1` : `HR-DSSS` (_`PSK / BPSK / QPSK`_) : `22 MHz`

- 802.11 BPSK / QPSK
- PHY: 2.4 GHz
- Data Rates: 1, 2, 5.5, 11 Mbps
- Channel Width: 22 MHz

![image](https://github.com/user-attachments/assets/d8849142-d6a8-4889-82c4-ebbf15a6b56f)

![image](https://github.com/user-attachments/assets/4f42cd14-cb38-4679-8b49-9639f9771089)

![image](https://github.com/user-attachments/assets/2ccb8151-0272-413f-96a5-ea8c7c372e73)

![image](https://github.com/user-attachments/assets/5c976d42-90c0-438a-817f-1d7028f4c085)


---

### Signatures: `2.4 GHz` : `802.11g` / `Wi-Fi 3` : `ERP-OFDM` : `20 MHz`

- 802.11 ERP-OFDM
- PHY: 2.4 GHz
- Data Rates: 6, 12, 24, 54 Mbps 
- Channel Width: 20 MHz
- 802.11g brought OFDM to 2.4GHz (The views are the same as 802.11a.)

![image](https://github.com/user-attachments/assets/11f5da3e-6f51-465b-bb01-e6d146248425)

![image](https://github.com/user-attachments/assets/34e437b2-9363-490f-901a-f2baf5d5bca0)

![image](https://github.com/user-attachments/assets/c130adf7-c929-450d-990b-8898a78e2533)



---

## 802.11a/n/ac – OFDM/HT/VHT

- Identifying OFDM, HT and VHT using spectrum analyzers is a matter of identifying bonded channels.
- HT & VHT standards use OFDM digital modulation.
- 802.11n introduced 40MHz wide channels.
- 802.11ac introduced 80 and 160MHz wide channels.

Identifying 40, 80, and 160MHz wide channels are easy; they appear as a wider 20MHz OFDM split on the center channel. With bonded channels, all management and control frames are sent on the primary channel which results in that channel being busier than others due to the required overhead to send 802.11 frames. Be sure you understand the number of subcarriers in use with OFDM when using 20 and 40 MHz wide channels.

![image](https://github.com/user-attachments/assets/890704c7-57fb-4273-98ab-1c574d70623b)


### Signatures: `5 GHz` : `802.11a` / `Wi-Fi 2` : `OFDM` (`BPSK, QPSK, 16QAM, 64Qam`) : `20 MHz`

- PHY: 5 GHz
- Data Rates: 6-54 Mbps
- Channel Width: 20 MHz
- Subcarrier Spacing = 312.15 Khz
- Total Subcarriers = 52
- Pilot Subcarriers = 4
- Data Subcarriers = 48

![image](https://github.com/user-attachments/assets/f1d36aaa-5c27-487c-a7c6-cbf9bc22e898)

![image](https://github.com/user-attachments/assets/4fbe7790-8bbe-4edd-9219-ad843271600c)

![image](https://github.com/user-attachments/assets/112eb11a-1b2e-4a45-b2f2-00fd101b2d56)

![image](https://github.com/user-attachments/assets/91e3d557-ba9a-4b52-a09b-59fe29de099b)

---

### Signatures: `5 GHz` : `802.11n` / `Wi-Fi 4` : `OFDM - 64 QAM` : `20 MHz`

- PHY: 2.4 & 5 GHz
- Data Rates: 6-450 Mbps
- Channel Width: 20-40 MHz

![image](https://github.com/user-attachments/assets/d8f764c6-5123-4922-b0d3-f209462b0e63)

---












### 80 mhZ:

Identifying 40, 80, and 160MHz wide channels are easy; they appear as a wider 20MHz OFDM split on the center channel. With bonded channels, all management and control frames are sent on the primary channel which results in that channel being busier than others due to the required overhead to send 802.11 frames.

![image](https://github.com/user-attachments/assets/8a5ca02e-1270-4755-8dd7-1cc153007247)






































## NON-802.11 Wi-Fi Singatures

### ZigBee

![image](https://github.com/user-attachments/assets/290e9a85-55a7-400f-9a8c-2375a6830f90)


### Bluetooth : 2.4 GHz

- Bluetooth devices are active in the 2.4 GHz band.
- These devices are **frequency hoppers that impact all channels**, so you can't move your Wi-Fi to avoid their transmissions.
- However, Bluetooth devices are relatively low-powered and hop very quickly, and **will have limited impact on Wi-Fi devices**.
- It isn't until **many Bluetooth devices are active simultaneously that you are likely to see problems with your Wi-Fi.**

![image](https://github.com/user-attachments/assets/5c686312-b844-4579-9c5a-1d6c73cf291c)

![image](https://github.com/user-attachments/assets/b0260fa5-7786-4a99-b3d6-0951a886a62f)

![image](https://github.com/user-attachments/assets/b40d0966-0ed6-4fe9-9936-f50e6739da83)

![image](https://github.com/user-attachments/assets/2224c7c5-57f8-482d-8d2b-3c3387fa0901)

![image](https://github.com/user-attachments/assets/4d700012-f5cb-4b6f-9e54-d36e4e0903e0)


--- 

### Cordless Phone : 2.4 GHz

- **Not all cordless phones create the same pattern in the spectrum.**
- Some may create a **constant spike in amplitude**
- Some may frequency hop **across the entire spectrum.**
- Cordless phones may change their frequency each time they are used.
- **Channel changes will be noticeable in the `amplitude history` or `waterfall`.**

![image](https://github.com/user-attachments/assets/1780f1b6-0178-486c-b085-9cccdcd718e7)

- Cordless Phone FHSS

![image](https://github.com/user-attachments/assets/e9a1e481-1abd-44ae-b7ea-288f48cbc45b)

![image](https://github.com/user-attachments/assets/ea2362fe-58fe-4437-a9f2-1466c2bf0372)


--- 

### Microwave : 2.4 GHz

- Microwave ovens operate in the 2.4 GHz band
- Typically create a **mountain-like shape in the Density View.**
- Most people use a **microwave oven in exact time lengths like 1 minute bursts, which are easily measured in the `Waterfall View`.**
- The amplitude levels of microwave oven leakage in the 2.4 GHz vary depending on their age, shielding, and distance from the spectrum analyzer.

![image](https://github.com/user-attachments/assets/8cbf3c61-ef11-47b5-8ef9-5daec9f98d2a)

![image](https://github.com/user-attachments/assets/b68fd8f6-9e3d-431b-9cf5-17f1ccb44d8f)


--- 

### Jammer

![image](https://github.com/user-attachments/assets/eb2b61ff-7334-4f7d-80a9-bedbea0a7a55)

### Narrow Band Jammer

- Jamming only narrow targeting

![image](https://github.com/user-attachments/assets/2e548a55-51af-4316-960b-42faa38a7c08)



### Video Camera

- 3 spikes is tyical for a videp camera

![image](https://github.com/user-attachments/assets/f9a8b02e-78b3-482f-8aa2-51e32737a7d6)








AX FFT

![image](https://github.com/user-attachments/assets/46b32017-540b-450d-9f4d-83ea1055344c)



AX SWEPT

![image](https://github.com/user-attachments/assets/464bc598-0dcf-4ab8-a2cd-4a681cdfdb33)
















## Spectrum Analysis: `Device Signatures` & `Non-WiFi Interference`
- [Metageek :: Wi-Fi & No-Wi-Fi Interference examples](https://www.metageek.com/training/resources/wifi-and-non-wifi-interference/)
- [Metageek :: Interference Identification Guide](https://www.4gon.co.uk/documents/meetageek_interference_identification_guide.pdf)
- [Ekahau :: Identifying Wi-Fi Interference with Ekahau Analyzer](https://www.ekahau.com/blog/identifying-wi-fi-interference-with-ekahau-analyzer/)
- [Aruba :: No-Wi-Fi interference examples](https://www.arubanetworks.com/techdocs/ArubaOS_8.11.0_Web_Help/Content/arubaos-solutions/spectrum-analysis/non-wifi-inte.htm) <br> <br>
- [Wideband Jammer]() `Ultra high & Wide Duty Cicle`
- [Bluetooth]() `Low Duty Cicle`
- [Cordless Phone]() `Low Duty Cicle` | 2 or more channels
- [Wireless Camera]() `High Duty Cicle`




## Spectrum Analysis: `Find non RF Device`

two systematic methods for dividing and locating or tracking unknown RF devices are:

	
- Triangulation
- Quadrants















































## Resources

- [Wireless Spectrum Analysis Tips](https://www.youtube.com/watch?v=ImSRW6CHcto) _`CWNP`_
- [Spectrum Analysis – PHYs and Interferers / Key Concepts](https://howiwifi.com/2020/07/03/spectrum-analysis-phys-and-interferers/) _`How to Wi-Fi`_
- [Spectrum Analysis](https://mrncciew.com/2014/10/17/cwap-spectrum-analysis/) _`nayarasi`_
- [Spectrum Analysis – PHYs and Interferers](https://howiwifi.com/2020/07/03/spectrum-analysis-phys-and-interferers/) _`how to Wi-Fi`_
- [FFT Tutorial // capturing and sampling with spectrum analyzer](https://www.youtube.com/watch?v=zKKGA30bHG0) _`video`_
- [Fundamentals of Real-Time Spectrum Analysis](https://svelto.faculty.polimi.it/didattica/materiale_didattico/materiale%20didattico_MRF/appnote/real_time_spectrum_analysis.pdf)
- [Metageek Wi-Spy Air Review](https://wifinigel.blogspot.com/2019/06/metageek-wi-spy-air-review.html) _`Wi-Fi nigel`_
- [Spectrum Analyzer How-To Guide](https://www.tek.com/en/documents/primer/what-spectrum-analyzer-and-why-do-you-need-one)
- https://aaronia.com/en/produkte/spectrum-analyzer?gad_source=1&gclid=CjwKCAiArva5BhBiEiwA-oTnXYGyJiON7XUdmxe3T9QGLJMCTTWrgasiRr0HBe1w5ME1yVcsmqvYWhoCOGkQAvD_BwE
- https://telonic.co.uk/real-time-vs-swept-spectrum-analysers/
- https://rfexplorer.com/wifisurveyor/
- https://www.cleartosend.net/spectrum-analysis/
- https://www.youtube.com/watch?v=ImSRW6CHcto
- https://support.metageek.com/hc/en-us/articles/201872824-Chanalyzer-5-Wi-Spy-User-Guide
- https://www.arubanetworks.com/techdocs/ArubaOS%206_3_1_Web_Help/Content/ArubaFrameStyles/Spectrum_Analysis/Customizing_Spectrum_Ana.htm#spectrum_analysis_69050016_1006374
- https://www.emona-tims.com/wp-content/uploads/2015/10/ILLINOIS-I-T-Spectral-Signatures-and-Interference-of-802_11-Wi-Fi-Signals-with-Barker-Code-Spreading.pdf
- https://www.4gon.co.uk/documents/meetageek_interference_identification_guide.pdf
- https://www.youtube.com/watch?v=w1mdQn-XL6U
- https://www.youtube.com/@AaroniaDe/videos
- https://www.batterfly.com/shop/en/blog-posts/introduction-density-view-spectrum-analyzer
- https://www.youtube.com/watch?v=YjXpc6uTg3g
- https://www.youtube.com/watch?v=r41ut1XfM7s
- https://www.youtube.com/watch?v=tKXsxqBsWMg
- https://www.sharetechnote.com/html/WLAN_PHY_Frames.html










In


<p align="center"> <img src="https://github.com/user-attachments/assets/807020b5-82bd-4313-8213-99a4a646f226" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/288352d5-8e95-44c5-8a14-8ec490c841dc" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/a6c4fa0d-bc83-4fe1-aaf0-34e9b0156266" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/738d0c96-dec6-41d4-9deb-dc2f93f04df5" width="300" height="300"> 
<img src="https://github.com/user-attachments/assets/e5ceb6d6-c752-43a8-ab50-cfc592ccd49f" width="300" height="300">
<img src="https://github.com/user-attachments/assets/bbe05510-5d98-4fcb-ba25-a5110ccf78da" width="300" height="300"> </p>


<p align="center"> <img src="https://github.com/user-attachments/assets/807020b5-82bd-4313-8213-99a4a646f226" height="300> </p>



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
