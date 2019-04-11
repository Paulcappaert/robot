import pyzed.sl as sl
import numpy as np
import cv2, time
import ImageMap

class ImageProcessing:

	zed = None	
	
	def __init__(self):
		# Create a Camera object
		self.zed = sl.Camera()
		# Set configuration parameters
		init_params = sl.InitParameters()
		init_params.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_MEDIUM
		init_params.coordinate_units = sl.UNIT.UNIT_METER
		#init_params.depth_minimum_distance = 0.3

		# Open the camera
		err = self.zed.open(init_params)
		if err != sl.ERROR_CODE.SUCCESS:
			print("Error opening camera")
			print(err)
			exit(1)

		self.runtime_parameters =sl.RuntimeParameters()
		self.runtime_parameters.sensing_mode = sl.SENSING_MODE.SENSING_MODE_FILL
		
	def getObstacleMap(self):
		depth_map  = sl.Mat()
		rgb_left_image = sl.Mat()      	
		if self.zed.grab(self.runtime_parameters) ==  sl.ERROR_CODE.SUCCESS :
			self.zed.retrieve_image(depth_map, sl.VIEW.VIEW_DEPTH)
			self.zed.retrieve_image(rgb_left_image, sl.VIEW.VIEW_LEFT)
			resizedDepthImage = cv2.resize(depth_map.get_data(), (0,0), fx=0.5, fy=0.5)
			resizedLeftImage = cv2.resize(rgb_left_image.get_data(), (0,0), fx=0.5, fy=0.5)
			path = ImageMap.getObstacleMap(resizedLeftImage,resizedDepthImage)
			
			
			#for x in path:
			#	print(x[0],end=" ")
			#	print(x[1])
				
			cv2.imshow('img',resizedLeftImage)			
			cv2.waitKey(1)

			
ip = ImageProcessing()
while True:
	ip.getObstacleMap()