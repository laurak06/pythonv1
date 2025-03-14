import telebot
from telebot import types

bot = telebot.TeleBot('7928041636:AAEbdJiGFBTidvseRwSpWnRv-9WK2XrkmNQ')

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('info')
# button2 = types.KeyboardButton()

keyboard.add(button1)


@bot.message_handler(commands=['start', 'hi'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'hi, write a message, i will put in your info')
    bot.register_next_step_handler(message, save_info)


def save_info(message):
    try:
        with open('user_info.txt', 'a') as file:
            info = message.text
            file.write(info + '\n')
    except:
        bot.send_message(message.chat.id, 'something gone wrong, try again')
    else:
        bot.send_message(message.chat.id, 'everything loaded', reply_markup=keyboard)
    finally:
        print('ok')


@bot.message_handler(content_types=['text'])
def sen_info(message):
    with open('user_info.txt') as file:
        bot.send_document(message.chat.id, file)


bot.polling(non_stop=True, interval=0)
