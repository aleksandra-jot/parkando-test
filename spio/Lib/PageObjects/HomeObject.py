from Lib.PageLocators.HomeLocators import HomeLocators, WelcomeLocators
from TestData.CommonData import CommonData
import time


class HomeObject(object):
    def __init__(self, driver):
        self.driver = driver

    def happy_login(self):
        idlog = self.driver.find_element_by_xpath(HomeLocators().cardid_input)
        idlog.clear()
        idlog.send_keys(CommonData().happypath_data["cardid"])
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().name_input)
        namelog.clear()
        namelog.send_keys(CommonData().happypath_data["name"])
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().surname_input)
        namelog.clear()
        namelog.send_keys(CommonData().happypath_data["surname"])
        time.sleep(2)

        log = self.driver.find_element_by_xpath(HomeLocators().button_submit)
        log.click()
        time.sleep(1)

    def bad_login(self):
        idlog = self.driver.find_element_by_xpath(HomeLocators().cardid_input)
        idlog.clear()
        idlog.send_keys(CommonData().bad_data["cardid"])
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().name_input)
        namelog.clear()
        namelog.send_keys(CommonData().bad_data["name"])
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().surname_input)
        namelog.clear()
        namelog.send_keys(CommonData().bad_data["surname"])
        time.sleep(2)

        log = self.driver.find_element_by_xpath(HomeLocators().button_submit)
        log.click()
        time.sleep(2)

    def user1_change(self):
        idlog = self.driver.find_element_by_xpath(HomeLocators().cardid_input)
        idlog.clear()
        idlog.send_keys(CommonData().user1_data["cardid"])
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().name_input)
        namelog.clear()
        namelog.send_keys(CommonData().user1_data["name"])
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().surname_input)
        namelog.clear()
        namelog.send_keys(CommonData().user1_data["surname"])
        time.sleep(2)

        log = self.driver.find_element_by_xpath(HomeLocators().button_submit)
        log.click()
        time.sleep(2)

    def blank_login(self):
        idlog = self.driver.find_element_by_xpath(HomeLocators().cardid_input)
        idlog.clear()
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().name_input)
        namelog.clear()
        time.sleep(2)

        namelog = self.driver.find_element_by_xpath(HomeLocators().surname_input)
        namelog.clear()
        time.sleep(2)

        log = self.driver.find_element_by_xpath(HomeLocators().button_submit)
        log.click()
        time.sleep(2)


    def welcome(self):
        choose = self.driver.find_element_by_xpath(WelcomeLocators().welcome_button)
        choose.click()
        time.sleep(2)
