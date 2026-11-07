def hitung_v(i, r):
    return i * r

def hitung_i(v, r):
    if r == 0:
        return None
    else:
        return v / r

def hitung_r(v, i):
    if i == 0:
        return None
    else:
        return v / i

pilihan = int(input("Pilih Operasi\n1.Tegangan (V) \n2.Arus Listrik (I) \n3.Hambatan (R)\nPilih (1-3) : "))

if pilihan == 1:
    i = float(input("Masukkan arus (I): "))
    r = float(input("Masukkan hambatan (R): "))
    hasil = hitung_v(i, r)
    print(f"Tegangan = {hasil} V")

elif pilihan == 2:
    v = float(input("Masukkan tegangan (V): "))
    r = float(input("Masukkan hambatan (R): "))
    hasil = hitung_i(v, r)
    if hasil is None:
        print("Hambatan tidak boleh nol.")
    else:
        print(f"Arus = {hasil} A")

elif pilihan == 3:
    v = float(input("Masukkan tegangan (V): "))
    i = float(input("Masukkan arus (i): "))
    hasil = hitung_r(v, i)
    if hasil is None:
        print("Arus tidak boleh nol.")
    else:
        print(f"Hambatan = {hasil} Ω")

else:
    print("Input tidak valid.")