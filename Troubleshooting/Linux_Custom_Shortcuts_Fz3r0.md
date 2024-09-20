# Fz3r0 - D00MS DAY MACHINE CHEATSHEET

## Build de Entorno

- `Linux`
- `amd64`
- `parrot` .......................................... Distribución
- `bspwm` ........................................... Entorno de ventanas
- `sxhkd` ........................................... Para shortcuts de ventanas
- `kitty` ........................................... Shell
- `polybar` ......................................... Barra Superior de tareas
- `feh` ............................................. Imagenes y fondos de escritorio 
- `picom` ........................................... Compositor (Opacity, Corners & Shadows)
- `power level 10k` ................................. Prompt & Shell 
- `zsh` ............................................. Functions & Alias - ~/.p10k.zsh  
- `rofi` ............................................ Search Manager
- `ranger` .......................................... Buscador  

## update y upgrade

**Parrot**

- **Siempre como root y NUNCA usar apt upgrade!!**

    - `apt update`
    - `parrot-upgrade`

- **Database del sistema:**

    - `updatedb`

**Kali Linux**

- `sudo apt update && sudo apt full-upgrade -y`


---    

## Keyboard Shortcuts

### Window Manager (sxhkdrc)

- `super` + `1,2,3---9` ............................. Cambiar de WorkSpace

- `super` + `enter` ................................. Nueva consola

- `super` + `d` ..................................... Abrir `rofi` 

- `super` + `esc` ................................... Guardar cambios `zxkdrc`

- `super` + `shift` + `r` ........................... Guardar Entorno AKA `bspc wm -r`

- `super` + `q` ..................................... Salir de ventana

- `super` + `U-D-L-F` ............................... Mover entre ventanas

- `super` + `shift` + `U-D-L-R` ..................... Mover ventana de lado

- `super` + `shift` + `1,2,3---9` ................... Mover ventana de WorkSpace

- `super` + `s` ..................................... Ventana small 

- `super` + `t` ..................................... Ventana tile chida (o volver a setear un small)

- `super` + `f` ..................................... Ventana full horrenda

- `super` + `m` ..................................... Ventana semi-full horrenda

- `super` + `alt` + `U-D-L-R` ....................... Resize ventana RLZ

- `super` + `ctrl` + `U-D-L-R` ...................... mover ventana

- `super` + `click-R` ............................... Resize ventana

- `super` + `click-L` ............................... Mover ventana

---

### Pre-Selector (sxhkdrc)

- `super` + `ctrl` + `alt` + `U-D-L-R` .............. Pre-Selector amarillo

- `super` + `ctrl` + `1,2,3---9` .................... Selector amarillo mini

- `super` + `ctrl` + `alt` + `space` ................ Pre-Selector amarillo cancel nodo

- `super` + `ctrl` + `shift` + `space` .............. Pre-Selector amarillo cancel desktop

---

### Kitty Manager:

- `ctrl` + shift + enter = nueva ventana de kitty

- `ctrl` + shift + n     = nueva ventana AKA `super` + `enter`

- `ctrl` + shift + w = cerrar ventana

- `ctrl` + shift + l = seleccionar posiciones predefinidas

- `ctrl` + UDLF mover entre ventanas

- `ctrl` + shift + b = mueve ventana de lugar

- `ctrl` + shift + r = resize... WNTS-R para mover

---

### Tabs:

ctrl + shift + alt + t = cambiar nombre a tab actual

ctrl + shift + t = nueva tab

ctrl + shift + `U-D-L-R` = mover entre ventana (sirve con clicks)

ctrl + shift + , = "arrastra" la tab actual entre otras tabs izq

ctrl + shift + . = "arrastra" la tab actual entre otras tabs der


## Copiar y Pegar desde/hacia Windows

- Lanzar este comando o ponerlo en el `bspwmrc`:

    - `vmware-user-suid-wrapper` 

---

## Launcher (inicio)

- Usar el ejecutable:

    - `~/.config/polybar/scripts/launcher`

- O mi super-script: 

    - `fz3r0launcher`

---

## Operar como root siempre en kitty

1. Entrar como root `sudo su`
2. ejecutar la kitty a mano `/opt/kitty/bin/kitty`
3. Para que la nueva kitty no dependa de la otra consola:
    - **`/opt/kitty/bin/kitty &> /dev/null & disown`**

---    

## rofi 

- `Windows` + `d` .................. Sacar rofi AKA `rofi -show run`
- `rofi-theme-selector` ............ Seleccionar tema + (`alt` + `a`)


---

## polybar

`xdg-open Documents &>/dev/null & disown`



## Hacknerdfonts

- Terminus .................... Font utilizada

