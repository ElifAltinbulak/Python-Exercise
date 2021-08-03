#day9
#girilen sayının pozitif negatif ya da o olduğunu bulan python örneği
sayı=int(input("sayınız giriniz: "))
if sayı<0:
    print(f"{sayı} bir negatif sayıdır")
elif sayı>0:
    print(f"{sayı} bir pozitif sayıdır")
else:
    print("Sayı sıfırdır")

