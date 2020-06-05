Introduction
============
* Python library provides page factory approach to implement page object model in selenium
* A Page Factory is one way of implementing a Page Object Model. In order to support the Page Object pattern.
* As in Java we are using @findBy, here we are declaring all web element in dictionary.
Dictionary keys become WebElement / class member variable with having all extended WebElement methods.
  
Github Project Page
===================

https://github.com/NayakwadiS/selenium-page-factory

Main Features
=============

* Initialise all the webElements declared in Point at a time.
* All WebElements methods are re-define to add extra features eg- click method extended to have explicit wait for element to be clickable.
* Cent percent unittest coverage.


Installation
=============
pip install::

	pip install selenium-page-factory

Update
===============
To updated to the lasted version::

	pip install selenium-page-factory --upgrade

Pre-Requisite
=============
Every Page in Page Object Model should have WebDriver object as class member
as shown below::

	class PageClass(PageFactory):

	    def __init__(self,driver):
		self.driver = driver
		self.timeout = 15 	#(Optional - Customise your explicit wait for every webElement)
		self.highlight = True 	#(Optional - To highlight every webElement in PageClass)

Extended WebElements Methods
============================
.. raw:: html
<embed>
<table>
  <tbody>
    <tr>
      <td >set_text</td>
      <td >get_text</td>
    </tr>
    <tr>
      <td >clear_text</td>
      <td >click_button</td>
    </tr>
    <tr>
      <td >double_click</td>
      <td >get_list_item_count</td>
    </tr>
	<tr>
      <td >select_element_by_text</td>
      <td >select_element_by_index</td>
    </tr>
	<tr>
      <td >select_element_by_value</td>
      <td >get_all_list_item</td>
    </tr>
	<tr>
      <td >get_list_selected_item</td>
      <td >highlight</td>
    </tr>
	<tr>
      <td >is_Enabled</td>
      <td >is_Checked</td>
    </tr>
	<tr>
      <td >getAttribute</td>
      <td >hover</td>
    </tr>
	<tr>
      <td >visibility_of_element_located</td>
      <td >invisibility_of_element_located</td>
    </tr>
	<tr>
      <td >element_to_be_clickable</td>
      <td >execute_script</td>
    </tr>
  </tbody>
</table>
</embed>

.. note::

	Every WebElement will be created after verifying it's Presence and visibility on Page at Run-Time. 

Examples
=============

Python - Unittest
--------------

Inside test_Login.py::

	import unittest
	from selenium import webdriver
	from seleniumpagefactory.Pagefactory import PageFactory

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


Python - Pytest
---------------

Inside test_Login.py::

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
		"lnkPost": ('XPATH', '//div[contains(text(),"Posts")]'),
        "lstAction": ('ID', 'bulk-action-selector-top')
	    }

	    def login(self):
		# set_text(), click_button() methods are extended methods in PageFactory
		self.edtUserName.set_text("opensourcecms")               # edtUserName become class variable using PageFactory
		self.edtPassword.set_text("opensourcecms")
		self.btnSignIn.click_button()

WebElement Methods Usage
==========================
set_text
---------
To perform set text operation::

	class LoginPage(PageFactory):
		
		def login(self):
			self.edtUserName.set_text("opensourcecms")

get_text
---------
To clear text from edit box::

	class LoginPage(PageFactory):
		
		def login(self):
			text_from_element = self.edtUserName.get_text()

clear_text
---------
To clear text from edit box::

	class LoginPage(PageFactory):
		
		def login(self):
			self.edtUserName.clear_text()  

click_button
-------------
To Click on any WebElement::

	class LoginPage(PageFactory):
		
		def login(self):
			self.btnSignIn.click_button()
						
						
get_list_item_count
------------------
Get list item count::

	class customPage(PageFactory):
		
		def perform_list_operation(self):
			list_item_count = self.lstAction.get_list_item_count()

select_element_by_text
----------------------
To Select list item by using visible text::

	class customPage(PageFactory):
		
		def perform_list_operation(self):
			self.lstAction.select_element_by_text("India")

select_element_by_index
----------------------
To Select list item by using index::

	class customPage(PageFactory):
		
		def perform_list_operation(self):
			self.lstAction.select_element_by_index(0)

select_element_by_value
----------------------
To Select list item by using webElement value property::

	class customPage(PageFactory):
		
		def perform_list_operation(self):
			self.lstAction.select_element_by_value("country India")

get_all_list_item
------------------
Get all list items::

	class customPage(PageFactory):
		
		def perform_list_operation(self):
			list_items = self.lstAction.get_all_list_item()

get_list_selected_item
------------------
Get selected list item::

	class customPage(PageFactory):
		
		def perform_list_operation(self):
			selected_list_item = self.lstAction.get_list_selected_item()

hover
-------------
To hover on any WebElement::

	class customPage(PageFactory):
		
		def login(self):
			self.btnSignIn.hover()

is_Checked
------------------
Verify RadioButton and CheckBox::

	class customPage(PageFactory):
		
		def checkbox_radiobutton_operation(self):
			checkBox_is_selected = self.chkGender.is_Checked()
			
is_Enabled
------------------
Verify Enable state of WebElemnt::

	class customPage(PageFactory):
		
		def checkbox_radiobutton_operation(self):
			checkBox_is_enabled = self.chkGender.is_Enabled()

getAttribute
------------------
Get HTML attribute value of WebElemnt::

	class customPage(PageFactory):
		
		def link_operation(self):
			title_attribute = self.nextLink.getAttribute("title")			
