import requests
import json
from config import keys

class ConvertionExceprion(Exception):
    pass

class CurrancyConverter():
    @staticmethod
    def conver_t(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExceprion(f'Одинаковые виды валют не подлежат переводу! Вы ввели одинаковые валюты - "{base}".')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExceprion(f'Неизвестная валюта! {quote}. Список поддерживаемых валют доступен по команде /values')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExceprion(f'Неизвестная валюта! {base}. Список поддерживаемых валют доступен по команде /values')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExceprion(f'Не удалось распознать введенное число {amount}. Скорее всего, Вы ввели не число :(')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount
        return total_base
