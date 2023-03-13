print("Create an account:")
username=input("Enter the username: ")
if len(username)<6:
    print("Username should consist of minimum 6 letters..Try again..")
    username=input("Enter the username: ")
password=input("Enter the password: ")
if len(password)<6:
    print("Password should consist of minimum 6 letters..Try again..")
    password=input("Enter the password: ")
print("Account created successfully.Please login")
us1=input("Enter the username: ")
ps1=input("Enter the password: ")
if us1==username and ps1==password:
    print("You are logged in")
elif us1==username or ps1==password:
    print("Username or password is wrong")
else:
    print("Invalid credentials")
