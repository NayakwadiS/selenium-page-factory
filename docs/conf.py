from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

# -- Project information -------------------------

project = 'selenium-page-factory'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '2.7'

# The master toctree document.
master_doc = 'index'

html_favicon = 'new_logo.JPG'

html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('css/custom.css?v20240414')
    
