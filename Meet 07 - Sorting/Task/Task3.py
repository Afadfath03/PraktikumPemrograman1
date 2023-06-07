# Program input nama buku dan sorting nama buku

def InputBuku():
    array = []
    n = int(input("Masukkan jumlah buku: "))
    for i in range(n):
        buku = input(f"Masukkan judul buku ke-{i+1}: ")
        array.append(buku)
    return array

def PrintBuku(array):
    for i in range(len(array)):
        print(f"Buku ke-{i+1}: {array[i]}")

def Insertion_ASC(array):
    for i in range(1, len(array)):
        indeks = array[i]
        j = i-1
        while j >= 0 and indeks < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = indeks
    PrintBuku(array)

def Insertion_DESC(array):
    for i in range(1, len(array)):
        indeks = array[i]
        j = i-1
        while j >= 0 and indeks > array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = indeks
    PrintBuku(array)

buku = InputBuku()

print("\n<=========== Urutkan ===========>")
print("1. Insertion Ascending  (A-Z)")
print("2. Insertion Descending (Z-A)")

pilih = int(input("Masukkan pilihan:"))
if pilih == 1:
    print("\n<--- Sorting Ascending (A-Z) --->")
    Insertion_ASC(buku)
elif pilih == 2:
    print("\n<--- Sorting Descending (Z-A) --->")
    Insertion_DESC(buku)
else:
    print("Pilihan tidak tersedia")