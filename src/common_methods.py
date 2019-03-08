from selene import browser
from selenium.webdriver import ActionChains


def move_to_element(element):
    # if the page is scrolled down we move to element without any action
    action = ActionChains(browser.driver())
    action.move_to_element(element)
    action.perform()

