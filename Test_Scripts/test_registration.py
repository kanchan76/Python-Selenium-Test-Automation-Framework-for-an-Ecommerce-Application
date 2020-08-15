from Data.ReadExcel import get_data
import pytest
from allure_commons.types import AttachmentType
from ddt import ddt, data, unpack
from PageObjects.RegistrationPage import RegistrationClass
import allure
import unittest


@ddt
@allure.severity(allure.severity_level.NORMAL)
class TestRegistration(unittest.TestCase):
    @pytest.mark.usefixtures("setUp")
    @data(*get_data("C:\\Users\\rajdeep.m\\PycharmProjects\\Avactis\\Data\\RegistrationData.xlsx"))
    @unpack
    def test_registration(self,Test,email,password,retypedpassword,firstname,lastname,country,state,ZIPcode,city,address1,address2,contact):
        RegistrationClass.registration(self,self.driver,email,password,retypedpassword,firstname,lastname,country,state,ZIPcode,city,address1,address2,contact)
        if Test == "Positive":
            test_status = 1
        elif Test == "Negative":
            test_status = 0
        self.assertEqual(RegistrationClass.is_registration_successful(self), bool(test_status))
        allure.attach(self.driver.get_screenshot_as_png(), name="NewRegistration", attachment_type=AttachmentType.PNG)






