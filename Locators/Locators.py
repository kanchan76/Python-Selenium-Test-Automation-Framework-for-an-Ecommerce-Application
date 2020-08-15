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


class NewRegistration:
    """New registration Locators"""
    url = "http://localhost:8012/avactis/register.php"
    register = (By.LINK_TEXT,"http://localhost:8012/avactis/register.php")
    email = (By.NAME,"customer_info[Customer][Email]")
    password = (By.NAME,"customer_info[Customer][Password]")
    repassword = (By.NAME,"customer_info[Customer][RePassword]")
    firstname =(By.NAME,"customer_info[Customer][FirstName]")
    lastname = (By.NAME,"customer_info[Customer][LastName]")
    country = (By.NAME,"customer_info[Customer][Country]")
    state = (By.NAME,"customer_info[Customer][State]")
    ZipCode = (By.NAME,"customer_info[Customer][ZipCode]")
    city = (By.NAME,"customer_info[Customer][City]")
    addressline1 = (By.NAME,"customer_info[Customer][Streetline1]")
    addressline2 = (By.NAME,"customer_info[Customer][Streetline2]")
    phone = (By.NAME,"customer_info[Customer][Phone]")
    registerbtn =(By.XPATH,"//input[@value='Register']")
    myaccounttitle = (By.XPATH, "//h3[contains(text(),'Manage Account and View Orders')]")
    myaccounttitletext = "Manage Account and View Orders"


class AddToCart:
    url = "http://localhost:8012/avactis/"
    product_name=(By.XPATH,"//div[@class='product_name']")
    add_to_cart = (By.XPATH,"//input[@value='Add To Cart']")
    my_cart = (By.LINK_TEXT,"My cart")
    my_cart_url ="http://localhost:8012/avactis/cart.php"
    checkout = (By.XPATH,"//a[@class='btn btn-primary'][contains(text(),'Checkout ')] ")
    continue_checkout1 = (By.XPATH,"//input[@onclick='submitStep(1);'][@type='button']")
    continue_checkout2 = (By.XPATH, "//input[@onclick='submitStep(2);'][@type='button']")
    ground_shipping = (By.XPATH,"//label[contains(text(),' Ground Shipping')]")
    place_order = (By.XPATH,"//input[@value='Place Order']")
    cart_table = (By.XPATH,"//table[@summary='Shopping cart']")
    product_added_message_box = (By.XPATH,"//div[@class='ajax_message_box_text']")
    shipping_same_as_billing = (By.NAME,"checkbox_shipping_same_as_billing")
    order_status = (By.XPATH,"//div[@class='row margin-bottom-40']/h1[contains(text(),'Thank you for your order!')]")
    order_success_status = "Your order is placed. Order ID:"


class BillingAddress:
    email = (By.NAME,"billingInfo[Email]")
    firstname =(By.NAME,"billingInfo[Firstname]")
    lastname = (By.NAME,"billingInfo[Lastname]")
    country = (By.NAME,"billingInfo[Country]")
    state = (By.NAME,"billingInfo[Statemenu]")
    ZipCode = (By.NAME,"billingInfo[Postcode]")
    city = (By.NAME,"billingInfo[City]")
    addressline1 = (By.NAME,"billingInfo[Streetline1]")
    addressline2 = (By.NAME,"billingInfo[Streetline2]")
    phone = (By.NAME,"billingInfo[Phone]")


class ShippingAddress:
    email = (By.NAME, "shippingInfo[Firstname]")
    firstname = (By.NAME, "shippingInfo[Lastname]")
    lastname = (By.NAME, "shippingInfo[Lastname]")
    country = (By.NAME, "shippingInfo[Country]")
    state = (By.NAME, "shippingInfo[Statemenu]")
    ZipCode = (By.NAME, "shippingInfo[Postcode]")
    city = (By.NAME, "shippingInfo[City]")
    addressline1 = (By.NAME, "shippingInfo[Streetline1]")
    addressline2 = (By.NAME, "shippingInfo[Streetline2]")
    phone = (By.NAME, "shippingInfo[Phone]")


class ProductCategories:
    notebooks = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Notebooks')]")
    desktops = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Desktops')]")
    furniture =(By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Furniture')]")
    sports = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Sport')]")
    classic_films = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Classic Films')]")
    Kids_dvd = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Kids DVDs')]")
    tv_on_dvd = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'TV on DVD')]")
    apparel = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Apparel')]")
    digital_distribution = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Digital Distribution')]")
    computers = (By.XPATH,"//li[@class='list-group-item clearfix']/a[contains(text(),'Computers')]")
    DVDS =(By.XPATH,"//li[@class='list-group-item clearfix dropdown']/a[contains(text(),'DVD')]")








    









