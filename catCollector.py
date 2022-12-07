#########################
# graphics 
#########################
import random
from cmu_112_graphics import *
from inventoryClass import *
from yardPositionClass import *
from yardClass import * 
from catClass import *
from keyPressedFunctions import *
from mousePressedFunctions import *
from PIL import Image
import os

rootdir = os.getcwd()

def getImagePath(imageName): # to open images
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(f"/{imageName}.png") or filepath.endswith(f"/{imageName}.jpg"):
                return (filepath)

def appStarted(app):
    initializeShop(app)
    initializeYard(app)
    initializeInventory(app)
    initializeCats(app)
    app.overlay = None
    app.yardFrame = 0
    app.startBestArrangements = False
    app.playSolutionAnimation = False
    app.playSleepAnimation = False
    app.timePassed = 0
    app.timerDelay = 75 
    app.instructionsFrame = 0
    app.currentPage = "new game?"

def initializeYard(app):
    app.bench = yardPosition("bench", 193, 297)
    app.porch = yardPosition("porch", 75, 380)
    app.carpetBack = yardPosition("carpet (back)", 245, 465)
    app.carpetFront = yardPosition("carpet (front)", 129, 510)
    app.stump = yardPosition("stump", 275, 525)
    app.yardPositionNames = {"bench": app.bench, "porch": app.porch, "carpet (back)": app.carpetBack,
    "carpet (front)": app.carpetFront, "stump": app.stump}
    app.myYard = yard([app.bench, app.porch, app.carpetBack, app.carpetFront, app.stump])

def initializeShop(app): 
    # key = "name of item"
    # value = (moneyType, price, cell position)
    # "UL" = up left, "UR" = up right, "DL" = down left, "DR" = down right
    app.shop = { 
    # PAGE 0    
    # foods
    "Frisky Bitz": ("fish", 30, "UL"), "Sashimi Boat": ("goldfish", 50, "UR"),

    # fish exchange
    "Fish Exchange": ("goldfish", 10, "DL"), "Gold Fish Exchange": ('fish', 500, "DR"),

    # PAGE 1
    "Baseball": ("fish", 90, "UL"), "Rubber Ball (Red)": ("fish", 60, "UR"), 
    "Rubber Ball (Yellow)": ("fish", 60, "DL"), "Rubber Ball (Blue)": ("fish", 60, "DR"),

    # PAGE 2
    "Pillow (Yellow)": ("fish", 120, "UL"), "Pillow (Green)": ("fish", 120, "UR"),
    "Cat Macaron (Pink)": ("fish", 210, "DL"), "Cat Macaron (Green)": ("fish", 210, "DR"),

    # PAGE 3
    "Cat Pancake": ("goldfish", 24, "UL"), "Cream-puff House": ("goldfish", 19, "UR"),
    "Honey Pot": ("fish", 230, "DL"), "Egg Tart Bed": ("fish", 290, "DR"),

    # PAGE 4
    "Sushi Cushion (Tuna)": ("goldfish", 20, "UL"), "Sushi Cushion (Shrimp)": ("goldfish", 20, "UR"), 
    "Pancake Cushion": ("goldfish", 15, "DL"), "Burger Cushion": ("goldfish", 14, "DR"),

    # PAGE 5
    "Kashiwamochi Cushion": ("fish", 300, "UL"), "Sakuramochi Cushion": ("goldfish", 12, "UR"),
    "Strawberry Cake": ("goldfish", 50, "DL"), "Penguin Plush": ("goldfish", 20, "DR")
    }

    app.page0 = {"Frisky Bitz": ("fish", 30, "UL"), "Sashimi Boat": ("goldfish", 50, "UR"),
    "Fish Exchange": ("goldfish", 10, "DL"), "Gold Fish Exchange": ('fish', 500, "DR"),}

    app.page1 = {"Baseball": ("fish", 90, "UL"), "Rubber Ball (Red)": ("fish", 60, "UR"), 
    "Rubber Ball (Yellow)": ("fish", 60, "DL"), "Rubber Ball (Blue)": ("fish", 60, "DR"),}

    app.page2 = {"Pillow (Yellow)": ("fish", 120, "UL"), "Pillow (Green)": ("fish", 120, "UR"),
    "Cat Macaron (Pink)": ("fish", 210, "DL"), "Cat Macaron (Green)": ("fish", 210, "DR"),}

    app.page3 = {"Cat Pancake": ("goldfish", 24, "UL"), "Cream-puff House": ("goldfish", 19, "UR"),
    "Honey Pot": ("fish", 230, "DL"), "Egg Tart Bed": ("fish", 290, "DR"),}

    app.page4 = {"Sushi Cushion (Tuna)": ("goldfish", 20, "UL"), "Sushi Cushion (Shrimp)": ("goldfish", 20, "UR"), 
    "Pancake Cushion": ("goldfish", 15, "DL"), "Burger Cushion": ("goldfish", 14, "DR"),}

    app.page5 = {"Kashiwamochi Cushion": ("fish", 300, "UL"), "Sakuramochi Cushion": ("goldfish", 12, "UR"),
    "Strawberry Cake": ("goldfish", 50, "DL"), "Penguin Plush": ("goldfish", 20, "DR")}

    # types of items
    # split into low and high end
    app.normalItems = {"Baseball", "Rubber Ball (Red)", 
        "Rubber Ball (Yellow)", "Rubber Ball (Blue)",
        "Pillow (Yellow)", "Pillow (Green)"}
    app.rareItems = {"Cat Macaron (Pink)", "Cat Macaron (Green)", 
        "Cat Pancake", "Cream-puff House", 
        # "Honey Pot", 
        "Egg Tart Bed", 
        "Sushi Cushion (Tuna)", "Sushi Cushion (Shrimp)", 
        "Pancake Cushion", "Burger Cushion",
        "Kashiwamochi Cushion", "Sakuramochi Cushion",
        "Strawberry Cake", "Penguin Plush"}

    # partition based on types of animations needed 
    # balls need to be resized
    app.balls = {"Baseball", "Rubber Ball (Red)", 
        "Rubber Ball (Yellow)", "Rubber Ball (Blue)"}
    app.lowSittingPillows = {"Egg Tart Bed", "Pillow (Yellow)", "Pillow (Green)", 
         "Kashiwamochi Cushion", "Sakuramochi Cushion", "Penguin Plush"}
    app.highSittingPillows = {"Sushi Cushion (Tuna)", 
        "Sushi Cushion (Shrimp)", "Pancake Cushion", 
        "Burger Cushion"}
    app.houses = {"Cat Macaron (Pink)", "Cat Macaron (Green)", 
        "Cat Pancake", "Cream-puff House", 
        "Strawberry Cake"}
    app.miscellaneous = {"Honey Pot"}
    # honey pot has separate pose

    # we assign "UL", "UR", "DL", "DR" to app.cellOfItem. 
    # when when we click on that cell, changing app.cellOfItem triggers "buy item?" pop up
    app.cellOfItem = None

