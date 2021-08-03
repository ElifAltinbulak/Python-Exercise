#day24
import random
rand=random.randint(1,100)
i=0
while True:
    i+=1
    sayı=int(input("Lütfen sayı giriniz:"))
    if sayı<rand:
        print("Daha yüksek bir sayı giriniz")
        continue
    elif sayı>rand:
        print("Daha düşük bir sayı giriniz")
        continue
    elif sayı==rand:
        print(f"BİLDİNİZZZ!! {rand}")
        break
    
