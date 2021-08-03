#day22
#kullanıcıya sinema ya da tiyatro tercihi sorulsun sinema izlemek için 15 tl tiyatro için 10 tl ödenmesi gerekmedi öğrencilere 50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan öğrenci değilse inimsiz tutan hesalayarak ekrana yazdıran kodu yazınız
secim=int(input("1-Sinema\n2-Tiyatro\nSeçim yapınız:"))
ucret=0
if secim==1:
    ucret=15
    while True:
        cıns=input("Öğrenci misinz? öğrenci ise e değilseniz h tuşuna basınız:")
        if cıns=="e":
            print(f"Ücretiniz:{ucret/2}")
            break
        elif cıns=="h":
            print(f"Ücretiniz:{ucret}")
            break
        else:
            print("GEÇERSİZ")
elif secim==2:
    ucret=10
    while True:
        cıns=input("Öğrenci misinz? öğrenci ise e değilseniz h tuşuna basınız:")
        if cıns=="e":
            print(f"Ücretiniz:{ucret/2}")
            break
        elif cıns=="h":
            print(f"Ücretiniz:{ucret}")
            break
        else:
            print("GEÇERSİZ")
    
    

    
    
