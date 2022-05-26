

import re

text = '13 pro max 512 silver - 100000₽🇪🇺'

match = re.match(r'pro', text)

# text = '13 pro max 512 silver - 100000₽🇪🇺'
# price = re.findall(r'\w+', text)
# new_price = int(price[5]) + count
# print(new_price)
#
#
# match = re.search(r'pro max', text)


#print(match[0] if match else 'Not found')

count = 4000
def reformat():
    text2 = '13 pro max 512 silver - 106000₽🇪🇺'
    price = re.findall(r'\w+', text2)
    new_price = int(price[5]) + count
    print(new_price)


data = text.split('\n')
for phone in data:
    phone_data = phone.split(' ')
    model = ' '.join(phone_data[:3])
    memory = phone_data[3]
    color = phone_data[4]
    price = phone_data[6][:-2]
    region = phone_data[6][-2:]


#data = text2.split('\n')
#print(data)
#for phone in data:
    #phone_data = phone.split(' ')
    #price = re.split(r'\w+', text2)
    #new_price = int(price[5]) + count
    #print(new_price)
    #model = ' '.join(phone_data[:3])
    #print(price)
    # memory = phone_data[3]
    # print(memory)
#     color = phone_data[4]
#     print(color)
#     price = phone_data[6][:-2]
#     region = phone_data[6][-2:]
#     print(model, memory, color, price, region)


#         elif len(phone_data) <= 7:
#             model = ' '.join(phone_data[:3])
#             memory = phone_data[3]
#             color = phone_data[4]
#             price = phone_data[6][:-2]
#             region = phone_data[6][-2:]
# Phone.objects.create(model_phone=model,
#                      memory_phone=memory,
#                      colors_phone=color,
#                      price_phone=price,
#                      region_phone=region)

# лучше bulk_create - множественоое создание. но это не критично

# def reverse_string(string):
#     index = len(string) - 1
#     reversed_string = ''
#
#     while index >= 0:
#         current_char = string[index]
#         reversed_string = reversed_string + current_char
#         # То же самое через интерполяцию
#         # reversed_string = f"{reversed_string}{current_char}"
#         index = index - 1
#
#     return reversed_string
#
# reverse_string('Game Of Thrones') # 'senorhT fO emaG'
# # Проверка нейтрального элемента
# reverse_string('')

# ''

'''
13 pro 512 green - 100000₽🇯🇵
13 pro max 512 silver - 100000₽🇪🇺
13 pro max 512 gold - 100000₽🇺🇸
13 pro max 256 gray - 100000₽🇺🇸
13 pro max 256 green - 100000₽🇯🇵
13 pro max 256 green - 100000₽🇦🇪
13 pro max 256 blue - 100000₽🇯🇵
13 pro max 256 blue - 100000₽🇺🇸
13 pro max 256 silver - 100000₽🇯🇵
13 pro max 128 gray - 100000₽🇺🇸
13 pro max 128 gray - 100000₽🇯🇵
13 pro max 128 blue - 100000₽🇯🇵
13 pro max 128 green - 100000₽🇯🇵

'''
'''
findall() — Возвращает список, содержащий все совпадения
search() — Возвращает объект Match, если где-либо в строке есть совпадение
split() — Возвращает список, в котором строка была разделена при каждом совпадении
sub() — Заменяет одно или несколько совпадений строкой
subn() — Делает то же самое, что и sub(), но возвращает новую строку и количество замен
match() — Ищет совпадение с начала строки
finditer() — Ищет все совпадения с pattern, возвращает итератор
compile() — Компилирует regular expression, на выходе получаем объект, к которому затем можно применять все перечисленные функции
fullmatch() — Проверяет, что вся строка соответствует описанному регулярному выражению
flags (флаги) — Указываются в функциях, влияют на поведение регулярного выражения'''

from django.test import TestCase

# Create your tests here.

# class short(list):
#     def __init__(self, model_phone, memory, colors, price, region):
#         self.model_phone = model_phone
#         self.memory = memory
#         self.colors = colors
#         self.price = price
#         self.region = region
#
#     def short_price(self):
#         pass

# coun = 0
# price = input().split()
# for i in price:
#     i += 1
#     print(price)
# print(price[0])

# for c, value in enumerate(price, 1):
#     print(c, value)
#     #print(c)
# for i in range(len(price)):
#     print(i)
# name_phone = print(price[0] + price[1], price[3] + price[4] + price[5])
# p2 = short(price)
# print(", ".join(price))

# import re
# result = re.findall(r'^\w+', '')
# print(result)




#Check if the string starts with "The" and ends with "Spain":
# txt = "13 pro max 512 green - 119500₽🇯🇵"
# x = re.search("^pro.*max$", txt)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# re.match()
# re.search()
# re.findall()
# re.split()
# re.sub()
# re.compile()


