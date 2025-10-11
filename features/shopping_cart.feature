Feature: Shopping cart for the customers selected items
	As a user I want to be able to select items to be put into a shopping cart

	Scenario: The user adds an item to the shopping cart
		Given the user is on the details page of a specific book
		When the user clicks on the add to chart button
		Then the book should be added to the shopping cart

	Scenario: The user removes an item from the shopping cart
		Given the user is viweing the shopping cart
		When the user clicks on the remove from cart button of a specific book
		Then the book should be removed from the shopping cart
