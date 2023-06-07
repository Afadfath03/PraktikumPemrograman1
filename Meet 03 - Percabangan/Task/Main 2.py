# Panggilan berdasarkan status

gender = input("Masukkan jenis kelamin anda! (L/P) : ")
status = input("Apakah Anda sudah Menikah? (Y/N)   : ")

if gender == "L" or "l":
    if status == "y" or "Y":
        print("Hallo, Bapak!")
    elif status == "n" or "N":
        print("Hallo, Mas!")
    else:
        print("Maaf, pilihan tidak ada!")
else:
    if status == "y" or "Y":
        print("Hallo, Ibu!")
    elif status == "n" or "N":
        print("Hallo, Mbak!")
    else:
        print("Maaf, pilihan tidak ada!")
        
        

