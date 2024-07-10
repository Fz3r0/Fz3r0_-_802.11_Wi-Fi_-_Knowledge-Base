
# How to remove recent remote interfaces in Wireshark

## Option 1: Erasing Remote Interfaces Block

**WIRESHARK MUST BE CLOSED BEFORE ANY STEP**

1. Go to: `C:\Users\%USERNAME%\AppData\Roaming\Wireshark`
2. Open with text editor the file: `recent comon`
3. Find the secction `######## Recent remote hosts, cannot be altered through command line ########` and erase that section, example:

````py
######## Recent remote hosts, cannot be altered through command line ########

recent.remote_host: 172.24.1.183,,0
recent.remote_host: 172.24.4.90,,0
recent.remote_host: 172.24.7.38,,0
````

After erasing that block, open wireshark and old cached remote interfaces should be removed

## Option 2: Erasing the "recent comon" file

_This will also erase all the recent settings like recent filters, or recent profiles used (dows not erase the profiles dont' worry)_

**WIRESHARK MUST BE CLOSED BEFORE ANY STEP**

1. Go to: `C:\Users\%USERNAME%\AppData\Roaming\Wireshark`
2. Erase the the file: `recent comon`

After erasing THE FILE, open wireshark and old cached remote interfaces and recent data should be removed
