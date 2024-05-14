import random
import string

def generate_password(length):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt user for password length
    length = int(input("Enter the desired length of the password: "))

    # Generate password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
