# 🔥🧱🛡️ Aruba: `Lab - WLANs`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Aruba` `MC` `Mobility Controller` `WLC` `IEEE 802.11` `Wireless`

---



<br>

# 📝❓📄 `Index`


# Wireless LAN Configuration 



In this tutorial, we will walk through the process of configuring a new wireless LAN.

## Step 1: Accessing Wireless LAN Configuration

On your **Mobility Controller** interface, go to the **Configuration** tab. Under Configuration, click on **Wireless LANs**, and then click the **Plus (+)** button to create a new wireless LAN.

![image](https://github.com/user-attachments/assets/330c2250-3ffb-4dd8-a343-bd4b1884ef35)

## Step 2: Naming and Setting Up the Wireless LAN

Assign a name for your SSID. You will also need to select the primary use of the wireless LAN, either for **employee** or **guest** purposes.

- **Employee**: This option provides enterprise-level authentication and encryption options on the security VLANs and access pages.
- **Guest**: This option enables captive portal settings.

![image](https://github.com/user-attachments/assets/d35e2fa7-f080-457a-ade2-82f48c531791)

## Step 3: Broadcasting Options

Next, decide whether to broadcast the SSID.

- **All Access Points**: Select this option to broadcast the SSID across all access points associated with the mobility controller.
- **Specific Groups**: Choose this option if you want to broadcast the SSID only on selected groups you have previously configured.

![image](https://github.com/user-attachments/assets/c9f3c015-e859-4568-9ceb-f7569fd23ddc)

## Step 4: Forwarding Mode Selection

Choose the forwarding mode. You have several options:

- **Tunnel**: Data will be tunneled to the mobility controller.
- **Decrypt Tunnel**: The access point will decrypt and encapsulate all 802.11 frames, sending 802.3 frames through the tunnel to the mobility controller.
- **Bridge**: The access point will perform encryption and decryption, and user traffic will be locally switched or routed (not recommended due to limitations).
- **Split Tunnel**: Wireless traffic is tunneled, while certain traffic is not, allowing a mix of tunneled and decrypted traffic.

![image](https://github.com/user-attachments/assets/3fb6d76f-908d-4172-8e39-7a481f279ca1)

In this case I will select "Tunnel", then click **Next** to continue.

## Step 5: VLAN Configuration

Here, you can configure the VLAN for your wireless LAN. For example, you might select VLAN 87 (or any another VLAN like 51, 5, 666, etc) to associate with your SSID. You can click the **Plus (+)** button to add a new VLAN if needed.

![image](https://github.com/user-attachments/assets/a8cc9516-0735-4a39-9741-61843892ba69)

## Step 6: Security Settings

Now, choose your preferred security settings based on the network type.

- **Enterprise Network**: Choose **WPA3 Enterprise** or **WPA2 Enterprise**. You can select key management options and add a RADIUS server for authentication.

![image](https://github.com/user-attachments/assets/fd2beefd-1762-4c5e-8a3b-33a1efcf8377)

![image](https://github.com/user-attachments/assets/060a54e4-ac82-418f-8e64-fd93890cb4f8)

![image](https://github.com/user-attachments/assets/11a48fd2-bd5e-48b2-a22d-e66e2c34f06d)
  
- **Personal Network**: Enter a passphrase for WPA3 or WPA2 personal security.

![image](https://github.com/user-attachments/assets/8e9f6ee8-4479-4538-b990-8ce8c3e28db4)
  
- **Open Network**: This option doesn't offer encryption but provides MAC authentication if desired.

For enterprise networks, you can configure re-authentication intervals, machine authentication, and blacklist settings to enhance security. Personal and open networks have simpler configurations with fewer options.

## Step 7: Finalizing Configuration
Select a **default role** (e.g., guest, user) for this wireless LAN. We'll discuss roles in more detail in future videos, but for now, selecting a default role is important for defining access levels.

At this point, you have successfully configured your new wireless LAN, including SSID naming, VLAN association, and security options. 

Thank you for watching this tutorial!





# 📚🗂️🎥 Resources

- 
  
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





