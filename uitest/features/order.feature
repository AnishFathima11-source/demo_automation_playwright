Feature: Placing an Order

  Scenario: Purchase an item from the cart
    Given the user has a product in the cart
    When the user places an order
    Then a purchase confirmation should appear