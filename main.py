import tkinter
import pyautogui
import chore
import time

def new_game(): #最初のスタート画面
    new_game_b.destroy()
    canvas.delete('BG_start')
    path = 'text/introduction.txt'
    narration(path,0,scr_h/2)
    root.mainloop()

def start():
    print('start')

def narration(path,x_pos,y_pos):
    def pop(i,label):
        try:
            label.destroy()
        except:
            pass
        label = tkinter.Label(root,text=narrative[i].strip(),font=('System',24))
        label.place(x=x_pos,y=y_pos)
        print(narrative[i])
        if i != len(narrative)-1:
            root.after(1000,pop,i+1,label)
        else:
            root.after(3000,start)
        root.mainloop()
    with open(path,'r',encoding='utf-8') as f:
        narrative = f.readlines()
    root.after(1000,pop,0,None)


scr_w,scr_h= pyautogui.size()
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
