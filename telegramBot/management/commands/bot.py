from django.core.management.base import BaseCommand
import telebot
from telebot import apihelper, types  # Нужно для работы Proxy
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from telegramBot.models import Profile, Message
from premiumsite.models import Phone, iPhone
from telegramBot import keyboard as kb

TOKEN = '1689112007:AAEujiNAdtUsZkoH86_dfPF15M6NIuhM4FU'
proxy = 'socks5://Proxy_User:Proxy_Password@Proxy_IP:Proxy_Port'

import urllib.request  # request нужен для загрузки файлов от пользователя

bot = telebot.TeleBot(TOKEN)  # Передаём токен из файла config.py
apihelper.proxy = {'http': proxy}  # Передаём Proxy из файла config.py
print(bot.get_me())

user_repear = ['ремонт', 'починить', 'отремонтировать', 'почистить']
user_buy = ['покупка', 'купить', 'покупать']
user_sale = ['продать', 'продажа', 'продаю', 'продавать']
user_other = ['другое']


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e

    return inner


# Тут работаем с командой start
@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    # Добавляем пользователя после запуска бота
    profile, _ = Profile.objects.get_or_create(external_id=chat_id, defaults={'name': message.from_user.username})
    user_id = Message(profile=profile)
    user_id.save()
    bot.send_message(message.chat.id, f'Приветствую тебя {user_name}', reply_markup=kb.markup_menu)


@bot.message_handler(commands=['Ремонт'])
def command_fix(message):
    us_name = message.from_user.first_name
    chat_id = message.chat.id


# Тут работаем с командой help
# @log_errors
# @bot.message_handler(commands=['help'])
# def welcome_help(message):
#     chat_id = message.chat.id
#     text = message.text
#     #bot.send_message(message.chat.id, 'Чем я могу тебе помочь')
#     p, _ = Profile.objects.get_or_create(external_id=chat_id, defaults={'name': message.from_user.username})
#     count = Message.objects.filter(profile=p).count()
#     count = 0
#     bot.send_message(chat_id, text=f'')

# Тут улавливает тексты пользователей
@bot.message_handler(content_types=["text"])
def text(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in user_buy:
        bot.send_message(chat_id, text="Прайc на Apple", reply_markup=kb.inline_kb_sale_menu)

    elif text in user_repear:
        bot.send_message(chat_id, text='Я так понимаю вас интересует ремонт, мы работаем над этим')

    elif text in user_sale:
        bot.send_message(chat_id, text='Я так понимаю вы хотите что-то продать, мы работаем над этим')

    elif text:
        bot.send_message(chat_id, text='Я так понимаю вас интересует ремонт, мы работаем над этим')

    elif text == 'Другое':
        bot.send_message(chat_id, text='Если не нашли то, что искали то напишите ')

    # Передаем текст пользователя в бд
    # text_user, _ = Profile.objects.get_or_create(external_id=chat_id, defaults={'name': message.from_user.username})
    # usermessage = Message(profile=text_user, text=text)
    # usermessage.save()
    # print(message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.message:
            if call.data == 'sale_new_iphone':
                bot.send_message(call.message.chat.id, text="iPhone", reply_markup=kb.inline_kb_chose_new_model_iphone)
            if call.data == 'sale_iphone13':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 13')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone13pro':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 13 Pro')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone13promax':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 13 Pro Max')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone13mini':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 13 Mini')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_12promax':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 12 Pro Max')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_12pro':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 12 Pro')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_12':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 12')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_12mini':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 12 Mini')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_se2':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone SE (2-го поколения)')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')


            elif call.data == 'sale_iphone_11pro':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 11 Pro')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_11promax':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 11 Pro Max')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_11':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 11')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_xs':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone XS')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'iPhone_xsmax':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone XS Max')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_xr':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone XR')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_x':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone X')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_8':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 8')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_8plus':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 8 Plus')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_7':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 7')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_7plus':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone 7 Plus')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')

            elif call.data == 'sale_iphone_se1':
                try:
                    model = Phone.objects.filter(model_phone__iphone_name='iPhone SE (1-го поколения)')
                    bot.send_message(call.message.chat.id, 'Отлично! Отправляю прайс')
                    for item in model:
                        bot.send_message(call.message.chat.id, text=item)
                except Phone.DoesNotExist:
                    bot.send_message(call.message.chat.id, 'Увы! Пока в наличии нет')



    except Exception as e:
        bot.send_message(call.message.chat.id, 'Упс 🤧 что-то не работает ⚙️')
        print(repr(e))


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        bot.polling(none_stop=True, interval=3)

# __gt для сравнений если больше
# __ls если меньше
# __gte больше или равно
# exclude не равно
# __isnull true or false
