Feature: Shopping cart for the customers selected items
        Testing the shopping cart with outline

	Scenario Outline: The shopping cart always displays the correct total and number of books
                Given the shopping cart contains <book_count> books with individual prices as in <prices>
                When the user opens the shopping cart
                Then the displayed total should equal <expected_total>
                And the book count is <book_count>

                Examples:
                        | book_count | prices                | expected_total |
                        | 0          | []                    | 0.00           |
                        | 1          | [120.00]              | 120.00         |
                        | 3          | [50.00, 75.00, 25.00] | 150.00         |

        Scenario Outline: The user adds a book that already exists in the shopping cart
                Given the user is on the details page of a book that already has <copy_count> copies of in the shopping cart
                When the user clicks on the add to cart button
                Then The copy count is <expected_copy_count>

                Examples:
                        | copy_count | expected_copy_count |
                        | 0          | 1                   |
                        | 1          | 2                   |
                        | 51         | 52                  |

        Scenario Outline: The user clears the shopping cart
                Given the user is viewing the shopping cart
                And the shopping cart has <book_count> books
                When the user clicks on the clear cart button
                Then the book count is 0
                And the total price is 0

                Examples:
                        | book_count |
                        | 0          |
                        | 1          |
                        | 5          |
                        | 10         |
