from Pages.Contact_page import Contact_Pages
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from Utility import consolelogger
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("test_setup_and_setdown")

class Test_Contact:
    @pytest.mark.regresion
    def test_facebook(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_facebook()
        store.switch_to_window()
        try:
            wait=WebDriverWait(self.driver, 10)
            wait.until(EC.title_contains("NopCommerce | Facebook"))
            store1 = self.driver.title
            assert store1 == "NopCommerce | Facebook"
            log.info("Facebook link is active")
        except TimeoutException:
            log.error("Facebook page did not load in time or title does not match.")
    @pytest.mark.regresion
    def test_twitter(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_twitter()
        store.switch_to_window()
        try:
            wait=WebDriverWait(self.driver, 10)
            wait.until(EC.title_contains("nopCommerce (@nopCommerce) / X"))
            store1 = self.driver.title
            assert store1 == "nopCommerce (@nopCommerce) / X"
            log.info("Twitter link is active")
        except TimeoutException:
            log.error("Twitter page did not load in time or title does not match.")
        
    @pytest.mark.regresion
    def test_youtube(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_youtube()
        store.switch_to_window()
        try:
            wait=WebDriverWait(self.driver, 10)
            wait.until(EC.title_contains("nopCommerce - YouTube"))
            store1 = self.driver.title
            assert store1 == "nopCommerce - YouTube"
            log.info("YouTube link is active")
        except TimeoutException:
            log.error("YouTube page did not load in time or title does not match.")

    @pytest.mark.regresion
    def test_rss(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_Rss()
        log.info("Rss link is active")
    
    @pytest.mark.regresion
    def test_google(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_google()
        store.switch_to_window()
        try:
            wait=WebDriverWait(self.driver, 10)
            wait.until(EC.title_contains("Google Workspace Updates: New community features for Google Chat and an update on Currents "))
            store1 = self.driver.title
            assert store1 == "Google Workspace Updates: New community features for Google Chat and an update on Currents "
            log.info("Google link is active")
        except TimeoutException:
            log.error("Google page did not load in time or title does not match.")
