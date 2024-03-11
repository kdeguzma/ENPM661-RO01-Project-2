# INSTRUCTIONS: Open a new terminal, and, in the same directory as this file, type "python3 dijkstra_kyle_deguzman.py".
# GitHub link: https://github.com/kdeguzma/ENPM661-RO01-Project-2
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
		return "[" + str(self.xnode) + ", " + str(self.ynode) + "]" #+ "Cost: " + str(self.cost) + " "
	def __repr__(self):
		return "[" + str(self.xnode) + ", " + str(self.ynode) + "]" #+ "Cost: " + str(self.cost) + " "
		
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

def obstacles(nodex, nodey): 
	xcoord = nodex
	ycoord = nodey
	if xcoord >= 90 and xcoord <= 175 and ycoord >= 90:  # Obstacle, First rectangle
		return True
	if xcoord >= 265 and xcoord <= 350 and ycoord <= 400: # Obstacle, Second rectangle
		return True
	if xcoord >= (645 - 77.5*math.sqrt(3)) and xcoord <= 645:  # Obstacle, Hexagon # Left to middle
		if ycoord <= (xcoord/math.sqrt(3)) - (645/math.sqrt(3)) + 400: # Upper left hexagon line
			return True
		if ycoord >= (-xcoord/math.sqrt(3)) + (645/math.sqrt(3)) + 90: # Lower left hexagon line
			return True
	if xcoord >= (645 - 77.5*math.sqrt(3)) and xcoord <= (645 + 77.5*math.sqrt(3)) and ycoord >= 167.5 and ycoord <= 322.5: # Middle rectangle in hexagon 
			return True
	if xcoord >= 645 and xcoord <= (645 + 77.5*math.sqrt(3)): # Middle to right
		if ycoord <= (-xcoord/math.sqrt(3)) + (645/math.sqrt(3)) + 400: # Upper right hexagon line
			return True
		if ycoord >= (xcoord/math.sqrt(3)) - (645/math.sqrt(3)) + 90: # Lower right hexagon line
			return True
	if xcoord >= 890 and xcoord <= 1100 and ycoord >= 365 and ycoord <= 450: # Obstacle, C shape (3 rectangles) # Top rectangle
		return True
	if xcoord >= 1010 and xcoord <= 1100 and ycoord >= 125 and ycoord <= 365: # Middle rectangle
		return True
	if xcoord >= 890 and xcoord <= 1100 and ycoord >= 40 and ycoord <= 125: # Bottom rectangle
		return True
	return False # fails every obstacle check, therefore is not an obstacle
			
