from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
path  = "C:\\dev\\\driver\\chrome\\chromedriver.exe"
base_url = "https://learn.letskodeit.com/p/practice"
driver = webdriver.Chrome(executable_path= path)
driver.maximize_window()
driver.get(base_url)
driver.implicitly_wait(5)
radio_btn1 = driver.find_element(By.XPATH, "//input[@id = 'bmwradio']" )
radio_btn1.click()
time.sleep(5)
radio_btn2 = driver.find_element(By.XPATH, "//input[@id ='hondaradio']")
radio_btn2.click()
time.sleep(5)
radio_btn3 = driver.find_element(By.XPATH, "//input[@id ='benzradio']")
radio_btn3.click()
chk_box1  = driver.find_element(By.ID, "bmwcheck")
chk_box1.click()
time.sleep(5)
chk_box2  = driver.find_element(By.ID, "benzcheck")
chk_box2.click()
time.sleep(5)
dpdw = driver.find_element(By.ID, "carselect")
sel = Select(dpdw)
sel.select_by_value("bmw")
time.sleep(5)   
sel.select_by_index(2)
time.sleep(5)
sel.select_by_visible_text("Benz")
time.sleep(5)
driver.quit()








