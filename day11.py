#day11
# yaşı girilen kişinin ehliyet alıp alamayacağını gösteren python örneği
yas=int(input("yaşınız: "))
if yas < 18:
    print("yaşınız ehliyet almak için uygun değil")
elif yas >= 18:
    print("yaşınız ehliyet almak için uygundur")
    
