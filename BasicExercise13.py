#Day13
#1-100 arası 3 e ve 5 e tam bölünün sayılar bulan python örneği
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
