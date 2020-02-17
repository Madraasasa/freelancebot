# from bot import bot


def task_name(message, bot):
    bot.send_message(message.chat.id, 'Введите описание')
    print(message.text)
    bot.register_next_step_handler(message, task_desc, message.text, bot)


def task_desc(message, name, bot):
    bot.send_message(message.chat.id, 'Введите сумму оплаты')
    bot.register_next_step_handler(message, task_sum, name, message.text, bot)


def task_sum(message, name, desc, bot):
    bot.send_message(message.chat.id, 'Введите пол исполнителя')
    bot.register_next_step_handler(message, task_sex, name, desc,message.text, bot)


def task_sex(message, name, desc, sum, bot):
    # print(name, desc, sum, message.text)
    bot.send_message(message.chat.id, 'Введите возраст')
    bot.register_next_step_handler(message, task_age, name, desc, sum, message.text, bot)


def task_age(message, name, desc, sum, sex, bot):
    bot.send_message(message.chat.id, 'Введите срок выбора исполнителя')
    bot.register_next_step_handler(message, task_date_tasker, name, desc, sum,sex,message.text, bot)


def task_date_tasker(message, name, desc, sum, sex,age, bot):
    bot.send_message(message.chat.id, 'Введите срок выполнения')
    bot.register_next_step_handler(message, task_date, name, desc, sum, sex, age, message.text, bot)


def task_date(message, name, desc, sum, sex, age, tasker_dt, bot):
    bot.send_message(message.chat.id, f'{name}, {desc}, {sum}, {sex},{age}, {tasker_dt}, {message.text}')
    print(name, desc, sum, sex,age, tasker_dt, message.text)

