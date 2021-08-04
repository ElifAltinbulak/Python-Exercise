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
