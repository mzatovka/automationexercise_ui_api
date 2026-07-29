from playwright.sync_api import sync_playwright
import time
import pytest
import requests

@pytest.fixture(scope="session")
def create_browser():
    with sync_playwright() as driver:
        browser = driver.chromium.launch(headless=False) # headless=False говорит об открытии браузера , если будет true браузер не откроется, все будет проходить в фоновом режиме 
        
        yield browser 
        
        browser.close()
        
@pytest.fixture()
def page(create_browser):
    new_page = create_browser.new_page()
    new_page.goto("https://automationexercise.com/")
    
    yield new_page
    
    new_page.close()
    

@pytest.fixture()
def new_user(create_browser):
    
    page = create_browser.new_page()
    page.goto("https://automationexercise.com/")
    page_login_btn = page.locator("//a[text()=' Signup / Login']")
    page_login_btn.click()

    time.sleep(3)
    
    new_email = f"test{time.time()}@gmail.com"
    
    page.locator("[data-qa='signup-name']").fill('mariaa')        
    page.locator("[data-qa='signup-email']").fill(new_email)
    
    signup_btn = page.locator("[data-qa='signup-button']")
    signup_btn.click()

    time.sleep(3)
    # метод для радио кнопок
    page.locator("#id_gender1").check()

    time.sleep(3)

    enter_password = page.locator('#password')
    enter_password.fill('password1234')
    
    # select option - работа с выпадающим списком 
    page.locator('#days').select_option('4')
    page.locator('#months').select_option('June')
    page.locator('#years').select_option('1996')
    
    page.get_by_label("Sign up for our newsletter!").check()
    
    page.locator('#first_name').fill('max')
    page.locator('#last_name').fill('zatovka')
    page.locator('[data-qa = "company"]').fill('freelance')
    page.locator('[data-qa = "address"]').fill('Grodno')
    page.locator('#country').select_option('United States')
    page.locator('[data-qa = "state"]').fill('Grodno')
    page.locator('[data-qa = "city"]').fill('Grodno')
    page.locator('[data-qa = "zipcode"]').fill('zipcode')
    page.locator('[data-qa = "mobile_number" ]').fill('375336200282')
    
    page.locator('[data-qa = "create-account"]').click()

    return{
        
        'email': new_email,
        'password': 'password1234'
        
    }
    
    
@pytest.fixture
def register_user_api():
    
    base_url = 'https://automationexercise.com/api/createAccount'
    
    data_for_user = {
        "name": "Test User",
        "email": "aqa_test_user_02@example.com",
        "password": "Passw0rd!",
        "title": "Mr",
        "birth_date": "10", "birth_month": "5", "birth_year": "1995",
        "firstname": "Test", "lastname": "User",
        "company": "QA School", "address1": "Test street 1",
        "address2": "", "country": "United States",
        "zipcode": "10001", "state": "NY", "city": "New York",
        "mobile_number": "1234567890",
    }
      
    response = requests.post(
        
        base_url,
        data = data_for_user
        
    )
    
    print(response.status_code)
    
    yield data_for_user
    
    data = {
        
        'email' : data_for_user['email'],
        'password' : data_for_user['password']
    }
    
    delete_response = requests.delete(
        
        'https://automationexercise.com/api/deleteAccount',
        data = data
        
    )
    
    print(delete_response.status_code)