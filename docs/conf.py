# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
sys.path.append(os.path.abspath("./"))

from definitions import substitutions

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Raith_GDSII'
copyright = '2023, Aaron Hryciw'
author = 'Aaron Hryciw'
release = '1.2.x'
version = '1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_search.extension',
    'sphinx_copybutton',
    'hoverxref.extension',
    'sphinxcontrib.matlab'
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

highlight_language = 'matlab'
primary_domain = 'mat'
add_module_names = False
nitpicky = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']

rst_prolog = """
.. include:: <s5defs.txt>

.. role:: matlab(code)
    :language: matlabsession
    :class: highlight
"""
rst_epilog = substitutions

copybutton_prompt_text = ">> "

autosectionlabel_prefix_document = True

hoverx_default_type = "tooltip"
hoverxref_domains = ["py"]
hoverxref_role_types = dict.fromkeys(
    ["ref", "numref", "class", "func", "meth", "attr", "exc", "data"],
    "tooltip",
)
hoverxref_auto_ref = True

numfig = True
