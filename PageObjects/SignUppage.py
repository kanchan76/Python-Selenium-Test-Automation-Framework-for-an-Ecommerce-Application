
from PageObjects.BasePage import BasePage
import selenium
from Locators.Locators import SignUpPagelocators


class SignupClass(BasePage):

    def signup(self,driver,emailid,password):
        try:
            self.driver = driver
            self.driver.get(SignUpPagelocators.url)
            BasePage.sendKeys(self,SignUpPagelocators.emailid,emailid)
            BasePage.sendKeys(self,SignUpPagelocators.password,password)
            BasePage.click(self,SignUpPagelocators.signuputton)
        except Exception as log:
            print("error occured : ",log)

    def is_signup_successful(self):
        return BasePage.is_visible(self,SignUpPagelocators.myaccounttitle)







