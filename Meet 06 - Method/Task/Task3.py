def PilihanOperasi():
    print("Pilih operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Pangkat (**)")
    print()
    pilihan = input("Masukkan pilihan (1-5) : ")

    try:
        pilihan = int(pilihan)
    except ValueError:
        print("Tidak valid")
        print()
        return None

    if pilihan == 1:
        return '+'
    elif pilihan == 2:
        return '-'
    elif pilihan == 3:
        return '*'
    elif pilihan == 4:
        return '/'
    elif pilihan == 5:
        return '**'
    else:
        print("Tidak valid")
        print()
        return None

def calculate(operasi, angka1, angka2):
    if operasi == '+':
        return angka1 + angka2
    elif operasi == '-':
        return angka1 - angka2
    elif operasi == '*':
        return angka1 * angka2
    elif operasi == '/':
        if angka2 == 0:
            print("Tidak bisa dibagi dengan nol")
            return None
        else:
            return angka1 / angka2
    elif operasi == '**':
        return angka1 ** angka2
    else:
        print("Operasi tidak valid")
        return None

def Ulang():
    ulang = input("Apakah Anda ingin mengulang? (y/n) : ")
    if ulang == 'y':
        print()
        return True
    elif ulang == 'n':
        print("Program Dihentikan")
        print()
        exit()
    else:
        print("Input Tidak valid, Program Dihentikan")
        print()
        exit()

while True:
    print("=" * 30)
    print("Kalkulator Sederhana")
    print("=" * 30)

    operasi = PilihanOperasi()
    if operasi is None:
        Ulang()

    if operasi == '**':
        angka1 = input("Masukkan angka dasar    : ")
        angka2 = input("Masukkan angka pangkat  : ")
    else:
        angka1 = input("Masukkan angka Pertama : ")
        angka2 = input("Masukkan angka Kedua   : ")

    try:
        angka2, angka1 = int(angka2), int(angka1)
    except ValueError:
        print("Tidak valid")
        print()
        continue

    hasil = calculate(operasi, angka1, angka2)

    if hasil is not None:
        print(f"{angka1} {operasi} {angka2} = {hasil}")
        print()

    Ulang()