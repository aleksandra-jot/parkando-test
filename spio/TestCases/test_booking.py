from Lib.PageObjects.HomeObject import HomeObject
from Lib.PageObjects.AssertLogObject import AssertLogObject
from Lib.BaseSetUp.BaseTestTestup import BaseTestTestup
from Lib.PageObjects.ParkingObject import ParkingObject
from Lib.PageObjects.ConfirmationObject import ConfirmationObject


class TestBooking(BaseTestTestup):

    def test_booking_happy(self):
        parking = ParkingObject(self.driver)
        HomeObject(self.driver).happy_login()
        AssertLogObject(self.driver, parking).assert_happylog()
        HomeObject(self.driver).welcome()
        parking.choose_parking()
        parking.choose_place()
        AssertLogObject(self.driver, parking).assert_booking()
        ConfirmationObject(self.driver).confirmation()
        ConfirmationObject(self.driver).logout()

