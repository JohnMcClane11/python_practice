import os
from pages.base import Page
from pages.elements import PageElements


class MainPage(Page):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)


    login_field = PageElements(xpath='//*[@class="full-input__input formvalidate-error"]')
    enter = PageElements(xpath='//*[@id="g-recap-0-btn"]')
    automatic_closing = PageElements(xpath='//*[@id="auth-success-login"]/input[2]')
    auth_error = PageElements(xpath='//a[contains(text(),"Введенного кода не существует")]')
    auth_error_2 = PageElements(xpath='//span[contains(text(),"Нельзя использовать символ «{N}»")]')


    logo = PageElements(xpath='//*[@class="b-header-b-logo-e-logo-wrap"]')
    winter_sale = PageElements(xpath='//*[@class="b-header-b-logo-e-discount"]')
    mesages = PageElements(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[1]/span')
    log_in = PageElements(xpath='//span[contains(text(),"Введите свой код скидки, телефон или эл.почту")]')
    my_labirint = PageElements(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[4]/a/span[2]')
    deferred = PageElements(xpath='//*[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    cart = PageElements(xpath='//*[@class="b-header-b-personal-e-list-item have-dropdown  last-child"]')
    plus_18 = PageElements(xpath='//*[@class="b-header-e-icon-adult b-header-e-icon-adult-m-big '
                               'b-header-e-sprite-background"]')
    header_books = PageElements(xpath='//span[@class="b-header-b-menu-e-link top-link-menu first-child"]')
    header_main_2021 = PageElements(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[2]/span/a')
    header_school = PageElements(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[3]/span/a')
    header_toys = PageElements(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[4]/span/a')
    header_office = PageElements(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[5]/span/a')
    header_club = PageElements(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[11]/span/a')
    delivery_and_payment = PageElements(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[1]/a')
    certificates = PageElements(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[2]/a')
    rating = PageElements(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    new_books = PageElements(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[4]/a')
    discount = PageElements(xpath='//a[@href="/sale/"]')
    contacts = PageElements(xpath='//*[@data-event-content="Контакты"]')
    support = PageElements(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[10]/a')
    maps = PageElements(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[11]/a')


    search = PageElements(id='search-field')
    search_btn = PageElements(xpath='//button[@type="submit"]')
    successful_search = PageElements(xpath='//span[contains(text(),"Все, что мы нашли в Лабиринте по запросу")]')
    not_successful_search = PageElements(xpath='//h1[contains(text(),"Мы ничего не нашли по вашему запросу! Что '
                                             'делать?")]')
    all_filers = PageElements(xpath='//span[contains(text(), "ВСЕ ФИЛЬТРЫ") and @class="navisort-item__content"]')
    reset_all_filers = PageElements(xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]/div/span[3]')
    available = PageElements(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[1]/label[1]/span[2]')
    not_available = PageElements(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[4]/label[1]/span[2]')
    show_all_found = PageElements(xpath='//input[@class="show-goods__button"]')


    best_sale = PageElements(xpath='//a[@href="/best/sale/"]')
    random_book = PageElements(xpath='//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[1]/div/div[1]/div/div[1]')
    random_book_1 = PageElements(xpath='//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[3]/div/div[1]/div/div[1]')
    buy_book = PageElements(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    successfuly_odered = PageElements(xpath='//span[contains(text(),"Ваш заказ")]')
    add_to_deferred = PageElements(xpath='//a[@class="fave"]')
    successfuly_deferred = PageElements(xpath='//a[@title="Выделить все отложенные товары"]')
    compare = PageElements(xpath='//a[@title="Добавить к сравнению"]')
    successfuly_compared = PageElements(xpath='//*[@class="compare big-compare done"]')
    compare_books = PageElements(xpath='//a[@href="/compare/"]')


    plus_one_more = PageElements(xpath='//span[@class="btn btn-increase btn-increase-cart"]')
    remove_from_cart = PageElements(xpath='//span[@class="btn btn-lessen btn-lessen-cart"]')
    two_books_in_cart = PageElements(xpath='//input[Compare(test()), "2") and @class="quantity"]')
    empty_cart = PageElements(xpath='//span[contains(text(),"Ваша корзина пуста. Почему?"]')
    btn_ok_close = PageElements(xpath='//span[@class="fright btn btn-primary btn-middle"]')