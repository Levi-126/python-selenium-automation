from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Webpage')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@given('Open Guitar Search Webpage From Target')
def open_target(context):
    context.driver.get(
        "https://www.target.com/p/best-choice-products-beginner-electric-guitar-kit-w-headphone-amp-padded-gig-bag-headphones/-/A-1002264550?preselect=1002220988#lnk=sametab"
    )

