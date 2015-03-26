from operator import add
import math

moves = raw_input("Enter the moves: ")

start_position = [0,0]
current_position = [0,0]

'''
heading = [1,90] - 1 step North
		  [1, -90] - 1 step South
		  [1,0] - East
		  [1,360] - West
'''

heading = [1,0]

for move in moves:
	if move.upper() == "G":

		angle = heading[1]
		step = heading[0]
		move_coord = [ round(step*math.cos(math.radians(angle))), round(step*math.sin(math.radians(angle))) ]
		current_position = map(add, current_position, move_coord)
	
	elif move.upper() == "L":
		heading = map(add, heading, [0, 90])

	elif move.upper() == "R":
		heading = map(add, heading, [0, -90])


if start_position == current_position:
	print "Given sequence of moves is circular"
else:
	print "Given sequence of moves is NOT circular"