def initializeInventory(app):
    app.myInventory = inventory(240, 20) #(fish, goldFish)
    app.giftsNotReceived = []

def initializeCats(app):
    snowball = cat("Snowball", "Solid White", "Mellow", 30, "Rubber Ball (Red)", "bench")
    lexy = cat("Lexy", "Grey & White", "Laid Back", 25, "Rubber Ball (Yellow)", "porch")
    smokey = cat("Smokey", "Solid Black", "Hot and Cold", 20, "Rubber Ball (Blue)", "carpet (back)")
    doris = cat("Doris", "White Mackerel", "Determined", 20, "Baseball", "stump")
    shadow = cat("Shadow", "Solid Grey", "Peculiar", 10, "Pillow (Yellow)", "carpet (front)")

    peaches = cat("Peaches", "Tan & Orange", "Capricious", 55, "Egg Tart Bed", "carpet (front)")
    anna = cat("Anna", "Heart", "Friendly", 100, "Cat Macaron (Green)", "stump")
    ginger = cat("Ginger", "Red w/ White Mitts", "Bashful", 60, "Sushi Cushion (Shrimp)", "carpet (front)")
    pumpkin = cat("Pumpkin", "Orange & White Tabby", "Spacey", 90, "Sushi Cushion (Tuna)", "carpet (back)")
    chocola = cat("Chocola", "Choco Pointed Siamese", "Forgetful", 80, "Kashiwamochi Cushion", "porch")

    callie = cat("Callie", "Calico", "Optimistic", 70, "Pancake Cushion", "porch")
    caramel = cat("Caramel", "Spotted", "Calm", 90, "Burger Cushion", "carpet (back)")
    bandit = cat("Bandit", "Tortoiseshell", "Shy", 85, "Cream-puff House", "bench")
    caroline = cat("Caroline", "Pointed Siamese", "Smart", 80, "Strawberry Cake", "stump")
    algorithm = cat("Al Gorithm", "Brown Tuxedo", "Good at CS", 130, "Penguin Plush", "stump")

    app.cats = {"Snowball": snowball, "Lexy": lexy, "Smokey": smokey, "Doris": doris, "Shadow": shadow,
                "Peaches": peaches, "Anna": anna, "Ginger": ginger, "Pumpkin": pumpkin, "Chocola": chocola,
                "Callie": callie, "Caramel": caramel, "Bandit": bandit, "Caroline": caroline, "Al Gorithm": algorithm}
    app.catsList = ["Snowball", "Lexy", "Smokey", "Doris", "Shadow",
                    "Peaches", "Anna", "Ginger", "Pumpkin", "Chocola",
                    "Callie", "Caramel", "Bandit", "Caroline", "Al Gorithm",
                    ] # index needed for cat page display, list for random choice

    # separate normal and rare cats
    app.normalCats = set()
    app.rareCats = set()
    for catName in app.cats:
        kitty = app.cats[catName]
        if kitty.powerlevel > 50:
            app.rareCats.add(catName)
        else:
            app.normalCats.add(catName)

def keyPressed(app, event):
    if app.playSleepAnimation == True:
        return None
    if app.currentPage == "new game?":
        if event.key == "1":
            app.currentPage = "instructions"
            app.instructionsFrame = 0 
        elif event.key == "2":
            fileName = input("Enter your name: ")
            file = open(f"{fileName}.txt")
            code = file.read()
            readFile(app, code)
            app.currentPage = "yard"
            app.startBestArrangements = False
    if event.key == "Escape":
        saveProgress(app)
        app.quit() # quit method: https://www.geeksforgeeks.org/how-to-close-a-tkinter-window-with-a-button/
    if app.currentPage == "instructions" and event.key == "Space":
        return keyPressedInstructions(app)
    if event.key == "s":
        app.overlay = "sleep"
        return None
    elif event.key == "m":
        app.overlay = "menu"
        return None
    if app.currentPage == "yard":
        return keyPressedYard(app, event)
    if app.overlay == None:
        if app.currentPage == "shop":
            return keyPressedShop(app, event)
        elif app.currentPage == "goodies":
            return keyPressedGoodies(app, event)
        elif app.currentPage == "cats":
            return keyPressedCats(app, event)

def mousePressed(app, event): # all helper functions return none.
    x, y = event.x, event.y
    if app.overlay == "menu":
        return mousePressedMenu(app, x, y) # this function returns None btw 
    elif app.overlay == "sleep":
        return mousePressedSleep(app, x, y)
    elif app.overlay == "no money": # click anywhere releases no money overlay
        app.overlay = None 
        return None
    elif app.overlay == "best arrangement instructions":
        if app.solution == "does not exist" or app.solution == "choose 5":
            app.solution = None
        if len(app.setOfCats) <= 5: 
            if (60 <= x <= 320) and (515 <= y <= 553): app.solution = "choose 5"
        if len(app.setOfCats) == 5:
            if (60 <= x <= 320) and (515 <= y <= 553): # coordinates of start button
                app.startButtonPressed = True
                app.solution = (bestArrangement(app))
                if app.solution != None: # then the solution is a dictionary 
                    app.playSolutionAnimation = True
                    app.startSolutionFrame = 0
                    for position in app.solution: # hardcode spawn instead!
                        catName = app.solution[position]
                        kitty = app.cats[catName]
                        app.myYard.forceSpawn(position, kitty)
                    app.currentPage = "yard"
                    app.overlay = None
                    app.startBestArrangements = False
                else: 
                    app.solution = "does not exist"
                return None
        return choose5Cats(app, x, y)
    if app.currentPage == "cats":
        if (7 <= x and x <= 126) and (8 <= y and y <= 52):
            app.overlay = "menu"
        return None
    elif app.currentPage == "yard":
        return mousePressedYard(app, x, y)
    elif app.currentPage == "shop":
        return mousePressedShop(app, x, y)
    elif app.currentPage == "goodies":
        return mousePressedGoodies(app, x, y)
    elif app.currentPage == "gifts":
        return mousePressedGifts(app, x, y)

def getItem(app): # returns item based on app.cellOfItem and app.shopPageNumber
    L = [
        ["Frisky Bitz", "Sashimi Boat", "Fish Exchange", "Gold Fish Exchange"],
        ["Baseball", "Rubber Ball (Red)", "Rubber Ball (Yellow)", "Rubber Ball (Blue)"],
        ["Pillow (Yellow)", "Pillow (Green)", "Cat Macaron (Pink)", "Cat Macaron (Green)"],
        ["Cat Pancake", "Cream-puff House", "Honey Pot", "Egg Tart Bed"],
        ["Sushi Cushion (Tuna)", "Sushi Cushion (Shrimp)", "Pancake Cushion", "Burger Cushion"],
        ["Kashiwamochi Cushion", "Sakuramochi Cushion", "Strawberry Cake", "Penguin Plush"]]
    if app.cellOfItem != None:
        cell = app.cellOfItem
    elif app.chosenItemPosition != None:
        cell = app.chosenItemPosition
    else: return None
    if cell == "UL":
        col = 0
    elif cell == "UR":
        col = 1
    elif cell == "DL":
        col = 2
    elif cell == "DR":
        col = 3
    if app.currentPage == "shop":
        row = app.shopPageNumber
    elif app.currentPage == "goodies":
        row = app.goodiesPageNumber
    return L[row][col]

