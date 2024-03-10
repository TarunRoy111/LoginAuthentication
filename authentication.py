
import hashlib
#Login Authentication

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()


    with open("users.txt", "a") as file:
        file.write(f"{username},{hashed_password}\n")

    print("Registration successful!")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")


    hashed_password = hashlib.sha256(password.encode()).hexdigest()


    with open("users.txt", "r") as file:
        for line in file:
            user, pw = line.strip().split(",")
            if user == username and pw == hashed_password:
                print("Login successful!")
                return True

    print("Invalid username or password.")
    return False

def secured_page():
    print("Welcome to the secured page!")
    print("You have successfully logged in.")
    print("Here's some exclusive content:")
    print("-" * 30)
    print("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    print("Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    print("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    print("-" * 30)


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                secured_page()
                break
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()