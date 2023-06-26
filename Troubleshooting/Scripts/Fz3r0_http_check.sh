#!/bin/bash

# Función para verificar si una dirección IP responde a través de HTTP

# perfecto para encontrar equipos!!!

check_http_response() {
    ip=$1
    response=$(curl -s -I "http://$ip" -o /dev/null -w "%{http_code}")
    if [ "$response" = "200" ]; then
        echo "La dirección $ip respondió correctamente a través de HTTP"
    fi
}

# Rango de direcciones IP
ranges=("192.168.33" "192.168.34" "192.168.35")

# Iterar sobre los rangos de direcciones IP y comprobar la respuesta HTTP
for range in "${ranges[@]}"; do
    for i in {1..254}; do
        ip="$range.$i"
        check_http_response "$ip"
    done
done
