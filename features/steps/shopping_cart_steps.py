from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then

class Book:
    def __init__(self, title, price, copy_count=1):
        self.title = title
        self.price = price
        self.copy_count = copy_count
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.price == other.price and self.copy_count == other.copy_count
        return False

@given(u'the user is viewing the details page of a book')
def step_given_viewing_(context):
    context.page = "details_page"
    print("User is on the details page of a book")
    context.cart = []       
    context.current_book = Book("Catcher in the rye", 199)

@when(u'the user clicks on the add to cart button')
def step_when_clicks_add(context):
    context.button_clicked = True
    print("The button has been clicked")
    book_already_exists = False
    for book in context.cart:
        if book.title == context.current_book.title:
            book.copy_count += 1
            book_already_exists = True
            break
    if book_already_exists == False:
        context.cart.append(context.current_book)

@then(u'the book is added to the cart')
def step_then_book_is_added(context):
    assert len(context.cart) == 1

@given(u'the user is viewing the details page of a book that already exists in the cart')
def step_given_details_page(context):
    context.page:"details_page"
    print("User is on the details page")
    existing_book = Book("Catcher in the rye", 199)
    context.cart = [existing_book]
    context.current_book = Book("Catcher in the rye", 199)

@then(u'The copy count is increased by 1')
def step_then_copies_are_increased(context):
    book_in_cart = context.cart[0]
    assert book_in_cart.copy_count == 2 

