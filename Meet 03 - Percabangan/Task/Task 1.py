# Task 1 - Menentukan Huruf Vokal atau Konsonan

huruf = input("Masukkan huruf: ")

if huruf == "":
    print("Anda belum memasukkan huruf")    
elif huruf in "aiueoAIUEO":
    print("Huruf", huruf, "adalah huruf Vokal")
elif huruf in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
    print("Huruf", huruf, "adalah huruf Konsonan")
else:
    print(huruf, "Bukan huruf")
    


