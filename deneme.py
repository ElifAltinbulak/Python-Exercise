a="3 2 4 6 -1 12"
b=a.split()
b=[int(i) for i in b]#sayısal anlamda büyük olması için int değere çevirmek gerekir
print(b)
buyuk=max(b)
kucuk=min(b)
print(buyuk,kucuk)
