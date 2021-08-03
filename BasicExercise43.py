#day52
#Klavyede 0 girilene kadar sayıların toplamını bulun program python
toplam=0
while True:
    sayı=int(input("Bir sayı giriniz: "))
    if sayı!=0:
        toplam+=sayı
    else:
        print(f"Sonuç: {toplam}")
        break
