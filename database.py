import psycopg2 as p
import datetime
# con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
# cur = con.cursor()
a = []



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
    cur.execute(f'''select id,name, "desc",sum,sex, ages, agee, tasker_d, t_date, current_sum from public.botmain_task where level = '{level}'
    ''')
    aa = ''
    m = cur.fetchall()
    # print(m)
    for i in m:
        ms = list(i)
        aa += f''' *Задания ID* - *{ms[0]}*\nНазвание {ms[1]}\nОписание - {ms[2]}\nСтоимость - {ms[3]}\nТекущая сумма донатов {ms[9]}\nПол исполнителя {ms[4]}\nСроки {ms[5]}-{ms[6]}\nСроки выбора исполнителя {ms[7]}\nдней Дата выполненя {ms[8]}дня/дней\n\n'''
    con.close()
    return aa


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


def check_user_balance(user_id):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(f'''select balance from public.botmain_user where telegram_id={user_id}''')
        info = list(cur.fetchone())[0]
        # print(info)
        return info
    except:
        return 0
        # print('error')


def update_balance(telegram_id, balance):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(f'''update public.botmain_user set balance={int(check_user_balance(telegram_id)) + int(balance)} where telegram_id={telegram_id}''')
        # info = list(cur.fetchone())[0]
        con.commit()
        # print(info)
        return balance
    except:
        return 0
        # print('error')


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
        cur = con.cursor()
        cur.execute(f'''UPDATE public.botmain_user SET balance={int(check_user_balance(telegram_id))-int(donate)} where telegram_id={telegram_id}''')
        cur.close()
        if sum <= res + res/10:
            cur = con.cursor()
            cur.execute(f'''UPDATE public.botmain_task SET status={1} where id={info}''')
            cur.close()

        con.commit()

        con.commit()
        a = check_user_balance(telegram_id)
        print(info)
        return 1, f'Успешно добавлен донат', a
    except:
        return 0, f'Произошла ошибка, повторите', a


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
        cur.execute(f'''select id,name, "desc",sum,sex, ages, agee, tasker_d, t_date, current_sum from public.botmain_task where level = '{level}' and status={status}
        ''')
        aa = ''
        m = cur.fetchall()

        print(m)
        for i in m:
            ms = list(i)
            aa += f''' *Задания ID* - *{ms[0]}*\nНазвание {ms[1]}\nОписание - {ms[2]}\nСтоимость - {ms[3]}\nТекущая сумма донатов -{ms[9]}\nПол исполнителя {ms[4]}\nСроки {ms[5]}-{ms[6]}\nСроки выбора исполнителя {ms[7]}\nдней Дата выполненя {ms[8]}дня/дней\n\n'''
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


# check_user_balance('120929625')

def get_my_task(telegram_id):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(
            f'''select bt.id, bt.name,bt.desc, bt.sum, bt.current_sum, ds.sum from public.botmain_task bt, (SELECT d.user_id, t.task_id, sum(dm.donate) as sum
        FROM public.botmain_donate_donater_id d, public.botmain_donate_task_id t, public.botmain_donate dm
    where d.donate_id =t.donate_id and dm.id = d.donate_id
    group by d.user_id, t.task_id) ds
    where bt.id = ds.task_id and ds.user_id = {telegram_id}
                ''')
        m = cur.fetchall()
        aa= ''
        print(m)
        for i in m:
            ms = list(i)
            aa += f''' *Задания ID* - *{ms[0]}*\nНазвание {ms[1]}\nОписание - {ms[2]}\nСтоимость - {ms[3]}\nТекущая сумма донатов -{ms[4]}\nВаш донат {ms[5]}\n'''
        con.close()
        return aa
    except:
        return 'Произошла ошибка, либо у вас нет донатов'

# insert_donate(0,1, 150)


def get_do_task(telegram_id):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(f'''SELECT id, name, current_sum,create_date from public.botmain_task where user_id_id={telegram_id}''')
        m = cur.fetchall()
        aa = ''
        print(m)
        for i in m:
            ms = list(i)
            aa += f''' *Задания ID* - *{ms[0]}*\nНазвание {ms[1]}\nТекущая сумма донатов -{ms[2]}\nДата создания {ms[3]}\n'''
        con.close()
        return aa
    except:
        return 'Произошла ошибка, либо вы не являетесь исполнителем ниодного задания'

def save_message_todb(message_id, telegram_id, text):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        try:
            cur.execute(f'''select telegram_id from public.botmain_chat where telegram_id= {telegram_id}''')
            info = list(cur.fetchone())
        except:
            info = 0
        cur.close()
        if info == 0:
            cur = con.cursor()
            cur.execute(f'''INSERT INTO public.botmain_chat(telegram_id) values({telegram_id})''')
            cur.close()
            con.commit()
        cur = con.cursor()
        cur.execute(f'''INSERT INTO public.botmain_message(telegram_id_id, message_id, text, answer) values({telegram_id}, {message_id}, '{text}', '')''')
        con.commit()
        return 1
    except:
        return 0

def select_faq():
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
        cur = con.cursor()
        cur.execute(
            f'''SELECT * from public.botmain_faq where is_active=true''')
        m = cur.fetchall()
        aa = ''
        for i in m:
            ms = list(i)
            aa += f'''{i[1]}\n'''
        return aa
    except:
        return 'Ошибка'

# a = save_message_todb('', 120929621, '')
# print(a)