## Picom

https://www.youtube.com/watch?v=6LZtRUHbjLo

full:
https://github.com/ibhagwan/picom



## fz3r0target

- los scripts estan en /bin

- es una combinacion entr eel laucncher sh de polycom, o modulos creados

para setear target (primero ip y luego ID) `fz3r0target 1.1.1.1 google`

para setear lhost id `fz3r0lhost Fz3r0 💀`





## Copiar de forma recursiva

- `cp * -r ~/.config/polybar` <--- ejemplo de como copiar todo desde una carpeta hacia polybar. 

- `echo 'esto es un string' >> /home/fz3r0/document.txt` - copiar directo 

- Si necesitas poder copiar y pegar archivos o copy paste desde windows agrega esta linea en tu bspwmrc vmware-user-suid-wrapper



  





## Configurar `sxhkd/sxhkdrc`

- sudo nano `~/.config/sxhkd/sxhkdrc`





## Abrir programas particulares

- Firefox - - `Super` + `shift` + `f`    = Tip: Abrirlo en otro work space ;)  




- zoom = `ctrl` + `shift` + `+/-`



## Pasarse cosas entre máquinas

1. Montar un servidor python en la maquina a enviar y servirlo desde el folder
    - `sudo python3 -m http.server 8080`

2. Entrar a la otra máquina y descargarlo de la IP. 

## Comandos extras! :P

- Ver 7z que hay dentro = `7z l archivo.zip`
- `unzip archivo.zip` = descomprimit

---

## Colores Fz3r0

- Verde          - #0cf00c 
- Verde claro    - #afff00
- Agua verde     - #66ff9e
- Azul claro     - #2ab2ec
- Morado         - #7600fe 
- Morado oscuro  - #340060
- Morado claro   - #e1abff
- Rosa/Morado    - #c428cc
- Naranja        - #ef7f02 
- Rojo           - #e52c2c 
- Rojo obs       - #ab0c04
- Gris           - #797979  
- Gris obscuro   - #1c1c1c
- Negro          - #000000  
- Blanco         - #ffffff  

## Bordes de colores en kitty:

- bspc config normal_border_color "#44475a"
- bspc config active_border_color "#bd93f9"
- bspc config focused_border_color "#ff79c6"
- bspc config presel_feedback_color "#6272a4"

"Active means, the node is the focused one on an unfocused monitor"

polybar wiki
https://github.com/polybar/polybar/wiki/Configuration#application-settings

; Enables pseudo-transparency for the bar
; If set to true the bar can be transparent without a compositor.
pseudo-transparency = false

## power level 10k

- reconfigurar: `p10k configure`

## zshrc

- `~/.zshrc`

## neofetch

- `neofet0ch`

## Borrar historico de consola para auto-completoar

- `echo '' > ~/.zsh_history`

## bat (batcat)

- `ctrl + alt` para seleccionar solo las letras

- cat algo.py -l py
- hay un alias catn (catnormal) sutom

## Alias

- `nano ~/.zshrc`

## Instalar .deb files

- revisar que los riles sean amd64.deb

- `dpkg -i caca_0.22.1_amd64.deb`

## lsd

- Normal:
    - lsd
    - lsd -l

- Custom en Alias

    - alias cat='batcat'
    - alias ll='lsd -lh --group-dirs=first'
    - alias la='lsd -a --group-dirs=first'
    - alias l='lsd --group-dirs=first'
    - alias lla='lsd -lha --group-dirs=first'
    - alias ls='lsd --group-dirs=first'   

## fzf (buscador intrelifgente fuzzer)

- escribir primer el `cat` y despues `ctrl+t` para la bsuqueda smart
- escribes lo que quieras buscar por ejemplo `passwd` y con enter seleccionar

- buscar en hsitorico
    - `ctrl+r` y sale el historico de a papi

## ranger 

- solo se escribe `ranger` y se ve todo mas papita     
- tree o tree -L 2    (3,4,5etc)

## script para sacar ip

#!/bin/sh

echo "%{F#0cf00c} jeje %{F#0cf00c}"

ifconfig ens33 | grep "inet " | awk '{print $2}'

## htop

- htop
- gotop
- cmatrix
- ranger

## Themes

- lxappearance (para todo lo gtk)
- qt5ct (para todo lo qt)
- https://www.youtube.com/watch?v=B3m1mPymnno

- You can specify a theme manually in ~/.config/gtk-3.0/settings.ini like so:

[Settings]
gtk-theme-name = Adwaita
gtk-application-prefer-dark-theme = true


## WireShark negro

`sudo apt install adwaita-qt`

`wireshark -style Adwaita-Dark`



