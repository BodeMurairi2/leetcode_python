#!/usr/bin/env python3


# Python dictionary
order = {1: "Bread",
         2: "Rice",
         3: "Beans",
         4: "Sugar",
         5: "Maize"}

# loop through each element of a dictionary:
for items, stuff in order.items():
    print("{:d} - {:s}".format(items, stuff))

order = {
    "Fashion": ["Lotion", "Sunglasses", "Jeans"],
    "Shoes": ["Sandals", "Sneakers", "Crocs", "Heels"],
    "Electronics": ["Phone", "Lapptop", "Drive"]
}


for category in order.values():
    for item in category:
        print(item)

test = ["Lotion", "Sunglasses", "Jeans"]
count = 0

for category, product in order.items():
    for j in range(0, len(product)):
        print(f"In {category}, we have {product[j]}")

user_input = input("Write the element you would like to add: ")


def add_element(test, user_input):
    '''
    Add an element
    '''
    test.append(user_input)
    print(test)


add_element(test, user_input)
