import selenium
from Locators.Locators import NewRegistration
from PageObjects.BasePage import BasePage


class RegistrationClass(BasePage):

    def registration(self,driver,email,password,retypedpassword,firstname,lastname,country,state,ZIPcode,city,address1,address2,contact):
        try:
            self.driver = driver
            self.driver.get(NewRegistration.url)
            BasePage.sendKeys(self, NewRegistration.email, email)
            BasePage.sendKeys(self, NewRegistration.password, password)
            BasePage.sendKeys(self, NewRegistration.repassword, retypedpassword)
            BasePage.sendKeys(self, NewRegistration.firstname, firstname)
            BasePage.sendKeys(self, NewRegistration.lastname, lastname)
            BasePage.sendKeys(self, NewRegistration.ZipCode, int(ZIPcode))
            BasePage.sendKeys(self, NewRegistration.city, city)
            BasePage.sendKeys(self, NewRegistration.addressline1, address1)
            BasePage.sendKeys(self, NewRegistration.addressline2, address2)
            BasePage.sendKeys(self, NewRegistration.phone,int(contact))
            BasePage.select_by_text(self,NewRegistration.country,country)
            BasePage.select_by_text(self,NewRegistration.state,state)
            BasePage.click(self,NewRegistration.registerbtn)
        except Exception as log:
            print(log)

    def is_registration_successful(self):
        return BasePage.is_visible(self,NewRegistration.myaccounttitle)