def timerFired(app):
    app.timePassed += 1
    if app.overlay != "best arrangement instructions": # we are not at backtracking page
        if app.timePassed%40 == 0: 
            catName = random.choice(app.catsList)
            kitty = app.cats[catName]
            if kitty.visiting == False and app.startBestArrangements == False:
                app.myYard.spawn(kitty, app.normalItems, app.rareItems, app.normalCats, app.rareCats)
        for catName in app.catsList: # to update time
            kitty = app.cats[catName]
            if kitty.visiting == True:
                kitty.updateTime(app, app.myYard)
    if app.currentPage == "new game?":
        app.instructionsFrame = (app.instructionsFrame + 1)%7
    if app.currentPage == "instructions":
        app.instructionsFrame = (app.instructionsFrame + 1)%7
    elif app.currentPage == "yard":
        if app.playSolutionAnimation == True:
            app.startSolutionFrame += 1
            if app.startSolutionFrame > 29: # animation is finished
                app.playSolutionAnimation = False
        if app.playSleepAnimation == True:
            app.sleepFrame += 1
            if app.sleepFrame > 15:
                app.playSleepAnimation = False
        app.yardFrame = (app.yardFrame + 1)%7
    elif app.currentPage == "shop":
        app.sparkleFrame = (app.sparkleFrame + 1)%6
    elif app.currentPage == "goodies":
        app.goodiesFrame = (app.goodiesFrame + 1)%5
    elif app.currentPage == "cats":
        app.catFrame = (app.catFrame + 1)%6 


def redrawAll(app, canvas):
    if app.currentPage == "new game?":
        canvas.create_rectangle(0, 0, 375, 667, fill = "#C4D3D9")
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'new game? {app.instructionsFrame}')))
        canvas.create_image(0,0, anchor=NW, image=display)
    elif app.currentPage == "instructions":
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'instructions{app.instructionsFrame}')))
        canvas.create_image(0,0, anchor=NW, image=display)
    elif app.currentPage == "yard":
        display = ImageTk.PhotoImage(Image.open(getImagePath('background')))
        canvas.create_image(0,0, anchor=NW, image=display)
        drawYard(app, canvas)
        if app.playSleepAnimation == True:
            canvas.create_rectangle(0, 0, 375, 667, fill = "#C4D3D9")
            display = ImageTk.PhotoImage(Image.open(getImagePath(f'zzz {app.sleepFrame%6}')))
            canvas.create_image(0,0, anchor=NW, image=display)
    elif app.currentPage == "cats":
        display = ImageTk.PhotoImage(Image.open(getImagePath('cat background')))
        canvas.create_image(0,0, anchor=NW, image=display)
        drawCatProfile(app, canvas, app.cats[app.catsList[app.catsPageNumber]]) # i promise this works 
    elif app.currentPage == "shop":
        display = ImageTk.PhotoImage(Image.open(getImagePath('shop')))
        canvas.create_image(0,0, anchor=NW, image=display)
        drawShop(app, canvas)
    elif app.currentPage == "goodies":
        display = ImageTk.PhotoImage(Image.open(getImagePath('goodies')))
        canvas.create_image(0,0, anchor=NW, image=display)
        drawGoodies(app, canvas)
    elif app.currentPage == "gifts":
        display = ImageTk.PhotoImage(Image.open(getImagePath('gifts')))
        canvas.create_image(0,0, anchor=NW, image = display)
        drawGiftsPage(app, canvas)
    # we draw money if overlay == none and currentPage != instructions
    if app.currentPage != "instructions" and app.currentPage != "new game?" and app.playSolutionAnimation == False and app.playSleepAnimation == False:
        drawMoney(app, canvas)
    # keep sleep and menu at the end!!!!
    if app.overlay == "menu": # draws over current image
        display = ImageTk.PhotoImage(Image.open(getImagePath('menu')))
        canvas.create_image(0,0, anchor=NW, image=display)
        if len(app.giftsNotReceived) > 0:
            display = display = ImageTk.PhotoImage(Image.open(getImagePath('gifts not received tag')))
            canvas.create_image(0,0, anchor=NW, image=display)
    elif app.overlay == "sleep":
        display = ImageTk.PhotoImage(Image.open(getImagePath('sleep')))
        canvas.create_image(0,0, anchor=NW, image=display)
    elif app.overlay == "no money":
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'no money {app.sparkleFrame}')))
        canvas.create_image(0,0, anchor=NW, image=display)
    elif app.overlay == "best arrangement instructions":
        drawStartBackTracking(app, canvas)


def drawMoney(app, canvas):
    canvas.create_text(10, 640, anchor = NW, 
    text = f"Fish: {app.myInventory.money['fish']}    Goldfish: {app.myInventory.money['goldfish']}",
    font = "Inter 14 bold", fill = "#9c3337")

def drawYard(app, canvas): # draws items! not the background itself
    for position in app.myYard.itemPositions:
        if app.myYard.itemPositions[position] != False:
            item = app.myYard.itemPositions[position]
            x,y = position.coordinates()
            display = ImageTk.PhotoImage(Image.open(getImagePath(f"{item}")))
            canvas.create_image(x, y + 60, anchor = S, image = display)
            if app.myYard.catPositions[position] != False:
                cat = app.myYard.catPositions[position]
                x, y = position.coordinates()
                drawCatPose(app, canvas, cat, item, (x,y))


    # leave tree stump at the end
    display = ImageTk.PhotoImage(Image.open(getImagePath('tree stump')))
    canvas.create_image(375, 667, anchor=SE, image=display)
    if app.myYard.itemPositions[app.stump] != False:
        item = app.myYard.itemPositions[position]
        x,y = position.coordinates()
        display = ImageTk.PhotoImage(Image.open(getImagePath(f"{item}")))
        canvas.create_image(x, y + 60, anchor = S, image = display)
        if app.myYard.catPositions[app.stump] != False:
                cat = app.myYard.catPositions[app.stump]
                x, y = position.coordinates()
                drawCatPose(app, canvas, cat, item, (x,y))
    if app.myYard.food == None: 
        drawArrow(app, canvas, (110, 610))
        if app.overlay == "place food":
            display = ImageTk.PhotoImage(Image.open(getImagePath(f"place {app.chooseFoodType}")))
            canvas.create_image(0, 0, anchor = NW, image = display)
            canvas.create_text(100, 227, anchor = NW, 
            text = f"Place {app.chooseFoodType}? {app.myInventory.pantry[app.chooseFoodType]} in stock", 
            fill = "#9c3337", font = "Inter 12 bold")
            if app.myInventory.pantry[app.chooseFoodType] < 1:
                display = ImageTk.PhotoImage(Image.open(getImagePath("food item unavailable 0.png")))
                canvas.create_image(0, 0, anchor = NW, image = display)
    else: # app.myYard.food has something
        drawItem(app, canvas, app.myYard.food, "food") 
        if app.overlay == "display food level":
            display = ImageTk.PhotoImage(Image.open(getImagePath(f"food level {app.myYard.foodLevel}")))
            canvas.create_image(0, 0, anchor = NW, image = display)
            display = ImageTk.PhotoImage(Image.open(getImagePath(f"{app.myYard.food}")))
            canvas.create_image(94, 254, anchor = NW, image = display)
            canvas.create_text(120, 252, anchor = NW, text = f"{app.myYard.food}",
            font = "Inter 12 bold", fill = "#9c3337")
    if app.playSolutionAnimation == True:
        if app.startSolutionFrame < 14:
            canvas.create_rectangle(0, 0, 375, 667, fill = "#C4D3D9")
            display = ImageTk.PhotoImage(Image.open(getImagePath(f'start best arrangement 17')))
            canvas.create_image(0,0, anchor=NW, image = display)
            drawCatCells(app, canvas)
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'loading best arrangement {app.startSolutionFrame}')))
        canvas.create_image(0,0, anchor = NW, image = display)

