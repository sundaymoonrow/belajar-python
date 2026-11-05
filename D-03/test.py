words = ['budi', 'messi', 'ronaldo', 'haaland']
for w in words:
    print(w, len(w)) # Ini adalah for untuk menghitung jumlah karakter pada setiap kata dalam list 'words'

users = {'Messi': 'Inactive', 'Ronaldo': 'Active', 'Haaland': 'Active'}
for user, status in users.copy().items():
    if status == 'Inactive':
        del users[user] # Ini adalah for untuk menghapus user yang statusnya inactive

active_users = {}
for user, status in users.items():
    if status == 'Active':
        active_users[user] = status # Ini adalah for untuk menambahkan user yang active ke dalam dict 'activ_users'

print("Active users:", active_users)

for i in range(0, 10, 3):
    print(i) # Ini adalah for untuk mencetak angka dari 0 sampai 9 dengan kelipatan 3 (0, 3, 6, 9)

for i in range(5, 10):
    print(i) # Ini adalah for untuk mencetak angka dari 5 sampai 9

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

for num in range(2,10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

spam = 0
while spam < 5:
    print('Hello, world.')
    spam += 1

name = ''
while name != 'budi':
    print('Please type your name.')
    name = input()
print('Thank you!')

while True:
    print("Who are you?")
    name = input('>')
    if name != 'Budi':
        continue
    print("Hello, budi. What is the password? (It is a fish.)")
    password = input('>')

    if password == 'lele':
        break
    
print("Access granted.")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

angka = 0
while angka < 1000:
    angka += 1
    print(angka)

for i in range(1, 6):
    print('*' * i)
