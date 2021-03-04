from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time

class BookingFlight():
    def Bok_flight(self):
        path  = "C:\\dev\\driver\\chrome\\chromedriver.exe"
        Base_Url =  "https://www.booking.com/"
        driver = webdriver.Chrome(executable_path= path)
        driver.maximize_window()
        driver.get(Base_Url)
        driver.implicitly_wait(20)

        Flight_tab = driver.find_element(By.XPATH, "//span[contains (text(),'Flights')]")
        Flight_tab.click()
        time.sleep(5)
        # Frm_btn = driver.find_element(By.XPATH, "//div[@aria-label = 'Flight origin input']")
        # Frm_btn.send_keys('BBI')
        # Frm_btn.send_keys(Keys.ENTER)
        # time.sleep(10)

        # To_btn = driver.find_element(By.XPATH, "//div[@aria-label = 'Flight destination input']")
        # To_btn.send_keys('BLR')
        # To_btn.send_keys(Keys.ENTER)
        # time.sleep(10)

        dept_dat = driver.find_element(By.CLASS_NAME, "//div[@id='p_AT-depart']")
        dept_dat.click()
        time.sleep(5)

        datToselt1 = driver.find_element(By.XPATH, "//div[@aria-label = 'March 1']")
        datToSelt1.click()
        time.sleep(5)

        arivalDat = driver.find_element(By.XPATH, "//div[@id='p_AT-return']")
        arivalDat.click()
        time.sleep(3)

        datToselt2 = driver.find_element(By.XPATH, "//div[@aria-label = 'March 3']")
        datToselt2.click()
        time.sleep(3)





        
        # wait = WebDriverWait(driver, 10, poll_frequency=1,
        # ignored_exceptions=[NoSuchElementException,
        # ElementNotVisibleException,
        # ElementNotSelectableException,])

        # Frm_btn = wait.until(EC.element_to_be_clickable(By.XPATH, "//div[@aria-label = 'Flight origin input']"))
        # Frm_btn.send_keys('BBI')
        # Frm_btn.send_keys(Keys.ENTER)
        # time.sleep(5)
        driver.quit()
af = BookingFlight()
af.Bok_flight()


