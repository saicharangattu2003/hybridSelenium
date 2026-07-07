from uistore.jiomart_locators import JioMartLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from time import sleep
from utilities.webDriverHelper import WebDriverHelper
class JioMartPage:
    def __init__(self,driver):
        self.driver = driver
        self.helper = WebDriverHelper(self.driver)

    def click_cross_button(self):
        self.helper.click_on_element(JioMartLocators.cross_button)

    def enter_hinjewadi(self):
        self.helper.send_keys_to_element(JioMartLocators.input_textarea,"hinjewadi")
        self.helper.send_keys_to_element(JioMartLocators.input_textarea,Keys.SPACE)
        self.helper.click_on_element(JioMartLocators.input_textarea)
    def select_hinje(self):
        self.helper.click_on_element(JioMartLocators.select_hinje)
    def click_confirm(self):
        self.helper.click_on_element(JioMartLocators.confirm_button)
        sleep(3)
    def click_shop(self):
        self.helper.click_on_element(JioMartLocators.shop_all)
        sleep(2)
    def search_chips(self):
        self.helper.click_on_element(JioMartLocators.search_bar)
        self.helper.send_keys_to_element(JioMartLocators.search_bar,"Chips")
        self.helper.send_keys_to_element(JioMartLocators.search_bar,Keys.ENTER)
        sleep(3)
    
        
    def click_first_prod(self):
        self.helper.click_on_element(JioMartLocators.first_prod)
    
    def scroll_to_about_us(self):
        self.helper.scroll_to_element(JioMartLocators.about_us)
        sleep(4)

    def click_least_price(self):
        prices = self.driver.find_elements(*JioMartLocators.all_prices)
        new_list = []
        for item in prices:
            price = item.text[1:]
            price = item.text.replace(",","")
            new_list.append(price) 
        min_price = min(new_list) 
        # with open("prices.txt","w",encoding="utf-8") as f:
        #     f.write(min_price)
        
        for item in prices:
            if item.text == min_price:
                item.click()
                sleep(5)
                break
            
        # with open("prices.txt","w",encoding="utf-8") as f:
        #     for item in prices:
        #         f.write(item.text+"\n") 
        #         new_list.append(item.text[1:]) 
        # # print(new_list)
        # min_value = min(new_list)
        # for item in prices:
        #     if item.text == min_value:
        #         item.click()
        #         sleep(4)
        #         break

        
        # min_price = min(prices)
        # for item in prices:
        #     if item.text() == min_price:
        #         item.click()
        # min_price.click() 
        # print(min_price)


    def JioMartPageMethods(self):
        self.click_cross_button()
        self.enter_hinjewadi()
        self.select_hinje()
        self.click_confirm()
        self.click_shop()
        self.search_chips()
        self.click_least_price()
        # self.click_first_prod()
        # self.scroll_to_about_us()

# check weather its coming or not ?
