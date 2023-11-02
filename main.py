import telebot
from telebot import types

token = ''
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Получить файл")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Получить файл":
        with open('/Users/timurdanilevskij/zxcprojects/files/Примеры инвентаря для начального уровня подготовки.docx', 'rb') as file:
            bot.send_document(message.chat.id, file)
        with open('/Users/timurdanilevskij/zxcprojects/files/Примеры инвентаря для продвинутого уровня подготовки.docx', 'rb') as file:
            bot.send_document(message.chat.id, file)
        with open('/Users/timurdanilevskij/zxcprojects/files/«Пробная тренировка».pdf', 'rb') as file:
            bot.send_document(message.chat.id, file)
        with open('/Users/timurdanilevskij/zxcprojects/files/«Необходимый инвентарь для тренировок».pdf', 'rb') as file:
            bot.send_document(message.chat.id, file)
        with open('/Users/timurdanilevskij/zxcprojects/files/«Как не заболеть после тренировки».pdf', 'rb') as file:
            bot.send_document(message.chat.id, file)






bot.infinity_polling()