from pages.locators import MainPage
# Запуск данного блока тестов осуществляется путем команд:
# python -m pytest -v --driver Chrome --driver-path driver/chromedriver.exe tests/test_prod_page.py

def test_add_book_to_differ(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.compare.click()

    assert page.compared_success

def test_different_books(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.compare.click()
    page.logo.click()
    page.best_sale.click()
    page.random_book_1.click()
    page.compare.click()
    page.compare_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/compare/'

def test_ready_to_buy_book(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()

    assert page.bought_success

def test_wait_to_buy(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.add_to_deferred.click()
    page.deferred.click()

    assert page.ready_to_be_bought