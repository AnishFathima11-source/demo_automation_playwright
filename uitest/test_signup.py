from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page


from constant import PASSWORD, USERNAME

scenarios("./features/signup.feature")

@given("the user opens the signup modal")
def open_signup(page: Page):
   
    page.click("#signin2")
    page.wait_for_timeout(1000)
    assert page.is_visible("#signInModal")

@when("the user enters a new username and password")
def enter_signup_data(page: Page):
    page.fill("#sign-username", USERNAME)
    page.fill("#sign-password", PASSWORD)

@when("the user submits the signup form")
def submit_signup(page: Page):
    page.click("//button[normalize-space()='Sign up']")
    alert = page.wait_for_event("dialog")
    alert.accept()

@then("a signup success message should appear")
def signup_success(page: Page):   
    page.wait_for_timeout(2000)