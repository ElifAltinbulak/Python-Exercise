#day23
#girilen sayının asal sayı mı değil mi olduğunu bulan python örneği
sayı=int(input("Sayı giriniz: "))
for i in range(2,sayı+1):
    if sayı%i==0:
        continue
    else:
        print("Asal sayıdır")
        break
