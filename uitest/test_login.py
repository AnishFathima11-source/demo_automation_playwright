from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page
from constant import PASSWORD, USERNAME

scenarios("./features/login.feature")

@given("the user opens the login modal")
def open_login(page: Page):
    page.goto("https://www.demoblaze.com")
    page.click("#logout2") #To verify te login functionality
    page.click("#login2")
    page.wait_for_selector("#loginusername")

@when("the user enters valid login credentials")
def enter_login_credentials(page: Page):
    page.fill("#loginusername", USERNAME)
    page.fill("#loginpassword", PASSWORD)

@when("the user clicks the login button")
def submit_login(page: Page):
    page.click("//button[normalize-space()='Log in']")
    page.wait_for_timeout(2000)

@then("the user should be logged in successfully")
def verify_login(page: Page):
    assert page.locator("#nameofuser").is_visible()
