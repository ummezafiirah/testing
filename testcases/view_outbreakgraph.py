'''
    TEST CASE ID >> TC#13
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
DISEASE_MENU = "//a[@id='navbarDropdown']"
DETECT = "//a[@href='/detect/']"
FLU_GRAPH = "//img[@src='/static/img/flu.png']"
GASTRO_GRAPH = "//img[@src='/static/img/gastro.png']"
CONJ_GRAPH = "//img[@src='/static/img/conj.png']"
RESPIRATORY_GRAPH = "//img[@src='/static/img/respiratoryinfection.png']"

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#click on disease menu
click(DISEASE_MENU)
click(DETECT)
time.sleep(3)

#verify if graphs are displayed
check_element_present(FLU_GRAPH)
time.sleep(1)
check_element_present(GASTRO_GRAPH)
time.sleep(1)
check_element_present(CONJ_GRAPH)
time.sleep(1)
check_element_present(RESPIRATORY_GRAPH)
time.sleep(1)


#closing browser...
close_browser()
