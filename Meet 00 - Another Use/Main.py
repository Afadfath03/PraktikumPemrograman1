Array = [{"Nama": "Afad", "Umur": 19}]

def read(Array):
    for i in Array:
        print("Nama :", i["Nama"])
        print("Umur :", i["Umur"])

print(read(Array))