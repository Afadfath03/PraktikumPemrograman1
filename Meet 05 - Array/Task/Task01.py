Array = []

jmhElemen = int(input("Masukkan jumlah kata : "))
for i in range(jmhElemen):
    kata = input("Masukkan Kata : ")
    Array.append(kata)

print()

Cari = input("Masukkan kata yang ingin dicari : ")
found = False
for i in range(len(Array)):
    if Cari == Array[i]:
        print(f"Kata {Cari} ditemukan pada indeks ke-{i}")
        found = True

    if i == len(Array)-1 and not found:
        print(f"Kata {Cari} tidak ditemukan")

