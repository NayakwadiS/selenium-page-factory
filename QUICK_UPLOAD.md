# Quick Upload Commands - selenium-page-factory v2.8

## 🚀 One-Line Upload (After you have tokens configured)

```powershell
# Upload to PyPI (Production)
python -m build; twine upload dist/*

# Upload to TestPyPI (Testing)
python -m build; twine upload --repository testpypi dist/*
```

---

## 📋 Step-by-Step (First Time)

### 1. Install Tools (One Time)
```powershell
pip install --upgrade build twine
```

### 2. Get API Token (One Time)
- Go to: https://pypi.org/manage/account/token/
- Create token with name: "selenium-page-factory-upload"
- **Save the token!** (You'll only see it once)

### 3. Build Package
```powershell
cd "C:\Drive D\selenium-page-factory"
python -m build
```

### 4. Check Package (Optional but Recommended)
```powershell
twine check dist/*
```
Should output: "PASSED" for both files

### 5. Upload to TestPyPI (Recommended First)
```powershell
twine upload --repository testpypi dist/*
```
- Username: `__token__`
- Password: (paste your TestPyPI token)

### 6. Test Installation from TestPyPI
```powershell
pip install --index-url https://test.pypi.org/simple/ selenium-page-factory==2.8
```

### 7. Upload to Production PyPI
```powershell
twine upload dist/*
```
- Username: `__token__`
- Password: (paste your PyPI token)

### 8. Verify on PyPI
Visit: https://pypi.org/project/selenium-page-factory/

### 9. Test Production Installation
```powershell
pip install selenium-page-factory==2.8
```

---

## 🎯 What to Enter When Asked

```
Enter your username: __token__
Enter your password: pypi-XXXXXXXXXXXXXXXXXXXXXXX
```

**Important:** 
- Username is literally the string `__token__` (with two underscores)
- Password is your full token including the `pypi-` prefix

---

## 🔄 Next Upload (After First Time)

```powershell
# 1. Update version in files
# 2. Clean and build
Remove-Item -Recurse -Force dist, build, *.egg-info
python -m build

# 3. Upload
twine upload dist/*
```

---

## ✅ Current State

Your package is **READY TO UPLOAD**:
- ✅ Built: `dist/selenium_page_factory-2.8-py3-none-any.whl`
- ✅ Built: `dist/selenium_page_factory-2.8.tar.gz`
- ✅ Version: 2.8  
- ✅ All files consistent

**Just run:** `twine upload dist/*`

