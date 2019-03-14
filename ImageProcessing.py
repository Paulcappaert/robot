import cv2
import pyzed.camera as zcam
import pyzed.types as tp
import pyzed.core as core
import pyzed.defines as sl
import numpy as np

class ImageProcessing:
	
	def __init__(self):
		
		cam = cv2.VideoCapture(1)
		cam.set(3,640)
		cam.set(4,480)
		cam.set(5,30)
		camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS
		str_camera_settings = "BRIGHTNESS"
		step_camera_settings = 1
		self.getPath = True
		init = zcam.PyInitParameters()
		init = zcam.PyInitParameters(depth_mode=sl.PyDEPTH_MODE.PyDEPTH_MODE_PERFORMANCE, coordinate_units=sl.PyUNIT.PyUNIT_METER,coordinate_system=sl.PyCOORDINATE_SYSTEM.PyCOORDINATE_SYSTEM_RIGHT_HANDED_Y_UP, sdk_verbose=True)
		cam2 = zcam.PyZEDCamera()
		if not cam2.is_opened():
			print("Opening ZED Camera...")
			status = cam2.open(init)
		if status != tp.PyERROR_CODE.PySUCCESS:
			print(repr(status))
			exit()
		
		runtime = zcam.PyRuntimeParameters()
		runtime.sensing_mode = sl.PySENSING_MODE.PySENSING_MODE_STANDARD  # Use STANDARD sensing mode
		mat = core.PyMat()
		depth = core.PyMat()
		point_cloud = core.PyMat()
		
	def getObstacleMap(self):
		#gets the image and creates a hopefuly not noisy edge detection
		_,img = cam.read()
		small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
		blur = cv2.GaussianBlur(small, (15, 15), 0)
		grayimage = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(grayimage, 50, 100)
		
		#todo - get the depth map
		
		#set up to divide the edge map into a grid with kernals of size 25
		edges = edges[int(len(edges)/2):len(edges),0:len(edges[0])]
		kernalSize = 25
		grid = []
		rows,cols = edges.shape
		height = int(rows/25)
		width = int(cols/25)
		
		#creates the obstacle map from edge map
		for i in range(height):
			row = []
			for j in range(width):
				cornerx = i*25;
				cornery = j*25;
				count = 0
				for x in range(25):
					for y in range(25):
						count = count + edges[x + cornerx][y + cornery]

				if count > 3:
					row.append(1)
				else:
					row.append(0)

			grid.append(row)
			
		#todo - update the obstacle map with information from the depth map
		return edges
		
	def getPath(self):
		grid = getObstacleMap(self)
		
		