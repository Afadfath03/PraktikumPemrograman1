# Mencari KPK dari 2 bilangan
bilangan1 = int(input("Masukkan bilangan pertama : "))
bilangan2 = int(input("Masukkan bilangan kedua   : "))

a = bilangan1
b = bilangan2

while a != b:
    if a < b:
        a += bilangan1
    else:
        b += bilangan2
        
print(f"KPK dari {bilangan1} dan {bilangan2} adalah {a}")

