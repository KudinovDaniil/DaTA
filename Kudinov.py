#import math
#def sqrt(a):
#    print(a)
#print("Hello world!")

#a = 17.5
#b=(6,1,82,6)
#print(math.factorial(5))


#a = "рпривет земля"
#print(a[::-1])


#a = "hello world"
#a = "H" + a[1:]
#b = "l"
#print(a.isdigit())
#print(a.isalpha())
#print(a.replace(b, "", 2))
#print(a.rfind(b))
#print(a.islower())

#a = "abc"
#print(a.rjust(5, "0"))

#a = "   1 2 3 4 5 \t \n"
#print(",".join(a.split()))

#a = "\thello \nworld"
#print(a)

#a = [1, 2, 3, 4]
#a[0] = 10
#print(a)
#print((a[0] + a[1] + a[2] + a [3])/len(a))

#a = [1, 2]
#b = [3, 4, 5]
#print(a * 5 + b)
#print(2 in b)

#a = "hi".encode("UTF-8")
#print(a)
#print(a.decode("ASCII"))

#a = [1,2,3,4]
#a.append(5)
#b = a + [5]
#print(a)

#a = [1,2,3,4]
#a.append([6,6,6])
#b = "gfddf"
#a.append(b)
#print(a)
#print(map(int, a))

#a = [1,2,3,4,3,3]
#end = a.pop()
#print(end)

#a = [1,2,3,4,3,3]
#b = a.count(1616)
#print(b)

#a = [1,2,3,4,3,3]
#b = a.index(3,4,6)
#print(b)

#a = int(input())
#if a%2==0:
#    if 0 < a < 9:
#        print("1")
#    else:
#        print("2")

#trok = "HELlo"
#t = str(input())
#res = strok.upper() if t == "U" else strok.lower()
#print(res)

#a = -1
#b = True
#while b:
#    a+=1
#    if a == 10:
#        b = False
#print(a)

#N = 6
#a = [0] * N
#for i in range(N):
#    a[i] = i**2
#print(a)

#b = [x ** 2 for x in range(N)]
#print(b)

#a = ["abc","food","cities","mother","cat","dog"]
#b = [5,96,-16,861,3,16]
#c = [int(d) for d in range(-5,10) if d % 2 == 0 and d % 3 == 0]
#d = [i for i in a if len(i) > 3]
#e = ["Четное" if x % 2 == 0 else "Нечетное" for x in b]
#print(e)

#a = [(i,j)
#     for i in range(3)
#     for j in range(4)
#     ]
#b = [f"{i}*{j} = {i*j}"
#     for i in range(1,11)
#     for j in range(1,11)
#c = [x
#     for i in a
#     for x in i
#     ]
#print(c)

#b = dict(one = 1, two = 2)
#a = {"house": "дом",
#     "car": "машино",
#     "tree": "дерево",
#     "car": "123"}
#print(a["car"])
#print(b)

#c = lambda a, b: a + b
#rint (c(1,2))
#stok = [4,5,lambda: print("lambda"), "else"]
#stok[2]()

#def get_filter(a, filter = None):
#    if filter is None:
#        return a
#    res = []
#    for x in a:
#        if filter(x):
#            res.append(x)
#    return res
#lst = [5,3,0,-6,8,10,1]
#print(get_filter(lst, lambda p: p % 2 == 0))

#a = 5
#w, h = 100, 100
#def my_fun(lst):
#    for x in lst:
#        n = x + 1
#        print(n)
##    print(w,n)
#    print(a,h)
#my_fun([1,2,3])
#print(a)

##import math as mt
#from math import ceil, pi
#import pprint
#pprint.pprint(locals())
#def ceil(x):
#    print("Мой ceil")
#    return x
#print(ceil(1.8))
##math = "Математика"
##print(mt.pi)

#def ceil(x):
#    print("Мой ceil")
#    return x
#from math import ceil as m_ceil, pi
#from time import *
#import pprint
#pprint.pprint(locals())
#print(time())
#print(ceil(1.8))

#Name = "my_module"
#def floor(x):
#    print("floop is my_model")
#    return int(x) if x>= 0 else int(x) -


import re
import json
import os

