"""Write a Python program that takes a number from the user and checks whether it is even or odd."""
num=int(input("Enter a number:"))
if num>1:
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("it is invalid,plz enter a positive number")