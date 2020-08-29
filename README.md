# Python-Selenium-Test-Automation-Framework-for-an-Ecommerce-Application
# Description
Test Automation Framework using selenium and Python with the below features:

* Framework is based on page object model.
* Reporting using Allure report.
* Reading locators from .py file.
* Reading test data from CSV/XLS file.
---
# Pre-requisites
* Python 3.x
* Allure
---
# Directories
* Data- Xls/CSV files with data
* DataDrivenTesting- xls/CSV configuration files
* Locators - .py files wither locators
* PageObjects - pages present here
* Reports - Allure reports with screenshots 
* Test - Test sripts  
---
# Run the Test case
In order to run the test case after creation, use on of the below commands:

py.test --alluredir=allure_report tests/test_login.py

allure serve allure_report
