import random

class Variables:
    user_name = f'Алексей{random.randint(0, 999)}'
    user_email = f'AlexTat_17_{random.randint(100, 999)}@yandex.ru'
    incorrect_password = random.randint(0, 99999)
    correct_password = random.randint(100000, 999999)
    user_email_static = "AlexTat_17_742@yandex.ru"
    correct_password_static = 129510

class Urls:
    url = "https://stellarburgers.nomoreparties.site/"