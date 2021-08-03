#day55
#for döngüsü ile liste öğlerin ortalamasını hesaplayın
n=int(input("Liste eleman sayısını giriniz: "))
liste=[]
for i in range (1,n+1) :
    a=int(input("Sayınızı giriniz: "))
    liste.append(i)
    sonuç=sum(liste)/n
print(liste)
print(f"Ortalama: {sonuç}")
    
    
    
