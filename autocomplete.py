from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

path  = "C:\\dev\\driver\\chrome\\chromedriver.exe"
Base_Url =  "https://www.southwest.com/"
driver = webdriver.Chrome(executable_path= path)
driver.get(Base_Url)
driver.maximize_window()
driver.implicitly_wait(5)

Depart_plc = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_originationAirportCode']")
Depart_plc.click()
Depart_plc.send_keys("New York")
time.sleep(3)

Arival_plc = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_destinationAirportCode']")
Arival_plc.click()
Arival_plc.send_keys("New Orleans")
time.sleep(3)

dept_date = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_departureDate']")
dept_date.click()
time.sleep(5)

selct_dt_1 = driver.find_element_by_xpath("//button[@id='calendar-66-2021-03-06']")
selct_dt_1.click()
time.sleep(5)

arival_date = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_returnDate']")
arival_date.click()
time.sleep(5)

selct_dt_2 = driver.find_element_by_xpath("//button[@id='calendar-69-2021-04-03']")
selct_dt_2.click()
time.sleep(5)

search_btn = driver.find_element_by_xpath("//button[@id='LandingAirBookingSearchForm_submit-button']")
search_btn.click()
time.sleep(3)

driver.quit()





