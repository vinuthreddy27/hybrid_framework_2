from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

driver=WebDriver()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/")

wait=WebDriverWait(driver,6,poll_frequency=3)
condition=wait.until(visibility_of_element_located(("xpath","//img[@alt='iPhone 6']")))
print(condition.is_displayed())




