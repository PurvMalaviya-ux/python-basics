Username = input("Enter your username :")

if len(Username)< 5 or len(Username)>15:
    print("Invaild : Length of your name must be 5 to 15")
else:
    print("Fine Length")
if not Username[0].isalpha():
    print("Invaild: Start With Letter")
else:
    print("Starts Correctly")
valid = True
for char in Username:
    if not (char.isalnum() or char == '_'):
        valid = False
        break
if valid: 
    print("Username is Valid")
else:
    print("Username Only Contains Letter , Numbers , Underscores")