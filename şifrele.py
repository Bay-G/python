import tkinter as tk
from tkinter import ttk

CRYPTE = {
    "\t": "0000 0000 0000 0000",
    " ": "0000",
    "a": "1000",
    "b": "0100",
    "c": "1100",
    "ç": "0010",
    "d": "1010",
    "e": "0110",
    "f": "1110",
    "g": "0001",
    "ğ": "1001",
    "h": "0101",
    "ı": "1101",
    "i": "0011",
    "j": "1011",
    "k": "0111",
    "l": "1111",
    "m": "00001",
    "n": "10001",
    "o": "01001",
    "ö": "11001",
    "p": "00101",
    "r": "10101",
    "s": "01101",
    "ş": "11101",
    "t": "00011",
    "u": "10011",
    "ü": "01011",
    "v": "11011",
    "y": "00111",
    "z": "10111"
}

def encrypt(message):
    encrypted_message = ""
    for char in message:
        encrypted_message += CRYPTE[char] + " "
    return encrypted_message.strip()

def save_to_file(encrypted_message, filename):
    with open(filename, "w") as file:
        file.write(encrypted_message)

def encrypt_and_save():
    message = entry.get()
    encrypted_message = encrypt(message)
    save_to_file(encrypted_message, "log_kayitlari.txt")
    result_label.config(text="Şifrelenmiş mesaj dosyaya kaydedildi.")

root = tk.Tk()
root.title("Mesaj Şifreleyici")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

label = ttk.Label(frame, text="Şifrelenecek Mesaj:")
label.grid(row=0, column=0, sticky=tk.W)

entry = ttk.Entry(frame, width=50)
entry.grid(row=0, column=1)

encrypt_button = ttk.Button(frame, text="Şifrele ve Kaydet", command=encrypt_and_save)
encrypt_button.grid(row=1, column=0, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
