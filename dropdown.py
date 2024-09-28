from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

driver=WebDriver()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame("frame-one796456169")
selectclass_element=driver.find_element("id","RESULT_RadioButton-3")
s1=Select(selectclass_element)
all_options=s1.options

for option in all_options:
    if option.text=="Automation Engineer":
        option.click()

sleep(1)