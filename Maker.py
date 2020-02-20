from database import *
def task_from_maker(message, bot):
    # print('я тут', get_taskbyid(message.text))
    if get_taskbyid(message.text, status=1):
        bot.send_message(message.chat.id, 'Ваша кандидатура добавлена')

        bot.register_next_step_handler(message, 'asasas', bot)
    else:
        bot.register_next_step_handler(message, task_from_maker, bot)

