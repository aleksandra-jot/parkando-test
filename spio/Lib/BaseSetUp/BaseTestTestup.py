from Lib.BaseSetUp import ServerTest
import unittest
from selenium import webdriver


class BaseTestTestup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(360, 800)
        self.driver.get(ServerTest.Servertest.test_server_url)

    def tearDown(self):
        self.driver.close()