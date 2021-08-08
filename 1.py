#1
print("Bu bizim ilk örneğimiz")

#2
#Girilen kullanıcı ismine göre ekrana merhaba kullanıcı yazdıran python kodunu yazınız
isim=input("İsminizi giriniz: ")
print(f"Merhaba {isim.capitalize()}")

#3
#Ehliyet almak için uygunmusunuz programı
yas=int(input("Yaşınız: "))
if yas<18:
    print(f"{yas} ne yazık ki ehliyet almak için uygun değilsiniz")
else:
    print(f"{yas} ehliyet almak için uygunsunuz")

#4
#1 den 10 a kadar olan sayıları alt alta yazdıran python kodunu yazınız
for i in range(1,11):
    print(i)
print("çift sayılar")

#5
#1 den 20 ye kadar olan çift sayıları alt alta yazıran python kodunu yazınız
for i in range(1,21):
    if i%2==0:
        print(i)
print("tek sayılar")

#6
#1 den 20 ye kadar olan tek sayılar alt alta yazdıran python kodunu yazınız
for i in range(1,21):
    if i%2==1:
        print(i)
print("3 ve 5 e bölünen sayılar")

#7
#1 den 100 e kadar olan sayılardın aynı anda 3 ve 5 e tam bölünen sayılar alt alta yazdıran python kodunu yazınız
for i in range(1,101):
    if i%5==0 and i%3==0:
        print(i)
#8
#klavyede kısa kenar uzunulğu ve uzun kenar uzunluğu girilen dikdörgenin alın ve çevresini hesaplayan python kodunu yazınız
kısa=int(input("Kısa kenar: "))
uzun=int(input("Uzun kenar: "))
print(f"Dikdörtgen Alan: {kısa*uzun}")

#9
#klavyede kısa kenar ve uzun kenar uzunluğu girilen dikdörtgenin alanını fonksiyon kullanarak hesaplayan python kodunu yazınız
def dikdörtgen_alan(kısa,uzun):
    return kısa*uzun
print(f"Fonksiyon alan formülü: {dikdörtgen_alan(2,5)}")

#10
#Önceden belirlenen bir liste içerisinde bulunan sayılardan kaç tanesinin 5 in katı olduğunu bulan python kodunu yazınız
sayılar=[18,15,22,19,85,32,65,30,95,10,12,20,32,55,34,28,101,5,4,32]
s=0
for i in sayılar:
    if i%5==0:
        s+=1
        print(i)
print(f"{s} tane 5 in katı vardır")

#11
#Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan çift sayıların ortalamasını bulan python kodunu yazınız
ba=int(input("Başlangıç sayısı: "))
bi=int(input("Bitiş sayısı: "))
çsayaç,çtoplam=0,0
for i in range(ba,bi+1):
    if i%2==0:
        çsayaç+=1
        çtoplam+=i
print(f"Ortalama: {çtoplam/çsayaç}")

#12
#klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan tek sayıların ortalamısını bulan python kodunu yazınız
ba=int(input("Başlangıç sayısı: "))
bi=int(input("Bitiş sayısı: "))
tsayaç,ttoplam=0,0
for i in range(ba,bi+1):
    if i%2==1:
        tsayaç+=1
        ttoplam+=i
print(f"Ortalama: {ttoplam/tsayaç}")

#13
#klavyden girilen başlangıç ve bitiş sayıların arasında bulunan sayıların ortalamısını bulan python kodunu yazınız
ba=int(input("Başlangıç sayısı: "))
bi=int(input("Bitiş sayısı: "))
sayaç,toplam=0,0
for i in range(ba,bi+1):
    sayaç+=1
    toplam+=i
print(f"Ortalama: {toplam/sayaç}")

#14
#klavyedan girilen başlangıç ve bitiş sayıları arasında bulunan sayıların toplamını bulan python kodunu yazınız
ba=int(input("Başlangıç sayısı:"))
bi=int(input("Bitiş sayısı: "))
toplam=0
for i in range(ba,bi+1):
    toplam+=i
print(f"Toplam: {toplam}")



#16
#klavyeden girilen üç yazılı notunun ortalamasını bulan python kodunu yazınız
toplama=0
for i in range(1,4):
    n=int(input(f"{i}.Yazılı notunu giriniz: "))
    toplama+=n
print(f"Ortalama: {toplama/i}")

#17
#klavyede girilen sayının tek sayı mı çift sayı mı olduğunu bulan ve sonucu ekranda gösteren python kodunu yazınız
sayı=int(input("Bir sayı giriniz: "))
if sayı%2==0:
    print(f"{sayı} çift bir sayıdır")
else:
    print(f"{sayı} tek bir sayıdır")

#18
"""Örnek bir otoparkın ücret taifesi aşağıdaki gibidir
1 saatte kadar: 5 tl
1-5 saat arası : saat başı 4 tl
5 saatte fazla: saat başı 3 tl
buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız"""
saat=int(input("1- 1 Saatte kadar\n2- 1-5 saat fazla\n3- 5 saatte fazla\nKaç saat kaldınız: "))
if saat==1:
    ucret=5
