def LinearSearch(Data, Keyword):
    for i in range(len(Data)):
        if (str(Data[i]).lower() == Keyword.lower()):
            print(f'{Keyword} ditemukan pada index ke-{i}') 
            return i
    print(f'{Keyword} tidak ditemukan')
    return -1

# def BinarySearch(arrayList, x):
    left = 0
    right = len(arrayList) - 1
    mid = 0

    while left <= right:
        mid = (right + left) // 2

        if arrayList[mid] < x:
            left = mid + 1
        elif arrayList[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1

arrayList = [8, 2, 6, 4, 7, 9, 1, 3, 5]

print(f'Array: {arrayList}')
x = input("Masukan Data yang ingin dicari: ")
print(LinearSearch(arrayList, x))

