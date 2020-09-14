#!/usr/bin/env python
import random
import pickle

import telebot
from telebot import types
from telebot.types import Message

TOKEN = '1280787634:AAEdtygfc6x6tEtxmJnL2_SRqnc7WKmF89c'
STICKER_ID = 'CAACAgIAAxkBAAM1X17aAXBfO5mlXXyDQmDbK6NSomkAAhMFAAJ8BQcbiV4bVmg06GsbBA' # лови двоечку
STICKER_ID2 = 'CAACAgIAAxkBAAM5X17ahOJGKOnF7MjEewoQITRDVkUAAggFAAJ8BQcbMyyxQklu1RUbBA' # привет рабы системы
STICKER_ID3 = 'CAACAgIAAxkBAAM6X17bvbVKDSJLcEdfPYs1rY1KSQwAAhwFAAJ8BQcblxtvdZORb4EbBA' #чьих будешь
STICKER_ARMY = 'CAACAgIAAxkBAAObX17llFQp_nLvV3tIzFf8HXiogdAAAgsFAAJ8BQcbfaTKf9BMucgbBA' #прямо по курсу

bot = telebot.TeleBot(TOKEN)

USERS = set()


@bot.message_handler(commands=['start'])
def command_handler(message: Message):
    bot.reply_to(message, 'Погнали !!! ')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    print(message.from_user.id)
    if '300' in message.text:
        bot.reply_to(message, 'Отсоси у тракториста, с уважением :)')
        return
    if 'Привет' in message.text:
        bot.send_sticker(message.chat.id, STICKER_ID2)
        return
    if 'привет' in message.text:
        bot.send_sticker(message.chat.id, STICKER_ID)
        return
    if 'help' in message.text:
        bot.reply_to(message, 'Бог поможет :(')
        return
    if 'ты кто' in message.text:
        bot.reply_to(message, 'Иван Фёдорович Крузенштерн - человек и пароход')
        return
    if 'как дела' in message.text:
        bot.reply_to(message, 'Нормуль!')
        bot.send_sticker(message.chat.id, STICKER_ID3)
        return
    if 'анекдот' in message.text:
        bot.reply_to(message, 'Прочтите Нидерланды с ударением на Ы и почувствуйте запах и простор казахской степи, терпкий вкус кумыса, уют юрты…')
        bot.send_sticker(message.chat.id, STICKER_ID)
        return
    if 'что умеешь' in message.text:
        bot.send_sticker(message.chat.id, STICKER_ID)
        return
    if 'что будет дальше' in message.text:
        bot.send_sticker(message.chat.id, STICKER_ARMY)
        return


#@bot.message_handler(content_types=['sticker'])
#def sticker_handler(message: Message):
    #print(message.sticker)
    #print(message)
    #bot.send_sticker(message.chat.id, STICKER_ID)


#@bot.inline_handler(lambda query: query.query)
#def query_text(inline_query):
#    print(inline_query)
#    try:
#        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
#        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
#        bot.answer_inline_query(inline_query.id, [r, r2])
#    except Exception as e:
 #       print(e)


bot.polling(timeout=60)
