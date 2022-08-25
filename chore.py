from PIL import Image, ImageTk
from pygame import mixer

def resize(path,mag_w=1,mag_h=1) -> ImageTk.PhotoImage: #画像の成形
    img = Image.open(path)
    h,w = img.size
    img = img.resize((int(w*mag_w),int(h*mag_h)))
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