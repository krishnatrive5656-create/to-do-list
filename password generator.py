

# This is a simple password generator using random letters, numbers, and symbols.

import random

print("Welcome to Password Generator!")

# Ask user for desired password length
length_input = input("How long should the password be? ")

# check if input is a no
if length_input.isdigit():
    password_length = int(length_input)
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=<>?/"

    all_chars = letters + numbers + symbols
    password = ""

    for i in range(password_length):
        password += random.choice(all_chars)

    print("\nYour new password is:")
    print(password)
else:
    print("Please enter a valid number for password length.")
