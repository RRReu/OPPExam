def tek_sayilarin_toplam_ve_carpimini_hesapla(N):
    tek_toplam = 0
    tek_carpim = 1
    cift_kare_toplam = 0

    for i in range(1, N+1):
        if i % 2 != 0:
            tek_toplam += i
            tek_carpim *= i
        else:
            cift_kare_toplam += i**2

    return tek_toplam, tek_carpim, cift_kare_toplam

# Kullanıcıdan giriş al
N = int(input("Bir sayı girin: "))

# Toplamlar ve çarpımları hesapla
tek_toplam, tek_carpim, cift_kare_toplam = tek_sayilarin_toplam_ve_carpimini_hesapla(N)

# Sonuçları yazdır
print(f"1'den {N}'a kadar olan tek sayıların toplamı: {tek_toplam}")
print(f"1'den {N}'a kadar olan tek sayıların çarpımı: {tek_carpim}")
print(f"1'den {N}'a kadar olan çift sayıların karelerinin toplamı: {cift_kare_toplam}")