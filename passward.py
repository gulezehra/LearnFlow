import os
import json
import random
import string
from cryptography.fernet import Fernet

# Naya encryption key generate karna
def generate_key():
    return Fernet.generate_key()

# File se encryption key load karna
def load_key():
    with open("encryption_keyfile.key", "rb") as file:
        return file.read()

# Encryption key ko file mein likhna
def write_key(key):
    with open("encryption_keyfile.key", "wb") as file:
        file.write(key)

# Password ko encrypt karna given key ke sath
def encrypt_password(password, key):
    fernet_instance = Fernet(key)
    return fernet_instance.encrypt(password.encode())

# Encrypt password ko decrypt karna using key
def decrypt_password(encrypted_password, key):
    fernet_instance = Fernet(key)
    return fernet_instance.decrypt(encrypted_password).decode()

# Strong aur random password generate karna specific length ke liye
def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Password ko securely store karna JSON file ke andar
def save_password(service_name, password, category):
    if os.path.exists("password_vault.json"):
        with open("password_vault.json", "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}

    if category not in passwords:
        passwords[category] = {}

    encrypted_password = encrypt_password(password, load_key())
    passwords[category][service_name] = encrypted_password.decode()

    with open("password_vault.json", "w") as file:
        json.dump(passwords, file)

# Stored password ko retrieve karna service aur category ke according
def retrieve_password(service_name, category):
    if os.path.exists("password_vault.json"):
        with open("password_vault.json", "r") as file:
            passwords = json.load(file)
    else:
        return "No password data available."

    try:
        encrypted_password = passwords[category][service_name].encode()
        return decrypt_password(encrypted_password, load_key())
    except KeyError:
        return "No password found for this service."

# Password manager ka main function jisme user interaction hoti hai
def password_manager():
    # Agar key file exist nahi karti to nayi key generate karo
    if not os.path.exists("encryption_keyfile.key"):
        key = generate_key()
        write_key(key)

    while True:
        print("\nActions:")
        print("1. Generate a New Password")
        print("2. Save a Password")
        print("3. Fetch a Password")
        print("4. Exit")
        user_input = input("Select an action: ")

        if user_input == '1':
            new_password = generate_random_password()
            print(f"Generated Password: {new_password}")

        elif user_input == '2':
            service = input("Enter service name: ")
            password = input("Enter password (or leave blank to generate): ")
            if not password:
                password = generate_random_password()
            category = input("Enter a category: ")
            save_password(service, password, category)
            print("Password saved securely.")

        elif user_input == '3':
            service = input("Enter service name: ")
            category = input("Enter category: ")
            fetched_password = retrieve_password(service, category)
            print(f"Retrieved Password: {fetched_password}")

        elif user_input == '4':
            print("Exiting Password Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    password_manager()
