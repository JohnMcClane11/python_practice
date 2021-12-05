import time
import pytest
from selenium import webdriver
driver = webdriver.Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('D:\driver\chromedriver.exe')
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()

#Входим в аккаунт
def test_my_pets_list():
   pytest.driver.find_element_by_id('email').send_keys('john555@gmail.com')
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

#проверяем уникальность имен в списке питомцев
def test_unique_names():
   pytest.driver.find_element_by_id('email').send_keys('john555@gmail.com')
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-deck")))
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   #проверяем уникальность имен после входа в аккаунт
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   pytest.driver.implicitly_wait(5)
   name = pytest.driver.find_elements_by_xpath('//td[1]')
   x = 0
   for i in range(len(name) - 1):
      for j in range(i + 1, len(name)):
         if name[i].text == name[j].text:
            x = 1
            quit()
   assert x == 0

#проверяем количество питомцев
def test_number_of_my_pets():
   pytest.driver.find_element_by_id('email').send_keys('john555@gmail.com')
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-deck")))
   #смотрим есть ли питомцы на странице
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   pytest.driver.implicitly_wait(5)
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr')
   cnt = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
   lines = cnt.split()
   print(lines[2])
   print(len(names))
   assert int(lines[2]) == len(names)

#проверяем наличие фотографий в карточках питомцев
def test_pets_profile_photo():
   pytest.driver.find_element_by_id('email').send_keys('john555@gmail.com')
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-deck")))
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   pytest.driver.implicitly_wait(5)
   pets_text = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
   assert 'Питомцев:' in pets_text.text
   amount_of_pets = int(pets_text.text.split('\n')[1].split(':')[1])
   lines = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//div[@id="all_my_pets"]/table[@class="table table-hover"]/tbody/tr')))
   lines_amount = len(lines)
   assert amount_of_pets == lines_amount
   lines = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//div[@id="all_my_pets"]/table[@class="table table-hover"]/tbody/tr/th/img')))
   pets_with_photo = 0
   for line in lines:
      if line.get_attribute('src') != '':
         pets_with_photo += 1
   assert pets_with_photo == amount_of_pets

#тестирование параметров карточек питомцев
def test_pets_profiles():
   pytest.driver.find_element_by_id('email').send_keys('john555@gmail.com')
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # удостоверяемся в наличии информации о питомцах
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-deck")))
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   images = pytest.driver.find_elements_by_xpath('//th/img')
   names = pytest.driver.find_elements_by_xpath('//td[1]')
   types = pytest.driver.find_elements_by_xpath('//td[2]')
   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert types[i].text != ''
      assert ', ' in types[i]
      parts = types[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

