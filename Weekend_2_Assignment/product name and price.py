# Write a script to sort a list of tuples containing product name and price

products=[("Milk", 20), ("Bread", 10), ("Eggs", 30)]
print(type(products))
for item in products:
    print(item,end=",")

print()

products.sort()
for item in products:
   print(item,end=",")
print()


# METHOD:2
# products = [("Milk", 2), ("Bread", 1), ("Eggs", 3)]
# sorted_products = sorted(products)
#
# print(sorted_products)

# METHOD:3
# products = ["Milk", ("Bread", ("Eggs"]
# price= [2,1,3]
# def get_price(product):
#     return product[1]
#
#
#
# if __name__ == '__main__':
#     sorted_products = sorted(products, key=get_price)
#
#     print(sorted_products)


