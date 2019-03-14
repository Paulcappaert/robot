import ImageProcessing, RobotMovement, Sensors, WiiRemote

class Robot:

	imageProcessing = None
	robotMovement = None
	Sensors = None
	wiiRemote = None
	running = False
	control = -1 #1 - manaual #2 - autonomous
	button_delay = 0.1
	leftSpeed = 65
	rightSpeed = 65

	def __init__(self):
		self.imageProcessing = ImageProcessing.ImageProcessing()
		self.robotMovement = RobotMovement.RobotMovement()
		self.Sensors = Sensors.Sensors()
		self.wiiRemote = WiiRemote.WiiRemote()
		self.running = True
		self.mainloop()

	def mainloop(self):
		while self.running:

			#Consider moving to WiiRemote
			self.wiiRemote.handleButtons()
			if(self.wiiRemote.getControl() == 2)
				self.autonomous()

	
			
	def autonomous(self, buttons):
		if (buttons & cwiid.BTN_B):
			self.Stop()
			self.changeControl(buttons, True)
		#Check ultrasonic sensors for immediate object
		
		#Process Image and compute path using ImageProcessing script
		#This should return a movement path
		
		#Execute movement path

robot = Robot()
	
	
	