def drawCatProfile(app, canvas, cat):
    if cat.visits == 0:
        display = ImageTk.PhotoImage(Image.open(getImagePath(f"mystery profile picture {app.catFrame}")))
        canvas.create_text(191, 227, text = "?????", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(202, 250, text = "?????", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(277, 274, text = "?????", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(211, 318, text = "?????", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(208, 341, text = "0", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(137, 381, text = "?????", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(18, 453, text = f"Prefers the {cat.favoriteItem.lower()} \nplaced on the {cat.favoritePosition}", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
    elif cat.visits > 0:
        display = ImageTk.PhotoImage(Image.open(getImagePath(f"{cat.name} profile picture {app.catFrame}")))
        canvas.create_text(191, 227, text = f"{cat.name}", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(202, 250, text = f"{cat.breed}", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(277, 274, text = f"{cat.personality}", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(211, 318, text = f"{cat.powerlevel}", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(208, 341, text = f"{cat.visits}", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
        canvas.create_text(137, 381, text = f"{cat.getTop3()}", anchor = NW, fill = "#30849D", font = "Inter 12 bold") 
        canvas.create_text(18, 453, text = f"{cat.name} prefers the {cat.favoriteItem.lower()} \nplaced on the {cat.favoritePosition}", anchor = NW, fill = "#30849D", font = "Inter 12 bold")
    canvas.create_image(0, 0, anchor=NW, image=display)

def drawShop(app, canvas):
    if app.shopPageNumber == 0:
        for item in app.page0:
            cell = app.page0[item][2]
            drawItem(app, canvas, item, cell) 
            if item in app.myInventory.catalog:
                drawItemPurchased(app, canvas, cell)
        if app.cellOfItem != None:
            display = ImageTk.PhotoImage(Image.open(getImagePath('buy pop up')))
            canvas.create_image(0,0, anchor=NW, image=display)
            # find the item that matches up to the cell of app.cellOfItem
            if getItem(app)!= None: item = getItem(app)
            drawItem(app, canvas, item, "buy pop up")
    elif app.shopPageNumber == 1:
        for item in app.page1:
            cell = app.page1[item][2]
            drawItem(app, canvas, item, cell)
            if item in app.myInventory.catalog:
                drawItemPurchased(app, canvas, cell)
        if app.cellOfItem != None:
            display = ImageTk.PhotoImage(Image.open(getImagePath('buy pop up')))
            canvas.create_image(0,0, anchor=NW, image=display)
            if getItem(app)!= None: item = getItem(app)
            drawItem(app, canvas, item, "buy pop up")
    elif app.shopPageNumber == 2:
        for item in app.page2:
            cell = app.page2[item][2]
            drawItem(app, canvas, item, cell)
            if item in app.myInventory.catalog:
                drawItemPurchased(app, canvas, cell)
        if app.cellOfItem != None:
            display = ImageTk.PhotoImage(Image.open(getImagePath('buy pop up')))
            canvas.create_image(0,0, anchor=NW, image=display)
            if getItem(app)!= None: item = getItem(app)
            drawItem(app, canvas, item, "buy pop up")
    elif app.shopPageNumber == 3:
        for item in app.page3:
            cell = app.page3[item][2]
            drawItem(app, canvas, item, cell)
            if item in app.myInventory.catalog:
                drawItemPurchased(app, canvas, cell)
        if app.cellOfItem != None:
            display = ImageTk.PhotoImage(Image.open(getImagePath('buy pop up')))
            canvas.create_image(0,0, anchor=NW, image=display)
            if getItem(app)!= None: item = getItem(app)
            drawItem(app, canvas, item, "buy pop up")
    elif app.shopPageNumber == 4:
        for item in app.page4:
            cell = app.page4[item][2]
            drawItem(app, canvas, item, cell)
            if item in app.myInventory.catalog:
                drawItemPurchased(app, canvas, cell)
        if app.cellOfItem != None:
            display = ImageTk.PhotoImage(Image.open(getImagePath('buy pop up')))
            canvas.create_image(0,0, anchor=NW, image=display)
            if getItem(app)!= None: item = getItem(app)
            drawItem(app, canvas, item, "buy pop up")
    elif app.shopPageNumber == 5:
        for item in app.page5:
            cell = app.page5[item][2]
            drawItem(app, canvas, item, cell)
            if item in app.myInventory.catalog:
                drawItemPurchased(app, canvas, cell)
        if app.cellOfItem != None:
            display = ImageTk.PhotoImage(Image.open(getImagePath('buy pop up')))
            canvas.create_image(0,0, anchor=NW, image=display)
            if getItem(app)!= None: item = getItem(app)
            drawItem(app, canvas, item, "buy pop up")

def drawItemPurchased(app, canvas, cell):
    display = ImageTk.PhotoImage(Image.open(getImagePath(f'purchased {app.sparkleFrame}')))
    if cell == "UL":
        x, y = (6, 137)
    elif cell == "UR":
        x, y = (189, 136)
    elif cell == "DL":
        x, y = (6, 292)
    elif cell == "DR":
        x, y = (188, 292)
    canvas.create_image(x,y, anchor=NW, image=display)

def drawItem(app, canvas, item, position):
    moneyType, price, x = app.shop[item] # we throw away x
    if position == "buy pop up":
        canvas.create_text(100, 227, anchor = NW, text = f"Buy {item}?", fill = "#613037", 
        font = "Inter 12 bold")
        x, y = 97, 243
        x0, y0 = 120, 372
    elif position == "place pop up":
        if app.itemToPlace not in app.myInventory.placed:
            canvas.create_text(108, 227, anchor = NW, text = f"Place {item}?", fill = "#613037", 
            font = "Inter 12 bold")
        elif app.itemToPlace in app.myInventory.placed:
            canvas.create_text(100, 227, anchor = NW, text = f"Remove {item}?", fill = "#613037", 
            font = "Inter 12 bold") 
        x, y = 97, 243
        x0, y0 = 120, 372
    elif position == "food":
        x, y = 22, 520
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'{item}')))
        canvas.create_image(x, y, anchor = NW, image = display)
    # item positions:  
    # top left (4, 139), text (27, 269)
    # top right (187, 139), text (210, 268)
    # and so on...
    elif position == "UL": 
        x, y = 4, 139
        x0, y0 = 27, 269 #nw coordinate of text 
    elif position == "UR":
        x, y = 185, 139
        x0, y0 = 210, 268 
    elif position == "DL":
        x, y = 4, 293
        x0, y0 = 27, 421  
    elif position == "DR":
        x, y = 187, 292
        x0, y0 = 210, 420 
    if moneyType == "goldfish":
        if app.currentPage == "shop": # draw white background and sparkle for goldfish items
            display = ImageTk.PhotoImage(Image.open(getImagePath('whiteBackground')))
            canvas.create_image(x, y, anchor = NW, image = display)
            itemImage = ImageTk.PhotoImage(Image.open(getImagePath(f'{item}')))
            canvas.create_image(x, y, anchor = NW, image = itemImage)
            canvas.create_text(x0, y0, anchor = NW, text = f"Price: {price} Goldfish", fill = "#e8be79",
            font = "Inter 12 bold")
            sparkle = ImageTk.PhotoImage(Image.open(getImagePath(f'sparkle{app.sparkleFrame}')))
            canvas.create_image(x, y, anchor=NW, image = sparkle) 
        elif app.currentPage == "goodies": # do not want white background on goodies page
            itemImage = ImageTk.PhotoImage(Image.open(getImagePath(f'{item}')))
            canvas.create_image(x, y, anchor = NW, image = itemImage)
    if moneyType == "fish":
        itemImage = ImageTk.PhotoImage(Image.open(getImagePath(f'{item}')))
        canvas.create_image(x, y, anchor = NW, image = itemImage)
        if app.currentPage == "shop":
            canvas.create_text(x0, y0, anchor = NW, text = f"Price: {price} Fish", fill = "#6ea6bd",
        font = "Inter 12 bold")
        
def drawGoodies(app, canvas): 
    drawGoodiesPage(app, canvas)
    if app.showOpenYardPositions == True:
        drawYardPositions(app, canvas)

def drawGoodiesPage(app, canvas):
    if app.goodiesPageNumber == 1:
        for item in app.page1:
            cell = app.page1[item][2]
            drawItem(app, canvas, item, cell) 
            if item not in app.myInventory.catalog:
                drawItemUnavailable(app, canvas, cell)
            if item in app.myInventory.placed:
                drawAlreadyPlaced(app, canvas, cell)
    elif app.goodiesPageNumber == 2:
        for item in app.page2:
            cell = app.page2[item][2]
            drawItem(app, canvas, item, cell) 
            if item not in app.myInventory.catalog:
                drawItemUnavailable(app, canvas, cell)
            if item in app.myInventory.placed:
                drawAlreadyPlaced(app, canvas, cell)
    elif app.goodiesPageNumber == 3:
        for item in app.page3:
            cell = app.page3[item][2]
            drawItem(app, canvas, item, cell) 
            if item not in app.myInventory.catalog:
                drawItemUnavailable(app, canvas, cell)
            if item in app.myInventory.placed:
                drawAlreadyPlaced(app, canvas, cell)
    elif app.goodiesPageNumber == 4:
        for item in app.page4:
            cell = app.page4[item][2]
            drawItem(app, canvas, item, cell) 
            if item not in app.myInventory.catalog:
                drawItemUnavailable(app, canvas, cell)
            if item in app.myInventory.placed:
                drawAlreadyPlaced(app, canvas, cell)
    elif app.goodiesPageNumber == 5:
        for item in app.page5:
            cell = app.page5[item][2]
            drawItem(app, canvas, item, cell) 
            if item not in app.myInventory.catalog:
                drawItemUnavailable(app, canvas, cell)
            if item in app.myInventory.placed:
                drawAlreadyPlaced(app, canvas, cell)
    if app.chosenItemPosition != None and (app.itemToPlace in app.myInventory.catalog):
        display = ImageTk.PhotoImage(Image.open(getImagePath('yes or no')))
        canvas.create_image(0,0, anchor=NW, image=display)
        drawItem(app, canvas, app.itemToPlace, "place pop up")
    return None
        
def drawAlreadyPlaced(app, canvas, cell):
    display = ImageTk.PhotoImage(Image.open(getImagePath(f'already placed {app.goodiesFrame}')))
    if cell == "UL":
        x, y = (6, 138)
    elif cell == "UR":
        x, y = (190, 137)
    elif cell == "DL":
        x, y = (6, 293)
    elif cell == "DR":
        x, y = (188, 292)
    canvas.create_image(x,y, anchor=NW, image=display)

def drawItemUnavailable(app, canvas, cell):
    display = ImageTk.PhotoImage(Image.open(getImagePath(f'item not available {app.goodiesFrame}')))
    if cell == "UL":
        x, y = (6, 138)
    elif cell == "UR":
        x, y = (190, 137)
    elif cell == "DL":
        x, y = (6, 293)
    elif cell == "DR":
        x, y = (188, 292)
    canvas.create_image(x,y, anchor=NW, image=display)
    
def drawYardPositions(app, canvas): # for placing goods
    # draw background
    display = ImageTk.PhotoImage(Image.open(getImagePath('background')))
    canvas.create_image(0,0, anchor=NW, image=display)
    drawYard(app, canvas)
    treeStump = ImageTk.PhotoImage(Image.open(getImagePath('tree stump')))
    canvas.create_image(375, 667, anchor=SE, image=treeStump)
    if app.myYard.itemPositions[app.stump] != False: 
        item = app.myYard.itemPositions[app.stump]
        x,y = app.stump.coordinates()
        display = ImageTk.PhotoImage(Image.open(getImagePath(f"{item}")))
        canvas.create_image(x, y + 60, anchor = S, image = display)
        if app.myYard.catPositions[app.stump] != False:
                cat = app.myYard.catPositions[app.stump]
                x, y = app.stump.coordinates()
                drawCatPose(app, canvas, cat, item, (x,y))
    for position in app.myYard.itemPositions: 
        if app.myYard.itemPositions[position] == False: 
            drawArrow(app, canvas, position.coordinates()) 
    

def drawArrow(app, canvas, coordinates):
    x, y = coordinates
    display = ImageTk.PhotoImage(Image.open(getImagePath('arrow')))
    if app.currentPage == "goodies" and coordinates != (110, 610): # exclude food
        arrowDisplacement = [0, 3, 6, 4, 2]
        canvas.create_image(x, y - arrowDisplacement[app.goodiesFrame], anchor = S, image = display)
    elif app.currentPage == "yard":
        arrowDisplacement = [0, 2, 4, 8, 4, 2, 1]
        canvas.create_image(x, y - arrowDisplacement[app.yardFrame], anchor = S, image = display)
        canvas.create_text(110, 550 - arrowDisplacement[app.yardFrame], 
        text = "place food", font = "Inter 12 bold", fill = "#9c3337")
    return None

def drawGiftsPage(app, canvas):
    totalCells = 5
    cellsToCover = totalCells - len(app.giftsNotReceived)
    y0 = 630
    y1 = 630 - cellsToCover*111 
    canvas.create_rectangle(30, y0, 350, y1, fill = "#AFCF91", 
        outline = "#AFCF91")
    drawingCellIndex = min(5, len(app.giftsNotReceived))
    for cell in range(drawingCellIndex):
        gift = app.giftsNotReceived[cell]
        drawGiftCell(app, canvas, gift, cell)

    return None

def drawGiftCell(app, canvas, gift, cell):
    y = 100 + cell*110
    canvas.create_text(140, y, anchor = NW, text = f"{gift.givenFrom} gifted \nyou {gift.quantity} {gift.moneyType}!",
    font = "Inter 14 bold", fill = "#7D3E3B")
    display = ImageTk.PhotoImage(Image.open(getImagePath(f'{gift.givenFrom} tiny face')))
    y = 110 + cell*110
    canvas.create_image(60, y, anchor = NW, image = display) 

def drawCatPose(app, canvas, cat, item, coordinates):
    x, y = coordinates
    if item in app.balls:
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'{cat.name} sleeping')))
        canvas.create_image(x, y + 30, anchor = S, image = display) 
    if item in app.lowSittingPillows:
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'{cat.name} sitting'))) 
        canvas.create_image(x, y + 30, anchor = S, image = display) 
    if item in app.highSittingPillows:
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'{cat.name} sleeping')))
        canvas.create_image(x - 3, y + 8, anchor = S, image = display) 
    if item in app.houses: 
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'{cat.name} sleeping')))
        canvas.create_image(x + 1, y + 57, anchor = S, image = display) 
        display = display = ImageTk.PhotoImage(Image.open(getImagePath(f'{item} top')))
        canvas.create_image(x, y - 18, image = display) 

