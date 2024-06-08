import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(password_length))
