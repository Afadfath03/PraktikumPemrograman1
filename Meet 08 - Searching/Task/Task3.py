def showList(Array):
    for i in range(len(Array)):
        print(Array[i], end=' ')

def Bubble_Sort(Array):
    for i in range(len(Array)):
        for j in range(len(Array) - 1):
            if Array[j] > Array[j + 1]:
                Array[j], Array[j + 1] = Array[j + 1], Array[j]
    return Array
    
def Binary_Search(Array, Kata_Kunci):
    Left = 0
    Right = len(Array) - 1
    while Left <= Right:
        Mid = (Left + Right) // 2
        if Array[Mid] > Kata_Kunci:
            Right = Mid - 1
        elif Array[Mid] < Kata_Kunci:
            Left = Mid + 1
        else:
            print(f'\n\nAngka {Kata_Kunci} ditemukan pada index ke-{Mid}')
            return Mid
    
    print(f'\n\nAngka {Kata_Kunci} tidak ditemukan')

List_Angka = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]

Kata_Kunci = 72

print('Daftar Angka: ')
showList(List_Angka)

print(f'\n\nAngka yang dicari: {Kata_Kunci}')
print('\nSetelah Diurutkan : ')
showList(Bubble_Sort(List_Angka))
Binary_Search(Bubble_Sort(List_Angka), Kata_Kunci)