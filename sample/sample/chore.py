from PIL import Image, ImageTk
from pygame import mixer

def resize(path,w,h):
    img = Image.open(path)
    img = img.resize((int(w),int(h)))
    tkimg = ImageTk.PhotoImage(img)
    return tkimg

def music(path):
    try:
        mixer.quit()
    except:
        pass
    mixer.init()
    mixer.music.load(path)
    #mixer.music.play(loops=0)

def roommaker(x,y):
    ls = []
    ls.append([1 for _ in range(x)])
    for i in range(y-2):
        x_ls = [1] + [0 for _ in range(x-2)] + [1]
        ls.append(x_ls)
    ls.append([1 for _ in range(x)])
    return ls
