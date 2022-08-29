data_dict = {
    'corrider':['./data/corrider.txt','./img/map/corrider.png',[2*scr_w,2*scr_h],[61*scr_w/80,-41*scr_h/500],[scr_w/2,scr_h/2],[23,21]],  #初期位置調整終了
    'class_room_A_right':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'class_room_A_left':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'class_room_B_right':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'class_room_B_left':['./data/class_room.txt','./img/map/class_room.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'gym_left':['./data/gym.txt','./img/map/gym.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'gym_right':['./data/gym.txt','./img/map/gym.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'infirmary':['./data/infirmary.txt','./img/map/infirmary.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'auditorium':['./data/auditorium.txt','./data/auditorium.png',[scr_w,scr_h],[0,0],[scr_w/2,scr_h/2],[11,9]],
    'staff_room_left':[],
    'staff_room_right':[],
    'library':[],
    'warehouse':[],
}
# 辞書の内容は[map_path,image_path,image_size,image_position,player_position,player_location]
 
corrider_back_dict = {
    'gym': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'class_room_A': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'infirmary': [[61*scr_w/80,-41*scr_h/500],[23,21]],
    'auditorium': [[61*scr_w/80,-41*scr_h/500],[23,21]],
}
# 辞書の内容は[image_position,player_location] 
