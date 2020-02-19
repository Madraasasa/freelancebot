from database import *


def task_get_id(message, bot):
    # print('я тут', get_taskbyid(message.text))
    if get_taskbyid(message.text):
        bot.send_message(message.chat.id, 'Введите сумму доната, не менее 45 тасков')
        bot.register_next_step_handler(message, task_donate, message.text, bot)
    else:
        bot.register_next_step_handler(message, task_get_id, bot)

def task_donate(message, task_id, bot):
    if message.text.isnumeric() and int(message.text) >= 45:
        a,b = insert_donate(message.chat.id, task_id, int(message.text))
        print(a, b)

    else:
        bot.send_message(message.chat.id, 'Введите сумму доната, не менее 45 тасков')
        bot.register_next_step_handler(message, task_donate,task_id, bot)