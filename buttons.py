main_buttons = ['создать задание', 'стать зрителем', 'стать исполнителем', 'мои задания', 'FAQ', 'магазин', 'служба поддержки']

levels = ['lite', 'medium', 'hard', 'extra']


def insert_main(user_markup):
    # main_buttons = [['создать задание', 'стать зрителем'], ['стать исполнителем', 'мои задания'], ['FAQ', 'магазин'], ['служба поддержки']]
    a = main_buttons.copy()
    a.reverse()
    # print(a)
    for item in range(0, len(a), 2):
        if len(a) != 1:
            user_markup.row(a.pop(), a.pop())
        else:
            user_markup.row(a.pop())
        # user_markup.row(item.pop())
        # print(i for i in item)
        sl = ''

        # if len(main_buttons) % 2:
        #     for i in main_buttons[::2]:
        #         print()
        # if len(item) > 1:
        #     print(item[0], item[1])
        #     # user_markup.row(item[0], item[1])
        # else:
        #     print(item[0])
        #     # user_markup.row(item[0])

    return user_markup


def insert_level(user_markup):
    user_markup.row('lite', 'medium')
    user_markup.row('hard', 'extra')
    user_markup.row('назад')
    return user_markup



# insert_main('')
# b = main_buttons
