from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# Open the chrome browser and browser the application and maximize the window.
path  = "C:\\dev\\driver\\chrome\\chromedriver.exe"
Base_Url =  "https://www.southwest.com/"
driver = webdriver.Chrome(executable_path= path)
driver.get(Base_Url)
driver.maximize_window()
driver.implicitly_wait(5)

# Give the Depart palce name.
Depart_place = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_originationAirportCode']")
Depart_place.click()
Depart_place.send_keys("New York")
time.sleep(3)

# Give the Arival place name.
Arival_place = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_destinationAirportCode']")
Arival_place.click()
Arival_place.send_keys("New Orleans")
time.sleep(3)

# click on depart date calender.
dept_date = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_departureDate']")
dept_date.click()
time.sleep(5)

# Select Perticular date from depart date calender.
dept_selct_date = driver.find_element_by_xpath("//button[@id='calendar-66-2021-03-15']")
dept_selct_date.click()
time.sleep(5)

# click on arival date calender.
arival_date = driver.find_element_by_xpath("//input[@id='LandingAirBookingSearchForm_returnDate']")
arival_date.click()
time.sleep(5)


# Select Perticular date from arival date calender.
arival_selct_date = driver.find_element_by_xpath("//button[@id='calendar-69-2021-03-20']")
arival_selct_date.click()
time.sleep(5)

# take a screenshot of given data
destination_filename = "C:\\Users\91741\\Desktop\\screnshot\\test1.png"
try:
    driver.save_screenshot(destination_filename)
    print("Screenshot is saved")
except NotADirectoryError:
    print("No Such Directory Found")

# click on the search button.
search_btn = driver.find_element_by_xpath("//button[@id='LandingAirBookingSearchForm_submit-button']")
search_btn.click()
time.sleep(3)

# close the application
driver.quit()













