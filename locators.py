# PLEASE NOTE THE SIGN-IN PAGE WAS NOT THE SAME AS OUR HOMEWORK EXAMPLE.
# 9 DIFFERENT LOCATORS WERE STILL ATTEMPTED.
# Your help with any corrections is much appreciated! Thank you!

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(2)

# Find Logo Icon
element1 = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
print(element1)

# Find Email Field
element2 = driver.find_element(By.ID, "ap_email_login")
print(element2)

# Find Continue button
element3 = driver.find_element(By.XPATH, "//input[@class = 'a-button-input']")
print(element3)

# Conditions of use link
element4 = driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")
print(element4)

# Privacy Notice link
element5 = driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")
print(element5)

# Need help link
element6 = driver.find_element(By.XPATH, "//span[@class='a-list-item']")
print(element6)

# Buying For Work Text
element7 = driver.find_element(By.XPATH, "//span[@class='a-text-bold']")
print(element7)

# Other issues with Sign-In link
element8 = driver.find_element(By.ID, "ab-registration-ingress-link")
print(element8)

# Help Button On The Bottom
element9 = driver.find_element(By.XPATH, "//a[@href='/help']")
print(element9)




