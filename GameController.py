from Models import *

input = raw_input('Enter your input:')
MyBoard = GameBoard(input)

print MyBoard

MyBoard.move(Movement.RIGHT)
print MyBoard

MyBoard.move(Movement.DOWN)
print MyBoard

MyBoard.move(Movement.DOWN_RIGHT)
print MyBoard

MyBoard.move(Movement.UP)
print MyBoard

MyBoard.move(Movement.UP_RIGHT)
print MyBoard

MyBoard.move(Movement.LEFT)
print MyBoard

MyBoard.move(Movement.DOWN_LEFT)
print MyBoard

MyBoard.move(Movement.UP_LEFT)
print MyBoard

##must fail here

MyBoard.move(Movement.UP_LEFT)
print MyBoard