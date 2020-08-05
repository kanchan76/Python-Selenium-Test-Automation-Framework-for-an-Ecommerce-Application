from PageObjects.SignUppage import SignupClass
import pytest
from DataDrivenTesting.read_csv import getCSVData
from ddt import ddt, data, unpack
import unittest
from Locators.Locators import SignUpPagelocators


@ddt
class TestSignUp(unittest.TestCase):

    #@pytest.mark.usefixtures("setUp")
    #def objectsetup(self):
      #   self.driver = signupclass(self,)
    @pytest.mark.usefixtures("setUp")
    @data(*getCSVData("C:\\Users\\rajdeep.m\\PycharmProjects\\Avactis\\DataDrivenTesting\\ConfigData.csv"))
    @unpack
    def test_signup(self,emailid,password):
        SignupClass.signup(self,self.driver,emailid,password)
        self.assertTrue(SignupClass.is_signup_successful(self))









