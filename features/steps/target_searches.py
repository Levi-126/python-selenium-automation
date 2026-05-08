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
    sleep(2)

@when('Select Your Account')
def select_my_account(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]').click()
    sleep(2)

@when('Choose To Sign In')
def choose_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()

@then('Verify Log In Is Possible')
def log_in_possible(context):
    context.driver.find_element(By.XPATH, '//h1[contains(text(), "Sign in or create account")]')
    sleep(3)

