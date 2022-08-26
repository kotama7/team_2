from PIL import Image, ImageTk
from pygame import mixer

def resize(path,w=1,h=1) -> ImageTk.PhotoImage: #画像の成形
    img = Image.open(path)
    img = img.resize((int(w),int(h)))
    tkimg = ImageTk.PhotoImage(img)
    return tkimg

def BGM(path):    #BGMの再生
    try:
        mixer.quit()
    except:
        pass
    mixer.init()
    mixer.music.load(path)
    mixer.music.play(loops=0)

def SE(path):   #効果音の再生
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()