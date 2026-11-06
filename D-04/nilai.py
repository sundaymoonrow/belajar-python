nilai = {"Budi": 80, "Siti": 90, "Joko": 50, "Ani": 85}

for nama, n in nilai.items():
    if n >= 85:
        print(f"{nama} mendapat nilai A")
    elif n >= 70:
        print(f"{nama} mendapat nilai B")
    else:
        print(f"{nama} mendapat nilai C")