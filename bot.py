import asyncio
import telebot
from telebot import types
import json
import logging
import os

from telebot.async_telebot import AsyncTeleBot

# Настройка логирования и сохранение логов в папку logs
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(
    filename=os.path.join("logs", "bot.log"),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# Загрузка текстов из JSON файла
with open("text.json", "r", encoding="utf-8") as f:
    text = json.load(f)

# Токен бота
bot = AsyncTeleBot("8409256017:AAE0OD0ETFLC-jWUSbw2TncCwKLwSyCZoeE", parse_mode=None)

# Создание inline-клавиатуры
def get_inline_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(text["buttons"]["calculator_cn"], callback_data="calculator_cn"),
        types.InlineKeyboardButton(text["buttons"]["calculator_int"], callback_data="calculator_int"),
        types.InlineKeyboardButton(text["buttons"]["course"], callback_data="course"),
        types.InlineKeyboardButton(text["buttons"]["price_cn"], callback_data="price_cn"),
        types.InlineKeyboardButton(text["buttons"]["contacts"], callback_data="contacts"),
        types.InlineKeyboardButton(text["buttons"]["faq"], callback_data="faq"),
        types.InlineKeyboardButton(text["buttons"]["commission"], callback_data="commission"),
        types.InlineKeyboardButton(text["buttons"]["test"], callback_data="test")
    )
    return markup

@bot.message_handler(commands=["info", "start"])
async def send_welcome_message(message):
    await bot.send_message(
        message.chat.id,
        text["welcome"],
        reply_markup=get_inline_markup()
    )

# Обработка нажатий кнопок
@bot.callback_query_handler(func=lambda call: True)
async def handle_inline_buttons(call):
    data = call.data
    answers = {
        "calculator_cn": text["answers"]["calculator_cn_answer"],
        "calculator_int": text["answers"]["calculator_int_answer"],
        "course": text["answers"]["course_answer"],
        "price_cn": text["answers"]["price_cn_answer"],
        "contacts": text["answers"]["contacts_answer"],
        "faq": text["answers"]["faq_answer"],
        "commission": text["answers"]["commission_answer"],
        "test": text["answers"]["test_answer"]
    }
    answer = answers.get(data, "Неизвестная команда.")
    await bot.send_message(call.message.chat.id, answer, reply_markup=get_inline_markup(), parse_mode="Markdown")
    await bot.answer_callback_query(call.id)

if __name__ == "__main__":
    
    # Основной цикл бота
    async def main():
        await bot.infinity_polling()

    asyncio.run(main())


