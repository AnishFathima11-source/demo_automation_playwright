from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page

scenarios("./features/cart.feature")

@given('the user navigates to the "Laptops" category')
def go_to_laptops(page: Page,signed_up_user,logged_in_user):
    page.click("//div[@class='col-lg-3']//a[1]")
    page.wait_for_timeout(1000)

@when("the user selects a product and adds it to cart")
def add_product_to_cart(page: Page):
    page.click("//div[@id='tbodyid']//div[1]//div[1]//a[1]//img[1]")
    assert page.locator("//h3[@class='price-container']").is_visible()

    page.wait_for_timeout(1000)

    with page.expect_event("dialog") as dialog_info:
        page.click("//a[contains(@onclick, 'addToCart')]")
    dialog_info.value.accept()


@then("the product should be added to the cart successfully")
def cart_success(page: Page):
    page.wait_for_timeout(2000)
    page.click("//a[normalize-space()='Cart']")
    assert page.locator("//table[@class='table table-bordered table-hover table-striped']").is_visible()
