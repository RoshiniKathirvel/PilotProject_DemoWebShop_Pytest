from Utility import read_config
from Pages.Register_page import RegisterPage
from Utility import consolelogger
import pytest
@pytest.mark.usefixtures("test_setup_and_setdown")
class Test_register:
    def  test_valid_female_register(self):
        log=consolelogger.get_logger()
        store=RegisterPage(self.driver)
        store.click_register()
        store.click_female()
        store.enter_first(read_config.get_config("register info","first"))
        store.enter_last(read_config.get_config("register info","last"))
        store.enter_email(store.random_email())
        store.enter_pass(read_config.get_config("register info","password"))
        store.enter_con_pass(read_config.get_config("register info","confirmpass"))
        store.click_register_btn()
        store.register_Success()
        log.info("New Female user Register into the application")
    
    def test_valid_male_register(self):
        log=consolelogger.get_logger()
        store=RegisterPage(self.driver)
        store.click_register()
        store.enter_first(read_config.get_config("register info","first_name"))
        store.enter_last(read_config.get_config("register info","last_name"))
        store.enter_email(store.random_email())
        store.enter_pass(read_config.get_config("register info","password_l"))
        store.enter_con_pass(read_config.get_config("register info","confirm_pass"))
        store.click_register_btn()
        store.register_Success()
        log.info("New Male user registered into the application")
    
    def test_exist_user(self):
        log=consolelogger.get_logger()
        store=RegisterPage(self.driver)
        store.click_register()
        store.click_female()
        store.click_register_btn()
        store.register_invalid_succ()
        log.info("Existing user..")