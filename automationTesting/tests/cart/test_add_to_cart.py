from playwright.async_api import expect

from automationTesting.src.pages.LogingPage import LoginPage


def test_add_to_cart(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    product_name = "Sauce Labs Bike Light"
    products_p.click_add_to_cart(product_name)


