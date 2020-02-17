main_buttons = ['создать задание', 'стать зрителем', 'стать исполнителем', 'мои задания', 'FAQ', 'магазин','служба поддержки']
levels = ['lite', 'medium', 'hard', 'extra']


def insert_main(user_markup):
    main_buttons = [['создать задание', 'стать зрителем'], ['стать исполнителем', 'мои задания'], ['FAQ', 'магазин'], ['служба поддержки']]

    for item in main_buttons:
        # user_markup.row(item.pop())
        # print(i for i in item)
        sl = ''
        if len(item) > 1:
            user_markup.row(item[0], item[1])
        else:
            user_markup.row(item[0])

    return user_markup


def insert_level(user_markup):
    user_markup.row('lite', 'medium')
    user_markup.row('hard', 'extra')
    return user_markup


