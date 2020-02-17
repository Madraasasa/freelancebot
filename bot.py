import telebot
from buttons import *
from TaskTemplate import *
from TaskerInfo import *
from Shop import *
# from db import *
# from parse_movie import *
import random
import enum
bot = telebot.TeleBot('986722664:AAEx7v_gw8gZvKS7VEZojP2P5JdKfBmoOEQ')
# admin_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
    bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name} \nВыберите задание', reply_markup=insert_main(user_makeup))
    if message.text in main_buttons:
        main_text(message)
    else:
        bot.register_next_step_handler(message, handle_text)


def main_text(message):
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
    if message.text not in main_buttons:
        # bot.send_message(message.chat.id)
        bot.register_next_step_handler(message, handle_text)
    if message.text == 'создать задание':
        bot.send_message(message.chat.id, 'Выберите сложность', reply_markup=insert_level(user_makeup))
        bot.register_next_step_handler(message, get_level)
    elif message.text == 'стать исполнителем':
        bot.send_message(message.chat.id, 'Введите имя')
        bot.register_next_step_handler(message, name_tasker, bot)
    elif message.text == 'магазин':
        bot.send_message(message.chat.id, 'Введите лот', reply_markup=insert_lots(user_makeup))
        bot.register_next_step_handler(message, shop_info, bot)
    elif message.text == 'стать зрителем':
        bot.send_message(message.chat.id, 'Выберите сложность', reply_markup=insert_level(user_makeup))
        bot.register_next_step_handler(message, get_levels_from)
    elif message.text == 'мои задания':
        user_makeup.row('Я зритель')
        user_makeup.row('Я исполнитель')
        bot.send_message(message.chat.id, 'Выберите тип заданий', reply_markup=user_makeup)
    elif message.text == 'FAQ':
        bot.send_message(message.chat.id, 'FAQ')
    elif message.text == 'служба поддержки':
        bot.send_message(message.chat.id, 'Служба поддержки не доступна')
    # print(message.text)


def get_levels_from(message):
    # get_tasks_by_level
    user_makeup = telebot.types.ReplyKeyboardRemove()
    if message.text in levels:
        bot.send_message(message.chat.id, f'Список заданий для уровня {message.text}', reply_markup=user_makeup)


def get_level(message):
    user_makeup = telebot.types.ReplyKeyboardRemove()
    if message.text in levels:
        # print(message.text)
        bot.send_message(message.chat.id, 'Введите название', reply_markup=user_makeup)
        bot.register_next_step_handler(message, task_name, bot)


if __name__ == '__main__':
    bot.polling()


