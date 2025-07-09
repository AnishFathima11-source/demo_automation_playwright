Feature: User Login

  Scenario: Login with valid credentials
    Given the user opens the login modal
    When the user enters valid login credentials
    And the user clicks the login button
    Then the user should be logged in successfully