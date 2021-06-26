import telebot # importamos la libreria de telebot

bot = telebot.TeleBot('') #anadimos el token

@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "Hola, como estas?")
    print("Mandaron hola o hi")

@bot.message_handler(commands=['nombre', 'name'])
def nombre(mensaje):
    bot.reply_to(mensaje, "Mi nombre es Filomeno")
    print("Mandaron nombre o name")

bot.polling()