Feature: User Registration

  Scenario: Register with valid data
    Given the user opens the signup modal
    When the user enters a new username and password
    And the user submits the signup form
    Then a signup success message should appear