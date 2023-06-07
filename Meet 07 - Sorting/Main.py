import timeit

def bubble_ASC(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array
def bubble_DESC(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] < array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array

def insertion_ASC(array):
    for i in range(1, len(array)):
        indeks = array[i]
        j = i-1
        while j >= 0 and indeks < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = indeks
    return array
def insertion_DESC(array):
    for i in range(1, len(array)):
        indeks = array[i]
        j = i-1
        while j >= 0 and indeks > array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = indeks
    return array

def selection_ASC(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
def selection_DESC(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] > array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

array = [7, 4, 2, 5, 3, 9, 1, 6, 0, 8]
print("Array            : ", array)

print("Selection (ASC)  : ", selection_ASC(array))
print("Selection (DESC) : ", selection_DESC(array))

# print("Bubble (ASC)     : ", bubble_ASC(array))
# print("Bubble (DESC)    : ", bubble_DESC(array))

# print("Insertion (ASC) :", insertion_ASC(array))
# print("Insertion (DESC):", insertion_DESC(array))