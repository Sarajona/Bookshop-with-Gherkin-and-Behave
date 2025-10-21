Feature: Discounts, Inventory management, and Order history
    As a customer I want to receive discounts for large orders,
    be prevented from buying more books than are in stock,
    and be able to view my past orders.


	Scenario Outline: The total price updates with discount when there is 3+ books in cart
		Given the cart is empty
		When the user adds <count> books named "<title>" priced at <price> to the cart
		Then the total price displayed in the cart should be <expected_total>

		Examples:
			| count | title       | price | expected_total |
			| 2     | Book A      | 100   | 200            |
			| 3     | Book B      | 100   | 300            |
			| 4     | Book C      | 100   | 360            |
			| 5     | Book D      | 100   | 450            |
			| 1000  | Cheap Book  | 1     | 900            |
			| 64000 | Cheap Book  | 1     | 57600	       |


	Scenario Outline: The customer cannot add more books than available in stock
        	Given the inventory for <book_title> is <stock_count>
        	And the cart is empty
        	When the customer adds <quantity> copies of <book_title> priced at <price>
        	Then the cart contains <final_quantity> copies of <book_title>
		And the system displays message <message>

        	Examples:
            	| book_title       | stock_count | quantity | price | final_quantity | message                                 |
            	| "Dracula"        | 5           | 3        | 129   | 3              | "Added to cart."                        |
            	| "The Hobbit"     | 2           | 5        | 100   | 2              | "Only 2 copies available in stock."     |
            	| "Neverwhere"     | 0           | 1        | 149   | 0              | "Out of stock."                         |

	
	Scenario: The customer's previous orders appear in the order history
        	Given the customer has placed the following orders:
            		| Order ID | Books                                          |
            		| 1        | [["Dracula", 129], ["Neverwhere", 149]]        |
            		| 2        | [["The Hobbit", 100]]                          |
        	When the customer opens the order history
        	Then the order history should contain 2 orders
        	And order 1 should list ["Dracula", "Neverwhere"]
        	And order 2 should list ["The Hobbit"]
