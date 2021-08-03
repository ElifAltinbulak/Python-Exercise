a=int(input("Lütfen ilk katsayıyı giriniz: "))
b=int(input("Lütfen ikinci katsayıyı giriniz: "))
c=int(input("Lütfen üçüncü katsayıyı giriniz: "))
print(f"{a}x²+{b}x+{c}=0")
delta=(b**2)-4*a*c
x1=(-b+(delta)**0.5)/2*a
x2=(-b-(delta)**0.5)/2*a
if delta<0:
    print("Reel kök yok")
elif delta==0:
    print("Çakışık kök vardır")
    print(f"ilk kök: {x1}\nikinci kök: {x2}")
else:
    print(f"ilk kök: {x1}\nikinci kök: {x2}")
