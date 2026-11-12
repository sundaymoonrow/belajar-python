nama = "     buDi herman miller  "
kalimat = "Saya sedang belajar Menulis"
angka = "0123456789"
diksi = "Budi Pergi ke Pasar"


print(nama.upper()) # Mengubah semua karakter menjadi kapital
print(nama.lower()) # Mengubah semua karakter menjadi huruf kecil
print(nama.title()) # Mengubah huruf pertama setiap kata menjadi kapital
print(nama.strip()) # Menghilangkan whitespace di awal kata dan di akhir kata, tidak bisa diantara kata

kalimat = kalimat.replace("Menulis", "Python") # Mengubah kata pada variabel
print(kalimat)

angka = angka.replace("0", "+62") # Mengubah 0 menjadi +62
print(angka)

kalimat = "Saya belajar Python"
tanggal = "12-11-2000"

kata = ["Saya", "Belajar", "Python"]

kalimat = kalimat.split() # Memecah string per-kata menjadi beberapa bagian dan menghasilkan list
print(kalimat)

tanggal = tanggal.split("-") # Menghilangkan - di string
print(tanggal)

hasil = " ".join(kata) # Menggabungkan string dari iterable seperti list, " " berfungsi sebagai pemisah antar kata
print("-".join(kata))
print("".join(kata))
print(" ".join(kata))

print("Python" in kalimat) # In berfungsi untuk menampilkan apakah karakter itu ada pada variabel atau tidak
print("berak" in kalimat)

print(diksi.find("Pergi")) # Menghasilkan output 5 karena pergi dimulai dari index ke-5
print(diksi.find("Berak")) # Menghasilkan output -1 yang artinya tidak ditemukan

print(diksi.startswith("Budi")) # Mengecek apakah kalimat diawali dengan kata Budi atau tidak
print(diksi.startswith("Yanto"))