from time import sleep

from test_automation_pratice.Library.lib import Base
from test_automation_pratice.utilities.locatorsHub import automation_pratice_page_locators

class Selenium(Base):

    def selenium(self,name,email,telephone,address,text,fname,message,sandesha):
        self.Scroll_by_amount(0,500)
        self.scroll(automation_pratice_page_locators.scroll)
        # self.Scroll_from_origin(automation_pratice_page_locators.origin,100,100)
        self.send_text_to_textfield(automation_pratice_page_locators.name_textfield,name)
        self.send_text_to_textfield(automation_pratice_page_locators.email_textfield,email)
        self.send_text_to_textfield(automation_pratice_page_locators.phone_textfield,telephone)
        self.send_text_to_textfield(automation_pratice_page_locators.address_textarea,address)
        self.click_on_element(automation_pratice_page_locators.male_radiobtn)
        self.click_on_element(automation_pratice_page_locators.day_radiobtn)
        self.click_on_element(automation_pratice_page_locators.pagination_table)
        self.send_text_to_textfield(automation_pratice_page_locators.search_textfield,text)
        self.click_on_element(automation_pratice_page_locators.search_btn)
        self.click_on_element(automation_pratice_page_locators.alert)
        self.accept_alert()
        self.click_on_element(automation_pratice_page_locators.conform)
        self.dismiss_alert()
        self.click_on_element(automation_pratice_page_locators.prompt)
        self.accept_alert()
        # self.switch_to_frame(automation_pratice_page_locators.frame1)
        # self.send_text_to_textfield(automation_pratice_page_locators.frame_name_tf,fname)
        self.switch_to_default_content()
        self.click_on_element(automation_pratice_page_locators.table_r5)
        self.clear_a_text(automation_pratice_page_locators.name_textfield)
        self.Send_keys_to_element(automation_pratice_page_locators.name_textfield,sandesha)
        # self.switch_to_frame(automation_pratice_page_locators.frame1)
        # self.click_on_element(automation_pratice_page_locators.female_rbtn)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator1)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator2)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator3)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator4)
        self.switch_to_default_content()
        self.clear_a_text(automation_pratice_page_locators.field1)
        self.send_text_to_textfield(automation_pratice_page_locators.field1,message)
        self.actionchanins_double_click(automation_pratice_page_locators.copy_text_btn)
        self.actions_drag_and_drop(automation_pratice_page_locators.source_element,automation_pratice_page_locators.target_element)
        self.hovering(automation_pratice_page_locators.anchor_link)
        self.select_a_option(automation_pratice_page_locators.select_locator,automation_pratice_page_locators.option_locator)
        self.select_a_option(automation_pratice_page_locators.select_locator,automation_pratice_page_locators.option_locator_c1)
        self.select_a_option(automation_pratice_page_locators.select_locator,automation_pratice_page_locators.option_locator_c2)
        self.select_a_option(automation_pratice_page_locators.select_locator,automation_pratice_page_locators.option_locator_c3)
        self.select_a_option(automation_pratice_page_locators.country_dropdown,automation_pratice_page_locators.option_locator_1)
        self.drag_and_drop_byoffset(automation_pratice_page_locators.slider,220,0)
        self.select_a_date("July","2025")
        self.select_previous_date("July","2021")
        # self.select_date_from_frame()

        self.drag_and_drop_byoffset(automation_pratice_page_locators.size,85,85)








