import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from Pages.Bookmodule_page import Bookmodule
from Pages.base_page import BasePage

# Using fixture
@pytest.mark.usefixtures("test_setup_and_setdown")
class TestBookmodule:
    # Using markers
    @pytest.mark.smoke
    def test_clickbookoption(self):
        bookoption = Bookmodule(self.driver)
        bookoption.click_book()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is("Demo Web Shop. Books"))
            actual_title = self.driver.title
            expected_title = "Demo Web Shop. Books"
            assert actual_title == expected_title
        except TimeoutException:
            print("The page is not loading as expected")

    def test_selectproduct(self):
        bookselect = Bookmodule(self.driver)
        bookselect.click_book()
        bookselect.select_product()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is("Demo Web Shop. Computing and Internet"))
            actual_title = self.driver.title
            expected_title = "Demo Web Shop. Computing and Internet"
            assert actual_title == expected_title
        except TimeoutException:
            print("The page is not loading as expected")

    @pytest.mark.smoke
    def test_display_option(self):
        display = Bookmodule(self.driver)
        display.click_book()
        display.change_display_size()

        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "products-pagesize")))
            select = Select(dropdown)
            select.select_by_visible_text("4")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "item-box")))
            # Find all product items
            products = self.driver.find_elements(By.CLASS_NAME, "item-box")
            # Assert that only 4 products are displayed
            assert len(products) == 4
        except TimeoutException:
            print("The page is not loaded as expected")

    @pytest.mark.smoke
    def test_position(self):
        position = Bookmodule(self.driver)
        position.click_book()
        position.select_position()
        try:
            dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Bookmodule.position_l))
            select = Select(dropdown)
            select.select_by_visible_text("Name: A to Z")
            product_names = position.get_product_names()
            assert product_names==sorted(product_names)
        except TimeoutException:
            print("The page is not loaded as expected")
            return
        
    @pytest.mark.smoke
    def test_click_filter(self):
        filter = Bookmodule(self.driver)
        filter.click_book()
        filter.apply_price_filter()
        remove_filter_element = self.driver.find_element(*Bookmodule.removefilter_l)
        element_text = remove_filter_element.text
        try:
            filterassert=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(Bookmodule.removefilter_l))
            assert "Remove Filter" in element_text, "Expected 'Remove Filter' not found in element text"
        except TimeoutException:
            print("The page is not loaded as expected")
    @pytest.mark.smoke
    def test_remove_filter(self):
        filter = Bookmodule(self.driver)
        filter.click_book()
        filter.apply_price_filter()
        filter.remove_filter()
        try:
            removefilterasser = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='filter-title']/strong"))
            )
            filter_title = removefilterasser.text
            assert "Filter by price" in filter_title
        except TimeoutException:
            print("The page is not loading as expected")
        

            
         