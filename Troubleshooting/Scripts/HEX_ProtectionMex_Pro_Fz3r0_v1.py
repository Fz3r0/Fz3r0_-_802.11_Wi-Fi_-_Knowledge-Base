import os
from colorama import Fore, Style, init

def flags_to_binary(flags_str):
    # Separa las líneas, ignora las vacías y procesa desde abajo hacia arriba
    lines = [line.strip() for line in flags_str.strip().splitlines() if line.strip()]
    
    # Procesa cada línea desde abajo hacia arriba, quita los puntos y toma solo los bits
    binary_str = ''.join(['1' if char == '1' else '0' for line in reversed(lines) for char in line if char in ['0', '1']])
    
    # Asegura que el resultado binario no exceda los 16 bits
    return binary_str[:16]

def binary_to_hex(binary_str):
    # Convertir la cadena binaria a un entero y luego a hexadecimal
    return hex(int(binary_str, 2))[2:].zfill(4)  # Asegura que siempre tenga 4 caracteres en hex

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    # Inicializa colorama
    init(autoreset=True)
    
    # Título del programa
    print()
    print(f"{Fore.CYAN}{Style.BRIGHT}#############################################################################################")
    print(f"{Fore.CYAN}{Style.BRIGHT}#                                                                                           #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#          {r'@@@@@@@@@@@@@@@@@@'}               ((_.-'-._| HT Protection to HEX |_.-'-._))      #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#        {r'@@@@@@@@@@@@@@@@@@@@@@@'}                                                            #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#      {r'@@@@@@@@@@@@@@@@@@@@@@@@@@@'}              Convert Blackshark binary into HEX          #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#     {r'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'}                                                         #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#    {r'@@@@@@@@@@@@@@@/      \@@@/   @'}      [+] Cyber-Weapon:............. HT Prot to HEX     #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#   {r'@@@@@@@@@@@@@@@@\      @@  @___@'}      [+] Version:.................. 1.0                #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#   {r'@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@'}    [+] Author:................... Fz3r0              #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#   {r'@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@'}    [+] Github:................... github.com/Fz3r0   #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#    {r'@@@@@@@@@@@@@@@/,/,/./´/_|.\`\,\ '}    [+] Twitter:.................. @Fz3r0_OPs         #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#      {r'@@@@@@@@@@@@@|  | | | | | | | | '}   [+] Youtube:.................. @Fz3r0_OPs         #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#                  {r'\_|_|_|_|_|_|_|_| '}                                                       #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#                                                                                           #")
    print(f"{Fore.CYAN}{Style.BRIGHT}#############################################################################################")

    # Valor de ntp en formato flags (puedes modificarlo aquí)
    ntp = '''
.... .... .... ..11
.... .... .... .1..
.... .... .... 0...
.... .... ...1 ....
...0 0000 000. ....
000. .... .... ....
    '''
    
    # Convertir flags a string binario (desde la última línea hacia la primera)
    binary_string = flags_to_binary(ntp)

    # Verifica si el binary_string está vacío
    if not binary_string:
        print(f"{Fore.RED}{Style.BRIGHT}Error: No se pudieron convertir las flags a una cadena binaria.")
        return

    # Convertir a hexadecimal
    hex_value = binary_to_hex(binary_string)

    # Imprimir resultados con colores
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}Bitmask (HT Information Flags):")
    print()
    print(ntp.strip())  # Se imprime con un solo salto de línea limpio
    print()
    print(f"{Fore.CYAN}{Style.BRIGHT}#############################################################################################")
    
    print(f"{Fore.BLUE}{Style.BRIGHT}\nBitmask to binary string:\n")
    print(' '.join(binary_string[i:i+4] for i in range(0, len(binary_string), 4)))  # Agrupamos en bloques de 4
    print()
    print(f"{Fore.CYAN}{Style.BRIGHT}#############################################################################################")
    
    print(f"{Fore.MAGENTA}{Style.BRIGHT}\nBinary string to HEX:\n")
    print(hex_value)  # Imprime el valor hexadecimal
    print()
    print(f"{Fore.CYAN}{Style.BRIGHT}#############################################################################################")

    print(f"{Fore.RED}{Style.BRIGHT}\nFinal HEX Result:\n")
    print(f"0x{hex_value}")  # Imprime el resultado en formato hexadecimal
    print()

if __name__ == "__main__":
    main()





