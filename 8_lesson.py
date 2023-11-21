my_dict = dict()

my_dict['name'] = 'John'
my_dict['age'] = 25
my_dict['city'] = 'New York'

print(my_dict)

my_dict['name'] = 26
my_dict['email'] = 'john@example.com'

print('country' in my_dict)

del my_dict['city']

for k, v in my_dict.items():
    print(f'Ключ: {k}, Значение: {v}')