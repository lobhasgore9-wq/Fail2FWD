"""Write a Python program that takes a number from the user and prints the multiplication table for that number up to 10"""
num=int(input("Enter a number:"))
print(f"The multiplication table of {num} is:")
for i in range(1,11):
    print(f"{num}x{i}={num*i}")