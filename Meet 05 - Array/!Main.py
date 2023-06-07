# Array
x_1 = [1, 2, 3, 4, 5]
x_2 = {["Satu", "Dua"],
       ["Tiga", "Empat"], 
       ["Lima"]}

def array_print(array):
    for index in array:
        print(index, end=" ")
    print()

def arary_2d_print(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print()

def array_append(array):
    x = int(input("Masukkan jumlah array: "))
    for i in range(x):
        array.append(input("Masukkan nilai: "))
    array_print(array)

def array_replace(array):
    x = int(input("Masukkan index yang ingin diganti: "))
    array[x] = input("Masukkan nilai baru: ")
    array_print(array)
    
def array_delete(array):
    x = input("Masukkan index yang ingin dihapus: ")
    # Cara 1
    array.pop(int(x))
    # Cara 2
    # array.remove(x)
    array_print(array)

""" 
# print("Array =", x_1)

# Print Array
array_print(x_1)
array_print(x_2)

# Append Array
array_append(x_1)

# Replace Array
array_replace(x_1) 

# Delete Array
array_delete(x_1)
"""

print(f"Array = {x_2}")
arary_2d_print(x_2)