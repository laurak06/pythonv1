import telebot

from parse import parsing

bot = telebot.TeleBot('7928041636:AAEbdJiGFBTidvseRwSpWnRv-9WK2XrkmNQ')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

button1 = telebot.types.KeyboardButton('Ноутбуки')
button2 = telebot.types.KeyboardButton('Телефоны')

keyboard.add(button1, button2)


@bot.message_handler(commands=['start'])
def start_msg(message):
    message2 = bot.send_message(message.chat.id, 'привет я могу спарсить страницу kivano.kg', reply_markup=keyboard)
    bot.register_next_step_handler(message2, handler)


def handler(message):
    if message.text.lower() == 'ноутбуки':
        laptops = [' '.join(i) for i in parsing('noutbuki')]
        laptops = '\n\n'.join(laptops)
        bot.send_message(message.chat.id, laptops)
    elif message.text.lower() == 'телефоны':
        telephones = [' '.join(i) for i in parsing('mobilnye-telefony')]
        telephones = '\n\n'.join(telephones)
        bot.send_message(message.chat.id, telephones)


bot.polling(none_stop=True)
