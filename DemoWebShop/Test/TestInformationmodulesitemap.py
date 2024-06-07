from Pages.informationmodulepage import Informationmodule
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("test_setup_and_setdown")  #Using fixtures

class TestContact:
    #using markers
    @pytest.mark.smoke
    #Test Case for sitemap page
    def test_sitemap(self):
        sitemap_page = Informationmodule(self.driver)
        sitemap_page.click_sitemap()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("Sitemap"))
            title = self.driver.title
            print(title)
            assert title == "Demo Web Shop. Sitemap"
        except TimeoutException:
            pytest.fail("Sitemap page did not load as expected")
    #Test Case for Shipping page
    @pytest.mark.smoke
    def test_shipping(self):
        shipping_page = Informationmodule(self.driver)
        shipping_page.click_shipping()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("Shipping"))
            title = self.driver.title
            print(title)
            assert title == "Demo Web Shop. Shipping & Returns"
        except TimeoutException:
            pytest.fail("Shipping and returns page did not load as expected")
    #Test case for privacy page
    @pytest.mark.smoke
    def test_privacy(self):
        privacy_page = Informationmodule(self.driver)
        privacy_page.click_privacy()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("Privacy policy"))
            title = self.driver.title
            print(title)
            assert title == "Demo Web Shop. Privacy policy"
        except TimeoutException:
            pytest.fail("Privacy notice page did not load as expected")
    #Test case for about page
    @pytest.mark.smoke
    def test_about(self):
        about_page = Informationmodule(self.driver)
        about_page.click_about()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("About"))
            title = self.driver.title
            print(title)
            assert title == "Demo Web Shop. About Us"
        except TimeoutException:
            pytest.fail("About us page did not load as expected")
    #Test case for contact page
    @pytest.mark.smoke
    def test_contact(self):
        contact_page = Informationmodule(self.driver)
        contact_page.click_contact()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("Contact"))
            title = self.driver.title
            print(title)
            assert title == "Demo Web Shop. Contact Us"
        except TimeoutException:
            pytest.fail("Contact us page did not load as expected")
    #Test case for condition page
    @pytest.mark.smoke
    def test_condition(self):
        condition_page = Informationmodule(self.driver)
        condition_page.click_condition()
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("Conditions"))
            title = self.driver.title
            print(title)
            assert title == "Demo Web Shop. Conditions of use"
        except TimeoutException:
            pytest.fail("Conditions of use page did not load as expected")