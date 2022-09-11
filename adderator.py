import traceback

import helpers as h


def add_zero(string):
    if len(string) < 2:
        return '0'+string
    return string


def add(start, end, group_id, config):
    # создаем объект для работы с апи редмайна
    err_code, redmine = h.get_redmine(config)
    if err_code != 0:
        print('Ошибка доступа к Redmine!')
        return

    user_ids = set()
    try:
        group = redmine.group.get(group_id, include=['users'])
        # забираем старых юзеров, чтобы не потерялись
        for user in group.users:
            user_ids.add(user.id)
    except Exception as e:
        traceback.print_exc()
        print('Ошибка получения группы!')
        return

    for i in range (int(start), int(end)+1):
        stud_id = 'stud_' + add_zero(str(i))
        try:
            users = redmine.user.filter(name=stud_id)
            if len(users) > 1:
                print('Обнаружено более одного пользователя ' + stud_id + '!')
            else:
                user_ids.add(users[0].id)
                print(stud_id + ' будет добавлен в группу '+ group.name + '...')
        except Exception as e:
            traceback.print_exc()
            print('Ошибка получения студента ' + stud_id)

    try:
        redmine.group.update(group_id, user_ids=list(user_ids))
        print('Всё хорошо')
    except Exception as e:
        traceback.print_exc()
        print('Ошибка обновления группы!')