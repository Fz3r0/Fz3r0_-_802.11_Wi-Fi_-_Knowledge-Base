@echo off

REM Banner

echo """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
echo "                                                                                          "
echo "         @@@@@@@@@@@@@@@@@@             ((_.-'-._| BlackShark v3.6 by Fz3r0 |_.-'-._))    "
echo "       @@@@@@@@@@@@@@@@@@@@@@@                                                            "
echo "     @@@@@@@@@@@@@@@@@@@@@@@@@@@        Networking & Cyber-Security PCAP Analysis Tool    "
echo "    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                         "
echo "   @@@@@@@@@@@@@@@/      \@@@/   @      [+] Cyber-Weapon:............. BlackShark         "
echo "  @@@@@@@@@@@@@@@@\      @@  @___@      [+] Version:.................. 3.6                "
echo "  @@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@    [+] Author:................... Fz3r0              "
echo "  @@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@    [+] Github:................... github.com/Fz3r0   "
echo "   @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\     [+] Twitter:.................. @Fz3r0_OPs         "
echo "     @@@@@@@@@@@@@|  | | | | | | | |    [+] Youtube:.................. @Fz3r0_OPs         "
echo "                 \_|_|_|_|_|_|_|_|                                                        "
echo "                                                                                          "
echo "                                                                                          "
echo """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

REM Execute BlackShark

echo           Bienvenido a BlackShark!!! Presiona cuaqluier tecla para continuar...
pause > nul
echo Ejecutando BlackShark, espere un momento...
echo.
start "" /D "C:\Program Files\Wireshark" "Wireshark.exe" -platform windows:darkmode=2
echo.
echo BlackShark ejecutado!!! 

REM Pausa para mostrar todos los mensajes en consola hasta salir

pause > nul
