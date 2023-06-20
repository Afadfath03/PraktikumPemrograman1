students = []

def create_student(nim, mahasiswa, gender):
    student = {
        "nim": nim,
        "mahasiswa": mahasiswa,
        "gender": gender
    }
    students.append(student)
    print(f"Mahasiswa dengan NIM {nim} telah ditambahkan.")

def read_students():
    if students:
        print("Daftar mahasiswa:")
        for student in students:
            print(f"NIM: {student['nim']}, Mahasiswa: {student['mahasiswa']}, Jenis Kelamin: {student['gender']}")
    else:
        print("Tidak ada mahasiswa yang ditemukan.")

def update_student(nim, mahasiswa, gender):
    for student in students:
        if student['nim'] == nim:
            student['mahasiswa'] = mahasiswa
            student['gender'] = gender
            print(f"Mahasiswa dengan NIM {nim} telah diperbarui.")
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

def delete_student(nim):
    for student in students:
        if student['nim'] == nim:
            students.remove(student)
            print(f"Mahasiswa dengan NIM {nim} telah dihapus.")
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

def search_student(nim):
    for student in students:
        if student['nim'] == nim:
            print(f"Mahasiswa dengan NIM {nim} ditemukan:")
            print(f"NIM: {student['nim']}, Mahasiswa: {student['mahasiswa']}, Jenis Kelamin: {student['gender']}")
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

def sort_students():
    n = len(students)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if students[j]['nim'] > students[j + 1]['nim']:
                students[j], students[j + 1] = students[j + 1], students[j]
    print("Mahasiswa diurutkan berdasarkan NIM.")

while True:
    print("\nPilih operasi yang diinginkan:")
    print("1. Tambah mahasiswa")
    print("2. Baca semua mahasiswa")
    print("3. Perbarui data mahasiswa")
    print("4. Hapus mahasiswa")
    print("5. Cari mahasiswa")
    print("6. Urutkan mahasiswa berdasarkan NIM")
    print("7. Keluar")

    choice = input("Masukkan pilihan Anda (1-7): ")

    if choice == '1':
        nim = int(input("Masukkan NIM: "))
        mahasiswa = input("Masukkan Nama Mahasiswa: ")
        gender = input("Masukkan Jenis Kelamin: ")
        create_student(nim, mahasiswa, gender)

    elif choice == '2':
        read_students()

    elif choice == '3':
        nim = int(input("Masukkan NIM mahasiswa yang akan diperbarui: "))
        mahasiswa = input("Masukkan Nama Mahasiswa baru: ")
        gender = input("Masukkan Jenis Kelamin baru: ")
        update_student(nim, mahasiswa, gender)

    elif choice == '4':
        nim = int(input("Masukkan NIM mahasiswa yang akan dihapus: "))
        delete_student(nim)

    elif choice == '5':
        nim = int(input("Masukkan NIM mahasiswa yang akan dicari: "))
        search_student(nim)

    elif choice == '6':
        sort_students()

    elif choice == '7':
        print("Program keluar.")
        break

    else:
        print("Pilihan tidak valid. Program keluar.")
        break