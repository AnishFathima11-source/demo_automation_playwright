from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page

scenarios("./features/logout.feature")

@given("the user is logged in to the system")
def login_user(page: Page,logged_in_user):
   pass

@when("the user clicks the logout option")
def click_logout(page: Page):
    page.click("#logout2")

@then("the user should be logged out and see the login button")
def verify_logout(page: Page):
    assert page.locator("#login2").is_visible()
