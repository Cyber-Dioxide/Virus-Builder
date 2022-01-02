import time

from files import colors
c = colors

def menu():
    print(f"""
    {c.c}[1]{c.lr} EXIT
    {c.c}[2]{c.lr} Application Bomber    
    {c.c}[3]{c.lr} Auto Shutdown
    {c.c}[4]{c.lr} CapsLock Toggle
    {c.c}[5]{c.lr} Danger Zone
    {c.c}[6]{c.lr} Registry Eraser
    {c.c}[7]{c.lr} System32 Remover
    {c.c}[8]{c.lr} Drive Eraser
    {c.c}[9]{c.lr} Fork Bomb
    {c.c}[10]{c.lr} Internet Disabler
    {c.c}[11]{c.lr} Network Flooder
    {c.c}[12]{c.lr} PC Crasher
    {c.c}[13]{c.lr} PC Crasher 2
    {c.c}[14]{c.lr} Shut Down{c.c}(Not Dangerous)
    {c.c}[15]{c.lr} Shut UP Internet
    {c.c}[16]{c.lr} Stop Internet
    {c.c}[17]{c.lr} System Eraser
    {c.c}[18]{c.lr} System Melter
    {c.c}[19]{c.lr} The Matrix
    {c.c}[20]{c.lr} Time Bomb{c.c}(Needs configuration)
    """)

def sleep(n):
    time.sleep(n)