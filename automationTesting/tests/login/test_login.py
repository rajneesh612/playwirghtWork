from playwright.sync_api import Page, expect

from automationTesting.src.pages.LogingPage import LoginPage


def test_loging_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    expect(products_p.products_header).to_have_text("Products")


def test_loging_with_invalid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'invalid_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    expected_error_msg = "Username and password do not match any user in this service"
    expect(login_p.error_msg_loc).to_contain_text(expected_error_msg)


def test_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p.products_header).to_have_text("Products")
    products_p.do_logout()
    expect(login_p.login_btn).to_be_visible()


def test_access_inventory_without_login(set_up_tear_down) -> None:
    page = set_up_tear_down
    page.goto("https://www.saucedemo.com/inventory.html")
    login_p = LoginPage(page)
    expect(login_p.error_msg_loc).to_contain_text("You can only access '/inventory.html' when you are logged in.")
