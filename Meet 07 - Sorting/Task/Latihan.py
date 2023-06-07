# Tambah Data Mahasiswa 
def addmahasiswa() :
    jumlah = int(input("Jumlah mahasiswa: "))
    mahasiswa = []
    while(jumlah > 0):
        nama = input("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1
    
    while (True) :
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if (jumlah < 0):
            break

# Hapus Data Mahasiswa
def removemahasiswa(arraymahasiswa) :
    mahasiswa = arraymahasiswa
    print(f"Data mahasiswa {arraymahasiswa}")
    mahasiswa.remove(input("Hapus mahasiswa: "))
    print(f"Data mahasiswa {mahasiswa}")
    panggil(mahasiswa)

#Urutkan Data Mahasiswa
def ascmahasiswa(arraymahasiswa) :
    mahasiswa = arraymahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    viewMahasiswa(mahasiswa)

# Lihat Data Mahasiswa
def viewMahasiswa(arraymahasiswa) :
    mahasiswa = arraymahasiswa
    for i in mahasiswa:
        print(f"Nama mahasiswa : {i}")
    panggil(mahasiswa)


def panggil(arraymahasiswa) :
    mahasiswa = arraymahasiswa
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Keluar")
    pilih = int(input("Masukkan pilihan: "))
    if (pilih == 1):
        addmahasiswa()
    elif (pilih == 2):
        removemahasiswa(mahasiswa)
    elif (pilih == 3):
        ascmahasiswa(mahasiswa)
    elif (pilih == 4):
        viewMahasiswa(mahasiswa)
    elif (pilih == 5):
        print("Keluar")
    else:
        print("Pilihan tidak tersedia")


addmahasiswa()