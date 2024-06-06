from Utility import read_config
from Pages.base_page import BasePage
from Utility.read_config import get_config
from Pages.login_page import Loginpage
from Utility import consolelogger
import pytest
@pytest.mark.usefixtures("test_setup_and_setdown")

class Test_Login:
    def test_login(self):
        log=consolelogger.get_logger()
        call=Loginpage(self.driver)
        call.click_login()
        call.enter_email(read_config.get_config("login info","user"))
        call.enter_pass(read_config.get_config("login info","pas"))
        call.click_loginbtn()
        call.login_success()
        log.info("Login Successful..")
    
    def test_invalid_username(self):
        log1=consolelogger.get_logger()
        calls=Loginpage(self.driver)
        calls.click_login()
        calls.enter_email(read_config.get_config("login info","inv_user"))
        calls.enter_pass(read_config.get_config("login info","val_pass"))
        calls.click_loginbtn()
        calls.invalid_login_success()
        log1.info("Invalid credentials.. Not Login into the application")
    
    def test_invalid_password(self):
        logs=consolelogger.get_logger()
        get=Loginpage(self.driver)
        get.click_login()
        get.enter_email(read_config.get_config("logins info","val_user"))
        get.enter_pass(read_config.get_config("logins info","inv_pass"))
        get.click_loginbtn()
        get.invalid_login_success()
        logs.info("Invalid credentials.. Not Login into the application")
    
    def test_invalid_credentials(self):
        logs=consolelogger.get_logger()
        get=Loginpage(self.driver)
        get.click_login()
        get.enter_email(read_config.get_config("logins info","invalid_user"))
        get.enter_pass(read_config.get_config("logins info","invalid_pass"))
        get.click_loginbtn()
        get.invalid_login_success()
        logs.info("Invalid credentials.. Not Login into the application")