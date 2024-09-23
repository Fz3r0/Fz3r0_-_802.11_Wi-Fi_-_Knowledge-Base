from scapy.all import rdpcap, raw
import binascii

# Cargamos la captura y vamos iterando los paquetes
scapycap = rdpcap("000 PSK filtrado Facility - facility2018.pcap")
count = 0  # Inicializamos la variable count para contar los mensajes del handshake

for packet in scapycap:
    if packet.haslayer("EAPOL"):
        raw_data = bytes(raw(packet["EAPOL"])).hex()
        # Si es el 1º mensaje del handshake
        if count == 0:
           # Extraemos anonce y lo pasamos a bin
           anonce = binascii.a2b_hex(raw_data[26:90])
           # Extraemos mac cli, eliminamos ":" y pasamos a hex
           macCli = binascii.a2b_hex(packet.addr1.replace(":", "").lower())
        # Si es el segundo mensaje del handshake
        elif count == 1:
           # Extraemos el snonce y lo pasamos a bin
           snonce = binascii.a2b_hex(raw_data[26:90])
           macAP = binascii.a2b_hex(packet.addr3.replace(":", "").lower())
           # Almacenamos el MIC
           captured_mic = raw_data[154:186] 
           #captured_mic = raw_data[192:208]  # Ajusta según la posición del MIC
           # Almacenamos en hexadecimal la capa de autenticación EAPOL
           Eapol2frame = raw_data
        count += 1

# Datos de AP convertidos a HEX legible:
macAP_hex = binascii.hexlify(macAP).decode('utf-8')
anonce_hex = binascii.hexlify(anonce).decode('utf-8')

# Datos de STA convertidos a HEX legible:
snonce_hex = binascii.hexlify(snonce).decode('utf-8')
macSTA_hex = binascii.hexlify(macCli).decode('utf-8')

# MIC a formato HEX legible:
captured_mic_hex = binascii.hexlify(binascii.a2b_hex(captured_mic)).decode('utf-8') if captured_mic else "No MIC found"

# Capa de autenticación EAPOL en HEX
Eapol2frame = Eapol2frame

print("Datos extraídos de AP:")
print()
print("MAC AP:", macAP_hex)
print("Anonce:", anonce_hex)
print()
print("Datos extraídos de STA:")
print()
print("MAC STA:", macSTA_hex)
print("SNonce (Hex):", snonce_hex)
print()
print("captured MIC:", captured_mic_hex)
print("Eapol2frame RAW Packet (Hex):", Eapol2frame)

if count == 0:
    print("No handshake found!")
    exit()


  
