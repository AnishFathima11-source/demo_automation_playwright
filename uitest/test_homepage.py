from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page, expect

scenarios("./features/home.feature")  # relative path to the .feature file


@given("the user navigates to the Demoblaze homepage")
def visit_home(page: Page):
    page.goto("https://www.demoblaze.com")

@then('the page title should be "STORE"')
def verify_title(page: Page):
    assert page.title() == "STORE"


@then("the logo should be visible")
def check_logo(page: Page):
    expect(page.locator("//a[@id='nava']//img")).to_be_visible()


@then("the navigation menu should be visible")
def check_navigation(page: Page):
    expect(page.locator("#navbarExample")).to_be_visible()


@then("featured products should be displayed")
def check_featured_products(page: Page):
    assert page.locator("//div[@id='tbodyid']//div[1]//div[1]//a[1]//img[1]").is_visible()
