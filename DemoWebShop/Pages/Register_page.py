import random
import string
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Utility import read_config
from Utility.read_config import get_config
class RegisterPage(BasePage):
    register=(By.XPATH,"//a[text()='Register']")
    female=(By.CSS_SELECTOR,"input#gender-female")
    male=(By.CSS_SELECTOR,"input#gender-male")
    firstname=(By.XPATH,"//input[@id='FirstName']")
    lastname=(By.XPATH,"(//input[@class='text-box single-line'])[2]")
    email=(By.CSS_SELECTOR,"input#Email")
    password=(By.CSS_SELECTOR,"input#Password")
    con_pass=(By.XPATH,"(//input[@type='password'])[2]")
    reg_button=(By.CSS_SELECTOR,"input#register-button")
    suc_msg=(By.CSS_SELECTOR,"div[class='result']")
    first_name=(By.XPATH,"//span[text()='First name is required.']")

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_register(self):
        store=self.find(self.register)
        self.for_click(store)
        
    def click_female(self):
        store=self.find(self.female)
        self.for_click(store)
    
    def click_male(self):
        store=self.find(self.male)
        self.for_click(store)
    
    def enter_first(self,value):
        store=self.find(self.firstname)
        self.for_send_keys(store,value)
    
    def enter_last(self,value):
        store=self.find(self.lastname)
        self.for_send_keys(store,value)
    
    def enter_email(self,value):
        store=self.find(self.email)
        self.for_send_keys(store,value)
    
    def enter_pass(self,value):
        store=self.find(self.password)
        self.for_send_keys(store,value)
        
    def enter_con_pass(self,value):
        store=self.find(self.con_pass)
        self.for_send_keys(store,value)
    
    def click_register_btn(self):
        store=self.find(self.reg_button)
        self.for_click(store)
    
    def register_Success(self):
        store=self.find(self.suc_msg).text
        assert store=="Your registration completed"
    
    def register_invalid_succ(self):
        store=self.find(self.first_name).text
        assert store.__eq__("First name is required.")
    
    def random_email(self, char_num=7):
        random_email = ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))
        return random_email + "@gmail.com"
    
