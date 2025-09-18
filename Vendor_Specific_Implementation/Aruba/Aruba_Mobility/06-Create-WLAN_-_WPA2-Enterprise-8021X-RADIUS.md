# 🏝️📡🛰️ Aruba Mobility: `Aruba Mobility - Create WLAN WPA2-Enterprise : 802.1X : RADIUS`

![My Video](https://user-images.githubusercontent.com/94720207/165892585-b830998d-d7c5-43b4-a3ad-f71a07b9077e.gif)

### 🐦 Twitter  : [@fz3r0_OPs](https://twitter.com/Fz3r0_OPs)
### 🐱 Github  : [Fz3r0](https://github.com/fz3r0) 

---
 
#### Keywords:  

`Aruba` `Mobility Controller` `Mobility Master` `ArubaOS` `AOS 8.x` `ACMA` `ACMP` `ACMX` `ACMX` `ACA‑Campus Access` `ACP‑Campus Access` `ACX‑Campus Access`  `AP` `Access Point` `Thin AP` `Campus AP` `Remote AP` `Instant AP (IAP)` `CAP` `RAP` `Control Plane` `Data Plane` `Centralized Forwarding` `Distributed Forwarding` `Tunnel Mode` `Bridge Mode` `WLAN` `SSID` `AAA Profile` `Role` `User Role` `Firewall Policy`  `Captive Portal` `Guest Access` `Mobility Domain` `LMS (Local Mobility Switch)` `Backup LMS` `Master-Local Architecture` `AP Fast Failover` `AP Database` `AP License` `PAPI Protocol` `Zoning` `Zone Assignment` `ARM (Adaptive Radio Management)` `Airmatch` `ClientMatch`  `IDS` `IPS` `Air Monitor` `Spectrum Analysis` `Cluster VRRP` `Controller Redundancy` `Aruba Licensing Model` `Policy Enforcement Firewall (PEF)` `AppRF` `DPI (Deep Packet Inspection)` `User Visibility` `AP Provisioning` `PKI` `ClearPass`  `Rolling AP Upgrade` `Zero Touch Provisioning (ZTP)` `Dynamic Segmentation` `Uplink` `GRE/IPSec Tunnel` `Branch Office RAP` `VPNC (VPN Concentrator)` `Overlay` `Underlay`


---

<br>

# 📄 `Index`


# 🏝️📡 Aruba Mobility :: `Create WLAN WPA2-Enterprise : 802.1X : RADIUS`

### IMPORTANT!!! 

BEFORE CONFIGURING AN SSID IN OTHER VLAN THAT DEFAULT 1, YOU NEED TO MAKE SURE THE MANAGEMENT INTERFACE OF THE MM IS SET TO TRUNK, ALLOWING THE VLANS WE WANT TO USE. EVEN IF THE MM IS LOCATED REMOTLY ON ANOTHER SUBNET, THIS BRINGS UP THE VLAN INTERFACE. 

<img width="1352" height="753" alt="image" src="https://github.com/user-attachments/assets/8df868af-dd53-4401-991d-2703be891492" />

Por alguna razon, con todas las VLANs fucniona el broisdge cuando las pongo dentro del trunk.... pero si intent con la vlan 300 radiarla, la cual ya es el mgmt de los APs, me sale como que tunneled bien raro: 

````
(MGD-DEV::MC-Fz3r0-1) #show user-table verbose

Users
-----
    IP              MAC            Name     Role         Age(d:h:m)  Auth           VPN link  AP name  Roaming             Essid/Bssid/Phy                        Profile               Forward mode  Type  Host Name  User Type  Server    Vlan       Bwm  UaStr:ParseDisable/Flag/ShortIndex
----------     ------------       ------    ----         ----------  ----           --------  -------  -------             ---------------                        -------               ------------  ----  ---------  ---------  ------    ----       ---  ----------------------------------
10.10.130.101  00:00:00:00:00:00            sys-ap-role  00:00:43    TRANSPORT-VPN            N/A                                                                 default-cap           tunnel                         WIRELESS             0 (0)           OFF/0/0
10.10.30.102   44:e5:17:06:e4:60            00-ALL       00:00:02                             Fz3r0    Associated(Remote)  Fz3r0-Aruba/f4:2e:7f:03:0f:50/5GHz-HE  Fz3r0-Aruba_aaa_prof  bridge                         WIRELESS             300 (300)       OFF/0/0

User Entries: 2/2
 Curr/Cum Alloc:2/18 Free:1/16 Dyn:3 AllocErr:0 FreeErr:0
(MGD-DEV::MC-Fz3r0-1) #show ap config ap-name Fz3r0 | include virtual-ap
Virtual AP enable                                               Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
VLAN                                                            300              300              N/A             300              wlan virtual-ap "Fz3r0-Aruba"
Forward mode                                                    bridge           bridge           N/A             bridge           wlan virtual-ap "Fz3r0-Aruba"
Allowed band                                                    all              all              N/A             all              wlan virtual-ap "Fz3r0-Aruba"
Allowed 5G radio                                                all              all              N/A             all              wlan virtual-ap "Fz3r0-Aruba"
Allow 6GHz band                                                 Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Disable 6GHz vap for mesh                                       Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Allow-band-6GHz-supplement                                      Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Band Steering                                                   Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Cellular handoff assist                                         Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Openflow Enable                                                 Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Fine Timing Measurement (802.11mc) Responder Mode               Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Steering Mode                                                   prefer-5ghz      prefer-5ghz      N/A             prefer-5ghz      wlan virtual-ap "Fz3r0-Aruba"
Dynamic Multicast Optimization (DMO)                            Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Dynamic Multicast Optimization (DMO) Threshold                  6                6                N/A             6                wlan virtual-ap "Fz3r0-Aruba"
Drop Broadcast and Multicast                                    Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Convert Broadcast ARP requests to unicast                       Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Authentication Failure Denylist Time                            3600 sec         3600 sec         N/A             3600 sec         wlan virtual-ap "Fz3r0-Aruba"
Denylist Time                                                   3600 sec         3600 sec         N/A             3600 sec         wlan virtual-ap "Fz3r0-Aruba"
Deny inter user traffic                                         Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Deny time range                                                 N/A              N/A              N/A             N/A              wlan virtual-ap "Fz3r0-Aruba"
DoS Prevention                                                  Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
HA Discovery on-association                                     Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Mobile IP                                                       Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Preserve Client VLAN                                            Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Remote-AP Operation                                             standard         standard         N/A             standard         wlan virtual-ap "Fz3r0-Aruba"
Station Denylisting                                             Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Strict Compliance                                               Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
VLAN Mobility                                                   Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
WAN Operation mode                                              always           always           N/A             always           wlan virtual-ap "Fz3r0-Aruba"
FDB Update on Assoc                                             Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Pure UAC BSS Deferred Deletion Delay                            10 min           10 min           N/A             10 min           wlan virtual-ap "Fz3r0-Aruba"
(MGD-DEV::MC-Fz3r0-1) # 
````

y en otra vlan como la 30, si sirvey se ve así: 

````
(MGD-DEV::MC-Fz3r0-1) #show user-table verbose

Users
-----
    IP                          MAC            Name     Role         Age(d:h:m)  Auth           VPN link  AP name  Roaming             Essid/Bssid/Phy                         Profile               Forward mode  Type   Host Name  User Type  Server    Vlan     Bwm  UaStr:ParseDisable/Flag/ShortIndex
----------                 ------------       ------    ----         ----------  ----           --------  -------  -------             ---------------                         -------               ------------  ----   ---------  ---------  ------    ----     ---  ----------------------------------
10.10.130.101              00:00:00:00:00:00            sys-ap-role  00:00:29    TRANSPORT-VPN            N/A                                                                  default-cap           tunnel                          WIRELESS             0 (0)         OFF/0/0
10.10.30.101               be:7c:4c:22:56:51            00-ALL       00:00:00                             Fz3r0    Associated(Remote)  Fz3r0-Aruba/f4:2e:7f:03:0f:50/5GHz-VHT  Fz3r0-Aruba_aaa_prof  bridge        Linux             WIRELESS             30 (30)       ON/1/105
fe80::bc7c:4cff:fe22:5651  be:7c:4c:22:56:51            00-ALL       00:00:00                             Fz3r0    Associated(Remote)  Fz3r0-Aruba/f4:2e:7f:03:0f:50/5GHz-VHT  Fz3r0-Aruba_aaa_prof  bridge        Linux             WIRELESS             30 (30)       ON/1/105


Total Roles:15
(MGD-DEV::MC-Fz3r0-1) #show ap config ap-name Fz3r0 | include virtual-ap
Virtual AP enable                                               Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
VLAN                                                            30               30               N/A             30               wlan virtual-ap "Fz3r0-Aruba"
Forward mode                                                    bridge           bridge           N/A             bridge           wlan virtual-ap "Fz3r0-Aruba"
Allowed band                                                    all              all              N/A             all              wlan virtual-ap "Fz3r0-Aruba"
Allowed 5G radio                                                all              all              N/A             all              wlan virtual-ap "Fz3r0-Aruba"
Allow 6GHz band                                                 Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Disable 6GHz vap for mesh                                       Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Allow-band-6GHz-supplement                                      Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Band Steering                                                   Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Cellular handoff assist                                         Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Openflow Enable                                                 Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Fine Timing Measurement (802.11mc) Responder Mode               Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Steering Mode                                                   prefer-5ghz      prefer-5ghz      N/A             prefer-5ghz      wlan virtual-ap "Fz3r0-Aruba"
Dynamic Multicast Optimization (DMO)                            Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Dynamic Multicast Optimization (DMO) Threshold                  6                6                N/A             6                wlan virtual-ap "Fz3r0-Aruba"
Drop Broadcast and Multicast                                    Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Convert Broadcast ARP requests to unicast                       Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Authentication Failure Denylist Time                            3600 sec         3600 sec         N/A             3600 sec         wlan virtual-ap "Fz3r0-Aruba"
Denylist Time                                                   3600 sec         3600 sec         N/A             3600 sec         wlan virtual-ap "Fz3r0-Aruba"
Deny inter user traffic                                         Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Deny time range                                                 N/A              N/A              N/A             N/A              wlan virtual-ap "Fz3r0-Aruba"
DoS Prevention                                                  Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
HA Discovery on-association                                     Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Mobile IP                                                       Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Preserve Client VLAN                                            Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Remote-AP Operation                                             standard         standard         N/A             standard         wlan virtual-ap "Fz3r0-Aruba"
Station Denylisting                                             Enabled          Enabled          N/A             Enabled          wlan virtual-ap "Fz3r0-Aruba"
Strict Compliance                                               Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
VLAN Mobility                                                   Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
WAN Operation mode                                              always           always           N/A             always           wlan virtual-ap "Fz3r0-Aruba"
FDB Update on Assoc                                             Disabled         Disabled         N/A             Disabled         wlan virtual-ap "Fz3r0-Aruba"
Pure UAC BSS Deferred Deletion Delay                            10 min           10 min           N/A             10 min           wlan virtual-ap "Fz3r0-Aruba"

````

### `Step 1`: Crear la VLAN que llevará mi WLAN/SSID

- La VLAN será la que transporte esta red, del lado del backbone esta VLAN tiene que estar configurada en el DHCP en caso de estar en modo bridge, o existir en la controladora en caso de estar tunneled.
- Es decir, la VLAN debe coincidir ya sea con la controladora o la LAN

**Grupo > Sub-Grupo > Configuration > Interfaces > VLAN:**

<img width="1919" height="766" alt="image" src="https://github.com/user-attachments/assets/e0ee79f3-afbd-459a-90d5-410de97bfbec" />

Agregar el VLAN ID y un nombre identificador y hacer deplot de los cambios

- Nota: Mas adelante se podrá seleccionar la VLAN tanto por el nombre como por el número. 

<img width="1952" height="523" alt="image" src="https://github.com/user-attachments/assets/692b81e8-c4af-4cca-8d7b-d8d31525ff8d" />

### `Step 2`: Configurar WLAN (SSID)

- Al principio no existirá ninguna WLAN ya que no hemos creado ninguna

**Grupo > Sub-Grupo > Configuration > WLANs:**

<img width="1919" height="767" alt="image" src="https://github.com/user-attachments/assets/eed65a02-8b77-4dc1-ada4-07cb22236875" />

Llenar los campos según sea necesario, particularmente para este lab yo usaré: 

- Name (SSID): `V10-EMPLOYEE_ENTERPRISE_TUNNEL`
- Primary usage: `Employee`
- Select AP Groups Broadcast: `AP-GROUP1_office-branch-01`
- Forwarding mode: `Tunnel`

NOTA: La gran diferencia entr ebridged y tunnel es que bridged se comporta el AP como un "switch" todas las VLANs que vienen de los SSID saldrán trunkled con 802.1q y por ende el switch también debe ser trunked, uan vez que sale del AP los datos ya todo se pasa a la LAN y ahi se debe hacer cargo del DHCP y demas, tal cual como otro switch truinked. Por otro lado, si esta tunnel todo sera tunneleado por una misma VLAN hasta la controladora, y ya la controladora se harña cargo de DHCP y el control de datos. 

NOTA 2: la diferneci aen aruba con un Employee un y Guest es..... aqui pon que odna vektor. 

<img width="632" height="456" alt="image" src="https://github.com/user-attachments/assets/2c51137b-be52-4d3b-8ad9-56d207c76b95" />

Después, seleccionar la VLAN:

- Aquí podemos usar ya sea el VLAN ID "10" o el nombre completo de la VLAN.
- Podemos incluso ver las VLANs que ya hay creadas por si tenemos duda

<img width="1256" height="658" alt="image" src="https://github.com/user-attachments/assets/69c63a95-8042-4f6d-84c4-0b5f0f1d33fa" />

Ahora pasamos a la parte de seguridad:

- Aquí podemos seleccionar ya sea WPA2 o WPA3 Enterprise, yo usaré WPA2 para fines prácticos
- El reauth interval en aruba es...
- el mahcina authentication es.... por ahor alo dejare en disabled
- el deny listing se suma con el max authentication, aqui simplemente es el nuemro de beves que peudes bla bla... el máximo es 5 

<img width="1173" height="680" alt="image" src="https://github.com/user-attachments/assets/34cd8050-2f3a-43d5-8fcf-8de3f9de1881" />

Hacer click en "+" para agregar el authetnication server. 

- En este lab yo usaré mi Windows Server 2022 Data center, dodne tengo ya un NPS jalando. RADIUS: 192.168.1.86	shared secret:	Cisco.12345

<img width="642" height="491" alt="image" src="https://github.com/user-attachments/assets/0426c71e-ea46-4484-ad28-512c9400ab2b" />

En caso de un "Employee" el Default Role siempre será guest (esto confirmamelo porfa vektor)

<img width="1188" height="238" alt="image" src="https://github.com/user-attachments/assets/c4615fc9-fc75-4fe6-a6b2-5104d3e3a295" />

Y listo! simplemente hacer el deploy: 

<img width="1280" height="291" alt="image" src="https://github.com/user-attachments/assets/93b960cc-73f6-4476-aff2-9ab1807ff08d" />




---

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
