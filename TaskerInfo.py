def name_tasker(message, bot):
    bot.send_message(message.chat.id, 'Введите фамилию')
    print(message.text)
    bot.register_next_step_handler(message, lastname_tasker, message.text, bot)


def lastname_tasker(message, name, bot):
    bot.send_message(message.chat.id, 'Введите возраст')
    bot.register_next_step_handler(message, age_tasker, name, message.text, bot)


def age_tasker(message, name, lastname, bot):
    bot.send_message(message.chat.id, 'Введите город')
    bot.register_next_step_handler(message, city_tasker, name, lastname, message.text, bot)


def city_tasker(message, name, lastname, age, bot):
    bot.send_message(message.chat.id, 'Введите пол')
    bot.register_next_step_handler(message, sex_tasker, name, lastname, age, message.text, bot)


def sex_tasker(message, name, lastname, age, city,bot):
    bot.send_message(message.chat.id, 'Введите о себе')
    bot.register_next_step_handler(message, desc_tasker, name, lastname, age, city,message.text, bot)


def desc_tasker(message, name, lastname, age, city,sex,bot):
    bot.send_message(message.chat.id, f'{name} {lastname} {age} {city} {sex} {message.text}')
    print(name, lastname, age, city, sex, message.text)