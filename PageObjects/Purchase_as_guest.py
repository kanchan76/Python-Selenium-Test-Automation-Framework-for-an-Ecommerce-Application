from PageObjects.BasePage import BasePage
import selenium
from Locators import Locators


class Purchase(BasePage):

    def Add_To_Cart(self,driver,url):
        try:
            self.driver = driver
            self.driver.get(url)
            BasePage.click(self,Locators.AddToCart.add_to_cart)
            BasePage.is_invisible(self,Locators.AddToCart.product_added_message_box)
        except Exception as log:
            print("Error",log)

    def Is_Product_Added_To_Cart(self,driver,product_name):
        try:
            self.driver = driver
            BasePage.click(self,Locators.AddToCart.my_cart)
            return BasePage.Is_data_present_in_table(self,Locators.AddToCart.cart_table,product_name)
        except Exception as log:
            print("Error",log)

    def checkout(self,driver,get_billing_address):
        try:
            self.driver = driver
            firstname, lastname,email, country, ZIPcode, state,  city, address1, address2, contact = get_billing_address
            print(firstname,city)
            BasePage.click(self,Locators.AddToCart.checkout)
            BasePage.sendKeys(self, Locators.BillingAddress.email, email)
            BasePage.sendKeys(self, Locators.BillingAddress.firstname, firstname)
            BasePage.sendKeys(self, Locators.BillingAddress.lastname, lastname)
            BasePage.sendKeys(self, Locators.BillingAddress.ZipCode, int(ZIPcode))
            BasePage.sendKeys(self, Locators.BillingAddress.city, city)
            BasePage.sendKeys(self, Locators.BillingAddress.addressline1, address1)
            BasePage.sendKeys(self, Locators.BillingAddress.addressline2, address2)
            BasePage.sendKeys(self, Locators.BillingAddress.phone,int(contact))
            BasePage.select_by_text(self,Locators.BillingAddress.country,country)
            BasePage.select_by_text(self,Locators.BillingAddress.state,state)
            BasePage.click(self,Locators.AddToCart.shipping_same_as_billing)
            BasePage.click(self,Locators.AddToCart.continue_checkout1)
            BasePage.click(self,Locators.AddToCart.ground_shipping)
            BasePage.click(self,Locators.AddToCart.continue_checkout2)
            BasePage.click(self,Locators.AddToCart.place_order)
        except Exception as log:
            print(log)

    def Is_order_placed(self,driver):
        try:
            self.driver = driver
            return BasePage.is_visible(self,Locators.AddToCart.order_status)
        except Exception as log:
            print("Error",log)

    def checkout_registered_user(self,driver):
        try:
            self.driver = driver
            BasePage.click(self,Locators.AddToCart.checkout)
            BasePage.click(self,Locators.AddToCart.continue_checkout1)
            BasePage.click(self,Locators.AddToCart.ground_shipping)
            BasePage.click(self,Locators.AddToCart.continue_checkout2)
            BasePage.click(self,Locators.AddToCart.place_order)
        except Exception as log:
            print(log)





