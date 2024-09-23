# 4-Way-Handshake

- The 4-Way-Handshake is the process of exchanging 4 messages between an access point (authenticator) and the client device (supplicant) to generate some encryption keys which can be used to encrypt actual data sent over Wireless medium.
- Occurs after the client STA is authenticated and associated. _(this means, after the State 3 of the State Machine = State 3: Associated)_
- Is used to generate the keys used to encrypt various types of traffic (Unicast, Multicast, Broadcat) between **AP** and **client STA**.
- Utilizes an **exchange of 4 EAPOL Key Frames also known as "Messages"** between the client STA and the AP (`M1`, `M2`, `M3`, `M4`).
- In a PSK Network (eg. WPA2), the exchange of frames occurs after the open system authentication and association _(just after the State 3 of the State Machine)_
- In a 802.1X Network (eg. EAP/RADIUS), the 4-way-handshake occurs after EAP authentication _(after the State 3 of the State Machine + EAP Exchange between AP & Authentication Server)_
- Through the 4-way-handshake procedure, several keys are generated sequentially

## EAPoL

- EAPOL stands for "Extensible Authentication Protocol(EAP) over LAN".
- The IEEE 802.11i protocol uses EAPOL-Key packets during key negotiation.
- The EAPoL frame is silently discarded by the 802.11 Station/AP if the Key Sequence counter value in a particular EAPOL frame received was already sent in a previous EAPOL frame or the MIC received by either party is not properly decoded. **No indication of failure is reported to the sender of the EAPOL frame.**

### EAPol Frame Structure

