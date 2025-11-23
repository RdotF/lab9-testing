import requests
import pytest
BASE_URL = "https://reqres.in/api"
HEADERS = {
 "x-api-key": "reqres-free-v1"
}
def test_get_user():
 response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
 assert response.status_code == 200
 json_data = response.json()
 assert 'data' in json_data
 assert json_data['data']['id'] == 2
 assert json_data['data']['first_name'] == 'Janet'
def test_create_user():
 payload = {"name": "morpheus", "job": "leader"}
 response = requests.post(f"{BASE_URL}/users", json=payload,
headers=HEADERS)
 assert response.status_code == 201
 json_data = response.json()
 assert json_data['name'] == payload['name']
 assert json_data['job'] == payload['job']
def test_update_user():
 payload = {"name": "morpheus", "job": "zion resident"}
 response = requests.put(f"{BASE_URL}/users/2", json=payload,
headers=HEADERS)
 assert response.status_code == 200
 json_data = response.json()
 assert json_data['job'] == 'zion resident'
if __name__ == "__main__":
 pytest.main()