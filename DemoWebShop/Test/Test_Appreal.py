from Pages.Appareal_page import Appreal
from Utility import consolelogger
import pytest
@pytest.mark.usefixtures("test_setup_and_setdown")

class Test_Appreal:
    @pytest.mark.retest
    def test_z_To_a(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.click_appreal()
        store.click_sortby()
        store.z_to_a()
        store.click_display()
        store.option()
        store.click_viewas()
        store.click_element()
        store.sucess_msg()
        log.info("Successfully Viewed")
    
    @pytest.mark.retest
    def test_a_to_z(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.click_appreal()
        store.click_sortby()
        store.a_to_z()
        store.click_display()
        store.option()
        store.click_viewas()
        store.click_element()
        store.atoz_success()
        log.info("Showed result for a to z")
    
    @pytest.mark.retest
    def test_low_high(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.click_appreal()
        store.click_sortby()
        store.low_to_high()
        store.click_display()
        store.click_viewas()
        store.click_element()
        store.low_success()
        log.info("low to high is success")
    
    @pytest.mark.retest
    def test_high_low(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.click_appreal()
        store.click_sortby()
        store.high_to_low()
        store.click_display()
        store.click_viewas()
        store.click_element()
        store.high_success()
        log.info("high to low is worked successful")
    
    @pytest.mark.retest
    def test_createdon(self):
        log=consolelogger.get_logger()
        store=Appreal(self.driver)
        store.click_appreal()
        store.click_sortby()
        store.click_createdon()
        store.click_viewas()
        store.viewas_list()
        store.click_display()
        store.option()
        store.click_element()
        store.createdon_success()
        log.info("Created on successfull")