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
            if (str(Data[j]).lower() > str(Data[j + 1]).lower()):
                Data[j], Data[j + 1] = Data[j + 1], Data[j]
    return Data

def BinarySearch(Data, Keyword):
    BubbleSort(Data)
    low = 0
    high = len(Data) - 1
    while low <= high:
        mid = (low + high) // 2
        if str(Data[mid]).lower() > Keyword.lower():
            high = mid - 1
        elif str(Data[mid]).lower() < Keyword.lower():
            low = mid + 1
        else:
            print(f'{Keyword} ditemukan pada index ke-{mid} setelah diurutkan')
            return mid
    
    print(f'{Keyword} tidak ditemukan')
    return -1

arrayList = [23, 3, 4, 78, 9, 32]

print(f'Array: {arrayList}')
x = input("Masukan Data yang ingin dicari:")
print()
# LinearSearch(arrayList, x)
BinarySearch(arrayList, x)