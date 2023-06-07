# Hitung Volume Kubus
print("*** Hitung Volume Kubus  ***")
sisi = int(input("Masukan nilai sisi kubus : "))
volKubus = sisi * sisi * sisi
print("Volume Kubus : ", volKubus)
print()

# Hitung Volume Balok
print("*** Hitung Volume Balok  ***")
panjang = int(input("Masukan nilai panjang balok : "))
lebar   = int(input("Masukan nilai lebar balok   : "))
tinggi  = int(input("Masukan nilai tinggi balok  : "))
volBalok = panjang * lebar * tinggi
print("Volume Balok : ", volBalok)
print()

# Hitung Volume Tabung
print("*** Hitung Volume Tabung  ***")
phi     = 3.14
r       = int(input("Masukan nilai jari-jari tabung : "))
tinggi  = int(input("Masukan nilai tinggi tabung    : "))
volTabung = phi * r * r * tinggi
print("Volume Tabung : ", volTabung)
print()

# Hitung Volume Bola
print("*** Hitung Volume Bola  ***")
phi = 3.14
r = int(input("Masukan nilai jari-jari bola : "))
volBola = 4/3 * phi * r * r * r
print("Volume Bola : ", volBola)
print()