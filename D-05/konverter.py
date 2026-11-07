def c_ke_f(c):
    return (9/5 * c) + 32

def c_ke_r(c):
    return 4/5 * c

def c_ke_k(c):
    return c + 273.15

while True:
    print("Konverter Satuan Celcius ke Suhu Lain.")
    print("Pilih menu:\n1. C ke F\n2. C ke R\n3. C ke K\n4. Keluar")
    pilihan = int(input(">"))

    if pilihan == 1:
        c = float(input("Masukkan suhu: "))
        hasil = c_ke_f(c)
        print(f"hasil = {hasil} F\n")

    elif pilihan == 2:
        c = float(input("Masukkan suhu: "))
        hasil = c_ke_r(c)
        print(f"hasil = {hasil} R\n")

    elif pilihan == 3:
        c = float(input("Masukkan suhu: "))
        hasil = c_ke_k(c)
        print(f"hasil = {hasil} K\n")

    elif pilihan == 4:
        print("Terima kasih.")
        break
    else:
        print("Input tidak valid")
        break
    