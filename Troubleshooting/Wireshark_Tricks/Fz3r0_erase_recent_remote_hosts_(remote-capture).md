1. Go to: `C:\Users\Fz3r0\AppData\Roaming\Wireshark`
2. Open with text editor the file: `recent comon`
3. Find the secction `######## Recent remote hosts, cannot be altered through command line ########` and erase that section, example:

````py
######## Recent remote hosts, cannot be altered through command line ########

recent.remote_host: 172.24.1.183,,0
recent.remote_host: 172.24.4.90,,0
recent.remote_host: 172.24.7.38,,0
````

After erasing that block, open wireshark and old cached remote interfaces should be removed
