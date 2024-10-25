from selenium.webdriver.chrome.webdriver import WebDriver

driver=WebDriver()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(15)

element=driver.find_element("link text","Nested Frames")
element.click()

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
element=driver.find_element("xpath","//body")
print(element.text)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
element1=driver.find_element("xpath","//body")
print(element1.text)


driver.quit()