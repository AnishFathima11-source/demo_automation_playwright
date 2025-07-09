from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page

from test_cart import add_product_to_cart

scenarios("./features/order.feature")

@given("the user has a product in the cart")
def ensure_product_in_cart(page: Page,logged_in_user):
    page.click("//div[@class='col-lg-3']//a[1]")
    add_product_to_cart(page)
    page.click("//a[@id='cartur']")
    page.wait_for_timeout(1000)
    

@when("the user places an order")
def place_order(page: Page):
    page.click("//button[normalize-space()='Place Order']")
    assert page.locator("#orderModal").is_visible()
    page.fill("#name", "Irfan")
    page.fill("#country", "India")
    page.fill("#city", "Udumalai")
    page.fill("#card", "1234567890")
    page.fill("#month", "07")
    page.fill("#year", "2025")
    page.click("//button[normalize-space()='Purchase']")

@then("a purchase confirmation should appear")
def confirm_purchase(page: Page):
    assert page.locator("//div[contains(@class,'showSweetAlert visible')]").is_visible()
   
    page.click("//button[normalize-space()='OK']")
    page.wait_for_timeout(1000)
