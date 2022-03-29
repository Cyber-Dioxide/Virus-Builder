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

    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Follow me on Instagram @cyber-dioxide ", "- " * 4 + ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX,  "- " * 4, " [+] Coding Instagram @cyber_dioxide_ ", "- " * 4+ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+ran + "|")


def banner2():


    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Coding Instagram @cyber_dioxide_ ", "- " * 4+ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+ran + "|")

def clear():
    os.system("clear")
