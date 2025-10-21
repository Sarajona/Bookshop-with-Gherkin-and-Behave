from behave import given, when, then
from shopping_cart_steps import Book
import ast


@given("the cart is empty")
def step_given_cart_empty(context):
    context.cart = []
    context.total = 0
    print("Cart is empty.")


@when('the user adds {count:d} books named "{book_title}" priced at {price:d} to the cart')
def step_when_add_count_books(context, count, book_title, price):
    context.cart = [Book(book_title, price) for _ in range(count)]
    
    total = sum(book.price for book in context.cart)
    if len(context.cart) > 3:
        total *= 0.9
        print(f"Discount applied: 10% off for {len(context.cart)} books.")
    else:
        print("No discount applied.")

    context.total = round(total, 2)
    print(f"Cart total is {context.total} kr.")


@then("the total price displayed in the cart should be {expected_total}")
def step_then_total_matches(context, expected_total):
    assert context.total == float(expected_total), f"Expected {expected_total} but got {context.total}"
    print(f"Total matches expected: {expected_total} kr.")


@given("the inventory for {book_title} is {stock_count}")
def step_given_inventory(context, book_title, stock_count):
    context.inventory = {}
    title = ast.literal_eval(book_title)
    context.inventory[title] = int(stock_count)
    print(f"Inventory set: {title} = {stock_count} in stock.")


@when("the customer adds {quantity} copies of {book_title} priced at {price}")
def step_when_add_quantity(context, quantity, book_title, price):
    title = ast.literal_eval(book_title)
    quantity = int(quantity)
    price = int(price)
    stock = context.inventory.get(title, 0)

    if stock == 0:
        context.cart = []
        context.message = "Out of stock."
        print(f"{title} is out of stock.")
    elif quantity > stock:
        context.cart = [Book(title, price, copy_count=stock)]
        context.message = f"Only {stock} copies available in stock."
        print(f"Attempted to add {quantity}, limited to {stock}.")
    else:
        context.cart = [Book(title, price, copy_count=quantity)]
        context.message = "Added to cart."
        print(f"Added {quantity} copies of {title} to cart.")


@then("the cart contains {final_quantity} copies of {book_title}")
def step_then_correct_quantity(context, final_quantity, book_title):
    title = ast.literal_eval(book_title)
    final_quantity = int(final_quantity)

    if context.cart:
        cart_book = context.cart[0]
        assert cart_book.copy_count == final_quantity, f"Expected {final_quantity}, got {cart_book.copy_count}"
        assert cart_book.title == title
    else:
        assert final_quantity == 0, "Cart should be empty"
    print(f"Cart contains {final_quantity} copies of {title}.")


@then('the system displays message "{message}"')
def step_then_displays_message(context, message):
    assert context.message == message, f"Expected '{message}', got '{context.message}'"
    print(f"System message: '{context.message}'")


@given("the customer has placed the following orders:")
def step_given_has_orders(context):
    context.order_history = {}
    for row in context.table:
        order_id = int(row["Order ID"])
        books = ast.literal_eval(row["Books"])
        context.order_history[order_id] = [Book(title, price) for title, price in books]
    print(f"Loaded order history with {len(context.order_history)} orders.")


@when("the customer opens the order history")
def step_when_opens_history(context):
    context.viewed_orders = context.order_history
    print("Customer views order history.")


@then("the order history should contain {count} orders")
def step_then_history_contains(context, count):
    count = int(count)
    assert len(context.viewed_orders) == count, f"Expected {count} orders, got {len(context.viewed_orders)}"
    print(f"Order history contains {count} orders.")


@then("order {order_id} should list {book_titles}")
def step_then_order_contains_books(context, order_id, book_titles):
    order_id = int(order_id)
    expected_titles = ast.literal_eval(book_titles)
    actual_titles = [book.title for book in context.viewed_orders[order_id]]
    assert actual_titles == expected_titles, f"Expected {expected_titles}, got {actual_titles}"
    print(f"Order {order_id} contains correct books: {expected_titles}.")
