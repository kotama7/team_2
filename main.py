import tkinter
import pyautogui
import chore

map = []
map_img = tkinter.PhotoImage
player_img = tkinter.PhotoImage
boo = True  #screenのscrollのbool値
scr_w,scr_h= pyautogui.size()
data_dict = {
    'corrider':['./data/corrider.txt','./img/map/corrider.png',[2*scr_w,2*scr_h],[scr_w,scr_h],[scr_w/2,scr_h/2],[23,21]],
    'class_room_A':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
}
# 辞書の内容は[map_path,image_path,image_size,image_position,player_position,player_location] 

def new_game(): #最初のスタート画面
    global condition, location_name
    new_game_b.destroy()
    canvas.delete('BG_start')
    location_name = 'corrider'
    set_up(location_name) 
    condition = True
    root.bind('<KeyPress>',action)
    root.mainloop()

def action(e):
    key = e.keysym
    move_ls = ['Up','Down','Right','Left']
    if key in move_ls:
        move_proc(key)

def move_proc(key):
    global condition, map_position, location_name, player_loc, player_screen_loc
    i = 0
    boo = False
    def recover():
        canvas.delete('Player')
        canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
    if key == 'Up' and map[player_loc[1]-1][player_loc[0]] != 1:
        condition = False
        player_loc[1] -= 1
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[1] += tile_y/10
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                root.after(0,recover)
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[1] -= tile_y/10
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                condition = True
            root.mainloop()
    if key == 'Down' and map[player_loc[1]+1][player_loc[0]] != 1:
        condition = False
        player_loc[1] += 1
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[1] -= tile_y/10
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                root.after(0,recover)
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[1] += tile_y/10
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                condition = True
            root.mainloop()
    if key == 'Right' and map[player_loc[1]][player_loc[0]+1] != 1:
        condition = False
        player_loc[0] += 1
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[0] -= tile_x/10
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                root.after(0,recover)
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[0] += tile_x/10
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                condition = True
            root.mainloop()
    if key == 'Left' and map[player_loc[1]][player_loc[0]-1] != 1:
        condition = False
        player_loc[0] -= 1
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[0] += tile_x/10
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                root.after(0,recover)
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[0] -= tile_x/10
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                condition = True
            root.mainloop()

def set_up(location):    #場面転換
    global map, map_img, player_img, boo, player_loc, tile_x, tile_y, map_position, player_screen_loc
    data = data_dict[location]
    map = chore.roommaker(data[0])
    map_img = chore.resize(data[1],data[2][0],data[2][1])
    player_screen_loc = data[3]
    canvas.create_image(data[3][0],data[3][1],image=map_img,tag=location)
    player_img = chore.resize('./img/player/front.png',scr_w/10,scr_h/10)    #随時変更の必要あり
    tile_x = data[4][0]
    tile_y = data[4][1]
    canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
    map_position = data[3]
    player_loc = data[5]
    if location == 'corrider':
        boo = True
    else:
        boo = False

chore.BGM('./music/BGM/bird.mp3')
root = tkinter.Tk()
root.geometry(f'{scr_w}x{scr_h}')
canvas = tkinter.Canvas(width=scr_w,height=scr_h,bg='white')
canvas.pack()
s_img_1 = chore.resize('./img/screen/start.png',scr_w,scr_h)
canvas.create_image(scr_w/2,scr_h/2,image=s_img_1,tag='BG_start')
b_img_1 = chore.resize('./img/buttun/new_game.png',scr_w/5,scr_h/10)
new_game_b = tkinter.Button(image=b_img_1,command=new_game)
new_game_b.place(x=int(scr_w*0.4),y=int(scr_h*0.7))
root.mainloop()
