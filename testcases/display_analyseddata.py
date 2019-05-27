'''
    TEST CASE ID >> TC#17
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
SEARCH_MENU= "//a[@href='/search/']"
FIRST_ROW = "//tr[@class='odd'][1]"
FIRST_FIELD = "//tr[@class='odd'][1]/td[1]"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#Click on search menu
click(SEARCH_MENU)
time.sleep(3)

#check if first row of table is displayed
check_element_present(FIRST_ROW)
time.sleep(1)

#check if first field gives disease name
text = browser.find_element_by_xpath(FIRST_FIELD).text
if (text == 'conjunctivitis'):
    element = get_web_element(FIRST_FIELD)
    assert (element.is_displayed())
else:
    print (NoSuchElementException)

#closing browser...
close_browser()