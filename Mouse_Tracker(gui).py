import tkinter as tk
import pyautogui

kontrol =False

def konum_guncelle():

    global kontrol

    if kontrol:
        kontrol=False
        return    

    kontrol = True

    while kontrol:
        x, y = pyautogui.position()
        labelx.config(text=f"X Konum: {x}")
        labely.config(text=f"Y Konum: {y}")
        root.update()
        

root = tk.Tk()
root.geometry("400x300")

labelx = tk.Label(root, text="X Konum: ")
labelx.pack(pady=10)

labely = tk.Label(root, text="Y Konum: ")
labely.pack(pady=10)

buton = tk.Button(root, text="Başlat/Dur", command=konum_guncelle)

buton.pack(pady=10)

root.mainloop()