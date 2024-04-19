import pyautogui
import time

def rpa_tikla(x, y):
    
        # Koordinatlara git
        pyautogui.moveTo(x, y, duration=0.5)

        # Tıkla
        pyautogui.click()

        print(f"Tıklama başarılı: {x}, {y}")

    

# Örnek kullanım
if __name__ == "__main__":
    # Tıklanacak koordinatları belirle
    hedef_x = 650
    hedef_y = 1055

    # RPA işlemi
    rpa_tikla(hedef_x, hedef_y)
