import random

from string import ascii_letters, digits, ascii_lowercase
from collections import Counter


def generation_id():
    while True:
        user_id = ''.join(random.choices(digits, k=3))
        last_digit = ''.join(random.choices(digits))
        return f'{user_id}{last_digit}{last_digit}'


def generation_username():
    while True:
        user_name = ''.join(random.choices(ascii_lowercase, k=6))
        letters = Counter(x for x in user_name)
        if all(cnt <= 2 for cnt in letters.values()):
            return user_name


def generation_password():
    symbols = f'{ascii_letters}{digits}'
    while True:
        pwrd = ''.join(random.choices(symbols, k=10))
        if pwrd[0] not in digits and any(n in digits for n in digits):
            return pwrd


def n_lst(n):
    lst = []
    us_id = set()
    username = set()
    password = set()

    while len(lst) < n:
        uid = generation_id()
        user = generation_username()
        passw = generation_password()

        if all([uid not in us_id, user not in username, passw not in password]):
            us_id.add(uid)
            username.add(user)
            password.add(passw)
            lst.append((uid, user, passw))
    return lst


print('Введите сколько хотите увидеть N троек вида (id, логин, пароль):')
num = int(input())
print(n_lst(num))
