import psycopg2 as p
# con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5433)
# cur = con.cursor()
a = []


# def start(message):
#     cur.execute('select * from task')
#     for row in cur:
#         a.append(row[0])


def insert_task(name, desc, sum, sex,age, tasker_dt, t_date, level, chat_id):
    try:
        con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5432)
        cur = con.cursor()
        list_age = age.split('-')
        cur.execute('select count(*) from public.botmain_task')
        count = cur.fetchone()
        cur.close()
        cur = con.cursor()
        cur.execute(f'''INSERT INTO public.botmain_task(id, name, "desc", sum, sex, ages, agee, tasker_d, t_date, level, creator_id_id) 
VALUES ({int(list(count)[0])+1},'{name}', '{desc}', {sum}, '{sex}', {list_age[0]}, {list_age[1]}, {tasker_dt}, {t_date}, '{level}', {chat_id})''')
        con.commit()
        con.close()
        return int(list(count)[0])+1, 'Задание успешно добавлено'
    except:
        return 0, 'Произошла ошибка. Повторите попытку'




def select_task_by_level(level):
    con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5432)
    cur = con.cursor()
    cur.execute(f'''select * from public.task where level = '{level}'
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
def insert_task1(name, desc, sum, sex,age, tasker_dt, t_date, level, chat_id):
    con = p.connect(database='bot', user='postgres', host='localhost', password='VivaProgressio', port=5432)
    cur = con.cursor()
    list_age = age.split('-')
    cur.execute('select count(*) from public.botmain_task')
    count = cur.fetchone()
    cur.close()
    cur = con.cursor()
    cur.execute(f'''INSERT INTO public.botmain_task(id, name, "desc", sum, sex, ages, agee, tasker_d, t_date, level, creator_id_id) 
VALUES ({int(list(count)[0])+1},'{name}', '{desc}', {sum}, '{sex}', {list_age[0]}, {list_age[1]}, {tasker_dt}, {t_date}, '{level}', {chat_id})''')
    con.commit()
    con.close()


insert_task1('test_name1', 'test_name2', 100, 'мужской', '18-22','5','7', 'medium', 120929625)
