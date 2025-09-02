"""Write a Python program that takes three numbers from the user and prints the largest among them."""
num1=int(input("Enter 1st No.="))
num2=int(input("Enter 2nd No.="))
num3=int(input("Enter 3rd No.="))
if(num1>=2 and num1>=num3):
   print("num1 is the greatest number among that three numbers")
elif(num2>=num1 and num2>=num3):
    print("num2 is the greatest number among that three numbers")
else:
    print("num3 is the greatest  number among the three numbers")