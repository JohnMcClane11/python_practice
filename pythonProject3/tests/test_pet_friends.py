from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os


pf = PetFriends()


def test_get_api_for_valid_user(email=valid_email, password=valid_password):
    '''Проверка получения ключа'''
    status, result = pf.get_api_keys(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    '''Проверка получения списка всех питомцев'''
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Драконус', animal_type='Дракон',
                                     age='100', pet_photo='images/dragon1.jpg'):
    '''Тест возможности создать нового питомца с фото'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_update_self_pet_info(name='Draggy', animal_type='dragon', age='101'):
    '''Тест апдейта информации о питомце на сайте'''
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

def test_delete_self_pet():
    '''Тест возможности удаления карточки питомца'''
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pets(auth_key, "Drag", "дракон", "200000", "images/dragon2.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pets(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    '''{1}Тест получения ключа при вводе неверного адреса почты'''
    status, result = pf.get_api_keys(email, password)
    assert status == 403

def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    '''{2}Тест возможности получения ключа при вводе неправильного пароля'''
    status, result = pf.get_api_keys(email, password)
    assert status == 403

def test_add_new_pet_without_photo(name='Draggy', animal_type='Дракон',
                                     age='99'):
    '''{3}Тест добавления нового питомца без фото профиля'''
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.no_photo_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_pet_photo(pet_photo='images/dragon2.jpg'):
    '''{4}Тест возможности добавления фотографии к уже существующему профилю питомца'''
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    _, result = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = result['pets'][0]['id']
    status, result = pf.photo_for_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo'] is not None
    assert 'jpeg' in result['pet_photo']

def test_add_new_pet_with_no_data(name='', animal_type='',
                                     age=''):
    '''{5}Нешативный тест на возможность создания профиля питомца с путыми строками'''
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.no_photo_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    """Ожидаемый статус код = 500, остальные значения - отклонение"""

def test_add_new_pet_with_incorrect_name(name='оевтгвкпвгпткг32576237*?:№%?№:ырпрыгмиышг',
                                      animal_type='дракон',
                                     age='100', pet_photo='images/dragon1.jpg'):
    '''{6} Негавтивный тест на возможность создания питомца с большим именем,
    содержащим недопутимые знаки'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    """Ожидаемый статус код = 500, остальные значения - отклонение"""

def test_add_new_pet_with_incorrect_animal_type(name='Дракон',
                                      animal_type='34276',
                                     age='100', pet_photo='images/dragon1.jpg'):
    '''{7} Негативный тест на возможность ввода чисел в поле animal_type'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    """Ожидаемый статус код = 500, остальные значения - отклонение"""

def test_add_new_pet_with_incorrect_age(name='Дракон',
                                      animal_type='Dragon',
                                     age='1000001', pet_photo='images/dragon1.jpg'):
    '''{8} Негативный тест на возможность ввода больших числовых значений в поле age'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    """Ожидаемый статус код = 500, остальные значения - отклонение"""

def test_add_new_pet_with_incorrect_age_again(name='Дракон',
                                      animal_type='Dragon',
                                     age='-15', pet_photo='images/dragon1.jpg'):
    '''{9} Негативный тест на возможность ввода отрицательных значений в поле age'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    """Ожидаемый статус код = 500, остальные значения - отклонение"""

def test_add_new_pet_with_incorrect_age_again_again(name='Дракон',
                                      animal_type='Dragon',
                                     age='Драконий возраст', pet_photo='images/dragon1.jpg'):
    '''{10} Негативный тест на возможность ввода текста в поле age'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_keys(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    """Ожидаемый статус код = 500, остальные значения - отклонение"""