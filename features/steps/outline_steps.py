from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then
from shopping_cart_steps import Book
import ast

@given(u'the user is viewing the shopping cart page')
def step_given_veiwing_cart(context):
    context.page = "cart_page"
    print("User is on the shopping cart page")    

@given(u'the cart has {list_of_books}')
def step_given_cart_has_content(context,list_of_books):
    book_data = ast.literal_eval(list_of_books)
    context.cart = []
    for book in book_data:
        title = book[0]
        price = book[1]
        new_book = Book(title, price)
        context.cart.append(new_book)
    print(f"The cart has {context.cart}")

@when(u'the user clicks on the remove from cart button on a {book}')
def step_when_clicks_remove_button(context, book):
    context.button_pressed = True
    print("The button has been pressed")
    book_to_remove = ast.literal_eval(book)
    title = book_to_remove[0]
    price = int(book_to_remove[1])
    for item in context.cart:
        if item.title == title and item.price == price:
            context.cart.remove(item)
            print(f"Removed {item.title}, {item.price} kr, from the cart.")
            break

@then(u'the cart has {expected_list_of_books}')
def step_then_item_is_removed(context, expected_list_of_books):
    expected_list_of_books = ast.literal_eval(expected_list_of_books)
    expected_cart = []
    for book in expected_list_of_books:
        title = book[0]
        price = book[1]
        new_book = Book(title, price)
        expected_cart.append(new_book)
    assert context.cart == expected_cart 
    print(f"The cart has correct contents ")

@when(u'the user opens the shopping cart')
def step_when_open_cart(context):
    context.page = "shopping_cart_page"
    print("The cart has been opened")
    context.total = 0
    for book in context.cart:
        book_total =  (book.price * book.copy_count)
        context.total += book_total
    print(f"The total of all the books has been calculated")
    context.count = 0
    for book in context.cart:
        context.count += book.copy_count
    print(f"The book count has been calculated")

@then(u'the total price is {expected_total}')
def step_then_total_is_correct(context, expected_total):
    assert context.total == int(expected_total)
    print(f"the total price is {expected_total}")                   

@then(u'it says that there are {book_count} books in the cart')
def step_then_count_is_correct(context,book_count):
    assert context.count == int(book_count)
    print(f"Book count is {book_count}")

@when(u'the user clicks on the clear cart button')
def step_when_clicks_clear(context):
    context.button = True
    print("The button has been clicked")
    context.cart.clear()
    print("The cart has been cleared")

@then(u'the list of items is empty')
def step_then_cart_empty(context):
    assert context.cart == []
    print("the cart is now empty")
