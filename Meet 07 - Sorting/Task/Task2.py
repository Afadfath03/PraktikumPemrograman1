# Program mengurutkan nama Anggota Organisasi

def Selection_ASC(array):
    for i in range(len(array)):
        indeks = i
        for j in range(i+1, len(array)):
            if array[indeks] > array[j]:
                indeks = j
        array[i], array[indeks] = array[indeks], array[i]
    return array

Nama = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]

print("Nama 10 Anggota Organisasi")
print("Nama Sebelum Diurutkan :", Nama)
print("Nama Setelah Diurutkan :", Selection_ASC(Nama))