import tkinter
import pyautogui
import chore
import time

def new_game(): #最初のスタート画面
    new_game_b.destroy()
    canvas.delete('BG_start')
    path = 'text/introductioin.txt'
    narration(path,scr_w/2,scr_h/2)

def narration(path,x,y):
    txt = ''
    with open(path,'r',encoding='utf-8') as f:
        narrative = f.read()
    for ele in narrative:
        txt += ele
        label = tkinter.Label(root,text=txt)
        label.pack(x=x,y=y)
        time.sleep(0.5)
        label.destroy()
    

scr_w,scr_h= pyautogui.size()
chore.BGM('./music/BGM/bird.mp3')
root = tkinter.Tk()
root.geometry(f'{scr_w}x{scr_h}')
canvas = tkinter.Canvas(width=scr_w,height=scr_h,bg='black')
canvas.pack()
s_img_1 = chore.resize('./img/screen/start.png',scr_w,scr_h)
canvas.create_image(scr_w/2,scr_h/2,image=s_img_1,tag='BG_start')
b_img_1 = chore.resize('./img/buttun/new_game.png',scr_w/5,scr_h/10)
new_game_b = tkinter.Button(image=b_img_1,command=new_game)
new_game_b.place(x=int(scr_w*0.4),y=int(scr_h*0.7))
root.mainloop()
