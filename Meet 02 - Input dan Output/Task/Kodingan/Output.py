print('Ini adalah Output')


string = "Ini adalah variabel"
print(string)

# Metode +str
MakananA = "Nasi Goreng"
MakananB = "Mie Goreng"
MakananC = "Soto"
print('Andi Suka '+str(MakananA)+ 
      ', Bela suka '+str(MakananB)+
      ', Caca suka '+str(MakananC))

# Metode format
MakananA = "Nasi Goreng"
MakananB = "Mie Goreng"
MakananC = "Soto"
print('Andi Suka {}, Bela suka {}, Caca suka {}'
    .format(MakananA, MakananB, MakananC))

# Metode f string
MakananA = "Nasi Goreng"
MakananB = "Mie Goreng"
MakananC = "Soto"
print(f'Andi Suka {MakananA}, Bela suka {MakananB}, Caca suka {MakananC}')


# Fungsi koma(,)
panjang = 10
lebar = 5
luas = panjang * lebar
print('luasnya adalah', luas)