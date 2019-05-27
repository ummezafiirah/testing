'''
    TEST CASE ID >> TC#16
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
GASTRO_BTN = "//button[@class='tablinks'][1]"
IMG = "//img[@src='https://nurseslabs.com/wp-content/uploads/2017/02/FT-Gastroenteritis-Nursing-Care-Plans.png']"
CONTENT = "//div[@id='gastro']//div[@class='tab__content'][1]//p"
CAUSES_TAB = "//div[@id='gastro']//label[contains(.,'Causes')]"
CAUSES_HEADING = "//div[@id='gastro']//div[@class='tab__content'][2]//h3"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)
scroll_down()

#click on gastro btn
click(GASTRO_BTN)
check_element_present(IMG)
text = browser.find_element_by_xpath(CONTENT).text
if (text.__contains__('Gastroenteritis')):
    element = get_web_element(CONTENT)
    assert (element.is_displayed())
else:
    print (NoSuchElementException)

#click on CAUSES tab
click(CAUSES_TAB)
text2 = browser.find_element_by_xpath(CAUSES_HEADING).text
if (text2.__contains__('Causes')):
    elem =get_web_element(CAUSES_HEADING)
    assert (elem.is_displayed())
else:
    print (NoSuchElementException)

time.sleep(1)
#closing browser...
close_browser()