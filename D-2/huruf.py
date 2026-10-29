angka = int(input("Masukkan angka (0-100): "))

if angka >= 85:
    print("Nilai A")
elif angka < 85 and angka >= 70:
    print("Nilai B")
elif angka < 70 and angka >= 55:
    print("Nilai C")
else:
    print("Nilai D")