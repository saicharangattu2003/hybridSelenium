from selenium.webdriver.support import expected_conditions as Ec 
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep
class WebDriverHelper:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
    
    def click_on_element(self,locator):
        element = self.wait.until(
            Ec.element_to_be_clickable(locator)
        )
        # element = self.driver.find_element(*locator)
        element.click()

    def send_keys_to_element(self,locator, text):
        element = self.wait.until(
            Ec.visibility_of_element_located(locator)
        )
        # element = self.driver.find_element(*locator)
        element.send_keys(text) 
    
    def scroll_by_pixel(self,value):
        self.driver.execute_script("windows.scrollBy(0,value)");
        sleep(2)
    def scroll_to_element(self,locator):
        element = self.wait.until(
            Ec.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
    



