from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select

class ComputersPage(BasePage):
    computers_menu = (By.CSS_SELECTOR, "ul[class='top-menu'] a[href='/computers']")
    desktops_link = (By.CSS_SELECTOR, "h2[class='title'] a[href='/desktops']")
    notebooks_link = (By.CSS_SELECTOR, "h2[class='title'] a[href='/notebooks']")
    accessories_link = (By.CSS_SELECTOR, "h2[class='title'] a[href='/accessories']")

    # Locators specific to product category pages
    sortBy_element = (By.XPATH, "//select[@id='products-orderby']")
    pageSize_element = (By.XPATH, "//select[@id='products-pagesize']")
    product_name_element = (By.XPATH, "//div[@class='product-name']//child::h1")
    click_desktop_first_element= (By.CSS_SELECTOR, "h2[class='product-title']")
    click_notebooks_first_element= (By.XPATH, "//h2[@class='product-title']//a[text()='14.1-inch Laptop']")
    click_accessories_first_element= (By.XPATH, "//h2[@class='product-title']//a[text()='TCP Self-Paced Training additional month']")
    grid=(By.XPATH,"//option[text()='Grid']")

    def _init_(self, driver):
        super().__init__(driver)

    def click_computers_menu(self):
        self.for_click(self.find(self.computers_menu))

    def click_desktops_link(self):
        self.for_click(self.find(self.desktops_link))

    def click_notebooks_link(self):
        self.for_click(self.find(self.notebooks_link))

    def click_accessories_link(self):
        self.for_click(self.find(self.accessories_link))

    def select_orderby(self, visible_text):
        sort_dropdown = Select(self.find(self.sortBy_element))
        sort_dropdown.select_by_visible_text(visible_text)

    def select_pagesize(self, visible_text):
        pagesize_dropdown = Select(self.find(self.pageSize_element))
        pagesize_dropdown.select_by_visible_text(visible_text)

    def select_viewmode(self):
        viewmode_element =self.find(self.grid)
        self.for_click(viewmode_element)

    def clickDesktop_first_product(self):
        click_desktop_first_elements = self.find(self.click_desktop_first_element)
        self.for_click(click_desktop_first_elements)

    def assert_Desktop_first_product(self):
        try:
            assert "Build your own cheap computer" in self._driver.title
        except AssertionError:
            print("Page does not match")
            raise

    def clickNotebooks_first_product(self):
        click_notebooks_first_element = self.find(self.click_notebooks_first_element)
        self.for_click(click_notebooks_first_element)

    def assert_Notebook_first_product(self):
        try:
            assert "14.1-inch Laptop" in self._driver.title
        except AssertionError:
            print("Page does not match")
            raise

    def clickAccessories_first_product(self):
        click_accessories_first_element = self.find(self.click_accessories_first_element)
        self.for_click(click_accessories_first_element)

    def assert_Accessories_first_product(self):
        try:
            assert "TCP Self-Paced Training additional month" in self._driver.title
        except AssertionError:
            print("Page does not match")
            raise