![image](https://github.com/user-attachments/assets/ae07e111-185e-4627-a28c-c7cf3943abdf)

# Key Hierarchy

- Instead of using a single key for everything, 4-Way-Handshake uses a hierarchy with many keys to encrypt and check the integrity of different 802.11 frames.

## Key Derivation Function (KDF)

- A key derivation function (KDF) is an algorithm sed in cryptography that creates cryptographic keys from a secret value, such as a password or master key.
- KDFs can be used to stretch keys to make them longer or to create keys in a specific format. 
- The purpose of key derivation is to produce keys that are cryptographically strong and suitable for specific cryptographic applications, like encryption, authentication, or digital signatures.
- **In the 4-Way-Handshake procees there are different KDF algorythms and methods used for deriving the different keys.** 

![image](https://github.com/user-attachments/assets/7177caaf-e152-4dcd-b935-c7341ae76ad5)

## Pairwise Keys and Group Keys

- There are 2 different type of keys in the Key Hierarchy Pairwise Keys and Group Keys
- The Pairwise and group keys are created differently and used for different kind of traffic.

### Pairwise Keys _(Unicast)_

- **Unicast traffic** between a wireless client and the AP has to be private. <br><br>
    - Other client STAs should not to be able to decrypt traffic between another wireless client STAs and the AP.
    - This is why you should have different keys between each client STA and AP.
    - We call these pairwise keys because **there is a pair of keys between each wireless client and the AP.**
    - **The AP has multiple pairwise keys, one for each associated wireless client.**

### Group Keys _(Multicast/Broadcast)_

- **Broadcast and mMlticast traffic** between all wireless client and the AP together has to be private. <br><br>
    - All wireless clients should be able to encrypt and decrypt this traffic, so we need a **shared key**.
    - All associated wireless clients of the AP have the same key. We call this a group key. 

## 4-Way-Handshake: Keys & Components

- MSK (Master Session Key): The first level key is generated is MSK during the process of 802.1X/EAP or PSK authentication.
- PMK (Pairwise Master Key): 
- GMK (Group Master Key)
- PTK (Pairwise Transient Key)
- GTK (Group Temporal Key)
- ANonce
- SNonce
- MIC 1
- MIC 2





---

# 🗝️👑🪪 MSK (Master Session Key) [AAA/802.1X Key]

- The MSK is the first level key and is derived during the process of **802.1X-EAP (Enterprise) authentication**.
- The MSK **serves as the foundation for deriving the PMK (Pairwise Master Key)**, which is then used in subsequent 4-way handshake processes to derive encryption keys like the **PTK (Pairwise Transient Key)** and **GTK (Group Temporal Key)**.
- When you use 802.1X, the authentication server (typically RADIUS) derives the PMK and exports it to the wireless client and AP. This is done using RADIUS attribute MS-MPPE-Recv-key (vendor_id=17).
- EAP methods (such as EAP-TLS or PEAP) specify their own ways to derive the MSK.
- The MSK must be at least **64 octets in length (512 bits (64 bytes))**, as mandated by **IETF RFC 3748**

### 👑🏭 MSK: 802.1X (WPA/WPA2/WPA3-Enterprise):

- The MSK is generated as part of the EAP (Extensible Authentication Protocol) process during authentication between the client (supplicant) and the authentication server (typically RADIUS).
- After successful authentication, the authentication server (AS) provides the 64-byte MSK to both the client and the Access Point (AP).
- This MSK is then used to derive the Pairwise Master Key (PMK), which is 32 bytes (256 bits). The PMK is crucial for the 4-Way Handshake that follows.

### 👑🏠 MSK: PSK (WPA/WPA2-Personal):

- In PSK mode like WPA/WPA2, the MSK is not derived through an authentication protocol like EAP. Instead, the Pre-Shared Key (PSK), which is the Wi-Fi password, is used directly to create the Pairwise Master Key (PMK).
- This means, PSK authentication doesn't need the use of a MSK during the 4-Way-Handshake; The PMK is derived directly from the Pre-Shared Key (PSK) instead. 

## 👑🧮 MSK Derivation

- `802.1X-EAP`: From the EAP process during authentication between the client STA (supplicant) and the authentication server (typically RADIUS).

## 👑💡 MSK Summary

- MSK Size: 512 bits (64 bytes).
- Generation Method: 802.1X-EAP method (e.g., EAP-TLS, EAP-PEAP).
- Used For: Deriving the PMK, which then derives the PTK and GTK for encryption and secure data transmission.
- Created by Supplicant (STA) and the Authentication Server independently, they should match with each other.
- Not transmitted: the MSK is never transmitted directly over the network.

## 👑🟰 MSK to PMK Conversion Formula:

The PMK is derived from the MSK. The first 256 bits (32 bytes) of the MSK are used as the PMK.

- **`PMK = MSK[:32]`**  _(First 32 bytes of the MSK are the PMK)_

### 👑🔢 Example of MSK (from):

- `MSK Hexadecimal Format`: When displayed or logged, the MSK is typically shown in hexadecimal format
- Lenght: `64 bytes (512 bits)`. 

````sh
# MSK
1A 2B 3C 4D 5E 6F 7A 8B 9C AD BE CF D0 E1 F2 03
14 25 36 47 58 69 7A 8B 9C AD BE CF D1 E2 F3 04
15 26 37 48 59 6A 7B 8C 9D AE BF C0 D1 E2 F3 14
25 36 47 58 69 7A 8B 9C AD BE CF D1 E2 F3 04 15
````

- The `PMK (Pairwise Master Key)` is derived from the MSK (Master Session Key) by taking the first 256 bits (32 bytes) of the MSK:

````sh
# PMK derived from MSK (first 256 bits (32 bytes) of the MSK)
1A 2B 3C 4D 5E 6F 7A 8B 9C AD BE CF D0 E1 F2 03
14 25 36 47 58 69 7A 8B 9C AD BE CF D1 E2 F3 04
````

## 🐍 MSK 802.1X derivation simulation: Python

NOTE: This is NOT a real-life MSK derivation process!!!

- In real 802.1X/EAP, MSK is derived during the EAP authentication process, not through PBKDF2.
- _This example is for educational purposes to simulate key derivation._

````py
# MSK Key Derivation Simulator by Fz3r0

# NOTE: This is NOT a real-life MSK derivation process.
# In real 802.1X/EAP, MSK is derived during the EAP authentication process, not through PBKDF2.
# This example is for educational purposes to simulate key derivation.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# Constants:
SALT_SIZE = 16  # Size of the salt (in bytes) used in the key derivation process.
KEY_SIZE = 64   # Size of the MSK (in bytes). Typically, the MSK is 512 bits (64 bytes).
ITERATIONS = 100000  # Number of iterations used in the PBKDF2 process to make it more resistant to brute-force attacks.

# Simulated shared secret:
# In a real EAP method, the MSK would be generated as part of the EAP authentication process.
# Here, we're using a pre-defined password or shared secret as a stand-in.
shared_secret = b"simulated_eap_shared_secret"

# Generate a random salt:
# In reality, the MSK is not derived using a salt, but this demonstrates key generation mechanics.
salt = os.urandom(SALT_SIZE)

# Simulated MSK Derivation using PBKDF2-HMAC-SHA256:
# This step is purely for demonstration purposes and doesn't reflect actual 802.1X/EAP methods.
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),  # The hashing algorithm used (SHA256 in this case).
    length=KEY_SIZE,  # The length of the derived key (MSK) in bytes.
    salt=salt,  # The salt used for the key derivation.
    iterations=ITERATIONS,  # Number of iterations for PBKDF2.
    backend=default_backend()  # Cryptographic backend used to perform the key derivation.
)

