from playwright.sync_api import Page, expect


def test_loging_with_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    product_header = page.locator("span.title")
    expect(product_header).to_have_text("Products")

def test_loging_with_invalid_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("ser123")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    error_msg_locator = page.locator("//h3[@data-test = 'error']")
    expected_error_msg = "Username and password do not match any user in this service"
    expect(error_msg_locator).to_contain_text(expected_error_msg)

