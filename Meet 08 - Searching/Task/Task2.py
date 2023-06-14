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
            print(f'\n\nNIM {Kata_Kunci} ditemukan pada index ke-{Mid}')
            return Mid
    
    print(f'\n\nNIM {Kata_Kunci} tidak ditemukan')

List_NIM = [20103023, 20103002, 20103019, 20103001, 20103017, 
           20103005, 20103011, 20103003, 20103009, 20103021, 
           20103006, 20103015, 20103013, 20103007]

Kata_Kunci = 20103015

print('Daftar NIM: ')
showList(List_NIM)

print(f'\n\nNIM yang dicari: {Kata_Kunci}')
print('\nSetelah Diurutkan : ')
showList(Bubble_Sort(List_NIM))
Binary_Search(Bubble_Sort(List_NIM), Kata_Kunci)