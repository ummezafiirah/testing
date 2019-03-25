import atexit
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException, NoSuchElementException)
import time

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

executable_path=os.path.join('chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# instantiate a chrome options object so you can set the size and headless preference
#options.add_argument("--headless")
options.add_argument("--start-maximized")
global browser

# TO USE FIREFOX WEBDRIVER UNCOMMENT BELOW LINE
#browser = webdriver.Firefox(executable_path='C:/WebScraper/firefox/geckodriver.exe')

browser = webdriver.Chrome(
    executable_path=executable_path,
    chrome_options=options,
    )
WAIT_TIME = 5
browser.wait = WebDriverWait(browser, WAIT_TIME)


def close_browser():
    """
    Close the browser.
    """
    try:
        browser.quit()
    except WebDriverException:
        # Might be already closed.
        pass


# Make sure browser is always closed, even on errors.
#atexit.register(close_browser, browser)

def enter(xpath):
    browser.find_element_by_xpath(xpath).send_keys(Keys.ENTER)

def sendText(text, xpath):
    try:
        element = browser.find_element_by_xpath(xpath)
        if is_visible(element):
            element.send_keys(text)
    except NoSuchElementException:
        print(NoSuchElementException)

def go_to_page(url):
    browser.get(url)

# return True if element is visible within 5 seconds, otherwise False
def is_visible(element, timeout=5):
    try:
        ui.WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(element))
        return True
    except TimeoutException:
        return False

def click(xpath):
    try:
        element = browser.find_element_by_xpath(xpath)
        if (element):
            action = webdriver.common.action_chains.ActionChains(browser)
            action.move_to_element(element).perform()
            element.click()
    except NoSuchElementException:
        pass

def scroll_to_element(element):
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

def scroll_down():
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom.
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_web_element(xpath):
    element = None
    try:
        element = browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        pass
    return element

def check_element_present(xpath):
    element = get_web_element(xpath)
    if (element):
        assert(element.is_displayed())
    else:
        print(NoSuchElementException)

def move_to_element(xpath):
    """
    Get element in the current viewport and have to mouse over it.
    """
    element = get_web_element(xpath)
    actions = ActionChains(browser)
    actions.move_to_element(element)
    actions.perform()