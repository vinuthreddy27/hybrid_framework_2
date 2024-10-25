from time import sleep

from test_automation_pratice.Library.lib import Base
from test_automation_pratice.utilities.locatorsHub import automation_pratice_page_locators

class Selenium(Base):

    def selenium(self,name,email,telephone,address,text,fname,message,sandesha,file,file2,file3,name2,name3,name4,option,option2,option3,option4,option5,option6,option7,option8):

        self.Scroll_by_amount(0,500)
        sleep(1)
        self.scroll(automation_pratice_page_locators.scroll)
        sleep(1)
        self.send_text_to_textfield(automation_pratice_page_locators.name_textfield,name)
        sleep(1)
        self.send_text_to_textfield(automation_pratice_page_locators.email_textfield,email)
        sleep(1)
        self.send_text_to_textfield(automation_pratice_page_locators.phone_textfield,telephone)
        sleep(1)
        self.send_text_to_textfield(automation_pratice_page_locators.address_textarea,address)
        sleep(1)

        self.click_on_element(automation_pratice_page_locators.male_radiobtn)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.female_radiobtn)
        sleep(1)

        self.click_on_element(automation_pratice_page_locators.check_box)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.check_box2)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.check_box3)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.check_box4)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.check_box5)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.check_box6)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.check_box7)


        self.send_text_to_textfield(automation_pratice_page_locators.file_upload,file)
        sleep(1)
        # self.send_text_to_textfield(automation_pratice_page_locators.file_upload2,file2)
        self.send_text_to_textfield(automation_pratice_page_locators.file_upload2, file3)
        sleep(1)

        self.send_text_to_textfield(automation_pratice_page_locators.name,name2)
        sleep(1)
        self.send_text_to_textfield(automation_pratice_page_locators.name2,name3)
        sleep(1)
        self.send_text_to_textfield(automation_pratice_page_locators.name3,name4)
        sleep(1)

        self.click_on_element(automation_pratice_page_locators.btn)
        self.click_on_element(automation_pratice_page_locators.btn2)
        self.click_on_element(automation_pratice_page_locators.btn3)

        self.hovering(automation_pratice_page_locators.hover)
        sleep(1)

        self.click_on_element(automation_pratice_page_locators.pagination_table)
        sleep(1)

        self.send_text_to_textfield(automation_pratice_page_locators.search_textfield,text)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.search_btn)
        sleep(1)
        self.click_on_element(automation_pratice_page_locators.alert)
        sleep(1)
        self.accept_alert()

        self.click_on_element(automation_pratice_page_locators.conform)
        sleep(1)
        self.dismiss_alert()
        self.click_on_element(automation_pratice_page_locators.prompt)
        sleep(1)
        self.accept_alert()

        self.switch_to_default_content()
        self.click_on_element(automation_pratice_page_locators.table_r5)
        sleep(1)
        self.clear_a_text(automation_pratice_page_locators.name_textfield)
        sleep(1)
        self.Send_keys_to_element(automation_pratice_page_locators.name_textfield,sandesha)


        self.switch_to_default_content()
        self.clear_a_text(automation_pratice_page_locators.field1)
        sleep(1)
        self.send_text_to_textfield(automation_pratice_page_locators.field1,message)
        sleep(1)
        self.actionchanins_double_click(automation_pratice_page_locators.copy_text_btn)
        sleep(1)
        self.actions_drag_and_drop(automation_pratice_page_locators.source_element,automation_pratice_page_locators.target_element)
        sleep(1)
        self.hovering(automation_pratice_page_locators.anchor_link)
        sleep(1)

        self.select_a_option(automation_pratice_page_locators.select_locator,option)
        sleep(1)
        self.select_a_option(automation_pratice_page_locators.select_locator,option2)
        sleep(1)
        self.select_a_option(automation_pratice_page_locators.select_locator,option3)
        sleep(1)
        self.select_a_option(automation_pratice_page_locators.select_locator,option4)
        sleep(1)
        self.select_a_option(automation_pratice_page_locators.select_locator, option6)
        sleep(1)
        self.select_a_option(automation_pratice_page_locators.select_locator, option7)
        sleep(1)
        self.select_a_option(automation_pratice_page_locators.select_locator, option8)
        sleep(1)
        self.select_a_option(automation_pratice_page_locators.country_dropdown,option5)
        sleep(1)

        self.drag_and_drop_byoffset(automation_pratice_page_locators.slider,220,0)
        sleep(1)
        self.select_a_date("July","2027")
        sleep(1)
        self.selection_of_date()
        sleep(2)

        # self.select_previous_date("July","2021")
        # self.select_date_from_frame()
        # self.drag_and_drop_byoffset(automation_pratice_page_locators.size,0,185)
        # self.switch_to_frame(automation_pratice_page_locators.frame1)
        # self.send_text_to_textfield(automation_pratice_page_locators.frame_name_tf,fname)
        # self.switch_to_frame(automation_pratice_page_locators.frame1)
        # self.click_on_element(automation_pratice_page_locators.female_rbtn)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator1)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator2)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator3)
        # self.select_a_option(automation_pratice_page_locators.select_locator_f,automation_pratice_page_locators.option_locator4)









