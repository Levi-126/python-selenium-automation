from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify {amount} Story Cards for Target Circle Page")
def verify_story_card_amount(context, amount):
    amount = int(amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="@web/SlingshotComponents/common/Storyblock"]')
    print('\nStory Card Elements: ')
    print(links)
    assert len(links) == amount, f'Expected {amount} links but got {len(links)}'



# SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton'][id*='addToCartButton']")
SELECT_TO_VIEW_THE_CART = (By.CSS_SELECTOR, "a[href='/cart']")
SUBTOTAL_TEXT = (By.XPATH, "//span[contains(text(), 'subtotal')]")

@then("Add Item to Cart")
def add_item_in_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(5)

@then("Confirm Add Item to Cart")
def cart_confirmation(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)

@then("Select The View Cart Option")
def cart_confirmation(context):
    context.driver.find_element(*SELECT_TO_VIEW_THE_CART).click()
    sleep(5)

@then("Verify Item In Cart Is {amount}")
def verify_item_count(context, amount):
    link = context.driver.find_element(*SUBTOTAL_TEXT).text
    assert f'{amount} item' in link, f"Expected {amount} items but got {link}"