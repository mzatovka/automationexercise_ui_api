from playwright.sync_api import sync_playwright
import time
import pytest
from playwright.sync_api import expect
from fixtures import page,  new_user , create_browser


@pytest.mark.regression
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
    
    
    
# Test Case 9
def test_search_products(page):
    
    assert page.url == 'https://automationexercise.com/'
    
    page.locator('a[href="/products"]').click()

    all_products = page.locator("h2.title", has_text="All Products")
    text_all_products = all_products.inner_text()
    
    assert text_all_products == 'ALL PRODUCTS'
    
    search_product =  page.locator('#search_product')
    search_product.fill('Winter top')
    page.locator('#submit_search').click()
 
    searched_title = page.locator("h2.title", has_text="Searched Products") 
    text_searched_title = searched_title.inner_text()
    assert text_searched_title == 'SEARCHED PRODUCTS'
 
    product_title = page.locator(".productinfo p")  
    expect(product_title).to_have_text("Winter Top")    