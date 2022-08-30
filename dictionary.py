import pyautogui

scr_w, scr_h = pyautogui.size()

data_dict = {
    'corrider':['./data/corrider.txt','./img/map/corrider.png',[2*scr_w,2*scr_h],[61*scr_w/80,-41*scr_h/500],[scr_w/2,scr_h/2],[23,21]],  #初期位置調整終了
    'class_room_A_right':['./data/class_room_A.txt','./img/map/class_room_A.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[11,2]],  #unnecessary
    'class_room_A_left':['./data/class_room_A.txt','./img/map/class_room_A.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[2917*scr_w/4000,594*scr_h/700],[11,9]],  #ini_pos fin
    'class_room_B_right':['./data/class_room_B.txt','./img/map/class_room_B.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[11,2]],  #unnecessary
    'class_room_B_left':['./data/class_room_B.txt','./img/map/class_room_B.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[2917*scr_w/4000,594*scr_h/700],[11,9]],  #ini_pos　fin
    'gym_left':['./data/gym.txt','./img/map/gym.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[375*scr_w/1200,1013*scr_h/2000],[1,5]],   #ini_pos  fin
    'gym_right':['./data/gym.txt','./img/map/gym.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[3*scr_w/4,1013*scr_h/2000],[1,12]],    #warehouse waiting
    'infirmary':['./data/infirmary.txt','./img/map/infirmary.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[192*scr_w/400,4*scr_h/5],[4,7]],  #ini_pos comp
    'auditorium':['./data/auditorium.txt','./img/map/auditorium.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[1094*scr_w/1600,18*scr_h/50],[13,1]],  #ini_pos  comp
    'auditorium_ghost':['./data/auditorium_ghost.txt','./img/map/auditorium_ghost.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[1094*scr_w/1600,18*scr_h/50],[13,1]],  #ini_pos  comp
    'staff_room_left':['./data/staff_room.txt','./img/map/staff_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[1985*scr_w/5000,294*scr_h/400],[2,7]],     #ini_pos  fin
    'staff_room_right':['./data/staff_room.txt','./img/map/staff_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[3025*scr_w/5000,294*scr_h/400],[7,7]],    #ini_pos  fin
    'library':['./data/library.txt','./img/map/library.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[1087*scr_w/4000,291*scr_h/400],[1,6]],      #ini_pos  fin
    'warehouse':['./data/warehouse.txt','./img/map/warehouse.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[1,1]],    #warehouse waiting
}
# 辞書の内容は[map_path,image_path,image_size,image_position,player_position,player_location]
 
corrider_back_dict = {
    'class_room_A_right': [[61*scr_w/80-22*scr_w/36,-41*scr_h/500+6*91*scr_h/1800],[45,15]],
    'class_room_A_left': [[61*scr_w/80-15*scr_w/36,-41*scr_h/500+6*91*scr_h/1800],[38,15]],
    'class_room_B_right': [[61*scr_w/80-36*scr_w/36,-41*scr_h/500+6*91*scr_h/1800],[59,15]],
    'class_room_B_left': [[61*scr_w/80-29*scr_w/36,-41*scr_h/500+6*91*scr_h/1800],[52,15]],
    'gym_left': [[61*scr_w/80-40*scr_w/36,-41*scr_h/500+4*91*scr_h/1800],[63,17]],
    'gym_right': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'infirmary': [[61*scr_w/80-8*scr_w/36,-41*scr_h/500+6*91*scr_h/1800],[31,15]],
    'auditorium': [[61*scr_w/80+14*scr_w/36,-41*scr_h/500+19*91*scr_h/1800],[9,2]],
    'staff_room_left': [[61*scr_w/80+12*scr_w/36,-41*scr_h/500+6*91*scr_h/1800],[11,15]],
    'staff_room_right': [[61*scr_w/80+5*scr_w/36,-41*scr_h/500+6*91*scr_h/1800],[18,15]],
    'library': [[61*scr_w/80-14*scr_w/36,-41*scr_h/500+19*91*scr_h/1800],[37,2]],
    'warehouse': [[61*scr_w/80,-41*scr_h/500],[23,21]],
}
# 辞書の内容は[image_position,player_location] 

text_dict= {
    'tako_start':'./text/めんだこ1.txt',
    'tako_class':'./text/めんだこ_教室.txt',
    'tako_gym':'./text/めんだこ_体育館.txt',
    'tako_library':'./text/めんだこ_図書館.txt',
    'tako_teacher':'./text/めんだこ_ノック.txt',
    'tako_play':'./text/めんだこ_鬼ごっこ.txt',
    'tako_walk':'./text/めんだこ_歩数.txt',
    'm':'./text/図書室_機械1.txt',
    'm2':'./text/図書室_機械2.txt',
    't':'./text/体育館_教壇.txt',
    'P':'./text/auditorium.txt',
    'd':'./text/職員室.txt',
    'd_NG':'./text/職員室_NG.txt',
    'd_OK':'./text/職員室_OK.txt',
    'b':'./text/図書室_本棚.txt',
    'g':'./text/保健室1.txt',
    'g2':'./text/保健室2.txt',
    'v':'./text/warehouse.txt',
    'k':'./text/教室1.txt',
    'k2':'./text/教室2.txt',
    'w':'./text/体育館_倉庫.txt',
    'N':'./text/体育館_出口.txt',
    '?':'./text/謎の部屋1.txt',
    '?2':'./text/謎の部屋2.txt',
    'death':'./text/幽霊.txt'
}
# 辞書の内容はsignal:path 

item_dict={
    'tako_start':['','',False],
    'tako_class':['','教室',False],
    'tako_gym':['','体育館',False],
    'tako_library':['','図書室',False],
    'tako_teacher':['','職員室',False],
    'tako_play':['','鬼ごっこ',False],
    'tako_walk':['','歩数',False],
    'm':['','',True],
    'm2':['貸出し済みの本','本',False],
    't':['','',True],
    'P':['','',False],
    'd':['','',True],
    'd_NG':['','',False],
    'd_OK':['謎の部屋の鍵','',False],
    'b':['本','',False],
    'g':['','',True],
    'g2':['','',False],
    'v':['ボール','',False],
    'k':['','',True],
    'k2':['','',False],
    'w':['','',False],
    'N':['','',False],
    '?':['','',True],
    '?2':['','',False],
    'death':['','',False],
}