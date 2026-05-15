from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CartPage(Page):

    EMPTY_CART_MESSAGE = (By.XPATH, '//h1[contains(text(), "Your cart is empty")]')

    def verify_cart_empty(self):
        empty_cart = self.driver.find_element(*self.EMPTY_CART_MESSAGE).text
        assert empty_cart == 'Your cart is empty', f'The cart is not empty'

