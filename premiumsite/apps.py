from django.apps import AppConfig
import asyncio

from telegramBot.management.commands.bot import start


class PremiumsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'premiumsite'

    def ready(self):
        from telegramBot import bot
        bot.start()




