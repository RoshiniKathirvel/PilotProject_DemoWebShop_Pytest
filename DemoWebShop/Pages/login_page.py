from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Utility import read_config

class Loginpage(BasePage):
    login=(By.XPATH,"//a[text()='Log in']")
    email=(By.XPATH,"//input[@class='email']")
    password=(By.XPATH,"//input[@class='password']")
    login_btn=(By.XPATH,"//input[@class='button-1 login-button']")
    login_msg=(By.XPATH,"//a[text()='j.k.rose1@gmail.com']")
    invalid_msg=(By.XPATH,"//div[@class='message-error']")
    blank_invalid=(By.XPATH,"//div[@class='validation-summary-errors']")

    def _init_(self, driver):
        super()._init_(driver)
    
    def click_login(self):
        clogin=self.find(self.login)
        self.for_click(clogin)
    
    def enter_email(self,value):
        emails=self.find(self.email)
        self.for_send_keys(emails,value)
    
    def enter_pass(self,value):
        pas=self.find(self.password)
        self.for_send_keys(pas,value)
    
    def click_loginbtn(self):
        log_btn=self.find(self.login_btn)
        self.for_click(log_btn)
    
    def login_success(self):
        suc=self.find(self.login_msg).text
        assert suc==(read_config.get_config("login info","user"))
        
    def invalid_login_success(self):
        msg=self.find(self.invalid_msg).text
        assert msg=="Login was unsuccessful. Please correct the errors and try again.\nThe credentials provided are incorrect"

    def blanks_invalid(self):
        msg=self.find(self.blank_invalid).text
        assert msg== "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"