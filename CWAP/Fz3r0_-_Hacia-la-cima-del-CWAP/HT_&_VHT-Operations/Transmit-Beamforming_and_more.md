
# Transmit Beamforming

Transmit beamforming got introduced in 802.11n, which has two methods Implicit and Explicit beamforming.


Can be used when there are more transmitting antennas than there are spatial data streams.
A digital signal processing technology on the transmitting device that duplicates the transmitted signal on more than one antenna to optimize a combined signal at the client.
Carefully controlling the phase of the signals transmitted from multiple antennas has the effect of improving gain, thus emulating a higher-gain unidirectional antenna.
Is adjusting the phase of the transmissions.
Result in greater range for individual clients communicating with an access point.
When utilizing transmit beamforming the transmitter will not be sending multiple unique spatial streams but will instead be sending multiple streams of the same data with the phase adjusted for each RF signal.
Types of transmit beamforming:

Implicit TxBF: Uses an implicit channel-sounding process to optimize the phase differentials between the transmit chains.
Explicit TxBF: Requires feedback from the stations in order to determine the amount of phase-shift required for each signal.
The 802.11n amendment defined transmit beamforming:

Optional PHY capability
Can use Implicit TxBF or Explicit TxBF 
The 802.11ac amendment defined transmit beamforming:

Uses Explicit TxBF
requiring the use of channel measurement frames
both the transmitter and the receiver must support beamforming.

## 

## VHT/HE NDP Announcement

- Null data packet (NDP) announcement frames **notify the recipient that an NDP will follow**.

The figure below shows the frame exchange process. The beamformer (AP) will request that the station send an NDP sounding frame by setting the training request (TRQ) value in the Link Adaption Control subfield of the HT Control Field. The information gathered from the sounding frame can be used to calculate a steering matrix for the purpose of using beamforming for future transmissions to the same station.


### NDP Announcement Frame Exchange:

![image](https://github.com/user-attachments/assets/2afe6b10-9a8f-4c9e-928a-a9c07a8ff589)

### NDP Announcement Frame Format:

![image](https://github.com/user-attachments/assets/320d9c8d-d3e6-43cf-9e0a-45c903814c69)


### Link Adaption Control Subfield Format:

![image](https://github.com/user-attachments/assets/db71346c-aade-4a1f-97e5-31bc5f9f4763)


### Announcement Frame:

![image](https://github.com/user-attachments/assets/16b2bb09-f5ff-47ae-ae99-f9b35286e11b)


# Key concepts

- When looking at an 802.11n packet decode in a protocol analyzer, you notice the NDP Announcement subfield set: An **NDP will follow the current frame but will not be seen by a protocol analyzer.**
- During a VHT Transmit Beamforming sounding exchange, the beamformee transmits a Compressed Beamforming frame to the beamformer: **Feedback Matrix is communicated within this Compressed Beamforming frame**



# Resources

- https://wificoops.com/2018/01/14/beam-me-up-scotty/
- https://community.fs.com/blog/beamforming.html
- https://dot11ap.wordpress.com/cwna/radio-frequency-rf-technologies/transmit-beam-forming-txbf-as-defined-in-the-802-11-standard/
- https://www.wirelessnewbies.com/post/transmit-beamforming
- https://howiwifi.com/2020/07/13/802-11-frame-types-and-formats/
- https://www.oreilly.com/library/view/80211ac-a-survival/9781449357702/ch04.html
- https://www.mathworks.com/help/wlan/ug/802-11ac-transmit-beamforming.html
