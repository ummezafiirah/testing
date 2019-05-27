'''
    TEST CASE ID >> TC#17
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
SEARCH_MENU= "//a[@href='/search/']"
DOWNLOAD = "//button[@class='dt-button buttons-pdf buttons-html5']"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#Click on search menu
click(SEARCH_MENU)
time.sleep(3)

#Click on pdf
click(DOWNLOAD)
