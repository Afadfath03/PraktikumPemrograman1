# Menghitung total nilai yang telah di input
bilangan = int(input("Masukkan bilangan: "))
total = 0

print(f"Total Bilangan = ", end="")

for i in range(bilangan, 0, -1):
    total = total + i
    if i == 1:
        print(f"{i} = {total}")
        break    
    print(f"{i} + ", end="")

