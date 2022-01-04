from pages.locators import MainPage
# Необходимые команды для тестирования корзины:
# python -m pytest -v --driver Chrome --driver-path driver/chromedriver.exe tests/test_basket.py

def test_book_to_purchase(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.btn_ok_close.click()

    assert page.for_purchase_success



def test_more_books_to_be_purchased(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.btn_ok_close.click()
    page.plus_one_more.click()

    assert page.two_books_to_purchase


def test_delete_book_from_list(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.btn_ok_close.click()
    page.remove_from_cart.click()

    assert page.no_books