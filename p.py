

products = ["rice","beans","plantain","chocolate","icecream","biro","bags"]
products.pop(6)
print(products)

products.append("milk")
print(products)


product1 = products.copy()
product1.sort(reverse = True)
print(product1)


products.insert(1, "chocolate")
print(products)



h = [1,2,4,5,8,9]
target_value =8
if target_value in h:
   print(h.index(target_value))
else:
    list1 = h.copy()
    list1.append(target_value)
    print(list1)





