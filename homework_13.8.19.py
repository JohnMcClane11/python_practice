tickets = int(input('Введите количество билетов:\t'))
q = 0
for price in range(1, tickets + 1):
    age = int(input("Введите возраст посетителя:\t"))
    if 0 <= age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    elif 25 <= age <= 99:
        price = 1390
    else:
        print('Вы ввели неправильный возраст!')
    q = q + price
if tickets > 3:
    discount = int(q - q * 0.1)
    print(f'Сумма вашего заказа: {discount} рублей. Спасибо за покупку!')
else:
    print(f'Сумма вашего заказа: {q} рублей. Спасибо за покупку!')