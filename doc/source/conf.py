# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import mariadb
from typing import Sequence
from datetime import datetime
print(mariadb.__path__)
sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)


# -- Project information -----------------------------------------------------

project = 'MariaDB Connector/Python'
copyright = '2019-%s MariaDB Corporation and Georg Richter' % datetime.now().year
author = 'Georg Richter'

# The full version, including alpha/beta/rc tags
release = mariadb.__version__
if len(mariadb.__version_info__) > 3:
    release= release + "-" + mariadb.__version_info__[3]
add_module_names= False


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.doctest', 'sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'recommonmark',
              'sphinx.ext.extlinks', 'sphinx_toolbox.collapse' ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

pygments_style = 'sphinx'

master_doc = 'index'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_show_sourcelink = False

highlight_language = 'python'

rst_epilog="""
.. |MCP| replace:: MariaDB Connector/Python
.. |MCC| replace:: MariaDB Connector/C
.. |MCC_minversion| replace:: 3.2.4
.. |DBAPI| replace:: DB API 2.0 (:PEP:`249`)
.. |MCDP| replace:: `MariaDB Connector Download page <https://mariadb.com/downloads/connectors/>`__
"""

extlinks= {
           'conpy' : ('https://jira.mariadb.org/browse/CONPY-%s', 'CONPY-%s'),
           'PEP'   : ('https://peps.python.org/pep-%s', 'PEP-%s')
          }
