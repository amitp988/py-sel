from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path  = "C:\\dev\\\driver\\chrome\\chromedriver.exe"
base_url = "https://learn.letskodeit.com/p/practice"
driver = webdriver.Chrome(executable_path= path)
driver.maximize_window()
driver.get(base_url)
radio_btn1 = driver.find_element(By.XPATH, "//input[@id = 'bmwradio']" )
radio_btn1.click()
time.sleep(5)
radio_btn2 = driver.find_element(By.XPATH, "//input[@id ='hondaradio']")
radio_btn2.click()
time.sleep(5)
radio_btn3 = driver.find_element(By.XPATH, "//input[@id ='benzradio']")
radio_btn3.click()
driver.close()


