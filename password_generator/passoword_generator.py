import string
import secrets
import pyperclip

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def copy_password_to_clipboard(password):
    pyperclip.copy(password)

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)

print("Generated password:", password)

save_to_file = input("Do you want to save the password to a file? (y/n): ")
if save_to_file.lower() == 'y':
    save_password_to_file(password)
    print("Password saved to file.")

copy_to_clipboard = input("Do you want to copy the password to clipboard? (y/n): ")
if copy_to_clipboard.lower() == 'y':
    copy_password_to_clipboard(password)
    print("Password copied to clipboard.")
