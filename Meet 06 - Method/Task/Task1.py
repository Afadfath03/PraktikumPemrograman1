def GenapGanjil(x):
    if x % 2 == 0:
        # print(f"{x} adalah bilangan Genap")
        return "Genap"
    else:
        # print(f"{x} adalah bilangan Ganjil")
        return "Ganjil"
        
Bilangan = int(input("Masukkan Bilangan: "))

# GenapGanjil(Bilangan)

print(f"{Bilangan} adalah bilangan {GenapGanjil(Bilangan)}")