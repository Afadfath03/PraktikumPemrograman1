""" def LuasPersegi(s):
    print("Luas persegi     : ", s * s)   

def KelilingPersegi(s):
    print("Keliling persegi : ", 4 * s)

sisi = int(input("Masukkan panjang sisi persegi: "))
KelilingPersegi(sisi)
LuasPersegi(sisi) """

def Bandingkan(a, b):
    if a > b:
        print("Nilai terbesar adalah: ", a)
    else:
        print("Nilai terbesar adalah: ", b)
    
a = int(input("Masukkan Bilangan 1 : "))
b = int(input("Masukkan Bilangan 2 : "))
Bandingkan(a, b)