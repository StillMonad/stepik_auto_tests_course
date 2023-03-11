import pytest
from .pages.product_page import ProductPage
from ..src.helpers import add_delay


variants = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + str(i)
            for i in range(0, 10)]
variants = [variants[0]]
'''
@add_delay(0, 0)
@pytest.mark.parametrize('link', variants)
def test_adding_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_product_name_in_success_message()
    product_page.should_be_product_price_in_basket_message()
    product_page.should_be_product_price_in_basket_top()
'''
@pytest.mark.parametrize('link', variants)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.parametrize('link', variants)
def test_guest_cant_see_success_message(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.guest_cant_see_success_message()

@pytest.mark.parametrize('link', variants)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.message_disappeared_after_adding_product_to_basket()