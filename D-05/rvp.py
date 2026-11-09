def tambah_print(a, b):
    print(a + b)

def tambah_return(a, b):
    return a + b

x = tambah_print(2,3)
y = tambah_return(2,3)

print(x) # Hasilnya None
print(y) # Hasilnya 5
print(tambah_return(2, 3) * 10) # Hasilnya 50