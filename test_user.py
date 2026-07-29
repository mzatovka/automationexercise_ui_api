from playwright.sync_api import sync_playwright
import time
import pytest
from playwright.sync_api import expect
from fixtures import page, new_user , create_browser, register_user_api
    
    
#@pytest.mark.dependency()
@pytest.mark.critical
#TESTCASE_1
def register_user(page):
    
    assert page.title() == 'Automation Exercise'
    
    page_login_btn = page.locator("//a[text()=' Signup / Login']")
    page_login_btn.click()

    enter_name = page.locator("[data-qa='signup-name']")
    enter_name.fill('mariaa')        
    
    enter_email = page.locator("[data-qa='signup-email']")
    current_time = time.time()
    enter_email.fill(f'mariaa{current_time}@gmail.com')
    
    signup_btn = page.locator("[data-qa='signup-button']")
    signup_btn.click()

    # метод для радио кнопок
    page.locator("#id_gender1").check()

    enter_password = page.locator('#password')
    enter_password.fill('maksim')
    
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
    
    success_message = page.get_by_text('Account Created!').inner_text()
    assert success_message == 'ACCOUNT CREATED!'
    
    page.get_by_text('Continue').click()
    
    page.locator("a[href='/delete_account']").click()
    delete_message = page.locator('b').inner_text()
    
    assert delete_message.strip().lower() == 'account deleted!'

# вход в аккаунт
#@pytest.mark.dependency(depends=['test_case1'])
@pytest.mark.critical
#вход в аккаунт
#TEST_CASE 2
def test_login(register_user_api,page):   

    page_login_btn = page.locator("//a[text()=' Signup / Login']")
    page_login_btn.click()
    
    page.locator('[data-qa="login-email"]').fill(register_user_api['email'])
    page.locator('[data-qa="login-password"]').fill(register_user_api['password'])
    page.locator('[data-qa="login-button"]').click()
    
    #page.wait_for_url("https://automationexercise.com/")
    
    current_url = page.url
    assert current_url == 'https://automationexercise.com/'
    
    user_status = page.locator('text= Logout')
    assert user_status.is_visible()
    
    page.locator('a[href="/logout"]').click()    
    assert page.url == 'https://automationexercise.com/login'
            
#        
def test_incorrect_password_or_email(page):
    
    page_login_btn = page.locator("//a[text()=' Signup / Login']")
    page_login_btn.click()   
    page.locator('[data-qa="login-email"]').fill('zatvka@gmail.com')
    page.locator('[data-qa="login-password"]').fill('maks')
    page.locator('[data-qa="login-button"]').click()
    
    user_status = page.locator('text= Your email or password is incorrect!')
    assert user_status.is_visible()
        
# TESTCASE 4 
#@pytest.mark.dependency(depends=['test_case1'])
@pytest.mark.regession
def log_out(register_user_api,page):
       
    assert page.url == "https://automationexercise.com/"
    
    (page.locator("a[href='/login']")).click()
    
    expect(page.get_by_text("Login to your account")).to_be_visible()
    
    page.locator('[data-qa="login-email"]').fill(register_user_api['email'])
    page.locator('[data-qa="login-password"]').fill(register_user_api['password'])
    page.locator('[data-qa="login-button"]').click()
    
    expect(page.get_by_text("Logged in as maria")).to_be_visible()    
       
    time.sleep(3)
    page.locator('a[href="/logout"]').click()
    assert page.url == 'https://automationexercise.com/login'
    
    
    
