from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

# -- Project information -------------------------

project = 'selenium-page-factory'

# The short X.Y version
version = '2.4'
# The full version, including alpha/beta/rc tags
release = '2.4'

# The master toctree document.
master_doc = 'index'

html_favicon = 'selenium-page-factory_logo.png'

html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('css/custom.css?v20211101')
    
