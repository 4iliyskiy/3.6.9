import pytest
from selenium import webdriver
import time
import math
from selenium.common.exceptions import NoSuchElementException

def test_guest_can_go_to_login_page(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

#def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button")
    except NoSuchElementException:
        return False
    assert True





