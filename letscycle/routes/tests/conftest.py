import pytest

def route_id_plugin():
    return None

def pytest_configure():
    pytest.route_id = route_id_plugin()