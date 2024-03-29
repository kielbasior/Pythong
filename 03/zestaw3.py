
def menu():
    while True:
     try:
        option = int(input("1. Password strength test\n 2. Password encryption \n 3. Password decryption\n Choose an option: "))
        break
     except ValueError:
        print("The char you have provided is not an integer. Try again.")
    if option == 1:
        ocena_hasla()
    elif option == 2:
        pass_encryption()
    elif option == 3:
        pass_decryption()



def ocena_hasla():
    haslo = input("Enter your password: ")
    specials = ";!@#$%^&*()-+?_=,<>\""
    points = 0
    if len(haslo) >= 10 and len(haslo) < 15:
        points += 1
    elif len(haslo) >= 15:
        points += 2
    elif len(haslo) >= 20:
        points += 3
    if any(z in specials for z in haslo):
        points += 1
    if any(letter.isupper() for letter in haslo):
        points += 1
    if any(letter.isnumeric() for letter in haslo):
        points += 1

    if points == 0 or points == 1 or len(haslo) <= 8:
        pass_grade = "Weak"
    elif points == 2 or points == 3:
        pass_grade = "Medium"
    elif points == 4:
        pass_grade = "Decent"
    else:
        pass_grade = "Strong"
    print(pass_grade)

def pass_encryption():
    haslo = input("Enter your password: ")
    code = ""
    ces1 = ""
    ces3 = ""
    for letter in haslo:
        ces1 += str(ord(letter)+3) + " "
    ces2 = ces1.split()
    for letter in ces2:
        ces3 += chr(int(letter))

    for letter in haslo:
        code += str(ord(letter)) + " "
    encrypted_pass = code[::-1]
    print("Encrypted password: " + encrypted_pass)
    print("Secret code that you'll need to decrypt your password: " + ces3)

def pass_decryption():
        secret_code = input("Enter the secret sentence: ")
        unicode = ""
        for x in secret_code:
            unicode += str(ord(x)-3) + " "
        code = input("Enter your code: ")
        code = code[::-1]
        if str(unicode.strip()) == str(code):
            code_as_list = code.split()
            password = ""
            for x in code_as_list:
                password += chr(int(x))
            print("Decrypted password: " + password)
        else:
              print("Secret code doesn't match with password that you've provided.")

menu()