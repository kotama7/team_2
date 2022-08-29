import tkinter
import pyautogui
import chore

map = []
map_img = tkinter.PhotoImage
player_img = tkinter.PhotoImage
boo = True  #screenのscrollのbool値
scr_w,scr_h= pyautogui.size()
data_dict = {
    'corrider':['./data/corrider.txt','./img/map/corrider.png',[2*scr_w,2*scr_h],[61*scr_w/80,-41*scr_h/500],[scr_w/2,scr_h/2],[23,21]],  #初期位置調整終了
    'class_room_A':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'gym':['./data/gym.txt','./img/map/gym.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'infirmary':['./data/infirmary.txt','./img/map/infirmary.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'auditorium': ['./data/auditorium.txt','./data/auditorium.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],

}
# 辞書の内容は[map_path,image_path,image_size,image_position,player_position,player_location]
 
corrider_back_dict = {
    'gym': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'class_room_A': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'infirmary': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'auditorium': [[61*scr_w/80,-41*scr_h/500],[23,21]],
}
# 辞書の内容は[image_position,player_location] 

def new_game(): #最初のスタート画面
    global condition, location_name
    new_game_b.destroy()
    canvas.delete('BG_start')
    location_name = 'corrider'
    set_up(location_name) 
    condition = True    #key受付の有無
    root.bind('<KeyPress>',action)
    root.mainloop()

def action(e):
    key = e.keysym
    move_ls = ['Up','Down','Right','Left']
    if key in move_ls:
        move_proc(key)

def event():
    pass

def screen_change_check():
    global location_name
    if map[player_loc[1]][player_loc[0]] == '2':    #体育館移動
        if location_name == 'corrider':
            location_name = 'gym'
            set_up(location_name)
        else:
            back_corrider_setup(location_name)
            location_name = 'corrider'
    if map[player_loc[1]][player_loc[0]] == '3':    #階段イベント    
        event('stairs_death')
    if map[player_loc[1]][player_loc[0]] == '4':    #教室A移動
        if location_name == 'corrider':
            location_name = 'class_room_A'
            set_up(location_name)
        else:
            back_corrider_setup(location_name)
            location_name = 'corrider'

def move_proc(key):
    global condition, map_position, location_name, player_loc, player_screen_loc, player_img
    i = 0
    if key == 'Up' and map[player_loc[1]-1][player_loc[0]] != '1':
        condition = False
        player_loc[1] -= 1
        path = './img/player/back.py'
        player_img = chore.resize(path,scr_w/15,scr_h/15)
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[1] += 91*tile_y/900            #y歩幅調整済み
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[1] -= 91*tile_y/900
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)                             #常に移動先の座標を表示
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
    if key == 'Down' and map[player_loc[1]+1][player_loc[0]] != '1':
        condition = False
        path = './img/player/front.py'
        player_img = chore.resize(path,scr_w/15,scr_h/15)
        player_loc[1] += 1
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[1] -= 91*tile_y/900
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[1] += 91*tile_y/900
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
    if key == 'Right' and map[player_loc[1]][player_loc[0]+1] != '1':
        condition = False
        path = './img/player/right.py'
        player_img = chore.resize(path,scr_w/15,scr_h/15)
        player_loc[0] += 1
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[0] -= tile_x/18   #歩幅調整完了
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[0] += tile_x/18
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
    if key == 'Left' and map[player_loc[1]][player_loc[0]-1] != '1':
        condition = False
        path = './img/player/left.py'
        player_img = chore.resize(path,scr_w/15,scr_h/15)
        player_loc[0] -= 1
        if boo:
            def move():
                canvas.delete(location_name)
                map_position[0] += tile_x/18    #歩幅調整完了
                canvas.create_image(map_position[0],map_position[1],image=map_img,tag=location_name)
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
        else:
            def move():
                canvas.delete('Player')
                player_screen_loc[0] -= tile_x/18
                canvas.create_image(player_screen_loc[0],player_screen_loc[1],image=player_img,tag='Player')
                canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
                print(player_loc)
                print(map[player_loc[1]][player_loc[0]])
            i += 1
            if i != 10:
                root.after(100,move)
            else:
                screen_change_check()
                condition = True
            root.mainloop()
         
def back_corrider_setup(location):
    global map, map_img, player_img, boo, player_loc, tile_x, tile_y, map_position, player_screen_loc
    data = corrider_back_dict[location]
    map = chore.roommaker('./data/corrider.txt')
    map_img = chore.resize('./img/map/corrider.png',2*scr_w,2*scr_h)
    player_screen_loc = data[0]
    canvas.create_image(data[0][0],data[0][1],image=map_img,tag=location)
    player_img = chore.resize('./img/player/front.png',scr_w/15,scr_h/15)    #縦廊下の1/3になるように調整
    tile_x = scr_w/2
    tile_y = scr_h/2
    canvas.create_image(tile_x,tile_y,image=player_img,tag='Player')
    map_position = data[0]
    player_loc = data[1]
    boo = True

def set_up(location):    #場面転換
    global map, map_img, player_img, boo, player_loc, tile_x, tile_y, map_position, player_screen_loc
    data = data_dict[location]
    map = chore.roommaker(data[0])
    map_img = chore.resize(data[1],data[2][0],data[2][1])
    player_screen_loc = data[3]
    canvas.create_image(data[3][0],data[3][1],image=map_img,tag=location)
    player_img = chore.resize('./img/player/front.png',scr_w/15,scr_h/15)    #縦廊下の1/3になるように調整
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
