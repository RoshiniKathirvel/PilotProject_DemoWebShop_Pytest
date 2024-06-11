from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self._driver=driver
        self._wait=WebDriverWait(self._driver,30)
        self._action=ActionChains(self._driver)
    
    def for_send_keys(self,element,value):
        element.send_keys(value)

    def for_click(self,element):
        element.click()
    
    def find(self,locator):
        return self._driver.find_element(*locator)

    
    
    def wait_for_element(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))
    
    def switch_to_window(self):
        self._driver.switch_to.window(self._driver.window_handles[1])

    def find_all(self, locator):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located(locator))
