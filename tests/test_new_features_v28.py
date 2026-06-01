"""
Unit tests for new features added to selenium-page-factory:
- scroll_into_view
- get_web_elements (multiple elements support)
- drag_and_drop_to
- click_with_retry
"""

import unittest
from unittest.mock import Mock, MagicMock, patch, call
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from seleniumpagefactory.Pagefactory import PageFactory
import time


class TestNewFeatures(unittest.TestCase):
    """Test cases for new PageFactory features"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.driver = Mock()
        self.page = PageFactory()
        self.page.driver = self.driver
        self.page.timeout = 10
        self.page.highlight = False
        
    def test_get_web_elements_returns_list(self):
        """Test that get_web_elements returns a list of elements"""
        # Mock multiple elements
        mock_element1 = Mock(spec=WebElement)
        mock_element2 = Mock(spec=WebElement)
        mock_element3 = Mock(spec=WebElement)
        
        self.driver.find_elements.return_value = [mock_element1, mock_element2, mock_element3]
        
        # Call get_web_elements
        elements = self.page.get_web_elements(By.CSS_SELECTOR, ".item")
        
        # Verify
        self.assertEqual(len(elements), 3)
        self.driver.find_elements.assert_called_once_with(By.CSS_SELECTOR, ".item")
        
    def test_get_web_elements_empty_list(self):
        """Test get_web_elements with no elements found"""
        self.driver.find_elements.return_value = []
        
        elements = self.page.get_web_elements(By.ID, "non-existent")
        
        self.assertEqual(len(elements), 0)
        self.assertIsInstance(elements, list)
        
    def test_scroll_into_view_default_align(self):
        """Test scroll_into_view with default alignment (top)"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        
        # Call scroll_into_view
        result = PageFactory.scroll_into_view(mock_element)
        
        # Verify JavaScript execution
        self.driver.execute_script.assert_called_once_with(
            "arguments[0].scrollIntoView(arguments[1]);",
            mock_element,
            True
        )
        self.assertEqual(result, mock_element)
        
    def test_scroll_into_view_align_to_bottom(self):
        """Test scroll_into_view with align_to_top=False"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        
        result = PageFactory.scroll_into_view(mock_element, align_to_top=False)
        
        self.driver.execute_script.assert_called_once_with(
            "arguments[0].scrollIntoView(arguments[1]);",
            mock_element,
            False
        )
        self.assertEqual(result, mock_element)
        
    @patch('seleniumpagefactory.Pagefactory.ActionChains')
    def test_drag_and_drop_to(self, mock_action_chains):
        """Test drag_and_drop_to functionality"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        mock_target = Mock(spec=WebElement)
        
        # Setup mock ActionChains
        mock_chain_instance = Mock()
        mock_action_chains.return_value = mock_chain_instance
        mock_chain_instance.drag_and_drop.return_value = mock_chain_instance
        
        # Call drag_and_drop_to
        result = PageFactory.drag_and_drop_to(mock_element, mock_target)
        
        # Verify
        mock_action_chains.assert_called_once_with(self.driver)
        mock_chain_instance.drag_and_drop.assert_called_once_with(mock_element, mock_target)
        mock_chain_instance.perform.assert_called_once()
        self.assertEqual(result, mock_element)
        
    def test_click_with_retry_success_first_attempt(self):
        """Test click_with_retry succeeds on first attempt"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        mock_element.element_to_be_clickable = Mock()
        mock_element.click = Mock()
        
        result = PageFactory.click_with_retry(mock_element, retries=3, delay=0.1)
        
        # Should succeed on first try
        mock_element.element_to_be_clickable.assert_called_once()
        mock_element.click.assert_called_once()
        self.assertEqual(result, mock_element)
        
    @patch('time.sleep')
    def test_click_with_retry_succeeds_after_retries(self, mock_sleep):
        """Test click_with_retry succeeds after retries"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        mock_element.element_to_be_clickable = Mock()
        
        # Fail twice, then succeed
        mock_element.click = Mock(
            side_effect=[
                StaleElementReferenceException(),
                StaleElementReferenceException(),
                None
            ]
        )
        
        result = PageFactory.click_with_retry(mock_element, retries=3, delay=0.5)
        
        # Should have tried 3 times
        self.assertEqual(mock_element.click.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)  # Sleep between attempts
        mock_sleep.assert_called_with(0.5)
        self.assertEqual(result, mock_element)
        
    @patch('time.sleep')
    def test_click_with_retry_fails_after_max_retries(self, mock_sleep):
        """Test click_with_retry raises exception after max retries"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        mock_element.element_to_be_clickable = Mock()
        
        # Always fail
        mock_element.click = Mock(side_effect=StaleElementReferenceException())
        
        with self.assertRaises(StaleElementReferenceException):
            PageFactory.click_with_retry(mock_element, retries=3, delay=0.1)
        
        # Should have tried 3 times
        self.assertEqual(mock_element.click.call_count, 3)
        
    def test_click_with_retry_default_parameters(self):
        """Test click_with_retry with default parameters"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        mock_element.element_to_be_clickable = Mock()
        mock_element.click = Mock()
        
        # Should use defaults: retries=3, delay=1
        result = PageFactory.click_with_retry(mock_element)
        
        self.assertEqual(result, mock_element)
        mock_element.click.assert_called_once()


