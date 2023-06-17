# Management Frames: `Beacon`

Los `Beacon Frames` son utilizados por los `APs` (y `STAs` en una `IBSS`) para **comunicar a través del área de servicio las características de la conexión ofrecida a los miembros de una `WLAN` dentro de la celda de cobertura del `AP`. Esta información es utilizada por los clientes que intentan conectarse a la red, así como por los clientes que ya están asociados al `BSS`.**

- Las Beacon Frames se envían periódicamente en un momento llamado `Target Beacon Transmission Time (TBTT).`

Los valores por default de un Beacon Frame son los siguientes:

- **`1 TU` = 1024 microsegundos**
- **`Beacon interval`  = 100 TU** (100 x 1024 microsegundos o 102.4 milisegundos)

Este es el Frame Format de un Beacon Frame:

![image](https://github.com/Fz3r0/Fz3r0_-_BlackShark/assets/94720207/2ac8ca5b-c2c8-4fe2-9fea-764ff9e57f77)

- En la sección del `Frame Body`, hay algunos **campos obligatorios** y algunos **campos opcionales**. 

Aquí están los campos obligatorios en un marco de baliza:

## Recursos

[CWNE#153 (Rasika Nayanajith) - 802.11 Mgmt : Beacon Frame](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
