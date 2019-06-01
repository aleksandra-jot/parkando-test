from Lib.PageObjects.HomeObject import HomeObject
from Lib.PageObjects.AssertLogObject import AssertLogObject
from Lib.BaseSetUp.BaseTestTestup import BaseTestTestup
from Lib.PageObjects.ParkingObject import ParkingObject


class TestLogin(BaseTestTestup):

    def test_1_log_happy(self):
        parking = ParkingObject(self.driver)
        HomeObject(self.driver).happy_login()
        AssertLogObject(self.driver, parking).assert_happylog()

    def test_2_log_sad(self):
        parking = ParkingObject(self.driver)
        HomeObject(self.driver).bad_login()
        AssertLogObject(self.driver, parking).assert_badlog()

    def test_3_log_blank(self):
        parking = ParkingObject(self.driver)
        HomeObject(self.driver).blank_login()
        AssertLogObject(self.driver, parking).assert_blank()
