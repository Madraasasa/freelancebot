# from bot import bot
from database import *
from telebot import types
from buttons import *

def task_name(message,level, bot):
    bot.send_message(message.chat.id, 'Введите описание')
    print(message.text)
    bot.register_next_step_handler(message, task_desc,level, message.text, bot)


def task_desc(message,level, name, bot):
    bot.send_message(message.chat.id, 'Введите сумму оплаты')
    bot.register_next_step_handler(message,  task_sum, level, name, message.text, bot)


def task_sum(message, level, name, desc, bot):
    if message.text.isnumeric():
        bot.send_message(message.chat.id, 'Введите пол исполнителя, (мужской, женский, любой)')
        bot.register_next_step_handler(message, task_sex, level, name, desc, message.text, bot)
    else:
        bot.send_message(message.chat.id, 'Неправильная сумма оплаты')
        bot.register_next_step_handler(message, task_sum, level, name, desc, bot)


def task_sex(message,level, name, desc, sum, bot):
    # print(name, desc, sum, message.text)
    if message.text.lower() not in ['мужской', 'женский', 'любой']:
        bot.send_message(message.chat.id, 'Неправильный пол исполнителя\nВведите пол исполнителя, (мужской, женский, любой)')
        bot.register_next_step_handler(message, task_sex, level, name, desc,sum, bot)
    else:
        bot.send_message(message.chat.id, 'Введите возраст, данного формата(возраст-возраст)')
        bot.register_next_step_handler(message, task_age, level, name, desc, sum, message.text.lower(), bot)


def task_age(message,level, name, desc, sum, sex, bot):
    interval = message.text.split('-')
    print(interval)
    if interval[0] and interval[1] and len(interval) == 2:
        bot.send_message(message.chat.id, 'Введите срок выполнения, не менее 5 дней')
        bot.register_next_step_handler(message, task_date_tasker, level, name, desc, sum, sex, message.text, bot)
    else:
        bot.send_message(message.chat.id, 'Введите возраст, данного формата(возраст-возраст)')
        bot.register_next_step_handler(message, task_age, level, name, desc, sum, message.text, bot)


def task_date_tasker(message, name,level, desc, sum, sex, age, bot):
    if message.text.isnumeric() and int(message.text) >= 5:
        bot.send_message(message.chat.id, 'Введите срок выполнения, не менее 4 дней')
        bot.register_next_step_handler(message, task_date, level, name, desc, sum, sex, age, message.text, bot)
    else:
        bot.send_message(message.chat.id, 'Введите срок выбора исполнителя, не менее 5 дней')
        bot.register_next_step_handler(message, task_date_tasker, level, name, desc, sum, sex, message.text, bot)


def task_date(message, name,level, desc, sum, sex, age, tasker_dt, bot):
    if message.text.isnumeric() and int(message.text) > 4:
        user_makeup = types.ReplyKeyboardMarkup(True, False)
        a,b = insert_task(name, desc, sum, sex,age, tasker_dt, message.text, level, message.chat.id)
        # print(name, desc, sum, sex,age, tasker_dt, message.text)
        bot.send_message(message.chat.id, f'Задание ID -{a}\n {name}, {desc}, {sum}, {sex},{age}, {tasker_dt}, {message.text}')
        bot.send_message(message.chat.id, b, reply_markup=insert_main(user_makeup))
    else:
        bot.send_message(message.chat.id, 'Введите срок выполнения, не менее 4 дней')
        bot.register_next_step_handler(message, task_date, level, name, desc, sum, sex, age, message.text, bot)

