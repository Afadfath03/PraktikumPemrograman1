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
                temp = Data[j]
                Data[j] = Data[j + 1]
                Data[j + 1] = temp
    return Data

def BinarySearch(Data, Keyword):
    BubbleSort(Data)
    print(f'Array setelah diurutkan: {Data}')
    
    low = 0
    high = len(Data) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if str(Data[mid]).lower() > Keyword.lower():
            high = mid - 1
        elif str(Data[mid]).lower() < Keyword.lower():
            low = mid + 1
        else:
            print(f'{Keyword} ditemukan pada index ke-{mid}')
            return mid
        
    print(f'{Keyword} tidak ditemukan')
    return -1

arrayList = [8, 2, 6, 4, 7, 9, 1, 3, 5]

print(f'Array: {arrayList}')
x = input("Masukan Data yang ingin dicari: ")
print(LinearSearch(arrayList, x))
print(BinarySearch(arrayList, x))