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