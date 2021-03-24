# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть

# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.

def writegood():
    global words
    file_good.write(str(words))
    file_good.write('\n')


def writebad():
    global words
    file_bad.write(str(words))
    file_bad.write('\n')


file = open('registrations.txt', 'r', encoding='utf-8')
file_bad = open('registrations_bad.txt', 'w', encoding='utf-8')
file_good = open('registrations_good.txt', 'w', encoding='utf-8')
string = file.read().split('\n')
for words in string:
    word = words.split(' ')
    if len(word) == 3:
        first_word = word[0].isalpha()
        if first_word:
            if '@' in word[1] and '.' in word[1]:
                if 99 > int(word[2]) > 10:
                    writegood()
                else:
                    writebad()
            else:
                writebad()
        else:
            writebad()
    else:
        writebad()


file.close()
file_bad.close()
file_good.close()
