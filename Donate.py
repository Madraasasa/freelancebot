from database import *
# from Shop import shop_info
# from bot import main_text
import telebot.types
from buttons import insert_main

def task_get_id(message, bot):
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)

    # print('я тут', get_taskbyid(message.text))
    if message.text.isnumeric():
        if get_taskbyid(message.text):
            bot.send_message(message.chat.id, 'Введите сумму доната, не менее 45 тасков', reply_markup=user_makeup)
            bot.register_next_step_handler(message, task_donate, message.text, bot)
        else:
            bot.send_message(message.chat.id, 'Необходимо ввести числи, которое написано выше "задание id"')
            bot.register_next_step_handler(message, task_get_id, bot)
    else:
        bot.send_message(message.chat.id,  f'Приветствую, {message.from_user.first_name} \nВыберите задание', reply_markup=insert_main(user_makeup))



def task_donate(message, task_id, bot):
    user_makeup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_makeup.row('назад')
    if message.text.isnumeric() and int(message.text) >= 45:
        cur_bal = check_user_balance(message.chat.id)
        if cur_bal >= int(message.text):
            a,b,c  = insert_donate(message.chat.id, task_id, int(message.text))
            print(a, b)
            bot.send_message(message.chat.id, b+ f'\nВаш текущий баланс {c}')
        else:
            bot.send_message(message.chat.id, 'Ваш баланс не достаточен\n Купите тасков в разделе "магазин"', reply_markup=user_makeup)

           # bot.register_next_step_handler(message, main_text)
    else:
        if message.text == 'назад':
            task_get_id(message, bot)
        else:
            bot.send_message(message.chat.id, 'Введите сумму доната, не менее 45 тасков', reply_markup=user_makeup)
            bot.register_next_step_handler(message, task_donate,task_id, bot)