

ItemsInCart = 0

def add_to_cart(items_to_add):
    global ItemsInCart

    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if (ItemsInCart + items_to_add > 5):
            raise Exception("Cart limit exceeded.")
    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


try:
    add_to_cart(2)  # Add 2 items
    add_to_cart(-1)  # This should raise an exception
except Exception as e:
    print(e)







