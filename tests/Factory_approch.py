from seleniumpagefactory.Pagefactory import PageFactory
import unittest
from os import environ

from selenium import webdriver

class LoginPage(PageFactory):

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "edtUserName": ('ID', 'user_login'),
        "edtPassword": ('NAME', 'pwd'),
        "btnSignIn": ('XPATH', '//input[@value="Log In"]'),
		"lnkPost": ('XPATH','//div[contains(text(),"Posts")]'),
		"lstAction": ('ID','bulk-action-selector-top')
    }

    def login(self):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text("opensourcecms")               # edtUserName become class variable using PageFactory
        self.edtPassword.set_text("opensourcecms")
        self.btnSignIn.click_button()


class LoginTest(unittest.TestCase):

    def test_Login(self):
        driver = webdriver.Chrome("D:\AutomationTool\Resources\drivers\chromedriver.exe")
        driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")
        pglogin = LoginPage(driver)
        pglogin.edtUserName.set_text("opensourcecms")               # edtUserName become class variable using PageFactory
        pglogin.edtPassword.set_text("opensourcecms")
        pglogin.btnSignIn.click_button()
        pglogin.lnkPost.click_button()
        print(pglogin.lstAction.get_all_list_item())


if __name__ == "__main__":
     unittest.main()