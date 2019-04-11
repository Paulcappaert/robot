import cv2, time
import numpy as np
import time

def getObstacleMap(img, depthImage):
	#gets the image and creates a hopefuly not noisy edge detection
	#small = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
	blur = cv2.GaussianBlur(img, (15, 15), 0)
	grayimage = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(grayimage, 50, 100)
	
	cv2.imshow('edges',edges)
	cv2.waitKey(1)	
	
	depthBlur = cv2.GaussianBlur(depthImage, (5, 5), 0)
	depthGrayimage = cv2.cvtColor(depthBlur,cv2.COLOR_BGR2GRAY)
	depthEdges = cv2.Canny(depthGrayimage, 50, 100)
	
	cv2.imshow('depthEdges',depthEdges)
	cv2.waitKey(1)
	
	#set up to divide the edge map into a grid with kernals of size 25
	edges = edges[int(len(edges)/2):len(edges),0:len(edges[0])]
	kernalSize = 25
	grid = []
	rows,cols = edges.shape
	height = int(rows/kernalSize)
	width = int(cols/kernalSize)
	
	depthEdges = depthEdges[int(len(depthEdges)/2):len(depthEdges),0:len(depthEdges[0])]
	
	#creates the obstacle map from edge map
	for i in range(height):
		row = []
		for j in range(width):
			cornerx = i*kernalSize;
			cornery = j*kernalSize;
			count1 = 0
			count2 = 0
			for x in range(kernalSize):
				for y in range(kernalSize):
					count1 = count1 + edges[x + cornerx][y + cornery]
					count2 = count2 + depthEdges[x + cornerx][y + cornery]

			if count1 > 3 and count2 > 3:
				row.append(1)
			else:
				row.append(0)

		grid.append(row)
		
	for i in range(height):
		for j in range(width):
			print(grid[i][j],end=" ")
		print()	
	print()
		
	return getPath(grid)
		
	
def getPath(grid):
	height = len(grid)
	width = len(grid[0])
	nodes = width * height
	graph = [] #1 if x is connection to y
	path = [] #contains the sequence of steps to get from the start point to the end
	
	if grid[height - 1][int(width/2)] == 1:
		return path
	
	#fills the graph with all 0
	for i in range(nodes):
		row = []
		for j in range(nodes):
			row.append(0)
		graph.append(row)
		
	#connects the correct nodes in the graph
	node_index = 0
	for i in range(height):
		for j in range(width):
			if graph[i][j] == 0:
				if i > 0 and grid[i - 1][j] == 0:
					graph[node_index][node_index - width] = 1
				if i < height - 1 and grid[i + 1][j] == 0:
					graph[node_index][node_index + width] = 1
				if j > 0 and grid[i][j - 1] == 0:
					graph[node_index][node_index - 1] = 1
				if j < width - 1 and grid[i][j + 1] == 0:
					graph[node_index][node_index + 1] = 1
			node_index += 1
	
	visited = []
	for i in range(nodes):
		visited.append(0)
	start = width * (height - 1) + int(width/2)
	
	bfs(graph, nodes, start, visited)
	
	#determines which position will be the endpoint
	end = 0
	stepVal = width*height # the path has to be shorter than this or else it doesn't exist
	for i in range(width):
		if visited[i] < stepVal and visited[i] != 0:
			stepVal = visited[i]
			end = i
	
	if stepVal == width*height:
		return path
		
	#saves the last positon of the path first
	path.append([0,end])
	
	#gets the path from the BFS and stores the positon of each grid visited
	curr_node = end
	while stepVal > 1:
		for i in range(nodes):
			if graph[curr_node][i] == 1 and visited[i] == stepVal - 1:
				
				#translates the node number back to its position in the grid
				y = i % width
				x = int(i / width)
				
				curr_node = i
				stepVal -= 1
				path.append([x,y])
	
	return path
		
def bfs(graph, nodes, start, visited):
	queue = [start]
	visited[start] = 1
	
	while len(queue) > 0:
		curr = queue.pop(0)
		visitNum = visited[curr]
		for i in range(nodes):
			if graph[curr][i] == 1 and visited[i] == 0:
				queue.append(i)
				visited[i] = visitNum + 1

	
#cap = cv2.VideoCapture(0)

#_,img = cap.read()
'''
start = time.time()
img = cv2.imread('hall6.JPG',1)
edges,grid = getObstacleMap(img)
path = getPath(grid)

for x in path:
	grid[x[0]][x[1]] = 2

print("")
for i in range(len(grid)):
	for j in range(len(grid[0])):
		print(grid[i][j],end=" ")
	print("")

end = time.time()
print(end - start)	

#cv2.imshow('hall',img)
cv2.imshow('hall1',edges)
cv2.waitKey(0)
'''
