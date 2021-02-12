from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path = "C:\\dev\\driver\\chrome\\chromedriver.exe"
baseurl = "https://letskodeit.teachable.com/"
driver = webdriver.Chrome(path)
driver.get(baseurl)
signin_btn = driver.find_element(By.LINK_TEXT, "Login")
signin_btn.click()
time.sleep(5)
email_btn = driver.find_element(By.XPATH, "//input[@id='user_email']")
email_btn.click()
email_btn.send_keys("amitpatnaik988@gmail.com")
passwrd_btn = driver.find_element(By.XPATH, "//input[@id='user_password']")
passwrd_btn.click()
passwrd_btn.send_keys("Amiy@1234")
submt_btn = driver.find_element(By.NAME, "commit")
submt_btn.click()