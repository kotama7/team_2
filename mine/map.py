import tkinter as tk

root =tk.Tk()
root.geometry("768x432")

canvas = tk.Canvas(root,width=768,height=432)
canvas.place(x=0,y=0)
gazou = tk.PhotoImage(file="職員室\職員室_昼.png")
canvas.create_image(384,216,image=gazou)
root.mainloop()
