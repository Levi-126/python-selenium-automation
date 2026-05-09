from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

@when('Select the Target Circle Icon')
def select_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, '#utilityNav-circle').click()
    sleep(2)


# @when("Search for {product}")
# def search_product(context, product):
#     context.driver.find_element(*SEARCH_FIELD).send_keys(product)
#     context.driver.find_element(*SEARCH_BTN).click()
#     sleep(7)
#
#
# @when('Click on Cart icon')
# def click_cart(context):
#     context.driver.find_element(*CART_ICON).click()


#Additional steps for checking login (Material from Lesson #3)
# @when('Select Your Account')
# def select_my_account(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]').click()
#     sleep(2)

# @when('Choose To Sign In')
# def choose_sign_in(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()
#
# @then('Verify Log In Is Possible')
# def log_in_possible(context):
#     context.driver.find_element(By.XPATH, '//h1[contains(text(), "Sign in or create account")]')
#     sleep(3)