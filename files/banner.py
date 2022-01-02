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
from colorama import Fore,Style
from files import colors
c = colors
def banner():
    print(c.ran + logo)
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "|"+ "\n", "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "|"+ "\n", "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    os.system("clear")