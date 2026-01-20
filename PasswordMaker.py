print("Hello it's Program To Check Your Password is Strong OR Weak")
print("                        ")


Name=str(input("Enter Your Name :"))
print("                        ")


Password = str(input("Enter Your Password"))
print("                        ")


length = len(Password)
if length >= 8:
    print(f"Hello {Name} Your Password Is Weak (Add Minimum 8 Charactors)")
elif not any(char.isdigit() for char in Password):
    print(f"Hello {Name} Your Password is Weak (Add Digits)")
elif not any(char.isupper() for char in Password):
    print(f"Hello {Name} your Password Is weak (Add Uppercase Charactor)")
elif not any(char.islower() for char in Password):
    print(f"Hello {Name} your Password is weak (add Lowercase charactor)")
elif not any(char in " !@#$%^&*()+=`~:;'~`<,>.:;?/{[]} " for char in Password):
    print(f"Hello {Name}Your Password is Weak (add Some Special Charactors)")
else:
    print(f"Hello {Name}your Password is Strong")
    print()
    print(f"Thanks {Name} For Using My Code")