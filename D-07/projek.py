nama = input("Masukkan nama : ")

nama = nama.strip()
nama = nama.split()
nama_rapi = " ".join(nama).title()
inisial = ".".join(n[0].upper() for n in nama) + "."

print(nama_rapi)
print(inisial)