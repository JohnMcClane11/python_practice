user_list = [
    'anna',
    'peter'
]
user_password = {
    'anna': 'qwerty',
    'peter': '12345'
}
username = input('Введите имя пользователя:\n')
if username in user_list:
    password = input('Введите ваш пароль:\n')
    if user_password[username] == password:
        print('ДОБРО ПОЖАЛОВАТЬ, ГОСПОДИН')
    else:
        print('неверный пароль')
else:
    print('Такого имени пользователя не существует')