def keyPressedInstructions(app):
    app.currentPage = "yard"
    app.yardFrame = 0
    return None

def keyPressedYard(app, event):
    if app.overlay == "place food": # arrow key triggers foodtype switch
        if event.key == "Left" or event.key == "Right": 
            if app.chooseFoodType == "Frisky Bitz":
                app.chooseFoodType = "Sashimi Boat"
            elif app.chooseFoodType == "Sashimi Boat":
                app.chooseFoodType = "Frisky Bitz"
            return None

def keyPressedShop(app, event):
    app.cellOfItem = None
    if event.key == "Left":
        app.shopPageNumber = (app.shopPageNumber - 1)%6
    elif event.key == "Right":
        app.shopPageNumber = (app.shopPageNumber + 1)%6
    return None

def keyPressedGoodies(app, event):
    app.chosenItemPosition = None
    if event.key == "Left": #goodiesPageNumber is never 0, page 0 has food and fish exchange
        app.goodiesPageNumber = (app.goodiesPageNumber - 2)%5 + 1
    elif event.key == "Right":
        app.goodiesPageNumber = (app.goodiesPageNumber)%5 + 1
    return None

def keyPressedCats(app, event):
    if event.key == "Left":
        app.catsPageNumber = (app.catsPageNumber - 1)%len(app.catsList) 
    if event.key == "Right":
        app.catsPageNumber = (app.catsPageNumber + 1)%len(app.catsList) 
    return None
