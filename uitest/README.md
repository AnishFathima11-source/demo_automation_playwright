# Automated UI test 

Look at the [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) to learn more.

## Prerequisites

- Python installed on your system.
- `pytest`, `pytest-bdd`, and `pytest-playwright` packages installed. You can install these using poetry:

  ```bash
  poetry init
  poetry install
  poetry add pytest pytest-bdd pytest-playwright
  ```

- Install the required browsers for Playwright:

  ```bash
  playwright install
  ```

## Project Structure

Your project should be organized as follows:

```bash
├── tests
│   ├── login
│   │       ├── test_valid_login.py
│   │       ├── test_invalid.py
│   │       └── features
│   │             ├── valid_login.feature
│   │             └── invalid_login.feature
│   │
│   └──sites
│          ├── test_valid_site.py
│          └── features
│                └── valid_site.feature
│  
├── conftest.py
└── pytest.ini
```

## Feature Files

In Playwright with pytest-bdd, a features file is used to define the behavior of your application in a human-readable format using the Gherkin language. These files are typically used to specify the scenarios for behavior-driven development (BDD).

### Structure of features

Feature: Describes the feature being tested.
Scenario: Defines a specific situation or use case.
Given: The initial context or preconditions.
When: The action or event that triggers the test.
Then: The expected outcome or result.
And: Additional conditions or actions.

```gherkin
Feature: Login to smartBuild

  Scenario: Log into smartBuild with valid credentails
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the user should be redirected to the dashboard
```

## To Run the testcases

   ```bash
    pytest [filepath]
   ``` 

## To Generate a Report While Running Test Cases in Playwright with Pytest
### To run the tests with detailed output, use the following command:

```bash
pytest [filepath] --tb=long > ui_test_result.text

```
### This command will:

``` Use --tb=long to generate detailed tracebacks for any failed tests.
Redirect the output to ui_test_result.text for easy inspection.
```

## To open the test report

  ```bash
  cat ui_test_result.text
  ```