def solver(width, height, sx, sy, gx, gy):
	initial_node = node(0, 0, sx, sy, 0)
	goal_node = node(0, 0, gx, gy, 0) # Dummy values of 0 and 0 for node.parent_index and node.node_index
	is_obstacle = obstacles(goalx, goaly) 
	if is_obstacle == True:
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
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
			if addRight:
				next_node = Right(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
			if addDown:
				next_node = Down(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
			if addUp:
				next_node = Up(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
			if addUp and addRight:	
				next_node = UpRight(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
			if addDown and addLeft:
				next_node = DownLeft(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
			if addUp and addLeft:
				next_node = UpLeft(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
			if addDown and addRight:	
				next_node = DownRight(current_point)
				is_in_list = any((next_node.xnode==i.xnode and next_node.ynode==i.ynode) for i in allnodes)
				is_obstacle = obstacles(next_node.xnode, next_node.ynode)
				if not is_in_list and not is_obstacle:
					allnodes.append(next_node)
					progress.append(next_node)
		progress.pop(0)
		current_node = progress[0]
		count += 1
	print("\n")
	return allnodes

def dijkstra(sx, sy, gx, gy, nodelist):
	connected = []
	truepath = []
	costlist = []
	previous_node = node(0, 0, gx, gy, 0)
	truepath = [previous_node]
	while not (previous_node.xnode == sx and previous_node.ynode == sy):
		for this_node in allnodes:
			if this_node.xnode == (previous_node.xnode - 1) and this_node.ynode == previous_node.ynode: # back left 
				connected.append(this_node)
			if this_node.xnode == (previous_node.xnode + 1) and this_node.ynode == previous_node.ynode: # back right
				connected.append(this_node)
			if this_node.xnode == previous_node.xnode and this_node.ynode == (previous_node.ynode + 1): # back up
				connected.append(this_node)
			if this_node.xnode == previous_node.xnode and this_node.ynode == (previous_node.ynode - 1):# back down
				connected.append(this_node)
			if this_node.xnode == (previous_node.xnode - 1) and this_node.ynode == (previous_node.ynode + 1):# back upleft
				connected.append(this_node)
			if this_node.xnode == (previous_node.xnode + 1) and this_node.ynode == (previous_node.ynode + 1):# back upright
				connected.append(this_node)
			if this_node.xnode == (previous_node.xnode - 1) and this_node.ynode == (previous_node.ynode - 1):# back downleft
				connected.append(this_node)
			if this_node.xnode == (previous_node.xnode + 1) and this_node.ynode == (previous_node.ynode - 1):# back downright
				connected.append(this_node)
		for item in connected:
			costlist.append(item.cost)	
		bestnode = [i for i in connected if (min(costlist)==i.cost)]
		truepath.append(bestnode[0])
		previous_node = bestnode[0]
	return truepath
	

# MAIN CODE
startx = int(input("Type x-coordinate starting point (mm): "))
starty = int(input("Type y-coordinate starting point (mm): "))


goalx = int(input("Type x-coordinate goal point (mm): "))
goaly = int(input("Type y-coordinate goal point (mm): "))


width = 1200-5 # -5 to account for 5 mm clearance of robot
height = 500-5

# ANIMATION/VISUALIZATION CODE
fig, ax = plt.subplots()
allnodes = solver(width, height, startx, starty, goalx, goaly)
realpath = dijkstra(startx, starty, goalx, goaly, allnodes)
print("Best Path:", realpath)
xcoord = []
ycoord = []
costlist = []

for this_node in allnodes:
	xcoord.append(this_node.xnode)
	ycoord.append(this_node.ynode)
	costlist.append(this_node.cost)
#print("Cost for each node:", costlist)
scat = ax.scatter(xcoord, ycoord, c = 'k')
plt.plot(xcoord, ycoord, c = 'k', linestyle = 'solid')
plt.axis([0, 1200-5, 0, 500-5])
obsrec1 = plt.Rectangle((90, 90), 85, 400, fc='blue', ec ='black')
obsrec2 = plt.Rectangle((265, 0), 85, 400, fc='blue', ec ='black')
obshexagon = np.array([[645-77.5*math.sqrt(3), 167.5],[645, 90],[645+77.5*math.sqrt(3), 167.5],[645+77.5*math.sqrt(3), 322.5],[645, 400],[645-77.5*math.sqrt(3), 322.5]])
h = Polygon(obshexagon, fc = 'blue', ec = 'black')
obscshape = np.array([[890, 40],[1100, 40],[1100, 450],[890, 450],[890, 365],[1010, 365],[1010, 125],[890, 125]])
c = Polygon(obscshape, fc = 'blue', ec = 'black')
plt.gca().add_patch(h) # plot hexagon
plt.gca().add_patch(c) # plot c shape (3 rectangles)
plt.gca().add_patch(obsrec1) # plot first rectangle
plt.gca().add_patch(obsrec2) # plot second rectangle
plt.xlabel("X Coordinate (mm)")
plt.ylabel("Y Coordinate (mm)")
fig.suptitle('Path and Obstacles (5 mm clearance included)')

def virtualize(i):
	scat.set_offsets((xcoord[i], ycoord[i]))
	return scat,

ani = animation.FuncAnimation(fig, virtualize, frames=len(xcoord), interval=100)
writer = animation.PillowWriter(fps = 10, metadata = dict(artist = 'Me'), bitrate = 1800)
ani.save('test.gif', writer = writer)
plt.show()








