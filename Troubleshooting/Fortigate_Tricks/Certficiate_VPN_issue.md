

# Troubleshooting Tip: FortiClient TLS 'error 5029': failed to establish the VPN connection

### Description

This article describes how to rectify the **`failed to establish the VPN connection, 5029 error`.

- While connecting the FortiClient, the following error may appear.

![image](https://github.com/Fz3r0/Fz3r0_-_802.11_Wi-Fi_-_Knowledge-Base/assets/94720207/348a09b5-e42d-4137-8a94-92c7af79c4ff)

## Solution

- Execute the following line in CMD as admin:

````bat
RunDll32.exe InetCpl.cpl,ResetIEtoDefaults
````
