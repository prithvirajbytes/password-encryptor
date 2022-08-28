import bcrypt
def encrypt():
    password = str(input("input password: "))
    # Encode password into a readable utf-8 byte code:
    password = password.encode('utf-8')
    # Hash the encoded password and generate a salt:
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    print(hashedPassword)

def check():
    password = str(input("input password: "))
    # Encode the stored password:
    password = password.encode('utf-8')
    # Encrypt the stored pasword:
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    # Create an authenticating password input field to check if a user enters the correct password:
    check = str(input("check password: "))
    # Encode the authenticating password as well:
    check = check.encode('utf-8')
    # Use conditions to compare the authenticating password with the stored one:
    if bcrypt.checkpw(check, hashed):
        print("login success")
    else:
        print("incorrect password")
def main():
    print("choose \n1.Enrypt your password \n2.Check the authentiic")
    choice = int(input("Enter choice"))
    if choice == 1:
        encrypt()
    elif choice == 2:
        check()

main()





