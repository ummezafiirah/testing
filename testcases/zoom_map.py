'''
    TEST CASE ID >> TC#12
'''

from framework.operations import *
import time

#variables declaration
URL = "https://mauri-health.herokuapp.com/"
ZOOM_IN = "//a[@class='leaflet-control-zoom-in']"
ZOOM_OUT = "//a[@class='leaflet-control-zoom-out']"
LIVE_MAP = "//a[@href='/map_realtime']"
MAP_CONTAINER = "//div[contains(@class, 'leaflet-container')]"

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

#CLICK ON ZOOM IN BTN
click(ZOOM_IN)
time.sleep(1)

#CLICK ON ZOOM OUT BTN
click(ZOOM_OUT)
time.sleep(1)

#closing browser...
close_browser()