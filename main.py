import ctypes
import threading
from playsound import playsound
user32 = ctypes.windll.user32
appcmd = 0x319
up = 0x0a0000
down = 0x090000
def addv():
    hd = user32.GetForegroundWindow()
    user32.PostMessageA(hd,appcmd,0,up)

def keep_max():
    while True:
        try:
            addv()
        except:
            pass

def pls():
    while True:
        try:
            playsound("play.mp3")
        except:
            pass

if __name__ == "__main__":
    k = threading.Thread(target=keep_max)
    p = threading.Thread(target=pls)
    k.start()
    p.start()
