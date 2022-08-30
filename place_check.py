import re

def check(number,location):
    if number == 'G':
        if location == 'corrider':
            return True, 'gym_left', True
        else:
            return True, 'corrider', False
    if number == 'M':
        if location == 'corrider':
            return True, 'auditorium', True
        else:
            return True, 'corrider', False
    if number == 'l':
        if location == 'corrider':
            return True, 'library', True
        else:
            return True, 'corrider', False
    if number == 'H':
        if location == 'corrider':
            return True, 'library', True
        else:
            return True, 'corrider', False
    if number == 'A':
        if location == 'corrider':
            return True, 'class_room_A_left', True
        else:
            return True, 'corrider', False
    if number == 'B':
        if location == 'corrider':
            return True, 'class_room_B_left', True
        else:
            return True, 'corrider', False
    if number == 'I':
        if location == 'corrider':
            return True, 'infirmary', True
        else:
            return True, 'corrider', False
    if number == 'L':
        if location == 'corrider':
            return True, 'staff_room_left', True
        else:
            return True, 'corrider', False
    if number == 'R':
        if location == 'corrider':
            return True, 'staff_room_right', True
        else:
            return True, 'corrider', False
   
    return False, None, None