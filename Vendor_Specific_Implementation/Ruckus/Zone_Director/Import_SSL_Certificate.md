Complete SSL Certificate Import Guide by an Idiot
it_registration
 it_registration
Contributor
‎11-04-2015 09:31 PM

I struggled for hours trying to figure out SSL certificates, I still don't understand them.  But below is a process I used to get certificates onto my Smart Redundant ZD's.

I'm not an expert use the information at your own risk.  Backup your configuration before you begin and also backup your Certificate settings/private keys (found under configure>certificate>advanced) before you begin.

The steps below were performed on Ruckus Zonedirector ZD1200 SR pair and the cert is working as expected.

This documentation has taken place about 5 hours after the actual work so please excuse any errors.  And I am by no means an expert in this stuff.  I had to fumble my way through it cause I'm extremely ignorant when it comes to Certificates, but I got it to work so I thought I'd share.  But again please back up everything before you begin.

Why would you want to do this?  I did this so my users when accessing the ZD for authentication were not "warned" that this site may not be safe.

A bit of information first:
The Zonedirector by default selects 1024 bit private key length.  If you look under advanced like I did, AFTER I figured out another way to do it, I could have selected 2048 bit private key.  The problem is that GoDaddy SSL creation (which is who I bought my Cert from) requires a 2048 bit key, as I think most CA's do now days.

I'm going to do this as a step by step process.

1. Buy your cert.  SSL UCC certs can be bought in 1, 5, 10, or more and for any # of years. But anyway I bought a 5 sites, Standard SSL cert from Go Daddy.

2. Generate your CSR (Cert signing request).  If I were to do this again I would try to use the ZD's built in CSR generator after having selected 2048 key length in the "Advanced" section under "Configure>Certificate".
a.  I used a tool called DigiCertUtil I found online and downloaded to create the CSR
 Download and run the tool and select "Create CSR" near the top right.
Filling out the form:
a.1. Common Name is the FQDN that you want for the cert.  ie.  wifi.xxxxxx.xxx
a.2. You do NOT need to add SAN (Subject Alternative Names).  Fill these in only needed if you want to add additional fully qualified domain name "servers", if you bought a multi site UCC cert..  ie. server2.xxxxxxx.xxx  If you do add SAN's later you can do it through Go Daddy's web site, but a new cert will be generated and you'll need to replace all the certs you have installed in your environment/servers.

3. Copy and paste the CSR txt into Go Daddy's SSL Certificate generator tool.

4.  GoDaddy then goes through a bunch of processes and makes sure your valid to create the cert.

5. Once the cert is created (5 - 30 mins) you can download it.  For Ruckus I download as Apache server.

6. If you generated the CSR on the ZoneDirector you maybe able to import directly onto the ZD at this point.
If you generated the CSR with the DigiCert Utility then follow these steps:
Once downloaded I use "DigiCert Utility" again and click "SSL" on the left and "Import".  I browse out to the downloaded cert and select the file to import.  If 
you select the wrong file it will tell you its not valid.

7.  Once the cert is imported at the bottom right you can perform a few functions.  We are going to, for the Ruckus cert, "Export Certificate".

8.  Once the "Certificate Export" dialog box opens I select "yes, export the private key" & "key file (Apache compatible format)".  By selecting Apache compatible format you'll get the PME file that you need for the Ruckus Zonedirector certificate import.
a. The export generates three files, as I understand it (I could be wrong) here's what they are/do:
a.1. The PME file: xxxfilenamexxx.crt
a.2. The private key file: xxfilenamexxx.key
a.3. The intermediate cert: CACert.crt
b.  All three of these files are usable during the import of the cert to Ruckus Zonedirector

9. Open up the web interface on the Zonedirector and navigate to "Configure>Certificate"
a. **NOTE** installing the certificate will cause the ZD to reboot.
b.  **NOTE** during installation you will be warned that the private key on the cert is different than the one on the ZD.  You can continue.  I honestly   don't know what consequences this may have, but I've not yet run into an issue.  I assume that if you were to generate the CSR on the ZD selecting 2048 key length you wouldn't experience this warning.

10. Under "Import Signed Certificate" select "Choose File" and browse out to the location of your exported PME files in step 8. above. (do not reboot)

11. Before rebooting you should be prompted if you want to upload the private key, do that, refer to step 8; (do not reboot)

12. You should again be prompted if you want to upload the CA, select yes and upload the CACert cert. in step 8.

13.  That should be the final step.... reboot.

14.  If you are running in Smart Redundancy on the ZD's, upon reboot it will fail over to the secondary ZD.  You should wait for the primary to completely reboot and then log back into it and navigate to "Configure>Certificate>Advanced" and select "Back Up Certificates for Smart Redundancy".  Save those to a new location on your hard drive so you don't get them mixed up with the other files you've been working with.  I named my folder ZD SR Cert.

15.  Log back into the secondary ZD, and navigate to "Configure>Certificate" select "Import Signed Certificate".

16.  Sit back watch the secondary unit reboot.

17.  One obvious last step if you used DNS as a SAN or FQDN, don't forget to add the DNS record to your internal DNS server.

18. Done.
