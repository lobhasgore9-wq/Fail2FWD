'''Write a Python program that asks the user to enter a word and then prints the number of vowels in that word. '''
word=input("Enter a word")
count=0
vowels="a,e,i,o,u,A,E,I,O,U"
for i in word:
    if i in vowels:
        count+=1
print(f"The number of vowels in {word} is:{count}")

