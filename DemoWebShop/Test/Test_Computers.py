import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from Pages.ComputersPage import ComputersPage

@pytest.mark.usefixtures("test_setup_and_setdown")
class Test_Computer:


    @pytest.mark.smoke
    def test_select_desktops(self):
        computers_page = ComputersPage(self.driver)
        computers_page.click_computers_menu()
        computers_page.click_desktops_link()
        sort_dropdown = Select(computers_page.find(computers_page.sortBy_element))
        sort_dropdown.select_by_visible_text("Name: A to Z")
        pagesize_dropdown = Select(computers_page.find(computers_page.pageSize_element))
        pagesize_dropdown.select_by_visible_text("4")
        computers_page.select_viewmode()  # Grid
        computers_page.clickDesktop_first_product()
        computers_page.assert_Desktop_first_product()

    def test_select_notebooks(self):
        computers_page = ComputersPage(self.driver)
        computers_page.click_computers_menu()
        computers_page.click_notebooks_link()
        sort_dropdown = Select(computers_page.find(computers_page.sortBy_element))
        sort_dropdown.select_by_visible_text("Price: Low to High")
        pagesize_dropdown = Select(computers_page.find(computers_page.pageSize_element))
        pagesize_dropdown.select_by_visible_text("8")
        computers_page.select_viewmode()
        computers_page.clickNotebooks_first_product()
        print("Clicked on notebooks first product link.")
        computers_page.assert_Notebook_first_product()
        print("Assertion for notebooks first product completed.")

    def test_select_accessories(self):
        computers_page = ComputersPage(self.driver)
        computers_page.click_computers_menu()
        computers_page.click_accessories_link()
        sort_dropdown = Select(computers_page.find(computers_page.sortBy_element))
        sort_dropdown.select_by_visible_text("Created on")
        pagesize_dropdown = Select(computers_page.find(computers_page.pageSize_element))
        pagesize_dropdown.select_by_visible_text("8")
        computers_page.select_viewmode()
        computers_page.clickAccessories_first_product()
        print("Clicked on accessories first product link.")
        computers_page.assert_Accessories_first_product()
        print("Assertion for accessories first product completed.")