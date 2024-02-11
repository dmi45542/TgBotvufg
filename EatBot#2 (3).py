import telebot
import requests
from translate import Translator
from telebot import types

bot = telebot.TeleBot('6843812944:AAGriOV0cxVXeEeTj8VbA3NCClB70Z_f2pk')


@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Рецепт')
    markup.add(item)
    bot.send_message(m.chat.id, 'Бот заработал, ура', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(m):
    print(1)
    if m.text.strip() == 'Рецепт':
        messg = bot.send_message(m.chat.id, "Ваш запрос:")
        bot.register_next_step_handler(messg, recept)


def recept(m):
    query = m.text
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': '7r1fPNwDFxchZr3GmHvzJg==s4b3PDtRutOrooAc'})
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)

    if response.status_code == requests.codes.ok:
        print(response.text)
        txt = response.text
        txt1 = eval(txt)[0]
        # translator = Translator(from_lang='English', to_lang='Russian')
        # txt_En1 = txt1['ingredients']
        # print(txt_En1 )
        # txt_ru = translator.translate(txt_En1)
        bot.send_message(m.chat.id, txt1['ingredients'])
    else:
        print('Error:', response.status_code, response.text)


bot.polling(none_stop=True, interval=0)
