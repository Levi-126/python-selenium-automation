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


#Previously used code from Lana

# SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
#
#
# @then("Verify search results for {product} shown")
# def verify_search_results(context, product):
#     actual_result = context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
#     assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'




