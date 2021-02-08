from selenium import webdriver
class Basicsl():
    def Onsel(self):
        driver = webdriver.Firefox(executable_path = 'C:/dev/driver/firefox/geckodriver')
        driver.get("https://learn.letskodeit.com/p/practice")
aa = Basicsl()
aa.Onsel()

