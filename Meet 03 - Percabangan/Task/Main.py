# Data Diri

print("======================================")
print("======== INPUT DATA DIRI ANDA ========")
Nama         = input("Nama          : ")
JenisKelamin = input("Jenis Kelamin : ")
print("| 1. Islam | 2. Kristen | 3. Katolik | 4. Hindu | 5. Budha | 6. Konghucu |")
Agama        = input("Agama         : ")

if    Agama == "1": Agama = "Islam" 
elif  Agama == "2": Agama = "Kristen"
elif  Agama == "3": Agama = "Katolik"
elif  Agama == "4": Agama = "Hindu"
elif  Agama == "5": Agama = "Budha"
elif  Agama == "6": Agama = "Konghucu"
else: Agama = "Tidak ada"

print()
print("======================================")
print("======== OUTPUT DATA DIRI ANDA =======")
print("Nama          : ", Nama)
print("Jenis Kelamin : ", JenisKelamin)
print("Agama         : ", Agama)



