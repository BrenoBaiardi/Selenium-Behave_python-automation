Feature: HomePage 

Scenario: Add product into empty cart
    Given I am currently at home page
    And the cart is empty 
    When I click add to cart button in a product
    Then the cart need to have only one product

Scenario: Add product into cart when not empty
    Given I am currently at home page
    And I add something to the cart
    And the cart is not empty 
    When I click add to cart button in a product
    Then the cart need to recieve the product

