from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class PageFactory(object):

    timeout = 10

    TYPE_OF_LOCATORS = {
        'css': By.CSS_SELECTOR,
        'id': By.ID,
        'name': By.NAME,
        'xpath': By.XPATH,
        'link_text': By.LINK_TEXT,
        'partial_link_text': By.PARTIAL_LINK_TEXT,
        'tag': By.TAG_NAME,
        'class_name': By.CLASS_NAME
    }

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        if not instance:
            return None
        else:
            self.driver = instance.driver

    def __getattr__(self, loc):

        if loc in self.locators.keys():
            self.locators[loc] = list(self.locators[loc])
            self.locators[loc][0] = self.TYPE_OF_LOCATORS[self.locators[loc][0].lower()]
            self.locators[loc] = tuple(self.locators[loc])
            try:
                element = WebDriverWait(self.driver,self.timeout).until(
                    EC.presence_of_element_located(self.locators[loc])
                )
            except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                raise Exception("An exception of type "+type(e).__name__+" occurred. With Element -: "+loc)

            try:
                element = WebDriverWait(self.driver,self.timeout).until(
                    EC.visibility_of_element_located(self.locators[loc])
                )
            except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                raise Exception("An exception of type " + type(e).__name__ + " occurred. With Element -: " + loc)

            element = self.get_web_element(*self.locators[loc])
            element._locator = self.locators[loc]
            return element

    def get_web_element(self, *loc):
        element = self.driver.find_element(*loc)
        return element

    def select_element_by_text(self, text):
        select = Select(self)
        select.select_by_visible_text(text)

    def select_element_by_index(self, index):
        select = Select(self)
        select.select_by_index(index)

    def select_element_by_value(self, value):
        select = Select(self)
        select.select_by_value(value)

    def click_button(self):
        self.element_to_be_clickable()
        self.click()
        return self

    def set_text(self, value):
        self.element_to_be_clickable()
        self.send_keys(value)
        return self

    def get_text(self):
        return self.text

    def clear(self):
        self.clear()

    def hover(self):
        ActionChains(self.parent).move_to_element(self).perform()

    def w3c(self):
        return self.w3c

    def element_to_be_clickable(self, timeout=None):
        """
        Wait till the element to be clickable
        """
        if timeout is None:
            timeout = PageFactory().timeout
        return WebDriverWait(self.parent, timeout).until(
            EC.element_to_be_clickable(self._locator)
        )

    def invisibility_of_element_located(self, timeout=None):
        """
        Wait till the element to be invisible
        """
        if timeout is None:
            timeout = PageFactory().timeout
        return WebDriverWait(self.parent, timeout).until(
            EC.invisibility_of_element_located(self._locator)
        )

    def visibility_of_element_located(self, timeout=None):
        """
        Wait till the element to be visible
        """
        if timeout is None:
            timeout = PageFactory().timeout
        return WebDriverWait(self.parent, timeout).until(
            EC.visibility_of(self)
        )


WebElement.click_button = PageFactory.click_button
WebElement.element_to_be_clickable = PageFactory.element_to_be_clickable
WebElement.invisibility_of_element_located = PageFactory.invisibility_of_element_located
WebElement.visibility_of_element_located = PageFactory.visibility_of_element_located
WebElement.set_text = PageFactory.set_text
WebElement.get_text = PageFactory.get_text
WebElement.hover = PageFactory.hover
WebElement.clear = PageFactory.clear
WebElement.w3c = PageFactory.w3c
WebElement.select_element_by_text = PageFactory.select_element_by_text
WebElement.select_element_by_index = PageFactory.select_element_by_index
WebElement.select_element_by_value = PageFactory.select_element_by_value

