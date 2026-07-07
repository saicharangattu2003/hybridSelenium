from selenium.webdriver.common.by import By
class JioMartLocators:
    cross_button = (By.XPATH,"//button[@aria-label='Close']")
    input_textarea = (By.XPATH,"//input[@placeholder='Search for area, landmark']")
    select_hinje = (By.CLASS_NAME,"pac-item")
    shop_all = (By.XPATH,"//span[text()='Shop all']") 
    confirm_button = (By.CLASS_NAME,"AddressFullscreenModal__confirm-button")
    search_bar = (By.XPATH,"//input[@class='SearchInput__searchInput SearchSection__searchInput']") 
    first_prod = (By.XPATH,"//div[@class='productContainer']//h3[@class='productCard__productTitle']")
    about_us = (By.XPATH,"//label[text()='About Us']")
    all_prices = (By.CLASS_NAME,"PriceContainer__currentPrice") 
    