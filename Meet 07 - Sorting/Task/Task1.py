# Program mengurutkan IPS mahasiswa dari yang terbesar ke terkecil

def Bubble_DESC(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] < array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array

IPS = [3.8, 2.9, 3.3, 4.0, 2.7]

print("Indeks Prestasi Mahasiswa (IPS)")
print("List Sebelum Diurutkan :", IPS)
print("List Setelah Diurutkan :", Bubble_DESC(IPS))