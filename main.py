import tkinter
import pyautogui
import chore
import time

scr_w,scr_h= pyautogui.size()
data_dict = {
    'corrider':['./data/corrider.txt','',[2*scr_w,2*scr_h],[],[]],
    'class_room_A':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[],[]],

}
# 辞書の内容は[map_path,image_path,image_size,image_position,player_position,player_location] 

def new_game(): #最初のスタート画面
    new_game_b.destroy()
    canvas.delete('BG_start')
    location_name = 'corrider'
    player_loc, map, scroll_boo = set_up(location_name,root,canvas) 
    condition = True
    root.bind('<KeyPress>',action)
    root.mainloop()

def action(e):
    key = e.keysym

def set_up(location):    #場面転換
    data = data_dict[location]
    map = chore.roommaker(data[0])
    map_img = chore.resize(data[1],data[2][0],data[2][1])
    canvas.create_image(data[3][0],data[3][1],image=map_img,tag=location)
    player_img = chore.resize('./img/player/front.png',scr_w/10,scr_h/10)    #随時変更の必要あり
    canvas.create_image(data[4][0],data[4][1],image=player_img,tag='Player')
    player_loc = data[5]
    return player_loc, map


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
