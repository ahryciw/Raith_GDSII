# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Raith_GDSII'
copyright = '2023, Aaron Hryciw'
author = 'Aaron Hryciw'
release = '1.2.x'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_search.extension',
    'sphinx_copybutton',
    'hoverxref.extension',
    'sphinxcontrib.matlab'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

highlight_language = 'matlab'
primary_domain = 'mat'
add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

rst_prolog = """
.. role:: matlab(code)
    :language: matlabsession
    :class: highlight
"""

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
