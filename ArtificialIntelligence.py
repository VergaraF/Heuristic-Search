from Models import *
import copy
from operator import itemgetter
import operator


class ArtificialIntelligence():

    PossibleMovements =  {

     1: Movement.UP,
     2: Movement.UP_RIGHT,
     3: Movement.RIGHT,
     4: Movement.DOWN_RIGHT,
     5: Movement.DOWN,
     6: Movement.DOWN_LEFT,
     7: Movement.LEFT,
     8: Movement.UP_LEFT
    }

    def __init__(self, goalState, gameBoard):
        self.goalState = copy.deepcopy(goalState)
        self.gameBoard = copy.deepcopy(gameBoard)
        self.rootNode = Node(self.gameBoard, 0)
        self.open = []
        self.closed = []
        self.solutionPath = []
        self.usingHeuristic = False


    def checkIfGoal(self, node):
        for index in range(len(node.gameBoard.Board)):
            if self.goalState[index] != node.gameBoard.Board[index]:
                return False

        return True

    def depthFirstSearch(self, maxDepth):
        self.usingHeuristic = False
        self.open = [self.rootNode]
        self.closed = []

        while self.open:
            nodeVisiting = self.open.pop()
            print nodeVisiting
            if self.checkIfGoal(nodeVisiting):
                return nodeVisiting

            if nodeVisiting.depth >= maxDepth:
                print "Depth too large, skip"
                continue

            children = self.generateChildren(nodeVisiting)

            while children:
                node = children.pop()
                nodeVisiting.children.append(node)
                self.open.append(node)

            self.closed.append(nodeVisiting)

        print "Open is empty - No solution found"

    def bestFirstSearch(self, depth, heuristicChoice):
        self.usingHeuristic = True
        self.closed = []

        self.usingHeuristic = True
        self.open = [(1, 1, self.rootNode)]
        self.closed = []
        self.solutionPath = []

        while self.open:
            visiting = self.open.pop(0)
            nodeVisiting = visiting[2]
            print nodeVisiting
            if self.checkIfGoal(nodeVisiting):
                return nodeVisiting

            self.closed.append(nodeVisiting)
            if nodeVisiting.depth >= depth:
                print "Too deep, skip"
                continue
            children = self.generateChildren(nodeVisiting)

            for child in children:
                if heuristicChoice == 1:
                    score = self.NumberOfTilesInWrongPosition(child.gameBoard.Board)
                    self.open.append((score, child.gameBoard.Moves[-1], child))
                elif heuristicChoice == 2:
                    score = self.PermutationInversion(child.gameBoard.Board)
                    self.open.append((score, child.gameBoard.Moves[-1], child))

            self.open = sorted(self.open, key=operator.itemgetter(0, 1))

        print "Nothing was found"


    def AStar(self, depth, heuristicChoice):
        self.usingHeuristic = True
        self.closed = []

        self.usingHeuristic = True
        self.open = [(1, 1, self.rootNode)]
        self.closed = []
        self.solutionPath = []

        while self.open:
            visiting = self.open.pop(0)
            nodeVisiting = visiting[2]

            print nodeVisiting

            if self.checkIfGoal(nodeVisiting):
                return nodeVisiting

            self.closed.append(nodeVisiting)

            if nodeVisiting.depth >= depth:
                print "skipping node"
                continue

            children = self.generateChildren(nodeVisiting)

            for child in children:
                if heuristicChoice == 1:
                    score = self.NumberOfTilesInWrongPosition(child.gameBoard.Board)
                    self.open.append((score + child.depth, child.gameBoard.Moves[-1], child))
                elif heuristicChoice == 2:
                    score = self.PermutationInversion(child.gameBoard.Board)
                    self.open.append((score + child.depth, child.gameBoard.Moves[-1], child))

            self.open = sorted(self.open, key=operator.itemgetter(0, 1))







    def generateChildren(self, parentNode):
        children = []

        for key, value in self.PossibleMovements.items():
            tempBoard = GameBoard(parentNode.gameBoard.Board)
            if tempBoard.move(value):
                newNode = Node(tempBoard, parentNode.depth + 1, action=tempBoard.CurrentPositionByLetter, parent=parentNode)
                if self.checkValidChild(newNode, parentNode):
                    children.append(newNode)


        return children

    def checkValidChild(self, childNode, parentNode):
        if self.checkIfNodesHaveSameBoard(childNode, parentNode):
            return False

        for nodeInOpenList in self.open:
            if self.usingHeuristic:
                node = nodeInOpenList[2]
            else:
                node = nodeInOpenList

            if self.checkIfNodesHaveSameBoard(node, childNode):
                return False

        for nodeInClosedList in self.closed:
            if self.checkIfNodesHaveSameBoard(nodeInClosedList, childNode):
                return False

        return True


    def checkIfNodesHaveSameBoard(self, node, otherNode):
        for index in range(len(node.gameBoard.Board)):
            if node.gameBoard.Board[index] != otherNode.gameBoard.Board[index]:
               return False

        return True

    def getSolution(self, node):
        if node.parent == None:
            self.solutionPath.append(node)
            return self.solutionPath

        self.solutionPath.append(node)
        self.getSolution(node.parent)
        return self.solutionPath

    def NumberOfTilesInWrongPosition(self, gameBoard):
        counter = 0
        for index in range(len(gameBoard)):
            if gameBoard[index] != self.goalState[index]:
                counter = counter + 1

        return counter

    def PermutationInversion(self, gameBoard):
        score = 0
        for x in range(len(gameBoard)-1):
            positionInGoalState = self.goalState.index(gameBoard[x])
            listOfNumbersInLeftSide = self.goalState[:positionInGoalState]
            for i in range(x +1, len(gameBoard)-1):
                if self.goalState[i] in listOfNumbersInLeftSide:
                    score = score + 1
        return score










