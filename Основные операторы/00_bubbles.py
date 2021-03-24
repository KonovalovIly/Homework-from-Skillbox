# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center_circle = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_circle, radius)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def paint_circle(x, y, radius_step):
    center_circle_2 = sd.get_point(x, y)
    radius_2 = 50
    for _ in range(3):
        radius_2 += radius_step
        sd.circle(center_circle_2, radius_2)


paint_circle(500, 500, 10)

# Нарисовать 10 пузырьков в ряд
for i in range(10):
    step = 100 * i
    paint_circle(step, 400, 10)

# Нарисовать три ряда по 10 пузырьков
for j in range(3):
    step_y = 100 * j
    for i in range(10):
        step = 100 * i
        paint_circle(step, step_y, 10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(101):
    sd.circle(sd.random_point(), 30)

sd.pause()
