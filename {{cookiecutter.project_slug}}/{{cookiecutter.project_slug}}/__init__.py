"""
{{cookiecutter.project_slug}}

{{cookiecutter.project_description}}

Documentation of the package begins here
Use doctests to demonstrate usage

>>> import {{cookiecutter.project_slug}}
>>> {{cookiecutter.project_slug}}.version()
'{{cookiecutter.version}}'

You can also supply objects that are available in doctests in `conftest.py`:

>>> 'Set this up in conftest.py' == doctest_namespace_demo
True
"""

__project_name__ = '{{cookiecutter.project_slug}}'
__version__ = '{{cookiecutter.version}}'
__url__ = '{{cookiecutter.project_url}}'
__author__ = '{{cookiecutter.author}}'
__author_email__ = '{{cookiecutter.email}}'
__description__ = '{{cookiecutter.project_description}}'


def version():
    return __version__


def url():
    return __url__
