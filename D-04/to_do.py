tugas = []
selesai = False

while True:
    pilihan = int(input("Masukkan pilihan \n1. Tambah tugas\n2. Lihat tugas\n3. Selesaikan tugas\n4. Hapus tugas\n5. Keluar\n> "))

    if pilihan == 1:
        tugas_baru = input("\nMasukkan tugas baru: ")
        tugas.append({"tugas": tugas_baru, "selesai": False})
        print("Tugas berhasil ditambahkan.\n")
        
    elif pilihan == 2:
        print("\nDaftar tugas:")
        for i in range(len(tugas)):
            print(f"{i + 1}. {tugas[i]['tugas']} - Status: {'Selesai' if tugas[i]['selesai'] else 'Belum selesai'}")

    elif pilihan == 3:
        nomor_tugas = int(input("\nMasukkan nomor tugas yang ingin diselesaikan: "))
        if 1 <= nomor_tugas <= len(tugas):
            tugas[nomor_tugas - 1]['selesai'] = True
            print("Tugas berhasil diselesaikan.")
        else:
            print("Nomor tugas tidak valid.")

    elif pilihan == 4:
        nomor_tugas = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor_tugas <= len(tugas):
            del tugas[nomor_tugas - 1]
            print("Tugas berhasil dihapus.\n")
        else:
            print("Nomor tugas tidak valid.")
    elif pilihan == 5:
        print("Terima kasih telah menggunakan aplikasi ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
