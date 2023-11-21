operations = ['+', '-', '/', '*']
print(f'Привет! Это простой простой калькулятор.\nДоступные операции: {", ".join(operations)}')
operator = input('Выберите операцию: ')
if operator not in operations:
    print('ERROR! Неверный оператор')
else:
    num1 = input('Введите 1 число: ')
    if not num1.isdigit():
        print('ERROR! Это не число')
    else:
        num2 = input('Введите 2 число: ')
        if not num2.isdigit():
            print('ERROR! Это не число')
        else:
            print(f'Результат: {eval(f"{num1} {operator} {num2}")}')

# По таске комментарии не обязательны ==> их нет
# Говнокод, вижу но могу улучшить его только переписав через PyQT5
