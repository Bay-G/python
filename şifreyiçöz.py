import tkinter as tk
from tkinter import ttk

ENCRYPTE = {
    "0000 0000 0000 0000": "\t",
    "0000": " ",
    "1000": "a",
    "0100": "b",
    "1100": "c",
    "0010": "ç",
    "1010": "d",
    "0110": "e",
    "1110": "f",
    "0001": "g",
    "1001": "ğ",
    "0101": "h",
    "1101": "ı",
    "0011": "i",
    "1011": "j",
    "0111": "k",
    "1111": "l",
    "00001": "m",
    "10001": "n",
    "01001": "o",
    "11001": "ö",
    "00101": "p",
    "10101": "r",
    "01101": "s",
    "11101": "ş",
    "00011": "t",
    "10011": "u",
    "01011": "ü",
    "11011": "v",
    "00111": "y",
    "10111": "z"
}

def decrypt(encrypted_message):
    decrypted_message = ""
    encrypted_list = encrypted_message.split()
    for item in encrypted_list:
        decrypted_message += ENCRYPTE[item]
    return decrypted_message

def decrypt_message():
    encrypted_message = entry.get()
    decrypted_message = decrypt(encrypted_message)
    result_label.config(text=f"Çözülmüş Mesaj: {decrypted_message}")

root = tk.Tk()
root.title("Şifreli Mesaj Çözücü")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

label = ttk.Label(frame, text="Çözülecek Şifreli Mesaj:")
label.grid(row=0, column=0, sticky=tk.W)

entry = ttk.Entry(frame, width=50)
entry.grid(row=0, column=1)

decrypt_button = ttk.Button(frame, text="Çöz", command=decrypt_message)
decrypt_button.grid(row=1, column=0, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
