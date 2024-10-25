from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://letcode.in/calendar")

month=driver.find_element("xpath","//div[@class='datepicker-nav-month']").text
year=driver.find_element("xpath","//div[@class='datepicker-nav-year']").text

while not(month.__eq__("November") and year.__eq__("2025")):
    next_btn=driver.find_element("xpath","(//button[@class='datepicker-nav-next button is-small is-text'])[1]")
    next_btn.click()
    month = driver.find_element("xpath", "//div[@class='datepicker-nav-month']").text
    year = driver.find_element("xpath", "//div[@class='datepicker-nav-year']").text

date=driver.find_element("xpath","//button[.='25']")
date.click()
sleep(1)


month=driver.find_element("xpath","//div[@class='datepicker-nav-month']").text
year=driver.find_element("xpath","//div[@class='datepicker-nav-year']").text

while not(month.__eq__("May") and year.__eq__("2023")):
    prev_btn=driver.find_element("xpath","//button[@class='datepicker-nav-previous button is-small is-text']")
    prev_btn.click()

    month = driver.find_element("xpath", "//div[@class='datepicker-nav-month']").text
    year = driver.find_element("xpath", "//div[@class='datepicker-nav-year']").text

date=driver.find_element("xpath","//button[.='12']")
date.click()
sleep(1)


driver.find_element("xpath","//input[@class='datetimepicker-dummy-input is-datetimepicker-range']").click()



driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")

calender3=driver.find_element("id","third_date_picker")
calender3.click()

wait=WebDriverWait(driver,12)
wait.until(expected_conditions.visibility_of_element_located(("id","ui-datepicker-div")))

select_class2=driver.find_element("xpath","//select[@class='ui-datepicker-year']")
s1=Select(select_class2)
s1.select_by_visible_text("2014")
sleep(1)

select_class=driver.find_element("xpath","//select[@class='ui-datepicker-month']")
s1=Select(select_class)
s1.select_by_visible_text("Dec")
sleep(1)

date=driver.find_element("xpath","//a[.='6']")
date.click()

calender4=driver.find_element("id","fourth_date_picker")
calender4.click()

month=driver.find_element("xpath","//select[@class='ui-datepicker-month']")
s1=Select(month)
s1.select_by_visible_text("Jul")
sleep(1)

year=driver.find_element("xpath","//select[@class='ui-datepicker-year']")
s1=Select(year)
s1.select_by_visible_text("2033")
sleep(1)

date=driver.find_element("xpath","//a[.='3']")
date.click()


calender2=driver.find_element("id","second_date_picker").click()

current_month=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
current_year=driver.find_element("xpath","//span[@class='ui-datepicker-year']").text


while not(current_month.__eq__("July") and current_year.__eq__("2029")):
    next_btn=driver.find_element("xpath","//a[@data-handler='next']")
    next_btn.click()

    current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

driver.find_element("xpath","//a[.='3']").click()



driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/datePick/iconstrigger?sublist=2")
driver.maximize_window()


calender_icon=driver.find_element("xpath","(//*[@xmlns='http://www.w3.org/2000/svg'])[1]")
calender_icon.click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located(("xpath","//div[@class='react-datepicker__month-container']")))

current_month_year=driver.find_element("xpath","//div[@class='react-datepicker__current-month']").text

while not(current_month_year.__eq__("August 2026")):
    next_btn=driver.find_element("xpath","//button[@aria-label='Next Month']")
    next_btn.click()

    current_month_year = driver.find_element("xpath", "//div[@class='react-datepicker__current-month']").text

date=driver.find_element("xpath","//div[.='14']")
date.click()

sleep(1)

from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

driver=WebDriver()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/datePick/datedropdown?sublist=1")
driver.maximize_window()

driver.find_element("xpath","//input[@placeholder='Select A Date']").click()

arrow=driver.find_element("xpath","//span[@class='react-datepicker__month-read-view--down-arrow']")
arrow.click()

driver.find_element("xpath","//div[.='Apr']").click()

aroow2=driver.find_element("xpath","//span[@class='react-datepicker__year-read-view--down-arrow']")
aroow2.click()

driver.find_element("xpath","//div[.='2029']").click()

driver.find_element("xpath","//div[.='20']").click()

sleep(1)


from selenium.webdriver.chrome.webdriver import WebDriver
driver=WebDriver()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element("id","datepicker").click()

current_mon=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
current_yer=driver.find_element("xpath","//span[@class='ui-datepicker-year']").text

while not(current_mon.__eq__("December") and current_yer.__eq__("2027")):
    next_btn=driver.find_element("xpath","//span[.='Next']")
    next_btn.click()

    current_mon = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
    current_yer = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

