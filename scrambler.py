# Шифратор/дешифратор текста с записью в текстовый файл

selection = int(input('Для шифрования текста введите - 1, для дешифрования - 2: '))

if selection != 1 and selection != 2:
    print("Некорректный ввод команды")
    exit()

text = input('Введите текст: ')
encoding_key = {'a': '7', 'b': '&', 'c': 'M', 'd': '>', 'e': '(', 'f': '=', 'g': ']', 'h': 'O', 'i': 'm', 'j': 'F',
                'k': "'", 'l': '{', 'm': '[', 'n': 'f', 'o': 'j', 'p': 'U', 'q': 'N', 'r': '3', 's': 'w', 't': 'J',
                'u': '4', 'v': '5', 'w': 'Q', 'x': ';', 'y': '<', 'z': '6', 'A': '"', 'B': 'D', 'C': 'I', 'D': 'h',
                'E': 'V', 'F': '_', 'G': 'p', 'H': '!', 'I': '1', 'J': 'v', 'K': 'q', 'L': 'X', 'M': 'B', 'N': '8',
                'O': '?', 'P': 'K', 'Q': 'n', 'R': 'x', 'S': '#', 'T': 'T', 'U': 'P', 'V': 'Y', 'W': 'd', 'X': '9',
                'Y': '2', 'Z': 'H', '0': '@', '1': 'z', '2': '\\', '3': 'i', '4': 'A', '5': '$', '6': '%', '7': '-',
                '8': ' ', '9': 'o', '!': 't', '"': 'S', '#': 'l', '$': 'W', '%': ')', '&': 's', "'": 'R', '(': 'g',
                ')': 'c', '*': '~', '+': '*', ',': 'y', '-': 'G', '.': 'u', '/': 'L', ':': 'C', ';': 'a', '<': '/',
                '=': 'k', '>': '^', '?': '`', '@': '+', '[': '0', '\\': ':', ']': '.', '^': ',', '_': 'b', '`': '}',
                '{': 'Z', ' ': 'e', '}': 'E', '~': 'r'}
decoding_key = {value: key for key, value in encoding_key.items()}

if selection == 1:
    encoded_text = ''
    for i in text:
        encoded_text += encoding_key[i]

    with open('C:\\Users\\Andrei\\тренинг задачи\\files\\encoded_file', 'w') as file:
        file.write(encoded_text)

elif selection == 2:
    decoded_text = ''
    for i in text:
        decoded_text += decoding_key[i]
    with open('C:\\Users\\Andrei\\тренинг задачи\\files\\decoded_file', 'w') as file:
        file.write(decoded_text)
