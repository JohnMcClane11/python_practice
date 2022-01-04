from pages.locators import MainPage
from selenium.webdriver import ActionChains

# Команды для запуска тестов главной страницы сайта:
# python -m pytest -v --driver Chrome --driver-path driver/chromedriver.exe tests/test_main_page.py

def test_logo(web_browser):
    page = MainPage(web_browser)
    page.logo.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


def test_sale(web_browser):
    page = MainPage(web_browser)
    page.winter_sale.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/wintersale/'


def test_mesages(web_browser):
    page = MainPage(web_browser)
    page.mesages.click()

    assert page.log_in


def test_labirint(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()

    assert page.log_in


def test_deferred(web_browser):
    page = MainPage(web_browser)
    page.deferred.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_basket(web_browser):
    page = MainPage(web_browser)
    page.cart.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


def test_age_limits(web_browser):
    page = MainPage(web_browser)
    page.plus_18.click()

    assert page.get_current_url() == 'https://www.labirint.ru/agreement/'


def test_header_books(web_browser):
    page = MainPage(web_browser)
    page.header_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/books/'


def test_main_book_2021(web_browser):
    page = MainPage(web_browser)
    page.header_main_2021.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/'


def test_header_school(web_browser):
    page = MainPage(web_browser)
    page.header_school.click()

    assert page.get_current_url() == 'https://www.labirint.ru/school/'


def test_header_toys(web_browser):
    page = MainPage(web_browser)
    page.header_toys.click()

    assert page.get_current_url() == 'https://www.labirint.ru/games/'


def test_header_office(web_browser):
    page = MainPage(web_browser)
    page.header_office.click()

    assert page.get_current_url() == 'https://www.labirint.ru/office/'


def test_header_club(web_browser):
    page = MainPage(web_browser)
    page.header_club.click()

    assert page.get_current_url() == 'https://www.labirint.ru/club/'


def test_delivery(web_browser):
    page = MainPage(web_browser)
    page.delivery_and_payment.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'

def test_certificates(web_browser):
    page = MainPage(web_browser)
    page.certificates.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


def test_rating(web_browser):
    page = MainPage(web_browser)
    page.rating.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


def test_new_books(web_browser):
    page = MainPage(web_browser)
    page.new_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


def test_discount(web_browser):
    page = MainPage(web_browser)
    page.discount.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&' \
                                     'paperbooks=1&ebooks=1&otherbooks=1'


def test_contacts(web_browser):
    page = MainPage(web_browser)
    page.contacts.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


def test_support(web_browser):
    page = MainPage(web_browser)
    page.support.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'


def test_maps(web_browser):
    page = MainPage(web_browser)
    page.maps.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


def test_in_socials_vkontakte(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    vkontakte = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(vkontakte)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirint_ru'



def test_in_socials_odnoklasniki(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    odnoklasniki = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-ok"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(odnoklasniki)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://ok.ru/labirintru'




def test_in_socials_dzen(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    dzen = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-zen"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(dzen)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


def test_in_socials_instargam(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    instargam = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-inst"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(instargam)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintru/'


def test_in_socials_twitter(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    twitter = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-tw"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(twitter)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://twitter.com/labirint_ru'



def test_in_socials_telegram(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    telegram = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-tg"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(telegram)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://t.me/labirintru'



def test_in_socials_youtube(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    youtube = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-yt"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(youtube)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


def test_in_socials_instargam_kids(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    instargam_kids = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-inst-children"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(instargam_kids)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintdeti/'


def test_in_socials_tik_tok(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    tik_tok = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-tiktok"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(tik_tok)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru?'


def test_in_facebook(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    facebook = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-fb"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(facebook)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.facebook.com/labirintru'


def test_in_socials_vkontakte_kids(web_browser):
    page = MainPage(web_browser)
    in_socials = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    vkontakte_kids = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk-children"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(in_socials)
    actions.click(vkontakte_kids)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirintdeti'