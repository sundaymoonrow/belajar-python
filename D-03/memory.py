print("Ini kalkulator OHM")

pilihan = int(input("Pilih jenis perhitungan (1. Tegangan, 2. Arus, 3. Hambatan): "))

if pilihan == 1:
    arus = float(input("Masukkan nilai arus (A): "))
    hambatan = float(input("Masukkan nilai hambatan (Ω): "))

    tegangan = arus * hambatan
    print(f"Tegangan (V) = {tegangan} Volt")

elif pilihan == 2:
    tegangan = float(input("Masukkan nilai tegangan (V): "))
    hambatan = float(input("Masukkan nilai hambatan (Ω): "))

    if hambatan == 0:
        print("Hambatan tidak boleh nol.")
    else:
        arus = tegangan / hambatan
        print(f"Arus (A) = {arus} Ampere")

elif pilihan == 3:
    tegangan = float(input("Masukkan nilai tegangan (V): "))
    arus = float(input("Masukkan nilai arus (A): "))

    if arus == 0:
        print("Arus tidak boleh nol.")
    else:
        hambatan = tegangan / arus
        print(f"Hambtan (Ω) = {hambatan} Ohm")

else:
    print("Pilihan tidak valid. Silakan ulangi...")