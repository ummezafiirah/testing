'''
    TEST CASE ID >> TC#17
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
SEARCH_MENU= "//a[@href='/search/']"
COPY_BTN = "//button[@class='dt-button buttons-copy buttons-html5']"
COPY_NOTIF = "//div[@id='datatables_buttons_info']/h2"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#Click on search menu
click(SEARCH_MENU)
time.sleep(3)

#click on copy
click(COPY_BTN)
check_element_present(COPY_NOTIF)

#closing browser...
close_browser()