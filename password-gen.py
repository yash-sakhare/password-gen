import random
import string

print("=" * 50)
print("         PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("Enter the desired password length (minimum 4): "))

        if length < 4:
            print("Password length should be at least 4.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

print("\nSelect Password Complexity:")
print("1. Letters Only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Special Characters")

choice = input("Enter your choice (1-3): ")

letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

if choice == "1":
    characters = letters
elif choice == "2":
    characters = letters + numbers
elif choice == "3":
    characters = letters + numbers + special
else:
    print("Invalid choice! Defaulting to Letters + Numbers + Special Characters.")
    characters = letters + numbers + special

password = "".join(random.choice(characters) for _ in range(length))

print("\n" + "=" * 50)
print("Generated Password:")
print(password)
print("=" * 50)