DATA_FILE = 'users.json'

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def validate_user_data(data):
    errors = {}
    is_valid = True

    if not data.get('email'):
        errors['email'] = 'Email не может быть пустым.'
        is_valid = False
    elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
        errors['email'] = 'Некорректный формат email. Ожидается XXX@XXX.XXX'
        is_valid = False

    if not data.get('password'):
        errors['password'] = 'Пароль не может быть пустым.'
        is_valid = False
    elif len(data['password']) < 8:
        errors['password'] = 'Пароль должен содержать не менее 8 символов.'
        is_valid = False
    elif not re.search(r'\d', data['password']):
        errors['password'] = 'Пароль должен содержать хотя бы одну цифру.'
        is_valid = False
    elif not re.search(r'[A-Z]', data['password']):
        errors['password'] = 'Пароль должен содержать хотя бы одну заглавную букву.'
        is_valid = False

    if not isinstance(data.get('age', None), int):
        errors['age'] = 'Возраст должен быть числом.'
        is_valid = False
    elif data.get('age', 0) < 18 or data.get('age', 0) > 100:
        errors['age'] = 'Возраст должен быть от 18 до 100.'
        is_valid = False

    if not data.get('phone'):
        errors['phone'] = 'Номер телефона не может быть пустым.'
        is_valid = False
    elif not re.match(r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$', data['phone']):
        errors['phone'] = 'Некорректный формат номера телефона. Ожидается +7(XXX)XXX-XX-XX'
        is_valid = False

    if 'tariff' in data and data['tariff'] not in ['', 'basic', 'standard', 'premium']:
        errors['tariff'] = 'Некорректный тариф. Доступные тарифы: basic, standard, premium.'
        is_valid = False
    return {'valid': is_valid, 'errors': errors}

tariff_info = {
    'basic': {
        'description': 'Тариф Basic: включает базовые функции и поддержку.',
        'gb': '10 ГБ',
        'cost': '350 руб/мес'
    },
    'standard': {
        'description': 'Тариф Standard: расширенные функции и приоритетная поддержка.',
        'gb': '50 ГБ',
        'cost': '500 руб/мес'
    },
    'premium': {
        'description': 'Тариф Premium: все функции + персональный менеджер и эксклюзивные предложения.',
        'gb': '200 ГБ',
        'cost': '800 руб/мес'
    }
}

def show_tariff_info(tariff):
    info = tariff_info.get(tariff)
    if info:
        print(f"\n{info['description']}")
        print(f"Объем данных: {info['gb']}")
        print(f"Стоимость: {info['cost']}\n")
    else:
        print('Информация о данном тарифе недоступна.')

def authorize(users):
    email = input("Введите ваш email: ")
    password = input("Введите ваш пароль: ")
    user_data = users.get(email)
    if user_data and user_data['password'] == password:
        print("Авторизация успешна.")
        return user_data
    else:
        print("Неверный email или пароль.")
        return None

def tariff_menu(user, users): #Функция для меню тарифов
    while True:
        print("\nМеню тарифов:")
        print("1 - подписаться на тариф")
        print("0 - отменить подписку")
        print("2 - пропустить (оставить текущий тариф)")
        print("3 - информация о тарифах")
        print("4 - завершить настройку тарифов и продолжить")
        print("5 - статус подписки тарифа")
        choice = input("Ваш выбор: ")

        if choice == '1':
            print("Выберите тариф: 1 - basic, 2 - standard, 3 - premium")
            tariff_choice = input("Введите номер тарифа: ")
            if tariff_choice == '1':
                tariff = 'basic'
            elif tariff_choice == '2':
                tariff = 'standard'
            elif tariff_choice == '3':
                tariff = 'premium'
            else:
                print("Некорректный выбор.")
                continue
            user['tariff'] = tariff
            show_tariff_info(tariff)
            save_users(users)
        elif choice == '0':
            tariff = ''
            print("Вы отменили подписку.")
            user['tariff'] = tariff
            save_users(users)
        elif choice == '2':
            pass
        elif choice == '3':
            print("Доступные тарифы:")
            for key, info in tariff_info.items():
                print(f"{key}: {info['description']}")
                print(f"  Объем данных: {info['gb']}")
                print(f"  Стоимость: {info['cost']}\n")
            continue
        elif choice == '4':
            break
        elif choice == '5':
            if user and user.get('tariff'):
                show_tariff_info(user['tariff'])
            else:
                print("Вы не подписаны на тариф.")
        else:
            print("Некорректный ввод.")

def main():
    users = load_users()
    user = None

    print("Добро пожаловать! Авторизация.")
    while not user:
        choice = input("1 - Войти, 2 - Зарегистрироваться: ")
        if choice == '1':
            user = authorize(users)

        elif choice == '2':
            print("Регистрация нового пользователя.")
            email = input("Введите email: ")
            if email in users:
                print("Этот email уже зарегистрирован.")
                continue
            password = input("Введите пароль: ")
            age = int(input("Введите возраст: "))
            phone = input("Введите номер телефона (+7(XXX)XXX-XX-XX): ")
            user_data = {
                'email': email,
                'password': password,
                'age': age,
                'phone': phone,
                'tariff': ''
            }

            validation = validate_user_data(user_data)
            if validation['valid']:
                users[email] = user_data
                save_users(users)
                print("Регистрация успешна.")
                user = user_data
            else:
                print("Ошибки при регистрации:", validation['errors'])
        else:
            print("Некорректный выбор.")

    if user: # Если пользователь успешно зашел или зарегистрировался
        print("Ваши текущие данные:")
        print(f"Email: {user['email']}")
        print(f"Возраст: {user['age']}")
        if user.get('tariff'):
            print(f"Текущий тариф: {user['tariff']} (подписан)")
        else:
            print("Текущий тариф: Не подписан")
        tariff_menu(user, users) # Вызов меню тарифов
        if user.get('tariff'):
             print(f"Вы подписаны на тариф: {user.get('tariff')}.")
        else:
            print("Вы не подписаны на тариф.")

while True:
    main()
    exit_choice = input("Хотите выйти? (да/нет): ").strip().lower()
    if exit_choice == 'да' or exit_choice == 'y' or exit_choice == 'yes':
        print("Завершение программы.")
        break
    else:
        print("Переходим к следующей итерации...\n")