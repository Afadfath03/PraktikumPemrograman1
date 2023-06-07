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

array = [7, 4, 8, 2, 9, 5, 4, 3, 9, 1, 6, 0]
print("Array     :", array)

print("Insertion :", insertion_ASC(array))
print("Bubble    :", bubble_ASC(array))
print("Selection :", selection_ASC(array))