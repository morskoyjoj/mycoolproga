import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
token = os.getenv("token")
bot = AsyncTeleBot(token, parse_mode="HTML")
########################################################################################################################
list_buttons = ["/C", "/C#", "/D", "/D#", "/E", "/F", "/F#", "/G", "/G#", "/A", "/A#", "/B", "/Cm", "/C#m", "/Dm", "/D#m", "/Em", "/Fm", "/Gm", "/G#m", "/Am", "/A#m", "/Bm", "/stop"]
list_buttons_hendler = list(list_buttons)

for i in range(len(list_buttons_hendler)):
    list_buttons_hendler[i] = list_buttons_hendler[i].replace('/','')

print(list_buttons_hendler)

chords = [""]

@bot.message_handler(commands=["help", "start"])
async def send_welcome(message):
    print(message.text)
    chat_id = message.from_user.id
    list_buttons = "/start", "/help", "/about", "/harmony"
    await bot.send_message(chat_id, "Выберите вариант: /help - Инструкция, /about - Об авторе, /harmony - Запуск программы", reply_markup=generate_reply_keyboard(list_buttons, 2))





def generate_reply_keyboard(list_buttons, row):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_buttons, row_width=row)
    return markup

@bot.message_handler(commands=["knopki"])
async def send_welcome(message):
    chat_id = message.from_user.id


@bot.message_handler(commands=["harmony"])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, "Выберите аккорд", reply_markup=generate_reply_keyboard(list_buttons, 5))

@bot.message_handler(commands=list_buttons_hendler)
async def send_welcome(message):
    if message.text == "/C":
        print('Выберите аккорд')
        chords.append("C")
    elif message.text == "/C#":
        print('Выберите аккорд')
        chords.append("C#")
    elif message.text == "/D":
        print('Выберите аккорд')
        chords.append("D")
    elif message.text == "/D#":
        print('Выберите аккорд')
        chords.append("D#")
    elif message.text == "/E":
        print('Выберите аккорд')
        chords.append("E")
    elif message.text == "/F":
        print('Выберите аккорд')
        chords.append("F")
    elif message.text == "F#":
        print('Выберите аккорд')
        chords.append("F#")
    elif message.text == "/G":
        print('Выберите аккорд')
        chords.append("G")
    elif message.text == "/G#":
        print('Выберите аккорд')
        chords.append("G#")
    elif message.text == "/A":
        print('Выберите аккорд')
        chords.append("A")
    elif message.text == "/A#":
        print('Выберите аккорд')
        chords.append("A#")
    elif message.text == "/B":
        print('Выберите аккорд')
        chords.append("B")
    elif message.text == "/stop":
        chat_id = message.from_user.id
        await bot.send_message(chat_id, chords)

@bot.message_handler(commands=["chords"])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, chords)

@bot.message_handler(commands=["about"])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<a href= "tg://user?id=1441797781">eto ya</a>')
    await bot.send_message(chat_id, '<a href= "https://github.com/morskoyjoj">github</a>')

    await bot.send_message(chat_id, '<a href="https://rb.gy/06z43">полезноео видево</a>', disable_web_page_preview=True)


########################################################################################################################
import asyncio

asyncio.run(bot.polling())