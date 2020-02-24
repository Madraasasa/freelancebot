from database import get_my_task, get_do_task
from telebot import types
from buttons import insert_main

def get_type(message, bot):
    if message.text.lower() == 'я зритель':
        s = get_my_task(message.chat.id)
        bot.send_message(message.chat.id, s)
    elif message.text.lower() == 'я исполнитель':
        s = get_do_task(message.chat.id)
        if s:
            bot.send_message(message.chat.id, s)
        else:
            bot.send_message(message.chat.id, 'Вы не выбраны исполнителем')
    elif message.text == 'назад':
        user_makeup = types.ReplyKeyboardMarkup(True, False)
        bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name} \nВыберите задание',
                         reply_markup=insert_main(user_makeup))
    else:

        bot.send_message(message.chat.id, 'Выберите одну из кнопок')
        bot.register_next_step_handler(message, get_type, bot)