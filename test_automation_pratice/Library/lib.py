from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.webdriver import WebDriver

class Base:

    def __init__(self,driver,ActionChains):
        self.driver=driver
        self.actions=ActionChains((self.driver))

    def search_for_element(self,locator):
        element=self.driver.find_element(*locator)
        return element

    def search_for_elements(self,locator):
        element=self.driver.find_elements(*locator)
        element.click()

    def click_on_element(self,locator):
        element=self.search_for_element(locator)
        element.click()

    def clear_a_text(self,locator):
        element=self.search_for_element(locator)
        element.clear()

    def send_text_to_textfield(self,locator,text):
        element=self.search_for_element(locator)
        element.send_keys(text)

    '''Select class'''
    def select_a_option(self,locator1,locator2):
        select_element=self.search_for_element(locator1)
        s1=Select(select_element)
        element=self.search_for_element(locator2)
        s1.select_by_visible_text(element.text)

    '''alerts'''
    def accept_alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert=self.driver.switch_to.alert
        alert.dismiss()

    '''navigational commands'''

    def nagigational_command_back(self):
        self.driver.back()

    def nagigational_command_forward(self):
        self.driver.forward()

    def nagigational_command_refresh(self):
        self.driver.refresh()

    '''frames'''
    def switch_to_frame(self,locator):
        self.driver.switch_to.frame(locator)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent()

    '''window handle'''
    def switch_window(self):
        parent_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles

        for handle in all_handles:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                break
        self.driver.switch_to.window(parent_window)


        '''ActionChains'''
    def actionchanins_click(self, locator):
        element = self.search_for_element(locator)
        self.actions.click(element).perform()

    def actionchanins_double_click(self, locator):
        element = self.search_for_element(locator)
        self.actions.double_click(element).perform()

    def actionchanins_right_click(self, locator):
        self.search_for_element(locator)
        self.actions.context_click().perform()

    def hovering(self, locator):
        element = self.search_for_element(locator)
        self.actions.move_to_element(element).perform()

    def actions_drag_and_drop(self, locator, locator2):
        source_element = self.search_for_element(locator)
        target_element = self.search_for_element(locator2)
        self.actions.drag_and_drop(source_element, target_element).perform()

    def Send_keys_to_element(self,locator,text):
        element=self.search_for_element(locator)
        self.actions.send_keys_to_element(element,text).perform()

    def drag_and_drop_byoffset(self,locator,x,y):
        element=self.search_for_element(locator)
        self.actions.drag_and_drop_by_offset(element,x,y).perform()

    def scroll(self,locator):
        element=self.search_for_element(locator)
        self.actions.scroll_to_element(element).perform()

    def Scroll_by_amount(self,x,y):
        self.actions.scroll_by_amount(x,y).perform()

    def Scroll_from_origin(self, locator, x, y):
        origin = self.search_for_element(locator)
        self.actions.scroll_from_origin(origin, x, y).perform()


    def select_a_date(self,month,year):
        self.driver.find_element("id","datepicker").click()
        current_month=self.driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
        current_year=self.driver.find_element("xpath","//span[@class='ui-datepicker-year']").text

        while not (current_month.__eq__(month) and current_year.__eq__(year)):
            next_btn = self.driver.find_element("xpath", "//a[@data-handler='next']")
            next_btn.click()
            current_month = self.driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
            current_year = self.driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

        self.driver.find_element("xpath","//a[.='3']").click()

    def select_previous_date(self, month, year):
        self.driver.find_element("id", "datepicker").click()
        current_month = self.driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
        current_year = self.driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

        while not (current_month.__eq__(month) and current_year.__eq__(year)):
            next_btn = self.driver.find_element("xpath", "//a[@data-handler='prev']")
            next_btn.click()
            current_month = self.driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
            current_year = self.driver.find_element("xpath", "//span[@class='ui-datepicker-year']").text

        self.driver.find_element("xpath", "//a[.='3']").click()


    def select_date_from_frame(self):
        self.driver.switch_to.frame("frame-one796456169")
        self.driver.find_element("xpath", "//span[@class='icon_calendar']").click()
        select_class = self.driver.find_element("xpath", "//select[@class='ui-datepicker-year']")
        s1 = Select(select_class)
        s1.select_by_visible_text("2034")

        current_month = self.driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
        while not (current_month.__eq__("November")):
            next_btn = self.driver.find_element("xpath", "//a[@data-handler='prev']")
            next_btn.click()
            current_month = self.driver.find_element("xpath", "//span[@class='ui-datepicker-month']").text
        date = self.driver.find_element("xpath", "//a[.='5']")
        date.click()