elif 1<saat<=5:
    ucret=saat*4
else:
    ucret=saat*3
print(f"Ödemeniz gereken ücret : {ucret}")

#19
#klavyeden girilen bir ifadeyi ekrana 10 defa yazdıran python kodunu yazınız
metin=input("Bir ifade giriniz: ")
for i in range(1,11):
    print(metin)

#20
#0 ile 100 arasındaki tek sayıların toplamı
toplam=0
for i in range(1,101):
    if i%2==1:
        toplam+=i
print(f"1 ile 100 arasındaki tek sayıların toplamı {toplam}")

#21
#klavyeden girilen sayıya kadar olan sayıların toplamının hesaplayan ve sonucu yazdıran python kodunu ghile döngüsü kullanarak yapan kodunu yazınız
bitiş=int(input("Bitiş sayısını giriniz: "))
toplam,i=0,0
while i<=bitiş:
    toplam+=i
    i+=1
print(f"Sonuç: {toplam}")

#23
#klavyeden girilen bir metni harflarıne ayıran python programını while döngüsü ile yazdıran kodunu yazınız
metin=input("Bir metin giriniz: ")
sayaç=0
while sayaç < len(metin):
    print(metin[sayaç])
    sayaç+=1

#24
#0 ile 100 arasında 10 tane rastgele tam sayı üreten ve bu sayılardan en büyüğü ile en küçüğünü bulan ve ekranda gösteren python kodunu yazınız
import random
sayı=[]
for i in range(0,10):
    rand=random.randint(1,100)
    sayı.append(rand)
print(f"En büyüğü: {max(sayı)}")
print(f"En küçüğü: {min(sayı)}")

#25
#klavyeden Fahrenheit cinsinden girilen sıcaklığı dereceye çeviren python kodunu yazınız
derece=int(input("Bir fahrenheit yazınız: "))
c=(derece-32)/1.8
print(f"{derece}F = {c}C'dir ")

#26
#klavyeden bir kenar uzunluğu girilen karenin alanını ve çevresini bulan ve ekrana yazdıran python kodunu yazınız
k=int(input("Kenar:"))
alan=k**2
çevre=k*4
print(f"Alan:{alan}\nÇevresi:{çevre}")

#27
#klavyeden girilen saniye değerinin kaç saat kaç dakika ve kaç saniye olduğunu bulan python kodunu yazınız
s=int(input("Saniye giriniz: "))
saat=s//3600
s=s%3600
dakika=s//60
s=s%60
print(f"Girdiğiniz saniyenin saat dönüşümü: {saat}sa {dakika}dk {s}sn")

#28
#klavyede girilen iki sayıdan büyük olanı bulan ve ekranda gösteren python kodunu yazınız
n1=int(input("1-Sayıyı giriniz: "))
n2=int(input("2-Sayıyı giriniz: "))
if n1>n2:
    print("Birinci sayı büyüktür")
elif n2>n1:
    print("İkinci sayı büyüktür")
else:
    print("İki sayı eşittir")

#29
#klavyeden girilen not ortalaması göre kişinin takdir teşekkür normal geçme ya da sınıf tekrarı yapması gerektiğini gösteren python kodunu yazınız
toplam=0
for i in range(1,4):
    n=int(input(f"{i}.Yazılı notu: "))
    toplam+=n
    sonuç=toplam/i
if 50<sonuç<=75:
    print(f"{sonuç} teşekkür belgesi")
elif sonuç>=85:
    print(f"{sonuç} takdir belgesi")
else:
    print("Boş")

#30
#klayeden girilen beş adet sayının toplamını bulan ve bulunan toplamın tek sayım yoksa çift sayı mı olduğunu bulan python kodunu yazınız
topla=0
for i in range(1,6):
    n=int(input(f"{i}.sayıyı giriniz: "))
    topla+=n
if topla%2==0:
    print(f"{topla} sayısı çifttir")
else:
    print(f"{topla} sayısı tektir")

#31
#0 ile 50 sayısı arasında 4 e bölünen sayıları listeleyen programın python kodlarını yazınız
liste=[]
for i in range(0,51):
    if i%4==0:
        liste.append(i)
print(liste)

#32
#klavyeden girilen beş tane sayıdan en büyüğünü bulup ekranda gösteren python kodunu yazınız
liste=[]
for i in range(1,6):
    n=int(input(f"{i}.sayıyı giriniz: "))
    liste.append(n)
print(max(liste))

#33
#klavyeden kullanıcının girdiği ismin kaç harfli olduğunu bulan programın python kodlarını yazınız
metin=input("Bir isim giriniz: ")
print(f"Harf sayısı: {len(metin)}")

