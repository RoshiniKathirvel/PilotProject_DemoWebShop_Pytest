from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
class Appreal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    appreal=(By.CSS_SELECTOR,"a[href='/apparel-shoes']")
    sort_by=(By.ID,"products-orderby")
    view_as=(By.ID,"products-pagesize")
    display=(By.ID,"products-viewmode")
    atoz=(By.XPATH,"//option[text()='Name: A to Z']")
    ztoa=(By.XPATH,"//option[text()='Name: Z to A']")
    option_4=(By.XPATH,"//option[text()='4']")
    click_ele=(By.XPATH,"//h2[@class='product-title']")
    check_pro=(By.CSS_SELECTOR,"div[class='product-name']")
    low_high=(By.XPATH,"//option[text()='Price: Low to High']")
    high_low=(By.XPATH,"//option[text()='Price: High to Low']")
    atoz_check=(By.XPATH,"//div[@class='product-name']")
    created_on=(By.XPATH,"//option[text()='Created on']")
    low_high_succ=(By.CSS_SELECTOR,"div.product-price")
    high_low_succ=(By.CSS_SELECTOR,"div[class='product-price']")
    viewas=(By.XPATH,"//option[text()='List']")
    created_sucess=(By.XPATH,"//div[@class='product-name']")
    def appreal_click(self):
        store=self.find(self.appreal)
        self.for_click(store)
    
    def sortby_click(self):
        store1=self.find(self.sort_by)
        self.for_click(store1)
    
    def z_to_a(self):
        store1=self.find(self.ztoa)
        self.for_click(store1)
    
    def a_to_z(self):
        store=self.find(self.atoz)
        self.for_click(store)
    
    def low_to_high(self):
        store=self.find(self.low_high)
        self.for_click(store)
    
    def high_to_low(self):
        store=self.find(self.high_low)
        self.for_click(store)
    
    def createdon(self):
        store=self.find(self.created_on)
        self.for_click(store)
    
    def viewas_click(self):
        store=self.find(self.view_as)
        self.for_click(store)
    
    def viewas_list(self):
        store=self.find(self.viewas)
        self.for_click(store)
    
    def display_click(self):
        store=self.find(self.display)
        self.for_click(store)
    
    def option(self):
        store=self.find(self.option_4)
        self.for_click(store)
    
    def click_element(self):
        store=self.find(self.click_ele)
        self.for_click(store)

    
    def sucess_msg(self):
        store1=self.find(self.check_pro).text
        assert store1.__eq__("Wool Hat")
    
    def atoz_success(self):
        store1=self.find(self.atoz_check).text
        assert store1.__eq__("50's Rockabilly Polka Dot Top JR Plus Size")
    
    def low_success(self):
        store=self.find(self.low_high_succ).text
        assert store.__eq__("1.00")
    
    def high_success(self):
        store=self.find(self.high_low_succ).text
        assert store.__eq__("40.00")
    
    def createdon_success(self):
        store=self.find(self.created_sucess).text
        assert store.__eq__("Green and blue Sneaker")