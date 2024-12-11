from cart import ShoppingCart
def test_can_add_item_to_cart(): #needs test in the name of method to run test
    cart = ShoppingCart()
    cart.add("apple")
    assert(cart.size() == 1)

def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart()
    cart.add("apple")
    assert "apple" in cart.get_items()