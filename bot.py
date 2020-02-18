import telebot
from buttons import *
from TaskTemplate import *
from TaskerInfo import *
from Shop import *
from database import *
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
    print(main_buttons)
    if message.text in main_buttons:
        main_text(message)
    else:
        # print(message.text)
        bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name} \nВыберите задание',
                         reply_markup=insert_main(user_makeup))
        bot.register_next_step_handler(message, handle_text)


def main_text(message):
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
    # print(main_buttons)
    if message.text not in main_buttons:
        # bot.send_message(message.chat.id)
        bot.register_next_step_handler(message, handle_text)
    # print(message.text)
    if message.text == main_buttons[0]:
        bot.send_message(message.chat.id, 'Выберите сложность', reply_markup=insert_level(user_makeup))
        bot.register_next_step_handler(message, get_level)
    elif message.text == main_buttons[2]:
        user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_makeup.row('назад')
        bot.send_message(message.chat.id, 'Введите имя',reply_markup=user_makeup)
        bot.register_next_step_handler(message, name_tasker, bot)
    elif message.text == main_buttons[5]:
        bot.send_message(message.chat.id, 'Введите лот', reply_markup=insert_lots(user_makeup))
        bot.register_next_step_handler(message, shop_info, bot)
    elif message.text == main_buttons[1]:
        bot.send_message(message.chat.id, 'Выберите сложность', reply_markup=insert_level(user_makeup))
        bot.register_next_step_handler(message, get_levels_from)
    elif message.text == main_buttons[3]:
        user_makeup.row('Я зритель')
        user_makeup.row('Я исполнитель')
        bot.send_message(message.chat.id, 'Выберите тип заданий', reply_markup=user_makeup)
    elif message.text == main_buttons[4]:
        bot.send_message(message.chat.id, 'FAQ')
    elif message.text == main_buttons[6]:
        bot.send_message(message.chat.id, 'Служба поддержки не доступна')
    # print(message.text)


def get_levels_from(message):
    # get_tasks_by_level
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
    # print(message.text)

    if message.text in levels:
    # aaa = select_task_by_level(message.text)
    # print(aaa)
        bot.send_message(message.chat.id, select_task_by_level(message.text), parse_mode='markdown', reply_markup=insert_main(user_makeup))
    elif message.text == 'назад':
        handle_text(message)


def get_level(message):
    user_makeup = telebot.types.ReplyKeyboardRemove()
    print(message.text)
    if message.text in levels:
        # print(message.text)
        bot.send_message(message.chat.id, 'Введите название', reply_markup=user_makeup)
        bot.register_next_step_handler(message, task_name, message.text, bot)

    elif message.text == 'назад':
        print('я тут')
        handle_text(message)


def name_tasker(message, bot):
    if message.text == 'назад':
        handle_text(message)
    else:
        bot.send_message(message.chat.id, 'Введите фамилию')
        bot.register_next_step_handler(message, lastname_tasker, message.text, bot)




if __name__ == '__main__':
    bot.polling()