#34
#klavyeden 0 rakamını girilene kadar girilen tüm sayıların kaç tane olduğunu ve bu sayıların toplamını bulan ve ekranda gösteren python kodunu yazınız
sayaç,toplam=0,0
while True:
    sayı=int(input("Bir sayı giriniz: "))
    if sayı!=0:
        toplam+=sayı
        sayaç+=1
    else:
        print(f"Sonuç: {toplam} Tane: {sayaç}")
        break
#35
#daha önce belirtilmiş bir liste içersinide rastgele bir sayı seçen ve ekran gösteren python kodunu yazınız
liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27]
sayı=random.choice(liste)
print(sayı)

#36
#klavye girilen a b c değerlereni göre 2.dereceden bir denkelemin köklerini bulan ve ekranda gösteren python kodunu yazınız
a=int(input("Lütfen ilk katsayıyı giriniz: "))
b=int(input("Lütfen ikinci katsayıyı giriniz: "))
c=int(input("Lütfen üçüncü katsayıyı giriniz: "))
print(f"{a}x²+{b}x+{c}=0")
delta=(b**2)-4*a*c
x1=(-b+(delta)**0.5)/2*a
x2=(-b-(delta)**0.5)/2*a
if delta<0:
    print("Reel kök yok")
elif delta==0:
    print("Çakışık kök vardır")
    print(f"ilk kök: {x1}\nikinci kök: {x2}")
else:
    print(f"ilk kök: {x1}\nikinci kök: {x2}")

#37
#klavyeden girilen yıl ve o yılın ayının takvimini ekranda gösteren python kodunu yazınız
import calendar

yıl = int(input("Yıl giriniz:  "))
ay = int(input("Ay Giriniz:  "))

print(calendar.month(yıl, ay))

#38
#klavyeden 10'luk tabanda girilmiş bir sıyıyı 2'lik 8'lik ve 16'lık tabana çeviren ve ekranda gösteren python kodunu yazınız
sayı=int(input("bir sayı giriniz: "))
print(f"2'lik tabanda:{bin(sayı)}")
print(f"8'lik tabanda:{oct(sayı)}")
print(f"16'lık tabanda:{hex(sayı)}")

#39
#klavyeden girilen bir ismin klavyeden girilen bir sayı kadar yan yana yazdıran python kodunu yazınız
isim=input("İsim giriniz: ")
sayı=int(input("kaç defa yazılsın: "))
print((isim+" ")*sayı)

#40
#klavyede girilen bir sayının karesini ve küpünü bulan ve ekranda gösteren python koduna yazınız
sayı=int(input("Sayı giriniz:"))
print(f"x²={sayı**2}\nx^3:{sayı**3}")

#41
#klavyede girilen başlangıç bitiş ve artış miktarı girilen sayıları alt alta ekranda yazdıran python kodunu yazınız
ba=int(input("başlangıç:"))
bi=int(input("bitiş:"))
artıs=int(input("artış:"))
for i in range(ba,bi,artıs):
    print(i)

#42
#klavyeden girilen sayıdan itibaren sıfıra kadar olan sayıları ekrana yazan python kodunu yazınız
n=int(input("Başlangıç: "))
for i in range(n,0,-1):
    print(i)

#43
#klavyeden girilen iki sayı arasındaki sayıların toplamını bulan python kodunu yazınız
ba=int(input("Başlat: "))
bi=int(input("Bitiş: "))
toplam=0
for i in range(ba,bi+1):
    toplam+=i
print(toplam)

#44
#klavyeden girilen iki sayı arasındaki sayıların ortalamasını bulan python kodunu yazınız
a=int(input("1-"))
b=int(input("2-"))
toplam=0
for i in range(a,b+1):
    toplam+=i
print(f"Sonuç: {toplam/2}")

#45
#klavyeden girilen sayı 0(sıfır) olana adar girilen tüm sayıları topamayın ve ekranda gösteren python programını while döngüsü ile yazınız
i=1
toplam=0
while i!=0:
    i=int(input("Sayı giriniz: "))
    toplam+=i
print(f"Sonuç: {toplam}")

#46
#3x3 bir matrisin eleman indislerini yazdıran python kodunu yazınız
for i in range(0,3):
    for j in range(0,3):
        print([i,j])

#47
#klavyeden girilen bir şifrenin karakterlerini kontrol ederek girilen şifrenin 4 karakte olana kadar yeni şefre isteyen girilince de doğru şifreyi ekranda gösteren python kodunu yazınız
while True:
    sifre=input("Bir şifre giriniz:")
    if len(sifre)<4 or len(sifre)>4:
        print("4 karakter olmalı")
    else:
        print("Şifreniz hazır")
        s=input("Şifrenizi görmek ister misiniz?(e/h): ")
        if s=="e":
            print(f"Şifreniz: {sifre}")
            break
        elif s=="h":
            print(f"Teşekkürler")
            break
        else:
            print("geçersiz")

        
