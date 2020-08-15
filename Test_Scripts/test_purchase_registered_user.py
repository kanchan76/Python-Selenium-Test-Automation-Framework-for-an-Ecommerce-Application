import unittest
import pytest
from allure_commons.types import AttachmentType
from ddt import ddt, data, unpack
from PageObjects.Purchase_as_guest import Purchase
import allure
from Data.ReadExcel import get_data


@ddt
@allure.severity(allure.severity_level.NORMAL)
class TestPurchase(unittest.TestCase):
    @pytest.mark.usefixtures("setUp")
    @data(get_data("C:\\Users\\rajdeep.m\\PycharmProjects\\Avactis\\Data\\ProductData.xlsx"))
    #@unpack
    def test_add_to_cart(self,testdata):
        is_addedtocart=[]
        for product in testdata:
            Purchase.Add_To_Cart(self,self.driver,product[2])
        for product in testdata:
            is_addedtocart.append(Purchase.Is_Product_Added_To_Cart(self,self.driver,product[1]))
        self.assertTrue(is_addedtocart, msg = "product not added to cart!")
        Purchase.checkout(self,self.driver,*get_data("C:\\Users\\rajdeep.m\\PycharmProjects\\Avactis\\Data\\Addresses.xls"))
        self.assertTrue(Purchase.Is_order_placed(self,self.driver))
        self.assertTrue(Purchase.Is_order_placed(self, self.driver))











