#day44
#10-20 arası sayılardan oluşan sayılar isimli bir liste oluşturun oluşturulan liste ile sayılar2 listesini birleştirerek 4 e tam bölünen sayılar ekrana yazdırınız
liste=[10,11,12,13,14,15,16,17,18,19,20]
liste2=[21,22,23,24,25]
liste+=liste2
for i in liste:
    if i%4==0:
        print(i)
