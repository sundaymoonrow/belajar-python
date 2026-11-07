def sapa(nama):
    print("Halo,", nama)

sapa("Budi")

def kuadrat(x):
    return x * x

hasil = kuadrat(3)
print(hasil)

def pangkat(angka, pangkat=2):
    return angka ** pangkat

print(pangkat(3)) # Hasilnya 9
print(pangkat(3, 3)) # Hasilnya 27
print(pangkat(pangkat=4, angka=2)) # Hasilnya 16