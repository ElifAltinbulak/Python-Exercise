#day10
#kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini
boy=float(input("Boyunuzu giriniz: "))
kilo=float(input("Kilonuzu giriniz: "))

endeks=kilo/(boy*boy)
if endeks <=18:
    print(f"vücut endeksiniz: {endeks}\n dünya sağlık örgütüne göre zayıf")
elif endeks>18 and endeks<=25:
    print(f"vücuk endeksiniz:{endeks}\n dünya sağlık örgütüne göre kilolu")
elif endeks>25 and endeks<=30:
    print(f"vücut endeksiniz:{endeks}\n dünya sağlık örgütüne göre obez")
elif endeks >30:
    print("ciddi bir kilonuz var mutlaka bir sağlık kuruluşuna başvurunuz")
    
    
