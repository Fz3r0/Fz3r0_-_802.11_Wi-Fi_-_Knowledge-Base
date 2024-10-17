import re

def limpiar_binario(texto):
    # Separar las líneas del texto
    lineas = texto.strip().splitlines()

    # Lista para almacenar las líneas limpias
    binarios_limpios = []

    # Expresión regular para detectar cualquier secuencia binaria
    patron_binario = re.compile(r'([\.01 ]+)')

    for linea in lineas:
        # Buscar el patrón binario en cada línea
        match = patron_binario.match(linea.strip())
        if match:
            # Si se encuentra, se agrega la parte del binario limpio a la lista
            binarios_limpios.append(match.group(0).strip())

    # Unir las líneas limpias en un solo string
    return "\n".join(binarios_limpios)

# Ejemplo de uso
texto = """
                .... .... .... ..10 = HT Protection: 20 MHz protection mode (0x2)
                .... .... .... .1.. = Non-greenfield STAs present: One or more associated STAs are not greenfield capable
                .... .... .... 0... = Reserved: 0x0
                .... .... ...0 .... = OBSS non-HT STAs present: Use of protection for non-HT STAs by overlapping BSSs is not needed
                ...0 0000 000. .... = Channel Center Frequency Segment 2: 0
                000. .... .... .... = Reserved: 0x0
"""

# Ejemplo de resultado

# python hex_cleaner_protection_mechs.py
# .... .... .... ..10
# .... .... .... .1..
# .... .... .... 0...
# .... .... ...0 ....
# ...0 0000 000. ....
# 000. .... .... ....

# Procesar el texto
resultado_limpio = limpiar_binario(texto)
print(resultado_limpio)
