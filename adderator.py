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

    user_ids = []
    try:
        group = redmine.group.get(group_id, include=['memberships', 'users'])
        # забираем старых юзеров, чтобы не потерялись
        for user in group.users:
            user_ids.append(user.id)
    except Exception as e:
        traceback.print_exc()
        print('Ошибка получения группы!')
        return

    for i in range (int(start), int(end)+1):
        try:
            user = redmine.user.get('stud_'+add_zero(str(i)))
            print('stud_' + add_zero(str(i))+' будет добавлен в группу '+ group.name+'...')
        except Exception as s:
            traceback.print_exc()
            print('Ошибка получения студента '+ add_zero(str(i)))
            return
        user_ids.append(user.id)

    try:
        redmine.group.update(group_id, user_ids=user_ids)
        print('Всё хорошо')
    except Exception as e:
        traceback.print_exc()
        print('Ошибка обновления группы!')