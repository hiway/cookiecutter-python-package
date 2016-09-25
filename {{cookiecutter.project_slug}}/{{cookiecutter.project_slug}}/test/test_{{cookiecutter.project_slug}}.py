# import pytest
import {{cookiecutter.project_slug}}


def test_{{cookiecutter.project_slug}}_version():
    assert {{cookiecutter.project_slug}}.version() == '{{cookiecutter.version}}'


def test_{{cookiecutter.project_slug}}_url():
    assert {{cookiecutter.project_slug}}.url() == '{{cookiecutter.project_url}}'