date=driver.find_element("xpath","//a[.='27']")
date.click()

sleep(1)


driver=WebDriver()
driver.get("http://seleniumpractise.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

alert=driver.find_element("xpath","//button[.='Try it']")
alert.click()

wait=WebDriverWait(driver,12)
wait.until(expected_conditions.alert_is_present())

alert=driver.switch_to.alert
alert.dismiss()

from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

driver=WebDriver()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
driver.implicitly_wait(10)

datepicker1=driver.find_element("xpath","//input[@class='form-control hasDatepicker']")
datepicker1.click()

current_month=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
current_year=driver.find_element("xpath","//span[@class='ui-datepicker-year']").text

while not(current_month.__eq__("July") and current_year.__eq__("2025")):
    next_btn=driver.find_element("xpath","//a[@title='Next']")
    next_btn.click()

    current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

date=driver.find_element("xpath","//a[.='3']")
date.click()

datepicker1=driver.find_element("xpath","//input[@class='form-control hasDatepicker']")
datepicker1.click()

current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

while not(current_month.__eq__("July") and current_year.__eq__("2023")):
    next_btn=driver.find_element("xpath","//a[@title='Prev']")
    next_btn.click()

    current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

date=driver.find_element("xpath","//a[.='3']")
date.click()
sleep(1)

datepicker1=driver.find_element("xpath","//input[@class='form-control hasDatepicker']")
datepicker1.click()

current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

if current_year=="2024" and current_month=="September":
    date = driver.find_element("xpath", "//a[.='28']")
    date.click()
    sleep(1)


datepicker2=driver.find_element("id","datepicker2")
datepicker2.click()

month=driver.find_element("xpath","//select[@class='datepick-month-year']")
s1=Select(month)
s1.select_by_index(11)
sleep(1)

year=driver.find_element("xpath","//select[@title='Change the year']")
s1=Select(year)
s1.select_by_visible_text("2034")

date=driver.find_element("xpath","//a[@title='Select Sunday, Dec 3, 2034']")
date.click()

sleep(1)


'''it fails due to ads'''
# calender1=driver.find_element("id","first_date_picker").click()
#
# current_month=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
# current_year=driver.find_element("xpath","//span[@class='ui-datepicker-year']").text


# while not(current_month.__eq__("July") and current_year.__eq__("2039")):
#     next_btn=driver.find_element("xpath","//a[@data-handler='next']")
#     next_btn.click()

#     current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
#     current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

# driver.find_element("xpath","//a[.='3']").click()

'''mulitple year and month'''
# from selen("https://www.makemytrip.com/")
# # driver.implicitly_wait(10)
# # driver.maximize_window()
#
# # driver.find_element("xpath","//span[@data-cy='closeModal']").click()
# #
# # driver.find_element("xpath","//label[@for='departure']").click()
#
# # current_mon_year=driver.find_element("xpath","//div[@class='DayPicker-Months']").text
# # current_mon_year2=driver.find_element("xpath","//div[@class='DayPicker-Months']").text
#
# # while not(current_mon_year.__eq__("March2025") and current_mon_year2.__eq__("April2025")):
#
# #     next_btn=driver.find_element("xpath","//span[@aria-label='Next Month']")
# #     next_btn.click()
# #     current_mon_year=driver.find_element("xpath", "//div[@class='DayPicker-Months']").text
# #     current_mon_year2=driver.find_element("xpath","//div[@class='DayPicker-Months']").text
#
# # date=driver.find_element("xpath","//div[@class='dateInnerCell']/../..//div[@aria-label='Thu Aug 14 2025']")
# # date.click()ium.webdriver.chrome.webdriver import WebDriver
# driver=WebDriver()
# driver.get

'''they have removed this locaters'''
# driver.get("https://testautomationpractice.blogspot.com/")
#
# driver.switch_to.frame("frame-one796456169")
#
# driver.find_element("xpath","//span[@class='icon_calendar']").click()
# sleep(5)
#
# select_class=driver.find_element("xpath","//select[@class='ui-datepicker-year']")
# s1=Select(select_class)
# s1.select_by_visible_text("2034")
#
# current_month=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text#
# while not(current_month.__eq__("November")):
#     next_btn=driver.find_element("xpath","//a[@data-handler='prev']")
#     next_btn.click()
#
#     current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
#
# date=driver.find_element("xpath","//a[.='5']")
# date.click()
#
# sleep(2)

driver.get("https://letcode.in/windows")

home_btn=driver.find_element("xpath","//button[.='Open Home Page']")
home_btn.click()

multi_btn=driver.find_element("id","multi")
multi_btn.click()

parent_window=driver.current_window_handle

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    if driver.title=="LetCode - Testing Hub":
        pass
    if driver.title=="LetCode with Koushik":
        print("ha i am in grand child window")
        driver.close()

driver.switch_to.window(parent_window)
print("i am back again to parent window")

sleep(2)

driver.get("https://letcode.in/waits")

driver.find_element("xpath","//button[.='Simple Alert']").click()

wait=WebDriverWait(driver,12,poll_frequency=3)
wait.until(expected_conditions.alert_is_present())

alert=driver.switch_to.alert
print(alert.text)
alert.accept()



driver.get("https://letcode.in/radio")

radio_btns=driver.find_elements("xpath","//input[@type='radio']")

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="yes":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="no":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="one":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="two":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="nobug":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="bug":
        btn.click()


for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="foo":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="notfoo":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="going":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="notG":
        btn.click()

for btn in radio_btns:
    radio_btn=btn.get_attribute("id")
    if radio_btn=="maybe":

     print(btn.is_enabled())


checkbox=driver.find_element("xpath","//label[.='Find if the checkbox is selected?']/..//input[@type='checkbox']")
print(checkbox.is_selected())

checkbox2=driver.find_element("xpath","//label[.='Accept the T&C']/..//input[@type='checkbox']")
checkbox2.click()

driver.get("https://letcode.in/dropable")

source_element=driver.find_element("id","draggable")
target_element=driver.find_element("id","droppable")
actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()

driver.refresh()
source_element=driver.find_element("id","draggable")
target_element=driver.find_element("id","droppable")

actions.click_and_hold(source_element).pause(2).move_to_element(target_element).release().perform()


driver.get("https://letcode.in/forms")
driver.find_element("xpath","//a[.='All in One']").click()
driver.find_element("id","firstname").send_keys("vinuth")

driver.find_element("id","lasttname").send_keys("reddy")

email=driver.find_element("id","email")
email.clear()
email.send_keys("reddyvinuth27@gmail.com")

# select=driver.find_element("xpath","//div[@class='select']")
# select.click()


driver.find_element("id","Phno").send_keys("7676252914")

driver.find_element("id","Addl1").send_keys("Btm layout second stage")

driver.find_element("id","Addl2").send_keys("Btm layout second stage,near pvr vega city mall")

driver.find_element("id","state").send_keys("Karnataka")

driver.find_element("id","postalcode").send_keys("582102")


radio_btn=driver.find_element("id","male")
radio_btn.click()
print(radio_btn.is_selected())

radio_btn=driver.find_element("id","female")
radio_btn.click()
print(radio_btn.is_selected())

radio_btn=driver.find_element("id","trans")
radio_btn.click()
print(radio_btn.is_selected())


for btn in radio_btns:
    button=btn.get_attribute("id")
    if btn.text=="trans":
        btn.click()

for btn in radio_btns:
    button=btn.get_attribute("id")
    if btn.text=="female":
        btn.click()


date=driver.find_element("id","Date")
date.click()

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
driver=WebDriver()
chrome_options=Options()
chrome_options.add_experimental_option("prefs",{"download.default_directory":r"C:\Users\swath\OneDrive\Desktop\py_sl"})
driver.get("https://letcode.in/file")
driver.maximize_window()
driver.implicitly_wait(10)

file=driver.find_element("name","resume")
file.send_keys("C:/Users/swath/Downloads/Student Athlete Resume.pdf")
sleep(5)

buttons=driver.find_elements("xpath","//button[@class='button']")
for button in buttons:
    download=button.get_attribute("download")
    if download=="sample.xlsx":
        button.click()

download=driver.find_element("id","xls")
download.click()
sleep(2)
downoad2=driver.find_element("id","pdf")
downoad2.click()
sleep(2)
downoad3=driver.find_element("id","txt")
downoad3.click()
sleep(2)


driver.get("https://letcode.in/draggable")
source_element=driver.find_element("id","sample-box")
actions=ActionChains(driver)
actions.drag_and_drop_by_offset(source_element,50,0).perform()
sleep(3)

driver.get("https://letcode.in/frame")

driver.switch_to.frame("firstFr")
driver.find_element("name","fname").send_keys("vinuth")
driver.find_element("name","lname").send_keys("reddy")

driver.switch_to.default_content()

inner_frame=driver.find_element("xpath","//iframe[@class='has-background-white']")
driver.switch_to.frame(inner_frame)

driver.find_element("name","email").send_keys("reddyvinuth27@gmail.com")
sleep(4)