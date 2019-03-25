
'''
    TEST CASE ID >> TC#11
'''

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
LIVE_MAP = "//a[@href='/map_realtime']"
MAP_CONTAINER = "//div[contains(@class, 'leaflet-container')]"
MAP_MARKER = "(//img[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive'])[3]"
POPUP = "//div[@class='leaflet-popup-content']"

from framework.operations import *
import time

#go to link
go_to_page(URL)

#allow page to load
time.sleep(5)

#click on LIVE MAP menu
click(LIVE_MAP)
time.sleep(3)

# CHECK IF MAP HAS BEEN DISPLAYED
check_element_present(MAP_CONTAINER)
scroll_down()
time.sleep(1)

#CHECK IF FIRST MARKER HAS BEEN DISPLAYED
check_element_present(MAP_MARKER)
time.sleep(1)

#CHECK IF HOVER POPUP DISPLAYS
move_to_element(MAP_MARKER)
time.sleep(1)
try:
    tooltip = MAP_MARKER.get_attribute('title')
    print (tooltip)
except:
    print("No tooltip displayed")
time.sleep(1)

#CHECK IF POPUP APPEARS WHEN MARKER IS CLICKED
click(MAP_MARKER)
time.sleep(1)
check_element_present(POPUP)

#closing browser...
close_browser()
