import pytest
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory

@pytest.fixture
def wp():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")
    try:
        yield driver
    finally:
        driver.close()


class LoginPage(PageFactory):

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver =driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "edtUserName": ('ID', 'user_login'),
        "edtPassword": ('NAME', 'pwd'),
        "btnSignIn": ('XPATH', '//input[@value="Log In"]'),
        "menuMedia": ('CSS', "#menu-media > a"),
        "unknownElement": ("CSS", "somethingWrong"),
    }

    def login(self):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text("opensourcecms")               # edtUserName become class variable using PageFactory
        self.edtPassword.set_text("opensourcecms")
        self.btnSignIn.click_button()


def test_Login(wp):
    pglogin = LoginPage(wp)
    pglogin.login()
    pglogin.menuMedia.click()
    # CSS selector were not working as expected while calling a CSS SELECTOR twice
    # because By.CSS_SELECTOR return a string 'css selector' which is
    # not present in TYPE_OF_LOCATORS, also getattr were altering locators
    # attribue
    pglogin.menuMedia.click()


def test_not_found_element(wp):
    with pytest.raises(Exception) as ex:
        pglogin = LoginPage(wp)
        pglogin.timeout = 2
        pglogin.unknownElement
    assert 'unknownElement - locator: (css selector, somethingWrong)' in str(ex.value)
