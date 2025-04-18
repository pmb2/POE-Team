@echo off
set "HOST_EXE=host.exe"
set "CLIENT_EXE=client.exe"

:: Add Windows Defender exclusions
powershell -Command "Add-MpPreference -ExclusionPath '%cd%\%HOST_EXE%'"
powershell -Command "Add-MpPreference -ExclusionPath '%cd%\%CLIENT_EXE%'"

:: Grant firewall access
netsh advfirewall firewall add rule name="PoE Sync Host" dir=in action=allow program="%cd%\%HOST_EXE%" enable=yes
netsh advfirewall firewall add rule name="PoE Sync Client" dir=in action=allow program="%cd%\%CLIENT_EXE%" enable=yes

echo [Success] Added antivirus exceptions! Press any key...
pause
