user_email = input("Enter your email: ")
password = input("Enter your password: ")
if user_email == "abcd123@gmail.com" and password == "123456":
    print("Login successful!")
elif user_email == "abcd123@gmail.com" and password != "123456":
    password = input("Enter your password again: ")
    if password == "123456":
        print("der aaye durust aaye")
    else:
        print("tumse nahi hoga")