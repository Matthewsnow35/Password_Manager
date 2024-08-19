from cryptography.fernet import Fernet
import os

# Path to the file where the encryption key will be stored
KEY_FILE = "secret.key"

# Function to load the key from a file, or generate and save it if it doesn't exist
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            key = file.read()
        return key
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
        return key

# Load or generate the encryption key
key = load_key()
cipher_suite = Fernet(key)

# Dictionary to store passwords with their associated service names
passwords = {}

def encrypt_password(password):
    """Encrypts a password using the cipher suite."""
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    """Decrypts a password using the cipher suite."""
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

def add_password():
    """Function to allow users to add a new password."""
    service = input("Enter the name of the service (e.g., Gmail, Facebook): ")
    username = input("Enter your username or email: ")
    password = input("Enter your password: ")

    # Encrypts the password before storing it
    encrypted_password = encrypt_password(password)

    # Stores the encrypted password in the dictionary with the service as the key
    passwords[service] = {"username": username, "password": encrypted_password}

    print(f"Password for {service} added successfully!\n")

def view_passwords():
    """Function checks if there are any passwords stored and displays them."""
    if not passwords:
        print("No passwords stored yet.\n")
        return

    print("Stored Passwords:")
    for service, details in passwords.items():
        decrypted_password = decrypt_password(details['password'])
        print(f"Service: {service}")
        print(f"  Username/Email: {details['username']}")
        print(f"  Password: {decrypted_password}")
        print()  # Prints a new line for better readability

def delete_password():
    """Function to delete a stored password."""
    view_passwords()

    if not passwords:
        return

    service = input("Enter the name of the service for the password you want to delete: ")

    if service in passwords:
        del passwords[service]
        print(f"Password for {service} deleted successfully.\n")
    else:
        print("No password found for the specified service.\n")

def save_passwords():
    """Function to save passwords to a file."""
    with open("passwords.txt", "w") as file:
        for service, details in passwords.items():
            file.write(f"{service},{details['username']},{details['password']}\n")
    print("Passwords saved successfully.")

def load_passwords():
    """Function to load passwords from a file."""
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                service, username, encrypted_password = line.strip().split(",", 2)
                passwords[service] = {"username": username, "password": encrypted_password}
        print("Passwords loaded successfully.")
    except FileNotFoundError:
        print("No saved passwords found. Starting with an empty list.")

def main():
    load_passwords()  # Load passwords when the program starts

    while True:
        print("Password Manager")
        print("1. Add a New Password")
        print("2. View Stored Passwords")
        print("3. Delete a Password")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            save_passwords()  # Save passwords when the program exits
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()