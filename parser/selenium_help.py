from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
import telegram

from parser import get_html_content, parse

bot = telegram.Bot('776721679:AAHASdfY35uawbgdW7hjjBMYN63gg-Ut-gE')

CHOISE = 1


def start(bot,update):
    update.message.reply_text(f'Привет {update.message.from_user.last_name}')


def hello(bot, update):
    update.message.reply_text('Hi!')


def action(update, context):
    update.message.reply_text('Попарсим?)')
    keys = [['Statr', 'No']]
    print('kkkkk')
    update.message.reply_text(reply_markup=ReplyKeyboardMarkup(keys))
    return CHOISE



def parser(bot, update):
    update.message.reply_text(f'Пагодь')
    html = get_html_content()
    table = parse(html)
    update.message.reply_text(f'От')
    update.message.reply_text(f'{table}')


def main():

    updater = Updater(bot=bot,  request_kwargs=True)

    base_handler = updater.dispatcher
    base_handler.add_handler(CommandHandler("start", start))
    base_handler.add_handler(CommandHandler("hello", hello))
    base_handler.add_handler(CommandHandler("parser", parser))
    base_handler.add_handler(RegexHandler('^(Start|No)$', action))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()