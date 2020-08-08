from selenium.webdriver.common.by import By


class SignUpPagelocators():
    """Sign Up page Locators"""

    url = "http://localhost:8012/avactis/sign-in.php"
    emailid = (By.ID,"account_sign_in_form_email_id")
    password = (By.ID,"account_sign_in_form_passwd_id")
    signuputton =(By.XPATH,"//input[@class='btn btn-primary input_submit']")
    keepmesignup = (By.NAME,"remember_me")
    myaccounttitle = (By.XPATH,"//h3[contains(text(),'Manage Account and View Orders')]")
    myaccounttitletext ="Manage Account and View Orders"



class NewRegisteration():
    """New registration Locators"""
    url = "http://localhost:8012/avactis/sign-in.php"
    register = (By.LINK_TEXT,"http://localhost:8012/avactis/register.php")
    email = (By.NAME,"customer_info[Customer][Email]")
    password = (By.NAME,"customer_info[Customer][Password]")
    repassword = (By.NAME,"customer_info[Customer][RePassword]")
    firstname =(By.NAME,"customer_info[Customer][FirstName]")
    lastname = (By.NAME,"customer_info[Customer][LastName]")
    country = (By.ID,"customer_info_Customer_Country")
    state = (By.NAME,"customer_info[Customer][State]")
    ZipCode = (By.NAME,"customer_info[Customer][ZipCode]")
    city = (By.NAME,"customer_info[Customer][City]")
    addressline1 = (By.NAME,"customer_info[Customer][Streetline1]")
    addressline2 = (By.NAME,"customer_info[Customer][Streetline2]")
    phone = (By.NAME,"customer_info[Customer][Phone]")
    registerbtn =(By.CLASS_NAME,"en btn btn-primary btn-register input_submit")










