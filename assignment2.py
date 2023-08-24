sort_integer = [1,2,4,5,8,9]
target_value = input('number: ')

if target_value in sort_integer:
   print(sort_integer.index(target_value))
else:
    list1 = sort_integer.copy()
    list1.append(target_value)
    print(list1)

"""
fix the returning of array instead of displaying index

score - 70 

comment - The code is good but you need to make the code flexiable
"""