def Linear_Search(ArrayList, Keyword):
    for i in range(len(ArrayList)):
        if ArrayList[i] == Keyword:
            print(f'{Keyword} ditemukan pada index ke-{i}')
    print('Plat Nomor tidak ditemukan')

ListPlat = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", 
         "R 3304 DA", "R 2401 SK", "R 2103 RT", "R 1708 RI", 
         "R 1111 SR", "R 4987 LH"]

Kata_Kunci = "R 2488 SR"

print(f'Daftar Plat Nomor: ')
for i in range(len(ListPlat)):
    print(f'{i}. {ListPlat[i]}')

print(f'\nPlat Nomor yang dicari: {Kata_Kunci}')
Linear_Search(ListPlat, Kata_Kunci)