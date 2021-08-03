#day7
#yazılı ortalaması girilen öğrencinin sınıf geçme durumunu geçti kaldı gösteren python örneği
n=int(input("ortalamanızı giriniz: "))
if n<50:
    print(f"{n} ile KALDINIZ")
elif n>=50:
    print(f"{n} ile GEÇTİNİZ")
    
