from selenium.webdriver import ActionChains

from test_automation_pratice.POM.atp_page import Selenium



def test_selenium(driver):
    atp_po=Selenium(driver,ActionChains)
    atp_po.selenium("vinuth",
                    "reddyvinuth27@gmail.com",
                    "7676252914",
                    "BTM layout Near PVR Vega City Mall",
                    "Nike shoes",
                    "jyothi",
                    "jyothi.....",
                    "vinuth ram reddy")





