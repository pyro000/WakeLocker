import keyboard
import time
import jsonloader
from pystray import Icon as icon, MenuItem as item
from PIL import Image
import threading
import pyautogui
import mouse

enabled = True
hotkeys = jsonloader.hotkeys
globaltime = time.time()
pos = mouse.get_position()

def loop():
    global pos, globaltime, enabled, hotkeys
    while True:
        if enabled:
            if mouse.get_position() == pos:
                if time.time() - globaltime >= hotkeys["time"]:
                    print("clicked")
                    pyautogui.click()
                    globaltime = time.time()
            else:
                print("mouse moved")
                pos = mouse.get_position()
                globaltime = time.time()
        time.sleep(1)

def ejecutar_macro(id):
    global enabled, hotkeys

    if hotkeys["hotkeys"][id][1] == "enabled":
        enabled = not enabled
        print(f"Status: ", "active" if enabled else "disabled")
        return
    elif hotkeys["hotkeys"][id][1] == "reload":
        resethotkeys()
        return

def resetear_macro(_, id):
    global hotkeys
    hotkeys["hotkeys"][id][2] = False

def addhotkeys():
    global hotkeys
    for i, h in enumerate(hotkeys["hotkeys"]):
        h.append(False)
        keyboard.add_hotkey(h[0], lambda id=i: ejecutar_macro(id))
        keyboard.on_release(lambda event, id=i: resetear_macro(event, id))

def resethotkeys():
    global hotkeys
    hotkeys = jsonloader.load()
    keyboard.unhook_all_hotkeys()
    addhotkeys()
    print("Reloaded settings.json")

icon_path = 'lib/icon.ico'
image = Image.open(icon_path)

menu = (
    item('Reload Config', resethotkeys),  
    item('Exit', lambda icon, item: icon.stop()),
)

addhotkeys()
main_thread = threading.Thread(target=loop, daemon=True)
main_thread.start()
icon('WakeLocker', image, menu=menu).run()