function Create-WiresharkFilter {
    Clear-Host

    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Cyan
    Write-Host "|          Filter Generator Wi-Fi 802.11 || AP <--> STA         |" -ForegroundColor Cyan
    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Cyan 
    Write-Host "|                                                               |" -ForegroundColor Cyan   
    Write-Host "|                       Twitter: Fz3r0_OPs                      |" -ForegroundColor Cyan
    Write-Host "|                       Github:  Fz3r0                          |" -ForegroundColor Cyan
    Write-Host "|                       Youtube: Fz3r0_OPs                      |" -ForegroundColor Cyan
    Write-Host "|                                                               |" -ForegroundColor Cyan
    Write-Host "|              ''And now... Let me read your mind...''          |" -ForegroundColor Cyan
    Write-Host "|                                                               |" -ForegroundColor Cyan   
    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Yellow
    Write-Host "[                         Instructions                          ]" -ForegroundColor Yellow
    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "[1] Add the MAC of the target STA." -ForegroundColor White
    Write-Host "    (Client, Smartphone, Tablet, PC, Wi-Fi device)" -ForegroundColor White
    Write-Host ""
    Write-Host "[2] Add the MAC of the target AP." -ForegroundColor White
    Write-Host "    (Access Point, Home Router, Hotspot, Wi-Fi Antenna)" -ForegroundColor White
    Write-Host ""
    Write-Host "[3] Add the MAC of the APs/STAs you want to remove from the filter." -ForegroundColor White
    Write-Host "    (Rogue APs, Neighbor APs, Interference, STAs...)" -ForegroundColor White
    Write-Host ""
    Write-Host "       -- PRESS ENTER if there are no MAC Addresses to add --" -ForegroundColor White
    Write-Host ""

    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Yellow
    Write-Host "[                      Add MAC Addresses                        ]" -ForegroundColor Yellow
    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Yellow
    Write-Host ""

    $STA = Read-Host "[1] STA MAC Address ----------------->>> :"
    $AP = Read-Host  "[2] AP MAC Address ------------------>>> :"

    $AdjacentMacs = @()  # Lista para almacenar MACs adyacentes

    do {
        $Adjacent = Read-Host "[3] Adjacent AP/STA MAC Address ----->>> :"
        if ($Adjacent) {
            $AdjacentMacs += $Adjacent
        }
    } while ($Adjacent)

    $Filter = "!wlan.fc.retry == 1 && (wlan.ta == $AP || wlan.ta == $STA || wlan.ra == $AP || wlan.ra == $STA)"
    
    foreach ($mac in $AdjacentMacs) {
        $Filter += " && !(wlan.ta == $mac || wlan.ra == $mac) && !(wlan.ta == $mac || wlan.ra == $mac)"
    }

    Write-Host "" 
    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Yellow
    Write-Host "[               Copy & Paste filter to BlackShark               ]" -ForegroundColor Yellow
    Write-Host "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" -ForegroundColor Yellow
    Write-Host "" 

    Write-Host "-----------------------------------------------------------------" -ForegroundColor Cyan
    Write-Host $Filter -ForegroundColor Magenta
    Write-Host "-----------------------------------------------------------------" -ForegroundColor Cyan
    Write-Host "" 
}

do {
    Create-WiresharkFilter
    $choice = Read-Host "Would you like to generate another filter? (Y/N)"
} while ($choice -eq "Y" -or $choice -eq "y")


