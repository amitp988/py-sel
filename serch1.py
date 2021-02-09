from selenium import webdriver
class Serachname():
    def Sachin(self):
        x = input('Enter The Name:')
        if x == "Sachin Tendulkar":
            driver = webdriver.Firefox(executable_path='C:/dev/driver/firefox/geckodriver')
            driver.get('https://en.wikipedia.org/wiki/Sachin_Tendulkar')
        else:
            print(x)
qw = Serachname()
qw.Sachin()
