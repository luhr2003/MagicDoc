import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

__version__ = "0.1.0"

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MagicDoc'
copyright = '2025, MAGICS Lab'
author = 'MAGICS Lab'
release = __version__
version = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_subfigure",
    "sphinxcontrib.video",
    "sphinx_togglebutton",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinx_new_tab_link",  # open external link in new tab, see https://github.com/ftnext/sphinx-new-tab-link
]

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = ["colon_fence", "dollarmath", "tasklist"]
# https://github.com/executablebooks/MyST-Parser/issues/519#issuecomment-1037239655
myst_heading_anchors = 4

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_logo = "_static/archer.svg"
html_favicon = "_static/archer.svg"

json_url = "_static/version_switcher.json"
version_match = os.environ.get("READTHEDOCS_VERSION")
html_theme_options = {
    "show_nav_level": 1,
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/MagicSimOrg/MagicSim",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Website",
            "url": "https://magicsimorg.github.io/",
            "icon": "fa-solid fa-globe",
        },
    ],
    "logo": {
        "image_dark": "_static/archer.svg",
    },
    "navbar_center": ["version-switcher", "navbar-nav"],
    "show_version_warning_banner": False,
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    "sidebarwidth": "150px",
}

html_context = {
    "display_github": True,
    "github_user": "MagicSimOrg",
    "github_repo": "MagicSim",
    "github_version": "main",
    "conf_py_path": "docs/source",
    "doc_path": "docs/source",
}
html_css_files = [
    # "css/custom.css",
]
html_show_copyright = True
html_show_sphinx = False
html_static_path = ["_static"]

### Autodoc configurations ###
autoclass_content = "class"
autodoc_typehints = "signature"
autodoc_class_signature = "separated"
autodoc_default_options = {
    "autosummary": True,
    "exclude-members": "__init__",
}
autodoc_inherit_docstrings = True
autodoc_member_order = "bysource"
autosummary_generate = True  # automatically generate rst files when there are no ones
autosummary_generate_overwrite = False  # do not overwrite existing rst files

########################################################
## Skip members from autodoc
########################################################


def skip_member(app, what, name, obj, skip, options):
    # List the names of the functions you want to skip here
    exclusions = ["from_dict", "to_dict", "replace", "copy", "validate", "__post_init__"]
    if name in exclusions:
        return True
    return None


def generate_task_markdown(app):
    script_path = os.path.join(app.srcdir, "dataset_benchmark", "tasks", "generate_task_docs.py")
    if not os.path.exists(script_path):
        # print(f"[Sphinx] ❌ generate_task_docs.py not found at {script_path}")
        return

    # print(f"[Sphinx] 🛠 Generating task markdown pages with: {script_path}")
    result = subprocess.run(
        [sys.executable, script_path], cwd=os.path.dirname(script_path), capture_output=True, text=True, check=False
    )


def setup(app):
    app.connect("autodoc-skip-member", skip_member)
    app.connect("builder-inited", generate_task_markdown)