import pyautogui

scr_w, scr_h = pyautogui.size()

data_dict = {
    'corrider':['./data/corrider.txt','./img/map/corrider.png',[2*scr_w,2*scr_h],[61*scr_w/80,-41*scr_h/500],[scr_w/2,scr_h/2],[23,21]],  #初期位置調整終了
    'class_room_A_right':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[11,2]],
    'class_room_A_left':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[11,9]],
    'class_room_B_right':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[11,2]],
    'class_room_B_left':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[11,9]],
    'gym_left':['./data/gym.txt','./img/map/gym.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[1,5]],
    'gym_right':['./data/gym.txt','./img/map/gym.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[1,12]],
    'infirmary':['./data/infirmary.txt','./img/map/infirmary.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[4,7]],
    'auditorium':['./data/auditorium.txt','./img/map/auditorium.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[13,1]],
    'staff_room_left':['./data/staff_room.txt','./img/map/staff_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[2,8]],
    'staff_room_right':['./data/staff_room.txt','./img/map/staff_room.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[7,8]],
    'library':['./data/library.txt','./img/map/library.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,4*scr_h/9],[1,6]],
    'warehouse':['./data/warehouse.txt','./img/map/warehouse.png',[scr_w,scr_h],[scr_w/2,45*scr_h/100],[scr_w/2,scr_h/2],[1,1]],
}
# 辞書の内容は[map_path,image_path,image_size,image_position,player_position,player_location]
 
corrider_back_dict = {
    'class_room_A_right': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'class_room_A_left': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'class_room_B_right': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'class_room_B_left': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'gym_left': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'gym_right': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'infirmary': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'auditorium': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'staff_room_left': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'staff_room_right': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'library': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'warehouse': [[61*scr_w/80,-41*scr_h/500],[23,21]],
}
# 辞書の内容は[image_position,player_location] 
