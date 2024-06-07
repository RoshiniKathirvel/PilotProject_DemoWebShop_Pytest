import pytest
from Pages.ComputerService import ComputerService

@pytest.mark.usefixtures("test_setup_and_setdown")
class Test_ComputerService:

    def test_validate_search_field(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_search()
        computers_page.search_product("computer")
        assert computers_page.get_product_count() == 4

    def test_validate_news_field(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_news_link()
        computers_page.assert_news_page()

    def test_validate_blog_field(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_blog_link()
        computers_page.assert_blog_page()

    def test_validate_recently_viewed_products(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_recently_viewed_link()
        computers_page.assert_recently_viewed_page()

    def test_validate_compare_product_list(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_compare_product_link()
        computers_page.assert_compare_products_page()

    def test_validate_new_products(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_new_products_link()
        computers_page.assert_new_products_page()

    def test_validate_empty_search_product(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_empty_search_button()
        # Handle alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert "Alert message" in alert_text  # Replace "Alert message" with the actual alert text
        alert.accept()

    def test_validate_minimum_search(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_computers_menu()
        computers_page.search_product("12")
        computers_page.assert_minimum_search_warning()

    def test_validate_invalid_search(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_computers_menu()
        computers_page.search_product("chocho")
        computers_page.assert_invalid_search_warning()

    def test_validate_blog_links(self, driver):
        computers_page = ComputerService(driver)
        computers_page.click_blog_link()
        computers_page.assert_blog_title()
        # Assuming the page reloads with the blog posts after clicking the blog link
        computers_page.assert_blog_link_text()