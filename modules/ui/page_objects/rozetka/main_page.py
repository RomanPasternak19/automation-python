from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    URL = "https://rozetka.com.ua/ua/"


    def __init__(self) -> None:
        super().__init__()


    def visit(self):
        self.driver.get(MainPage.URL)


    def search_item(self, name):
        search_input = self.driver.find_element(By.NAME, "search")
        search_input.send_keys(name)
        submit_button = self.driver.find_element(By.CLASS_NAME, "search-form__submit")
        submit_button.click()
    

    def add_item_to_basket(self):
        basket_icon = self.driver.find_element(By.CLASS_NAME, "goods-tile__buy-button")
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
        badge_inserted = self.driver.find_element(By.CSS_SELECTOR, ".badge.badge--green.ng-star-inserted")
        
        return int(badge_inserted.text) == quantityOfGoods


    def check_category_heading(self, expected_name):
        heading = self.driver.find_element(By.CLASS_NAME, "portal__heading")
        
        return heading.text == expected_name
    

    def check_sum_in_basket(self):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, ".cart-product__price.cart-product__price--red")
        first_price = int(price_elements[0].text.replace(' ', '')[:-1])
        second_price = int(price_elements[1].text.replace(' ', '')[:-1])
        sum_element = self.driver.find_element(By.CSS_SELECTOR, ".cart-receipt__sum-price")
        sum = int(sum_element.text.replace(' ', '')[:-1])

        return sum == (first_price + second_price)