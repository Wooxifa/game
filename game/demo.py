import tkinter
import random


def prepare_and_start():
    global player, exit, fires
    canvas.delete("all")
    player_pos = (random.randint(0, N_X - 1) * step,
                  random.randint(0, N_Y - 1) * step)
    exit_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]),
        (player_pos[0] + step, player_pos[1] + step),
        fill='green')
    exit = canvas.create_oval(
        (exit_pos[0], exit_pos[1]),
        (exit_pos[0] + step, exit_pos[1] + step),
        fill='yellow')
    N_FIRES = 6  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(0, N_X - 1) * step,
                    random.randint(0, N_Y - 1) * step)
        fire = canvas.create_oval(
            (fire_pos[0], fire_pos[1]),
            (fire_pos[0] + step, fire_pos[1] + step),
            fill='red')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    x_left, y_top, x_right, y_bottom = canvas.coords(obj)
    if x_right <= 0:
        canvas.move(obj, step * N_X, 0)
    if x_left >= step * N_X:
        canvas.move(obj, -step * N_X, 0)
    if y_bottom <= 0:
        canvas.move(obj, 0, step * N_Y)
    if y_top >= step * N_Y:
        canvas.move(obj, 0, -step * N_Y)


def do_nothing(x):
    pass


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    elif event.keysym == 'Down':
        move_wrap(player, (0, +step))
    elif event.keysym == 'Right':
        move_wrap(player, (+step, 0))
    else:
        move_wrap(player, (-step, 0))
    check_move()


master = tkinter.Tk()

step = 60
N_X = 10
N_Y = 10
canvas = tkinter.Canvas(master, bg='blue',
                        width=step * N_X, height=step * N_Y)

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
exit_pos = (random.randint(0, N_X - 1) * step,
            random.randint(0, N_Y - 1) * step)

player = canvas.create_oval((player_pos[0], player_pos[1]),
                            (player_pos[0] + step, player_pos[1] + step),
                            fill='green')
exit = canvas.create_oval((exit_pos[0], exit_pos[1]),
                          (exit_pos[0] + step, exit_pos[1] + step),
                          fill='yellow')

restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
