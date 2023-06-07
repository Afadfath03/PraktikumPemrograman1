Array = []

jmhElemen = int(input("Masukkan jumlah mata kuliah : "))
for i in range(jmhElemen):
    kata = input(f"Masukkan nilai mata kuliah ke-{i+1} : ")
    Array.append(kata)

print()

total = 0
for i in range(len(Array)):
    total += int(Array[i])
    rerata = total / len(Array)

    if int(Array[i-1]) > 100 or int(Array[i-1]) < 0:
        print("Nilai Tidak Valid")
        exit()

if 90 <= rerata <= 100:
    predikat = "A"
elif rerata >= 70:
    predikat = "B"
elif rerata >= 50:
    predikat = "C"
elif rerata >= 30:
    predikat = "D"
else:
    predikat = "E"

print(f"Hasil predikat {predikat} dengan nilai : ")
for i in range(len(Array)):
    print(f"Mata kuliah ke-{i}  : {Array[i]}")