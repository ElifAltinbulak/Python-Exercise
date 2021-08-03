#day19
#kullanıcıdan gidiği iki sayı arasındaki sayıların toplamını gösteren python örneği
sayı1=int(input("Sayı giriniz: "))
sayı2=int(input("Sayı giriniz: "))
toplam=0
for i in range(sayı1,sayı2+1):
    toplam+=i
print(f"girinlen sayıların arasındaki sonuç: {toplam}")
