import re

def check(number,location):
    if number == '2':
        if location == 'corrider':
            return True, 'gym_left', True
        else:
            return True, 'corrider', False
    return False, None, None