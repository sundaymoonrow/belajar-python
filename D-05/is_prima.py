def is_prima(n):
    if n < 2:
        return False
    for pembagi in range(2, n):
        if n % pembagi == 0:
            return False
    return True

def faktorial(n):
    hasil = 1
    for angka in range(1, n + 1):
        hasil = hasil * angka
    return hasil
hasil = faktorial(4)
print(hasil)