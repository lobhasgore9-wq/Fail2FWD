#print a number which starts with a vowel
vowels=('A','E','I','O','U','a','i','o','u')
for i in range(5):
    name=input("enter a name")
    if name[0] in vowels:
        print(name)