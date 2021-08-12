#Siz Kodlayın
import random
sayı=random.randint(1,101)
sayac=1
while 1<=sayac<=7:
    tahmin=int(input(f"Sayı giriniz {sayac}. hakkınız:"))
    if sayı==tahmin:
        print("TEBRİKLER KAZANDINIZ")
        break
    elif sayı>tahmin:
        print("KÜÇÜK BİR TAHMİNDE BULUNDUNUZ")
        sayac+=1
        continue
    elif sayı<tahmin:
        print("BÜYÜK BİR TAHMİNDE BULUNDUNUZ")
        sayac+=1
        continue
print("HAKKINIZ BİTTİ TEKRAR BEKLERİZ")
"""if 1<=sayac<=7:
    while 1<=sayac<=7:
        tahmin=int(input(f"Sayı giriniz {sayac}. hakkınız:"))
        if sayı==tahmin:
            print("TEBRİKLER KAZANDINIZ")
            break
        elif sayı>tahmin:
            print("KÜÇÜK BİR TAHMİNDE BULUNDUNUZ")
            sayac+=1
            continue
        elif sayı<tahmin:
            print("BÜYÜK BİR TAHMİNDE BULUNDUNUZ")
            sayac+=1
            continue
else:
    print("HAKKINIZ BİTTİ TEKRAR BEKLERİZ")
    
"""

    
