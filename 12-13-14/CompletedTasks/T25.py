

cart = []

def add_to_cart(item):
    global cart
    cart.append(item)

def remove_from_cart(item):
    global cart
    cart.remove(item)

def clear_cart():
    global cart
    cart.clear()

def show_cart():
    print(cart)


