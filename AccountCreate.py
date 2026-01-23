print("======== Create your Account =======")
print("           ")
print("Let's Start")

#-----------Username------------

Username = input("Enter Your Name :")
Username_valid = True

#Rule:1 Username Name lenth 5 to 15

if len(Username)<5 or len(Username)>15 :
    print("Username must be 5 to 15 letters")
    Username_valid = False

#Rule:2 Username First Letter
if not Username[0].isalpha():
    print("Username must Start With Letter")
    Username_valid = False

#Rule:3 Spaces are not allowed in Username
if any(char.isspace() for char in Username):
    print("Space is not allowed in Username")
    Username_valid = False

#Rule:-4 Only Letter and Underscore 
for char in Username:
    if not (char.isalpha() or char == "_"):
        print("Username only contain Letter and Underscore")
        Username_valid = False
        break
if Username_valid:
#-------Password--------
    Password = input("Enter Password :")
    Password_valid = True

#Rule:1 Password Must be 8 or More char.
    if len(Password)<8:
        print("Password is Too Short")
        Password_valid = False

#Rule:2 Add One UpperCase Letter
    if not any(char.isupper()for char in Password):
        print("Password Must Contain One Uppercase Letter")
        Password_valid = False

#Rule:3 Add Lowercase Letter
    if not any(char.islower()for char in Password):
        print("Password Must Contain One Lowercase Letter")
        Password_valid = False

#Rule:4 Add Number In Password
    if not any(char.isdigit() for char in Password):
        print("Add a Number")
        Password_valid = False

#Rule:5 add Any special Charector in Password
    if not any(char in '!@#$%^&*()_-'for char in Password):
        print("Add Any Special Charector in Password")
        Password_valid = False

#------------Final Result------------
    if Password_valid:
        print("Account Created SUCCESSFULLY")
    else:
        print("Invalid Password , Account Not Created ")
else:
    print("Invalid Username, Account Not Created")