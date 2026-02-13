print('Задание 1')

user1 = input('Введите ваше имя: ')
user2 = input('Введите вашу фамилию: ')
user3 = input('Введите ваш возраст: ')
#format
print('Ваше имя: {}, фамилия: {}, возраст: {}'.format(user1, user2, user3))
#f-string
print(f'Ваше имя: {user1}, фамилия: {user2}, возраст: {user3}')

print('Задание 2')

cc = input('Введите число ')
if cc.isdigit():
    cc = int(cc)
    if cc%2 == 0: print('Число четное')
    else: print('Число нечетное')
else: print('Введено не число')

print('Задание 3')

age = input('Укажите свой возраст ')
if age.isdigit():
    age = int(age)
    if age>=18:
        print('Вы совершеннолетний')
    elif age<18: print('Вы несовершеннолетний')
    else: print('Возраст не может быть отрицательным')
else: print('Возраст должен быть положительным')

print('Задание 4')

while True:
    nu = input('Введите целое число ')
    if nu == 'exit':
        print('Выход из программы...')
        break
    if nu.lstrip('-').isdigit():
        if nu.startswith('-'):
            print('В этом числе', len(nu)-1, 'цифр')
        else:
            print('В этом числе', len(nu), 'цифр')
        break  
    else:
        print('Это должны быть числа')

