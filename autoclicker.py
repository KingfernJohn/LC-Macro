from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
mouse = Controller()
key__i = input("Start and Stop key: ")
inter_key = KeyCode(char=key__i)
def ackt(key):
    if(key==inter_key):
        mouse.click(Button.left)
with Listener(on_press=ackt) as listener:
    listener.join()