#day30
#kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulan python örneği sıyının çift olup olmadığı fonksoyun ile kontrol ediliyon
def çift(sayı):
    return sayı%2==0
sayı1=int(input("başlangıç sayınızı giriniz: "))
sayı2=int(input("bitiş sayınızı giriniz: "))
çtoplam=0
s=0
for i in range(sayı1,sayı2+1):
    if çift(i):
        çtoplam=çtoplam+i
        s=s+1
print(çtoplam)
print(f"Ortalama={çtoplam/s}")
