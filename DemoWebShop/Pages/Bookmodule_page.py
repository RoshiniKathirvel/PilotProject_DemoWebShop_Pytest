from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class Bookmodule(BasePage):
    book_l = (By.XPATH, "(//li/a)[5]")
    position_l = (By.ID, "products-orderby")
    product_l = (By.XPATH, "(//h2/a)[1]")
    view_l = (By.ID, "products-viewmode")
    addtocard_l = (By.XPATH, "(//input[@class='button-2 product-box-add-to-cart-button'])[1]")
    display_l = (By.ID, "products-pagesize")
    pricefilter_l = (By.XPATH, "(//span[text()='50.00'])[2]")
    actualprice_l = (By.XPATH, "//span[@class='price actual-price']")
    removefilter_l = (By.XPATH, "//a[text()='Remove Filter']")
    assertremove_l = (By.XPATH, "(//div/strong)[4]")
    continueshoppint_l = (By.XPATH, "//input[@class='button-2 continue-shopping-button']")
    verifyalert_l = (By.XPATH, "//p[@class='content']")
    productitle_l = (By.XPATH, "//h2[@class='product-title']/a")
    verify_shopping = (By.XPATH, "//div[@class='page-title']/h1")
    asserting_product = (By.XPATH, "//div/h1")
    recentlyviewproduct = (By.XPATH, "(//a[text()='Computing and Internet'])[2]")
    click_shoppingcart = (By.XPATH, "//p[@class='content']/a")

    def __init__(self, driver):
        super().__init__(driver)

    def click_book(self):
        book_element = self.find(self.book_l)
        self.for_click(book_element)

    def select_position(self):
        position_element = self.find(self.position_l)
        self.for_click(position_element)

    def select_product(self):
        product_element = self.find(self.product_l)
        self.for_click(product_element)

    def change_view(self):
        view_element = self.find(self.view_l)
        self.for_click(view_element)

    def add_to_cart(self):
        add_to_cart_element = self.find(self.addtocard_l)
        self.for_click(add_to_cart_element)

    def change_display_size(self):
        display_element = self.find(self.display_l)
        self.for_click(display_element)

    def apply_price_filter(self):
        price_filter_element = self.find(self.pricefilter_l)
        self.for_click(price_filter_element)

    def remove_filter(self):
        remove_filter_element = self.find(self.removefilter_l)
        self.for_click(remove_filter_element)

    def continue_shopping(self):
        continue_shopping_element = self.find(self.continueshoppint_l)
        self.for_click(continue_shopping_element)

    def verify_alert(self):
        alert_element = self.find(self.verifyalert_l)
        return alert_element.text

    def get_product_title(self):
        product_title_element = self.find(self.productitle_l)
        return product_title_element.text

    def verify_shopping_title(self):
        shopping_title_element = self.find(self.verify_shopping)
        return shopping_title_element.text

    def assert_product(self):
        asserting_product_element = self.find(self.asserting_product)
        return asserting_product_element.text

    def recently_view_product(self):
        recently_view_product_element = self.find(self.recentlyviewproduct)
        self.for_click(recently_view_product_element)

    def click_shopping_cart(self):
        shopping_cart_element = self.find(self.click_shoppingcart)
        self.for_click(shopping_cart_element)
        
    def get_product_names(self):
        product_elements = self._driver.find_elements(*self.productitle_l)
        product_names = [element.text for element in product_elements]
        return product_names
    
    
