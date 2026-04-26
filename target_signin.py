from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.target.com/")
sleep(2)

driver.find_element(By.XPATH, "//span[@class='sc-40e81479-3 chaKyG display-name h-margin-r-x3']").click()
sleep(4)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(4)

element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in or create account')]")
print(element)

