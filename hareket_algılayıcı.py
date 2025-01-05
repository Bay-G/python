import cv2
import numpy as np


# Kamerayı başlat
cap = cv2.VideoCapture(0)

# İlk görüntüyü al (başlangıç durumu)
ret, prev_frame = cap.read()
if not ret:
    print("Kamera görüntüsü alınamadı!")
    cap.release()
    cv2.destroyAllWindows()

# Görüntüyü BGR formatında analiz et
prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

print("Kamera başlatıldı. Çıkış yapmak için 'q' tuşuna basın.")
sayaç=1
threshold_value = 70
while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    # Görüntüyü gri tona çevir
    current_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Önceki görüntü ile şu anki görüntü arasındaki farkı hesapla
    frame_diff = cv2.absdiff(prev_frame_gray, current_frame_gray)

    # Farkın belli bir eşik değeri üzerinde olup olmadığını kontrol et
    
    _, thresh = cv2.threshold(frame_diff, threshold_value, 255, cv2.THRESH_BINARY)

    # Eğer fark varsa (yani bir renk değişikliği olmuşsa)
    if np.sum(thresh) > 0:
        print("Görüntüde renk değişikliği tespit edildi!",sayaç," threshold değeri: ",threshold_value)
        sayaç+=1
        

    # Görüntüdeki değişiklikleri göstermek için farkları ekrana yansıt
    cv2.imshow("Farklı Piksel Alanları", thresh)

    # Yeni görüntüyü önceki görüntü olarak güncelle
    prev_frame_gray = current_frame_gray

    # Orijinal görüntüyü göster
    cv2.imshow("Kamera Görüntüsü", frame)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        threshold_value+=10

    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        threshold_value-=10

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
