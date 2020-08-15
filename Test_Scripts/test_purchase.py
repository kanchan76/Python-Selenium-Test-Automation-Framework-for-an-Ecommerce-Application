import unittest
import pytest
from allure_commons.types import AttachmentType
from ddt import ddt, data, unpack
from PageObjects.Purchase_as_guest import Purchase
import allure
from Data.ReadExcel import get_data
from PageObjects.SignUppage import SignupClass
from DataDrivenTesting.read_csv import getCSVData


@ddt
@allure.severity(allure.severity_level.NORMAL)
class TestPurchase(unittest.TestCase):
    @pytest.mark.usefixtures("setUp")
    @data(get_data("C:\\Users\\rajdeep.m\\PycharmProjects\\Avactis\\Data\\ProductData.xlsx"))
    #@unpack
    def test_purchase(self,testdata):
        credentials = getCSVData("C:\\Users\\rajdeep.m\\PycharmProjects\\Avactis\\DataDrivenTesting\\ConfigData.csv")
        credential = credentials[:1]
        print(credentials,credential)
        SignupClass.signup(self,self.driver,credential[0][1],credential[0][2])
        self.assertEqual(SignupClass.is_signup_successful(self),eval(credential[0][0]))
        is_addedtocart=[]
        for product in testdata:
            Purchase.Add_To_Cart(self,self.driver,product[2])
        for product in testdata:
            is_addedtocart.append(Purchase.Is_Product_Added_To_Cart(self,self.driver,product[1]))
        self.assertTrue(is_addedtocart, msg = "product not added to cart!")
        Purchase.checkout_registered_user(self,self.driver)
        self.assertTrue(Purchase.Is_order_placed(self,self.driver))
        allure.attach(self.driver.get_screenshot_as_png(), name="TestSignUP", attachment_type=AttachmentType.PNG)












