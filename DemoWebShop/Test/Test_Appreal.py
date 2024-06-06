from Pages.Appareal_page import Appreal
from Utility import consolelogger
import pytest
@pytest.mark.usefixtures("test_setup_and_setdown")

class Test_Appreal:

    def test_click_z_To_a(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.appreal_click()
        store.sortby_click()
        store.z_to_a()
        store.display_click()
        store.option()
        store.viewas_click()
        store.click_element()
        store.sucess_msg()
        log.info("Successfully Viewed")
    
    def test_a_to_z(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.appreal_click()
        store.sortby_click()
        store.a_to_z()
        store.display_click()
        store.option()
        store.viewas_click()
        store.click_element()
        store.atoz_success()
        log.info("Showed result for a to z")
    
    def test_low_high(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.appreal_click()
        store.sortby_click()
        store.low_to_high()
        store.display_click()
        store.viewas_click()
        store.click_element()
        store.low_success()
        log.info("low to high is success")
    
    def test_high_low(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.appreal_click()
        store.sortby_click()
        store.high_to_low()
        store.display_click()
        store.viewas_click()
        store.click_element()
        store.high_success()
        log.info("high to low is worked successful")
    
    def test_createdon(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.appreal_click()
        store.sortby_click()
        store.createdon()
        store.viewas_click()
        store.viewas_list()
        store.display_click()
        store.option()
        store.click_element()
        store.createdon_success()
        log.info("Created on successfull")