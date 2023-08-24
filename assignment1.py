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