# Este script imprime una gráfica pie con el porcentaje de tipos de Frame 802.11 en un PCAP

import subprocess
import matplotlib.pyplot as plt

# Ejecutar el comando tshark y capturar la salida
tshark_command = "tshark -r /home/fz3r0/Documents/averg.pcap -T fields -e wlan.fc.type_subtype"
output = subprocess.check_output(tshark_command, shell=True).decode()

# Contar los valores de cada tipo de frame
counters = {
    "Data": 0,
    "Management": 0,
    "Control": 0
}

for line in output.splitlines():
    if "80" in line or "08" in line:
        counters["Data"] += 1
    elif "40" in line or "44" in line or "48" in line or "4c" in line or "50" in line or "54" in line or "58" in line or "5c" in line or "a0" in line or "a4" in line or "a8" in line or "ac" in line or "b0" in line or "b4" in line or "b8" in line or "bc" in line:
        counters["Control"] += 1
    elif "00" in line or "10" in line or "20" in line or "30" in line:
        counters["Management"] += 1

# Crear el gráfico de pastel
labels = counters.keys()
sizes = counters.values()
colors = ["green", "yellow", "red"]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title("Tipo de frames WLAN")
plt.show()
