from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


path  = "C:/dev/driver/firefox/geckodriver"
base_url = "https://learn.letskodeit.com/p/practice"
driver = webdriver.Firefox(executable_path= path)
driver.maximize_window
driver.get(base_url)
driver.implicitly_wait(5)

#find the parent handle
parenthandles = driver.current_window_handle
print("Parent Handles is :" + parenthandles)

#find the element of new tab
swtchtowindow = driver.find_element(By.ID, "openwindow")
swtchtowindow.click()

#find child handles

chidhandle = driver.window_handles

#switch to window and search course
for handle in chidhandle:
    if handle not in parenthandles:
        driver.switch_to_window(handle)
        searchbox = driver.find_element(By.ID, "search-courses")
        searchbox.send_keys("Selenium WebDriver With Python 3.x")
        time.sleep(5)
        driver.close()

driver.switch_to_window(parenthandles)
driver.find_element(By.ID, "bmwradio").click()
time.sleep(5)
driver.quit()







