# Shopping Cart Validation
# Instructions:
# Create a variable ItemsInCart and initialize it to 0.
# Write a function called add_to_cart that accepts an integer parameter items_to_add.
# If items_to_add is less than 0, raise an exception with the message "Cannot add a negative number of items."
# If the total count of items after addition exceeds 5, raise an exception with the message "Cart limit exceeded."
# # Example function structure
# def add_to_cart(items_to_add):
#     # Your code here
# # Example of using the function
# try:
#     add_to_cart(2)  # Add 2 items
#     add_to_cart(-1)  # This should raise an exception
# except Exception as e:
#     print(e)
# Expected Result:
# 2 items added. Total in cart: 2
# Cannot add a negative number of items.

ItemsInCart = 0


def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


# Example of using the function
try:
    add_to_cart(2)  # Add 2 items
    add_to_cart(-1)  # This should raise an exception
except Exception as e:
    print(e)