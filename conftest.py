import pytest
from moduls.api.clients.github import GitHub

class User:

    def __init__(self):
        self.name = None
        self.second_name = None


    def create (self):
        self.name = 'Olga'
        self.second_name = 'As'

    def remove(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user
    user.remove()

@pytest.fixture
def github_api():
    api = GitHub()
    yield api 
