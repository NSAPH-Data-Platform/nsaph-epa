# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

sys.path.insert(0, os.path.abspath('../src/python'))
sys.path.insert(0, os.path.abspath('../../nsaph-core-platform/src/python'))

add_module_names = False
autoclass_content = 'both'
autodoc_member_order = 'bysource'

# -- Project information -----------------------------------------------------

project = 'NSAPH EPA Pipelines'
copyright = '2021, Harvard University'
author = 'Michael A Bouzinier'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'sphinx_paramlinks',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]
myst_heading_anchors = 5

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.nsaph', 'notes']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.cwl': 'cwl',
}


intersphinx_mapping = {
    'platform-docs': ('../../nsaph-platform-docs/docs', None),
}