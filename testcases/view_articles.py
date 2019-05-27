'''
    TEST CASE ID >> TC#15
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
ARTICLE1 = "//div[@class='media tm-notification-item'][1]"
LINK = "//div[@class='media tm-notification-item'][1]//a[@class='tm-notification-link']"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#Check if first article is displayed
check_element_present(ARTICLE1)
time.sleep(1)

#click on the link
click(LINK)
time.sleep(1)

#closing browser...
close_browser()