from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify The Cart Is Empty')
def verify_cart_empty(context):
    context.driver.find_element(By.XPATH, '//h1[contains(text(), "Your cart is empty")]')
    sleep(2)