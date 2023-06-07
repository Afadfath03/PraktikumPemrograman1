# TASK 2 - Validasi Nilai Pembagi

bilangan = int(input("Masukkan bilangan utama   : "))
pembagi  = int(input("Masukkan bilangan pembagi : "))

if (pembagi == 0):
    print("Bilangan pembagi tidak boleh nol")
else:
    hasil = bilangan / pembagi
    print("Hasil bagi adalah", hasil)