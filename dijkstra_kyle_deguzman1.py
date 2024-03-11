# INSTRUCTIONS: Open a new terminal, and, in the same directory as this file, type "python3 proj2_kyle_deguzman.py".
import numpy as np
import math
import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Polygon

class node:
	def __init__(self, parent_index, node_index, x, y, cost):
		self.parent_index = parent_index
		self.node_index = node_index
		self.xnode = x
		self.ynode = y
		self.cost = cost
	def __str__(self):
		return "[" + str(self.xnode) + ", " + str(self.ynode) + "]" 
	def __repr__(self):
		return "[" + str(self.xnode) + ", " + str(self.ynode) + "]" 
		
def Left(point):
	next_node = copy.deepcopy(point)
	if next_node.xnode >= 0: # Ensure the movement does not go back to the origin
		next_node.xnode -= 1
		next_node.cost += 1
	return next_node
		
def Right(point):
	next_node = copy.deepcopy(point)
	if next_node.xnode >= 0:
		next_node.xnode += 1
		next_node.cost += 1
	return next_node
	
def Down(point):
	next_node = copy.deepcopy(point)
	if next_node.ynode >= 0:
		next_node.ynode -= 1
		next_node.cost += 1
	return next_node
		
def Up(point):
	next_node = copy.deepcopy(point)
	if next_node.ynode >= 0:
		next_node.ynode += 1
		next_node.cost += 1
	return next_node

def UpLeft(point):
	next_node = copy.deepcopy(point)
	if next_node.xnode >= 0 and next_node.ynode >= 0:
		next_node.xnode -= 1
		next_node.ynode += 1
		next_node.cost += 1.4
	return next_node
		
def UpRight(point):
	next_node = copy.deepcopy(point)
	if next_node.xnode >= 0 and next_node.ynode >= 0:
		next_node.xnode += 1
		next_node.ynode += 1
		next_node.cost += 1.4
	return next_node
		
def DownLeft(point):
	next_node = copy.deepcopy(point)
	if next_node.xnode >= 0 and next_node.ynode >= 0:
		next_node.xnode -= 1
		next_node.ynode -= 1
		next_node.cost += 1.4
	return next_node
		
def DownRight(point):
	next_node = copy.deepcopy(point)
	if next_node.xnode >= 0 and next_node.ynode >= 0:
		next_node.xnode += 1
		next_node.ynode -= 1
		next_node.cost += 1.4
	return next_node

'''def obstacles(width, height, sx, sy, gx, gy, allnodes): 
	allnodes = solver(width, height, sx, sy, gx, gy)
	obstacles = []
	for coord in allnodes: # loop to append obstacle coordinates
		xcoord = node.xnode
		ycoord = node.ynode
		if xcoord >= 90 and xcoord <= 175 and ycoord >= 90:  # Obstacle, First rectangle
			obstacles.append((xcoord, ycoord))
		if xcoord >= 265 and xcoord <= 350 and ycoord <= 400: # Obstacle, Second rectangle
			obstacles.append((xcoord, ycoord))
		if xcoord >= (645 - 77.5*math.sqrt(3)) and xcoord <= 645:  # Obstacle, Hexagon # Left to middle
			if ycoord <= (xcoord/math.sqrt(3)) - (645/math.sqrt(3)) + 400: # Upper left hexagon line
				obstacles.append((xcoord, ycoord))
			if ycoord >= (-xcoord/math.sqrt(3)) + (645/math.sqrt(3)) + 90: # Lower left hexagon line
				obstacles.append((xcoord, ycoord))
		if xcoord >= (645 - 77.5*math.sqrt(3)) and xcoord <= (645 + 77.5*math.sqrt(3)) and ycoord >= 167.5 and ycoord <= 322.5: # Middle rectangle in hexagon 
				obstacles.append((xcoord, ycoord))
		if xcoord >= 645 and xcoord <= (645 + 77.5*math.sqrt(3)): # Middle to right
			if ycoord <= (-xcoord/math.sqrt(3)) + (645/math.sqrt(3)) + 400: # Upper right hexagon line
				obstacles.append((xcoord, ycoord))
			if ycoord >= (xcoord/math.sqrt(3)) - (645/math.sqrt(3)) + 90: # Lower right hexagon line
				obstacles.append((xcoord, ycoord))
		if xcoord >= 890 and xcoord <= 1100 and ycoord >= 365 and ycoord <= 450: # Obstacle, C shape (3 rectangles) # Top rectangle
			obstacles.append((xcoord, ycoord))
		if xcoord >= 1010 and xcoord <= 1100 and ycoord >= 125 and ycoord <= 365: # Middle rectangle
			obstacles.append((xcoord, ycoord))
		if xcoord >= 890 and xcoord <= 1100 and ycoord >= 40 and ycoord <= 125: # Bottom rectangle
			obstacles.append((xcoord, ycoord))
	#return obstacles
	print("obstacles:", obstacles)'''	
			
def solver(width, height, sx, sy, gx, gy):
	initial_node = node(0, 0, sx, sy, 0)
	goal_node = node(0, 0, gx, gy, 0) # Dummy values of 0 and 0 for node.parent_index and node.node_index
	#obstacles = obstacles(width, height, node)
	#mapwhole(mapwidth, mapheight)
	if goalx and goaly in obstacles:
		print("Error: Chosen points are invalid. Goal is inside obstacle. Close the program and try again.") # Error message for points chosen inside obstacles
	if startx == goalx and starty == goaly:
		print("Error: Start and goal points cannot be the same. Close the program and try again.") # Error message if start and goal coordinates are identical'''
	progress = []
	allnodes = []
	progress.append(initial_node)
	allnodes.append(initial_node)
	count = 0
	nodeindex = 0
	count += 1
	current_node = progress[0]
	while not (current_node.xnode == gx and current_node.ynode == gy):
		current_point = copy.deepcopy(current_node)
		#node_network = nodemap(width, height, current_point, allnodes, progress, count)
		x = current_point.xnode
		y = current_point.ynode
		if x < width and y < height:
			addLeft = (x-1) >= 0
			addRight = (x+1) < width
			addUp = (y+1) < height
			addDown = (y-1) >= 0
			# corner cases, 3 possible child branches from parent
			if addLeft:
				next_node = Left(current_point)
				is_in_list = any((next_node.xnode==i.xnode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
			if addRight:
				next_node = Right(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
			if addDown:
				next_node = Down(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
			if addUp:
				next_node = Up(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
			if addUp and addRight:	
				next_node = UpRight(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
			if addDown and addLeft:
				next_node = DownLeft(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
			if addUp and addLeft:
				next_node = UpLeft(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
			if addDown and addRight:	
				next_node = DownRight(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				if is_in_list == False:
					allnodes.append(next_node)
					progress.append(next_node)
		progress.pop(0)
		current_node = progress[0]
		count += 1
	print("\n")
	return allnodes

# MAIN CODE
startx = 0 # int(input("Type x-coordinate starting point (mm): "))
starty = 0 # int(input("Type y-coordinate starting point (mm): "))


goalx = 0 # int(input("Type x-coordinate goal point (mm): "))
goaly = 1 # int(input("Type y-coordinate goal point (mm): "))


width = 1200-5 # -5 to account for 5 mm clearance of robot
height = 500-5

#obstacles(width, height, node)










