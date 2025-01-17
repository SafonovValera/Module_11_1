import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from requests import head, get
from io import BytesIO


#=============== Pandas =================

# Загрузим данные из текстового файла и отобразим первых 5 строк данных.
data = pd.read_fwf(r'Gogol_MD.txt')
print(data.head())
# Создадим таблицу из словаря.
data = { 'Имя': ['Вася', 'Вова', 'Саша'], 'Возраст': [21, 32, 43],
         'Город': ['Сочи', 'Питер', 'Москва'] }
table = pd.DataFrame(data)
print(table)
# Создадим таблицу из списка.
data = [ ['Вася', 21, 'Сочи'], ['Вова', 32, 'Питер'], ['Саша', 43, 'Москва'] ]
table = pd.DataFrame(data, columns=['Имя', 'Возраст', 'Город'])
print(table)

#=============== Pillow =================

# Откроем файл.
img = Image.open('img.jpg')
print("Исходный размер:", img.size)

# Уменьшим размер изображения в два раза.
new_size = (img.width // 2, img.height // 2)
resized_img = img.resize(new_size)

# Сохраним уменьшенное изображение в файл.
resized_img.save('resize_img.jpg')
print("Изменённый размер:", resized_img.size)

# Преобразуем изображение в черно-белый формат.
bw_img = img.convert('L')
bw_img.save('bw_img.jpg')

# Сохраним его в формате png.
img.save('new_img.png', format='PNG')

# Добавим текст на изображение.
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', size=40)
draw.text((15, 15), 'Это использование библиотеки Pillow!', fill='red', font=font)
img.save('pillow_img.jpg')

#================ Requests ==================

# Получим HTTP-заголовки.
response = head('https://www.ozon.ru/')
print(response.headers)

# Достанем изображение в формате строки байт и сохраним в png формате.
response = get('https://ir-7.ozone.ru/s3/multimedia-d/wc1000/6834952453.jpg')
print(response.content)
img = Image.open(BytesIO(response.content))
img.save('grob_img.png')

# Делаем запрос на чтение страницы.
response = get('https://mfc47.ru/')
print(response.ok)  # проверяем успешен ли запрос?
print(response.text)  # выводим полученный ответ на экран