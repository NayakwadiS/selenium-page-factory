# Changelog

All notable changes to selenium-page-factory will be documented in this file.

## [2.8] - 2026-06-01

### Added
- **scroll_into_view()** - Scroll elements into viewport before interaction
  - Supports both top and bottom alignment
  - Essential for elements below the fold or in scrollable containers
  - Returns self for method chaining

- **get_web_elements()** - Multiple elements support
  - Find and work with lists of elements (search results, tables, cards, etc.)
  - Returns list of WebElements with all extended methods
  - Supports highlighting for multiple elements

- **drag_and_drop_to()** - Complete drag and drop functionality
  - Drag current element to target element using ActionChains
  - Supports method chaining
  - Works seamlessly with other element methods

- **click_with_retry()** - Automatic retry mechanism for clicks
  - Handles StaleElementReferenceException automatically
  - Configurable retry count (default: 3) and delay (default: 1s)
  - Perfect for dynamic content and flaky tests
  - Returns self for method chaining

## [2.7] - Previous Release

### Features
- Page Factory pattern implementation
- Extended WebElement methods with explicit waits
- Element highlighting support
- Selenium 4 ActionChains support
- Appium/mobile testing support
- Custom Page Factory exceptions
- Comprehensive WebElement methods (click_button, set_text, hover, etc.)

## [2.9] - Plan Next Release
- Shadow DOM support (increasingly common with web components)
- Enhanced logging/screenshots on failure
- Wait for element stability (animations)
- Element caching (optimization)
- Soft assertions
- Advanced mobile gestures