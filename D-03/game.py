
import random

number = random.randint(1, 100)

for guesses_taken in range (1, 7):
    guess = int(input("Tebak angka 1 - 100: "))

    if guess < number:
        print("Tebakan terlalu kecil.")
    elif guess > number:
        print("Tebakan terlalu besar.")
    elif guess == number:
        print(f"Selamat! Tebakan anda benar, angkanya adalah {number}.")
        break
    if guesses_taken == 6:
        print(f"Maaf, tebakan anda salah. Angkanya adalah {number}.")
