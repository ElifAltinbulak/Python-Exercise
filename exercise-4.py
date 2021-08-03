#day36
#Kullanıcının girdiği n adet sayıdan tek ve çift olanların ayrı ayrı ortalaması hesaplayan ve ekranda gösteren python kodları
n=int(input("Kaç tane sayı gireceksiniz: "))
çtoplam,ttoplam,sç,st=0,0,0,0
for i in range(n):
    s=int(input("Sayınızı giriniz: "))
    if s%2==0:
        çtoplam+=s
        sç+=1
    else:
        ttoplam+=s
        st+=1
if st!=0 and sç!=0:
    print(f"Girilen tek sayıların ortalaması:{ttoplam/st}")
    print(f"Girilen çift sayıların ortalaması:{çtoplam/sç}")
else:
    print("Kabul edilmez")
        
