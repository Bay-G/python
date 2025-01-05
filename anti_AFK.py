import pyautogui as py
import time
import tkinter as tk
from threading import Thread

isActive = False

def start():
    global isActive
    isActive = True
    run_autoclicker()

def stop():
    global isActive
    isActive = False

def run_autoclicker():
    def autoclicker():
        while isActive:
            time.sleep(5)
            py.moveTo(950, 550, 1)
            py.click()
            py.moveTo(965, 555, 1)
            py.click()
            time.sleep(5)
    
    thread = Thread(target=autoclicker)
    thread.start()

window = tk.Tk()
window.geometry("300x400")

buton1 = tk.Button(window, text="Başlat", command=start)
buton1.pack()

buton2 = tk.Button(window, text="Durdur", command=stop)
buton2.pack()

window.mainloop()
