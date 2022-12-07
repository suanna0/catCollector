# buttons for menu
def inCatsButton(x, y): 
    if (95 <= x and x <= 185) and (284 <= y and y <= 356):
        if (140 <= x and x <= 185) and (318 <= y and y <= 356):
            return False
        return True
    return False

def inShopButton(x, y): 
    if (193 <= x and x <= 285) and (284 <= y and y <= 356):
        if (193 <= x and x <= 190) and (318 <= y and y <= 356):
            return False
        return True
    return False

def inGoodiesButton(x, y):
    if (95 <= x and x <= 187) and (362 <= y and y <= 434):
        if (135 <= x and x <= 187) and (362 <= y and y <= 404):
            return False
        return True
    return False

def inGiftsButton(x, y):
    if (193 <= x and x <= 285) and (362 <= y and y <= 434):
        if (193 <= x and x <= 240) and (362 <= y and y <= 404):
            return False
        return True
    return False

def inTopLeft(x, y):
    if (9 <= x and x <= 183) and (142 <= y and y <= 290):
        return True
    return False

def inTopRight(x, y):
    if (192 <= x and x <= 366) and (143 <= y and y <= 291):
        return True
    return False

def inBottomLeft(x, y):
    if (9 <= x and x <= 183) and (297 <= y and y <= 445):
        return True
    return False

def inBottomRight(x, y):
    if (192 <= x and x <= 366) and (297 <= y and y <= 445):
        return True
    return False

def pressedYes(x, y):
    if (104 <= x and x <= 185) and (401 <= y and y<= 438):
        return True
    return False

def pressedNo(x, y):
    if (193 <= x and x <= 274) and (401 <= y and y<= 438):
        return True
    return False
