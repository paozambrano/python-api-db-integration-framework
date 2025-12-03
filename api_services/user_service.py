import requests
from config.config import Config

class UserService:
    def __init__(self):
        self.base_url = Config.API_BASE_URL

    def create_user(self, payload: dict):
        url = f'{self.base_url}/users'
        response = requests.post(url, json=payload, timeout=Config.TIMEOUT_SECONDS)
        return response
    
    def get_user_by_id(self, user_id: int):
        url = f'{self.base_url}/users/{user_id}'
        response = requests.get(url, timeout=Config.TIMEOUT_SECONDS)
        return response