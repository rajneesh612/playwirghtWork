

class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_headers = page.locator("span.title")
        self._burger_menu = page.locator("//button[@id='react-burger-menu-btn']")
        self._logout_btn = page.locator("#logout_sidebar_link")
        self._add_to_cart = page.locator("#add-to-cart-sauce-labs-bike-light")

    @property
    def products_header(self):
        """It returns locator or selector of product header text"""
        return self._products_headers

    def click_berger_menu_btn(self):
        """It clicks on hamberger menu in products page"""
        self._burger_menu.click()

    def click_logout(self):
        """This will click on logout in the berger menu"""
        self._logout_btn.click()

    def do_logout(self):
        """This method is for user logout."""
        self.click_berger_menu_btn()
        self.click_logout()


    def get_add_to_cart_or_remove_from_cart_locator(self,product):
        """This will return locator add to cart button or remove button"""
        return self.page.locator(f"//div[text()='{product}']/ancestor::div[2]//div[@class='pricebar']/button")

    def click_add_to_cart(self,product):
        self.get_add_to_cart_or_remove_from_cart_locator(product).click()


