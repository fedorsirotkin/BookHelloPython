# Подключение модулей
from tkinter import *
from random import randint
from math import sqrt
from time import sleep

# Глобальные переменные
width = 925
height = 628

# Скороть перемещения космического корабля игрока
move_q = 10

# Создание вражеских космических кораблей
enemy_id = list()
enemy_spd = list()

# Создание снарядов
shoot_id = list()
shoot_speed = 15

# Создание игрового экрана
tk = Tk()
tk.title("Космический защитник")

canvas = Canvas(tk, width=width, height=height, bg="dimgray")
# Отрисовка игры
canvas.pack()

image = PhotoImage(file="images/space.gif")
canvas.create_image(0, 0, anchor=NW, image=image)

# Создание космического корабля игрока
ship = canvas.create_polygon(30, 0, 0, 40, 60, 40, fill="ivory", outline="cyan")
mid_x = width / 2
bottom_y = height - 50
canvas.move(ship, mid_x, bottom_y)


# Пользовательские функции
def create_enemy():
    y = 0
    x = randint(40, width - 40)
    ids = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="tomato", outline="linen")
    spd = randint(2, 5)
    enemy_id.append(ids)
    enemy_spd.append(spd)

# Перемещение кораблей противника
def move_enemy():
    for i in range(len(enemy_id)):
        canvas.move(enemy_id[i], 0, enemy_spd[i])

# Создание снаряда
def make_shoot():
    if len(shoot_id) < 5:
        pos = canvas.coords(ship)
        x = pos[0]
        y = pos[1]
        ids = canvas.create_oval(x - 6, y - 6, x + 6, y + 6, fill="yellow", outline="magenta")
        shoot_id.append(ids)

# Перемещение снаряда
def move_shoot():
    for i in range(len(shoot_id)):
        canvas.move(shoot_id[i], 0, -shoot_speed)

# Положение снаряда на игровом поле
def coords_shoot(in_num):
    pos = canvas.coords(in_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

# Положение противника на игровом поле
def coords_enemy(id_num):
    pos = canvas.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

# Удаление снаряда
def del_shoot(i):
    canvas.delete(shoot_id[i])
    del shoot_id[i]

# Удаление вражеского корабля
def del_enemy(i):
    canvas.delete(enemy_id[i])
    del enemy_id[i]

# Стирание снаряда игрока при вылете за экран
def clean_shoot():
    for i in range(len(shoot_id) - 1, -1, -1):
        x, y = coords_shoot(shoot_id[i])
        if y < 0:
            del_shoot(i)

# Стирание корабля противника при вылете за экран
def clean_enemy():
    for i in range(len(enemy_id) - 1, -1, -1):
        x, y = coords_shoot(enemy_id[i])
        if y > height:
            del_enemy(i)

# Расстояние между двумя объектами
def distance(id_1, id_2):
    x_1, y_1 = coords_enemy(id_1)
    x_2, y_2 = coords_shoot(id_2)
    return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

# Стирание корабля противника при попадании снаряда
def bum():
    for i in range(len(enemy_id) - 1, -1, -1):
        for j in range(len(shoot_id) - 1, -1, -1):
            if (distance(enemy_id[i], shoot_id[j]) < 26):
                del_enemy(i)
                del_shoot(j)

# Движение корабля игрока по нажатию клавиши
def ship_move(press):
    if press.keysym == "Left":
        canvas.move(ship, -move_q, 0)
    elif press.keysym == "Right":
        canvas.move(ship, move_q, 0)
    elif press.keysym == "space":
        make_shoot()


# Оживляем космический корабль игрока
canvas.bind_all("<Key>", ship_move)

# Основное тело программы
while True:
    if randint(1, 40) == 1:
        create_enemy()
    move_enemy()
    move_shoot()
    clean_enemy()
    clean_shoot()
    bum()
    tk.update()
    sleep(0.05)

tk.mainloop()
