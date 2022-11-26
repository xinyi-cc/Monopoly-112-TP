from cmu_112_graphics import *

import random, tkinter

##########################################
# Grid class
##########################################

class Grid:
    def __init__(self, gridName, gridPriceToBuy):
        self.name = gridName
        self.owner = None
        self.priceToBuy = gridPriceToBuy
        self.priceToUpgrade = int(0.4 * self.priceToBuy)
        
        self.level = 0
        self.toll = 0
        self.priceToSell = int(self.priceToBuy * 0.7)

        self.chargeTolls = False
    
    def buying(self, owner):
        self.owner = owner
        self.level = 1
        self.chargeTolls = True
        self.toll = int(4 * 0.1 * self.priceToBuy)

    def upgrading(self):
        self.level += 1
        self.toll += int(4 * 0.1 * self.priceToBuy)

    def selling(self):
        self.owner = None
        self.toll -= int(4 * 0.1 * self.priceToBuy)

    def __repr__(self): ####need to improve
        return f'{self.name}'
        


##########################################
# Board class
##########################################
board1 = [[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
          [0,0,0,0,0,0,0,0,0,1,1,1,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
          [1,1,1,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,1,1,1,1,1,1,1,1,0,0,0,0,0]
]



board2 = [[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1],
          [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]
]

board3 = [[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,1,1,1,1,1,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
          [0,0,0,1,0,0,0,0,0,1,1,1,1,1,1],
          [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
]

board4 = [[0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
          [1,1,1,1,0,0,0,0,0,0,0,1,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
          [1,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]



class Board():
    def __init__(self, selectedBoard):
        self.map = selectedBoard
        self.detailedInfo = self.makeDetailedInfo()
    
    def makeDetailedInfo(self):

        nameList = ['Peak District', 'Lake District', 'Snowdonia', 'Dartmoor',
                    'Pembrokeshire Coast', 'North York Moors','Yorkshire Dales',
                    'Exmoor', 'Northumberland', 'Brecon Beacons', 'The Broads',
                    'Cairngorms', 'New Forest', 'South Downs',
                    'Royal Gorge Park', 'Falls Park', 'Scioto Audubon',
                    'Rifle Mountain Park', 'Fairmount Park', 'City Park',
                    'Zilker Park', 'The Gathering Place', 'Papago Park']
        index = 0
        detailedInfo = dict()
        rows, cols = self.getDims()
        for row in range(rows):
            for col in range(cols):
                coord = (row, col)
                if self.map[row][col] != 0:
                    if index == 7:
                        gridName = 'prison'
                    elif 0 < index % 7 % 4 <= 3:
                        gridName = None
                        gridPriceToBuy = 0
                    else:
                        gridName = random.choice(nameList)
                        gridPriceToBuy = random.randint(3000, 6000)
                    if (gridName is not None) and (gridName is not 'prison'):
                            nameList.remove(gridName)
                    detailedInfo[coord] = dict()
                    self.map[row][col] = Grid(gridName, gridPriceToBuy) #####
                    grid = self.map[row][col]
                    if gridName != None:
                        detailedInfo[coord]['property name'] = gridName
                        detailedInfo[coord]['price to buy'] = grid.priceToBuy
                        if grid.owner != None:
                            detailedInfo[coord]['owner'] = grid.owner
                            detailedInfo[coord]['cost to upgrade'] = (
                                                            grid.priceToUpgrade)
                            detailedInfo[coord]['toll'] = (grid.toll)
                        detailedInfo[coord]['owner'] = 'No Owner'
                    else:
                        detailedInfo[coord] = None
                    index += 1
        return detailedInfo


    def getDims(self):
        rows = len(self.map)
        cols = len(self.map[0])
        return rows, cols

    def getRandomPlace(self): 
        rows, cols = self.getDims()
        if True:
            row = random.randint(0, rows-1)
            for col in range(cols):
                if self.map[row][col]:
                    return row, col



##########################################
# Player class
##########################################




class Player:
    def __init__(self, app, playerName):
        # self.loc = app.myBoard.getRandomPlace() #returns a tuple
        self.cards = []
        self.myTurn = False
        self.myProperties = []
        self.money = 50000
        # self.ori = self.checkOri(app)
        # self.color = random.choice(colors)
        # colors.remove(self.color)
        self.playerName = playerName
    
    
    def __repr__(self):
        return f'Player {self.playerName}'
 

    def isLegalMove(self, app, checkingMove):
        curLocRow, curLocCol = self.loc
        dRow, dCol = checkingMove
        boardRows, boardCols = app.myBoard.getDims()

        if ((0 <= curLocRow + dRow < boardRows) and 
            (0 <= curLocCol + dCol < boardCols) and
            isinstance(app.myBoard.map[curLocRow + dRow][curLocCol + dCol], Grid)):
            return True
        return False


    def checkOri(self, app):
        leftMove = (0, -1)
        rightMove = (0, +1)
        upMove = (+1, 0)
        downMove = (-1, 0)
        for i in (rightMove, leftMove, downMove, upMove):
            if self.isLegalMove(app, i):
                ori = i
                return ori


    def changeOri(self, app): #only modify self.ori
        lastOri = self.ori
        leftMove = (0, -1)
        rightMove = (0, +1)
        upMove = (+1, 0)
        downMove = (-1, 0)
        availableOris = [rightMove, leftMove, downMove, upMove]
        if lastOri == rightMove:
            availableOris.remove(leftMove)
        elif lastOri == leftMove:
            availableOris.remove(rightMove)
        elif lastOri == downMove:
            availableOris.remove(upMove)
        else:
            availableOris.remove(downMove)

        for checkingMove in availableOris:
            if self.isLegalMove(app, checkingMove):
                self.ori = checkingMove

    def playDice(self):
        dice = random.randint(1,6)
        return dice

    def move(self, app, dice): # only modify self.loc
        curLocRow, curLocCol = self.loc
        for _ in range(dice):
            if not self.isLegalMove(app, self.ori):
                self.changeOri(app)
            curLocRow += self.ori[0]
            curLocCol += self.ori[1]
            self.loc = curLocRow, curLocCol
            app.playerInfo[app.curPlayer]['loc'] = self.loc
    

    def changeMyTurn(self):
        self.myTurn = True
        

    def buyProperty(self, app):
        curRow, curCol = self.loc
        grid = app.myBoard.map[curRow][curCol]
        # modify the params of the grid
        grid.buying(self)

        # modify the params of players
        self.myProperties.append(grid)
        self.money -= grid.priceToBuy


    def upgradeProperty(self, app): # modify params of player and return msg
        curRow, curCol = self.loc
        grid = app.myBoard.map[curRow][curCol]
        if self.money < grid.priceToUpgrade:
            return "No enough money to upgrade!"
        elif self.money >= grid.priceToUpgrade:
            self.money -= grid.priceToUpgrade
            # modify the params of the grid
            grid.upgrading()
            return "Successfully upgraded the property."


    def sellProperty(self, app):
        curRow, curCol = self.loc
        grid = app.myBoard.map[curRow][curCol]
        # modify the params of players
        self.money += grid.priceToSell
        self.myProperties.remove(grid)

        # modify the params of the grid
        grid.selling()
        return f'''Successfully sold {grid.name}.\
Now you have {self.money} dollars left.\
        '''

# The concept of mode is learnt from 112 course website
##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, app.height/3, text='Monopoly',
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2.5, 
                       text='Press y to start the game!',
                       font=font, fill='black')


def splashScreenMode_keyPressed(app, event):
    if event.key == 'y':
        app.mode = 'playerSettingMode'

# ##########################################
# # Player setting Mode
# ##########################################

def playerSettingMode_redrawAll(app, canvas):
    font = font = 'Times 28 bold italic'
    
    canvas.create_text(app.width/2, app.height/8, 
                       text=app.message,
                       font=font, fill='black')
    canvas.create_text(app.width/7, app.height/8, 
                       text=f"Player number: {app.playerNum}",
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2, 
                       text=f"Press 'y' to start the game!",
                       font=font, fill='black')


def playerSettingMode_mousePressed(app, event):
    name = app.getUserInput('Please enter your name:)')
    if app.playerNum < 4:
        if name != None:
            app.playerNum += 1
            app.message = 'Successfully add a player'
            app.playerNameList.append(name)
    if app.playerNum == 4:
            app.message = '''
                Has reached the maximum of players. Let's start the game!
            '''
        
        

def playerSettingMode_keyPressed(app, event):
    if event.key == 'y':
        if app.playerNum < 2:
            app.message = "Please add at least two player in total."
        else:
            app.mode = 'mapChooseMode'
    



# ##########################################
# # Map Choose Mode
# ##########################################

def mapChooseMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, app.height/8, 
                       text="Please press left and right key to choose the map",
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/5.7, 
                       text="Press 'y' to start the game!",
                       font=font, fill='black')
    mapChooseMode_drawBoard(app, canvas)


def mapChooseMode_keyPressed(app, event):

    if event.key == 'Left':
        app.index = max(1, app.index-1)
        
    elif event.key == 'Right':
        app.index = min(app.index+1, 4)
    
    if app.index == 1:
        app.myBoard = Board(board1)
    elif app.index == 2:
        app.myBoard = Board(board2)
    elif app.index == 3:
        app.myBoard = Board(board3)
    elif app.index == 4:
        app.myBoard = Board(board4)

    if event.key == 'y':
        # set players
        for playerName in app.playerNameList:
            player = Player(app, playerName)
            app.playerInfo[player] = dict()
            loc = app.myBoard.getRandomPlace() #returns a tuple
            player.loc = loc
            app.playerInfo[player]["loc"] = player.loc
            app.playerInfo[player]["myTurn"] = player.myTurn
            # {Player ic: {'loc': (2, 11), 'myTurn': False}, Player lynn: {'loc': (6, 0), 'myTurn': False}}
            ori = player.checkOri(app)
            player.ori = ori
        app.playerInfoKeysList = list(app.playerInfo)
        app.curPlayer = app.playerInfoKeysList[app.curPlayerIndex-1] #app.playerNameList[0]
        app.whoseTurn = app.curPlayer
        # modify app mode
        app.mode = 'gameMode'
    


def mapChooseMode_drawBoard(app, canvas):
    rows, cols = app.myBoard.getDims()
    for row in range(rows):
        for col in range(cols):
            if app.myBoard.map[row][col] != 0:
                cx = app.gridWidth * col + app.width * 0.4
                cy = app.gridHeight * row
                placeGrid(app, canvas, cx, cy)

##########################################
# Game Mode
##########################################

def gameMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, 20, text='Game',
                       font=font, fill='black')
    x0Ins = app.width * 0.85
    y0Ins = app.height * 0.2
    x1Ins = app.width * 0.95
    y1Ins = app.height * 0.3
    
    canvas.create_oval(x0Ins, y0Ins, x1Ins, y1Ins, fill = 'white') # Instruction
    canvas.create_text(app.width * 0.8, app.height * 0.28, 
                       text = "Instruction", anchor = 'sw',
                       fill = 'black', font = font)

    x0Card = app.width * 0.85
    y0Card = app.height * 0.35
    x1Card = app.width * 0.95
    y1Card = app.height * 0.45
    canvas.create_oval(x0Card, y0Card, x1Card, y1Card, fill = 'white') # Special cards
    canvas.create_text(app.width * 0.845, app.height * 0.43, text = "Cards",
                       anchor = 'sw',
                       fill = 'black', font = font)
    gameMode_drawBoard(app, canvas)
    # gameMode_addPlayers(app)
    gameMode_drawPlayer(app, canvas)

    canvas.create_text(app.width/2, 35, text=f"now it's {app.whoseTurn}'s Turn.\
                                               Press 'r' to roll a dice.",
                       font=font, fill='black')
    if type(app.dice) != str:
        canvas.create_text(app.width/2, 45, text=f"You rolled {app.dice}.",
                           font=font, fill='blue')

    gameMode_drawGridInfo(app, canvas)


    

def gameMode_mousePressed(app, event):
    # instruction page and special cards mode
    x0Ins = app.width * 0.85
    y0Ins = app.height * 0.2
    x1Ins = app.width * 0.95
    y1Ins = app.height * 0.3
    x0Card = app.width * 0.85
    y0Card = app.height * 0.35
    x1Card = app.width * 0.95
    y1Card = app.height * 0.45
    
    if x0Ins < event.x < x1Ins and y0Ins < event.y < y1Ins:
        app.mode = 'instructionMode'
    elif x0Card < event.x < x1Card and y0Card < event.y < y1Card:
        app.mode = 'specialCardsMode'

    # click grids
    Isocx, Isocy = event.x, event.y
    twoDcx, twoDcy = isoToTwoD(Isocx, Isocy)
    col = int((twoDcx - app.width * 0.4) / app.gridWidth)
    row = int(twoDcy / app.gridHeight)
    print(f'You click [{row},{col}]')
    if (((row, col) in app.myBoard.makeDetailedInfo()) and 
        (app.myBoard.makeDetailedInfo()[(row, col)] != None)):
        print('it has gridInfo')
        app.gridInfo = app.myBoard.makeDetailedInfo()[(row, col)]


# def gameMode_timerFired(app):
#     printDetailedInfoOfGrid(app)
    
def gameMode_drawGridInfo(app, canvas):
    if app.gridInfo != None:
        font = 'Times 28 bold italic'
        # print(app.myBoard.makeDetailedInfo())
        # print(app.gridInfo)
        canvas.create_text(app.width/2, 200, 
                           text=app.gridInfo, font=font, fill='blue')


def gameMode_drawPlayer(app, canvas):
    
    for eachPlayer in app.playerInfo:
        
        loc = app.playerInfo[eachPlayer]['loc'] #returns a tuple
        # app.playerInfo[player]["loc"] = player.loc
        # ori = player.checkOri(app)
        # player.ori = ori

        
        twoDRow, twoDCol = loc[0], loc[1]

        cx = app.gridWidth * twoDCol + app.width * 0.4
        cy = app.gridHeight * twoDRow
        isoX, isoY = twoDToIso(cx, cy)
        playerRadius = 9
        x0 = isoX - playerRadius
        y0 = isoY - playerRadius
        x1 = isoX + playerRadius
        y1 = isoY + playerRadius
        canvas.create_oval(x0, y0, x1, y1, fill='black')
        
        # if app.playerInfo[eachPlayer]['myTurn'] == True:
        #     dice = eachPlayer.playDice()
        #     eachPlayer.move(app, dice)
        #     eachPlayer.myTurn = False


def gameMode_keyPressed(app, event):
    if event.key == 'r': # A player rolled the dice
        # app.mode = 'mapChooseMode'
        # after A rolled the dice, current turn changes
        app.dice = app.curPlayer.playDice()
        app.curPlayer.move(app, app.dice)
        app.curPlayer.myTurn = 'False'
        app.curPlayerIndex = (app.curPlayerIndex + 1) % app.playerNum
        app.curPlayer = app.playerInfoKeysList[app.curPlayerIndex-1]
        app.curPlayer.myTurn = 'True'
        app.whoseTurn = app.curPlayer
        




###########
#draw map
###########
# the concept of the calculation of isometric x and y is from 
# https://gamedevelopment.tutsplus.com/tutorials/
# creating-isometric-worlds-a-primer-for-game-developers--gamedev-6511
def twoDToIso(twoDx, twoDy):
    isoX = twoDx - twoDy
    isoY = (twoDx + twoDy) / 2
    return(isoX, isoY)

def gameMode_drawBoard(app, canvas):
    rows, cols = app.myBoard.getDims()
    for row in range(rows):
        for col in range(cols):
            if app.myBoard.map[row][col] != 0:
                cx = app.gridWidth * col + app.width * 0.4
                cy = app.gridHeight * row
                
                if app.myBoard.map[row][col].name == 'prison':
                    placePrisonGrid(app, canvas, cx, cy)
                elif app.myBoard.map[row][col].name == None:
                    placeNoneGrid(app, canvas, cx, cy)
                else:
                    placeGrid(app, canvas, cx, cy)
                    

def placeGrid(app, canvas, cx, cy):
    Isocx, Isocy = twoDToIso(cx, cy)

    isox0, isoy0 = Isocx, Isocy - app.gridHeight/2
    isox1, isoy1 = Isocx + app.gridWidth, Isocy
    isox2, isoy2 = Isocx, Isocy + app.gridHeight/2
    isox3, isoy3 = Isocx - app.gridWidth, Isocy
    coord = isox0, isoy0, isox1, isoy1, isox2, isoy2, isox3, isoy3
    canvas.create_polygon(coord, fill='pink', outline='black')


def placePrisonGrid(app, canvas, cx, cy):
    twoDcx, twoDcy = twoDToIso(cx, cy)

    isox0, isoy0 = twoDcx, twoDcy - app.gridHeight/2
    isox1, isoy1 = twoDcx + app.gridWidth, twoDcy
    isox2, isoy2 = twoDcx, twoDcy + app.gridHeight/2
    isox3, isoy3 = twoDcx - app.gridWidth, twoDcy
    coord = isox0, isoy0, isox1, isoy1, isox2, isoy2, isox3, isoy3
    canvas.create_polygon(coord, fill='yellow', outline='black')

def placeNoneGrid(app, canvas, cx, cy):
    twoDcx, twoDcy = twoDToIso(cx, cy)

    isox0, isoy0 = twoDcx, twoDcy - app.gridHeight/2
    isox1, isoy1 = twoDcx + app.gridWidth, twoDcy
    isox2, isoy2 = twoDcx, twoDcy + app.gridHeight/2
    isox3, isoy3 = twoDcx - app.gridWidth, twoDcy
    coord = isox0, isoy0, isox1, isoy1, isox2, isoy2, isox3, isoy3
    canvas.create_polygon(coord, fill='purple', outline='black')



###########
#click map
###########
# the concept of the calculation of twoD x and twoD y is from 
# https://gamedevelopment.tutsplus.com/tutorials/
# creating-isometric-worlds-a-primer-for-game-developers--gamedev-6511
def isoToTwoD(isoX, isoY):
    twoDx = (2 * isoY + isoX) / 2
    twoDy = (2 * isoY - isoX) / 2
    return twoDx, twoDy

##########################################
# Instruction Mode
##########################################

def instructionMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, 200, text='This is the instruction!', 
                       font=font, fill='black')
    canvas.create_text(app.width/2, 300, text='Press r to return to the game!',
                       font=font, fill='black')

def instructionMode_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'gameMode'

##########################################
# Special cards Mode
##########################################

def specialCardsMode_redrawAll(app, canvas):
    font = 'Times 28 bold italic'
    canvas.create_text(app.width/2, 200, 
                       text='Here are all the special cards you have!', 
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350, text='Press r to return to the game!',
                       font=font, fill='black')

def specialCardsMode_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'gameMode'


##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = 'splashScreenMode'
    app.gridHeight = 23
    app.gridWidth = 23
    app.myBoard = Board(board1)
    app.index = 1
    app.playerNum = 0
    app.message = 'Click the mouse to add a player!'
    app.playerNameList = list()
    app.playerInfo = dict()
    app.curPlayerIndex = 1
    # if app.playerNum != 0:
    #     app.curPlayer = app.playerNameList[app.curPlayerIndex]
    app.dice = 'Please roll the dice.'
    app.gridInfo = None
runApp(width=900, height=600)


# Please ignore the code below





# def keyPressed(app, event):
#     app.message = f"event.key == '{event.key}'"

# def redrawAll(app, canvas):
#     canvas.create_text(app.width/2, 40, text=app.message,
#                        font='Arial 30 bold', fill='black')
    
#     keyNamesText = '''Here are the legal event.key names:
#                       * Keyboard key labels (letters, digits, punctuation)
#                       * Arrow directions ('Up', 'Down', 'Left', 'Right')
#                       * Whitespace ('Space', 'Enter', 'Tab', 'BackSpace')
#                       * Other commands ('Delete', 'Escape')'''

#     y = 80
#     for line in keyNamesText.splitlines():
#         canvas.create_text(app.width/2, y, text=line.strip(),
#                            font='Arial 20', fill='black')
#         y += 30

