'''
    TEST CASE ID >> TC#22
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
INPUT_DISEASE_PORTAL = "//button[@class='w3-btn w3-block w3-orange']"
FLU_BTN = "//input[@value='influenza']"
LOCATION = "//input[@name='location']"
DATE = "//input[@name='date']"
SUBMIT_BTN ="//button[@type='submit']"
NOTIF1 = "//div[@id='notifs']/div[1]"
NOTIF_CONTENT = "//div[@id='notifs']/div[1]//p"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)
scroll_down()

main_window = browser.current_window_handle

#click on input disease portal link
click(INPUT_DISEASE_PORTAL)
time.sleep(1)

browser.switch_to.window(browser.window_handles[1])
time.sleep(1)
scroll_down()
click(FLU_BTN)
time.sleep(1)
sendText('Port Louis', LOCATION)
sendText('342019', DATE)
time.sleep(1)
click(SUBMIT_BTN)
time.sleep(1)

browser.switch_to.window(main_window)

time.sleep(1)
check_element_present(NOTIF1)
text = browser.find_element_by_xpath(NOTIF_CONTENT).text
if (text.__contains__('Port Louis')):
    element = get_web_element(NOTIF_CONTENT)
    assert (element.is_displayed())
else:
    print (NoSuchElementException)

#closing
browser.quit()