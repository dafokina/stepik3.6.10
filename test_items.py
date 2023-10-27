from selenium.webdriver.common.by import By
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), '---Нет кнопки добавить в корзину---'

