import math

# 2D uzayda noktaları temsil eden bir liste oluşturuyoruz
noktalar = [(1, 2), (3, 4), (5, 6), (7, 8)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def mesafeHesapla(nokta1, nokta2):
    x1, y1 = nokta1
    x2, y2 = nokta2
    # Öklid mesafesi formülünü uyguluyoruz
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Tüm mesafeleri hesaplamak için bir liste oluşturuyoruz
mesafeler = []
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):  # Aynı nokta üzerinden hesaplama yapmıyoruz
        mesafe = mesafeHesapla(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Hesaplanan mesafeler arasından en küçük olanı buluyoruz
min_mesafe = min(mesafeler)

# Sonuçları yazdırıyoruz
print("Hesaplanan mesafeler:", mesafeler)
print("En küçük mesafe:", min_mesafe)
