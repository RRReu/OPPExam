ağırlık = 100
uzunluk = 20
ağırlıkbüyüme = 0.05
uzunlukbüyüme = 0.1
hedefağırlık = 30
hedefuzunluk = 150

şimdikiağırlık = ağırlık
şimdikiuzunluk = ağırlık
ay = 0

while ağırlık<hedefağırlık or uzunluk<hedefuzunluk:
    ağırlık += şimdikiağırlık*ağırlıkbüyüme
    uzunluk += şimdikiuzunluk*uzunlukbüyüme
    ay += 1

print(f"İstenin kilo ve boy uzunluğuna ulaşmak toplam {ay} ay sürecektir. ")