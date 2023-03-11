from .base_page import BasePage
from .locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        self.solve_quiz_and_get_code()

    def should_be_product_name_in_success_message(self):
        pr_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADDED)
        assert pr_name.text == message.text, "Product name is not correct in success message"

    def should_be_product_price_in_basket_top(self):
        pr_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price1 = self.browser.find_element(*ProductPageLocators.BASKET_PRICE1)
        assert pr_price.text in basket_price1.text, "Product price is not correct in basket top"

    def should_be_product_price_in_basket_message(self):
        pr_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price2 = self.browser.find_element(*ProductPageLocators.BASKET_PRICE2)
        assert pr_price.text in basket_price2.text, "Product price is not correct in basket message"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        self.solve_quiz_and_get_code()
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED)

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED)

    def message_disappeared_after_adding_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        self.solve_quiz_and_get_code()
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_ADDED)

