from django.apps import AppConfig


class PremiumsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'premiumsite'

    def ready(self):
        import os
        from telegramBot.management.commands import bot
        # from . import jobs
        # RUN_MAIN check to avoid running the code twice since manage.py runserver runs 'ready' twice on startup
        if os.environ.get('RUN_MAIN', None) != 'true':
            try:
                bot.polling(none_stop=True, timeout=123, interval=2)
            except Exception as e:
                print(f'Error {e}')




        # Your function to run the bot goes here
