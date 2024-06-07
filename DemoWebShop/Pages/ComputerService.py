from selenium.webdriver.common.by import By
from .base_page import BasePage

class ComputerService(BasePage):
    Search = (By.CSS_SELECTOR, "div[class='column customer-service'] a[href='/search']")
    search_field = (By.CSS_SELECTOR, "input[name='q']")
    search_button = (By.CSS_SELECTOR, "input[type='submit']")
    product_list = (By.XPATH, "//div[@class='product-grid']//div[@class='item-box']")
    news_link = (By.CSS_SELECTOR, "a[href='/news']")
    news_assert = (By.XPATH, "//div[@class='page-title']//child::h1")
    blog_link = (By.CSS_SELECTOR, "a[href='/blog']")
    blog_assert = (By.XPATH, "//div[@class='page-title']//child::h1")
    recently_viewed_link = (By.XPATH, "//a[@href='/recentlyviewedproducts']")
    recently_viewed_assert = (By.XPATH, "//div[@class='page-title']//child::h1")
    compare_product_link = (By.XPATH, "//a[text()='Compare products list']")
    compare_assert = (By.XPATH, "//div[@class='page-title']//child::h1")
    new_products_link = (By.XPATH, "//a[text()='New products']")
    new_products_assert = (By.XPATH, "//div[@class='page-title']//child::h1")
    empty_search_button = (By.XPATH, "//input[@value='Search']")
    warning_minimum = (By.XPATH, "//div[@class='search-results']//child::strong")
    warning_invalid = (By.XPATH, "//strong[@class='result']")
    blog_title = (By.XPATH, "//a[text()='Customer Service - Client Service']")
    blog_link_text = (By.XPATH, "//div[@class='page-title']//child::h1")

    def click_search(self):
        self.for_click(self.find(self.Search))

    def search_product(self, product_name):
        search_input = self.find(self.search_field)
        self.for_send_keys(search_input, product_name)
        self.for_click(self.find(self.search_button))

    def get_product_count(self):
        return len(self._driver.find_elements(*self.product_list))

    def click_news_link(self):
        self.for_click(self.find(self.news_link))

    def click_blog_link(self):
        self.for_click(self.find(self.blog_link))

    def click_recently_viewed_link(self):
        self.for_click(self.find(self.recently_viewed_link))

    def click_compare_product_link(self):
        self.for_click(self.find(self.compare_product_link))

    def click_new_products_link(self):
        self.for_click(self.find(self.new_products_link))

    def assert_news_page(self):
        assert self.find(self.news_assert).text == "News"

    def assert_blog_page(self):
        assert self.find(self.blog_assert).text == "Blog"

    def assert_recently_viewed_page(self):
        assert self.find(self.recently_viewed_assert).text == "Recently viewed products"

    def assert_compare_products_page(self):
        assert self.find(self.compare_assert).text == "Compare products"

    def assert_new_products_page(self):
        assert self.find(self.new_products_assert).text == "New products"

    def click_empty_search_button(self):
        self.for_click(self.find(self.empty_search_button))

    def assert_minimum_search_warning(self):
        assert self.find(self.warning_minimum).text == "Search term minimum length is 3 characters"

    def assert_invalid_search_warning(self):
        assert self.find(self.warning_invalid).text == "No products were found that matched your criteria."

    def assert_blog_title(self):
        assert self.find(self.blog_title).text == "Customer Service - Client Service"

    def assert_blog_link_text(self):
        assert self.find(self.blog_link_text).text == "Blog posts tagged with 'e-commerce'"