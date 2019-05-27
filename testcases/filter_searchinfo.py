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
SECOND_FIELD= "//tr[@class='odd'][1]/td[2]"
SEARCH_BOX = "//input[@type='search']"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#Click on search menu
click(SEARCH_MENU)
time.sleep(3)

#filter by disease name
sendText('flu', SEARCH_BOX)
time.sleep(1)
check_element_present(FIRST_ROW)

text = browser.find_element_by_xpath(FIRST_FIELD).text
if (text == 'influenza'):
    elem = get_web_element(FIRST_FIELD)
    assert (elem.is_displayed())
else:
    print (NoSuchElementException)
time.sleep(1)

#filter by date
sendText('2019-01', SEARCH_BOX)
time.sleep(1)
check_element_present(FIRST_ROW)

text2 = browser.find_element_by_xpath(SECOND_FIELD).text
if  (text2.__contains__('2019-01')):
    element = get_web_element(SECOND_FIELD)
    assert (element.is_displayed())
else:
    print (NoSuchElementException)
time.sleep(1)

#closing browser...
close_browser()