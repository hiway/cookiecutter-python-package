import pytest

@pytest.fixture(autouse=True)
def example_of_globally_available_objects_in_doctests(doctest_namespace):
    """pytest+doctest: http://doc.pytest.org/en/latest/doctest.html"""
    doctest_namespace['doctest_namespace_demo'] = 'Set this up in conftest.py'
