from automationTesting.src.pages.ProductListPage import ProductListPage


import pytest

class LoginPage:

    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._loging_btn = page.get_by_text("Login")
        self._error_msg= page.locator("//h3[@data-test = 'error']")

    def enter_username(self,user_name):
        self._username.clear()
        self._username.fill(user_name)

    def enter_password(self, pass_wd):
        self._password.clear()
        self._password.fill(pass_wd)

    def click_login_btn(self):
        self._loging_btn.click()

    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login_btn()
        return ProductListPage(self.page)

    @property
    def error_msg_loc(self):
        return self._error_msg

    @property
    def login_btn(self):
        return self._loging_btn

