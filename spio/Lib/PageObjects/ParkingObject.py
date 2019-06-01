from Lib.PageLocators.ParkingLocators import ParkingLocators
import time

class ParkingObject(object):

    def __init__(self, driver):
        self.driver = driver
        self.park_id = 0

    def choose_parking(self):
        parking = self.driver.find_element_by_xpath(ParkingLocators().choose_parking)
        parking.click()
        time.sleep(3)

    def choose_place(self):
        place = self.driver.find_element_by_xpath(ParkingLocators().choose_place)
        self.park_id = self.driver.find_element_by_xpath(ParkingLocators().choose_place).get_attribute("id")
        place.click()
        time.sleep(3)