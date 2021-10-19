import telebot
from config import keys, token
from extensions import ConvertionExceprion, CurrancyConverter

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_(message: telebot.types.Message):
    text = 'Для начала конвертации необходимо ввести команду боту в виде:\n' \
           '<ваша валюта> <валюта для перевода> <количество валюты> \n' \
           'Введите команду /values для вывода информации о доступных валютах для обмена\n' \
           'Введите команду /help для помощи при пользовании ботом'
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help_(message: telebot.types.Message):
    text = 'Формат для ввода запроса: <ваша валюта> <валюта для перевода> <количество валюты> \n' \
           'Данные необходимо ввести с маленькой буквы, через пробел. \n' \
           'Введите команду /values для вывода информации о доступных валютах для обмена'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def conver_t(message: telebot.types.Message):
    try:
        value_s = message.text.split(' ')

        if len(value_s) != 3:
            raise ConvertionExceprion('Введите данные заново:\n'
                                      'в именительном падеже\n'
                                      'с маленькой буквы\n'
                                      'через пробел')

        quote, base, amount = value_s
        total_base = CurrancyConverter.conver_t(quote, base, amount)

    except ConvertionExceprion as e:
        bot.reply_to(message, f'Ошибка ввода. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Неизвестная команда\n{e}')
    else:
        text = f'Стоимость {amount} {quote} относительно {base} = {total_base} '
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)