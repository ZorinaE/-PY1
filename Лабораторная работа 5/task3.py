from random import  randint
def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    count = 15

    list_number = []  # вводим список для хранения укальных чисел
    for _ in range(count):
        i = randint(start, stop) # присваиваем рандомное значение
        while i in list_number:  # цикл для создания уникальных значения
            i = randint(start, stop)
        list_number.append(i)

    return list_number

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
