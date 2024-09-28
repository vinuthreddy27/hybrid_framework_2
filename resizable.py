from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

driver=WebDriver()
driver.get("https://jqueryui.com/resizable/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to.frame(0)

resize_element=driver.find_element("xpath","//div[contains(@class,'ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se')]")
print(resize_element.size)
actions=ActionChains(driver)
# actions.click_and_hold(resize_element).move_by_offset(200,100).release().perform()
actions.drag_and_drop_by_offset(resize_element,200,100).perform()
sleep(5)

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

driver=WebDriver()
driver.get("https://demo.automationtesting.in/Resizable.html")
driver.maximize_window()
driver.implicitly_wait(10)
first=driver.find_element("id","resizable")
print(first.size)
actions=ActionChains(driver)
resize_element2=driver.find_element("xpath","//div[contains(@class,'ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se')]")

# actions.drag_and_drop_by_offset(resize_element2,150,180).perform()

actions.click_and_hold(resize_element2).move_by_offset(100,100).release().perform()
print(resize_element2.size)



from selenium.webdriver.chrome.webdriver import WebDriver
driver=WebDriver()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

resize_element3=driver.find_element("id","resizable")
print(resize_element3.size)
element=driver.find_element("xpath","//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
actions=ActionChains(driver)
actions.move_to_element_with_offset(resize_element3,70,70).perform()
print(element.size)
sleep(5)