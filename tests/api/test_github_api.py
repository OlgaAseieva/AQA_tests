import pytest
# from moduls.api.clients.github import GitHub


# @pytest.mark.api
# def test_user_exists():
#     api = GitHub()
#     user = api.get_user_defunkt()
#     assert user['login'] == 'defunkt'

# @pytest.mark.api
# def test_not_user_exists():
#     api = GitHub()
#     r = api.get_non_exist_user()
#     #print(r)
#     assert r['message'] == 'Not Found'

# modifing tests after class optimizing
# @pytest.mark.api
# def test_user_exists():
#     api = GitHub()
#     user = api.get_user('defunkt')
#     assert user['login'] == 'defunkt'

# @pytest.mark.api
# def test_not_user_exists():
#     api = GitHub()
#     r = api.get_user('olgaas')
#     #print(r)
#     assert r['message'] == 'Not Found'

# 3 after ficture creation:

@pytest.mark.api
def test_user_exists(github_api):
    # api = GitHub()
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_not_user_exists(github_api):
    # api = GitHub()
    r = github_api.get_user('olgaas')
    #print(r)
    assert r['message'] == 'Not Found'

# Github repo searching by  reponame 

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    #print(r)
    assert r['total_count'] == 27
    assert 'become-qa-auto' in r['items'][0]['name'] == 13

@pytest.mark.api
def test_repo_can_not_be_found(github_api):
    r = github_api.search_repo('aso_not_existing_repo')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_found(github_api):
    r = github_api.search_repo('a')
    assert r['total_count'] != 0
 