'''
    TEST CASE ID >> TC#14
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
DISEASE_MENU = "//a[@id='navbarDropdown']"
PREDICT = "//a[@href='/predict']"
INFLUENZA_BTN = "//button[@data-show='.darwin']"
FLU_GRAPH = "//iframe[@src='/static/influenza.html']"
FLU_TRENDS = "//img[@src='/static/img/influenza.png']"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#click on disease menu
click(DISEASE_MENU)
click(PREDICT)
time.sleep(3)

#Click on influenza btn
click(INFLUENZA_BTN)
time.sleep(1)
check_element_present(FLU_GRAPH)
time.sleep(1)

#check if disease trends graphs are displayed
check_element_present(FLU_TRENDS)

#closing browser...
close_browser()