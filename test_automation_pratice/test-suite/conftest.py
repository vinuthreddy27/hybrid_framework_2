import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(autouse=True)
def driver():
  print("browser launched")
  driver=WebDriver()
  driver.maximize_window()
  driver.get("https://testautomationpractice.blogspot.com/")
  yield driver
  driver.quit()
  print("browser closed")


