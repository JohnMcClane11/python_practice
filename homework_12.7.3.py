money = float(input("Введите сумму депозита: "))
per_cent = {'ТБК': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
my_deposit = []
my_deposit.append(per_cent['ТБК'] / 100 * money)
my_deposit.append(per_cent['СКБ'] / 100 * money)
my_deposit.append(per_cent['ВТБ'] / 100 * money)
my_deposit.append(per_cent['СБЕР'] / 100 * money)
print(list(map(round, my_deposit)))
max_deposit = max(my_deposit)
print('Максимальная сумма, которую вы можете заработать: ', round(max_deposit))
