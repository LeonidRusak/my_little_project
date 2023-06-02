# Поиск текстовой строки, которая может находиться в любом из текстовых файлов
import os

search_text = input('Введите текст который необходимо найти: ')

all_text_file_list = []
search_results = []

for name in os.listdir('C:\\Users\\Andrei\\тренинг задачи\\files'):
    if name[-3:] == 'txt':
        all_text_file_list.append(name)

if len(all_text_file_list) == 0:
    print('Текстовые файлы не найдены')
else:
    for text_file in all_text_file_list:
        with open(f'C:\\Users\\Andrei\\тренинг задачи\\files\\{text_file}', 'r',
                  encoding='UTF-8') as file:
            text_in_file = file.read()
            if search_text in text_in_file:
                search_results.append(text_file)

if len(search_results) == 0:
    print('Текст в файлах не найден')

print(*search_results)
