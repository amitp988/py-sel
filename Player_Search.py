from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path="C:\\dev\\driver\\chrome\\chromedriver.exe")
driver.get("https://www.cricbuzz.com/")
driver.implicitly_wait(10)
search_bar = driver.find_element_by_id("search_bar")
search_bar.click()
search_bar.send_keys('Sachin Tendulkar')
time.sleep(5)
search_btn = driver.find_elements_by_link_text("SEARCH")
search_btn.click()
