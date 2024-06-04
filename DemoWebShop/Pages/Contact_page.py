from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
class Contact_Pages(BasePage):
    facebook=(By.XPATH,"//a[text()='Facebook']")
    twitter=(By.XPATH,"//a[text()='Twitter']")
    rss=(By.XPATH,"//a[text()='RSS']")
    you=(By.XPATH,"//a[text()='YouTube']")
    google=(By.XPATH,"//a[text()='Google+']")
    def __init__(self, driver):
        super().__init__(driver)

    def do_click_facebook(self):
        store=self.find(self.facebook)
        self.for_click(store)

    def do_click_twitter(self):
        clicks=self.find(self.twitter)
        self.for_click(clicks)
    
    def do_click_Rss(self):
        cli=self.find(self.rss)
        self.for_click(cli)
    
    def do_click_youtube(self):
        you=self.find(self.you)
        self.for_click(you)
    
    def do_click_google(self):
        googles=self.find(self.google)
        self.for_click(googles)