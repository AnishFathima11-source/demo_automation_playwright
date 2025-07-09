Feature: Homepage Verification

  Scenario: Verify homepage loads successfully
    Given the user navigates to the Demoblaze homepage
    Then the page title should be "STORE"
    And the logo should be visible
    And the navigation menu should be visible
    And featured products should be displayed