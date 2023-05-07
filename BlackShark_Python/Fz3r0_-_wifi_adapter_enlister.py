#!/usr/bin/python3

#
# Fz3r0 WiFi Adapters Enlister & One-Liner
#

    # - Estre script enlista y lo guarda en variable todos los adaptadores 802.11 WiFi del sistema

    # - También genera un one-liner separado con comas sin espacios

    # - La finalidad es tener 2 diferentes tipo de variables (lista y one-liner) para usarlo con diferentes objetivos:

    # - Los objetivos particulares pueden ser la necesidad de ejecutar comandos linux o enlistar detalles que necesitan los nombres exactos de los adaptadores. 

import subprocess

#
# Def: ind_wifi_adapters
#

def find_wifi_adapters(cmd="iwconfig"):
    """
    Encuentra los adaptadores WiFi conectados utilizando el comando especificado.
    Retorna una lista con los nombres de los adaptadores WiFi encontrados.
    """
    # Ejecutar el comando y redirigir la salida a la entrada estándar y de error
    # subprocess es una biblioteca para ejecutar comandos en la terminal
    # Popen es una función para abrir un proceso que ejecutará un comando en una nueva terminal
    # stdout y stderr son parámetros que definen los flujos de entrada y salida del proceso
    # PIPE es una constante que define que el proceso no tiene salida o entrada de datos
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capturar la salida y la salida de error del comando
    # communicate es una función que espera a que el proceso termine y devuelve la salida y error
    output, error = proc.communicate()

    # Decodificar la salida a una cadena y dividirla en líneas
    # decode convierte bytes a una cadena
    # split divide la cadena en una lista de subcadenas, utilizando un separador
    output = output.decode().split("\n")

    # Buscar los nombres de los adaptadores WiFi
    # for es un bucle que recorre los elementos de una lista
    # append agrega elementos a una lista
    wifi_ifaces = []
    for line in output:
        if "IEEE 802.11" in line or "WIFI" in line:
            wifi_ifaces.append(line.split()[0])

    # Retornar los nombres de los adaptadores WiFi encontrados
    return wifi_ifaces

######################################################################################################

#
# Program: find_wifi_adapters
#

# Llamar a la función y asignar el resultado a una variable
wifi_ifaces = find_wifi_adapters()

# Imprimir los nombres de los adaptadores WiFi encontrados
if wifi_ifaces:
    print("\nAdaptadores WiFi encontrados:\n")
    for i, iface in enumerate(wifi_ifaces):
        # f-string es una forma de concatenar cadenas y variables
        print(f"Adaptador {i+1}: {iface}")
    # join convierte una lista en una cadena, separando los elementos por un separador
    iface_string = ",".join(wifi_ifaces)
    print(f"\nOne-Liner string: {iface_string}")
else:
    print("No se encontraron adaptadores WiFi.")
