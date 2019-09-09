from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver =driver

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


def test_Login():
    driver = webdriver.Chrome("path for driver exe")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

    pglogin = LoginPage(driver)
    pglogin.login()
