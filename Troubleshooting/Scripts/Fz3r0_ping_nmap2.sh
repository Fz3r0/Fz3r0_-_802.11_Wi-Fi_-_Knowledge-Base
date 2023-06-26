#!/bin/bash

## Este calcula en rango entre 192.168.32.1 - 192.168.39.254 es dcir CIDR /21

# Función para verificar si una dirección IP responde al ping
ping_ip() {
    ip=$1
    ping -c 3 -q "$ip" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "$ip"
    fi
}

# Iterar sobre las direcciones IP y hacer ping
for i in {32..39}; do
    for j in {1..254}; do
        ip="192.168.$i.$j"
        ping_ip "$ip"
    done
done
