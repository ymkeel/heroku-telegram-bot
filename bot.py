from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# BOT_KEY = os.environ['BOT_KEY']

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5060494830:AAHYMbYNGz9gTW73yCKRSgxB0UgLPPZlcK4')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()