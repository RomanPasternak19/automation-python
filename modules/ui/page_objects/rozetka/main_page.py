from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "https://rozetka.com.ua/ua/"


    def __init__(self) -> None:
        super().__init__()


    def __format_conversion(expression):
        
        return int(expression.text.replace(' ', '')[:-1])


    def visit(self):
        self.driver.get(MainPage.URL)

    
    def wait_element(self, selector, selector_value):
        wait = WebDriverWait(self.driver, 10)

        return wait.until(EC.presence_of_element_located((selector, selector_value)))


    def search_item(self, name):
        search_input = self.driver.find_element(By.NAME, "search")
        search_input.send_keys(name)
        submit_button = self.driver.find_element(By.CLASS_NAME, "search-form__submit")
        submit_button.click()
    

    def add_item_to_basket(self):
        # wait = WebDriverWait(self.driver, 10)
        # basket_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "goods-tile__buy-button")))
        basket_icon = MainPage.wait_element(self, By.CLASS_NAME, "goods-tile__buy-button")
        basket_icon.click()
    

    def open_shopping_cart(self):
        basket = self.driver.find_element(By.CSS_SELECTOR, ".header__button.header__button--active.ng-star-inserted")
        basket.click()


    def open_catalogue_menu(self):
        self.driver.set_window_size(1100, 700)
        
        catalogue_button = self.driver.find_element(By.ID, "fat-menu")
        catalogue_button.click()


    def select_category_by_name(self, name):
        category = self.driver.find_element(By.LINK_TEXT, name)
        category.click()
    
    
    def check_item_name(self, name):
        items_name = self.driver.find_element(By.CLASS_NAME, "goods-tile__title")
        
        return name in items_name.text

    
    def check_product_added_to_cart(self, quantityOfGoods):
        badge_inserted = MainPage.wait_element(self,By.CSS_SELECTOR, ".badge.badge--green.ng-star-inserted")

        return int(badge_inserted.text) == quantityOfGoods
    

    def check_sum_in_basket(self):
        MainPage.wait_element(self, By.CSS_SELECTOR, ".cart-product__price.cart-product__price--red")

        price_elements = self.driver.find_elements(By.CSS_SELECTOR, ".cart-product__price.cart-product__price--red")
        first_price = MainPage.__format_conversion(price_elements[0])
        second_price = MainPage.__format_conversion(price_elements[1])
        sum_element = self.driver.find_element(By.CSS_SELECTOR, ".cart-receipt__sum-price")
        sum = MainPage.__format_conversion(sum_element)
        
        return sum == (first_price + second_price)
    

    def check_category_heading(self, expected_name):
        heading = MainPage.wait_element(self, By.CLASS_NAME, "portal__heading")
        
        return heading.text == expected_name