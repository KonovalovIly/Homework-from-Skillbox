# -*- coding: utf-8 -*-

from collections import defaultdict
import re

# напишите функцию
# котрая читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# for group_time, event_count in date_by_counter.items():
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

file_name = 'events.txt'
pattern_datetime = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')
date_by_counter = defaultdict(int)


def parser(file_name):
    with open(file_name) as file:
        for line in file:
            if 'NOK' not in line:
                continue

            match = pattern_datetime.search(line)
            # Проверка, что регулярка смогла найти дату
            if match:
                date_str = match.group(1)  # Получение даты
                date_by_counter[date_str] += 1


parser(file_name)

for group_time, event_count in date_by_counter.items():
    print(f'[{group_time}] {event_count}')
