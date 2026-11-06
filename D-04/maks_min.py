numlist = [4, 8, 15, 16, 23, 42]
terbesar = numlist[0]
terkecil = numlist[0]

for n in numlist:
    if n > terbesar:
        terbesar = n
    elif n < terkecil:
        terkecil = n

avg = sum(numlist) / len(numlist)
print(terbesar, terkecil, avg)
