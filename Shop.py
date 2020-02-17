from bot import main_text

lots = ['1 лот - 50 р - 45 тасков', '2 лот - 100 р - 90 тасков', '3 лот - 300 р - 270 тасков', '4 лот - 700 р - 610 тасков', '5 лот - 1500 р - 1350 тасков', '6 лот - 5000 р - 4500 тасков']


def insert_lots(user_markup):
    for i in lots:
        user_markup.row(i)
    return user_markup


def shop_info(message, bot):
    if message.text in lots:
        bot.send_message(message.chat.id, f'Вы купили лот, {message.text}')
    else:
        main_text(message)


