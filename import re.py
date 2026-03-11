import re
import json
import os

DATA_FILE = 'C:...\DATA_FILE'

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