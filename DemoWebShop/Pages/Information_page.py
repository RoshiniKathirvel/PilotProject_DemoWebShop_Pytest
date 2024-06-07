from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class Informationmodule(BasePage):
    sitemap_l=(By.XPATH, "//a[text()='Sitemap']")
    shipping_l=(By.XPATH,"//a[text()='Shipping & Returns']")
    privacy_l = (By.XPATH, "//a[text()='Privacy Notice']")
    condition_l = (By.XPATH, "//a[text()='Conditions of Use']")
    about_l = (By.XPATH, "//a[text()='About us']")
    contact_l = (By.XPATH, "//a[text()='Contact us']")
    pagetitle = (By.XPATH, "//div[@class='page-title']/h1")


    def __init__(self, driver):
        super().__init__(driver)
    
    def click_sitemap(self):
       sitemap=self.find(self.sitemap_l)
       self.for_click(sitemap)
    
    def click_shipping(self):
        shipping=self.find(self.shipping_l)
        self.for_click(shipping)

    def click_privacy(self):
        privacy=self.find(self.privacy_l)
        self.for_click(privacy)
    
    def click_condition(self):
        condition=self.find(self.condition_l)
        self.for_click(condition)

    def click_about(self):
        about=self.find(self.about_l)
        self.for_click(about)
    
    def click_contact(self):
        contact=self.find(self.contact_l)
        self.for_click(contact)



    
