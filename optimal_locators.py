from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://stackoverflow.com/users/signup')
sleep(4)


#Locator For "Create Your Account"
driver.find_element(By.XPATH, "//h1[contains(text(), 'Create your account')]")

#Locator For Agree To Terms Sentence
driver.find_element(By.XPATH, "//div[contains(text(), 'By clicking')]")

#Locator For Email
driver.find_element(By.CSS_SELECTOR,'input#email')

#Locator For Password
driver.find_element(By.CSS_SELECTOR,'input#password')

#Locator To Show Password Button
driver.find_element(By.CSS_SELECTOR,'svg.js-show-password.svg-icon')

#Locator For Sign Up Button
driver.find_element(By.CSS_SELECTOR,'button#submit-button')

#Locator For Google Sign Up Button
driver.find_element(By.CSS_SELECTOR,'button.s-btn__google.bar-md')

#Locator For GitHub Sign Up Button
driver.find_element(By.CSS_SELECTOR,'button.s-btn__github.bar-md')

#Locator For Get Stack Overflow Internal Sentence
driver.find_element(By.XPATH,"//a[contains(text(), 'Get Stack Overflow Internal free for up to 50 users')]")


