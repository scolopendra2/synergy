# лень кидать в zip реализую 3 функции, асинхронными их делать бессмысленно
# в прошых тасках забыл проверку на отрицательный возраст ну ладно


def task_1():
    age = input('Введите совй возраст: ')
    if not age.isdigit():
        print('ERROR! Это не число')
    else:
        return 'Вы совершеннолетний' if int(age) > 17 else 'Вы несовершеннолетний'


def task_2():
    num1 = input('Введите 1 число: ')
    if not num1.isdigit():
        return 'ERROR! Это не число'
    else:
        num2 = input('Введите 2 число: ')
        if not num2.isdigit():
            return 'ERROR! Это не число'
        else:
            if eval(f'{num1} == {num2}'):
                return 'Оба числа равны'
            else:
                return 'Первое число больше второго' if int(num1) > int(num2) else \
                    'Второе число больше первого'


def task_3():
    name = input('Введите своё имя: ')
    if name == '':
        return 'Вы не ввели имя.'
    else:
        return f'Привет, {name}!'


if __name__ == '__main__':
    print(task_1())
    print(task_2())
    print(task_3())

# По таске комментарии не обязательны ==> их нет
# код по стандарту PEP8 в таких программах flake8 бессмысленно юзать
