from Lib.PageLocators.HomeLocators import WelcomeLocators
from Lib.PageLocators.HomeLocators import HomeLocators
from Lib.PageLocators.ParkingLocators import ParkingLocators
from Lib.PageLocators.ConfirmationLocators import ConfirmationLocators
from TestData.CommonData import *


class AssertLogObject(object):
    def __init__(self, driver, parking):
        self.driver = driver
        self.parking = parking

    def assert_happylog(self):

        self.locator = WelcomeLocators()

        actual_login_element = self.driver.find_element_by_xpath(self.locator.welcome_username)
        actual_username = actual_login_element.text
        expected_username = CommonData.happypath_data['name']
        assert actual_username.capitalize() == expected_username
        print('~~~~')
        print('UŻYTKOWNIK ZOSTAŁ PRAWIDŁOWO ZALOGOWANY')
        print('~~~~')

    def assert_badlog(self):

        self.locator = HomeLocators()

        alert_locator = self.driver.find_element_by_xpath(self.locator.alert_error)
        alert_text = alert_locator.text
        assert alert_text == "Nazwa musi być dłuższa niż 3 znaki"
        print('~~~~')
        print('UŻYTKOWNIK NIE ZOSTAŁ ZALOGOWANY')
        print('~~~~')

    def assert_booking(self):

        actual_booked_element = self.driver.find_element_by_xpath(ParkingLocators.alert_booked)
        actual_booked = actual_booked_element.text
        actual_booking = self.parking.park_id
        assert actual_booking == actual_booked
        print('~~~~')
        print('WYBÓR MIEJSCA WYKONANE POPRAWNIE')
        print('~~~~')

    def assert_reservation(self):
        expected_booked_element = self.driver.find_element_by_xpath(ConfirmationLocators.reservation)
        expected_booked = expected_booked_element.text
        actual_booked = CommonData.user1_data['park_place_id']
        assert actual_booked == expected_booked
        print('')
        print('~~~~')
        print('ASSERCJA NA WYBÓR MIEJSCA PRZEBIEGŁA POMYŚLNIE')
        print('~~~~')

