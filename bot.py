import telebot
from telebot import types 
import json
import logging

# Логирование
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Выводит всю отладочную информацию в консоль

# Загрузка текстов из JSON файла
with open("text.json", "r", encoding="utf-8") as f:
    text = json.load(f)

# Токен бота
bot = telebot.TeleBot("Your token here", parse_mode=None)

# Создание клавиатуры и указание её параметров
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

# Кнопки
itembtncalc_cn = types.KeyboardButton(text["buttons"]["calculator_cn"])
itembtncalc_int = types.KeyboardButton(text["buttons"]["calculator_int"])
itembtncourse = types.KeyboardButton(text["buttons"]["course"])
itembtnprice_cn = types.KeyboardButton(text["buttons"]["price_cn"])
itembtnfaq = types.KeyboardButton(text["buttons"]["faq"])
itembtncont = types.KeyboardButton(text["buttons"]["contacts"])
itembtncom = types.KeyboardButton(text["buttons"]["commission"])
itembtntst = types.KeyboardButton(text["buttons"]["test"])

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == text["buttons"]["calculator_cn"]:
        bot.send_message(message.chat.id, text["answers"]["calculator_cn_answer"], reply_markup=markup, parse_mode="Markdown")
    elif message.text == text["buttons"]["course"]:
        bot.send_message(message.chat.id, text["answers"]["course_answer"], reply_markup=markup, parse_mode="Markdown")
    elif message.text == text["buttons"]["faq"]:
        bot.send_message(message.chat.id, text["answers"]["faq_answer"], reply_markup=markup, parse_mode="Markdown")
    elif message.text == text["buttons"]["contacts"]:
        bot.send_message(message.chat.id, text["answers"]["contacts_answer"], reply_markup=markup, parse_mode="Markdown")
    elif message.text == text["buttons"]["price_cn"]:
        bot.send_message(message.chat.id, text["answers"]["price_cn_answer"], reply_markup=markup, parse_mode="Markdown")
    elif message.text == text["buttons"]["calculator_int"]:
        bot.send_message(message.chat.id, text["answers"]["calculator_int_answer"], reply_markup=markup, parse_mode="Markdown")
    elif message.text == text["buttons"]["test"]:
        bot.send_message(message.chat.id, text["answers"]["test_answer"], reply_markup=markup, parse_mode="Markdown")
    elif message.text == text["buttons"]["commission"]:
        bot.send_message(message.chat.id, text["answers"]["commission_answer"], reply_markup=markup, parse_mode="Markdown")
    


# Расположение кнопок по сетке
markup.row(itembtncalc_cn, itembtncalc_int, itembtncourse, itembtnprice_cn)
markup.row(itembtncont, itembtnfaq, itembtncom)

# Основное тело бота
@bot.message_handler(commands=["info"])
def send_welcome_message(message):
   bot.send_message(
       message.chat.id,
       text["welcome"],
       reply_markup=markup
   )
   
# Основной цикл бота
bot.infinity_polling()


