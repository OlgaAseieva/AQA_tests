# def test_check_math():
#     assert 7 * 7 == 49

# перенесли фикстуру в файл conftest.py
import pytest

# class User:

#     def __init__(self):
#         self.name = 'Olga'
#         self.second_name = 'As'


# @pytest.fixture
# def user():
#      yield Usre()

# user = User()
@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Olga'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'As'