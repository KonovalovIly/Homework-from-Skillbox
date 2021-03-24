# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = input("Enter the month number: ")
month = int(user_input)
if month == 1:
    day_in_month = 31
elif month == 2:
    day_in_month = 28
elif month == 3:
    day_in_month = 31
elif month == 4:
    day_in_month = 30
elif month == 5:
    day_in_month = 31
elif month == 6:
    day_in_month = 30
elif month == 7:
    day_in_month = 31
elif month == 8:
    day_in_month = 31
elif month == 9:
    day_in_month = 30
elif month == 10:
    day_in_month = 31
elif month == 11:
    day_in_month = 30
elif month == 12:
    day_in_month = 31
else:
    print("You entered a nonexistent month")
    day_in_month = 0
print(f'Вы ввели {month} в нем {day_in_month} дней')
