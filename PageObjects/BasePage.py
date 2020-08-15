from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from PageObjects import Webtables_handling


class BasePage():
    """"It contains all basic functions"""

    def __init__(self,driver):
        self.driver = driver

    def click(self,by_locator):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator)).click()

    def is_enabled(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            element = False
        return bool(element)

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def sendKeys(self,by_locator,fieldvalue):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(fieldvalue)
        except Exception as log:
            print(log)

    def submit(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).submit()

    def select_by_text(self,by_locator,text):
        try:
            Select(self.driver.find_element(*by_locator)).select_by_visible_text(str(text))

        except Exception as log:
            print(log)

    def Is_data_present_in_table(self,table_locator,data):
        try:
            table = Webtables_handling.WebTable_Optimized(WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(table_locator)))
            return table.presence_of_data(data)
        except Exception as log:
            print(log)

    def is_invisible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        except TimeoutException:
            element = False
        return bool(element)

    def get_text(self,by_locator):
        try:
            text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
            return text
        except Exception as log:
            print(log)