def mousePressedGifts(app, x, y):
    if (6 <= x <= 125) and (7 <= y <= 50):
        app.overlay = "menu"
        return None
    if (141 <= x <= 323):
        if (148 <= y <= 176) and len(app.giftsNotReceived) >= 1: # cell 0
            gift = app.giftsNotReceived.pop(0)
            gift.receive(app.myInventory)
        elif (258 <= y <= 286) and len(app.giftsNotReceived) >= 2: # cell 1
            gift = app.giftsNotReceived.pop(1)
            gift.receive(app.myInventory)
        elif (368 <= y <= 396) and len(app.giftsNotReceived) >= 3: # cell 2
            gift = app.giftsNotReceived.pop(2)
            gift.receive(app.myInventory)
        elif (478 <= y <= 506) and len(app.giftsNotReceived) >= 4: # cell 3
            gift = app.giftsNotReceived.pop(3)
            gift.receive(app.myInventory)
        elif (588 <= y <= 616) and len(app.giftsNotReceived) >= 5: # cell 4 
            gift = app.giftsNotReceived.pop(4)
            gift.receive(app.myInventory)
    return None

def mousePressedYard(app, x, y):
    if (80 <= x <= 150) and (530 <= y <= 640) and app.overlay == None and app.myYard.food == None: # the arrow to choose food
        app.overlay = "place food"
        app.chooseFoodType = "Frisky Bitz"
        return None
    elif app.overlay == "place food":
        if pressedYes(x,y) == True:
            if app.myInventory.pantry[app.chooseFoodType] > 0:
                app.myInventory.pantry[app.chooseFoodType] -= 1
                app.myYard.food = app.chooseFoodType
                app.myYard.foodLevel = 24
                app.overlay = None
            else:
                app.overlay = None
                app.currentPage = "shop"
                app.shopPageNumber = 0
                app.cellOfItem = None
                app.sparkleFrame = 0
            return None
        elif pressedNo(x,y) == True: # release 'place food' overlay
            app.overlay = None
            return None

    # display food level when food is clicked on
    elif (80 <= x <= 150) and (530 <= y <= 640) and app.overlay == None and app.myYard.food != None:
        app.overlay = "display food level"
        return None
    elif app.overlay == "display food level":
        if (90 <= x <= 102) and (250 <= y <= 272):
            app.overlay = None
    return None

