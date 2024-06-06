from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class Informationmodule(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sitemap_l = self.find((By.XPATH, "//a[text()='Sitemap']"))
        self.shipping_l = self.find((By.XPATH, "//a[text()='Shipping & Returns']"))
        self.privacy_l = self.find((By.XPATH, "//a[text()='Privacy Notice']"))
        self.condition_l = self.find((By.XPATH, "//a[text()='Conditions of Use']"))
        self.about_l = self.find((By.XPATH, "//a[text()='About us']"))
        self.contact_l = self.find((By.XPATH, "//a[text()='Contact us']"))
        self.pagetitle = self.find((By.XPATH, "//div[@class='page-title']/h1"))

    def click_sitemap(self):
        self.for_click(self.sitemap_l)
        self.get_page_title().__eq__('Sitemap')

    def click_shipping(self):
        self.for_click(self.shipping_l)
        self.get_page_title().__eq__('Shipping & Returns')

    def click_privacy(self):
        self.for_click(self.privacy_l)
        self.get_page_title().__eq__('Privacy Notice')

    def click_condition(self):
        self.for_click(self.condition_l)
        self.get_page_title().__eq__('Conditions of Use')

    def click_about(self):
        self.for_click(self.about_l)
        self.get_page_title().__eq__('About us')

    def click_contact(self):
        self.for_click(self.contact_l)
        self.get_page_title().__eq__('Contact us')

    def get_page_title(self):
        return self.pagetitle.text
    
