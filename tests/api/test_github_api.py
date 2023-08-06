import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')

    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('romanpasternakwrong')
    
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    
    assert r['total_count'] == 43
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('roman_repo_non_exist')
    
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')

    assert r['total_count'] != 0

@pytest.mark.api
def test_check_number_commits(github_api):
    r = github_api.get_commits('RomanPasternak19', 'automation-cypress-test-allo')
    
    assert len(r) == 4

@pytest.mark.api
def test_check_commit_messege(github_api):
    r = github_api.get_commits('RomanPasternak19', 'automation-cypress-test-allo')
    
    assert r[0]['commit']['message'] == "Update .gitignore"

@pytest.mark.api
def test_check_commit_author_name(github_api):
    r = github_api.get_commits('RomanPasternak19', 'automation-cypress-test-allo')
    
    assert r[0]['commit']['author']['name'] == "Roman Pasternak"

@pytest.mark.api
def test_emojis_count(github_api):
    r = github_api.get_emojis()
    
    assert len(r) > 0