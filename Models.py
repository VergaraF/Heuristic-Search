## we will store all our model classes here so we can import them and use them lately in our controller
from enum import Enum

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
   # Root = Node()

    def __init__(self, numbers):
        ##TODO : Remove magic number
        print len(str(numbers).strip())
        if len(str(numbers).strip()) != 25:
           raise TypeError("Error trying to build the gameboard. You did not submit an invalid input")
        else:
            self.Board = [ x for x in numbers.split(" ") if str(x).isdigit()]
            self.findCurrentPosition()
            self.Root = Node(self.Board)

    def __str__(self):
        return str(self.Board)

    def findCurrentPosition(self):
        for x in range(len(self.Board)):
            if (self.Board[x] == 0):
                self.CurrentPosition = x
                self.CurrentPositionByLetter = self.BoardPosition[x]

##TODO : Refactor code (remove redundant code)
    def move(self, movement):
        if not isinstance(movement, Movement):
            raise TypeError("movement must be an instance of Movement enum (a valid movement)")
        else:
            if (movement is  Movement.RIGHT):
                try:
                    self.MoveRight()
                except:
                    print "Illegal move right"

            if (movement is Movement.LEFT):
                try:
                    self.MoveLeft()
                except:
                    print "Illegal move left"

            if (movement is Movement.DOWN):
                try:
                    self.MoveDown()
                except:
                    print "Illegal move down"

            if (movement is Movement.UP):
                try:
                    self.MoveUp()
                except:
                    print "Illegal move up"

            if (movement is Movement.DOWN_LEFT):
                try:
                    self.MoveLeft()
                    self.MoveDown()
                except:
                    print "Illegal move down left"

            if (movement is Movement.DOWN_RIGHT):
                try:
                   self.MoveRight()
                   self.MoveDown()
                except:
                    print "Illegal move down right"

            if (movement is Movement.UP_LEFT):
                try:
                    self.MoveLeft()
                    self.MoveUp()
                except:
                    print "Illegal move up left"

            if (movement is Movement.UP_RIGHT):
                try:
                    self.MoveRight()
                    self.MoveUp()
                except:
                    print "Illegal move up right"



    def MoveRight(self):
        print "Moving Right"
        previousPos = self.CurrentPosition
        tempCurrentPos = self.CurrentPosition + 1
        tempPreviousValue = self.Board[previousPos]
        tempCurrentValue = self.Board[tempCurrentPos]

        if (tempCurrentPos > len(self.Board)):
            raise TypeError("Illegal movement")
        elif (tempCurrentPos % 4 == 0):
            raise TypeError("Illegal movement")
        else:
            self.CurrentPosition = tempCurrentPos
            self.CurrentPositionByLetter = self.BoardPosition[self.CurrentPosition]
            self.Board[previousPos] = tempCurrentValue
            self.Board[tempCurrentPos] = tempPreviousValue
            print self.BoardPosition[self.CurrentPosition]

    def MoveLeft(self):
        print "Moving Left"
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
            self.CurrentPosition = tempCurrentPos
            self.CurrentPositionByLetter = self.BoardPosition[self.CurrentPosition]
            self.Board[previousPos] = tempCurrentValue
            self.Board[tempCurrentPos] = tempPreviousValue
            print self.BoardPosition[self.CurrentPosition]

    def MoveDown(self):
        print "Moving Down"
        previousPos = self.CurrentPosition
        tempCurrentPos = self.CurrentPosition + 4
        tempPreviousValue = self.Board[previousPos]
        tempCurrentValue = self.Board[tempCurrentPos]
        if (tempCurrentPos > len(self.Board)):
            raise TypeError("Illegal movement")
        else:
            self.CurrentPosition = tempCurrentPos
            self.CurrentPositionByLetter = self.BoardPosition[self.CurrentPosition]
            self.Board[previousPos] = tempCurrentValue
            self.Board[tempCurrentPos] = tempPreviousValue
            print self.BoardPosition[self.CurrentPosition]

    def MoveUp(self):
        print "Moving Up"
        previousPos = self.CurrentPosition
        tempCurrentPos = self.CurrentPosition - 4
        tempPreviousValue = self.Board[previousPos]
        tempCurrentValue = self.Board[tempCurrentPos]
        if (tempCurrentPos < 0):
            raise TypeError("Illegal movement")
        ##TODO: May give problems in the future, check
        else:
            self.CurrentPosition = tempCurrentPos
            self.CurrentPositionByLetter = self.BoardPosition[self.CurrentPosition]
            self.Board[previousPos] = tempCurrentValue
            self.Board[tempCurrentPos] = tempPreviousValue
            print self.BoardPosition[self.CurrentPosition]

class Node(object):

    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)

