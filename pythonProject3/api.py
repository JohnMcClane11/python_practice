import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    '''В библитеке лежат API запросы к приложению PetFriends'''
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_keys(self, email, password):
        '''Делаем get запрос с почтой и паролем в заголовке
        Получаем статус код и ключ в формате json или text'''
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def get_list_of_pets(self, auth_key, filter):
        '''С помощью данного метода мы получаем список питомцев
        в виде json или тектовом формате'''
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pets(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        '''С помощью post метода добавляем информацию о новом питомце
        В ответ получаем статус код и информацию о питомце в формате json/text'''
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })

        headers = {
            'auth_key': auth_key['key'],
            'Content-Type': data.content_type
        }

        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pets(self, auth_key: json, pet_id: str) -> json:
        '''Делаем delete запрос, с помощью которого удаляем питомца по его id
        В ответ получаем статус код операции'''
        headers = {
            'auth_key': auth_key['key'],
            'pet_id': pet_id
        }

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: str) -> json:
        '''Обновляем карточку уже существующего питомца
        В ответ получаем статус код и новые данные о питомце в формате json/text'''
        headers = {
            'auth_key': auth_key['key'],
            'pet_id': pet_id
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def no_photo_new_pet(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        '''С помощью метода post создаем новую карточку питомца без фото
        В ответ получае статус код и информацию о новом питомце в формате json/text'''
        headers = {
            'auth_key': auth_key['key'],
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def photo_for_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        '''С помощью метода post добавляем фотографию в уже созданную карточку питомца
        В ответ получаем информацию о питомце в формате json/text'''
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {
            'auth_key': auth_key['key'],
            'Content-Type': data.content_type
        }

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result