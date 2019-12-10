selenium-page-factory
=====================

<img src="./selenium-page-factory_logo.png"  height="150">

Python library provides page factory approach to implement page object model in selenium

Project Page
=============
https://selenium-page-factory.readthedocs.io

Introduction
============

* A Page Factory is one way of implementing a Page Object Model. In order to support the Page Object pattern.
* As in Java we are using @findBy, here we are declaring all web element in dictionary.
Dictionary keys become WebElement / class member variable with having all extended WebElement methods.
  

Main Features
=============

* Initialise all the webElements declared in Point at a time.
* All WebElements methods are re-define to add extra features eg- click method extended to have explicit wait.
* Cent percent unittest coverage.

Installation
=============
pip install

```shell
> pip install selenium-page-factory
```

WebElements Methods
===================
* set_text
* get_text
* clear_text
* click_button
* get_list_item_count
* select_element_by_text
* select_element_by_index
* select_element_by_value
* get_all_list_item
* get_list_selected_item
* hover
* is_Checked
* getAttribute
* element_to_be_clickable
* invisibility_of_element_located
* visibility_of_element_located
 
 Note: 
 Every WebElement will be created after verifying it's Presence and visibility on Page at Run-Time. 
 
Examples
=============
Python - Unittest

```python
from seleniumpagefactory.Pagefactory import PageFactory
import unittest
from selenium import webdriver

class LoginPage(PageFactory):

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "edtUserName": ('ID', 'user_login'),
        "edtPassword": ('NAME', 'pwd'),
        "btnSignIn": ('XPATH', '//input[@value="Log In"]')
    }

    def login(self):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text("opensourcecms")               # edtUserName become class variable using PageFactory
        self.edtPassword.set_text("opensourcecms")
        self.btnSignIn.click_button()


class LoginTest(unittest.TestCase):

    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

        pglogin = LoginPage(driver)
        pglogin.login()

if __name__ == "__main__":
     unittest.main()
```
Python - Pytest

Inside test_Login.py
```python
import pytest
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory

def test_Login():
    driver = webdriver.Chrome("")
    driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

    pglogin = LoginPage(driver)
    pglogin.login()

class LoginPage(PageFactory):

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "edtUserName": ('ID', 'user_login'),
        "edtPassword": ('NAME', 'pwd'),
        "btnSignIn": ('XPATH', '//input[@value="Log In"]')
    }

    def login(self):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text("opensourcecms")               # edtUserName become class variable using PageFactory
        self.edtPassword.set_text("opensourcecms")
        self.btnSignIn.click_button()
```

Pre-Requisite
=============
Every Page in Page Object Model should have WebDriver object as class member
as shown below

```python
class PageClass(PageFactory):

    def __init__(self,driver):
        self.driver = driver
```
