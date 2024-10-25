# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
#
# driver=WebDriver()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://tutorialsninja.com/demo/")
#
# wait=WebDriverWait(driver,6,poll_frequency=3)
# condition=wait.until(visibility_of_element_located(("xpath","//img[@alt='iPhone 6']")))
# print(condition.is_displayed())



from time import sleep
from selenium.webdriver.firefox.webdriver import WebDriver
driver = WebDriver()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://demoapps.qspiders.com/ui/radio?sublist=0")

radio_btn=driver.find_element("id","attended1")
button=radio_btn.get_attribute('value')
if button == 'wallet':
   radio_btn.click()

if radio_btn.is_selected():
    print("test case passed")
else:
    print("test case faild")




driver.get("https://demoapps.qspiders.com/ui?scenario=1")

inputs=driver.find_elements("xpath","//input")
for input in inputs:
    textbox=input.get_attribute('id')
    if textbox=='name':
        input.send_keys("vinuth")

    textbox2=input.get_attribute('id')
    if textbox2=='email':
        input.clear()
        input.send_keys("reddyvinuth@gmail.com")

    textbox3 = input.get_attribute('id')
    if textbox3 == 'password':
        input.clear()
        input.send_keys("password")


driver.get("https://demoapps.qspiders.com/ui/table?scenario=1")
table=driver.find_element("xpath","//table[@class='w-full text-sm text-left text-gray-500 ']//thead/tr/th']")
print(table.text)
driver.quit()





