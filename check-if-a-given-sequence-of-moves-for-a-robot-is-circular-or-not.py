'''
URL: http://www.geeksforgeeks.org/check-if-a-given-sequence-of-moves-for-a-robot-is-circular-or-not/
====

Python 2.7 compatible

Problem statement:
====================

Given a sequence of moves for a robot, check if the sequence is circular or not. A sequence of moves is circular if first and last positions of robot are same. A move can be on of the following.

  G - Go one unit
  L - Turn left
  R - Turn right 

'''

from operator import add
import math

moves = raw_input("Enter the moves: ")

start_position = [0,0]
current_position = [0,0]

'''
heading = [1,90] - 1 step North
		  [1, -90] - 1 step South
		  [1,0] - East
		  [1,+-180] - West
'''

heading = [1,0]

for move in moves:
	if move.upper() == "G":

		angle = heading[1]
		step = heading[0]

		# move_coord holds the x and y coordinate movement for the robot
		move_coord = [ round(step*math.cos(math.radians(angle))), round(step*math.sin(math.radians(angle))) ]
		current_position = map(add, current_position, move_coord)
	
	elif move.upper() == "L":
		# turn the robot 90 degrees anti-clockwise
		heading = map(add, heading, [0, 90])

	elif move.upper() == "R":
		# turn the robot 90 degrees clockwise
		heading = map(add, heading, [0, -90])


if start_position == current_position:
	print "Given sequence of moves is circular"
else:
	print "Given sequence of moves is NOT circular"