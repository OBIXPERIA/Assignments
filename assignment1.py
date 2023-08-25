products = ["rice","beans","plantain","chocolate","icecream","biro","bags"]
commodity = input("enter item: ")
# if products not in products:
#     products.append(commodity)
#     print(products)
# else:  

# adding item to product
for i in products:
    if commodity in products:
        print("Product already avaliable")
        break
    else:
        products.append(commodity)
        print(f'add {commodity} successfully')
        print(products)


# removing items from product
get_item_index = products.index(commodity)
products.pop(get_item_index)
print(products)

"""
    pro_index = products.index(commodity)
    print((pro_index))
    products.pop(pro_index)
    print(products)
"""


# products.insert(1, "chocolate")
# print(products)

"""
Note : stop writing static codes 

1. items can only be added to the store if it is not no the store

score - 30
"""