# Quick Reference Guide - New Features v2.8

## 🚀 Quick Start

All 4 new methods are now available on every WebElement in your page objects!

---

## 📋 Method Reference

### 1️⃣ scroll_into_view(align_to_top=True)
**When to use**: Before clicking elements below the fold or in scrollable containers

```python
# Basic usage
page.footer_link.scroll_into_view()

# Align to bottom
page.element.scroll_into_view(align_to_top=False)

# Chain with other methods
page.element.scroll_into_view().click_button()
```

**Returns**: self (for chaining)

---

### 2️⃣ get_web_elements(By, locator)
**When to use**: Working with lists, tables, search results, or any multiple elements

```python
# Find all matching elements
results = page.get_web_elements(By.CSS_SELECTOR, ".product")

# Iterate and interact
for result in results:
    print(result.text)
    result.click()

# Access by index
results[0].click()  # First element
results[-1].click()  # Last element
```

**Returns**: List of WebElements with all extended methods

---

### 3️⃣ drag_and_drop_to(target_element)
**When to use**: Drag and drop operations (sortable lists, kanban boards, file uploads)

```python
# Basic drag and drop
page.draggable.drag_and_drop_to(page.drop_zone)

# With scroll
page.item.scroll_into_view().drag_and_drop_to(page.target)

# Multiple drag operations
for item in items:
    item.drag_and_drop_to(basket)
```

**Returns**: self (for chaining)

---

### 4️⃣ click_with_retry(retries=3, delay=1)
**When to use**: Dynamic content, SPAs, AJAX-heavy pages, flaky elements

```python
# Default (3 retries, 1 second delay)
page.dynamic_button.click_with_retry()

# Custom retry settings
page.element.click_with_retry(retries=5, delay=2)

# With other methods
page.element.scroll_into_view().click_with_retry()
```

**Handles**: StaleElementReferenceException automatically  
**Returns**: self (for chaining)

---

## 💡 Common Patterns

### Pattern 1: Scroll + Retry Click
```python
page.footer_button.scroll_into_view().click_with_retry()
```

### Pattern 2: Find Multiple + Process Each
```python
items = page.get_web_elements(By.CSS_SELECTOR, ".item")
for item in items:
    item.scroll_into_view()
    print(item.get_text())
```

### Pattern 3: Drag from List
```python
sources = page.get_web_elements(By.CLASS_NAME, "draggable")
target = page.drop_zone
for source in sources:
    source.drag_and_drop_to(target)
```

### Pattern 4: Retry Click on Dynamic List
```python
buttons = page.get_web_elements(By.CSS_SELECTOR, "button.dynamic")
for button in buttons:
    button.click_with_retry(retries=5)
```

---

## ⚡ Performance Tips

1. **Use click_with_retry sparingly** - Only for known flaky elements
2. **Batch scroll operations** - Scroll container once, not each element
3. **Cache get_web_elements results** - Don't repeatedly find same elements
4. **Set appropriate retry delays** - Balance speed vs. reliability

---

## 🐛 Troubleshooting

### Element not scrolling into view?
- Check if element is in iframe
- Verify element is not `display:none`
- Try `align_to_top=False` for bottom alignment

### get_web_elements returns empty list?
- Wait for page load before calling
- Check selector syntax
- Use `page.driver.implicitly_wait(10)` if needed

### Drag and drop not working?
- Ensure both elements are visible
- Try scrolling both elements into view first
- Check if ActionChains are supported (not on all browsers)

### click_with_retry still failing?
- Increase retry count and delay
- Check if element is actually clickable
- Verify element is not overlapped by another element

---

## 📊 Upgrade Checklist

- [x] Install/update package: `pip install selenium-page-factory==2.7`
- [ ] Update existing scroll code to use `scroll_into_view()`
- [ ] Replace manual element lists with `get_web_elements()`
- [ ] Add `click_with_retry()` to flaky element clicks
- [ ] Implement drag and drop features using `drag_and_drop_to()`
- [ ] Run test suite to verify compatibility
- [ ] Update team documentation

---

## 🔗 Resources

- **Full Documentation**: See `examples/new_features_example.py`
- **Test Suite**: See `tests/test_new_features.py`
- **Changelog**: See `CHANGELOG.md`
- **Implementation Details**: See `IMPLEMENTATION_SUMMARY.md`

---

## 📝 Notes

- All methods return `self` for method chaining (except get_web_elements)
- All methods respect existing `timeout` and `highlight` settings
- 100% backward compatible with v2.6
- All methods have comprehensive unit tests

---

**Version**: 2.7  
**Date**: June 1, 2026  
**Status**: Production Ready ✅

