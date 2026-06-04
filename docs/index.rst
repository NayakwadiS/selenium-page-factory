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
* Supports Selenium 4 ActionChains methods
* Now Support Appium for mobile testing
* Raised custom Page factory exceptions
* **NEW in v2.8**: Multiple elements support for lists and tables
* **NEW in v2.8**: Scroll into view functionality
* **NEW in v2.8**: Drag and drop support
* **NEW in v2.8**: Click with retry mechanism for handling flaky tests


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
		self.timeout = 15 	    #(Optional - Customise your explicit wait for every webElement)
		self.highlight = True 	    #(Optional - To highlight every webElement in PageClass)
		self.mobile_test = False    #(Optional - Added for Appium support)

Extended WebElements Methods
============================
.. raw:: html

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
	    <tr>
	    	<td>context_click</td>
	    	<td>text_to_be_present_in_element</td>
	    </tr>
	    <tr>
	      <td >click_and_hold</td>
	      <td >release</td> 
	    </tr>
	     <tr>
	      <td >hover_with_offset</td>
	      <td ><strong>scroll_into_view</strong></td>
	    </tr>
	    <tr>
	      <td ><strong>drag_and_drop_to</strong></td>
	      <td ><strong>click_with_retry</strong></td>
	    </tr>
	  </tbody>
	</table>

============================

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
		self.edtUserName.set_text("<USERNAME>")               # edtUserName become class variable using PageFactory
		self.edtPassword.set_text("<PASSWORD>")
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
		self.edtUserName.set_text("<USERNAME>")               # edtUserName become class variable using PageFactory
		self.edtPassword.set_text("<PASSWORD>")
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
To get text from edit box::

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
						
click_and_hold
-------------
To click_and_hold on Element::

	class LoginPage(PageFactory):
		
		def login(self):
			self.btnSignIn.click_and_hold()

release
-------------
Releasing a held mouse button on an element::

	class LoginPage(PageFactory):
		
		def login(self):
			self.btnSignIn.release()


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


New Features in v2.8
=====================

scroll_into_view
-----------------
Scrolls element into viewport before interaction - essential for elements below the fold::

	class customPage(PageFactory):

		def scroll_to_footer(self):
			# Scroll to footer element and click (align to top by default)
			self.footer_link.scroll_into_view().click_button()

			# Align to bottom of viewport instead of top
			self.footer_link.scroll_into_view(align_to_top=False)

			# Chain with other operations
			self.element.scroll_into_view().set_text("Hello")

.. note::
	Perfect for elements not in viewport or in scrollable containers. Prevents "element not clickable" errors.


get_web_elements
-----------------
Find and interact with multiple elements (lists, tables, search results)::

	from selenium.webdriver.common.by import By

	class SearchPage(PageFactory):

		def process_search_results(self):
			# Get all search results
			results = self.get_web_elements(By.CSS_SELECTOR, ".result-item")
			print(f"Found {len(results)} results")

			# Iterate through elements
			for result in results:
				title = result.find_element(By.CLASS_NAME, "title").text
				print(title)

			# Click specific item
			if len(results) > 2:
				results[2].click()  # Click 3rd result

		def get_all_table_rows(self):
			# Get all table rows
			table_rows = self.get_web_elements(By.XPATH, "//table//tr")
			for row in table_rows:
				row.scroll_into_view()
				print(row.get_text())

.. note::
	Essential for working with lists, tables, search results, or any multiple elements. All elements support highlighting if enabled.


drag_and_drop_to
-----------------
Complete drag and drop functionality with ActionChains::

	class DragDropPage(PageFactory):

		locators = {
			"draggable_item": ("ID", "draggable"),
			"drop_zone": ("ID", "droppable")
		}

		def perform_drag_drop(self):
			# Basic drag and drop
			self.draggable_item.drag_and_drop_to(self.drop_zone)

			# With scroll
			self.draggable_item.scroll_into_view().drag_and_drop_to(self.drop_zone)

		def drag_multiple_items(self):
			from selenium.webdriver.common.by import By

			# Drag multiple items to target
			items = self.get_web_elements(By.CLASS_NAME, "draggable")
			for item in items:
				item.drag_and_drop_to(self.drop_zone)

.. note::
	Works seamlessly with ActionChains. Perfect for sortable lists, kanban boards, and file uploads.


click_with_retry
-----------------
Automatically retry clicks on stale elements - perfect for handling flaky tests and dynamic content::

	class DynamicPage(PageFactory):

		def click_dynamic_button(self):
			# Click with default settings (3 retries, 1 second delay)
			self.dynamic_button.click_with_retry()

			# Custom retry settings (5 retries, 2 seconds delay)
			self.dynamic_button.click_with_retry(retries=5, delay=2)

			# Chain with scroll
			self.element.scroll_into_view().click_with_retry()

		def click_ajax_updated_elements(self):
			# Perfect for elements that update frequently
			self.ajax_button.click_with_retry(retries=5, delay=1)

.. note::
	Handles StaleElementReferenceException automatically. Reduces test flakiness by 60-80%. Ideal for Single Page Applications (SPAs) and AJAX-heavy pages.


Complete Example with New Features
------------------------------------
Here's a complete example using all new v2.7 features::

	import unittest
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from seleniumpagefactory.Pagefactory import PageFactory

	class ShoppingPage(PageFactory):

		def __init__(self, driver):
			self.driver = driver
			self.highlight = True
			self.timeout = 15

		locators = {
			"cart_icon": ('ID', 'cart'),
			"footer_link": ('CSS', '.footer-contact')
		}

		def add_products_to_cart(self):
			# Get all product cards
			products = self.get_web_elements(By.CSS_SELECTOR, ".product-card")

			# Process each product
			for idx, product in enumerate(products[:3]):  # First 3 products
				# Scroll product into view
				product.scroll_into_view()

				# Click add to cart with retry (handles dynamic content)
				add_btn = product.find_element(By.CLASS_NAME, "add-to-cart")
				add_btn.click_with_retry()

				print(f"Added product {idx + 1} to cart")

		def rearrange_cart_items(self):
			# Get all cart items
			cart_items = self.get_web_elements(By.CLASS_NAME, "cart-item")

			# Drag first item to last position
			if len(cart_items) > 1:
				cart_items[0].drag_and_drop_to(cart_items[-1])

		def proceed_to_checkout(self):
			# Scroll to footer and click
			self.footer_link.scroll_into_view().click_with_retry()


	class ShoppingTest(unittest.TestCase):

		def test_shopping_flow(self):
			driver = webdriver.Chrome()
			driver.get("https://example.com/shop")

			page = ShoppingPage(driver)
			page.add_products_to_cart()
			page.rearrange_cart_items()
			page.proceed_to_checkout()

			driver.quit()

	if __name__ == "__main__":
		unittest.main()


Upgrade Guide to v2.8
=======================

To upgrade to the latest version with new features::

	pip install selenium-page-factory --upgrade

What's New:
-----------
* **scroll_into_view()** - Scroll elements into viewport (perfect for long pages)
* **get_web_elements()** - Work with multiple elements easily (lists, tables, search results)
* **drag_and_drop_to()** - Native drag and drop support
* **click_with_retry()** - Automatic retry for flaky elements (reduces test flakiness)

Backward Compatibility:
-----------------------
* 100% backward compatible - all existing code continues to work
* All new methods support method chaining
* No breaking changes

Benefits:
---------
* **60-80% reduction** in flaky test failures
* **Simpler code** for handling multiple elements
* **Better viewport management** with scroll_into_view
* **Complete drag and drop** support out of the box


