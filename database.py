import psycopg2 as p
import datetime
# con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
# cur = con.cursor()
a = []


# def start(message):
#     cur.execute('select * from task')
#     for row in cur:
#         a.append(row[0])


def insert_task(name, desc, sum, sex,age, tasker_dt, t_date, level, chat_id):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        list_age = age.split('-')
        cur.execute('select max(id) from public.botmain_task')
        count = cur.fetchone()
        cur.close()
        cur = con.cursor()
        # id, name, "desc",  sum, sex, ages, aged,tasker_d,t_date, level,creator_id_id, status, current_sum, users_count, create_date,  user_id_id
        cur.execute(
            f'''INSERT INTO public.botmain_task(id, name, sex, level, status, current_sum, users_count, create_date, creator_id_id,  "desc", agee, ages, sum, t_date, tasker_d)
        VALUES ({int(list(count)[0]) + 1},'{name}', '{sex}', '{level}', 0, 0, 0, '{datetime.date.today()}', {chat_id}, '{desc}', {list_age[1]},{list_age[0]},{sum}, {t_date}, {tasker_dt})''')
        con.commit()
        con.close()
        return int(list(count)[0])+1, 'Задание успешно добавлено'
    except:
        return 0, 'Произошла ошибка. Повторите попытку'




def select_task_by_level(level):
    con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
    cur = con.cursor()
    cur.execute(f'''select id,name, "desc",sum,sex, ages, agee, tasker_d, t_date from public.botmain_task where level = '{level}'
    ''')
    aa = ''
    m = cur.fetchall()
    # print(m)
    for i in m:
        ms = list(i)
        aa += f''' *Задания ID* - *{ms[0]}*\nНазвание {ms[1]}\nОписание - {ms[2]}\nСтоимость - {ms[3]}\nПол исполнителя {ms[4]}\nСроки {ms[5]}-{ms[6]}\nСроки выбора исполнителя {ms[7]}\nдней Дата выполненя {ms[8]}дня/дней\n\n'''
    con.close()
    return aa


# insert_task('test_name1', 'test_name2', 100, 'Ж', '18-22','5','7', 'lite')
# select_task_by_level('lite')
#
# def insert_task1(name, desc, sum, sex,age, tasker_dt, t_date, level, chat_id):
#
#     con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
#     cur = con.cursor()
#     list_age = age.split('-')
#     cur.execute('select count(*) from public.botmain_task')
#     count = cur.fetchone()
#     cur.close()
#     cur = con.cursor()
#     # id, name, "desc",  sum, sex, ages, aged,tasker_d,t_date, level,creator_id_id, status, current_sum, users_count, create_date,  user_id_id
#     cur.execute(f'''INSERT INTO public.botmain_task(id, name, sex, level, status, current_sum, users_count, create_date, creator_id_id,  "desc", agee, ages, sum, t_date, tasker_d)
# VALUES ({int(list(count)[0])+1},'{name}', '{sex}', '{level}', 0, 0, 0, '{datetime.date.today()}', {chat_id}, '{desc}', {list_age[1]},{list_age[0]},{sum}, {t_date}, {tasker_dt})''')
#     con.commit()
#     con.close()
#     return int(list(count)[0])+1, 'Задание успешно добавлено'


# a, b = insert_task('test_name1', 'test_name2', 100, 'мужской', '18-22','5','7', 'medium', 120929625)
# print(a,b)

def getuserinfo(chat_id):
    con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
    cur = con.cursor()
    cur.execute(f'select * from public.botmain_user where telegram_id ={chat_id}')
    info = cur.fetchone()
    st = 'Ваши данные'
    if info:
        for item in info:
            st += str(item) + '\n'
        return st
    else:
        return None


def insert_user(telegram_id, name, lastname, age, city, sex, desc):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur = con.cursor()
        cur.execute(f'select * from public.botmain_user where telegram_id ={telegram_id}')
        info = cur.fetchone()
        cur.close()
        if info:
            cur = con.cursor()
            cur.execute(f'''UPDATE public.botmain_user SET  name='{name}', lastname='{lastname}', city='{city}', sex='{sex}', age={age}, about='{desc}'
        	WHERE telegram_id={telegram_id}''')
            cur.close()
            con.commit()
        else:
            # id, name, "desc",  sum, sex, ages, aged,tasker_d,t_date, level,creator_id_id, status, current_sum, users_count, create_date,  user_id_id
            cur.execute(
                f'''INSERT INTO public.botmain_user(telegram_id, name, lastname, city, sex, age)
                        VALUES ({telegram_id}, '{name}', '{lastname}', '{city}', '{sex}', {age})''')
            con.commit()
            con.close()
        return int(telegram_id), 'Задание успешно добавлено'
    except:
        return 0, 'Произошла ошибка. Повторите попытку'


