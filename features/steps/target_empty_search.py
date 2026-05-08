from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target Webpage')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(4)

@when('Select The Cart Icon')
def select_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()
    sleep(4)

@then('Verify The Cart Is Empty')
def verify_cart_empty(context):
    context.driver.find_element(By.XPATH, '//h1[contains(text(), "Your cart is empty")]')
    sleep(4)
