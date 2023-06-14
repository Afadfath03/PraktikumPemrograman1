def LinearSearch(Data, Keyword):
    for i in range(len(Data)):
        if (str(Data[i]).lower() == Keyword.lower()):
            print(f'{Keyword} ditemukan pada index ke-{i}') 
            return i
    print(f'{Keyword} tidak ditemukan')
    return -1

def BubbleSort(Data):
    for i in range(len(Data)):
        for j in range(len(Data) - 1):
            if Data[j] > Data[j + 1]:
                Data[j], Data[j + 1] = Data[j + 1], Data[j]
    print(Data)
    return Data

def BinarySearch(Data, Keyword):
    Left = 0
    Right = len(Data) - 1
    while Left <= Right:
        Mid = (Left + Right) // 2
        if Data[Mid] > Keyword:
            Right = Mid - 1
        elif Data[Mid] < Keyword:
            Left = Mid + 1
        else:
            print(f'{Keyword} ditemukan pada index ke-{Mid}')
            return Mid
    
    print(f'{Keyword} tidak ditemukan')
    return -1

arrayList = [23, 3, 4, 78, 9, 32]

print(f'Array: {arrayList}')
x = input("Masukan Data yang ingin dicari: ")

Data = BubbleSort(arrayList)
BinarySearch(Data, int(x))

# LinearSearch(arrayList, x)