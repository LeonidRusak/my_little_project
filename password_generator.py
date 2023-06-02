# Генерация пароля по заданной длине
import random
import string

len_password = int(input('Введите количество символов в генерируемом пароле:'))

password_elements = [i for i in string.ascii_letters] + [i for i in string.digits] + [i for i in string.punctuation]

password_list = []
while len(password_list) != len_password:
    password_list.append(password_elements[random.randint(0, len(password_elements) - 1)])

print(f'Сгенерированный пароль из {len_password} символов:', ''.join(password_list), sep='\n')
