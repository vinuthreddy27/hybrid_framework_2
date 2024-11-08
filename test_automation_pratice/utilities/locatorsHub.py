from test_automation_pratice.Library.lib import Base

class automation_pratice_page_locators(Base):

    name_textfield = ("id", "name")
    email_textfield = ("id", "email")
    phone_textfield = ("id", "phone")
    address_textarea = ("id", "textarea")
    male_radiobtn = ("id", "male")
    female_radiobtn = ("id", "female")
    country_dropdown = ("id", "country")
    option_locator_1=("xpath","//option[.='India']")

    check_box=("id","sunday")
    check_box2=("id","monday")
    check_box3=("id","tuesday")
    check_box4=("id","wednesday")
    check_box5=("id","thursday")
    check_box6=("id","friday")
    check_box7=("id","saturday")

    file_upload=("id","singleFileInput")
    file_upload2=("id","multipleFilesInput")


    name=("name","input1")
    name2=("name", "input2")
    name3= ("name", "input3")

    btn=("id","btn1")
    btn2= ("id", "btn1")
    btn3= ("id", "btn1")

    hover=("xpath","//button[.='Point Me']")

    select_locator = ("id", "colors")


    date_textfield = ("id", "datepicker")

    pagination_table = ("xpath", "//td[.='$5.99']/..//input")

    search_textfield = ("id", "Wikipedia1_wikipedia-search-input")
    search_btn = ("xpath", "//input[@type='submit']")

    alert = ("xpath", "//button[@onclick='myFunctionAlert()']")
    conform = ("xpath", "//button[@onclick='myFunctionConfirm()']")
    prompt = ("xpath", "//button[@onclick='myFunctionPrompt()']")

    click_btn = ("xpath", "//button[@ondblclick='myFunction1()']")

    frame1 = ("frame-one796456169")
    frame_name_tf = ("id", "RESULT_TextField-0")

    female_rbtn = ("xpath","//label[@for='RESULT_RadioButton-1_1']")

    table_r5=("xpath","//td[.='$7.99']/..//input")

    field1=("id","field1")
    copy_text_btn=("xpath","//button[.='Copy Text']")

    source_element=("id","draggable")
    target_element=("id","droppable")

    anchor_link=("xpath","//a[.='Posts (Atom)']")
    calender_icon=("xpath","//span[@class='icon_calendar']")

    c_locator=("id","datepicker")
    current_month=("xpath","//span[.='September' and //span[.='2024']]")
    current_year=("xpath"," //span[.='2024']")
    next_btn_locator=("xpath","//span[.='2024']/../..//a[@data-handler='next']")
    target=("xpath","//td[@data-year='2026']/..//a[.='5']")

    scroll=("xpath","//div[@class='feed-links']")

    slider=("xpath","//span[@tabindex='0']")

    select_locator_f=("id","RESULT_RadioButton-3")
    option_locator1=("xpath","//option[.='Automation Engineer']")
    option_locator2=("xpath","//option[.='QA Engineer']")
    option_locator3=("xpath","//option[.='Developer']")
    option_locator4=("xpath","//option[.='Manager']")

    origin=("xpath","//div[@class='feed-links']")

    size=("xpath","//div[contains(@class,'ui-resizable-handle ui-resizable-se')]")




