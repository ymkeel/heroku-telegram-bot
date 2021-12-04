import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from newsapi import NewsApiClient

#Creamos un archivo env.py para guardar nuestras credenciales
# from env import NEWS_API_KEY, BOT_KEY
BOT_KEY = os.environ['BOT_KEY']

#Creamos la intefaz con la API de Noticas.
# newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def start(update, context):
    # Configuramos el comando start para enviar un mensaje de bienvenida
    update.message.reply_text('Bienvenido, escribe algo para comenzar a buscar noticias.')


def help(update, context):
    # Configuramos el comando help para enviar un mensaje con instrucciones
    update.message.reply_text('Hola escriba algunas palabras clave para empezar a buscar noticias en la web.')


def echo(update, context):
    # Configuramos para enviar un mensaje con el texto que envió el usuario, aquí es donde va a ir toda la lógica de nuestro bot
    update.message.reply_text(update.message.text)


def main():
    # Creamos el Updater y le pasamos el token de nuestro bot. Este se encargará de manejar las peticiones de los usuarios.
    updater = Updater(BOT_KEY, use_context=True)

    # Obtenemos el Dispatcher para crear los comandos
    dp = updater.dispatcher

    # Creamos el comando /start y definimos que se ejecute este mismo método
    dp.add_handler(CommandHandler("start", start))
    # Creamos el comando /help y definimos que se ejecute el método help
    dp.add_handler(CommandHandler("help", help))

    # De no ejecutarse ninguno de los anteriores asumimos que el usuario escribió algo y ejecutamos el método echo que nos va a permitir obtener los campos de las búsquedas del usuario
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()