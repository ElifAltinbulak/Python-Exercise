#day20
#1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda gösteren python örneği
sayı=int(input("sayı giriniz: "))
çtoplam=0
ttoplam=0
for i in range(1,sayı+1):
    if i%2==0:
        çtoplam+=i
    else:
        ttoplam+=i
print(f"Girilen sayı:{sayı}\nÇift sayı toplamı:{çtoplam}\nTek sayı toplamı:{ttoplam}")
