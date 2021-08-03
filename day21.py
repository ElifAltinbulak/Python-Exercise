#day21
#maaş ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren python örneği
maas=int(input("Maaşınızın giriniz: "))
zam=int(input("Zam Oranı(%): "))
yenimaas=maas+(maas*zam/100)
print(f"Zamlı yeni maaş:{yenimaas}")