# Derive the "MSK":
# This simulates the key derivation process, but in reality, the MSK is produced during EAP authentication.
msk = kdf.derive(shared_secret)

# Display the derived MSK in hexadecimal format:
# In real-world, the MSK is a 512-bit key shared between the client and authenticator.
print("Simulated MSK (Master Session Key):", msk.hex())

# Display the salt used in hexadecimal format:
# Not part of real MSK derivation, but here for educational purposes.
print("Salt used (for demo):", salt.hex())

````

# 🗝️🟰🤝 PMK (Pairwise Master Key)

- The pairwise master key (PMK) is a 256-bit key at the top of the key hierarchy and is used indirectly for unicast traffic and the WPA 4-way handshake (AP and client STA use the PMK to derive the PTK which is used for unicast data encryption).  
- The wireless client and AP have the PMK, which should last the entire session, so it should not be exposed. To accomplish this, we use different keys derived from the PMK.
- The PMK serves as the foundation for deriving further encryption keys, such as the PTK (Pairwise Transient Key) and GTK (Group Temporal Key).
- The PMK is never transmitted over the network; instead, it is independently derived and resides on all stations as in AP and client STAs, so this information is not shared through the network. 
- For secure communication, the PMK generated by both parties must match, ensuring successful authentication and enabling secure data transmission.
- Both parties (AP & STA), uses the same formula to derive the PMK (that's why the PMK must match)

### 🟰🏭 PMK: 802.1X (WPA/WPA2/WPA3-Enterprise):

- This PMK is derived from: `MSK (AAA/801.1X Key)`

### 🟰🏠 PMK: PSK (WPA/WPA2-Personal):

- This PMK is derived from: `PSK (Pre-Shared Key)`
- Pre-shared key is a key previously configured (for example a string/hexadecimal password).
- A Password-Based Key Derivation Function 2 (PBKDF2) is used to create a 256-bit PMK.



## 🟰💡 PMK Summary

- PMK Size: 256 bits (32 bytes).
- Derivation Method: PBKDF2 with HMAC-SHA1 (WPA2-Personal) // Derived from the MSK (802.1X-Enterprise) // SAE Handshake (WPA3-Personal).
- Created by Authenticator (AP) & Supplicant (STA) independently, they should match with each other.
- Not transmitted: the PMK is never transmitted directly over the network.

### 🟰🔢 Example of PMK:

- `PMK Hexadecimal Format`: When displayed or logged, the PMK is typically shown in hexadecimal format :: 32 bytes (256 bits):

````sh
# PMK
3A 5B 7C 9D AE BF C1 D2 E3 F4 65 76 87 98 A9 BA
CB DC ED FE 10 11 12 13 14 15 16 17 18 19 1A 34
````

## 🟰🧮 PMK Derivation

PMK derivation refers to the process of generating the PMK from a shared secret (like a pre-shared key) or from an authentication method (like EAP in 802.1X).

### ⭕ WPA2-Personal (PSK): 

The PMK is derived from a Pre-Shared Key (PSK), typically using a process like PBKDF2 with HMAC-SHA1 to transform the passphrase and SSID into a secure key.

### ⭕ WPA2-Enterprise (802.1X): 

The PMK is derived from the Master Session Key (MSK), which is generated during the EAP (Extensible Authentication Protocol) authentication process. The PMK in this case is the first 256 bits of the MSK.

### ⭕ WPA3-Personal: 

The PMK is derived from the SAE (Simultaneous Authentication of Equals) handshake, which is based on elliptic-curve cryptography and does not directly use the password.

## 🟰 PMK: `WPA2-Personal (PSK)`

- In WPA2-Personal, The PMK is derived using the PBKDF2 (Password-Based Key Derivation Function 2) algorithm, often with HMAC-SHA1.
- The function is applied multiple times (e.g., 4096 iterations) to make brute-force attacks more difficult.

### ⭕ PBKDF2 PMK Inputs:

- `Passphrase (WPA)`: User's WPA2 passphrase
- `Salt`: Network SSID.
- `Iterations`: 4096 rounds of HMAC-SHA1.
- `Output`: 256-bit PMK used for subsequent key derivations (like PTK and GTK) in the WPA2 authentication process.

### ⭕ PBKDF2 derivation formula

- **`PMK = PBKDF2(HMAC-SHA1, PSK, SSID(salt), rounds=4096, dklen=32)`**

### 🐍 PMK derivation using PBKDF2: `Python`

````py
# PMK Key Generator in Python by Fz3r0

import hashlib
import binascii

# Function to derive the PMK using PBKDF2 with HMAC-SHA1
def generate_pmk(password, ssid, iterations=4096, dklen=32):

    """
    Generates the PMK (Pairwise Master Key) using PBKDF2 with HMAC-SHA1.

    :param password:   Wi-Fi password (preshared key)
    :param ssid:       Wi-Fi network name (SSID)
    :param iterations: Number of iterations (default 4096)
    :param dklen:      Desired length of the derived key (32 bytes = 256 bits by default)
    :return:           PMK in hexadecimal format
    """

    # Ensure that the password and SSID are in byte format
    password_bytes = password.encode('utf-8')  # Converts password to bytes
    ssid_bytes = ssid.encode('utf-8')          # Converts SSID to bytes
    
    # Use PBKDF2 with HMAC-SHA1 to derive the key
    # 'sha1' is the hashing algorithm, password_bytes is the input key,
    # ssid_bytes is the salt, iterations is the number of rounds,
    # and dklen is the desired key length (32 bytes)
    pmk = hashlib.pbkdf2_hmac('sha1', password_bytes, ssid_bytes, iterations, dklen)
    
    # Convert the PMK to hexadecimal format for better readability
    return binascii.hexlify(pmk).decode().upper()

# Example usage
password = "password123"  # Wi-Fi password (pre-shared key)
ssid = "ExampleSSID"      # Wi-Fi network SSID

# Generate the PMK using the password and SSID
pmk = generate_pmk(password, ssid)

# Print the resulting PMK in hexadecimal format
print(f"PMK: {pmk}")

````

## PMK using 802.1X-EAP (Enterprise)

- In WPA2-Enterprise (802.1X), the PMK is derived from the MSK generated during the EAP process, so PBKDF2 is not used.

## PMK using WPA3

- One of the key differences between WPA2 and WPA3 is how the PMK (Pairwise Master Key) is derived, particularly in WPA3-Personal.
- In WPA2-Personal, the PMK is derived from a pre-shared key (PSK), while in WPA3-Personal, the PSK mechanism is replaced by SAE (Simultaneous Authentication of Equals).
- SAE is a password-based key exchange protocol that uses elliptic-curve cryptography (Dragonfly handshake) to derive the PMK, without transmitting or directly using the password.
- After the SAE handshake establishes the PMK, WPA3 still uses a 4-way handshake, much like WPA2, to derive other keys like the PTK (Pairwise Transient Key) and the GTK (Group Temporal Key).









# PTK

- The Pairwise Transient Key (PTK) is used for encryption and integrity checks in all unicast traffic between a client station and the access point. It is also used for protecting the 4-way handshake.
- PTK is unique between a client station and access point. 


## PTK Derivation Formula

- **`PTK = PRF (PMK + Anonce + SNonce + Mac (AA)+ Mac (SA))`**

The PTK is derived by combining these attributes using a **PRF (pseudo-random function)**:

- PMK
- AP Nonce (Anonce)
- STA Nonce (Snonce)
- AP MAC address
- STA MAC address

### PRF (pseudo-random function)

- PRF is a pseudo-random function which is applied to all the input.
- PRF-n - Pseudo-random function producing n bits of output, there are the 128, 192, 256, 384 and 512 versions, each of these output these number of bits.
- The pairwise key hierarchy utilizes PRF-384 or PRF-512 to derive session-specific keys from a PMK, generating a PTK, which gets partitioned into a KCK and a KEK plus all the temporal keys used by the MAC to protect unicast communication.
- The GTK shall be a random number which also gets generated by using PRF-n, usually PRF-128 or PRF-256, in this model, the group key hierarchy takes a GMK (Group Master Key) and generates a GTK.

## 🟰💡 PMK Summary

- PMK Size: TKIP = 512 bits (64 bytes)  //  AES/CCMP = 384 bits (48 bytes).
- Derivation Method: PBKDF2 with HMAC-SHA1 (WPA2-Personal) // Derived from the MSK (802.1X-Enterprise) // SAE Handshake (WPA3-Personal).
- Created by Authenticator (AP) & Supplicant (STA) independently, they should match with each other.
- Not transmitted: the PMK is never transmitted directly over the network.

## Anonce & Snonce

- These nonces are random 256-bit (32-byte) values generated during the 4-way handshake process to provide freshness and prevent replay attacks. 
- The ANonce (Authenticator Nonce) is a `256-bit (32-byte)` random value generated by the **Access Point (AP)** during the 4-way handshake process.
- The SNonce (Supplicant Nonce) is a `256-bit (32 bytes)` random value generated by the Supplicant (client STA) during the 4-Way Handshake process.
- They are unique per session and are essential for deriving the session keys securely.
- They play a critical role in the derivation of the **Pairwise Transient Key (PTK)**.
- They allow to both the AP (Authenticator) and the STA (Supplicant) to **independently calculate the same PTK.**

## AP & STA MAC Address

- This information is included in every 802.11 frame MAC Header Information usin at least the first 3 WLAN Addresses.
- This means, the client AP and the STA know the WLAN Address of each other even before the 4-Way-Handshake process. 

Example:

````py
# client STA MAC (WLAN Address)

# AP MAC (WLAN Address)
````

### Anonce example

```` sh
# ANonce (Access Point Nonce) - String Format:
A7F1E5C4A36D5E7B8A94C1C1D3E7B1A8CBBF7456E3191D2F8E9A5B3C4D6E7F8B

# ANonce (Access Point Nonce) - Block Format:
A7 F1 E5 C4 A3 6D 5E 7B 8A 94 C1 C1 D3 E7 B1 A8
CB BF 74 56 E3 19 1D 2F 8E 9A 5B 3C 4D 6E 7F 8B
````
### Snonce example

````sh
# SNonce (Supplicant Nonce) - String Format:
94D2E7F1A8C4A7B6F319C1CBB5A8E9F3D7C6E9B1A45E3D6A8F1E3B9C4D7A5C1D

# SNonce (Supplicant Nonce) - Block Format:
94 D2 E7 F1 A8 C4 A7 B6 F3 19 C1 CB B5 A8 E9 F3
D7 C6 E9 B1 A4 5E 3D 6A 8F 1E 3B 9C 4D 7A 5C 1D
````

### Anonce & Snonce generator: Python

````py
# Anonce & Snonce Generator in Python by Fz3r0

import os
import binascii

# Generate ANonce (Access Point Nonce)
def generate_anonce():
    # Generate 32 random bytes (256 bits)
    anonce = os.urandom(32)
    return anonce

# Generate SNonce (Supplicant Nonce)
def generate_snonce():
    # Generate 32 random bytes (256 bits)
    snonce = os.urandom(32)
    return snonce

# Convert the generated nonces to a continuous string (hexadecimal format)
def format_nonce_as_string(nonce):
    return binascii.hexlify(nonce).upper().decode('utf-8')

# Convert the generated nonces to formatted hexadecimal blocks with 16 bytes per line
def format_nonce_as_block(nonce):
    hex_string = binascii.hexlify(nonce).upper().decode('utf-8')
    # Break the hex string into chunks of two characters (bytes)
    byte_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    # Group into 16 byte pairs per line
    formatted_block = '\n'.join([' '.join(byte_pairs[i:i+16]) for i in range(0, len(byte_pairs), 16)])
    return formatted_block

# Generate and display ANonce and SNonce in both formats
anonce = generate_anonce()
snonce = generate_snonce()

print("ANonce (Access Point Nonce) - String Format:")
print(format_nonce_as_string(anonce))

print("\nANonce (Access Point Nonce) - Block Format:")
print(format_nonce_as_block(anonce))

print("\nSNonce (Supplicant Nonce) - String Format:")
print(format_nonce_as_string(snonce))

print("\nSNonce (Supplicant Nonce) - Block Format:")
print(format_nonce_as_block(snonce))

````


## Message 1 (M1)

- Source: AP
- Destination: client STA
- Includes: `Anonce (Authenticator/AP Nonce)`

### AP Operations Before M1

1. **`PMK Derivation`**: This happens before the 4-Way-Handshake depending on authentication method:

    - WPA2-PSK:
    - WPA3-PSK: 
    - 802.1X-EAP: 

### AP Sends M1

- AP sends EAPOL Message 1 with: Anonce (random number); Anonce will be used by the client sTA to generate PTK.
- This message is unencrypted and has no integrity check.
- If someone messes with this message _(e.g. frame tampering)_, the handshake will fail and that's it.

## Message 2 (M2)

- Source: client STA
- Destination: AP
- Includes: `MIC`, `Snonce (Supplicant/STA Nonce)`

### STA Operations Before M2

1. **`PMK Derivation`**: This happens before the 4-Way-Handshake depending on authentication method:

    - WPA2-PSK:
    - WPA3-PSK:
    - 802.1X-EAP:

2. **`PTK Derivation`**: Remember, client STA "knows" APs MAC Address since the State Machine 1-3 Process, then: 

    - Client STA has `PMK` + `Snonce` + `STA MAC Address` + `AP MAC Address`... Once it receives `Anonce` from AP, **it has all the inputs to create the `PTK`**.
    - Client creates the **`PTK`** using a **PRF (pseudo-random function)** :: **`PTK = PRF (PMK + Anonce + SNonce + Mac (AA)+ Mac (SA))`**

3. `MIC Generation`: STA uses the **KCK** to generate the MIC.

   - AP Compares the MIC when the M2 is received to verify whether this message corrupted or modified 

### STA Sends M2

- STA sends EAPOL Message 2 (M2) to AP with `MIC (Message Integrity Check)` value to make sure when the AP can verify whether this message corrupted or modified.
    - The Key Confirmation Key (KCK) is used to calculate the MIC. <br><br>
- STA sends also the `SNonce` in the M2, which is needed by the AP to generate PTK as well.
    - Snonce will be used by the AP to generate PTK.


## Message 3 (M2)

### AP Operations Before M3

1. **`PTK Derivation`**: Remember, AP "knows" STAs MAC Address since the State Machine 1-3 Process, then:  <br><br>

    - AP has `PMK` + `Anonce` + `STA MAC Address` + `AP MAC Address`... Once it receives `Snonce` from client STA, **it has all the inputs to create the `PTK`**. 
    - Client creates the **`PTK`** using a **PRF (pseudo-random function)** :: **`PTK = PRF (PMK + Anonce + SNonce + Mac (AA)+ Mac (SA))`**

2. `MIC generation/validation`: AP uses the KCK to generate the MIC.

   - AP Compares received MIC with calculated MIC to verify whether this message corrupted or modified. <br><br>
       - 🔓 **If the MIC is the same, this proves that the client and AP both have the same PMK.**


### STA Sends M3

- STA sends EAPOL Message 3 (M3) to AP with `MIC (Message Integrity Check)` value to make sure when the AP can verify whether this message corrupted or modified.
    - The Key Con








- https://telcomatraining.com/what-is-msk-master-session-key-2/
- https://networklessons.com/cisco/ccnp-encor-350-401/wpa-and-wpa2-4-way-handshake
- https://networklessons.com/cisco/ccnp-encor-350-401/introduction-to-wpa-key-hierarchy
- https://www.wifi-professionals.com/2019/01/4-way-handshake
- https://mrncciew.com/2014/08/19/cwsp-4-way-handshake/
- https://www.youtube.com/watch?app=desktop&v=wrbNNri-E1E
- https://networklessons.com/cisco/ccnp-encor-350-401/eapol-extensible-authentication-protocol-over-lan
- https://support.accessagility.com/hc/wifi-glossary-master-session-key-msk
- https://en.wikipedia.org/wiki/PBKDF2
- https://github.com/k1nd0ne/ScapyWifi/blob/master/ScapyFi.py
- https://www.hitchhikersguidetolearning.com/2017/09/17/eapol-4-way-handshake/
- https://waitbutwifi.com/deconstructing-the-4-way-handshake/
- https://support.hpe.com/techhub/eginfolib/networking/docs/routers/msrv7/cg/5200-3028_wlan_cg/content/466576914.htm
- https://en.wikipedia.org/wiki/IEEE_802.11i-2004



