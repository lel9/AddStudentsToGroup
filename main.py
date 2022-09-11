import argparse

import helpers as h
import adderator as ad

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Параметры запуска:')
    parser.add_argument('start', type=str, help='Начальный stud_id, например, stud_01')
    parser.add_argument('end', type=str, help='Конечный stud_id, например, stud_02')
    parser.add_argument('group_id', type=int, help='ID группы студентов в Redmine')
    parser.add_argument('-s', '--settings', type=str,
                        default='./settings.ini',
                        help='Путь к настроечному файлу (по-умолчанию ./settings.ini)')
    ns = parser.parse_args()
    print(ns)

    # читаем конфиги
    err_code, config = h.read_config(ns.settings)
    if err_code != 0:
        print('Ошибка чтения настроечного файла!')
        exit(err_code)
    else:
        print('Настроечный файл успешно прочитан...')
        ad.add(ns.start, ns.end, ns.group_id, config)
