
# Задача 1.1.

# Есть строка с перечислением песен
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

print(len(my_favorite_songs))

my_favorite_songs[:14] + ' ' + my_favorite_songs[64:77] + ' ' + my_favorite_songs[16:30] + ' ' + my_favorite_songs[50:62]

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
print("Три песни звучат", random.choice(my_favorite_songs)[1] + random.choice(my_favorite_songs)[1] + random.choice(my_favorite_songs)[1], "минут")

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
import random 
print('Три песни звучат', random.choice(list(my_favorite_songs_dict.values())) + random.choice(list(my_favorite_songs_dict.values())) + random.choice(list(my_favorite_songs_dict.values())), 'минут')

# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

a = int(input("Введите номер месяца: "))
if a == 1:
    print("Вы ввели январь. 31 дней")
if a == 2:
    print("Вы ввели февраль. 28 дней")
if a == 3:
    print("Вы ввели март. 31 дней")
if a == 4:
    print("Вы ввели апрель. 30 дней")
if a == 5:
    print("Вы ввели май. 31 дней")
if a == 6:
    print("Вы ввели июнь. 30 дней")
if a == 7:
    print("Вы ввели июль. 31 дней")
if a == 8:
    print("Вы ввели август. 31 дней")
if a == 9:
    print("Вы ввели сентябрь. 30 дней")
if a == 10:
    print("Вы ввели октябрь. 31 дней")
if a == 11:
    print("Вы ввели ноябрь. 30 дней")
if a == 12:
    print("Вы ввели декабрь. 31 дней")
elif a >= 13:
    print('Такого месяца нет!')

# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175},]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"


print((list(titles))[0],'-',(store['100000110'][0])['quantity'],'шт,', 'стоимость ',((store['100000110'][0])['quantity']*(store['100000110'][0])['price']), 'руб')
print((list(titles))[1],'-',(store['100000146'][0])['quantity']+(store['100000146'][1])['quantity'], 'шт,', 'стоимость', (((store['100000146'][0])['quantity']*(store['100000146'][0])['price'])+((store['100000146'][1])['quantity']*(store['100000146'][1])['price'])), 'руб')
print((list(titles))[2],'-',(store['100000149'][0])['quantity']+(store['100000149'][1])['quantity'], 'шт,', 'стоимость', (((store['100000149'][0])['quantity']*(store['100000149'][0])['price'])+((store['100000149'][1])['quantity']*(store['100000149'][1])['price'])), 'руб')
print((list(titles))[3],'-',(store['100000194'][0])['quantity']+(store['100000194'][1])['quantity'], 'шт,', 'стоимость', (((store['100000194'][0])['quantity']*(store['100000194'][0])['price'])+((store['100000194'][1])['quantity']*(store['100000194'][1])['price'])), 'руб')
print((list(titles))[4],'-',(store['100000224'][0])['quantity']+(store['100000224'][1])['quantity']+(store['100000224'][2])['quantity'], 'шт,', 'стоимость', (((store['100000224'][0])['quantity']*(store['100000224'][0])['price'])+((store['100000224'][1])['quantity']*(store['100000224'][1])['price'])+((store['100000224'][2])['quantity']*(store['100000224'][2])['price'])), 'руб')
print((list(titles))[5],'-',(store['100000280'][0])['quantity'],'шт,', 'стоимость ',((store['100000280'][0])['quantity']*(store['100000280'][0])['price']), 'руб')
