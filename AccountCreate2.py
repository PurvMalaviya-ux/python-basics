print("=====Acount Creation=====")
print(" ")

# Username
while True:
    Username = input("Enter Your Name :-")
    valid = True 

    #Rule 1 Length
    if len(Username)<5 or len(Username)>15:
        print("Username must be in 5 to 15 Letter")
        valid = False
    
    #Rule 2 Uppercase and Lowercase
    if not any(char.isupper()for char in Username):
        print("Add One UpperCase Letter in it.")
        valid = False
    if not any(char.islower()for char in Username):
        print("Add one lowercase Letter")
        valid = False
    
    #Rule 3 First Uppercase 
    if not Username[0].isupper():
        print("First Letter Should be in Uppercase")
        valid = False
    elif not Username[0].isalpha():
        print("First Letter should be Letter not number")
        valid = False

    #Rule 5 No space
    if any(char.isspace()for char in Username):
        print("No Spaces are allowed")
        valid = False 

    #Rule 6 Only letter and Underscore
    if not all(char.isalnum() or char == "_" for char in Username):
        print("Only Letter , Numbers and Underscore")
        valid = False
    
    if valid:
        print("Username accepted")
        break # Exit From Username Loop
    else:
        print("Try Again")

# Password
while True:
    Password = input("Enter Password :-")
    valid = True

    #Rule 1 Must 7 or more Letters
    if len(Password)<7:
        print("Password is Too Short , minimum 7 Letters")
        valid = False
    
    #Rule 2 Upper
    if not any(char.isupper() for char in Password):
        print("Add One uppercase")
        valid = False

    #Rule 3
    if not any(char.islower()for char in Password):
        print("add lowercase")
        valid = False

    #Rule 4 
    if not any(char.isdigit() for char in Password):
        print("add Letter or Number")
        valid = False
    
    #Rule 5 
    if not any(char in "!@#$%^&*()_" for char in Password):
        print("Add Special Char Like !@#$%^&*()_")
        valid = False
    
    if valid:
        print("Password Accepted")
        break
    else:
        print("Try Again")

print("Account Created Successfully!")