from setuptools import setup
import sys

import {{cookiecutter.project_slug}}

requires = [
    # Following are handled in tox.ini
    # 'pytest', 
    # 'pytest-cov', 
    # 'sphinx'
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License',
    'Mozilla Public License 2.0': 'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
} %}

setup(
    name = "{{cookiecutter.project_name}}",
    version = {{cookiecutter.project_slug}}.__version__,
    url = {{cookiecutter.project_slug}}.__url__,
    author = {{cookiecutter.project_slug}}.__author__,
    author_email = {{cookiecutter.project_slug}}.__author_email__,
    description = {{cookiecutter.project_slug}}.__description__,
    packages = ['{{cookiecutter.project_slug}}'],
    include_package_data = True,
    install_requires = requires, 
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        {%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',{%- endif %}
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    
)
