import os

logo = f"""
██╗   ██╗██╗██████╗ ██╗   ██╗███████╗               
██║   ██║██║██╔══██╗██║   ██║██╔════╝               
██║   ██║██║██████╔╝██║   ██║███████╗               
╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║               
 ╚████╔╝ ██║██║  ██║╚██████╔╝███████║               
  ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝               
                                                    
██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗ 
██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                  
"""

from files.colors import *


def banner():
    print(ran + logo)

    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX,  "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+ran + "|")


def banner2():


    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+ran + "|")

def clear():
    os.system("clear")