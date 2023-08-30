def add (num1,num2):
    return num1 + num2

def sub (num1,num2):
    return num1 - num2


print('welcome\n\n'.capitalize().center(120))

options = int(input("""
1. add numbers
2. subtract numbers
:: """))


if options == 1 :
    num1 = int(input("first num: "))
    num2 = int(input("second num: "))
    print(add(num1,num2))

elif options == 2 :
    num1 = int(input("first num: "))
    num2 = int(input("second num: "))
    print(sub(num1,num2))
