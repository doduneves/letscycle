import requests
import json
from django.urls import reverse
from jsonschema import validate
from jsonschema import Draft6Validator

def test_get_employee_details_check_status_code_equals_200():
    response = requests.get("http://localhost:8000" + reverse('route-list'), headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == 200
