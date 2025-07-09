Feature: Logout Functionality

  Scenario: Logout from account
    Given the user is logged in to the system
    When the user clicks the logout option
    Then the user should be logged out and see the login button