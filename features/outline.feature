Feature: Shopping cart for the customers selected items
	As a customer I'd like to keep my selected items in a shopping cart

	Scenario Outline: The user removes an item from the cart
		Given the user is viewing the shopping cart page
		And the cart has <list_of_books>
		When the user clicks on the remove from cart button on a <book>
		Then the cart has <expected_list_of_books>

		Examples:
			| list_of_books				  | book			  | expected_list_of_items |
			| [["Catcher in the Rye", 199]]		  | ["Catcher in the Rye", 199]	  | []			   |
			| [["Dracula", 129], ["Neverwhere", 149]] | ["Dracula", 129]		  | [["Neverwhere", 149]]  |

	Scenario Outline: The shopping cart always displays the correct total and number of books
		Given the cart has <list_of_books>
		When the user opens the shopping cart
		Then the total price is <expected_total>
		And the book count is <book_count>

		Examples:
			| list_of_books								| expected_total | book_count |
			| []									| 0		 | 0          |
			| [["1Q84", 149], ["The Call of Cthulhu", 99], ["The Hobbit", 100]]	| 348		 | 3	      |
			
	Scenario Outline: The user clears the shopping cart
		Given the user is viewing the shopping cart page
		And the cart has <list_of_books>
		When the user clicks on the clear cart button
		Then the list of items is empty

		Examples:
			| list_of_books					|
			| [["Dracula", 129], ["Neverwhere", 149]]	|
			| [["Klara and the sun", 199]]			|