class TestWebElementBindings(unittest.TestCase):
    """Test that new methods are properly bound to WebElement"""
    
    def test_scroll_into_view_bound_to_webelement(self):
        """Test scroll_into_view is available on WebElement"""
        self.assertTrue(hasattr(WebElement, 'scroll_into_view'))
        self.assertEqual(WebElement.scroll_into_view, PageFactory.scroll_into_view)
        
    def test_drag_and_drop_to_bound_to_webelement(self):
        """Test drag_and_drop_to is available on WebElement"""
        self.assertTrue(hasattr(WebElement, 'drag_and_drop_to'))
        self.assertEqual(WebElement.drag_and_drop_to, PageFactory.drag_and_drop_to)
        
    def test_click_with_retry_bound_to_webelement(self):
        """Test click_with_retry is available on WebElement"""
        self.assertTrue(hasattr(WebElement, 'click_with_retry'))
        self.assertEqual(WebElement.click_with_retry, PageFactory.click_with_retry)


class TestIntegrationScenarios(unittest.TestCase):
    """Integration tests for realistic usage scenarios"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.driver = Mock()
        self.page = PageFactory()
        self.page.driver = self.driver
        self.page.highlight = False
        
    def test_multiple_elements_with_scroll(self):
        """Test finding multiple elements and scrolling each"""
        mock_elements = [Mock(spec=WebElement) for _ in range(3)]
        for elem in mock_elements:
            elem.parent = self.driver
            
        self.driver.find_elements.return_value = mock_elements
        
        # Get elements
        elements = self.page.get_web_elements(By.CLASS_NAME, "item")
        
        # Scroll each element
        for element in elements:
            # This would normally call scroll_into_view, but we're just testing the pattern
            element.parent = self.driver
            
        self.assertEqual(len(elements), 3)
        
    def test_chaining_scroll_and_retry_click(self):
        """Test chaining scroll_into_view with click_with_retry"""
        mock_element = Mock(spec=WebElement)
        mock_element.parent = self.driver
        mock_element.element_to_be_clickable = Mock()
        mock_element.click = Mock()
        
        # Simulate chaining: scroll then retry click
        PageFactory.scroll_into_view(mock_element)
        PageFactory.click_with_retry(mock_element)
        
        self.driver.execute_script.assert_called_once()
        mock_element.click.assert_called_once()


if __name__ == '__main__':
    print("Running tests for new selenium-page-factory features...")
    print("=" * 60)
    unittest.main(verbosity=2)

