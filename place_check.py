def check(number,location):
    if number == '2':
        if location == 'corrider':
            return 'gym', True
        if location == 'gym':
            return 'corrider', False