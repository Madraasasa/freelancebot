import telebot
from buttons import *
from TaskTemplate import *
from TaskerInfo import *
from Shop import *
from database import *
from Donate import *
from MyTask import get_type
from telegraph import create_telegraph
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
    # print(main_buttons)
    print(message.message_id)
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
        # создать задание
        bot.send_message(message.chat.id, 'Выберите сложность', reply_markup=insert_level(user_makeup))
        bot.register_next_step_handler(message, get_level)
    elif message.text == main_buttons[2]:
        # стать исполнителем
        user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
        if getuserinfo(message.chat.id):
            bot.send_message(message.chat.id, 'Выберите сложность', reply_markup=insert_level(user_makeup))
            bot.register_next_step_handler(message, get_levels_maker, 1)
        else:
            bot.send_message(message.chat.id, 'Введите имя', reply_markup=user_makeup)
            bot.register_next_step_handler(message, name_tasker, bot)
    elif message.text == main_buttons[5]:
        # магазин
        bot.send_message(message.chat.id, 'Введите лот', reply_markup=insert_lots(user_makeup))
        bot.register_next_step_handler(message, shop_info, bot)
    elif message.text == main_buttons[1]:
        # стать зрителем
        bot.send_message(message.chat.id, 'Выберите сложность', reply_markup=insert_level(user_makeup))
        bot.register_next_step_handler(message, get_levels_from)
    elif message.text == main_buttons[3]:
        # мои задания
        user_makeup.row('Я зритель')
        user_makeup.row('Я исполнитель')
        user_makeup.row('назад')
        bot.send_message(message.chat.id, 'Выберите тип заданий', reply_markup=user_makeup)
        bot.register_next_step_handler(message, get_type, bot)
    elif message.text == main_buttons[4]:
        # FAQ
        bot.send_message(message.chat.id, create_telegraph(), reply_markup=insert_main(user_makeup))
    elif message.text == main_buttons[6]:
        # служба поддержки
        user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_makeup.row('назад')
        bot.send_message(message.chat.id, 'Введите ваше сообщение', reply_markup=user_makeup)
        bot.register_next_step_handler(message, save_message)
    elif message.text == main_buttons[7]:
        # аккаунт
        if getuserinfo(message.chat.id):
            user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_makeup.row('редактировать')
            user_makeup.row('назад')
            bot.send_message(message.chat.id, getuserinfo(message.chat.id), reply_markup=user_makeup)
            bot.register_next_step_handler(message, edit_account)
        else:
            user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_makeup.row('назад')
            bot.send_message(message.chat.id, 'Введите имя', reply_markup=user_makeup)
            # bot.register_next_step_handler(message, name_tasker, bot)
    # print(message.text)
    else:
        bot.send_message(message.chat.id, 'Выберите один из пунктов', reply_markup=insert_main(user_makeup))
        bot.register_next_step_handler(message, main_text)

def edit_account(message):
    if message.text == 'редактировать':
        bot.send_message(message.chat.id, 'Введите имя')
        bot.register_next_step_handler(message, name_tasker, bot)
    elif message.text == 'назад':
        handle_text(message)


def get_levels_from(message, status=0):
    # get_tasks_by_level
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
    # print(message.text)
    remove_makeup = telebot.types.ReplyKeyboardRemove()

    if message.text in levels:
        # Проверка сложности
        bot.send_message(message.chat.id, select_task_by(message.text, status), parse_mode='markdown', reply_markup=remove_makeup)

        if select_task_by(message.text, status) != 'Заданий для данного случая нет':
            bot.send_message(message.chat.id, 'Введите id задания, необходимо ввести число')
            bot.register_next_step_handler(message, task_get_id, bot)
        else:
            handle_text(message)
    elif message.text == 'назад':
        handle_text(message)
    else:
        handle_text(message)


def get_levels_maker(message, status=1):
    # get_tasks_by_level
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
    # print(message.text)

    if message.text in levels:
        # Проверка сложности
        bot.send_message(message.chat.id, select_task_by(message.text, status), parse_mode='markdown', reply_markup=insert_main(user_makeup))

        if select_task_by(message.text, status) != 'Заданий для данного случая нет':
            bot.send_message(message.chat.id, 'Введите id задания')
            bot.register_next_step_handler(message, task_get_id, bot)
        else:
            handle_text(message)
    elif message.text == 'назад':
        handle_text(message)
    else:
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


def save_message(message):
    if message.text !='назад':
        a = save_message_todb(message.message_id, message.chat.id, message.text)
        if a:
            bot.send_message(message.chat.id, 'Вам ответят в ближайшее время')
        else:
            bot.send_message(message.chat.id, 'Произошла ошибка повторите позже')
        bot.register_next_step_handler(message, main_text)

if __name__ == '__main__':
    bot.polling()


