Feature: Add product to cart

  Scenario: Add a laptop to cart
    Given the user navigates to the "Laptops" category
    When the user selects a product and adds it to cart
    Then the product should be added to the cart successfully