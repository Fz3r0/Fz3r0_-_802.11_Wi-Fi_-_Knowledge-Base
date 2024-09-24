# Catpures



## WPA 2 Auth

2.4 WPA2-PSK

![image](https://github.com/user-attachments/assets/85c52560-bda4-42d7-b61d-21904fc4c400)



````py
# Activando Monitor Mode en un adaptador Fresh (wlan0) 
clear; airmon-ng start wlan0; iwconfig wlan0mon channel 11 && ifconfig wlan0mon down; macchanger --mac=f0:f0:f0:f0:f0:f0 wlan0mon; ifconfig wlan0mon up && clear; echo -e "\033[31m[+] Fz3r0 💀 Wireless IEEE 802.11 (WiFi) Adapter Validator v1.0\033[0m"; echo -e "\033[31m[+] Twitter: @Fz3r0_OPs | Github: Fz3r0\033[0m"; echo ""; echo -e "\033[97m--- SYSTEM:\033[0m"; echo ""; echo -e "\033[32m$(uname -a)\033[0m"; echo ""; echo -e "\033[97m--- USB ADAPTERS & DRIVERS:\033[0m"; echo ""; if iwconfig 2>/dev/null | grep -q 'Mode:Monitor'; then printf "\033[32mWLAN Interface Status:%25s\nMonitor Mode:%33s\033[0m" "Present" "Active"; elif iwconfig 2>/dev/null | grep -q 'no wireless'; then echo -e "\033[31mWLAN Interface Status:%25s\n%s\033[0m" "Not Present" "No WLAN interface detected"; else echo -e "\033[31mWLAN Interface Status:%20s\nMonitor Mode:%33s\033[0m" "Present" "Inactive"; fi && echo "" ; echo -e "\033[32m$(airmon-ng)\033[0m"; echo ""; echo -e "\033[97m--- PHYSICAL INTERFACES:\033[0m"; echo ""; echo -e "\033[36m$(ifconfig)\033[0m"; echo ""; echo -e "\033[97m--- WIRELESS ADAPTERS & MODE:\033[0m"; echo ""; iwconfig 2>/dev/null | grep -vE 'eth|lo' | grep -v 'no wireless extensions'; iw dev
````

![image](https://github.com/user-attachments/assets/24d83074-d8de-4040-a659-b345111a65f9)




![image](https://github.com/user-attachments/assets/71ebbd84-ae55-41db-9086-f5110af1033e)
