import tkinter
import pyautogui

scr_w,scr_h= pyautogui.size()
root = tkinter.Tk()
root.geometry(f'{scr_w}x{scr_h}')
root.mainloop()