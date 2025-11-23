import pytest
import requests

class TestAPI:
    
    @pytest.mark.api
    def test_api_status(self):
        """Тест статуса API"""
        response = requests.get('https://httpbin.org/status/200')
        assert response.status_code == 200
    
    @pytest.mark.api
    def test_api_json(self):
        """Тест JSON ответа"""
        response = requests.get('https://httpbin.org/json')
        assert response.status_code == 200
        data = response.json()
        assert 'slideshow' in data