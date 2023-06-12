# Добавление текстового водяного знака в правом нижнем углу на выбранное фото
from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_image, output_image, text, position):
    photo = Image.open(input_image)
    img = ImageDraw.Draw(photo)
    color = (136, 8, 8)  # Цвет текста (RGB)
    font = ImageFont.truetype('C:\\Windows\\Fonts\\arial.ttf', 30)
    img.text(position, text, fill=color, font=font)
    photo.show()  # Всплывающее окно для предварительного просмотра картинки с водяным знаком
    photo.save(output_image)


if __name__ == '__main__':
    file_name = input('Введите имя файла: ')
    text_watermark = input('Введите текст на водяном знаке: ')
    file_name_out = file_name[:-4] + '_watermark.jpg'
    add_watermark(file_name, file_name_out, text_watermark, position=(900, 500))
    print('Водяной знак добавлен')
