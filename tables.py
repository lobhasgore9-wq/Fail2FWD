#print tables from 1 to 10
def table():
    for number in range(1,11):
        print(f"\nmultiplication table of {number} is....")
        for index in range(1,11):
            print(f"{number}x{index}={number * index}")
table()




