import pytest
import requests

class TestAPI:
    
    def test_api_status(self):
        """Тест статуса API"""
        response = requests.get('https://httpbin.org/status/200')
        assert response.status_code == 200
    
    def test_api_json(self):
        """Тест JSON ответа"""
        response = requests.get('https://httpbin.org/json')
        assert response.status_code == 200
        data = response.json()
        assert 'slideshow' in data

class TestUI:
    
    def test_ui_elements(self):
        """Пример UI теста"""
        # Здесь будет код Selenium тестов
        assert True
    
    @pytest.mark.slow
    def test_slow_operation(self):
        """Медленный тест"""
        import time
        time.sleep(2)
        assert True