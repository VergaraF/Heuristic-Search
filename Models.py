## we will store all our model classes here so we can import them and use them lately in our controller
from enum import Enum
import copy

class Movement(Enum):
    UP = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGHT = 4
    DOWN = 5
    DOWN_LEFT =6
    LEFT = 7
    UP_LEFT = 8


class GameBoard():
    Board = []
    BoardPosition = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    CurrentPosition = 0
    CurrentPositionByLetter = "-"
    Moves = [0]

    def __init__(self, state):
        self.Board = copy.deepcopy(state)
        self.findCurrentPosition()

    def __str__(self):
        return str(self.Board)

    def findCurrentPosition(self):
        for x in range(len(self.Board)):
            if (self.Board[x] == '0'):
                self.CurrentPosition = x
                self.CurrentPositionByLetter = self.BoardPosition[x]

##TODO : Refactor code (remove redundant code)
    def move(self, movement):
        if not isinstance(movement, Movement):
            raise TypeError("movement must be an instance of Movement enum (a valid movement)")
        else:
            if (movement is  Movement.RIGHT):
                try:
                    self.moveRight()

                except:
                   #print "Illegal move right"
                    return False

            if (movement is Movement.LEFT):
                try:
                    self.moveLeft()
                except:
                    #print "Illegal move left"
                    return False

            if (movement is Movement.DOWN):
                try:
                    self.moveDown()
                except:
                    #print "Illegal move down"
                    return False

            if (movement is Movement.UP):
                try:
                    self.moveUp()
                except:
                    #print "Illegal move up"
                    return False

            if (movement is Movement.DOWN_LEFT):
                try:
                    self.moveLeft()
                    self.moveDown()
                except:
                    #print "Illegal move down left"
                    return False

            if (movement is Movement.DOWN_RIGHT):
                try:
                   self.moveRight()
                   self.moveDown()
                except:
                   # print "Illegal move down right"
                    return False

            if (movement is Movement.UP_LEFT):
                try:
                    self.moveLeft()
                    self.moveUp()
                except:
                   # print "Illegal move up left"
                    return False

            if (movement is Movement.UP_RIGHT):
                try:
                    self.moveRight()
                    self.moveUp()
                except:
                    #print "Illegal move up right"
                    return False

            self.findCurrentPosition()
            self.Moves.append(movement.value)
            return True



    def moveRight(self):

        previousPos = self.CurrentPosition
        tempCurrentPos = self.CurrentPosition + 1
        tempPreviousValue = self.Board[previousPos]
        tempCurrentValue = self.Board[tempCurrentPos]

        if (tempCurrentPos > len(self.Board)):
            raise TypeError("Illegal movement")
        elif (tempCurrentPos % 4 == 0):
            raise TypeError("Illegal movement")
        else:
            self.swap(tempCurrentPos, tempCurrentValue, previousPos, tempPreviousValue)
            #print self.BoardPosition[self.CurrentPosition]

    def moveLeft(self):

        previousPos = self.CurrentPosition
        tempCurrentPos = self.CurrentPosition - 1
        tempPreviousValue = self.Board[previousPos]
        tempCurrentValue = self.Board[tempCurrentPos]

        if (tempCurrentPos < 0):
            raise TypeError("Illegal movement")
    ##TODO: May give problems in the future, check
        elif (self.CurrentPosition % 4 == 0):
            raise TypeError("Illegal movement")
        else:
            self.swap(tempCurrentPos, tempCurrentValue, previousPos, tempPreviousValue)
            #print self.BoardPosition[self.CurrentPosition]

    def moveDown(self):

        previousPos = self.CurrentPosition
        tempCurrentPos = self.CurrentPosition + 4
        tempPreviousValue = self.Board[previousPos]
        tempCurrentValue = self.Board[tempCurrentPos]
        if (tempCurrentPos > len(self.Board)):
            raise TypeError("Illegal movement")
        else:
            self.swap(tempCurrentPos, tempCurrentValue, previousPos, tempPreviousValue)
            #print self.BoardPosition[self.CurrentPosition]

    def moveUp(self):

        previousPos = self.CurrentPosition
        tempCurrentPos = self.CurrentPosition - 4
        tempPreviousValue = self.Board[previousPos]
        tempCurrentValue = self.Board[tempCurrentPos]
        if (tempCurrentPos < 0):
            raise TypeError("Illegal movement")
        ##TODO: May give problems in the future, check
        else:
            self.swap(tempCurrentPos, tempCurrentValue, previousPos, tempPreviousValue)
            #print self.BoardPosition[self.CurrentPosition]

    def swap(self, tempCurrentPos, tempCurrentValue, previousPos, tempPreviousValue):
        self.CurrentPosition = tempCurrentPos
        self.CurrentPositionByLetter = self.BoardPosition[self.CurrentPosition]
        self.Board[previousPos] = tempCurrentValue
        self.Board[tempCurrentPos] = tempPreviousValue


class Node(object):

    def __init__(self, gameBoard, depth, action=None, parent = None):
        self.gameBoard = gameBoard
        self.depth = depth
        self.parent = parent
        self.action = action
        self.children = []

    def __str__(self):
        if (self.action == None):
            return "0" + str(self.gameBoard.Board)

        return str(self.action) + str(self.gameBoard.Board)

    def addChild(self, obj):
        self.children.append(obj)

    __repr__ = __str__




