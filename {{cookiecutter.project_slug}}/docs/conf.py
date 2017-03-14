#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# {{ cookiecutter.project_slug }} documentation build configuration file

import alabaster

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'alabaster'
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# general project information
project = '{{ cookiecutter.project_name }}'
copyright = '{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}'
#version = {{ cookiecutter.project_slug }}.__version__
#release = {{ cookiecutter.project_slug }}.__version__

# styles
pygments_style = 'sphinx'
highlight_language = 'python3'

# The theme to use for HTML and HTML Help pages.
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]

html_theme_options = {
    'description': '{{ cookiecutter.project_short_description }}',
    'github_user': '{{ cookiecutter.github_username }}',
    'github_repo': '{{ cookiecutter.project_slug }}',
    'github_button': True,
    'github_type': 'star',
    'github_banner': True,
    'shield_list': [
        {
            'image': 'https://img.shields.io/circleci/project/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg',
            'target': 'https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}'
        },
        {
            'image': 'https://img.shields.io/codecov/c/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg',
            'target': 'https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}'
        },
        {
            'image': 'https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg',
            'target': 'https://pypi.org/project/{{ cookiecutter.project_slug }}/'
        }
    ]
}
