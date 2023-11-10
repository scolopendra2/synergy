# лень кидать в zip реализую 2 функции, асинхронными их делать бессмысленно


def task_1():
    my_tuple = (1, 2, 3, 4)
    print(f'Кортеж: {my_tuple}')
    print(f'Первое число: {my_tuple[0]}')
    print(f'Второе число: {my_tuple[1]}')
    print(f'Третье число: {my_tuple[2]}')
    print(f'Четвёртое число: {my_tuple[3]}')
    print(f'Сумма: {sum(my_tuple)}')


def task_2():
    list_1 = input('Введите первый список: ').split()
    list_2 = input('Введите второй список: ').split()
    all_list = list_1 + list_2
    print(f'Количество пересечений: {len(all_list) - len(set(all_list))}')


if __name__ == '__main__':
    task_1()
    task_2()

# По таске комментарии не обязательны ==> их нет
# код по стандарту PEP8 в таких программах flake8 бессмысленно юзать