def mousePressedMenu(app, x,y):
    if (142 <= x and x <= 234) and (324 <= y and y <= 398):
            app.overlay = None
            app.currentPage = "yard"
            app.yardFrame = 0
            app.startBestArrangements = False
    elif inCatsButton(x,y) == True:
            app.overlay = None
            app.currentPage = "cats"
            app.catsPageNumber = 0
            app.catFrame = 0
    elif inShopButton(x,y) == True:
            app.overlay = None
            app.currentPage = "shop"
            app.shopPageNumber = 0
            app.cellOfItem = None
            app.sparkleFrame = 0
    elif inGoodiesButton(x,y) == True:
            app.overlay = None
            app.currentPage = "goodies"
            app.chosenItemPosition = None
            app.showOpenYardPositions = False
            app.goodiesPageNumber = 1
            app.goodiesFrame = 0
    elif inGiftsButton(x,y) == True:
            app.overlay = None
            app.currentPage = "gifts"
            app.giftsFrame = 0
    return None

def mousePressedSleep(app, x, y):
    app.overlay = None
    if (96 <= x and x <= 285) and (283 <= y and y <= 330):
        app.currentPage = "yard"
        app.playSleepAnimation = True
        app.sleepFrame = 0
        return sleep20Minutes(app)
    elif (95 <= x and x <= 284) and (336 <= y and y <= 382):
        app.playSleepAnimation = True
        app.currentPage = "yard"
        app.sleepFrame = 0
        return sleep1Hour(app)
    elif (95 <= x and x <= 284) and (388 <= y and y <=434):
        app.playSleepAnimation = True
        app.currentPage = "yard"
        app.sleepFrame = 0
        return sleep8Hours(app)
    return None

def choose5Cats(app, x, y):
    if 335 <= y <= 385: 
        row = 0
    elif 394 <= y <= 444: 
        row = 1
    elif 453 <= y <= 503:
        row = 2
    else: return None # not in zone
    if 41 <= x <= 94:
        col = 0
    elif 101 <= x <= 154:
        col = 1
    elif 161 <= x <= 214:
        col = 2
    elif 221 <= x <= 274:
        col = 3
    elif 281 <= x <= 334:
        col = 4
    else: return None
    cellNumber = row*5 + col
    chosenCat = app.catsList[cellNumber] 
    if chosenCat not in app.setOfCats and len(app.setOfCats) < 5:
        app.setOfCats.add(chosenCat)
    elif chosenCat in app.setOfCats:
        app.setOfCats.remove(chosenCat)

