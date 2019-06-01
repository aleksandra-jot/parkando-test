from Lib.PageObjects.HomeObject import HomeObject
from Lib.PageObjects.AssertLogObject import AssertLogObject
from Lib.BaseSetUp.BaseTestTestup import BaseTestTestup
from Lib.PageObjects.ParkingObject import ParkingObject
from Lib.PageObjects.ConfirmationObject import ConfirmationObject


class TestBooking(BaseTestTestup):

    def test_booking_happy(self):
        parking = ParkingObject(self.driver)
        HomeObject(self.driver).user1_change()
        AssertLogObject(self.driver, parking).assert_reservation()
        ConfirmationObject(self.driver).logout()
