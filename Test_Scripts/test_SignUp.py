import unittest

import pytest
from allure_commons.types import AttachmentType
from ddt import ddt, data, unpack

from DataDrivenTesting.read_csv import getCSVData
from PageObjects.SignUppage import SignupClass
import allure

@ddt
@allure.severity(allure.severity_level.NORMAL)
class TestSignUp(unittest.TestCase):

    #@pytest.mark.usefixtures("setUp")
    #def objectsetup(self):
      #   self.driver = signupclass(self,)
    @pytest.mark.usefixtures("setUp")
    @data(*getCSVData("C:\\Users\\rajdeep.m\\PycharmProjects\\Avactis\\DataDrivenTesting\\ConfigData.csv"))
    @unpack
    def test_signup(self,credential,emailid,password):
        SignupClass.signup(self,self.driver,emailid,password)
        self.assertEqual(SignupClass.is_signup_successful(self),eval(credential))
        print(SignupClass.is_signup_successful(self))
        allure.attach(self.driver.get_screenshot_as_png(),name="TestSignUP",attachment_type = AttachmentType.PNG)









