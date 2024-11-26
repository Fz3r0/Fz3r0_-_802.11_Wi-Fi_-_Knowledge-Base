
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




## 📈📏 Spectrum Views: `Real time FFT (Fast Fourier Transform)`

- `Frequency` represented in **horizontal** axis
- `Energy` represented in **`dBm defined`** in **vertical** axis

<p align="center"> <img src="https://github.com/user-attachments/assets/a66c4bfa-b413-4c6a-954c-58ca4ded148f" height="450"> </p>

<p align="center"> <img src="https://github.com/user-attachments/assets/115dafa3-ff0d-4811-9209-fcccb386aff5" height="170"> </p>



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

![image](https://github.com/user-attachments/assets/2168616b-b5d3-4be8-b9db-bbea11227ab3)


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

- Swept: This is the same information as the real-time FFT but often in a different view and tracked over a longer period. These views can often be configured within software to specify the length of time
- Waterfall: The information from the swept spectrogram showing time, frequency, and power but viewed vertically.

#### Swept View

![image](https://github.com/user-attachments/assets/21a3c49a-33f2-47db-9dad-bf99953247d1)



#### Waterfall View

![image](https://github.com/user-attachments/assets/b9985589-e1a3-42f4-b534-ff94315d311c)



![image](https://github.com/user-attachments/assets/756e48bf-a7af-47d2-9af5-7212337e93fe)

![image](https://github.com/user-attachments/assets/e7242689-bf1f-42e6-8b7d-08274a2b598f)




- This view is considered a **Swept Spectrum Analyzer (SA).**
- This is the **same information as the real-time FFT** but often in a different view and tracked over a longer period.
- These views can often be configured within software to specify the length of time.
- The **Waterfall View** is the information from the **swept spectrogram** showing: time, frequency, and power but viewed vertically.

---

### 📈🌈 Spectrum Views: `Power Spectral Density` / `Density View`

❗ Horizontal axis represent frequency & vertical axis represent energy in dBm with **`brightness of color`** being determined by how many times that specific bit of information has been captured.

![image](https://github.com/user-attachments/assets/2e19ae70-850f-4679-8836-2534293e4931)

![image](https://github.com/user-attachments/assets/92fc8055-15eb-4e42-97f9-4b8ba2dd992c)




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


### Signatures: `2.4 GHz` : `PSK` : `20 MHz`

![image](https://github.com/user-attachments/assets/2ccb8151-0272-413f-96a5-ea8c7c372e73)




### Signatures: `5 GHz` : `OFDM` : `UNNI-2` : `20 MHz`

![image](https://github.com/user-attachments/assets/91e3d557-ba9a-4b52-a09b-59fe29de099b)











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
