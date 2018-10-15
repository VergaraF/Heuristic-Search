from Models import *
from ArtificialIntelligence import *

input = raw_input('Enter your input:')

if len(str(input).strip()) != 25:
    raise TypeError("Error trying to build the gameboard. You did not submit an invalid input")
else:
    input = [x for x in input.split(" ") if str(x).isdigit()]
MyBoard = GameBoard(input)
goal = ['1', '2' , '3', '4' ,'5', '6', '7', '8' ,'9', '10', '11', '0']
AI = ArtificialIntelligence(goal, MyBoard)

'''solutionNodeDFS = AI.depthFirstSearch(50)
solutionPathDFS = AI.getSolution(solutionNodeDFS)
print (solutionPathDFS)
'''
#solutionNodeBFS1 = AI.bestFirstSearch(1)
solutionNodeBFS2 = AI.bestFirstSearch(2)


#solutionPathBFS1 = AI.getSolution(solutionNodeBFS1)
solutionPathBFS2 = AI.getSolution(solutionNodeBFS2)
#print (solutionPathBFS1)
print (solutionPathBFS2)
