# from time import sleep
#
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.select import Select

# driver=WebDriver()
# driver.maximize_window()
#
# driver.switch_to.frame("frame-one796456169")
# selectclass_element=driver.find_element("id","RESULT_RadioButton-3")
# s1=Select(selectclass_element)
# all_options=s1.options
#
# for option in all_options:
#     if option.text=="Automation Engineer":
#         option.click()
#
# sleep(1)get("https://testautomationpractice.blogspot.com/")


from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
driver=WebDriver()
driver.get("file:///C:/Users/swath/Downloads/demo%20(1).html")
driver.maximize_window()
driver.implicitly_wait(10)

select=driver.find_element("id","multiple_cars")
s3=Select(select)

all_options=s3.options

for option in all_options:
    if option.text=="BMW":
        option.click()

sleep(2)

boxs=driver.find_elements("xpath","//input[@class='alert']")
for box in boxs:
    box.click()

sleep(1)

checkboxs=driver.find_elements("xpath","//input[@type='checkbox']")

for checkbox in checkboxs:
    option=checkbox.get_attribute("name")
    if option=="download":
        checkbox.click()

sleep(1)

file_upload=driver.find_element("id","resume")
file_upload.send_keys("C:/Users/swath/Downloads/Student Athlete Resume.pdf")

sleep(1)


# elements=driver.find_elements("xpath","//a")
#
# for element in elements:
#     element.click()
#
# parent_window=driver.current_window_handle
#
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     if driver.title=="Demo Web Shop":
#         pass
#     driver.find_element("xpath","//a[.='Log in']").click()
#
#
# sleep(3)
# driver.switch_to.window(parent_window)
#
# sleep(2)
