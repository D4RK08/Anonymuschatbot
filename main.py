from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from telegram import Bot

TOKEN = "7195518842:AAHFDbmhEfIK6PTiVuxnezlMmTa-l7n8ttM"

def start(update, context):
   update.message.reply_text("Ciao")


bot = Bot(token=TOKEN)
updater = Updater(bot=bot)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
