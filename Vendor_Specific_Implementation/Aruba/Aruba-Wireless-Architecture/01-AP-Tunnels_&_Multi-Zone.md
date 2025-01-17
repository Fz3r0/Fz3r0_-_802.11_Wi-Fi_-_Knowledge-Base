# 🔥🧱🛡️ Aruba: `Tunnels & MultiZone`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Aruba` `MC` `Mobility Controller` `WLC` `IEEE 802.11` `Wireless`

---

<br>

# 📝❓📄 `Index`

# Aruba: `Tunnels` & `MultiZone`

before talking about Multi-zone. First, we need to understand tunnels that are created by access points to controller Aruba 

## Aruba: `AP Tunnels`

- Access points will create GRE tunnels.
- And in those tunnels you will see that access points will send the traffic directly to the controller.
- The controller will decrypt the packets in those tunnels because normally the access point receives the packets encrypted.
- The controller will firewall the packet. Then, according to the need, it will either switch the packet inside or route it to the outside network.
- Before this, the user must authenticate to the network and this will happen with the help of control traffic.
- **So as you can see, you will have two tunnels. **One is for data**, the other **one is for control**.
- The **contorl traffic** will use CPSec This is a secure tunnel that is using PaPi protocol using porr 90 and 11 UDP.
- The **data traffic** will use GRE using the port 47.

Extra notes about tunnels:

- When you configure your cluster (WLC) your AP will forward the user traffic to the user controller using the GRE tunnel. 
- An access point will send the control traffic to its access point anchor controller, and this willthis will be sent with the help of puppy.
- Access points will not use the GRE tunnel to forward the user traffic in the bridge mode So this is an exception to sending the user traffic in GRE and the mobility controller, Aruba Mobility

Controller Side Tasks:

- controller will deal with the configuration of access point
-  will deal with the client authentication
-  User roles and firewall policies.

GRE Tunnels

- When you're using GRE tunnels, you need to know that you can have different tunnels for different wireless lans.
- So, when your access point get the configuration from the controller, it essentially creates GRE tunnels and pass that user traffic from the access point to your controller, and APs will create one tunnel per SSID.
- It sill also create one extra GRE tunnel for the keep-alives.
- The total of tunnels will be: **Total SSIDs + 1 (keep alive)**
- If you have 3 SSIDs and 2 radios (2.4 & 5 ghz), then you will have 6 SSIDs and 1 keeps alive:  **Total SSIDs x 2 (2.4 & 5) + 1 (keep alive)**
- So, if we have 10 APs with 2 radios each and 6 SSIDs each would be the total of tunnels:
    - SSIDs = 6
    - APs = 10
    - Keep Alive = 1 * 10
    - GRE for SSIDs = 12 * 10
    - Total Tunels = 130 

# 📚🗂️🎥 Resources

- https://www.arubanetworks.com/assets/matrix/matrix_WLAN-platforms-software-support-matrix.pdf
- https://www.arubanetworks.com/products/wireless/gateways-and-controllers/9200-series/
- https://www.hpe.com/psnow/doc/a00121209enw
  
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





