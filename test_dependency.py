import pytest


@pytest.mark.dependency() # слово dependency говорит о том что остальные тесты зависят от данного теста
@pytest.mark.critical()
def test_login_profile():
    assert True

@pytest.mark.regression()
def test_password_min_len():
    assert True
    
@pytest.mark.dependency(depends = ['test_login_profile'])   # depends указывает от какого теста зависит этот тест
def test_view_profile():
    assert True 

    
@pytest.mark.dependency(depends = ['test_login_profile'])    # depends указывает от какого теста зависит этот тест     
def test_edit_profile():
    assert True
    
    

# pytest test_dependency.py -m critical
# pytest test_dependency.py -m 'not regression'
# pytest test_dependency.py -m "critical or regression"