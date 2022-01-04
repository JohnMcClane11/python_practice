from pages.locators import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск данного блока тестов осуществляется путем команд:
# python -m pytest -v --driver Chrome --driver-path driver/chromedriver.exe tests/test_search.py

def test_search_with_success(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Фэнтези')
    page.search_btn.click()

    assert page.search_success




def test_search_in_eng(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Fantasy')
    page.search_btn.click()

    assert page.search_success


def test_search_with_numbers(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('4357')
    page.search_btn.click()

    assert page.search_success



def test_blanc_search(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('               ')
    page.search_btn.click()

    assert page.search_without_success


def test_random_symbols(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys(')(&*%^%$')
    page.search_btn.click()

    assert page.search_without_success



def test_only_available(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Сборник Толкиен')
    page.search_btn.click()
    page.all_filers.click()
    page.reset_all_filers.click()
    page.available.click()
    page.show_all_found.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@class="btn buy-link btn-primary"]'))
    )

    assert element


def test_only_not_available(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Сборник Толкиен')
    page.search_btn.click()
    page.all_filers.click()
    page.reset_all_filers.click()
    page.not_available.click()
    page.show_all_found.click()

    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//span[text()="Нет в продаже"]'))
    )

    assert element