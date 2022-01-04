import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import colored

class Page(object):

    _web_driver = None

    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self.get(url)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self.__getattribute__(name)._set_value(self._web_driver, value)
        else:
            super(WebPage, self).__setattr__(name, value)

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)

        if not item.startswith('_') and not callable(attr):
            attr._web_driver = self._web_driver
            attr._page = self

        return attr

    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()

    def get_back(self):
        self._web_driver.back()
        self.wait_page_loaded()

    def refresh(self):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def save_screenshot(self, file_name='screenshot.png'):
        self._web_driver.save_screenshot(file_name)

    def window_switching(self):
        self._web_driver.switch_to.window(self.window_handles[1])

    def scroll(self):
        self._web_driver.find_element_by_tag_name('body').send_keys(Keys.END)

    def scroll_part_down(self):

        self._web_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

    def current_url(self):

        return self._web_driver.current_url

    def get_page_source(self):

        source = ''
        try:
            source = self._web_driver.page_source
        except:
            print(colored('Не удается получить доступ к странице', 'red'))

        return source

    def js_errors_revision(self, ignore_list=None):

        ignore_list = ignore_list or []

        logs = self._web_driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'Внимание!':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS ошибка на странице"{0}"!'.format(log_message)

    def wait_for_ajax_loading(web_browser, class_name):
        WebDriverWait(web_browser, 10).until(lambda web_browser: len(web_browser.find_elements_by_class_name(
            class_name)) == 0)

    def wait_for_loading(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        source = ''
        try:
            source = self._web_driver.page_source
        except:
            pass

        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                try:
                    self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                new_source = ''
                try:
                    new_source = self._web_driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self._web_driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self._web_driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass

            assert k < timeout, 'Загрузка страницы заняла больше {0} секунд!'.format(timeout)

            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')