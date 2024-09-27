from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

driver=WebDriver()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

wait=WebDriverWait(driver,6)
wait.until(visibility_of_element_located(("xpath","//img[@alt='MacBookAir']"))).click()

