print("INI ADALAH KALKULATOR OHM")
print("=========================\n")

pilihan = int(input("Pilih Operasi\n1.Tegangan (V) \n2.Arus Listrik (I) \n3.Hambatan (R)\nPilih (1-3) : "))


if pilihan == 1:
    input_i = float(input("\nMasukkan Arus Listrik (I) : "))
    input_r = float(input("Masukkan Hambatan (R) : "))
    
    hasil = input_i * input_r
    
    print(f"\nTegangan = {hasil} (V)")
    
elif pilihan == 2:
    input_v = float(input("\nMasukkan Tegangan (V) : "))
    input_r = float(input("Masukkan Hambatan (R) : "))

    if input_r == 0:
        print("Pembagi tidak boleh nol")        
    else:
        hasil = input_v / input_r
        
        print(f"\nArus Listrik = {hasil} (A)")
    
elif pilihan == 3:
    input_v = float(input("\nMasukkan Tegangan (V) : "))
    input_i = float(input("Masukkan Arus Listrik (I) : "))
    
    if input_i == 0:
        print("Pembagi tidak boleh nol")
    else:
        hasil = input_v / input_i
        
        print(f"\nHambatan = {hasil} (Ω)")

else:
    print("Masukkan angka...")