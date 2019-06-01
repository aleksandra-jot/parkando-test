from Lib.PageLocators.ConfirmationLocators import ConfirmationLocators
import time


class ConfirmationObject(object):
    def __init__(self, driver):
        self.driver = driver

    def confirmation(self):
        confirm_button = self.driver.find_element_by_xpath(ConfirmationLocators().confirm)
        confirm_button.click()
        time.sleep(5)

    def choose_other(self):
        return_button = self.driver.find_element_by_xpath(ConfirmationLocators().back)
        return_button.click()
        time.sleep(2)

    def logout(self):
        logout_button = self.driver.find_element_by_xpath(ConfirmationLocators().logout)
        logout_button.click()
        time.sleep(2)