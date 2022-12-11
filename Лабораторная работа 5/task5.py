import string
from random import sample
def get_random_password(count=8) -> str:
    list_1 = [i for i in str(string.ascii_uppercase + string.ascii_lowercase + string.digits)]  # список всех  возможных символов
    list_password = sample(list_1, count) # генерация пароля

    return "".join(str(i) for i in list_password) # перевод в виде строки


print(get_random_password())
