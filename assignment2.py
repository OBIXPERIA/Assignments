#sort_integer = [1,2,4,5,8,9]
#target_value = input('number: ')

#if target_value in sort_integer:
#   print(sort_integer.index(target_value))
#else:
    #list1 = sort_integer.copy()
    #list1.append(target_value)
    #print(list1)

"""
fix the returning of array instead of displaying index

score - 70 

comment - The code is good but you need to make the code flexiable
"""

a = "rice"
b = "bread"
c = "cake"
def add_product(a,b,c):
    return a+b

def remove_product(a,b,c):
    return a-b-c

def arrange_product(a,b,c):
    return a,b,c
commodity = add_product("rice","cake","bread" )
print(commodity)
'''
print("welcome to global supermarket stores \n\n".upper().center(130))

option = (input ("""
1. add a product
2. remove a product
3. arrange a product         
::  """))


if option == add_product:
    a = input("enter a product")
    b = input("enter a product")
    print(add_product(a+b))'''