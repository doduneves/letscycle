import requests
import json
import pytest

from django.urls import reverse


pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestRoutes:
    pytestmark = pytest.mark.django_db
    api_url = 'http://localhost'
    application_port = 8044


    def test_list_routes_returns_200(self):
        response = requests.get(
            f'{self.api_url}:{self.application_port}' + reverse('route-list'),
            headers={'Accept': 'application/json'}
        )

        assert response.status_code == 200


    def test_post_new_route(self):
        new_route_data = {
            "name": "Uyuni",
            "level": 1,
            "creator": 1
        }

        response = requests.post(
            f'{self.api_url}:{self.application_port}' + reverse('route-list'),
            data=new_route_data,
            headers={'Accept': 'application/json'}
        )

        assert response.status_code == 201
        if response.status_code == 201:
            pytest.route_id = response.json().get('id')


    def test_post_new_route(self):
        new_route_data = {
            "name": "Uyuni",
            "level": 1,
            "creator": 1
        }

        response = requests.post(
            f'{self.api_url}:{self.application_port}' + reverse('route-list'),
            data=new_route_data,
            headers={'Accept': 'application/json'}
        )

        assert response.status_code == 201
        if response.status_code == 201:
            pytest.route_id = response.json().get('id')


    def test_routes_has_keys(self):
        routes_response_keys = [
            'id', 'name', 'display_level',
            'level', 'average_rating', 'created_at',
            'creator', 'creator_name',
            'coordinates', 'ratings', 'comments'
        ]

        response = requests.get(
            f'{self.api_url}:{self.application_port}' + reverse('route-detail',
            args=[1]),
            headers={'Accept': 'application/json'}
        )

        assert response.headers["Content-Type"] == "application/json"
        for k in response.json().keys():
            assert k in routes_response_keys


    def test_update_posted_route(self):
        new_data = {'level': 2}

        response = requests.patch(
            f'{self.api_url}:{self.application_port}' + reverse('route-detail', args=[pytest.route_id]),
            data=new_data,
            headers={'Accept': 'application/json'}
        )

        assert response.status_code == 200


    def test_delete_posted_data(self):
        response = requests.delete(
            f'{self.api_url}:{self.application_port}' + reverse('route-detail', args=[pytest.route_id]),
            headers={'Accept': 'application/json'}
        )

        assert response.status_code == 204
