'''
Task 1
'''


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, item):
        self.items[index] = item

    def __delitem__(self, index):
        del self.items[index]

    def __str__(self):
        return f'ShoppingCart: {", ".join(self.items) if self.items else "Empty"}'

    def __contains__(self, item):
        return item in self.items


cart = ShoppingCart()

cart.add_items('Book')
cart.add_items('Laptop')
cart.add_items('Coffee')
print(len(cart))

print(cart[0])

cart[1] = 'Journal'

print(cart)

cart = ShoppingCart()
print(cart)