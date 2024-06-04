from Pages.Contact_page import Contact_Pages
import pytest
from Utility import consolelogger
@pytest.mark.usefixtures("test_setup_and_setdown")

class Test_Contact:
    def test_facebook(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_facebook()
        log.info("Facebook link is active")
    
    def test_twitter(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_twitter()
        log.info("Twitter link is active")
    
    def test_youtube(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_youtube()
        log.info("Youtube link is active")
    
    def test_rss(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_Rss()
        log.info("Rss link is active")
    
    def test_google(self):
        log=consolelogger.get_logger()
        store=Contact_Pages(self.driver)
        store.do_click_google()
        log.info("Google link is active")
        
