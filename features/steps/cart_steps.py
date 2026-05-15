from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    # context.driver.find_element(By.XPATH, '//h1[contains(text(), "Your cart is empty")]')
    context.app.cart_page.verify_cart_empty()
