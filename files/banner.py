import os
from rgbprint import gradient_print
import platform

logo = f"""
            ██╗  ██╗██╗███╗   ██╗ ██████╗               
            ██║ ██╔╝██║████╗  ██║██╔════╝                 
            █████╔╝ ██║██╔██╗ ██║██║  ███╗               
            ██╔═██╗ ██║██║╚██╗██║██║   ██║               
            ██║  ██╗██║██║ ╚████║╚██████╔╝              
            ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝               
                                                                
            ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗ 
            ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
            ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
            ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
            ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
            ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                 Author: king_hxcker_daddy | Virus Installer     (V4.0)
        =============================================================
                        [+] Discord ( discord.gg/mrontop ) 
                        [+] Instagram @king_hxcker_daddy                          
        =============================================================
"""




def banner():
    gradient_print(logo , start_color='cyan' , end_color='yellow')


def clear():
    os.system("cls") if 'Windows' in platform.platform() else os.system("clear")
