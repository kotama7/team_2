import tkinter
import pyautogui as pag
import chore
import sys
import time

scr_w,scr_h= pag.size()
tile_x = int(scr_w/10)
tile_y = int(scr_h/5)
field_ls = []
player1_map_loc = [0,0]
condition = True
root = tkinter.Tk()
img_t = chore.resize('./sample/img/object/tile.png',tile_x,tile_y)
img_w = chore.resize('./sample/img/object/wall.png',tile_x,tile_y)
img_p = chore.resize('./sample/img/character/player_1.png',tile_x,tile_y)
player1_scr_loc = [int(3*tile_x/2),int(3*tile_y/2)]
origin = [0,0]
room_x = room_y = 0
turn = 1

def room_conditioner():
    canvas.delete('PLAYER_1')
    canvas.create_image(player1_scr_loc[0],player1_scr_loc[1],image=img_p,tag='PLAYER_1')

def roommaking(o):
    y_counter = 0
    for ele_y in field_ls:  
        x_counter = 0
        for ele_x in ele_y:
            object_x = tile_x * x_counter + tile_x/2 + o[0]
            object_y = tile_y * y_counter + tile_y/2 + o[1]
            if ele_x == 0:
                canvas.create_image(object_x,object_y,image=img_t,tag=f'{x_counter},{y_counter}')
            elif ele_x == 1:
                canvas.create_image(object_x,object_y,image=img_w,tag=f'{x_counter},{y_counter}')
            x_counter += 1               
        y_counter += 1    

def roomdeleting():
    for y in range(room_y):
        for x in range(room_x):
            canvas.delete(f'{x},{y}')

def new_game():
    global start_b
    new_game_b.destroy()
    b_img_2 = chore.resize('./sample/img/buttun/start.png',scr_w/5,scr_h/10)
    start_b = tkinter.Button(image=b_img_2,command=game_start)
    start_b.place(x=int(scr_w*0.4),y=int(scr_h*0.7))
    root.mainloop()

def game_start():
    global start_b, player1_map_loc, field_ls, room_x, room_y
    room_x = 10
    room_y = 10
    start_b.destroy()
    canvas.delete('BG')
    chore.music('./sample/music/BGM/retroparty.mp3')
    field_ls = chore.roommaker(room_x,room_y)
    player1_map_loc = [1,1]
    roommaking(origin)
    canvas.create_image(player1_scr_loc[0],player1_scr_loc[1],image=img_p,tag='PLAYER_1')
    root.bind('<KeyPress>',key_push)
    root.mainloop()

def key_push(e):
    key = e.keysym
    if key in ['Up','Down','Left','Right'] and condition:
        move_proc(key)
        time.sleep(0.5)
        print(player1_map_loc)

def turn_end():
    pass

def move_proc(key):
    global condition, player1_map_loc, turn
    if key == 'Up' and field_ls[player1_map_loc[1]-1][player1_map_loc[0]] != 1:
        condition = False
        player1_map_loc[1] -= 1
        if (player1_map_loc[1] < 3 or player1_map_loc[1] > room_y-3) and player1_scr_loc[1] > tile_y:
            for _ in range(10):
                time.sleep(0.05)
                canvas.delete('PLAYER_1')
                player1_scr_loc[1] -= tile_y/10
                canvas.create_image(player1_scr_loc[0],player1_scr_loc[1],image=img_p,tag='PLAYER_1')
        else:
            for _ in range(5):
                time.sleep(0.1)
                origin[1] += tile_y/5
                roomdeleting()
                roommaking(origin)
            room_conditioner()
        turn_end()
        condition = True
        turn += 1
    elif key == 'Down' and field_ls[player1_map_loc[1]+1][player1_map_loc[0]] != 1:
        condition = False
        player1_map_loc[1] += 1
        if (player1_map_loc[1] < 4 or player1_map_loc[1] > room_y-3) and player1_scr_loc[1] < scr_h - tile_y:
            for _ in range(10):
                time.sleep(0.05)
                canvas.delete('PLAYER_1')
                player1_scr_loc[1] += tile_y/10
                canvas.create_image(player1_scr_loc[0],player1_scr_loc[1],image=img_p,tag='PLAYER_1')
        else:
            for _ in range(5):
                time.sleep(0.1)
                origin[1] -= tile_y/5
                roomdeleting()
                roommaking(origin)
            room_conditioner()
        turn_end()
        condition = True
        turn += 1
    elif key == 'Left' and field_ls[player1_map_loc[1]][player1_map_loc[0]-1] != 1:
        condition = False
        player1_map_loc[0] -= 1
        if (player1_map_loc[0] < 7 or player1_map_loc[0] > room_x-7) and player1_scr_loc[0] > tile_x :
            for _ in range(10):
                time.sleep(0.05)
                canvas.delete('PLAYER_1')
                player1_scr_loc[0] -= tile_x/10
                canvas.create_image(player1_scr_loc[0],player1_scr_loc[1],image=img_p,tag='PLAYER_1')
        else:
            for _ in range(5):
                time.sleep(0.1)
                origin[0] += tile_x/5
                roomdeleting()
                roommaking(origin)
            room_conditioner()
        turn_end()
        condition = True
        turn += 1
    elif key == 'Right' and field_ls[player1_map_loc[1]][player1_map_loc[0]+1] != 1:
        condition = False
        player1_map_loc[0] += 1
        if (player1_map_loc[0] < 7 or player1_map_loc[0] > room_x-7) and player1_scr_loc[0] < scr_w - tile_x:
            for _ in range(10):
                time.sleep(0.05)
                canvas.delete('PLAYER_1')
                player1_scr_loc[0] += tile_x/10
                canvas.create_image(player1_scr_loc[0],player1_scr_loc[1],image=img_p,tag='PLAYER_1')
        else:
            for _ in range(5):
                time.sleep(0.1)
                origin[0] -= tile_x/5
                roomdeleting()
                roommaking(origin)
            room_conditioner()
        turn_end()
        condition = True
        turn += 1


if __name__ == '__main__':
    chore.music('./sample/music/BGM/bird.mp3')
    root.title('sample')
    root.geometry('800x600')
    root.state('zoomed')
    canvas = tkinter.Canvas(width=scr_w,height=scr_h,bg='black')
    canvas.pack()
    s_img_1 = chore.resize('./sample/img/screen/start.png',scr_w,scr_h)
    canvas.create_image(scr_w/2,scr_h/2,image=s_img_1,tag='BG')
    b_img_1 = chore.resize('./sample/img/buttun/new_game.png',scr_w/5,scr_h/10)
    new_game_b = tkinter.Button(image=b_img_1,command=new_game)
    new_game_b.place(x=int(scr_w*0.4),y=int(scr_h*0.7))
    root.mainloop()
