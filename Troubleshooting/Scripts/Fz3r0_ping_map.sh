#!/bin/bash

## Es como un nmap pero de puro ping, para buscar equipos en una red administrativa. 

## En este caso va del 192.168.34.1 al 192.168.34.254

# Función para verificar si una dirección IP responde al ping
ping_ip() {
    ip=$1
    ping -c 3 -q "$ip" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "$ip"
    fi
}

# Iterar sobre las direcciones IP y hacer ping
for i in {1..254}; do
    ip="192.168.34.$i"
    ping_ip "$ip"
done
