# 🧠🏗️🌐 Ruckus SmartZone: `Configure AAA 802.1X Authentication with Windows Server RADIUS (NPS)`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords: `Cisco` `CCNA` `CCNP` `Datacenter` `NX-OS` `Cisco Nexus` `Leaf & Spine` `DC Switching` `Modular Chassis` `Fixed Form Factor` `vPC` `ECMP` `FEX` `Fabric Extender` `Nexus 2000` `Nexus 5000` `Nexus 7000` `Nexus 9000`  `Port-Channel` `LAG` `VLAN` `VRF` `Overlay` `Underlay` `EVPN` `VXLAN`  `Spine Switch` `Leaf Switch` `Control Plane` `Forwarding Plane` `Supervisor Card` `Line Card`  `Redundant Power Supply` `Hot-swappable` `In-Service Software Upgrade (ISSU)` `High Availability`  `Twinax Cable` `SFP+` `QSFP28` `QSFP-DD` `10G` `25G` `40G` `100G` `400G`

---

<br>

# 📄 `Index`

# 🛜🐶🔐 Ruckus SmartZone: `Configure AAA 802.1X Authentication with Windows Server RADIUS (NPS)`

<img width="362" height="425" alt="image" src="https://github.com/user-attachments/assets/754f0edb-3043-4951-89cb-042bea295da8" />

<img width="371" height="415" alt="image" src="https://github.com/user-attachments/assets/2832be0f-fd95-4042-8de8-4cb3bffe37f4" />


<img width="365" height="407" alt="image" src="https://github.com/user-attachments/assets/c08bb31a-8174-4bda-813d-7b1c5fa4d857" />

<img width="360" height="414" alt="image" src="https://github.com/user-attachments/assets/146f58fd-b407-42cd-99b3-ff56a30f9080" />

<img width="392" height="404" alt="image" src="https://github.com/user-attachments/assets/aa7d71d4-a1f0-4c02-928c-c4be50befcd0" />

<img width="404" height="515" alt="image" src="https://github.com/user-attachments/assets/ef75feef-0158-47b7-8316-18a0e7ca632a" />



## PEAP and Certificate explanation

PEAP Certificate Validation real life example:

- Many Android devices (especially Xiaomi, Huawei, some Samsung models) default to “Do not validate certificate” when configuring Wi-Fi with EAP-PEAP/MSCHAPv2.

- This allows them to connect without prompting the user about the RADIUS server’s certificate, even if it’s self-signed or untrusted.

- While convenient, it exposes users to “evil twin” or rogue AP attacks, since the client will trust any server that presents a PEAP tunnel.

By contrast:

- iOS and macOS are stricter: they prompt the user to explicitly trust the server certificate the first time.

- Windows also enforces certificate validation by default, warning if the CA isn’t trusted.

On Android, users can manually enable certificate validation by selecting “Use system certificates” and specifying the trusted CA. However, many skip this step or leave it as “Do not validate,” creating a security gap.


## Descargar certificado a mano (manual fast & ez)



---

## Unir laptop a dominio (certificado automatico y enrollment)

Pasos para unir tu laptop a tu dominio fz3r0.dojo

1. Confirma la red/DNS

- Tu laptop debe tener como DNS principal la IP de tu controlador de dominio (el Windows Server donde instalaste AD DS).
- Ejemplo: si tu servidor tiene la IP 192.168.1.100, en la laptop pon eso como DNS (si usas otro DNS no va a resolver fz3r0.dojo).

2. Comprueba con (Debe devolverte la IP de tu server):

- nslookup fz3r0.dojo

Abre configuración del sistema en tu laptop:

- Haz clic derecho en Este equipo → Propiedades / O ve a Panel de control → Sistema y seguridad → Sistema.
- Ahí verás el nombre del equipo y el grupo de trabajo.
- Cambiar a dominio
- Haz clic en Cambiar configuración (a la derecha, donde dice “Nombre del equipo, dominio y grupo de trabajo”).
- En la nueva ventana, dale a Cambiar….
- Marca Dominio y escribe: fz3r0.dojo

3. Credenciales

- Te pedirá un usuario con permisos en el dominio (generalmente tu Administrador de AD).
- Ejemplo Usuario: fz3r0\Administrator
- Password: el del admin que creaste al instalar AD.
- Exit y reinicio

Si todo sale bien, te dirá “¡Bienvenido al dominio fz3r0.dojo!”.

- Dale aceptar y reinicia la laptop.
- Inicia sesión con tu usuario de dominio
- En el login ya no solo verás la cuenta local. Ahora podrás elegir un usuario de AD.
- Ejemplo Usuario: fz3r0\juanito
- Password: el que configuraste en AD.

A partir de ese momento, tu laptop es parte del dominio. Ya puedes aplicar Group Policies (GPO), empujar certificados, mapear carpetas, etc.

# 🗃️ Resources

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
