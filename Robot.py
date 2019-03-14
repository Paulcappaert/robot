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
			buttons = self.wiiRemote.getButtons()
			if (buttons):
				self.control = self.changeControl(buttons, False)
			if (self.control == 1):
				self.manual(buttons)
			elif (self.control == 2):
				self.autonomous(buttons)
			
			
				
	def changeControl(self, buttons, emergencyStop):
		if (buttons & cwiid.BTN_1):
			self.control = 1
		elif(buttons & cwiid.BTN_2):
			self.control = 2
		elif (emergencyStop):
			self.control = 1
	
	def manual(self, buttons):
		if(buttons & cwiid.BTN_LEFT):
			self.robotMovement.Left(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_MINUS):
			self.robotMovement.RotateLeft(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_PLUS):
			self.robotMovement.RotateRight(leftSpeed, rightSpeed)
		elif(buttons & cwiid.BTN_RIGHT):
			self.robotMovement.Right(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_UP):
			self.robotMovement.Forward(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_DOWN):
			self.robotMovement.Backward(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_B):
			self.Stop()
		if (buttons):
			time.sleep(button_delay)
			
	def autonomous(self, buttons):
		if (buttons & cwiid.BTN_B):
			self.Stop()
			self.changeControl(buttons, True)
		#Check ultrasonic sensors for immediate object
		
		#Process Image and compute path using ImageProcessing script
		#This should return a movement path
		
		#Execute movement path

robot = Robot()
	
	
	
