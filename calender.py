from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")


calender3=driver.find_element("id","third_date_picker")
calender3.click()

wait=WebDriverWait(driver,12)
wait.until(expected_conditions.visibility_of_element_located(("id","ui-datepicker-div")))

select_class2=driver.find_element("xpath","//select[@class='ui-datepicker-year']")
s1=Select(select_class2)
s1.select_by_visible_text("2014")
sleep(3)

select_class=driver.find_element("xpath","//select[@class='ui-datepicker-month']")
s1=Select(select_class)
s1.select_by_visible_text("Dec")
sleep(3)

date=driver.find_element("xpath","//a[.='6']")
date.click()

calender4=driver.find_element("id","fourth_date_picker")
calender4.click()

month=driver.find_element("xpath","//select[@class='ui-datepicker-month']")
s1=Select(month)
s1.select_by_visible_text("Jul")
sleep(2)

year=driver.find_element("xpath","//select[@class='ui-datepicker-year']")
s1=Select(year)
s1.select_by_visible_text("2033")
sleep(2)

date=driver.find_element("xpath","//a[.='3']")
date.click()

calender1=driver.find_element("id","first_date_picker").click()

current_month=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
current_year=driver.find_element("xpath","//span[@class='ui-datepicker-year']").text


while not(current_month.__eq__("July") and current_year.__eq__("2039")):
    next_btn=driver.find_element("xpath","//a[@data-handler='next']")
    next_btn.click()

    current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

driver.find_element("xpath","//a[.='3']").click()


calender2=driver.find_element("id","second_date_picker").click()

current_month=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
current_year=driver.find_element("xpath","//span[@class='ui-datepicker-year']").text


while not(current_month.__eq__("July") and current_year.__eq__("2029")):
    next_btn=driver.find_element("xpath","//a[@data-handler='next']")
    next_btn.click()

    current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

driver.find_element("xpath","//a[.='3']").click()

driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame("frame-one796456169")

driver.find_element("xpath","//span[@class='icon_calendar']").click()
sleep(5)

select_class=driver.find_element("xpath","//select[@class='ui-datepicker-year']")
s1=Select(select_class)
s1.select_by_visible_text("2034")


current_month=driver.find_element("xpath","//span[@class='ui-datepicker-month']").text

while not(current_month.__eq__("November")):
    next_btn=driver.find_element("xpath","//a[@data-handler='prev']")
    next_btn.click()

    current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text

date=driver.find_element("xpath","//a[.='5']")
date.click()

sleep(7)

from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

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

sleep(7)

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

sleep(4)

# from selenium.webdriver.chrome.webdriver import WebDriver
# driver=WebDriver()
# driver.get("https://www.makemytrip.com/")
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# driver.find_element("xpath","//span[@data-cy='closeModal']").click()
#
# driver.find_element("xpath","//label[@for='departure']").click()
#
# current_mon_year=driver.find_element("xpath","//div[@class='DayPicker-Months']").text
# current_mon_year2=driver.find_element("xpath","//div[@class='DayPicker-Months']").text
#
# while not(current_mon_year.__eq__("March2025") and current_mon_year2.__eq__("April2025")):
#
#     next_btn=driver.find_element("xpath","//span[@aria-label='Next Month']")
#     next_btn.click()
#     current_mon_year=driver.find_element("xpath", "//div[@class='DayPicker-Months']").text
#     current_mon_year2=driver.find_element("xpath","//div[@class='DayPicker-Months']").text
#
# date=driver.find_element("xpath","//div[@class='dateInnerCell']/../..//div[@aria-label='Thu Aug 14 2025']")
# date.click()


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

sleep(3)

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait

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
sleep(3)

datepicker1=driver.find_element("xpath","//input[@class='form-control hasDatepicker']")
datepicker1.click()

current_month = driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
current_year = driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

if current_year=="2024" and current_month=="September":
    date = driver.find_element("xpath", "//a[.='28']")
    date.click()
    sleep(3)


datepicker2=driver.find_element("id","datepicker2")
datepicker2.click()

month=driver.find_element("xpath","//select[@class='datepick-month-year']")
s1=Select(month)
s1.select_by_index(11)
sleep(2)

year=driver.find_element("xpath","//select[@title='Change the year']")
s1=Select(year)
s1.select_by_visible_text("2034")

date=driver.find_element("xpath","//a[@title='Select Sunday, Dec 3, 2034']")
date.click()

sleep(3)