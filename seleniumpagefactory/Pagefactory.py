from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class PageFactoryException(Exception):
    """Base class for exceptions in this module."""
    pass
class ElementNotFoundException(PageFactoryException):
    """Raised when the element is not found in the page. (Using ` EC.presence_of_element_located` function from within __getattr__ method)."""
class ElementNotVisibleException(PageFactoryException):
    """Raised when the element is not visible in the page. (Using `EC.visibility_of_element_located` function from within __getattr__ method)."""


class PageFactory(object):
    timeout = 10
    highlight = False
    mobile_test = False     #Added for Mobile support

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

        if self.mobile_test == True:
            if loc in self.locators.keys():
                element = self.find_element_by_accessibility_id(self.locators[loc][1])
                return element             
        else:
            if loc in self.locators.keys():
                locator = (self.TYPE_OF_LOCATORS[self.locators[loc][0].lower()], self.locators[loc][1])
                try:
                    element = WebDriverWait(self.driver, self.timeout).until(
                        EC.presence_of_element_located(locator)
                    )
                except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                    raise ElementNotFoundException(
                        "An exception of type " + type(e).__name__ +
                        " occurred. With Element -: " + loc +
                        " - locator: (" + locator[0] + ", " + locator[1] + ")"
                    )
    
                try:
                    element = WebDriverWait(self.driver, self.timeout).until(
                        EC.visibility_of_element_located(locator)
                    )
                except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                    raise ElementNotVisibleException(
                        "An exception of type " + type(e).__name__ +
                        " occurred. With Element -: " + loc +
                        " - locator: (" + locator[0] + ", " + locator[1] + ")"
                    )
    
                element = self.get_web_element(*locator)
                element._locator = locator
                return element
        return super().__getattr__(loc)

    def get_web_element(self, *loc):
        element = self.driver.find_element(*loc)
        self.highlight_web_element(element)
        return element

    def highlight_web_element(self, element):
        """
        To highlight webElement
        :param: WebElement
        :return: None
        """
        if self.highlight:
            self.driver.execute_script("arguments[0].style.border='2px ridge #33ffff'", element)

    def select_element_by_text(self, text):
        """
        Select webElement from dropdown list
        :param: Text of Item in dropdown
        :return: None
        """
        select = Select(self)
        select.select_by_visible_text(text)

    def select_element_by_index(self, index):
        """
        Select webElement from dropdown list
        :param: Index of Item in dropdown
        :return: None
        """
        select = Select(self)
        select.select_by_index(index)

    def select_element_by_value(self, value):
        """
        Select webElement from dropdown list
        :param: value of Item in dropdown
        :return: None
        """
        select = Select(self)
        select.select_by_value(value)

    def get_list_item_count(self):
        """
        Count of Item from Dropdown
        :param: None
        :return: count
        """
        select = Select(self)
        return len(select.options)

    def get_all_list_item(self):
        """
        Get list of Item from Dropdown
        :param: None
        :return: list of items present in dropdown
        """
        select = Select(self)
        list_item = []
        for item in select.options:
            list_item.append(item.text)
        return list_item

    def get_list_selected_item(self):
        """
        Get list of Selected item in Dropdown
        :param: None
        :return: list of items selected in dropdown
        """
        select = Select(self)
        list_item = []
        for item in select.all_selected_options:
            list_item.append(item.text)
        return list_item

    def verify_list_item(self, text):
        """
        Verify text to be present in  Dropdown
        :param: item to be verify
        :return: True / False
        """
        select = Select(self)
        list_item = []
        for item in select.options:
            if text == item.text:
                return True
        return False

    def click_button(self):
        """
        Perform  click on webElement
        :param: None
        :return: webElement
        """
        self.element_to_be_clickable()
        self.click()
        return self

    def double_click(self):
        """
        perform Double click on webElement
        :param: None
        :return: webElement
        """
        self.element_to_be_clickable()
        ActionChains(self.parent).double_click(self).perform()
        return self

    def context_click(self):
        """
        perform Right click on webElement
        Added support for Selenium 4
        :param: None
        :return: webElement
        """
        self.element_to_be_clickable()
        ActionChains(self.parent).context_click(on_element=self)
        return self

    def click_and_hold(self):
        """
        This method will replace the moveToElement(onElement).clickAndHold()
        Added support for Selenium 4
        :param: None
        :return: webElement
        """
        self.element_to_be_clickable()
        ActionChains(self.parent).click_and_hold(on_element=self)
        return self

    def release(self):
        """
        Releasing a held mouse button on an element.
        Added support for Selenium 4
        :param: None
        :return: webElement
        """
        ActionChains(self.parent).release(on_element=self)
        return self

    def set_text(self, value):
        """
        type text in input box
        :param: Text to be Enter
        :return: webElement
        """
        self.element_to_be_clickable()
        self.send_keys(value)
        return self

    def get_text(self):
        """
        get text from input box
        :param: None
        :return: text from webElement
        """
        return self.text

    def clear_text(self):
        """
        Clear text from EditBox
        :param: None
        :return: None
        """
        self.clear()

    def hover(self):
        """
        perform hover operation on webElement
        :param: None
        :return: None
        """
        ActionChains(self.parent).move_to_element(self).perform()

    def is_Checked(self):
        """
        Check Radio button / CheckBox is selected
        :param: None
        :return: Boolean
        """
        return self.isSelected()

    def is_Enabled(self):
        """
        get Enable state of webElement
        :param: None
        :return: Boolean
        """
        return self.isEnabled()

    def getAttribute(self, attributeName):
        """
        get webElement attribute
        :param: name of Attribute
        :return: webElement attribute value
        """
        return self.get_attribute(attributeName)

    def setAttribute(self, attributeName, value):
        """
        set webElement attribute
        :param: name of Attribute
        :return: webElement attribute value
        """
        return self.parent.execute_script("arguments[0].setAttribute(" + attributeName + "," + value + ")", self)

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

    def execute_script(self, script):
        """
        Execute JavaScript using web driver on selected web element
        :param: Javascript to be execute
        :return: None / depends on Script
        """
        return self.parent.execute_script(script, self)


WebElement.click_button = PageFactory.click_button
WebElement.double_click = PageFactory.double_click
WebElement.context_click = PageFactory.context_click
WebElement.click_and_hold = PageFactory.click_and_hold
WebElement.release = PageFactory.release
WebElement.element_to_be_clickable = PageFactory.element_to_be_clickable
WebElement.invisibility_of_element_located = PageFactory.invisibility_of_element_located
WebElement.visibility_of_element_located = PageFactory.visibility_of_element_located
WebElement.set_text = PageFactory.set_text
WebElement.get_text = PageFactory.get_text
WebElement.hover = PageFactory.hover
WebElement.clear_text = PageFactory.clear_text
WebElement.w3c = PageFactory.w3c
WebElement.is_Checked = PageFactory.is_Checked
WebElement.is_Enabled = PageFactory.is_Enabled
WebElement.getAttribute = PageFactory.getAttribute
WebElement.setAttribute = PageFactory.setAttribute
WebElement.select_element_by_text = PageFactory.select_element_by_text
WebElement.select_element_by_index = PageFactory.select_element_by_index
WebElement.select_element_by_value = PageFactory.select_element_by_value
WebElement.get_list_item_count = PageFactory.get_list_item_count
WebElement.get_all_list_item = PageFactory.get_all_list_item
WebElement.get_list_selected_item = PageFactory.get_list_selected_item
WebElement.execute_script = PageFactory.execute_script
WebElement.verify_list_item = PageFactory.verify_list_item
