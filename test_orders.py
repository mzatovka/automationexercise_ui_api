from playwright.sync_api import sync_playwright
import time
import pytest
from playwright.sync_api import expect
from fixtures import page, new_user , create_browser, register_user_api
    
    
def test_add_products_to_cart(page):
    
    assert page.url == 'https://automationexercise.com/'
    
    page.locator('a[href="/products"]').click()
    
    
    
    page.locator('a[data-product-id="1"]').first.click()
    page.locator("button.btn-success.close-modal").click()
    page.locator('a[data-product-id="2"]').first.click()
    page.locator("button.btn-success.close-modal").click()
    page.locator('a[href="/view_cart"]').first.click()    

    assert page.locator("tr#product-1").is_visible()
    assert page.locator("tr#product-2").is_visible()
    
    product_1 = page.locator("tr#product-1")
    expect(product_1.locator("td.cart_price")).to_contain_text("Rs. 500")
    expect(product_1.locator("td.cart_quantity button")).to_contain_text("1")
    expect(product_1.locator("td.cart_total")).to_contain_text("Rs. 500")
    
    product_2 = page.locator("tr#product-2")
    expect(product_2.locator("td.cart_price")).to_contain_text("Rs. 400")
    expect(product_2.locator("td.cart_quantity button")).to_contain_text("1")
    expect(product_2.locator("td.cart_total")).to_contain_text("Rs. 400")
    
# Test Case16
def test_login_before_chekout(new_user,page):
    
    assert page.url == 'https://automationexercise.com/'
    
    (page.locator("a[href='/login']")).click()

    page.locator('[data-qa="login-email"]').fill(new_user['email'])
    page.locator('[data-qa="login-password"]').fill(new_user['password'])
    page.locator('[data-qa="login-button"]').click()
    expect(page.get_by_text("Logged in as mariaa")).to_be_visible()    

    page.locator('a[data-product-id="1"]').first.click()
    page.locator("button.btn-success.close-modal").click()
    page.locator('a[data-product-id="2"]').first.click()
    page.locator("button.btn-success.close-modal").click()
    page.locator('a[data-product-id="3"]').first.click()
    page.locator("button.btn-success.close-modal").click()
    page.locator('a[href="/view_cart"]').first.click()    

    assert page.url == 'https://automationexercise.com/view_cart'
    
    page.locator("a.check_out").click()
    
    page.locator('textarea[name="message"]').fill("buy clothes")   
    page.locator('a[href="/payment"]').click()
    
    page.locator('[data-qa="name-on-card"]').fill("Maksim Zatouka")
    page.locator('[data-qa="card-number"]').fill("123456789")
    page.locator('[data-qa="cvc"]').fill("123")
    page.locator('[data-qa="expiry-month"]').fill("12")
    page.locator('[data-qa="expiry-year"]').fill('2200')
    page.locator('[data-qa="pay-button"]').click()
    
    expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()

    page.locator('a[href="/delete_account"]').click() 
    expect(page.get_by_text("Account Deleted!")).to_be_visible()    
    

# Test Case 18
def tests_view_category_products(page):
    
    Kids_btn = page.locator('a[href="#Kids"]')
    Men_btn = page.locator('a[href="#Men"]')
    woman_btn = page.locator('a[href="#Women"]')
  
    expect(Kids_btn).to_have_text("Kids")
    expect(Men_btn).to_have_text("Men")
    expect(woman_btn).to_have_text("Women")
    
    woman_btn.click()
    
    page.locator('a[href="/category_products/1"]').click()
    
    find_title_locator = page.locator("h2.title", has_text="Women")
    find_title_locator.wait_for(state="visible", timeout=5000)
    find_text_woman = find_title_locator.inner_text().strip()
    
    assert find_text_woman.upper() == "WOMEN - DRESS PRODUCTS"
    
    page.locator('a[href="#Men"]').click()
    page.locator(".panel-body a", has_text="Tshirts").click()
    
    find_text_man = page.locator(".title", has_text="Men").inner_text().strip()
    assert find_text_man.upper() == "MEN - TSHIRTS PRODUCTS"
