import numpy as np                 # NumPy kütüphanesini np kısaltmasıyla içe aktarır.
import pandas as pd                # Pandas kütüphanesini pd kısaltmasıyla içe aktarır.
import matplotlib.pyplot as plt   # Matplotlib kütüphanesinin pyplot modülünü plt kısaltmasıyla içe aktarır.

# Rastgele koordinatları üretme
num_points = 1000                              # Oluşturulacak koordinat sayısını belirler.
x_coords = np.random.randint(0, 1001, num_points)  # 0 ile 1000 arasında rastgele tam sayı x koordinatları oluşturur.
y_coords = np.random.randint(0, 1001, num_points)  # 0 ile 1000 arasında rastgele tam sayı y koordinatları oluşturur.

# Veri çerçevesini oluşturma
df = pd.DataFrame({'X': x_coords, 'Y': y_coords})  # Pandas DataFrame'i oluşturarak x ve y koordinatlarını içeren bir veri çerçevesi oluşturur.

# Excel dosyasına kaydetme
df.to_excel('koordinatlar.xlsx', index=False)     # Oluşturulan veri çerçevesini 'koordinatlar.xlsx' adlı Excel dosyasına kaydeder. index=False, satır indekslerini dosyaya yazmamayı sağlar.

# Grafik oluşturma
plt.figure(figsize=(8, 8))                       # Boyutu 8x8 inç olan yeni bir grafik penceresi oluşturur.
plt.scatter(x_coords, y_coords, s=5, c='blue', alpha=0.5)  # Scatter plot (dağılım grafiği) çizer. Her bir nokta 5 piksel büyüklüğünde, mavi renkte ve yarı saydamdır.
plt.grid(True)                                   # Izgara çizgilerini ekler.
plt.title('Rastgele Koordinatlar')              # Grafiğin başlığını belirler.
plt.xlabel('X Koordinati')                       # X ekseninin etiketini belirler.
plt.ylabel('Y Koordinati')                       # Y ekseninin etiketini belirler.
plt.show()                                       # Grafiği gösterir.
