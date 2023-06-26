#!/bin/bash

# Función para verificar si una dirección IP responde a través de HTTP o HTTPS
check_http_response() {
    ip=$1
    http_response=$(curl -s -I "http://$ip" -o /dev/null -w "%{http_code}")
    https_response=$(curl -s -I "https://$ip" -o /dev/null -w "%{http_code}")
    
    if [ "$http_response" = "200" ] || [ "$https_response" = "200" ]; then
        echo "La dirección $ip respondió correctamente a través de HTTP o HTTPS"
    fi
}

# Iterar sobre las direcciones IP y comprobar la respuesta HTTP o HTTPS
for i in {192..192}; do
    for j in {168..168}; do
        for k in {34..34}; do
            for l in {1..5}; do
                ip="$i.$j.$k.$l"
                check_http_response "$ip"
            done
        done
    done
done
