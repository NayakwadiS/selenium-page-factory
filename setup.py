from setuptools import setup, Extension ,find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="selenium-page-factory",
    version="2.1",
    author = "Sujit Nayakwadi",
    author_email="nayakwadi.sujit@gmail.com",
    description="Python library provides page factory approach to implement page object model in selenium",
    license="MIT",
    keywords="selenium, page object model, pom, pages, page factory",
    install_requires=['selenium'],
    url="https://github.com/NayakwadiS/selenium-page-factory",
    packages=find_packages(),
    long_description = long_description,
    long_description_content_type='text/markdown',
    tests_require=["pytest"],
)