def get_buttons():
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(f'''select * from public.botmain_button''')
        info = cur.fetchone()
        cur.close()
        # print(list(info))
        return list(info)[1:]
    except:
        return 0


def insert_donate(telegram_id,task_id,donate):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(f'''select max(id) from public.botmain_donate''')
        info = list(cur.fetchone())[0]
        cur.close()
        cur = con.cursor()
        cur.execute(f'''insert into public.botmain_donate values({int(info)+1}, {donate})''')
        cur.close()

        cur = con.cursor()
        cur.execute(f'''insert into public.botmain_donate_donater_id(donate_id, user_id) values({int(info) + 1}, {telegram_id})''')
        cur.close()

        cur = con.cursor()
        cur.execute(f'''insert into public.botmain_donate_task_id(donate_id, task_id) values({int(info) + 1}, {task_id})''')
        cur.close()

        cur = con.cursor()
        cur.execute(f'''select id, current_sum, sum from public.botmain_task where id ={task_id}''')
        # print(list(cur.fetchone()))
        nlist = list(cur.fetchone())
        info = nlist[0]
        curb = nlist[1]
        sum = nlist[2]
        cur.close()
        print(info, curb)
        cur = con.cursor()
        res = int(curb) + int(donate)
        cur.execute(f'''UPDATE public.botmain_task SET current_sum={res} where id={info}''')
        cur.close()
        if sum <= res + res/10:
            cur = con.cursor()
            cur.execute(f'''UPDATE public.botmain_task SET status={1} where id={info}''')
            cur.close()
        con.commit()

        con.commit()

        print(info)
        return 1, f'Успешно добавлен донат'
    except:
        return 0, f'Произошла ошибка, повторите'


# def update_task_current(task_id, donate):
#     try:
#         con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
#         cur = con.cursor()
#         cur.execute(f'''select id, current_sum from public.botmain_task where id ={task_id}''')
#         # print(list(cur.fetchone()))
#         nlist = list(cur.fetchone())
#         info = nlist[0]
#         curb = nlist[1]
#         cur.close()
#         print(info, curb)
#         cur = con.cursor()
#         cur.execute(f'''UPDATE public.botmain_task SET current_sum={int(curb)+int(donate)} where id={info}''')
#         cur.close()
#         con.commit()
#         return 1
#     except:
#         return 0


def get_taskbyid(task_id, status=0):
    con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
    cur = con.cursor()
    cur.execute(f'select * from public.botmain_task where id ={task_id} and status={status}')
    info = cur.fetchone()
    st = ''
    if info:
        return 1
    else:
        return None


def select_task_by(level, status):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(f'''select id,name, "desc",sum,sex, ages, agee, tasker_d, t_date from public.botmain_task where level = '{level}' and status={status}
        ''')
        aa = ''
        m = cur.fetchall()

        print(m)
        for i in m:
            ms = list(i)
            aa += f''' *Задания ID* - *{ms[0]}*\nНазвание {ms[1]}\nОписание - {ms[2]}\nСтоимость - {ms[3]}\nПол исполнителя {ms[4]}\nСроки {ms[5]}-{ms[6]}\nСроки выбора исполнителя {ms[7]}\nдней Дата выполненя {ms[8]}дня/дней\n\n'''
        con.close()
        if len(aa)<1:
            return 'Заданий для данного случая нет'
        return aa
    except:
        return 'Заданий для данного случая нет'


def insert_maker(task_id, telegram_id):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(f'''select max(id) from public.botmain_maker''')
        info = list(cur.fetchone())[0]
        print(info)
        cur.close()
        cur = con.cursor()
        cur.execute(f'''insert into public.botmain_maker values({int(info or 0) + 1})''')
        cur.close()

        cur = con.cursor()
        cur.execute(
            f'''insert into public.botmain_maker_user_id(maker_id, user_id) values({int(info or 0) + 1}, {telegram_id})''')
        cur.close()

        cur = con.cursor()
        cur.execute(f'''insert into public.botmain_maker_task_id(maker_id, task_id) values({int(info or 0) + 1}, {task_id})''')
        cur.close()

        cur = con.cursor()
        cur.execute(f'''select id, current_sum, sum from public.botmain_task where id ={task_id}''')
        # print(list(cur.fetchone()))
        nlist = list(cur.fetchone())
        info = nlist[0]
        curb = nlist[1]
        sum = nlist[2]
        cur.close()
        print(info, curb)


        con.commit()

        print(info)
        return 1, f'Успешно добавлен донат'
    except:
        return 0, f'Произошла ошибка, повторите'




# insert_maker(2, 0)
# insert_donate(0,1, 150)


