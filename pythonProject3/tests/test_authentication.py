from pages.locators import MainPage
# Для запуска блока тестов, связанных с авторизацией, необходимы команды:
# python -m pytest -v --driver Chrome --driver-path driver/chromedriver.exe tests/test_authentication.py

def test_email_login(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("johnmcclane@gmail.com")
    page.enter.click()

    assert page.login_field

def test_blanc_login(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("             ")

    assert page.auth_problem

def test_invalid_login(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("BI81-JU55-12ER")
    page.enter.click()

    assert page.auth_problem_1