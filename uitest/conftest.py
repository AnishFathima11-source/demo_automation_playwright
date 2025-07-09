import pytest
import os

from playwright.sync_api import Browser, sync_playwright

from constant import PASSWORD, USERNAME

headless_mode = os.environ.get("HEADLESS_MODE", False)
if headless_mode == "true":
    headless_mode = True
elif headless_mode == "false":
    headless_mode = False


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode, slow_mo=1000)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(ignore_https_errors=True)
    yield context
    context.close()


@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()




@pytest.fixture(scope="session")
def signed_up_user(page):
    page.goto("https://www.demoblaze.com")
    page.click("#signin2")
    page.wait_for_selector("#signInModal")
    
    page.fill("#sign-username", USERNAME)
    page.fill("#sign-password", PASSWORD)
    page.doub("//button[normalize-space()='Sign up']")
    alert = page.wait_for_event("dialog")
    alert.accept()
    page.wait_for_timeout(1000)
    yield page
    page.close()

@pytest.fixture(scope="session")
def logged_in_user(page):
    page.goto("https://www.demoblaze.com")
    page.click("#login2")
    page.wait_for_selector("#loginusername")
    page.fill("#loginusername", USERNAME)
    page.fill("#loginpassword", PASSWORD)
    page.click("//button[normalize-space()='Log in']")
    page.wait_for_selector("#nameofuser", timeout=5000)
    return page