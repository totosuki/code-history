from pynput import mouse, keyboard
import pyautogui
import sys

def on_press(key):
    global click_count
    if key == keyboard.Key.esc:
        return False
    elif key.char == 's':
        pyautogui.click(button="left", clicks=100, interval=0.1)
    elif key.char == 'e':
        print("aiu")

keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
keyboard_listener.join()












    




