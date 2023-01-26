import pytest

# class User:

#     def __init__(self):
#         self.name = None
#         self.second_name = None


#     def create (self):
#         self.name = 'Olga'
#         self.second_name = 'As'

#     def remove(self):
#         self.name = ''
#         self.second_name = ''

# @pytest.fixture
# def user():
#     user = User()
#     user.create()

#     yield user
#     user.remove()
@pytest.mark.check
def test_change_name():
    assert user.name == 'Olga'

@pytest.mark.check
def test_change_second_name():
    assert user.second_name == 'As'

# def test_change_name():
#     user = User()
#     user.create()

#     assert user.name == 'Olga'
#     user.remove()

# def test_change_second_name():
#     user = User()
#     user.create()

#     assert user.second_name == 'As'
#     user.remove()