def mousePressedBuyItem(app, x,y):
    if pressedYes(x,y) == True:
        if getItem(app)!= None: item = getItem(app)
        # index first two items of app.shop[item] to get tuple (moneyType, price)
        if app.myInventory.buy(item, app.shop[item][:2]) == "not enough money": 
            app.cellOfItem = None # close pop up
            app.overlay = "no money" # triggers pop up in redraw all 
        else: 
            app.cellOfItem = None # close pop up
    if pressedNo(x,y) == True:
        app.cellOfItem = None # close pop up
    return None

def mousePressedShop(app, x,y):
    if (6 <= x and x <= 123) and (10 <= y and y <= 64): # click on shop button
        app.overlay = "menu"
        return None
    if app.cellOfItem == None:
        if inTopLeft(x,y) == True:
            app.cellOfItem = "UL"
        elif inTopRight(x,y) == True:
            app.cellOfItem = "UR"
        elif inBottomLeft(x,y) == True:
            app.cellOfItem = "DL"
        elif inBottomRight(x,y) == True:
            app.cellOfItem = "DR"
        return None
    if app.cellOfItem != None: # overlay is up, check if Y/N buttons pressed
        return mousePressedBuyItem(app, x, y)

def chooseCellAndItemToPlace(app, x, y): # placing and removing items from yard
    if inTopLeft(x,y) == True:
        app.chosenItemPosition = "UL"
    elif inTopRight(x,y) == True:
        app.chosenItemPosition = "UR"
    elif inBottomLeft(x,y) == True:
        app.chosenItemPosition = "DL"
    elif inBottomRight(x,y) == True:
        app.chosenItemPosition = "DR"
    app.itemToPlace = getItem(app)
    if app.itemToPlace in app.myInventory.placed:
        app.placeOrRemove = "remove"
    else:
        app.placeOrRemove = "place"
    return None

def mousePressedGoodies(app, x,y): 
    if (6 <= x and x <= 123) and (10 <= y and y <= 64): # click on title button
        app.overlay = "menu"
        return None 
    if app.chosenItemPosition == None:
        return chooseCellAndItemToPlace(app, x, y)
    if app.chosenItemPosition != None: # we have chosen an item. the 'place item?' pop up is up
        if pressedYes(x,y) == True:
            if app.placeOrRemove == "remove":
                app.myInventory.removeGood(app.myYard, app.itemToPlace)
                app.chosenItemPosition = None
            else:
                app.showOpenYardPositions = True 
            return None
        if app.showOpenYardPositions == True: # place the item
            if clickedOnPosition(app, x, y)!= None: # statement checks if we clicked a valid area
                position = clickedOnPosition(app, x, y) 
                app.myInventory.placeItem(app.itemToPlace, app.myYard, position)
                app.chosenItemPosition = None
                app.currentPage = "yard"
                app.startBestArrangements = False
                if app.myInventory.bestArrangementConditions() == True:
                    app.startBestArrangements = True
                    app.startButtonPressed = False
                    app.setOfCats = set()
                    app.overlay = "best arrangement instructions"
                    app.solution = None
                    app.startBestArrangementAnimationTime = app.timePassed
            else: 
                app.chosenItemPosition = None # close pop up
        if pressedNo(x,y) == True:
            app.chosenItemPosition = None # close pop up
        return None

def clickedOnPosition(app, x, y): # choose position to place good
    if (162 <= x <= 230) and (230 <= y <= 310): # within range
        return app.bench
    elif (40 <= x <= 110) and (310 <= y <= 400):
        return app.porch
    elif (210 <= x <= 280) and (390 <= y <= 480):
        return app.carpetBack
    elif (100 <= x <= 170) and (440 <= y <= 530):
        return app.carpetFront
    elif (246 <= x <= 314) and (475 <= y <= 540):
        return app.stump
    return None

def randomVisits(app, numberOfVisits): 
    for visit in range(numberOfVisits*3):
        catName = random.choice(app.catsList)
        catVisiting = app.cats[catName]
        if catVisiting.visiting == False:
            app.myYard.spawn(catVisiting, app.normalItems, app.rareItems, app.normalCats, app.rareCats)
    return None

def sleep20Minutes(app):
    for catName in app.cats: # evict current cats
        kitty = app.cats[catName]
        if kitty.visiting == True:
            kitty.visitTime += 12000
    randomVisits(app, 5)
    for catName in app.cats: 
        kitty = app.cats[catName]
        if kitty.visiting == True:
            kitty.visitTime += 12000
            kitty.updateTime(app, app.myYard) 
    app.timePassed += 12000
    trueOrFalse = [0,1]
    spawnCat = random.choice(trueOrFalse)
    if spawnCat == 1:
        catName = random.choice(app.catsList)
        kitty = app.cats[catName]
        if kitty.visiting == False and len(app.myInventory.placed) < 5:
                app.myYard.spawn(kitty, app.normalItems, app.rareItems, app.normalCats, app.rareCats)
    return None

def sleep1Hour(app):
    for catName in app.cats:
        kitty = app.cats[catName]
        if kitty.visiting == True:
            kitty.visitTime += 36000
    randomVisits(app, 10)
    for catName in app.cats:
        kitty = app.cats[catName]
        if kitty.visiting == True:
            kitty.visitTime += 36000
            kitty.updateTime(app, app.myYard)
    app.timePassed += 36000
    trueOrFalse = [0,1]
    spawnCat = random.choice(trueOrFalse)
    if spawnCat == 1:
        catName = random.choice(app.catsList)
        kitty = app.cats[catName]
        if kitty.visiting == False and len(app.myInventory.placed) < 5:
                app.myYard.spawn(kitty, app.normalItems, app.rareItems, app.normalCats, app.rareCats)
    return None

def sleep8Hours(app): 
    for hour in range(8):
        sleep1Hour(app)
    return None

def drawStartBackTracking(app, canvas):
    canvas.create_rectangle(0, 0, 375, 667, fill = "#C4D3D9")
    frame = app.timePassed - app.startBestArrangementAnimationTime + 1
    if frame <= 17:
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'start best arrangement {frame}')))
    elif frame > 17:
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'start best arrangement 17')))
    if app.solution == "does not exist":
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'sol does not exist')))
    elif app.solution == "choose 5":
        display = ImageTk.PhotoImage(Image.open(getImagePath(f'choose 5')))
    canvas.create_image(0,0, anchor=NW, image = display)
    if frame > 17: drawCatCells(app, canvas)
    return None

def drawCatCells(app, canvas):
    for row in range(3):
        y = 337 + row*59
        for col in range(5):
            x = 38 + col*60
            cellNumber = row*5 + col
            catName = app.catsList[cellNumber]
            display = ImageTk.PhotoImage(Image.open(getImagePath(f'{catName} tiny face')))
            canvas.create_image(x, y, anchor = NW, image = display)
            if catName in app.setOfCats: # draw checkmark
                display = ImageTk.PhotoImage(Image.open(getImagePath(f'check')))
                canvas.create_image(x + 3, y - 4, anchor = NW, image = display)
                

def bestArrangement(app):
    setOfCats = app.setOfCats
    listOfPositions = []
    for position in app.myYard.itemPositions:
        listOfPositions.append(position)
    return bestArrangementHelper(app, dict(), listOfPositions, setOfCats)

