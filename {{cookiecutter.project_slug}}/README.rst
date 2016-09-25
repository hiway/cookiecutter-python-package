{% set is_open_source = cookiecutter.license != 'None' -%}
===============================
{{ cookiecutter.project_name }}
===============================

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates


{{ cookiecutter.project_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `hiway/cookiecutter-python-package`_ project template, which borrows code from `audreyr/cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`hiway/cookiecutter-python-package`: https://github.com/hiway/cookiecutter-python-package
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
