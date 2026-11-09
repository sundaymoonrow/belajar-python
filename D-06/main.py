import os

file = "pengeluaran.txt"

def muat_data():
    data = []
    if os.path.exists(file):
        with open(file, "r") as f:
            for baris in f:
                    baris = baris.strip()
                    bagian = baris.split("|")
                    pengeluaran = {"tanggal": bagian[0], "keterangan": bagian[1], "jumlah": int(bagian[2])}
                    data.append(pengeluaran)

    return data

def simpan_data(data):
     with open(file, "w") as f:
          for item in data:
               baris = f"{item['tanggal']}|{item['keterangan']}|{item['jumlah']}\n"
               f.write(baris)

data = muat_data()

while True:
    print("=== PENCATAT KEUANGAN ===")
    print("Menu:\n1. Tambah Pengeluaran\n2. Lihat Pengeluaran\n3. Keluar")
    pilihan = int(input("> "))

    if pilihan == 1:
        tanggal = input("Tanggal (2026-01-01): ")
        keterangan = input("Keterangan (Topup Diamond): ")
        jumlah = int(input("Jumlah/Harga (20000): "))

        pengeluaran = {"tanggal": tanggal, "keterangan": keterangan, "jumlah": jumlah}
        data.append(pengeluaran)
        simpan_data(data)

        print("\n- Pengeluaran berhasil disimpan -\n")

    elif pilihan == 2:
        print("\n--- Pengeluaran kamu ---")

        if len(data) == 0:
             print("Belum ada pengeluaran.")

        else:
            total = 0
            for nomor, item in enumerate(data, start=1):
                print(f"{nomor}. {item['tanggal']} | {item['keterangan']} | Rp {item['jumlah']}")
                total = total + item['jumlah']

            print(f"Total: Rp {total}\n")
    elif pilihan == 3:
        print("Terimakasih sudah berinteraksi.")
        break

    else:
        print("Input tidak valid")