Feature: Shopping cart for the customers selected items
	As a user I want to be able to select items to be put into a shopping cart

        Scenario: The user adds an item to the cart
                Given the user is viewing the details page of a book
                When the user clicks on the add to cart button
                Then the book is added to the cart

	Scenario: The user adds a book that already exists in the shopping cart
                Given the user is viewing the details page of a book that already exists in the cart
                When the user clicks on the add to cart button
                Then The copy count is increased by 1


	

	