def bestArrangementHelper(app, solution, listOfPositions, setOfCats): # set of cats has names of cats
    if listOfPositions == []:
        return solution
    position = listOfPositions[0]
    item = app.myYard.itemPositions[position]
    for catName in setOfCats:
        kitty = app.cats[catName]
        if item == kitty.favoriteItem and position.name == kitty.favoritePosition: # checks if pairing is legal 
            solution[position] = catName
            setOfCats.remove(catName)
            result = bestArrangementHelper(app, solution, listOfPositions[1:], setOfCats)
            if result != None:
                return result
            del solution[position]
            setOfCats.add(catName)
    return None

def stringToSet(string): # helper function
    if string == "set()":
        return set()
    result = set()
    string = string[1:-1]
    elems = string.split(", ")
    for elem in elems:
        while "'" in elem:
            i = elem.index("'")
            elem = elem[:i] + elem[i + 1:]
        while '"' in elem:
            i = elem.index('"')
            elem = elem[:i] + elem[i + 1:]
        result.add(elem)
    return result

def stringToDictionary(string): # helper function
    if string == "{}" or string == "dict()":
        return dict()
    result = dict()
    string = string[1:-1] # remove dictionary brackets
    listOfPairs = string.split(", ")
    for pair in listOfPairs:
        while "'" in pair: # remove quotes
            i = pair.index("'") 
            pair = pair[:i] + pair[i+1:]
        separateList = pair.split(": ")
        key, val = separateList[0], separateList[1]
        result[key] = val
    return result

def stringToList(string):
    string = string[1:-1] # remove list brackets 
    elems = string.split(", ")
    result = []
    for elem in elems:
        while "'" in elem:
            i = elem.index("'")
            elem = elem[:i] + elem[i + 1:]
        while '"' in elem:
            i = elem.index('"')
            elem = elem[:i] + elem[i + 1:]
        result.append(elem)
    return result

def stringTo2DList(string):
    string = string[1:-1]
    elems = string.split(", [")
    result = []
    for elem in elems:
        if elem[0] != '[':
            elem = '[' + elem
        elem = stringToList(elem)
        result.append(elem)
    return result
            

def saveCats(app):
    catProgressList = []
    for catName in app.catsList:
        kitty = app.cats[catName]
        catProgressList.append(kitty.getInfo())
    return catProgressList
    
def saveProgress(app):
    fileName = input("Enter your name: ") # write getInfo functions for everything
    progress = f"""YARD: {app.myYard.getInfo()} \nINVENTORY: {app.myInventory.getInfo()} \nCATS: {saveCats(app)} \nTIME: {app.timePassed}"""
    f = open(f"{fileName}.txt", "w") # creates file, from https://www.freecodecamp.org/news/file-handling-in-python/
    f.writelines(progress)
    f.close()

def readFile(app, code): 
    for line in code.splitlines(): # from 11-29-22 15-112 lecture
        line = line.strip()
        if line.startswith("YARD"):
            yardInfo = line[7:-1] # removes brackets from tuple
            yardInfo = yardInfo.split(", 'sep', ")
            setYard(app, yardInfo)
        elif line.startswith("INVENTORY"):
            inventoryInfo = line[12: -1]
            inventoryInfo = inventoryInfo.split(", 'sep', ")
            setInventory(app, inventoryInfo)
        elif line.startswith("CATS"):
            catInfo = line[6:] 
            setCats(app, catInfo)
        elif line.startswith("TIME"):
            app.timePassed = int(line[6:])
    print("progress restored successfully!")
    return None

def setYard(app, yardInfo):
    itemPositions = dict()
    badDictionary = stringToDictionary(yardInfo[0]) # we want the keys to be the position object, not the name of the position
    for key in badDictionary: 
        object = app.yardPositionNames[key]
        if badDictionary[key] == "False":
            itemPositions[object] = False
        else: itemPositions[object] = badDictionary[key]
    app.myYard.itemPositions = itemPositions
    catPositions = dict()
    badDictionary = stringToDictionary(yardInfo[1])
    for key in badDictionary:
        object = app.yardPositionNames[key]
        if (badDictionary[key]) == "False":
            catPositions[object] = False
        else:
            catName = badDictionary[key]
            catPositions[object] = app.cats[catName] # want cat as object, not as string
    app.myYard.catPositions = catPositions
    app.myYard.itemPositionsList = stringToList(yardInfo[2])
    while "'" in yardInfo[3]:
        i = yardInfo[3].index("'")
        yardInfo[3] = yardInfo[3][:i] + yardInfo[3][i + 1:]
    while '"' in yardInfo[3]:
        i = yardInfo[3].index('"')
        yardInfo[3] = yardInfo[3][:i] + yardInfo[3][i + 1:] # remove quotes
    food = yardInfo[3]
    if food == "None":
        food = None
    app.myYard.food = food
    app.myYard.foodLevel = int(yardInfo[4])

def setInventory(app, inventoryInfo):
    # fix inventory.money
    badDictionary = stringToDictionary(inventoryInfo[0])
    money = dict()
    for key in badDictionary:
        money[key] = int(badDictionary[key]) # convert string to quantity
    app.myInventory.money = money
    # fix inventory.pantry 
    badDictionary = stringToDictionary(inventoryInfo[1])
    pantry = dict()
    for key in badDictionary:
        pantry[key] = int(badDictionary[key]) # convert string to quantity
    app.myInventory.pantry = pantry
    app.myInventory.catalog = stringToSet(inventoryInfo[2])
    app.myInventory.placed = stringToSet(inventoryInfo[3])

def setCats(app, catInfo):
    i = 0 
    catInfo = stringTo2DList(catInfo)
    while i < len(app.catsList):
        catName = app.catsList[i]
        kitty = app.cats[catName]
        info = catInfo[i]
        # there may be a dictionary inside info!
        visits = int(info[0])
        if info[-3] == "False":
            visiting = False
        else:
            visiting = True
        if info[-2] == "None":
            visitTime = None
        elif info[-2] == "False":
            visitTime = False
        elif info[-2] == "True":
            visitTime = True
        else:
            visitTime = int(info[-2])
        timeToLeave = int(info[-1])
        info = info[1: -3] # chop off non-dictionary elements
        if info[0].startswith("{") and info[0].endswith("}"):
            itemsFrequency = stringToDictionary(info[0])
            for key in itemsFrequency:
                itemsFrequency[key] = int(itemsFrequency[key])
        else: 
            itemsFrequency = dict()
            for j in info:
                if j.startswith("{"): # remove bracket
                    j = j[1:]
                if j.endswith("}"):
                    j = j[:-1]
                pair = j.split(": ") # separate key and value 
                itemsFrequency[pair[0]] = int(pair[1])
        kitty.updateInfo(visits, itemsFrequency, visiting, visitTime, timeToLeave)
        i += 1

def display():
    width = 375
    height = 667
    runApp(width=width, height=height)

def main():
    display()

if __name__ == '__main__':
    main()
    pass
